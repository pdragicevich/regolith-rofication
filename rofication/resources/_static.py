from .._metadata import ROFICATION_VERSION
from .._util import Resource

__version__ = ROFICATION_VERSION

value_font = Resource(env_name='font', xres_name='i3xrocks.value.font', default='Source Code Pro Medium 13')

notify_none = Resource(env_name='i3xrocks_label_notify_none', xres_name='i3xrocks.label.notify.none', default='N')
notify_some = Resource(env_name='i3xrocks_label_notify_some', xres_name='i3xrocks.label.notify.some', default='N')
notify_error = Resource(env_name='i3xrocks_label_notify_error', xres_name='i3xrocks.label.notify.error', default='N')

value_color = Resource(env_name='color', xres_name='i3xrocks.value.color', default='#E6E1CF')
label_color = Resource(env_name='label_color', xres_name='i3xrocks.label.color', default='#E6E1CF')
nominal_color = Resource(env_name='background_color', xres_name='i3xrocks.nominal', default='#E6E1CF')
warning_color = Resource(env_name='warn_color', xres_name='i3xrocks.warning', default='#FFD580')
critical_color = Resource(xres_name='i3xrocks.critical.color', default='#BF616A')

apps_blocked = Resource(env_name='i3xrocks_rofication_apps_blocked', xres_name='i3xrocks.rofication.apps.blocked', default='')
apps_can_expire = Resource(env_name='i3xrocks_rofication_apps_can_expire', xres_name='i3xrocks.rofication.apps.can_expire', default='notify-send')
apps_single = Resource(env_name='i3xrocks_rofication_apps_single', xres_name='i3xrocks.rofication.apps.single', default='VLC media player')
