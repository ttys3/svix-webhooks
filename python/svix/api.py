import typing as t
from dataclasses import asdict, dataclass
from datetime import datetime

from .internal.openapi_client.api.application import list_applications_api_v1_app_get
from .internal.openapi_client.client import AuthenticatedClient
from .internal.openapi_client.models.application_in import ApplicationIn
from .internal.openapi_client.models.application_out import ApplicationOut
from .internal.openapi_client.models.dashboard_access_out import DashboardAccessOut
from .internal.openapi_client.models.endpoint_headers_in import EndpointHeadersIn
from .internal.openapi_client.models.endpoint_headers_out import EndpointHeadersOut
from .internal.openapi_client.models.endpoint_in import EndpointIn
from .internal.openapi_client.models.endpoint_out import EndpointOut
from .internal.openapi_client.models.endpoint_secret_out import EndpointSecretOut
from .internal.openapi_client.models.endpoint_secret_rotate_in import EndpointSecretRotateIn
from .internal.openapi_client.models.event_type_in import EventTypeIn
from .internal.openapi_client.models.event_type_out import EventTypeOut
from .internal.openapi_client.models.event_type_update import EventTypeUpdate
from .internal.openapi_client.models.list_response_application_out import ListResponseApplicationOut
from .internal.openapi_client.models.list_response_endpoint_message_out import ListResponseEndpointMessageOut
from .internal.openapi_client.models.list_response_endpoint_out import ListResponseEndpointOut
from .internal.openapi_client.models.list_response_event_type_out import ListResponseEventTypeOut
from .internal.openapi_client.models.list_response_message_attempt_endpoint_out import (
    ListResponseMessageAttemptEndpointOut,
)
from .internal.openapi_client.models.list_response_message_attempt_out import ListResponseMessageAttemptOut
from .internal.openapi_client.models.list_response_message_endpoint_out import ListResponseMessageEndpointOut
from .internal.openapi_client.models.list_response_message_out import ListResponseMessageOut
from .internal.openapi_client.models.message_attempt_out import MessageAttemptOut
from .internal.openapi_client.models.message_in import MessageIn
from .internal.openapi_client.models.message_out import MessageOut
from .internal.openapi_client.models.message_status import MessageStatus
from .internal.openapi_client.models.recover_in import RecoverIn

DEFAULT_SERVER_URL = "https://api.svix.com"


@dataclass
class SvixOptions:
    debug: bool = False
    server_url: t.Optional[str] = None


@dataclass
class ListOptions:
    iterator: t.Optional[str] = None
    limit: t.Optional[int] = None

    def to_dict(self) -> t.Dict[str, t.Any]:
        return {k: v for k, v in asdict(self).items() if v is not None}


@dataclass
class PostOptions:
    idempotency_key: t.Optional[str] = None

    def to_dict(self) -> t.Dict[str, t.Any]:
        return {k: v for k, v in asdict(self).items() if v is not None}


@dataclass
class MessageListOptions(ListOptions):
    event_types: t.Optional[t.List[str]] = None
    before: t.Optional[datetime] = None
    channel: t.Optional[str] = None


@dataclass
class ApplicationListOptions(ListOptions):
    pass


@dataclass
class EventTypeListOptions(ListOptions):
    with_content: t.Optional[bool] = None
    include_archived: t.Optional[bool] = None


@dataclass
class EndpointListOptions(ListOptions):
    pass


@dataclass
class IntegrationListOptions(ListOptions):
    pass


@dataclass
class MessageAttemptListOptions(ListOptions):
    status: t.Optional[MessageStatus] = None
    event_types: t.Optional[t.List[str]] = None
    before: t.Optional[datetime] = None
    channel: t.Optional[str] = None


# ApiClass = t.TypeVar(
#     "ApiClass",
#     bound=t.Union[
#         AuthenticationApi, ApplicationApi, EndpointApi, EventTypeApi, IntegrationApi, MessageApi, MessageAttemptApi
#     ],
# )


class ApiBase:
    _client: AuthenticatedClient

    def __init__(self, client: AuthenticatedClient) -> None:
        self._client = client


