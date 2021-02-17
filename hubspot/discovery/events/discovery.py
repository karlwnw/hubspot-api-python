import hubspot.events as api_client
from ..discovery_base import DiscoveryBase


class Discovery(DiscoveryBase):
    @property
    def events_api(self) -> api_client.EventsApi:
        return self._configure_api_client(api_client, "EventsApi")
