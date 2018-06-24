__all__ = ["plugin"]

from . import plugin
import config_manager as config
Plugin = plugin.Plugin


def LoadPlugins():
    """Load plugins from config data"""
    p = config.get("plugins")
    print(p)
    return {}