# class Authentication(ApiBase[AuthenticationApi]):
#     _ApiClass = AuthenticationApi

#     def dashboard_access(self, app_id: str, options: PostOptions = PostOptions()) -> DashboardAccessOut:
#         with self._api() as api:
#             return api.get_dashboard_access_api_v1_auth_dashboard_access_app_id_post(
#                 app_id=app_id, **options.to_dict(), _check_return_type=False
#             )

#     def logout(self, options: PostOptions = PostOptions()) -> None:
#         with self._api() as api:
#             return api.logout_api_v1_auth_logout_post(**options.to_dict(), _check_return_type=False)
class ApplicationAsync(ApiBase):
    async def list(self, options: ApplicationListOptions = ApplicationListOptions()) -> ListResponseApplicationOut:
        return await list_applications_api_v1_app_get.asyncio(client=self._client, **options.to_dict())


class Application(ApiBase):
    def list(self, options: ApplicationListOptions = ApplicationListOptions()) -> ListResponseApplicationOut:
        return list_applications_api_v1_app_get.sync(client=self._client, **options.to_dict())

    # def create(self, application_in: ApplicationIn, options: PostOptions = PostOptions()) -> ApplicationOut:
    #     with self._api() as api:
    #         return api.create_application_api_v1_app_post(
    #             application_in=application_in, **options.to_dict(), _check_return_type=False
    #         )

    # def get(self, app_id: str) -> ApplicationOut:
    #     with self._api() as api:
    #         return api.get_application_api_v1_app_app_id_get(app_id=app_id, _check_return_type=False)

    # def get_or_create(self, application_in: ApplicationIn, options: PostOptions = PostOptions()) -> ApplicationOut:
    #     with self._api() as api:
    #         return api.create_application_api_v1_app_post(
    #             application_in=application_in, get_if_exists=True, **options.to_dict(), _check_return_type=False
    #         )

    # def update(self, app_id: str, application_in: ApplicationIn) -> ApplicationOut:
    #     with self._api() as api:
    #         return api.update_application_api_v1_app_app_id_put(
    #             app_id=app_id, application_in=application_in, _check_return_type=False
    #         )

    # def delete(self, app_id: str) -> None:
    #     with self._api() as api:
    #         return api.delete_application_api_v1_app_app_id_delete(app_id=app_id, _check_return_type=False)


# class Endpoint(ApiBase[EndpointApi]):
#     _ApiClass = EndpointApi

#     def list(self, app_id: str, options: EndpointListOptions = EndpointListOptions()) -> ListResponseEndpointOut:
#         with self._api() as api:
#             return api.list_endpoints_api_v1_app_app_id_endpoint_get(
#                 app_id=app_id, **options.to_dict(), _check_return_type=False
#             )

#     def create(self, app_id: str, endpoint_in: EndpointIn, options: PostOptions = PostOptions()) -> EndpointOut:
#         with self._api() as api:
#             return api.create_endpoint_api_v1_app_app_id_endpoint_post(
#                 app_id, endpoint_in=endpoint_in, **options.to_dict(), _check_return_type=False
#             )

#     def get(self, app_id: str, endpoint_id: str) -> EndpointOut:
#         with self._api() as api:
#             return api.get_endpoint_api_v1_app_app_id_endpoint_endpoint_id_get(
#                 app_id=app_id, endpoint_id=endpoint_id, _check_return_type=False
#             )

#     def update(self, app_id: str, endpoint_id: str, endpoint_update: EndpointUpdate) -> EndpointOut:
#         with self._api() as api:
#             return api.update_endpoint_api_v1_app_app_id_endpoint_endpoint_id_put(
#                 app_id=app_id, endpoint_id=endpoint_id, endpoint_update=endpoint_update, _check_return_type=False
#             )

#     def delete(self, app_id: str, endpoint_id: str) -> None:
#         with self._api() as api:
#             return api.delete_endpoint_api_v1_app_app_id_endpoint_endpoint_id_delete(
#                 app_id=app_id, endpoint_id=endpoint_id, _check_return_type=False
#             )

