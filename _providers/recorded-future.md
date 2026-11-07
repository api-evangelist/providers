---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: true
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: mostly
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 58.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 107
  human_in_the_loop: 5
  name: Recorded Future Agentic Access
  operation_count: 307
  slug: recorded-future-agentic-access
  summary_line: 307 operations · 107 acting · 5 human-in-the-loop
api_count: 25
apis:
- baseURL: https://api.recordedfuture.com/v2
  baseurl_source: declared
  description: The Recorded Future Intelligence Cloud REST API (api.recordedfuture.com) provides programmatic access to threat intelligence sourced from over a million open-web, dark-web, technical, and customer fee
  name: Recorded Future Intelligence Cloud API
  slug: recorded-future-connect-api
- baseURL: https://api.recordedfuture.com
  baseurl_source: declared
  description: The Alert API allows for interacting with Recorded Future Alerts and Alert rules. Please read the [documentation](https://docs.recordedfuture.com/reference/alerts-get-by-id) before using this API.
  name: Recorded Future Alert API
  slug: alert
- baseURL: https://api.recordedfuture.com/analyst-note
  baseurl_source: declared
  description: A Recorded Future API for creating, fetching, editing and deleting Analyst Notes. Please read the [Recorded Future Docs](https://docs.recordedfuture.com/reference/analyst-note) before using this API.
  name: Recorded Future Analyst Note API
  slug: analyst-note
- baseURL: https://api.securitytrails.com/v2
  baseurl_source: declared
  description: 'The Attack Surface Intelligence (ASI) Project API is designed to allow you full-featured access to all of the `Assets` within all of the `Project`s as well as , most importantly, the `Exposures` that '
  name: Recorded Future ASI Project API
  slug: asi-project
- baseURL: https://api.recordedfuture.com/autonomous-threat-operations
  baseurl_source: declared
  description: APIs for interacting with Recorded Future Autonomous Threat Operations
  name: Recorded Future Autonomous Threat Operations API
  slug: autonomous-threat-operations
- baseURL: https://api.recordedfuture.com/case
  baseurl_source: declared
  description: Case — part of the Recorded Future API documented at docs.recordedfuture.com. A very descriptive description will be available Soon(TM)
  name: Recorded Future Case
  slug: case
- baseURL: https://api.recordedfuture.com/collective-insights/
  baseurl_source: declared
  description: Submit events captured by your security tools to your organization's Recorded Future enterprise. Collective Insights enriches submissions with threat context from Recorded Future Intelligence Graph to
  name: Recorded Future Collective Insights API
  slug: collective-insights
- baseURL: https://api.riskrecon.com
  baseurl_source: declared
  description: Common Platform Enumeration APIs V0 — part of the Recorded Future API documented at docs.recordedfuture.com.
  name: Recorded Future Common Platform Enumeration APIs V0
  slug: common-platform-enumeration-apis-v0
- baseURL: https://api.sandbox.riskrecon.com
  baseurl_source: declared
  description: Customer APIs V0 — part of the Recorded Future API documented at docs.recordedfuture.com.
  name: Recorded Future Customer APIs V0
  slug: customer-apis-v0
- baseURL: https://api.sandbox.riskrecon.com
  baseurl_source: declared
  description: Customer APIs V2 — part of the Recorded Future API documented at docs.recordedfuture.com.
  name: Recorded Future Customer APIs V2
  slug: customer-apis-v2
- baseURL: https://api.recordedfuture.com/detection-rule
  baseurl_source: declared
  description: The Detection Rule API allows clients to programmatically search for and download YARA, Sigma, and Snort rules authored by Recorded Future's Insikt Group. Please read the [detailed support article](ht
  name: Recorded Future Detection Rule API
  slug: detection-rule
- baseURL: https://api.recordedfuture.com/detection-rule-relation
  baseurl_source: declared
  description: API to fetch entities and types associated with detection rules
  name: Recorded Future Detection Rule Relation API
  slug: detection-rule-relation
- baseURL: https://api.recordedfuture.com
  baseurl_source: declared
  description: External API for integrations and clients to lookup entity IDs by name and/or type, and also to find entities given their ID. See [Entity Types and ID Prefixes](https://docs.recordedfuture.com/referen
  name: Recorded Future Entity Match API
  slug: entity-match
- baseURL: https://api.recordedfuture.com/fusion/v3
  baseurl_source: declared
  description: A Recorded Future API for managing Fusion flows, files and custom blocks Please read the [detailed support article](https://support.recordedfuture.com/hc/en-us/articles/360000713994-Introduction-to-th
  name: Recorded Future Fusion API
  slug: fusion
- baseURL: https://api.recordedfuture.com
  baseurl_source: declared
  description: API to lookup identity leaks data.<br><br> [Identity API](https://support.recordedfuture.com/hc/en-us/articles/4402477586707-Identity-API)<br> [Identity Lookup API Response](https://support.recordedfu
  name: Recorded Future Identity API
  slug: identity
- baseURL: https://api.recordedfuture.com/links
  baseurl_source: declared
  description: An API to retrieve verified links between entities. Links may come from technical analysis of cyber threats or Insikt Group research. Please read the [detailed support article](https://support.recorde
  name: Recorded Future Links API
  slug: links
- baseURL: https://api.recordedfuture.com
  baseurl_source: declared
  description: External List API for reading and writing user lists Please read the [detailed support article](https://support.recordedfuture.com/hc/en-us/articles/360058691913-List-API) before using this API.
  name: Recorded Future List API
  slug: list
- baseURL: https://api.recordedfuture.com/malware-intelligence
  baseurl_source: declared
  description: A Recorded Future API for Malware Intelligence. The Malware Intelligence API provides programmatic access to the functionality of Recorded Future Malware Intelligence.
  name: Recorded Future Malware Intelligence
  slug: malware-intelligence
- baseURL: https://api.sandbox.riskrecon.com
  baseurl_source: declared
  description: RiskRecon provides organizations with frequent, comprehensive, actionable visibility into the security quality of their business partners. RiskRecon does this by automatically measuring the security p
  name: Recorded Future Mastercard Riskrecon API
  slug: mastercard-riskrecon
- baseURL: https://pfi.regemini.com/api/v1
  baseurl_source: declared
  description: Payment Fraud Intelligence API — part of the Recorded Future API documented at docs.recordedfuture.com.
  name: Recorded Future Payment Fraud Intelligence API
  slug: payment-fraud-intelligence
- baseURL: https://api.recordedfuture.com/playbook-alert
  baseurl_source: declared
  description: 'A Recorded Future API for Playbook Alerts. The playbook alert API provides programmatic access to Recorded Future playbook alerts. These alerts differ quite a bit from the standard "alerts" generated '
  name: Recorded Future Playbook Alerts
  slug: playbook-alerts
- baseURL: https://api.recordedfuture.com/risk
  baseurl_source: declared
  description: A Recorded Future API for fetching risk and risk risk history information.
  name: Recorded Future Risk API
  slug: risk
- baseURL: https://sandbox.recordedfuture.com/api/v0
  baseurl_source: declared
  description: Recorded Future Sandbox API (formerly Hatching Tria.ge). Provides malware analysis capabilities including file/URL submission, behavioral analysis, YARA rule management, and organizational settings.
  name: Recorded Future recorded-future-sandbox-api-secopsti
  slug: sandbox-api-secopsti
- baseURL: https://api.recordedfuture.com/soar/v3
  baseurl_source: declared
  description: The SOAR API is designed for high throughput risk checks using Recorded Future's threat intelligence in bulk. It supports five IOC types, IP Address, Domain, Hash, URL and Vulnerability. Please read t
  name: Recorded Future Soar API
  slug: soar
- baseURL: https://api.recordedfuture.com/threat
  baseurl_source: declared
  description: External API to retrieve threat data such as threat maps, threat actors and their categories. Please read the [detailed support article](https://support.recordedfuture.com/hc/en-us/articles/1444392730
  name: Recorded Future Threat API
  slug: threat
artifact_total: 158
common:
- group: other
  href: https://artifacts.apis.io/recorded-future/capabilities/recorded-future-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/recorded-future-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/recorded-future/agentic-access/recorded-future-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/recorded-future-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/recorded-future/rules/recorded-future-rules.yml
  title: ''
  type: Spectral
  url: rules/recorded-future-rules.yml
- group: design
  href: https://artifacts.apis.io/recorded-future/json-ld/recorded-future-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/recorded-future-context.jsonld
- group: design
  href: https://artifacts.apis.io/recorded-future/vocabulary/recorded-future-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/recorded-future-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/recorded-future/data-model/recorded-future-data-model.yml
  title: ''
  type: DataModel
  url: data-model/recorded-future-data-model.yml
- group: operate
  href: https://artifacts.apis.io/recorded-future/changelog/recorded-future-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/recorded-future-changelog.yml
- group: design
  href: https://artifacts.apis.io/recorded-future/conventions/recorded-future-conventions.yml
  title: ''
  type: Conventions
  url: conventions/recorded-future-conventions.yml
- group: design
  href: https://artifacts.apis.io/recorded-future/lifecycle/recorded-future-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/recorded-future-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/recorded-future/errors/recorded-future-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/recorded-future-error-codes.yml
- group: design
  href: https://artifacts.apis.io/recorded-future/errors/recorded-future-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/recorded-future-problem-types.yml
- group: design
  href: https://artifacts.apis.io/recorded-future/conformance/recorded-future-conformance.yml
  title: ''
  type: Conformance
  url: conformance/recorded-future-conformance.yml
- group: agent
  href: https://artifacts.apis.io/recorded-future/llms/recorded-future-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/recorded-future-llms.txt
- group: agent
  href: https://artifacts.apis.io/recorded-future/mcp/recorded-future-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/recorded-future-mcp.yml
- group: auth
  href: https://artifacts.apis.io/recorded-future/well-known/recorded-future-sandbox-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/recorded-future-sandbox-security.txt
- group: auth
  href: https://artifacts.apis.io/recorded-future/well-known/recorded-future-pfi-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/recorded-future-pfi-security.txt
- group: auth
  href: https://artifacts.apis.io/recorded-future/well-known/recorded-future-mcp-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/recorded-future-mcp-security.txt
- group: auth
  href: https://artifacts.apis.io/recorded-future/well-known/recorded-future-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/recorded-future-app-security.txt
- group: agent
  href: https://artifacts.apis.io/recorded-future/well-known/recorded-future-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/recorded-future-well-known.yml
- group: other
  href: https://artifacts.apis.io/recorded-future/hosts/recorded-future-hosts.yml
  title: ''
  type: Hosts
  url: hosts/recorded-future-hosts.yml
- group: build
  href: https://artifacts.apis.io/recorded-future/integrations/recorded-future-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/recorded-future-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/recorded-future/vendors/recorded-future-vendors.yml
  title: ''
  type: Vendors
  url: vendors/recorded-future-vendors.yml
- group: build
  href: https://artifacts.apis.io/recorded-future/packages/recorded-future-packages.yml
  title: ''
  type: SDKs
  url: packages/recorded-future-packages.yml
- group: build
  href: https://artifacts.apis.io/recorded-future/packages/recorded-future-packages.yml
  title: ''
  type: Packages
  url: packages/recorded-future-packages.yml
- group: auth
  title: ''
  type: Security
  url: https://www.recordedfuture.com/security
- group: start
  title: ''
  type: Login
  url: https://id.recordedfuture.com/login/sso?sso_id=google&request_id=6dM1avqWks4UrAG8_NwNU2K0qrNkMC73CiIHUdZ8hvWa_Vv7tJcHxkjarcRrp4X3loSDCYr3CiRiqH78rWy_P2ygnyZMTwvibTUUrZnvMIHGQzQvXBnUu9eJQnbGpgXmdfIlmTXNjFXAHEhpayR0JY-wwRzPI577teEC4Y365wA-eBNziKeEKdTv9A_DdbYFtlbzI0lCvgW-Fl-BnQnziNcnRG99ms5Ps38zKjBhqsy7kmWf4n_NvOUFxkP9RWDSz3TUoLJEnTSrbYCwGS8i-8Dgr44i3Ep_DkmtuRtGeYLloqQYXKusoNXcIlUDzGrDzW4T9JzdGkRaVPSiS9yCZd0iR4fB4eymOqEMH41Jn4cjEokE4_hi_ECKvOST2E_3ac4u8GL4iLy4AD5qdVLjYCI-OAjB_rhNmweswdxQEpYkDI7dVkI7d4H2iDysdiQWtobLEUqe2dxZkc5FQz2_xUd4j8p4t9l8Fv7z3fTK2OaF99xCzGWc9Y62eCoeK4Z3v9gidC_jxuiPoghsssONqPw8W9lbZgAl8hSLKuSICYuaLPzWqWTDmdqxmpDo-qDojzvCbS02ESR-zT3LFPl31HjJfo-u5C9G7_fE7KjNC-H9sVQHcT6XXoIhFeqletcioTEnFrEmPyev76IoaO_TXnDFaa10Tnh5FwPQgjrJ-ZNtrAyDBS1S-fKGHoFfgYERBDSlxty1dXccligl36LKw7IY993w3DNe7FFqnggmvFI0UlA3ZX6p5w
- group: auth
  href: https://artifacts.apis.io/recorded-future/authentication/recorded-future-authentication.yml
  title: ''
  type: Authentication
  url: authentication/recorded-future-authentication.yml
- group: commercial
  href: https://artifacts.apis.io/recorded-future/plans/recorded-future-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/recorded-future-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/recorded-future/rate-limits/recorded-future-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/recorded-future-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/recorded-future/finops/recorded-future-finops.yml
  title: ''
  type: FinOps
  url: finops/recorded-future-finops.yml
- group: auth
  href: https://artifacts.apis.io/recorded-future/security/recorded-future-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/recorded-future-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/recorded-future/security/recorded-future-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/recorded-future-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/recorded-future
- group: company
  title: ''
  type: Website
  url: https://www.recordedfuture.com/
- group: start
  title: Recorded Future Customer Portal
  type: Portal
  url: https://app.recordedfuture.com/
- group: operate
  title: ''
  type: Support
  url: https://support.recordedfuture.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.recordedfuture.com/blog
- group: company
  title: The Record by Recorded Future
  type: News
  url: https://therecord.media/
- group: operate
  title: ''
  type: ContactSales
  url: https://www.recordedfuture.com/contact
- group: company
  title: ''
  type: Careers
  url: https://www.recordedfuture.com/careers
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.recordedfuture.com/legal/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.recordedfuture.com/legal/terms-of-use
- group: docs
  title: ''
  type: Documentation
  url: https://docs.recordedfuture.com/reference
- group: docs
  title: ''
  type: APIReference
  url: https://docs.recordedfuture.com/reference
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.recordedfuture.com/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.recordedfuture.com/reference/get-started
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/recordedfuture
- group: commercial
  title: ''
  type: Pricing
  url: https://www.recordedfuture.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.recordedfuture.com/
- group: operate
  title: ''
  type: Community
  url: https://community.recordedfuture.com/
created: '2026-05-23'
description: Recorded Future is a threat intelligence platform whose Intelligence Cloud combines open-web, dark-web, technical, and customer telemetry sources via the Intelligence Graph, indexed and analyzed by Insikt Group analysts and AI. The platform spans Threat Intelligence, Brand Intelligence, Identity Intelligence, SecOps Intelligence, Vulnerability Intelligence, Attack Surface Intelligence, Payment Fraud Intelligence, and Geopolitical Intelligence, plus Cyber Daily and the AI Analyst. Recorded Future exposes a REST API at api.recordedfuture.com (commonly called ConnectAPI) that customers and integration partners use to pull indicators, entities, alerts, and risk scores into SIEMs, SOARs, TIPs, and custom security workflows. Named a Leader in the 2026 Gartner Magic Quadrant for Cyberthreat Intelligence Technologies.
features:
- description: Unified intelligence platform delivering prioritized, organization-specific intelligence
  name: Intelligence Cloud
- description: Core graph data structure indexing and analyzing 1M+ open-web, dark-web, technical, and telemetry sources
  name: Intelligence Graph
- description: Tactical, operational, and strategic threat intelligence on actors, malware, TTPs, and indicators
  name: Threat Intelligence
- description: Detection of brand impersonation, typosquatting, and digital risk to corporate brands
  name: Brand Intelligence
- description: Monitoring of leaked credentials, identity exposures, and credential compromise events
  name: Identity Intelligence
- description: Intelligence purpose-built for SOC workflows, alerting, and triage
  name: SecOps Intelligence
- description: Vulnerability risk scoring, exploit chatter, and prioritization for patching decisions
  name: Vulnerability Intelligence
- description: Continuous discovery and monitoring of external-facing assets and exposures
  name: Attack Surface Intelligence
- description: Intelligence on stolen cards, fraud actors, and dark-web payment fraud markets
  name: Payment Fraud Intelligence
- description: Geopolitical and physical security intelligence for global operations
  name: Geopolitical Intelligence
- description: Generative AI assistant that summarizes intelligence and accelerates analyst workflows
  name: AI Analyst
- description: Daily curated digest of the global threat landscape
  name: Cyber Daily
- description: In-house intelligence research and analyst team producing finished intelligence
  name: Insikt Group
finops:
- has_sources: false
  method: generated
  name: Recorded Future Finops
  primary_unit: ''
  service_category: API
  slug: recorded-future-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/recorded-future.png
json_schemas:
- name: AddOperationResponse
  property_count: 1
  slug: recorded-future-add-operation-response
- name: AlertRuleSearchResponseV2
  property_count: 2
  slug: recorded-future-alert-rule-search-response-v2
- name: AlertSearchDetailsResponseV2
  property_count: 2
  slug: recorded-future-alert-search-details-response-v2
- name: AlertSearchResponseV2
  property_count: 2
  slug: recorded-future-alert-search-response-v2
- name: AlertSearchResponseV3
  property_count: 2
  slug: recorded-future-alert-search-response-v3
- name: AlertUpdateData
  property_count: 0
  slug: recorded-future-alert-update-data
- name: AlertUpdateResponse
  property_count: 2
  slug: recorded-future-alert-update-response
- name: AssetSearchRequest
  property_count: 4
  slug: recorded-future-asset-search-request
- name: AssetsFilterRequest
  property_count: 2
  slug: recorded-future-assets-filter-request
- name: AuditLogResponse
  property_count: 3
  slug: recorded-future-audit-log-response
- name: BulkTagAssetsRequest
  property_count: 1
  slug: recorded-future-bulk-tag-assets-request
- name: CaseLookupBulkRequest
  property_count: 3
  slug: recorded-future-case-lookup-bulk-request
- name: CaseSearchRequest
  property_count: 11
  slug: recorded-future-case-search-request
- name: CaseSearchResponse
  property_count: 4
  slug: recorded-future-case-search-response
- name: CategoriesResponse
  property_count: 2
  slug: recorded-future-categories-response
- name: ContextResponse
  property_count: 3
  slug: recorded-future-context-response
- name: CreateCaseRequest
  property_count: 7
  slug: recorded-future-create-case-request
- name: CreateSigmaJobRequest
  property_count: 4
  slug: recorded-future-create-sigma-job-request
- name: CreateYaraJobRequest
  property_count: 3
  slug: recorded-future-create-yara-job-request
- name: CredentialsLookupRequest
  property_count: 7
  slug: recorded-future-credentials-lookup-request
- name: CredentialsSearchRequest
  property_count: 6
  slug: recorded-future-credentials-search-request
- name: CveProductLookups
  property_count: 0
  slug: recorded-future-cve-product-lookups
- name: DarkWebBrandResponse
  property_count: 8
  slug: recorded-future-dark-web-brand-response
- name: DeleteCaseResponse
  property_count: 3
  slug: recorded-future-delete-case-response
- name: DetectionRuleFilter
  property_count: 6
  slug: recorded-future-detection-rule-filter
- name: DetectionRuleResult
  property_count: 4
  slug: recorded-future-detection-rule-result
- name: DomainAbuseResponse
  property_count: 8
  slug: recorded-future-domain-abuse-response
- name: DomainLookupResponse
  property_count: 2
  slug: recorded-future-domain-lookup-response
- name: DraftRequest
  property_count: 5
  slug: recorded-future-draft-request
- name: EditYaraJobRequest
  property_count: 2
  slug: recorded-future-edit-yara-job-request
- name: EnrichRequest
  property_count: 6
  slug: recorded-future-enrich-request
- name: EnrichResponse
  property_count: 3
  slug: recorded-future-enrich-response
- name: EntityEntry
  property_count: 4
  slug: recorded-future-entity-entry
- name: EntityEntryWithTags
  property_count: 5
  slug: recorded-future-entity-entry-with-tags
- name: EntityLookupResponse
  property_count: 1
  slug: recorded-future-entity-lookup-response
- name: EntityMatchResponse
  property_count: 3
  slug: recorded-future-entity-match-response
- name: EntityResult
  property_count: 0
  slug: recorded-future-entity-result
- name: EntityTypes
  property_count: 0
  slug: recorded-future-entity-types
- name: Enumeration
  property_count: 2
  slug: recorded-future-enumeration
- name: FileDirectoryResponse
  property_count: 4
  slug: recorded-future-file-directory-response
- name: file.Request
  property_count: 2
  slug: recorded-future-file-request
- name: FileResponse
  property_count: 0
  slug: recorded-future-file-response
- name: FileUploadResponse
  property_count: 7
  slug: recorded-future-file-upload-response
- name: FiltersResponse
  property_count: 4
  slug: recorded-future-filters-response
- name: Finding
  property_count: 87
  slug: recorded-future-finding
- name: Findings language
  property_count: 8
  slug: recorded-future-findings-language
- name: Findings
  property_count: 0
  slug: recorded-future-findings
- name: GeopoliticsFacilityResponse
  property_count: 7
  slug: recorded-future-geopolitics-facility-response
- name: GetActiveRiskRuleRequest
  property_count: 4
  slug: recorded-future-get-active-risk-rule-request
- name: GetActiveRiskRuleResponse
  property_count: 2
  slug: recorded-future-get-active-risk-rule-response
- name: GetSigmaJobResponse
  property_count: 12
  slug: recorded-future-get-sigma-job-response
- name: GetSigmaJobsRequest
  property_count: 2
  slug: recorded-future-get-sigma-jobs-request
- name: HashLookupResponse
  property_count: 2
  slug: recorded-future-hash-lookup-response
- name: IncidentReportRequest
  property_count: 5
  slug: recorded-future-incident-report-request
- name: IndustryTrends
  property_count: 2
  slug: recorded-future-industry-trends
- name: IpLookupResponse
  property_count: 2
  slug: recorded-future-ip-lookup-response
- name: ListExclusionsResponse
  property_count: 3
  slug: recorded-future-list-exclusions-response
- name: ListInfo
  property_count: 10
  slug: recorded-future-list-info
- name: LookupResponse
  property_count: 3
  slug: recorded-future-lookup-response
- name: mage.ResponseAddToQueue
  property_count: 4
  slug: recorded-future-mage-response-add-to-queue
- name: MaliciousSitesCreateOptions
  property_count: 5
  slug: recorded-future-malicious-sites-create-options
- name: MaliciousSitesResponse
  property_count: 7
  slug: recorded-future-malicious-sites-response
- name: MalwareCategoriesResponse
  property_count: 2
  slug: recorded-future-malware-categories-response
- name: MalwareLookupResponse
  property_count: 2
  slug: recorded-future-malware-lookup-response
- name: MalwareThreatMapRequest
  property_count: 3
  slug: recorded-future-malware-threat-map-request
- name: MetadataCommon
  property_count: 4
  slug: recorded-future-metadata-common
- name: OperationResult
  property_count: 1
  slug: recorded-future-operation-result
- name: PortfolioMember
  property_count: 3
  slug: recorded-future-portfolio-member
- name: preset.ClientRequest-preset_MagecartMerchantClientConfig
  property_count: 3
  slug: recorded-future-preset-client-request-preset-magecart-merchant-client-config
- name: preset.ClientRequest-preset_MagescannerScansClientConfig
  property_count: 3
  slug: recorded-future-preset-client-request-preset-magescanner-scans-client-config
- name: preset.ClientRequest-preset_PartialCardSoldClientConfig
  property_count: 3
  slug: recorded-future-preset-client-request-preset-partial-card-sold-client-config
- name: PreviewRequest
  property_count: 6
  slug: recorded-future-preview-request
- name: ProfileId
  property_count: 0
  slug: recorded-future-profile-id
- name: Profile
  property_count: 7
  slug: recorded-future-profile
- name: PublishRequest
  property_count: 9
  slug: recorded-future-publish-request
- name: QueryNLResponse
  property_count: 4
  slug: recorded-future-query-nlresponse
- name: Query
  property_count: 3
  slug: recorded-future-query
- name: queue.ResponseStatus
  property_count: 6
  slug: recorded-future-queue-response-status
- name: SampleDetail
  property_count: 10
  slug: recorded-future-sample-detail
- name: SampleSummary
  property_count: 8
  slug: recorded-future-sample-summary
- name: SearchRequest
  property_count: 12
  slug: recorded-future-search-request
- name: SearchResponse
  property_count: 3
  slug: recorded-future-search-response
- name: SearchRiskHistoriesRequest
  property_count: 3
  slug: recorded-future-search-risk-histories-request
- name: SearchRiskHistoriesResponse
  property_count: 2
  slug: recorded-future-search-risk-histories-response
- name: Source
  property_count: 5
  slug: recorded-future-source
- name: SubmitDetectionsRequest
  property_count: 3
  slug: recorded-future-submit-detections-request
- name: SubmitDetectionsResponse
  property_count: 1
  slug: recorded-future-submit-detections-response
- name: TagAssetRequest
  property_count: 2
  slug: recorded-future-tag-asset-request
- name: TagOperationRequest
  property_count: 2
  slug: recorded-future-tag-operation-request
- name: TagOperationResponse
  property_count: 2
  slug: recorded-future-tag-operation-response
- name: ThreatActorsRequest
  property_count: 3
  slug: recorded-future-threat-actors-request
- name: ThreatActorsResponse
  property_count: 3
  slug: recorded-future-threat-actors-response
- name: ThreatHuntJobId
  property_count: 0
  slug: recorded-future-threat-hunt-job-id
- name: ThreatHuntJobStatus
  property_count: 0
  slug: recorded-future-threat-hunt-job-status
- name: Threat Intell Results
  property_count: 0
  slug: recorded-future-threat-intell-results
- name: ThreatMapRequest
  property_count: 3
  slug: recorded-future-threat-map-request
- name: TriageResponse
  property_count: 3
  slug: recorded-future-triage-response
- name: UpdateRequest
  property_count: 6
  slug: recorded-future-update-request
- name: UpdateStaticAssetsResponse
  property_count: 2
  slug: recorded-future-update-static-assets-response
- name: UrlLookupResponse
  property_count: 2
  slug: recorded-future-url-lookup-response
- name: Vulnerabilities and Language
  property_count: 2
  slug: recorded-future-vulnerabilities-and-language
- name: Vulnerabilities
  property_count: 0
  slug: recorded-future-vulnerabilities
- name: VulnerabilityLookupResponse
  property_count: 2
  slug: recorded-future-vulnerability-lookup-response
jsonld:
- class_count: 120
  name: Recorded Future Context
  property_count: 227
  slug: recorded-future-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.recordedfuture.com over HTTP.
  name: Recorded Future MCP Server
  slug: recorded-future
modified: '2026-10-20'
name: Recorded Future
nav: Providers
network: true
overview: 'Recorded Future publishes 25 API contracts indexed on the [APIs.io](https://apis.io/) network, including Intelligence Cloud API, Alert API, Analyst Note API, and 22 more. Tagged areas include Cybersecurity, Threat Intelligence, Intelligence Cloud, Brand Intelligence, and Identity Intelligence.


  The Recorded Future catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Recorded Future''s developer surface includes changelog, authentication, developer portal, support, engineering blog, product news, documentation, and 43 more developer resources.'
plans:
- name: Recorded Future Plans Pricing
  plan_count: 3
  slug: recorded-future-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 1
  name: Recorded Future Rate Limits
  slug: recorded-future-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Recorded Future API Rules
  rule_count: 11
  severity_counts:
    error: 6
    hint: 0
    info: 3
    warn: 2
  slug: recorded-future-rules
scopes:
- name: Recorded Future Scopes
  scope_count: 0
  slug: recorded-future-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 61.6
  coverage:
    artifact_dirs: 31
    catalog_earned: 85.8
    catalog_earned_first_party: 20.0
    catalog_gap: 29.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.6
  facets:
    access_clarity: 59.2
    contract_governance: 22.0
    contract_quality: 70.7
    developer_ergonomics: 50.0
    discoverability: 80.8
    operational_transparency: 44.7
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 67.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 96.0
      derived: 0
      marker_coverage: 100.0
      total: 25
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 38.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 27.8
screenshot: https://apis.io/screenshots/recorded-future/recorded-future-2026-06-20T192704.png
security:
- kind: authentication
  name: Recorded Future Authentication
  slug: recorded-future-authentication
  summary_line: apiKey/http/oauth2 · 5 schemes
- kind: domain-security
  name: Recorded Future Domain Security
  slug: recorded-future-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Recorded Future Vulnerability Disclosure
  slug: recorded-future-vulnerability-disclosure
  summary_line: Bugcrowd · security.txt · contact published
slug: recorded-future
tags:
- Cybersecurity
- Threat Intelligence
- Intelligence Cloud
- Brand Intelligence
- Identity Intelligence
- Vulnerability Intelligence
- AI Analyst
use_cases:
- description: Enrich SIEM and SOAR alerts with risk scores and entity context from the Intelligence Cloud
  name: SOC Alert Triage
- description: Prioritize CVE remediation using real-world exploit and threat-actor activity
  name: Vulnerability Management
- description: Detect and respond to brand impersonation, typosquatting, and phishing infrastructure
  name: Brand Protection
- description: Detect leaked credentials and identity exposures for employees and customers
  name: Identity and Credential Monitoring
- description: Monitor third-party and supply-chain partners for threat exposure
  name: Third-Party Risk
- description: Track geopolitical events affecting people, facilities, and operations
  name: Geopolitical Risk
website: https://www.recordedfuture.com/
---
