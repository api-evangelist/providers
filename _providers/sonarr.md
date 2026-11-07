---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 114
  human_in_the_loop: 3
  name: Sonarr Agentic Access
  operation_count: 242
  slug: sonarr-agentic-access
  summary_line: 242 operations · 114 acting · 3 human-in-the-loop
api_count: 2
apis:
- description: Sonarr API (v5) – programmatic interface for Sonarr v5.
  name: Sonarr API
  slug: sonarr-api
- baseURL_template: '{protocol}://{hostpath}'
  baseurl_source: spec_template
  description: The ApiInfo API from Sonarr — 1 operation(s) for apiinfo.
  name: Sonarr API Info API
  slug: sonarr-apiinfo-api
- baseURL_template: '{protocol}://{hostpath}'
  baseurl_source: spec_template
  description: The Authentication API from Sonarr — 5 operation(s) for authentication.
  name: Sonarr Authentication API
  slug: sonarr-authentication-api
- baseURL_template: '{protocol}://{hostpath}'
  baseurl_source: spec_template
  description: The AutoTagging API from Sonarr — 6 operation(s) for autotagging.
  name: Sonarr Auto Tagging API
  slug: sonarr-autotagging-api
- baseURL_template: '{protocol}://{hostpath}'
  baseurl_source: spec_template
  description: The Backup API from Sonarr — 8 operation(s) for backup.
  name: Sonarr Backup API
  slug: sonarr-backup-api
- baseURL_template: '{protocol}://{hostpath}'
  baseurl_source: spec_template
  description: The Blocklist API from Sonarr — 6 operation(s) for blocklist.
  name: Sonarr Blocklist API
  slug: sonarr-blocklist-api
- baseURL_template: '{protocol}://{hostpath}'
  baseurl_source: spec_template
  description: The Calendar API from Sonarr — 4 operation(s) for calendar.
  name: Sonarr Calendar API
  slug: sonarr-calendar-api
- baseURL_template: '{protocol}://{hostpath}'
  baseurl_source: spec_template
  description: The CalendarFeed API from Sonarr — 2 operation(s) for calendarfeed.
  name: Sonarr Calendar Feed API
  slug: sonarr-calendarfeed-api
- baseURL_template: '{protocol}://{hostpath}'
  baseurl_source: spec_template
  description: The Command API from Sonarr — 4 operation(s) for command.
  name: Sonarr Command API
  slug: sonarr-command-api
- baseURL_template: '{protocol}://{hostpath}'
  baseurl_source: spec_template
  description: The Connection API from Sonarr — 6 operation(s) for connection.
  name: Sonarr Connection API
  slug: sonarr-connection-api
- baseURL_template: '{protocol}://{hostpath}'
  baseurl_source: spec_template
  description: The CustomFilter API from Sonarr — 4 operation(s) for customfilter.
  name: Sonarr Custom Filter API
  slug: sonarr-customfilter-api
- baseURL_template: '{protocol}://{hostpath}'
  baseurl_source: spec_template
  description: The CustomFormat API from Sonarr — 8 operation(s) for customformat.
  name: Sonarr Custom Format API
  slug: sonarr-customformat-api
- baseURL_template: '{protocol}://{hostpath}'
  baseurl_source: spec_template
  description: The Cutoff API from Sonarr — 4 operation(s) for cutoff.
  name: Sonarr Cutoff API
  slug: sonarr-cutoff-api
- baseURL_template: '{protocol}://{hostpath}'
  baseurl_source: spec_template
  description: The DelayProfile API from Sonarr — 6 operation(s) for delayprofile.
  name: Sonarr Delay Profile API
  slug: sonarr-delayprofile-api
- baseURL_template: '{protocol}://{hostpath}'
  baseurl_source: spec_template
  description: The DiskSpace API from Sonarr — 2 operation(s) for diskspace.
  name: Sonarr Disk Space API
  slug: sonarr-diskspace-api
- baseURL_template: '{protocol}://{hostpath}'
  baseurl_source: spec_template
  description: The DownloadClient API from Sonarr — 14 operation(s) for downloadclient.
  name: Sonarr Download Client API
  slug: sonarr-downloadclient-api
