"""Config flow for Palazzetti New."""
from .palazzetti_sdk_local_api import PalDiscovery, Palazzetti

from homeassistant import config_entries
from homeassistant.helpers import config_entry_flow

from .const import DOMAIN


async def _async_has_devices(hass) -> bool:
    """Return if there are devices that can be discovered."""
    # TODO Check if there are any devices that can be discovered in the network.
    # devices = await hass.async_add_executor_job(PalDiscovery.discovery_UDP(hass))
    # devices = await PalDiscovery.discovery_UDP(PalDiscovery)
    devices = ["192.168.1.133", "192.168.1.130"]
    hass.data[DOMAIN] = devices
    return len(devices) > 0


# punto di partenza del tutto: questo apre la finestra che chiede conferma
# di avviare il discovery. Quando finisce passa a __init__.py -> async_setup_entry
config_entry_flow.register_discovery_flow(
    DOMAIN, "Palazzetti New", _async_has_devices, config_entries.CONN_CLASS_LOCAL_POLL
)