#     def get_secret(self, app_id: str, endpoint_id: str) -> EndpointSecretOut:
#         with self._api() as api:
#             return api.get_endpoint_secret_api_v1_app_app_id_endpoint_endpoint_id_secret_get(
#                 app_id=app_id, endpoint_id=endpoint_id, _check_return_type=False
#             )

#     def rotate_secret(
#         self,
#         app_id: str,
#         endpoint_id: str,
#         endpoint_secret_rotate_in: EndpointSecretRotateIn,
#         options: PostOptions = PostOptions(),
#     ) -> None:
#         with self._api() as api:
#             return api.rotate_endpoint_secret_api_v1_app_app_id_endpoint_endpoint_id_secret_rotate_post(
#                 app_id=app_id,
#                 endpoint_id=endpoint_id,
#                 endpoint_secret_rotate_in=endpoint_secret_rotate_in,
#                 **options.to_dict(),
#                 _check_return_type=False,
#             )

#     def recover(
#         self, app_id: str, endpoint_id: str, recover_in: RecoverIn, options: PostOptions = PostOptions()
#     ) -> None:
#         with self._api() as api:
#             api.recover_failed_webhooks_api_v1_app_app_id_endpoint_endpoint_id_recover_post(
#                 app_id=app_id,
#                 endpoint_id=endpoint_id,
#                 recover_in=recover_in,
#                 **options.to_dict(),
#                 _check_return_type=False,
#             )

#     def get_headers(self, app_id: str, endpoint_id: str) -> EndpointHeadersOut:
#         with self._api() as api:
#             return api.get_endpoint_headers_api_v1_app_app_id_endpoint_endpoint_id_headers_get(
#                 app_id=app_id,
#                 endpoint_id=endpoint_id,
#                 _check_return_type=False,
#             )

#     def update_headers(self, app_id: str, endpoint_id: str, endpoint_headers_in: EndpointHeadersIn) -> None:
#         with self._api() as api:
#             api.update_endpoint_headers_api_v1_app_app_id_endpoint_endpoint_id_headers_put(
#                 app_id=app_id,
#                 endpoint_id=endpoint_id,
#                 endpoint_headers_in=endpoint_headers_in,
#                 _check_return_type=False,
#             )

#     def patch_headers(self, app_id: str, endpoint_id: str, endpoint_headers_in: EndpointHeadersIn) -> None:
#         with self._api() as api:
#             api.patch_endpoint_headers_api_v1_app_app_id_endpoint_endpoint_id_headers_patch(
#                 app_id=app_id,
#                 endpoint_id=endpoint_id,
#                 endpoint_headers_in=endpoint_headers_in,
#                 _check_return_type=False,
#             )


# class EventType(ApiBase[EventTypeApi]):
#     _ApiClass = EventTypeApi

#     def list(self, options: EventTypeListOptions = EventTypeListOptions()) -> ListResponseEventTypeOut:
#         with self._api() as api:
#             return api.list_event_types_api_v1_event_type_get(**options.to_dict(), _check_return_type=False)

#     def create(self, event_type_in: EventTypeIn, options: PostOptions = PostOptions()) -> EventTypeOut:
#         with self._api() as api:
#             return api.create_event_type_api_v1_event_type_post(
#                 event_type_in=event_type_in, **options.to_dict(), _check_return_type=False
#             )

#     def get(self, event_type_name: str) -> EventTypeOut:
#         with self._api() as api:
#             return api.get_event_type_api_v1_event_type_event_type_name_get(
#                 event_type_name=event_type_name, _check_return_type=False
#             )

#     def update(self, event_type_name: str, event_type_update: EventTypeUpdate) -> EventTypeOut:
#         with self._api() as api:
#             return api.update_event_type_api_v1_event_type_event_type_name_put(
#                 event_type_name=event_type_name, event_type_update=event_type_update, _check_return_type=False
#             )

#     def delete(self, event_type_name: str) -> None:
#         with self._api() as api:
#             return api.delete_event_type_api_v1_event_type_event_type_name_delete(
#                 event_type_name=event_type_name, _check_return_type=False
#             )


# class Integration(ApiBase[IntegrationApi]):
#     _ApiClass = IntegrationApi