- baseURL_template: '{protocol}://{hostpath}'
  baseurl_source: spec_template
  description: The DownloadClientConfig API from Sonarr — 2 operation(s) for downloadclientconfig.
  name: Sonarr Download Client Config API
  slug: sonarr-downloadclientconfig-api
- baseURL_template: '{protocol}://{hostpath}'
  baseurl_source: spec_template
  description: The DownloadClientSettings API from Sonarr — 2 operation(s) for downloadclientsettings.
  name: Sonarr Download Client Settings API
  slug: sonarr-downloadclientsettings-api
- baseURL_template: '{protocol}://{hostpath}'
  baseurl_source: spec_template
  description: The Episode API from Sonarr — 6 operation(s) for episode.
  name: Sonarr Episode API
  slug: sonarr-episode-api
- baseURL_template: '{protocol}://{hostpath}'
  baseurl_source: spec_template
  description: The EpisodeFile API from Sonarr — 7 operation(s) for episodefile.
  name: Sonarr Episode File API
  slug: sonarr-episodefile-api
- baseURL_template: '{protocol}://{hostpath}'
  baseurl_source: spec_template
  description: The FileSystem API from Sonarr — 6 operation(s) for filesystem.
  name: Sonarr File System API
  slug: sonarr-filesystem-api
- baseURL_template: '{protocol}://{hostpath}'
  baseurl_source: spec_template
  description: The GeneralSettings API from Sonarr — 2 operation(s) for generalsettings.
  name: Sonarr General Settings API
  slug: sonarr-generalsettings-api
- baseURL_template: '{protocol}://{hostpath}'
  baseurl_source: spec_template
  description: The Health API from Sonarr — 2 operation(s) for health.
  name: Sonarr Health API
  slug: sonarr-health-api
- baseURL_template: '{protocol}://{hostpath}'
  baseurl_source: spec_template
  description: The History API from Sonarr — 10 operation(s) for history.
  name: Sonarr History API
  slug: sonarr-history-api
- baseURL_template: '{protocol}://{hostpath}'
  baseurl_source: spec_template
  description: The HostConfig API from Sonarr — 2 operation(s) for hostconfig.
  name: Sonarr Host Config API
  slug: sonarr-hostconfig-api
- baseURL_template: '{protocol}://{hostpath}'
  baseurl_source: spec_template
  description: The ImportList API from Sonarr — 14 operation(s) for importlist.
  name: Sonarr Import List API
  slug: sonarr-importlist-api
- baseURL_template: '{protocol}://{hostpath}'
  baseurl_source: spec_template
  description: The ImportListConfig API from Sonarr — 2 operation(s) for importlistconfig.
  name: Sonarr Import List Config API
  slug: sonarr-importlistconfig-api
- baseURL_template: '{protocol}://{hostpath}'
  baseurl_source: spec_template
  description: The ImportListExclusion API from Sonarr — 7 operation(s) for importlistexclusion.
  name: Sonarr Import List Exclusion API
  slug: sonarr-importlistexclusion-api
- baseURL_template: '{protocol}://{hostpath}'
  baseurl_source: spec_template
  description: The ImportListSettings API from Sonarr — 2 operation(s) for importlistsettings.
  name: Sonarr Import List Settings API
  slug: sonarr-importlistsettings-api
- baseURL_template: '{protocol}://{hostpath}'
  baseurl_source: spec_template
  description: The Indexer API from Sonarr — 14 operation(s) for indexer.
  name: Sonarr Indexer API
  slug: sonarr-indexer-api
- baseURL_template: '{protocol}://{hostpath}'
  baseurl_source: spec_template
  description: The IndexerConfig API from Sonarr — 2 operation(s) for indexerconfig.
  name: Sonarr Indexer Config API
  slug: sonarr-indexerconfig-api
- baseURL_template: '{protocol}://{hostpath}'
  baseurl_source: spec_template
  description: The IndexerFlag API from Sonarr — 2 operation(s) for indexerflag.
  name: Sonarr Indexer Flag API
  slug: sonarr-indexerflag-api
- baseURL_template: '{protocol}://{hostpath}'
  baseurl_source: spec_template
  description: The IndexerSettings API from Sonarr — 2 operation(s) for indexersettings.
  name: Sonarr Indexer Settings API
  slug: sonarr-indexersettings-api
