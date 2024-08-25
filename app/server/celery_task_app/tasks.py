import importlib
import logging
from celery import Task
import asyncio

from .worker import app


class PredictTask(Task):
    """
    Abstraction of Celery's Task class to support loading ML model.
    """

    abstract = True

    def __init__(self) -> None:
        super().__init__()
        self.model = None

    async def water(self, file, user_id):
        """
        Load model on first call (i.e. first task processed)
        Avoids the need to load model on each task request
        """
        import os
        if self.model is None:
            logging.info("Loading Model")
            module_import = importlib.import_module(self.path[0])
            model_obj = getattr(module_import, self.path[1])
            self.model = model_obj()
            logging.info("Model Loaded")

        return await self.model.predict(file)


@app.task(
    ignore_results=False,
    bind=True,
    base=PredictTask,
    path=("celery_task_app.ml.model", "ChurnModel"),
    name="server.celery_task_app.tasks.predict_churn_signals"
)
def predict_churn_signals(self, file, user_id):
    loop = asyncio.get_event_loop()
    pred = loop.run_until_complete(self.water(file, user_id))
    import os
    import sys
    import inspect

    currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    parentdir = os.path.dirname(currentdir)
    sys.path.insert(0, parentdir) 

    from handlers.user_handler import update_user
    val = loop.run_until_complete(
            update_user(
                user_id,
                {
                    "interest": pred
                }
            )
        )
    print(val)
