---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 55.0
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 221
  human_in_the_loop: 5
  name: Rapid7 Agentic Access
  operation_count: 459
  slug: rapid7-agentic-access
  summary_line: 459 operations · 221 acting · 5 human-in-the-loop
api_count: 50
apis:
- description: REST API for the InsightVM vulnerability management product, exposing assets, scans, vulnerabilities, remediation projects, and reports. Authentication uses an Insight Platform API key in the `X-Api-K
  name: Rapid7 InsightVM Cloud API
  slug: insightvm-api
- description: Cross-product REST API for the Insight Platform that covers user and key management, organizations, audit logs, and platform-level integrations. Authentication uses `X-Api-Key` against the regional en
  name: Rapid7 Insight Platform API
  slug: insight-platform-api
- description: REST API for the InsightIDR SIEM/XDR product covering investigations, alerts, log search, threats, and SOC workflows. Authentication uses `X-Api-Key` against the regional Insight Platform endpoint.
  name: Rapid7 InsightIDR API
  slug: insightidr-api
- description: An API used to find and search InsightIDR accounts. See https://docs.rapid7.com/insightidr/users-and-accounts-on-your-domain for further information on accounts.
  name: Rapid7 Accounts API
  slug: rapid7-accounts-api
- description: Provides access administrative operations and procedures.
  name: Rapid7 Administration API
  slug: rapid7-administration-api
- description: 'An App <i>owns</i> Scan Configs, Schedules, Scans and Vulnerabilities; you must create an App in order to create any of these other resources. Consequently, if an App is deleted it will delete all of '
  name: Rapid7 Apps API
  slug: rapid7-apps-api
- description: Resources and operations for managing assets. Assets can be created under the <a href="#operation/createAssetUsingPOST">Site Assets</a> resource.
  name: Rapid7 Asset API
  slug: rapid7-asset-api
- description: Resources for managing and viewing the mechanisms used to automatically discover assets.
  name: Rapid7 Asset Discovery API
  slug: rapid7-asset-discovery-api
- description: Resources and operations for managing asset groups.
  name: Rapid7 Asset Group API
  slug: rapid7-asset-group-api
- description: An API used to find and search InsightIDR assets. See https://docs.rapid7.com/insightidr/assets-on-your-domain for further information on assets.
  name: Rapid7 Assets API
  slug: rapid7-assets-api
- description: An API used to upload, list, download and delete attachments. For example, the create API can be used to upload an attachment.
  name: Rapid7 Attachments API
  slug: rapid7-attachments-api
- description: An Attack Template describes <i>if</i> and <i>how</i> Attacks should be executed during the execution of a Scan. There exist pre-defined, system-provided and immutable templates, as well as custom tem
  name: Rapid7 Attack Templates API
  slug: rapid7-attack-templates-api
- description: A blackout is a period of time when all scanning activities for the specified scope are blocked. A blackout can be scoped globally or to a specific App, this is implied by the <code>scope</code> prope
  name: Rapid7 Blackouts API
  slug: rapid7-blackouts-api
- description: An API used to manage collectors for an organization.
  name: Rapid7 Collectors API
  slug: rapid7-collectors-api
- description: An API used to find, create, and delete comments. For example, these APIs can be used to create a comment for a particular investigation.
  name: Rapid7 Comments API
  slug: rapid7-comments-api
- description: An API used to add and replace indicators for Community Threats. See https://insightidr.help.rapid7.com/docs/threats#section-threat-api for further information on how to generate threat keys.
  name: Rapid7 Community Threats API
  slug: rapid7-community-threats-api
- description: Resources and operations for managing shared credentials.
  name: Rapid7 Credential API
  slug: rapid7-credential-api
- description: An Engine Group is a resource which defines a container for a logical grouping of Engines and therefore the purpose of assigning Scans to one of those Engines. Any created Engine Group can contain 0 o
  name: Rapid7 Engine Groups API
  slug: rapid7-engine-groups-api
- description: An Engine encapsulates the state and high-level attributes of the components which may be installed and running on a specific On-Premise host. The status of an Engine is not mutable via the API; it re
  name: Rapid7 Engines API
  slug: rapid7-engines-api
- description: Files are used primarily to manage content that can be required to successfully scan an App. For example, many supported methods of configuring authentication in a Scan Config require a payload and si
  name: Rapid7 Files API
  slug: rapid7-files-api
- description: An API used to retrieve health metrics of an organization.
  name: Rapid7 Health Metrics API
  slug: rapid7-health-metrics-api
- description: The Investigations API from Rapid7 — 4 operation(s) for investigations.
  name: Rapid7 Investigations API
  slug: rapid7-investigations-api
- description: An API used to find and search InsightIDR local accounts. See https://docs.rapid7.com/insightidr/users-and-accounts-on-your-domain for further information on local accounts.
  name: Rapid7 Local Accounts API
  slug: rapid7-local-accounts-api
- description: Resources and operations for managing policies.
  name: Rapid7 Policy API
  slug: rapid7-policy-api
- description: Policy Override Resource Controller
  name: Rapid7 Policy Override API
  slug: rapid7-policy-override-api
- description: Resources for determining the details required to remediate vulnerabilities.
  name: Rapid7 Remediation API
  slug: rapid7-remediation-api
- description: Resources and operations for managing and generating reports. Reports are broadly categorized into `document`, `export`, and `file` types. `document` reports use section-based report templates to cont
  name: Rapid7 Report API
  slug: rapid7-report-api
- description: 'Reports provide the ability to share information with stakeholders at both scan and app levels. The following table lists the report templates and the various formats that are available: <table> <thea'
  name: Rapid7 Reports API
  slug: rapid7-reports-api
- description: Provides access to primary entry point for discovering the available resources in this API.
  name: Rapid7 Root API
  slug: rapid7-root-api
- description: Resources and operations for managing scans.
  name: Rapid7 Scan API
  slug: rapid7-scan-api
- description: A Scan Config defines all the necessary information required to perform a Scan of an App. An App <i>must</i> be created prior to creating a Scan Config. It is the main document that describes <i>what<
  name: Rapid7 Scan Configs API
  slug: rapid7-scan-configs-api
- description: Resources and operations for managing scan engines.
  name: Rapid7 Scan Engine API
  slug: rapid7-scan-engine-api
- description: Scan Template Resource Controller
  name: Rapid7 Scan Template API
  slug: rapid7-scan-template-api
- description: A Scan encapsulates all the information for a single execution of the criteria defined in the provided Scan Config. An App and a Scan Config <i>must</i> be created prior to submitting a Scan. All Scan
  name: Rapid7 Scans API
  slug: rapid7-scans-api
- description: A Schedule defines the automated execution of a Scan, using a specified Scan Config. Both the App and Scan Config must be created prior to creating a Schedule. There are two options available to speci
  name: Rapid7 Schedules API
  slug: rapid7-schedules-api
- description: A global Search API is exposed to facilitate the execution of user-defined queries that can perform a Search across the supported resource types exposed via the API. Each Search Request must specify b
  name: Rapid7 Search API
  slug: rapid7-search-api
- description: Resources and operations for managing sites.
  name: Rapid7 Site API
  slug: rapid7-site-api
- description: Resources and operations for managing tags.
  name: Rapid7 Tag API
  slug: rapid7-tag-api
- description: Tags are customer-defined labels that can be used for a variety of purposes. The management of Tags is performed by this API, and other APIs facilitate applying these Tags to other resources. These ap
  name: Rapid7 Tags API
  slug: rapid7-tags-api
- description: A Target essentially specifies an allowlisted Fully Qualified Domain Name (FQDN) which can be Scanned by InsightAppSec. A Target can be created, edited and deleted by an API consumer provided the perm
  name: Rapid7 Targets API
  slug: rapid7-targets-api
- description: Resources and operations for managing users, permissions, and privileges.
  name: Rapid7 User API
  slug: rapid7-user-api
- description: An API used to find and search InsightIDR users. See https://docs.rapid7.com/insightidr/users-and-accounts-on-your-domain for further information on users.
  name: Rapid7 Users API
  slug: rapid7-users-api
- description: The Variances Documentation API from Rapid7 — 2 operation(s) for variances documentation.
  name: Rapid7 Variances Documentation API
  slug: rapid7-variances-documentation-api
- description: A Vulnerability is a resource that encapsulates any information found by any Scan over the lifetime of an App, that <i>may</i> identify where and how an App could be exploited. Each Vulnerability cont
  name: Rapid7 Vulnerabilities API
  slug: rapid7-vulnerabilities-api
- description: Resources and operations for viewing vulnerability content and managing exceptions.
  name: Rapid7 Vulnerability API
  slug: rapid7-vulnerability-api
- description: Resources and operations for view vulnerability checks that can be run as a part of vulnerability content.
  name: Rapid7 Vulnerability Check API
  slug: rapid7-vulnerability-check-api
- description: A Vulnerability Comment is a resource that allows users to add context to the Vulnerability.
  name: Rapid7 Vulnerability Comments API
  slug: rapid7-vulnerability-comments-api
- description: Vulnerability Exception Resource Controller
  name: Rapid7 Vulnerability Exception API
  slug: rapid7-vulnerability-exception-api
- description: A Vulnerability History resource represents the change applied to a specific Vulnerability at a point of time in its existence.
  name: Rapid7 Vulnerability History API
  slug: rapid7-vulnerability-history-api
- description: Resources and operations for retrieving vulnerability results on assessed assets.
  name: Rapid7 Vulnerability Result API
  slug: rapid7-vulnerability-result-api
artifact_total: 273
collections:
- collection_type: open
  name: InsightAppSec API
  slug: open-insightappsec
- collection_type: open
  name: InsightIDR API
  slug: open-insightidr
- collection_type: open
  name: InsightVM API
  slug: open-insightvm-console-swagger
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/rapid7-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/rapid7-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rapid7-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/rapid7-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/rapid7
- group: company
  title: ''
  type: Website
  url: https://www.rapid7.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.rapid7.com
- group: other
  title: ''
  type: API Overview
  url: https://docs.rapid7.com/insight/api-overview/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.rapid7.com/contact/
- group: start
  title: ''
  type: Signup
  url: https://insight.rapid7.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/rapid7
- group: operate
  title: ''
  type: Community
  url: https://discuss.rapid7.com
- group: operate
  title: ''
  type: Support
  url: https://www.rapid7.com/services/support/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.rapid7.com
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/rapid7/rapid7-bulk-export-mcp
- group: company
  title: ''
  type: Blog
  url: https://www.rapid7.com/rss.xml
created: '2026-05-11'
description: Rapid7 is a cybersecurity company providing the Insight Platform with products for vulnerability management (InsightVM), SIEM/XDR (InsightIDR), application security (InsightAppSec), cloud security (InsightCloudSec), and SOAR (InsightConnect). The Rapid7 Command/Insight Platform API exposes REST endpoints across regional hosts such as us.api.insight.rapid7.com for managing assets, vulnerabilities, investigations, and integrations. Authentication is performed with an organization or user API key passed in the `X-Api-Key` header.
examples:
- key_count: 6
  name: Rapid7 Addindicators Example
  slug: rapid7-addindicators-example
- key_count: 6
  name: Rapid7 Createcommunitythreat Example
  slug: rapid7-createcommunitythreat-example
- key_count: 6
  name: Rapid7 Getmetrics Example
  slug: rapid7-getmetrics-example
- key_count: 6
  name: Rapid7 Replaceindicators Example
  slug: rapid7-replaceindicators-example
finops:
- name: Rapid7 Finops
  service_category: API
  slug: rapid7-finops
graphqls:
- description: This conceptual GraphQL schema represents the Rapid7 Insight Platform API surface, covering InsightVM (vulnerability management), InsightIDR (SIEM/XDR), and InsightConnect (SOAR). The schema is derive
  name: Rapid7 GraphQL Schema
  slug: rapid7-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rapid7.png
json_schemas:
- name: AccountV2
  property_count: 6
  slug: rapid7-accountv2
- name: AddCollectorRequest
  property_count: 3
  slug: rapid7-addcollectorrequest
- name: AddCollectorResponse
  property_count: 3
  slug: rapid7-addcollectorresponse
- name: AlertInfo
  property_count: 3
  slug: rapid7-alertinfo
- name: AlfDataFile
  property_count: 4
  slug: rapid7-alfdatafile
- name: app
  property_count: 1
  slug: rapid7-app
- name: AssetV2
  property_count: 2
  slug: rapid7-assetv2
- name: Assignee
  property_count: 2
  slug: rapid7-assignee
- name: AssignUserToInvestigationRequest
  property_count: 1
  slug: rapid7-assignusertoinvestigationrequest
- name: Attachment
  property_count: 7
  slug: rapid7-attachment
- name: attack_template
  property_count: 1
  slug: rapid7-attack-template
- name: AttackDocumentation
  property_count: 3
  slug: rapid7-attackdocumentation
- name: AttackerConfig
  property_count: 18
  slug: rapid7-attackerconfig
- name: AttackMetadata
  property_count: 4
  slug: rapid7-attackmetadata
- name: AttackModule
  property_count: 6
  slug: rapid7-attackmodule
- name: AttackTemplate
  property_count: 8
  slug: rapid7-attacktemplate
- name: AuthConfig
  property_count: 68
  slug: rapid7-authconfig
- name: AutoSequenceConfig
  property_count: 2
  slug: rapid7-autosequenceconfig
- name: BinaryContentType
  property_count: 1
  slug: rapid7-binarycontenttype
- name: BinaryExtension
  property_count: 1
  slug: rapid7-binaryextension
- name: Blackout
  property_count: 11
  slug: rapid7-blackout
- name: BrowserDoNotDownloadContentType
  property_count: 1
  slug: rapid7-browserdonotdownloadcontenttype
- name: BrowserDoNotDownloadExtension
  property_count: 1
  slug: rapid7-browserdonotdownloadextension
- name: BrowserDownloadAllowlist
  property_count: 1
  slug: rapid7-browserdownloadallowlist
- name: BrowserFormLoginConfig
  property_count: 8
  slug: rapid7-browserformloginconfig
- name: BulkCloseInvestigationsRequest
  property_count: 6
  slug: rapid7-bulkcloseinvestigationsrequest
- name: ChatbotConfig
  property_count: 17
  slug: rapid7-chatbotconfig
- name: ChromeHostConfig
  property_count: 1
  slug: rapid7-chromehostconfig
- name: ClosedInvestigations
  property_count: 2
  slug: rapid7-closedinvestigations
- name: Comment
  property_count: 7
  slug: rapid7-comment
- name: CommentCreateRequest
  property_count: 3
  slug: rapid7-commentcreaterequest
- name: CrawlConfig
  property_count: 103
  slug: rapid7-crawlconfig
- name: CrawlerInitializationConfig
  property_count: 12
  slug: rapid7-crawlerinitializationconfig
- name: CrawlerMonitoringConfig
  property_count: 7
  slug: rapid7-crawlermonitoringconfig
- name: Creator
  property_count: 2
  slug: rapid7-creator
- name: CredentialResource
  property_count: 1
  slug: rapid7-credentialresource
- name: CustomHeaders
  property_count: 1
  slug: rapid7-customheaders
- name: CustomParameterFile
  property_count: 2
  slug: rapid7-customparameterfile
- name: DefaultDoNotAttackParam
  property_count: 2
  slug: rapid7-defaultdonotattackparam
- name: DeleteThreatEvent
  property_count: 1
  slug: rapid7-deletethreatevent
- name: DenyListExtension
  property_count: 1
  slug: rapid7-denylistextension
- name: DomElementRestriction
  property_count: 8
  slug: rapid7-domelementrestriction
- name: DomRestrictions
  property_count: 5
  slug: rapid7-domrestrictions
- name: Engine
  property_count: 7
  slug: rapid7-engine-group
- name: Engine
  property_count: 8
  slug: rapid7-engine
- name: EngineAssignment
  property_count: 3
  slug: rapid7-engineassignment
- name: EngineGroup
  property_count: 3
  slug: rapid7-enginegroup
- name: EntityModelApp
  property_count: 4
  slug: rapid7-entitymodelapp
- name: EntityModelAttackTemplate
  property_count: 9
  slug: rapid7-entitymodelattacktemplate
- name: EntityModelBlackout
  property_count: 12
  slug: rapid7-entitymodelblackout
- name: EntityModelEngine
  property_count: 9
  slug: rapid7-entitymodelengine
- name: EntityModelEngineGroup
  property_count: 4
  slug: rapid7-entitymodelenginegroup
- name: EntityModelFile
  property_count: 10
  slug: rapid7-entitymodelfile
- name: EntityModelReport
  property_count: 9
  slug: rapid7-entitymodelreport
- name: EntityModelScan
  property_count: 12
  slug: rapid7-entitymodelscan
- name: EntityModelScanConfig
  property_count: 9
  slug: rapid7-entitymodelscanconfig
- name: EntityModelSchedule
  property_count: 9
  slug: rapid7-entitymodelschedule
- name: EntityModelTag
  property_count: 5
  slug: rapid7-entitymodeltag
- name: EntityModelTarget
  property_count: 5
  slug: rapid7-entitymodeltarget
- name: EntityModelVulnerability
  property_count: 14
  slug: rapid7-entitymodelvulnerability
- name: EntityModelVulnerabilityComment
  property_count: 8
  slug: rapid7-entitymodelvulnerabilitycomment
- name: EntityModelVulnerabilityDiscovery
  property_count: 5
  slug: rapid7-entitymodelvulnerabilitydiscovery
- name: Error
  property_count: 3
  slug: rapid7-error
- name: ErrorResponse
  property_count: 2
  slug: rapid7-errorresponse
- name: ErrorResponse1
  property_count: 2
  slug: rapid7-errorresponse1
- name: ErrorResponse2
  property_count: 2
  slug: rapid7-errorresponse2
- name: ErrorResponse3
  property_count: 2
  slug: rapid7-errorresponse3
- name: Exchange
  property_count: 3
  slug: rapid7-exchange
- name: File
  property_count: 9
  slug: rapid7-file
- name: FrameworkConfig
  property_count: 10
  slug: rapid7-frameworkconfig
- name: FrameworksCrawlConfig
  property_count: 3
  slug: rapid7-frameworkscrawlconfig
- name: Schedule
  property_count: 7
  slug: rapid7-frequency
- name: GlobalTokenReplacement
  property_count: 6
  slug: rapid7-globaltokenreplacement
- name: GraphQlConfigObject
  property_count: 8
  slug: rapid7-graphqlconfigobject
- name: GrayListExtension
  property_count: 1
  slug: rapid7-graylistextension
- name: HmacConfig
  property_count: 4
  slug: rapid7-hmacconfig
- name: HtmlContentType
  property_count: 1
  slug: rapid7-htmlcontenttype
- name: HttpAuthExt
  property_count: 3
  slug: rapid7-httpauthext
- name: HttpHeadersConfig
  property_count: 11
  slug: rapid7-httpheadersconfig
- name: HttpParameter
  property_count: 3
  slug: rapid7-httpparameter
- name: IdResource
  property_count: 1
  slug: rapid7-idresource
- name: Investigation
  property_count: 9
  slug: rapid7-investigation
- name: Link
  property_count: 4
  slug: rapid7-link
- name: LocalAccountV2
  property_count: 4
  slug: rapid7-localaccountv2
- name: LockedCookie
  property_count: 1
  slug: rapid7-lockedcookie
- name: LogEvent
  property_count: 2
  slug: rapid7-logevent
- name: LuxorPageable
  property_count: 7
  slug: rapid7-luxorpageable
- name: MacroConfig
  property_count: 2
  slug: rapid7-macroconfig
- name: MacroFile__1
  property_count: 10
  slug: rapid7-macrofile-1
- name: MacroFile
  property_count: 6
  slug: rapid7-macrofile
- name: ManualCrawlingConfig
  property_count: 1
  slug: rapid7-manualcrawlingconfig
- name: ManualSequenceConfig
  property_count: 1
  slug: rapid7-manualsequenceconfig
- name: ModuleConfig
  property_count: 7
  slug: rapid7-moduleconfig
- name: ModuleMetadata
  property_count: 3
  slug: rapid7-modulemetadata
- name: MsalConfig
  property_count: 9
  slug: rapid7-msalconfig
- name: MultiRegexUrlParserConfig
  property_count: 6
  slug: rapid7-multiregexurlparserconfig
- name: NetworkSettingsConfig
  property_count: 20
  slug: rapid7-networksettingsconfig
- name: OauthConfig
  property_count: 18
  slug: rapid7-oauthconfig
- name: OAuthCustomField
  property_count: 2
  slug: rapid7-oauthcustomfield
- name: OneTimePasswordConfig
  property_count: 5
  slug: rapid7-onetimepasswordconfig
- name: OneTimeTokenConfig
  property_count: 5
  slug: rapid7-onetimetokenconfig
- name: Page
  property_count: 2
  slug: rapid7-page
- name: PageAccountV2
  property_count: 2
  slug: rapid7-pageaccountv2
- name: PageApp
  property_count: 3
  slug: rapid7-pageapp
- name: PageAssetV2
  property_count: 2
  slug: rapid7-pageassetv2
- name: PageAttachment
  property_count: 2
  slug: rapid7-pageattachment
- name: PageAttackTemplate
  property_count: 3
  slug: rapid7-pageattacktemplate
- name: PageBlackout
  property_count: 3
  slug: rapid7-pageblackout
- name: PageComment
  property_count: 2
  slug: rapid7-pagecomment
- name: PageEngine
  property_count: 3
  slug: rapid7-pageengine
- name: PageEngineGroup
  property_count: 3
  slug: rapid7-pageenginegroup
- name: PageFile
  property_count: 3
  slug: rapid7-pagefile
- name: PageInvestigation
  property_count: 2
  slug: rapid7-pageinvestigation
- name: PageLocalAccountV2
  property_count: 2
  slug: rapid7-pagelocalaccountv2
- name: PageMetadata
  property_count: 6
  slug: rapid7-pagemetadata
- name: PageMetadata1
  property_count: 4
  slug: rapid7-pagemetadata1
- name: PageMetadata2
  property_count: 4
  slug: rapid7-pagemetadata2
- name: PageMetadata3
  property_count: 4
  slug: rapid7-pagemetadata3
- name: PageObject
  property_count: 3
  slug: rapid7-pageobject
- name: PageReport
  property_count: 3
  slug: rapid7-pagereport
- name: PageScan
  property_count: 3
  slug: rapid7-pagescan
- name: PageScanConfig
  property_count: 3
  slug: rapid7-pagescanconfig
- name: PageSchedule
  property_count: 3
  slug: rapid7-pageschedule
- name: PageTag
  property_count: 3
  slug: rapid7-pagetag
- name: PageTarget
  property_count: 3
  slug: rapid7-pagetarget
- name: PageUserV2
  property_count: 2
  slug: rapid7-pageuserv2
- name: PageVulnerability
  property_count: 3
  slug: rapid7-pagevulnerability
- name: PageVulnerabilityComment
  property_count: 3
  slug: rapid7-pagevulnerabilitycomment
- name: PageVulnerabilityDiscovery
  property_count: 3
  slug: rapid7-pagevulnerabilitydiscovery
- name: ParameterParserConfig
  property_count: 3
  slug: rapid7-parameterparserconfig
- name: ParameterTrainingConfig
  property_count: 2
  slug: rapid7-parametertrainingconfig
- name: ParameterValue
  property_count: 3
  slug: rapid7-parametervalue
- name: ParameterValueConfig
  property_count: 1
  slug: rapid7-parametervalueconfig
- name: PerformanceConfig
  property_count: 7
  slug: rapid7-performanceconfig
- name: ProxyConfig
  property_count: 9
  slug: rapid7-proxyconfig
- name: ProxyExclusions
  property_count: 1
  slug: rapid7-proxyexclusions
- name: ReadOnlyIdResource
  property_count: 1
  slug: rapid7-readonlyidresource
- name: ReferenceResource
  property_count: 1
  slug: rapid7-referenceresource
- name: Report
  property_count: 8
  slug: rapid7-report
- name: Report Generation
  property_count: 9
  slug: rapid7-reportgeneration
- name: RequiredIdResource
  property_count: 1
  slug: rapid7-requiredidresource
- name: RootCause
  property_count: 3
  slug: rapid7-rootcause
- name: RRN
  property_count: 6
  slug: rapid7-rrn
- name: RRN1
  property_count: 6
  slug: rapid7-rrn1
- name: scan_config
  property_count: 1
  slug: rapid7-scan-config
- name: Scan
  property_count: 11
  slug: rapid7-scan
- name: ScanConfig
  property_count: 8
  slug: rapid7-scanconfig
- name: ScanConfigOptions
  property_count: 24
  slug: rapid7-scanconfigoptions
- name: ScanExecutionDetails
  property_count: 10
  slug: rapid7-scanexecutiondetails
- name: ScanModuleParameterFiles
  property_count: 2
  slug: rapid7-scanmoduleparameterfiles
- name: ScanStateActionResource
  property_count: 1
  slug: rapid7-scanstateactionresource
- name: ScanSubmitter
  property_count: 2
  slug: rapid7-scansubmitter
- name: ScanVerificationResource
  property_count: 1
  slug: rapid7-scanverificationresource
- name: Schedule
  property_count: 8
  slug: rapid7-schedule
- name: ScopeConstraint
  property_count: 5
  slug: rapid7-scopeconstraint
- name: SearchRequest
  property_count: 2
  slug: rapid7-searchrequest
- name: SearchRequestCriteria
  property_count: 3
  slug: rapid7-searchrequestcriteria
- name: SearchRequestSort
  property_count: 2
  slug: rapid7-searchrequestsort
- name: SeedUrl
  property_count: 1
  slug: rapid7-seedurl
- name: SeleniumConfig
  property_count: 6
  slug: rapid7-seleniumconfig
- name: SeleniumFile
  property_count: 1
  slug: rapid7-seleniumfile
- name: SequenceConfig
  property_count: 3
  slug: rapid7-sequenceconfig
- name: SequenceIgnoreContentType
  property_count: 1
  slug: rapid7-sequenceignorecontenttype
- name: SequenceIgnoreExtension
  property_count: 1
  slug: rapid7-sequenceignoreextension
- name: SequenceRequest
  property_count: 2
  slug: rapid7-sequencerequest
- name: Sort
  property_count: 3
  slug: rapid7-sort
- name: SpecializedScanParamsResource
  property_count: 4
  slug: rapid7-specializedscanparamsresource
- name: SslCertConfig
  property_count: 5
  slug: rapid7-sslcertconfig
- name: StandardUrlParserConfig
  property_count: 6
  slug: rapid7-standardurlparserconfig
- name: StringReferenceResource
  property_count: 1
  slug: rapid7-stringreferenceresource
- name: SwaggerFile
  property_count: 4
  slug: rapid7-swaggerfile
- name: Tag
  property_count: 4
  slug: rapid7-tag
- name: Target
  property_count: 4
  slug: rapid7-target
- name: TextContentType
  property_count: 1
  slug: rapid7-textcontenttype
- name: TextExtension
  property_count: 1
  slug: rapid7-textextension
- name: Threat
  property_count: 4
  slug: rapid7-threat
- name: ThreatUpdateResult
  property_count: 2
  slug: rapid7-threatupdateresult
- name: TokenReplacement
  property_count: 4
  slug: rapid7-tokenreplacement
- name: TokenReplacementConfig
  property_count: 1
  slug: rapid7-tokenreplacementconfig
- name: TrafficFile
  property_count: 5
  slug: rapid7-trafficfile
- name: TrafficHeader
  property_count: 1
  slug: rapid7-trafficheader
- name: TrainingParameter
  property_count: 7
  slug: rapid7-trainingparameter
- name: UploadAttachmentRequest
  property_count: 1
  slug: rapid7-uploadattachmentrequest
- name: UserDoNotAttackParam
  property_count: 2
  slug: rapid7-userdonotattackparam
- name: UserSummaryV2
  property_count: 2
  slug: rapid7-usersummaryv2
- name: UserSummaryV21
  property_count: 2
  slug: rapid7-usersummaryv21
- name: UserV2
  property_count: 5
  slug: rapid7-userv2
- name: ValidationError
  property_count: 3
  slug: rapid7-validationerror
- name: ValidationErrors
  property_count: 4
  slug: rapid7-validationerrors
- name: Variance
  property_count: 11
  slug: rapid7-variance
- name: VarianceDocumentation
  property_count: 4
  slug: rapid7-variancedocumentation
- name: VarianceFilterRequest
  property_count: 4
  slug: rapid7-variancefilterrequest
- name: Vulnerability
  property_count: 13
  slug: rapid7-vulnerability
- name: VulnerabilityChange
  property_count: 3
  slug: rapid7-vulnerabilitychange
- name: VulnerabilityComment
  property_count: 7
  slug: rapid7-vulnerabilitycomment
- name: VulnerabilityDiscovery
  property_count: 4
  slug: rapid7-vulnerabilitydiscovery
- name: VulnerabilityHistory
  property_count: 3
  slug: rapid7-vulnerabilityhistory
- name: VulnerabilityHistory
  property_count: 4
  slug: rapid7-vulnerabilityupdate
- name: VulnerabilityUpdateSource
  property_count: 2
  slug: rapid7-vulnerabilityupdatesource
- name: WebDriverConfig
  property_count: 2
  slug: rapid7-webdriverconfig
- name: WebServiceAuthConfig
  property_count: 7
  slug: rapid7-webserviceauthconfig
- name: WebServiceConfig
  property_count: 15
  slug: rapid7-webserviceconfig
- name: WebServiceParameter
  property_count: 2
  slug: rapid7-webserviceparameter
- name: Wsdl
  property_count: 1
  slug: rapid7-wsdl
- name: XmlContentType
  property_count: 1
  slug: rapid7-xmlcontenttype
json_structures:
- name: Rapid7 Structure
  property_count: 0
  slug: rapid7-structure
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: Rapid7
nav: Providers
network: true
overview: 'Rapid7 publishes 47 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Administration API, Apps API, and 44 more. Tagged areas include Security, Vulnerability Management, SIEM, XDR, and Cloud Security.


  The Rapid7 catalog on APIs.io includes 1 Spectral governance ruleset.


  Rapid7''s developer surface includes authentication, documentation, pricing, signup flow, support, engineering blog, and 10 more developer resources.'
plans:
- name: Rapid7 Plans Pricing
  plan_count: 1
  slug: rapid7-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 2
  name: Rapid7 Rate Limits
  slug: rapid7-rate-limits
rules:
- name: Rapid7 API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: rapid7-jsonschema-spectral-rules
score:
  band: developing
  composite: 48.2
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 63.6
    developer_ergonomics: 34.8
    discoverability: 50.0
    governance: 58.3
    operational_transparency: 42.1
  previous_composite: 48.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 47
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/rapid7/refs/heads/main/screenshots/rapid7-2026-06-20T192558.png
security:
- kind: authentication
  name: Rapid7 Authentication
  slug: rapid7-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Rapid7 Domain Security
  slug: rapid7-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Rapid7 Vulnerability Disclosure
  slug: rapid7-vulnerability-disclosure
  summary_line: disclosure policy published
slug: rapid7
tags:
- Security
- Vulnerability Management
- SIEM
- XDR
- Cloud Security
- SOAR
- Application Security
website: https://www.rapid7.com
---