- baseURL_template: '{protocol}://{hostpath}'
  baseurl_source: spec_template
  description: The Language API from Sonarr — 4 operation(s) for language.
  name: Sonarr Language API
  slug: sonarr-language-api
- baseURL_template: '{protocol}://{hostpath}'
  baseurl_source: spec_template
  description: The LanguageProfile API from Sonarr — 2 operation(s) for languageprofile.
  name: Sonarr Language Profile API
  slug: sonarr-languageprofile-api
- baseURL_template: '{protocol}://{hostpath}'
  baseurl_source: spec_template
  description: The LanguageProfileSchema API from Sonarr — 1 operation(s) for languageprofileschema.
  name: Sonarr Language Profile Schema API
  slug: sonarr-languageprofileschema-api
- baseURL_template: '{protocol}://{hostpath}'
  baseurl_source: spec_template
  description: The Localization API from Sonarr — 6 operation(s) for localization.
  name: Sonarr Localization API
  slug: sonarr-localization-api
- baseURL_template: '{protocol}://{hostpath}'
  baseurl_source: spec_template
  description: The Log API from Sonarr — 2 operation(s) for log.
  name: Sonarr Log API
  slug: sonarr-log-api
- baseURL_template: '{protocol}://{hostpath}'
  baseurl_source: spec_template
  description: The LogFile API from Sonarr — 4 operation(s) for logfile.
  name: Sonarr Log File API
  slug: sonarr-logfile-api
- baseURL_template: '{protocol}://{hostpath}'
  baseurl_source: spec_template
  description: The ManualImport API from Sonarr — 2 operation(s) for manualimport.
  name: Sonarr Manual Import API
  slug: sonarr-manualimport-api
- baseURL_template: '{protocol}://{hostpath}'
  baseurl_source: spec_template
  description: The MediaCover API from Sonarr — 2 operation(s) for mediacover.
  name: Sonarr Media Cover API
  slug: sonarr-mediacover-api
- baseURL_template: '{protocol}://{hostpath}'
  baseurl_source: spec_template
  description: The MediaManagementConfig API from Sonarr — 2 operation(s) for mediamanagementconfig.
  name: Sonarr Media Management Config API
  slug: sonarr-mediamanagementconfig-api
- baseURL_template: '{protocol}://{hostpath}'
  baseurl_source: spec_template
  description: The MediaManagementSettings API from Sonarr — 2 operation(s) for mediamanagementsettings.
  name: Sonarr Media Management Settings API
  slug: sonarr-mediamanagementsettings-api
- baseURL_template: '{protocol}://{hostpath}'
  baseurl_source: spec_template
  description: The Metadata API from Sonarr — 12 operation(s) for metadata.
  name: Sonarr Metadata API
  slug: sonarr-metadata-api
- baseURL_template: '{protocol}://{hostpath}'
  baseurl_source: spec_template
  description: The MetadataSourceSettings API from Sonarr — 2 operation(s) for metadatasourcesettings.
  name: Sonarr Metadata Source Settings API
  slug: sonarr-metadatasourcesettings-api
- baseURL_template: '{protocol}://{hostpath}'
  baseurl_source: spec_template
  description: The Missing API from Sonarr — 4 operation(s) for missing.
  name: Sonarr Missing API
  slug: sonarr-missing-api
- baseURL_template: '{protocol}://{hostpath}'
  baseurl_source: spec_template
  description: The NamingConfig API from Sonarr — 3 operation(s) for namingconfig.
  name: Sonarr Naming Config API
  slug: sonarr-namingconfig-api
- baseURL_template: '{protocol}://{hostpath}'
  baseurl_source: spec_template
  description: The NamingSettings API from Sonarr — 3 operation(s) for namingsettings.
  name: Sonarr Naming Settings API
  slug: sonarr-namingsettings-api
- baseURL_template: '{protocol}://{hostpath}'
  baseurl_source: spec_template
  description: The Notification API from Sonarr — 6 operation(s) for notification.
  name: Sonarr Notification API
  slug: sonarr-notification-api
- baseURL_template: '{protocol}://{hostpath}'
  baseurl_source: spec_template
  description: The Parse API from Sonarr — 2 operation(s) for parse.
  name: Sonarr Parse API
  slug: sonarr-parse-api