#     def list(
#         self, app_id: str, options: IntegrationListOptions = IntegrationListOptions()
#     ) -> ListResponseIntegrationOut:
#         with self._api() as api:
#             return api.list_integrations_api_v1_app_app_id_integration_get(
#                 app_id=app_id, **options.to_dict(), _check_return_type=False
#             )

#     def create(self, app_id: str, integ_in: IntegrationIn, options: PostOptions = PostOptions()) -> IntegrationOut:
#         with self._api() as api:
#             return api.create_integration_api_v1_app_app_id_integration_post(
#                 app_id, integration_in=integ_in, **options.to_dict(), _check_return_type=False
#             )

#     def get(self, app_id: str, integ_id: str) -> IntegrationOut:
#         with self._api() as api:
#             return api.get_integration_api_v1_app_app_id_integration_integ_id_get(
#                 app_id=app_id, integ_id=integ_id, _check_return_type=False
#             )

#     def update(self, app_id: str, integ_id: str, integ_update: IntegrationUpdate) -> IntegrationOut:
#         with self._api() as api:
#             return api.update_integration_api_v1_app_app_id_integration_integ_id_put(
#                 app_id=app_id, integ_id=integ_id, integration_update=integ_update, _check_return_type=False
#             )

#     def delete(self, app_id: str, integ_id: str) -> None:
#         with self._api() as api:
#             return api.delete_integration_api_v1_app_app_id_integration_integ_id_delete(
#                 app_id=app_id, integ_id=integ_id, _check_return_type=False
#             )

#     def get_key(self, app_id: str, integ_id: str) -> IntegrationKeyOut:
#         with self._api() as api:
#             return api.get_integration_key_api_v1_app_app_id_integration_integ_id_key_get(
#                 app_id=app_id, integ_id=integ_id, _check_return_type=False
#             )

#     def rotate_key(self, app_id: str, integ_id: str, options: PostOptions = PostOptions()) -> IntegrationKeyOut:
#         with self._api() as api:
#             return api.rotate_integration_key_api_v1_app_app_id_integration_integ_id_key_rotate_post(
#                 app_id=app_id, integ_id=integ_id, **options.to_dict(), _check_return_type=False
#             )


# class Message(ApiBase[MessageApi]):
#     _ApiClass = MessageApi

#     def list(self, app_id: str, options: MessageListOptions = MessageListOptions()) -> ListResponseMessageOut:
#         with self._api() as api:
#             return api.list_messages_api_v1_app_app_id_msg_get(
#                 app_id=app_id, **options.to_dict(), _check_return_type=False
#             )

#     def create(self, app_id: str, message_in: MessageIn, options: PostOptions = PostOptions()) -> MessageOut:
#         with self._api() as api:
#             return api.create_message_api_v1_app_app_id_msg_post(
#                 app_id=app_id, message_in=message_in, **options.to_dict(), _check_return_type=False
#             )

#     def get(self, app_id: str, msg_id: str) -> MessageOut:
#         with self._api() as api:
#             return api.get_message_api_v1_app_app_id_msg_msg_id_get(
#                 app_id=app_id, msg_id=msg_id, _check_return_type=False
#             )


# class MessageAttempt(ApiBase[MessageAttemptApi]):
#     _ApiClass = MessageAttemptApi

#     def list(
#         self, app_id: str, msg_id: str, options: MessageAttemptListOptions = MessageAttemptListOptions()
#     ) -> ListResponseMessageAttemptOut:
#         with self._api() as api:
#             return api.list_attempts_api_v1_app_app_id_msg_msg_id_attempt_get(
#                 app_id=app_id, msg_id=msg_id, **options.to_dict(), _check_return_type=False
#             )

#     def get(self, app_id: str, msg_id: str, attempt_id: str) -> MessageAttemptOut:
#         with self._api() as api:
#             return api.get_attempt_api_v1_app_app_id_msg_msg_id_attempt_attempt_id_get(
#                 app_id=app_id, msg_id=msg_id, attempt_id=attempt_id, _check_return_type=False
#             )

