
import logging
from hydromt.models.model_api import Model
from typing import Optional, Dict, Any

logger = logging.getLogger(__name__)

class {{cookiecutter.model_name}}(Model):

    # Any global class variables your model should have go here
    _NAME: str = "{{cookiecutter.model_name}}"
    _GEOMS: Dict[str, Any] = {}
    _MAPS: Dict[str,Any] = {}
    _DATADIR = ""
    _CONF = "model.yaml"


    def __init__(
        self,
        root: Optional[str] = None,
        mode: str = 'w',
        config_fn: Optional[str] = None,
        data_libs: Optional[List[str],str] = None,
        logger: Logger = logger
    ):
        super().__init__(
            root=root,
            mode=mode,
            config_fn=config_fn,
            data_libs=data_libs,
            logger=logger
        )
        # If your model needs any extra setup add it after this point