- baseURL_template: '{protocol}://{hostpath}'
  baseurl_source: spec_template
  description: The Ping API from Sonarr — 1 operation(s) for ping.
  name: Sonarr Ping API
  slug: sonarr-ping-api
- baseURL_template: '{protocol}://{hostpath}'
  baseurl_source: spec_template
  description: The QualityDefinition API from Sonarr — 6 operation(s) for qualitydefinition.
  name: Sonarr Quality Definition API
  slug: sonarr-qualitydefinition-api
- baseURL_template: '{protocol}://{hostpath}'
  baseurl_source: spec_template
  description: The QualityProfile API from Sonarr — 4 operation(s) for qualityprofile.
  name: Sonarr Quality Profile API
  slug: sonarr-qualityprofile-api
- baseURL_template: '{protocol}://{hostpath}'
  baseurl_source: spec_template
  description: The QualityProfileSchema API from Sonarr — 2 operation(s) for qualityprofileschema.
  name: Sonarr Quality Profile Schema API
  slug: sonarr-qualityprofileschema-api
- baseURL_template: '{protocol}://{hostpath}'
  baseurl_source: spec_template
  description: The Queue API from Sonarr — 6 operation(s) for queue.
  name: Sonarr Queue API
  slug: sonarr-queue-api
- baseURL_template: '{protocol}://{hostpath}'
  baseurl_source: spec_template
  description: The QueueAction API from Sonarr — 4 operation(s) for queueaction.
  name: Sonarr Queue Action API
  slug: sonarr-queueaction-api
- baseURL_template: '{protocol}://{hostpath}'
  baseurl_source: spec_template
  description: The QueueDetails API from Sonarr — 2 operation(s) for queuedetails.
  name: Sonarr Queue Details API
  slug: sonarr-queuedetails-api
- baseURL_template: '{protocol}://{hostpath}'
  baseurl_source: spec_template
  description: The QueueStatus API from Sonarr — 2 operation(s) for queuestatus.
  name: Sonarr Queue Status API
  slug: sonarr-queuestatus-api
- baseURL_template: '{protocol}://{hostpath}'
  baseurl_source: spec_template
  description: The Release API from Sonarr — 2 operation(s) for release.
  name: Sonarr Release API
  slug: sonarr-release-api
- baseURL_template: '{protocol}://{hostpath}'
  baseurl_source: spec_template
  description: The ReleaseProfile API from Sonarr — 4 operation(s) for releaseprofile.
  name: Sonarr Release Profile API
  slug: sonarr-releaseprofile-api
- baseURL_template: '{protocol}://{hostpath}'
  baseurl_source: spec_template
  description: The ReleasePush API from Sonarr — 3 operation(s) for releasepush.
  name: Sonarr Release Push API
  slug: sonarr-releasepush-api
- baseURL_template: '{protocol}://{hostpath}'
  baseurl_source: spec_template
  description: The RemotePathMapping API from Sonarr — 4 operation(s) for remotepathmapping.
  name: Sonarr Remote Path Mapping API
  slug: sonarr-remotepathmapping-api
- baseURL_template: '{protocol}://{hostpath}'
  baseurl_source: spec_template
  description: The RenameEpisode API from Sonarr — 4 operation(s) for renameepisode.
  name: Sonarr Rename Episode API
  slug: sonarr-renameepisode-api
- baseURL_template: '{protocol}://{hostpath}'
  baseurl_source: spec_template
  description: The RootFolder API from Sonarr — 4 operation(s) for rootfolder.
  name: Sonarr Root Folder API
  slug: sonarr-rootfolder-api
- baseURL_template: '{protocol}://{hostpath}'
  baseurl_source: spec_template
  description: The SeasonPass API from Sonarr — 2 operation(s) for seasonpass.
  name: Sonarr Season Pass API
  slug: sonarr-seasonpass-api
- baseURL_template: '{protocol}://{hostpath}'
  baseurl_source: spec_template
  description: The Series API from Sonarr — 5 operation(s) for series.
  name: Sonarr Series API
  slug: sonarr-series-api
