from krita import Krita, DockWidgetFactory, DockWidgetFactoryBase
from .ai_assistant import DockerTemplate

DOCKER_ID = "ai_assistant"

instance = Krita.instance()

dock_widget_factory = DockWidgetFactory(
    DOCKER_ID,
    DockWidgetFactoryBase.DockRight,
    DockerTemplate
)

instance.addDockWidgetFactory(dock_widget_factory)