# flake8: noqa

if __import__("typing").TYPE_CHECKING:
    # import apis into api package
    from prowlarr.api.api_info_api import ApiInfoApi
    from prowlarr.api.app_profile_api import AppProfileApi
    from prowlarr.api.application_api import ApplicationApi
    from prowlarr.api.authentication_api import AuthenticationApi
    from prowlarr.api.backup_api import BackupApi
    from prowlarr.api.command_api import CommandApi
    from prowlarr.api.custom_filter_api import CustomFilterApi
    from prowlarr.api.development_config_api import DevelopmentConfigApi
    from prowlarr.api.download_client_api import DownloadClientApi
    from prowlarr.api.download_client_config_api import DownloadClientConfigApi
    from prowlarr.api.file_system_api import FileSystemApi
    from prowlarr.api.health_api import HealthApi
    from prowlarr.api.history_api import HistoryApi
    from prowlarr.api.host_config_api import HostConfigApi
    from prowlarr.api.indexer_api import IndexerApi
    from prowlarr.api.indexer_default_categories_api import IndexerDefaultCategoriesApi
    from prowlarr.api.indexer_proxy_api import IndexerProxyApi
    from prowlarr.api.indexer_stats_api import IndexerStatsApi
    from prowlarr.api.indexer_status_api import IndexerStatusApi
    from prowlarr.api.localization_api import LocalizationApi
    from prowlarr.api.log_api import LogApi
    from prowlarr.api.log_file_api import LogFileApi
    from prowlarr.api.newznab_api import NewznabApi
    from prowlarr.api.notification_api import NotificationApi
    from prowlarr.api.ping_api import PingApi
    from prowlarr.api.search_api import SearchApi
    from prowlarr.api.static_resource_api import StaticResourceApi
    from prowlarr.api.system_api import SystemApi
    from prowlarr.api.tag_api import TagApi
    from prowlarr.api.tag_details_api import TagDetailsApi
    from prowlarr.api.task_api import TaskApi
    from prowlarr.api.ui_config_api import UiConfigApi
    from prowlarr.api.update_api import UpdateApi
    from prowlarr.api.update_log_file_api import UpdateLogFileApi
    
else:
    from lazy_imports import LazyModule, as_package, load

    load(
        LazyModule(
            *as_package(__file__),
            """# import apis into api package
from prowlarr.api.api_info_api import ApiInfoApi
from prowlarr.api.app_profile_api import AppProfileApi
from prowlarr.api.application_api import ApplicationApi
from prowlarr.api.authentication_api import AuthenticationApi
from prowlarr.api.backup_api import BackupApi
from prowlarr.api.command_api import CommandApi
from prowlarr.api.custom_filter_api import CustomFilterApi
from prowlarr.api.development_config_api import DevelopmentConfigApi
from prowlarr.api.download_client_api import DownloadClientApi
from prowlarr.api.download_client_config_api import DownloadClientConfigApi
from prowlarr.api.file_system_api import FileSystemApi
from prowlarr.api.health_api import HealthApi
from prowlarr.api.history_api import HistoryApi
from prowlarr.api.host_config_api import HostConfigApi
from prowlarr.api.indexer_api import IndexerApi
from prowlarr.api.indexer_default_categories_api import IndexerDefaultCategoriesApi
from prowlarr.api.indexer_proxy_api import IndexerProxyApi
from prowlarr.api.indexer_stats_api import IndexerStatsApi
from prowlarr.api.indexer_status_api import IndexerStatusApi
from prowlarr.api.localization_api import LocalizationApi
from prowlarr.api.log_api import LogApi
from prowlarr.api.log_file_api import LogFileApi
from prowlarr.api.newznab_api import NewznabApi
from prowlarr.api.notification_api import NotificationApi
from prowlarr.api.ping_api import PingApi
from prowlarr.api.search_api import SearchApi
from prowlarr.api.static_resource_api import StaticResourceApi
from prowlarr.api.system_api import SystemApi
from prowlarr.api.tag_api import TagApi
from prowlarr.api.tag_details_api import TagDetailsApi
from prowlarr.api.task_api import TaskApi
from prowlarr.api.ui_config_api import UiConfigApi
from prowlarr.api.update_api import UpdateApi
from prowlarr.api.update_log_file_api import UpdateLogFileApi

""",
            name=__name__,
            doc=__doc__,
        )
    )