- baseURL_template: '{protocol}://{hostpath}'
  baseurl_source: spec_template
  description: The SeriesEditor API from Sonarr — 2 operation(s) for serieseditor.
  name: Sonarr Series Editor API
  slug: sonarr-serieseditor-api
- baseURL_template: '{protocol}://{hostpath}'
  baseurl_source: spec_template
  description: The SeriesFolder API from Sonarr — 2 operation(s) for seriesfolder.
  name: Sonarr Series Folder API
  slug: sonarr-seriesfolder-api
- baseURL_template: '{protocol}://{hostpath}'
  baseurl_source: spec_template
  description: The SeriesImport API from Sonarr — 2 operation(s) for seriesimport.
  name: Sonarr Series Import API
  slug: sonarr-seriesimport-api
- baseURL_template: '{protocol}://{hostpath}'
  baseurl_source: spec_template
  description: The SeriesLookup API from Sonarr — 2 operation(s) for serieslookup.
  name: Sonarr Series Lookup API
  slug: sonarr-serieslookup-api
- baseURL_template: '{protocol}://{hostpath}'
  baseurl_source: spec_template
  description: The StaticResource API from Sonarr — 5 operation(s) for staticresource.
  name: Sonarr Static Resource API
  slug: sonarr-staticresource-api
- baseURL_template: '{protocol}://{hostpath}'
  baseurl_source: spec_template
  description: The Statistics API from Sonarr — 1 operation(s) for statistics.
  name: Sonarr Statistics API
  slug: sonarr-statistics-api
- baseURL_template: '{protocol}://{hostpath}'
  baseurl_source: spec_template
  description: The System API from Sonarr — 10 operation(s) for system.
  name: Sonarr System API
  slug: sonarr-system-api
- baseURL_template: '{protocol}://{hostpath}'
  baseurl_source: spec_template
  description: The Tag API from Sonarr — 4 operation(s) for tag.
  name: Sonarr Tag API
  slug: sonarr-tag-api
- baseURL_template: '{protocol}://{hostpath}'
  baseurl_source: spec_template
  description: The TagDetails API from Sonarr — 4 operation(s) for tagdetails.
  name: Sonarr Tag Details API
  slug: sonarr-tagdetails-api
- baseURL_template: '{protocol}://{hostpath}'
  baseurl_source: spec_template
  description: The Task API from Sonarr — 4 operation(s) for task.
  name: Sonarr Task API
  slug: sonarr-task-api
- baseURL_template: '{protocol}://{hostpath}'
  baseurl_source: spec_template
  description: The UiConfig API from Sonarr — 2 operation(s) for uiconfig.
  name: Sonarr UI Config API
  slug: sonarr-uiconfig-api
- baseURL_template: '{protocol}://{hostpath}'
  baseurl_source: spec_template
  description: The UiSettings API from Sonarr — 2 operation(s) for uisettings.
  name: Sonarr UI Settings API
  slug: sonarr-uisettings-api
- baseURL_template: '{protocol}://{hostpath}'
  baseurl_source: spec_template
  description: The Update API from Sonarr — 2 operation(s) for update.
  name: Sonarr Update API
  slug: sonarr-update-api
- baseURL_template: '{protocol}://{hostpath}'
  baseurl_source: spec_template
  description: The UpdateLogFile API from Sonarr — 4 operation(s) for updatelogfile.
  name: Sonarr Update Log File API
  slug: sonarr-updatelogfile-api
- baseURL_template: '{protocol}://{hostpath}'
  baseurl_source: spec_template
  description: The UpdateSettings API from Sonarr — 2 operation(s) for updatesettings.
  name: Sonarr Update Settings API
  slug: sonarr-updatesettings-api
artifact_total: 94
common:
- group: design
  href: https://artifacts.apis.io/sonarr/rules/sonarr-rules.yml
  title: ''
  type: Spectral
  url: rules/sonarr-rules.yml
- group: design
  href: https://artifacts.apis.io/sonarr/json-ld/sonarr-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/sonarr-context.jsonld
- group: design
  href: https://artifacts.apis.io/sonarr/vocabulary/sonarr-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/sonarr-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/sonarr/conformance/sonarr-conformance.yml
  title: ''
  type: Conformance
  url: conformance/sonarr-conformance.yml
