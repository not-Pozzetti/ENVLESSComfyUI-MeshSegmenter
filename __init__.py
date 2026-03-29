import logging
from .nodes import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS

log = logging.getLogger("meshsegmenter")
log.info("loading...")

from comfy_dynamic_widgets import write_mappings
write_mappings(NODE_CLASS_MAPPINGS, __file__)

WEB_DIRECTORY = "./web"
__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS', 'WEB_DIRECTORY']