#     def resend(self, app_id: str, msg_id: str, endpoint_id: str, options: PostOptions = PostOptions()) -> None:
#         with self._api() as api:
#             return api.resend_webhook_api_v1_app_app_id_msg_msg_id_endpoint_endpoint_id_resend_post(
#                 app_id=app_id, msg_id=msg_id, endpoint_id=endpoint_id, **options.to_dict(), _check_return_type=False
#             )

#     def list_attempted_messages(
#         self, app_id: str, endpoint_id: str, options: MessageAttemptListOptions = MessageAttemptListOptions()
#     ) -> ListResponseEndpointMessageOut:
#         with self._api() as api:
#             return api.list_attempted_messages_api_v1_app_app_id_endpoint_endpoint_id_msg_get(
#                 app_id=app_id, endpoint_id=endpoint_id, **options.to_dict(), _check_return_type=False
#             )

#     def list_attempted_destinations(
#         self, app_id: str, msg_id: str, options: MessageAttemptListOptions = MessageAttemptListOptions()
#     ) -> ListResponseMessageEndpointOut:
#         with self._api() as api:
#             return api.list_attempted_destinations_api_v1_app_app_id_msg_msg_id_endpoint_get(
#                 app_id=app_id, msg_id=msg_id, **options.to_dict(), _check_return_type=False
#             )

#     def list_attempts_for_endpoint(
#         self,
#         app_id: str,
#         msg_id: str,
#         endpoint_id: str,
#         options: MessageAttemptListOptions = MessageAttemptListOptions(),
#     ) -> ListResponseMessageAttemptEndpointOut:
#         with self._api() as api:
#             return api.list_attempts_for_endpoint_api_v1_app_app_id_msg_msg_id_endpoint_endpoint_id_attempt_get(
#                 app_id=app_id, msg_id=msg_id, endpoint_id=endpoint_id, **options.to_dict(), _check_return_type=False
#             )
class ClientBase:
    _client: AuthenticatedClient

    def __init__(self, auth_token: str, options: SvixOptions = SvixOptions()) -> None:
        from . import __version__

        host = options.server_url or DEFAULT_SERVER_URL
        client = AuthenticatedClient(base_url=host, token=auth_token)
        self._client = client.with_headers(headers={"user_agent": f"svix-libs/{__version__}/python"})


class SvixAsync(ClientBase):
    @property
    def application(self) -> ApplicationAsync:
        return ApplicationAsync(self._client)


class Svix(ClientBase):

    # @property
    # def authentication(self) -> Authentication:
    #     return Authentication(self._client)

    @property
    def application(self) -> Application:
        return Application(self._client)

    # @property
    # def endpoint(self) -> Endpoint:
    #     return Endpoint(self._client)

    # @property
    # def event_type(self) -> EventType:
    #     return EventType(self._client)

    # @property
    # def integration(self) -> Integration:
    #     return Integration(self._client)

    # @property
    # def message(self) -> Message:
    #     return Message(self._client)

    # @property
    # def message_attempt(self) -> MessageAttempt:
    #     return MessageAttempt(self._client)


__all__ = [
    "ApplicationIn",
    "ApplicationOut",
    "ListResponseApplicationOut",
    "DashboardAccessOut",
    "EndpointHeadersIn",
    "EndpointHeadersOut",
    "EndpointIn",
    "EndpointOut",
    "EndpointSecretOut",
    "EndpointSecretRotateIn",
    "ListResponseEndpointOut",
    "EventTypeIn",
    "EventTypeOut",
    "EventTypeUpdate",
    "ListResponseEventTypeOut",
    "ListResponseMessageOut",
    "MessageIn",
    "MessageOut",
    "ListResponseMessageAttemptOut",
    "ListResponseEndpointMessageOut",
    "ListResponseMessageEndpointOut",
    "ListResponseMessageAttemptEndpointOut",
    "MessageAttemptOut",
    "MessageStatus",
    "SvixOptions",
    "ApplicationListOptions",
    "EventTypeListOptions",
    "EndpointListOptions",
    "MessageAttemptListOptions",
    "RecoverIn",
    "Svix",
]