- group: design
  href: https://artifacts.apis.io/sonarr/data-model/sonarr-data-model.yml
  title: ''
  type: DataModel
  url: data-model/sonarr-data-model.yml
- group: auth
  href: https://artifacts.apis.io/sonarr/authentication/sonarr-authentication.yml
  title: ''
  type: Authentication
  url: authentication/sonarr-authentication.yml
- group: design
  href: https://artifacts.apis.io/sonarr/lifecycle/sonarr-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/sonarr-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/sonarr/errors/sonarr-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/sonarr-problem-types.yml
- group: other
  href: https://artifacts.apis.io/sonarr/hosts/sonarr-hosts.yml
  title: ''
  type: Hosts
  url: hosts/sonarr-hosts.yml
- group: other
  href: https://artifacts.apis.io/sonarr/vendors/sonarr-vendors.yml
  title: ''
  type: Vendors
  url: vendors/sonarr-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.sonarr.tv/
- group: auth
  href: https://artifacts.apis.io/sonarr/security/sonarr-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sonarr-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sonarr.tv/
- group: docs
  title: ''
  type: APIReference
  url: https://sonarr.tv/docs/api
- group: start
  title: ''
  type: GettingStarted
  url: https://sonarr.tv/docs/api/#v5/description/introduction
- group: operate
  title: ''
  type: Support
  url: https://forums.sonarr.tv
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Sonarr
- group: operate
  title: ''
  type: Roadmap
  url: https://github.com/Sonarr/Sonarr/milestones
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/postman-atlas/workspace/sonarr
created: '2026-10-28'
description: Sonarr is an open-source PVR (Personal Video Recorder) application that automates the download, organization, and management of TV series. It integrates with Usenet and torrent indexers, monitors RSS feeds for new episodes, and automatically retrieves them via configured download clients. Sonarr provides a web-based UI, extensive quality and naming profiles, and supports multiple platforms through Docker, Windows, macOS, and Linux installations. The project is community-driven, with frequent updates, a rich plugin ecosystem, and detailed API documentation for developers to build integrations and automation tools.
image: https://sonarr.tv/img/logo.png
json_schemas:
- name: ConnectionResource
  property_count: 39
  slug: sonarr-connection-resource
- name: GeneralSettingsResource
  property_count: 45
  slug: sonarr-general-settings-resource
- name: QueueResource
  property_count: 29
  slug: sonarr-queue-resource
- name: SeriesResource
  property_count: 55
  slug: sonarr-series-resource
- name: StatisticsResource
  property_count: 23
  slug: sonarr-statistics-resource
- name: SystemResource
  property_count: 31
  slug: sonarr-system-resource
jsonld:
- class_count: 120
  name: Sonarr Context
  property_count: 371
  slug: sonarr-context
layout: provider
modified: '2026-10-28'
name: Sonarr
nav: Providers
network: true
overview: 'Sonarr publishes 81 API contracts indexed on the [APIs.io](https://apis.io/) network, including API Info API, Authentication API, Auto Tagging API, and 78 more. Tagged areas include Company, PVR, TV, Usenet, and Torrent.


  The Sonarr catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Sonarr''s developer surface includes authentication, API reference, getting-started guide, support, and 15 more developer resources.'
random_paper: 13
rate_limits:
- limit_count: 0
  name: Sonarr Rate Limits
  slug: sonarr-rate-limits
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Sonarr API Rules
  rule_count: 10
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 2
  slug: sonarr-rules
scopes:
- name: Sonarr Scopes
  scope_count: 0
  slug: sonarr-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 28.5
  coverage:
    artifact_dirs: 25
    catalog_earned: 48.8
    catalog_earned_first_party: 0.0
    catalog_gap: 66.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 2.3
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 48.9
    developer_ergonomics: 26.2
    discoverability: 57.1
    operational_transparency: 13.2
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 26.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 80
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/sonarr/sonarr-2026-11-03T143518.png
security:
- kind: authentication
  name: Sonarr Authentication
  slug: sonarr-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Sonarr Domain Security
  slug: sonarr-domain-security
  summary_line: TLSv1.3
slug: sonarr
tags:
- Company
- PVR
- TV
- Usenet
- Torrent
- Automation
website: https://sonarr.tv/
---
