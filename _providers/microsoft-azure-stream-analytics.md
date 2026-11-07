---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Paid · Self-serve signup
  onboarding: self-serve
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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: derived
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 6
  human_in_the_loop: 1
  name: Microsoft Azure Stream Analytics Agentic Access
  operation_count: 14
  slug: microsoft-azure-stream-analytics-agentic-access
  summary_line: 14 operations · 6 acting · 1 human-in-the-loop
api_count: 8
apis:
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The Clusters API from Azure Stream Analytics — 7 operation(s) for clusters, served through Azure Resource Manager (api-version 2020-03-01).
  name: Azure Stream Analytics Clusters API
  slug: microsoft-azure-stream-analytics-clusters-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The Functions API from Azure Stream Analytics — 7 operation(s) for functions, served through Azure Resource Manager (api-version 2020-03-01).
  name: Azure Stream Analytics Functions API
  slug: microsoft-azure-stream-analytics-functions-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The Inputs API from Azure Stream Analytics — 6 operation(s) for inputs, served through Azure Resource Manager (api-version 2020-03-01).
  name: Azure Stream Analytics Inputs API
  slug: microsoft-azure-stream-analytics-inputs-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The Outputs API from Azure Stream Analytics — 6 operation(s) for outputs, served through Azure Resource Manager (api-version 2020-03-01).
  name: Azure Stream Analytics Outputs API
  slug: microsoft-azure-stream-analytics-outputs-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The StreamingJobs API from Azure Stream Analytics — 10 operation(s) for streamingjobs, served through Azure Resource Manager (api-version 2020-03-01).
  name: Azure Stream Analytics StreamingJobs API
  slug: microsoft-azure-stream-analytics-streamingjobs-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The Transformations API from Azure Stream Analytics — 3 operation(s) for transformations, served through Azure Resource Manager (api-version 2020-03-01).
  name: Azure Stream Analytics Transformations API
  slug: microsoft-azure-stream-analytics-transformations-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The Subscriptions API from Azure Stream Analytics — 1 operation(s) for subscriptions, served through Azure Resource Manager (api-version 2020-03-01).
  name: Azure Stream Analytics Subscriptions API
  slug: microsoft-azure-stream-analytics-subscriptions-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The Operations API from Azure Stream Analytics — 1 operation(s) for operations.
  name: Azure Stream Analytics Operations API
  slug: microsoft-azure-stream-analytics-operations-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The Private Endpoints API from Azure Stream Analytics — 2 operation(s) for private endpoints.
  name: Azure Stream Analytics Private Endpoints API
  slug: microsoft-azure-stream-analytics-private-endpoints-api
artifact_total: 49
collections:
- collection_type: open
  name: Azure Stream Analytics REST Clusters API
  slug: open-microsoft-azure-stream-analytics-clusters-api
- collection_type: open
  name: Azure Stream Analytics REST Clusters Functions API
  slug: open-microsoft-azure-stream-analytics-functions-api
- collection_type: open
  name: Azure Stream Analytics REST Clusters Inputs API
  slug: open-microsoft-azure-stream-analytics-inputs-api
- collection_type: open
  name: Azure Stream Analytics REST Clusters Outputs API
  slug: open-microsoft-azure-stream-analytics-outputs-api
- collection_type: open
  name: Azure Stream Analytics REST Clusters StreamingJobs API
  slug: open-microsoft-azure-stream-analytics-streamingjobs-api
- collection_type: open
  name: Azure Stream Analytics REST Clusters Transformations API
  slug: open-microsoft-azure-stream-analytics-transformations-api
- collection_type: open
  name: Azure Stream Analytics REST API
  slug: open-microsoft-azure-stream-analytics
common:
- group: design
  href: https://artifacts.apis.io/microsoft-azure-stream-analytics/rules/microsoft-azure-stream-analytics-rules.yml
  title: ''
  type: Spectral
  url: rules/microsoft-azure-stream-analytics-rules.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-stream-analytics/json-ld/microsoft-azure-stream-analytics-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/microsoft-azure-stream-analytics-context.jsonld
- group: design
  href: https://artifacts.apis.io/microsoft-azure-stream-analytics/vocabulary/microsoft-azure-stream-analytics-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/microsoft-azure-stream-analytics-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/microsoft-azure-stream-analytics/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-stream-analytics/data-model/microsoft-azure-stream-analytics-data-model.yml
  title: ''
  type: DataModel
  url: data-model/microsoft-azure-stream-analytics-data-model.yml
- group: build
  href: https://artifacts.apis.io/microsoft-azure-stream-analytics/cli/microsoft-azure-stream-analytics-cli.yml
  title: ''
  type: CLI
  url: cli/microsoft-azure-stream-analytics-cli.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-stream-analytics/conventions/microsoft-azure-stream-analytics-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/microsoft-azure-stream-analytics-conventions.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-stream-analytics/conventions/microsoft-azure-stream-analytics-conventions.yml
  title: ''
  type: Conventions
  url: conventions/microsoft-azure-stream-analytics-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.microsoft.com/en-us/trust-center
- group: design
  href: https://artifacts.apis.io/microsoft-azure-stream-analytics/lifecycle/microsoft-azure-stream-analytics-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/microsoft-azure-stream-analytics-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-stream-analytics/errors/microsoft-azure-stream-analytics-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/microsoft-azure-stream-analytics-problem-types.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-stream-analytics/conformance/microsoft-azure-stream-analytics-conformance.yml
  title: ''
  type: Conformance
  url: conformance/microsoft-azure-stream-analytics-conformance.yml
- group: agent
  href: https://artifacts.apis.io/microsoft-azure-stream-analytics/llms/microsoft-azure-stream-analytics-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/microsoft-azure-stream-analytics-llms.txt
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-stream-analytics/well-known/microsoft-azure-stream-analytics-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/microsoft-azure-stream-analytics-security.txt
- group: agent
  href: https://artifacts.apis.io/microsoft-azure-stream-analytics/well-known/microsoft-azure-stream-analytics-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/microsoft-azure-stream-analytics-well-known.yml
- group: other
  href: https://artifacts.apis.io/microsoft-azure-stream-analytics/hosts/microsoft-azure-stream-analytics-hosts.yml
  title: ''
  type: Hosts
  url: hosts/microsoft-azure-stream-analytics-hosts.yml
- group: other
  href: https://artifacts.apis.io/microsoft-azure-stream-analytics/vendors/microsoft-azure-stream-analytics-vendors.yml
  title: ''
  type: Vendors
  url: vendors/microsoft-azure-stream-analytics-vendors.yml
- group: build
  href: https://artifacts.apis.io/microsoft-azure-stream-analytics/packages/microsoft-azure-stream-analytics-packages.yml
  title: ''
  type: SDKs
  url: packages/microsoft-azure-stream-analytics-packages.yml
- group: build
  href: https://artifacts.apis.io/microsoft-azure-stream-analytics/packages/microsoft-azure-stream-analytics-packages.yml
  title: ''
  type: Packages
  url: packages/microsoft-azure-stream-analytics-packages.yml
- group: auth
  title: ''
  type: Security
  url: https://techcommunity.microsoft.com/tag/security
- group: other
  title: ''
  type: Leadership
  url: https://news.microsoft.com/leadership
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.microsoft.com/en-us/changelog
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-stream-analytics/scopes/microsoft-azure-stream-analytics-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-azure-stream-analytics-scopes.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-stream-analytics/security/microsoft-azure-stream-analytics-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/microsoft-azure-stream-analytics-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-stream-analytics/security/microsoft-azure-stream-analytics-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/microsoft-azure-stream-analytics-vulnerability-disclosure.yml
- group: commercial
  href: https://artifacts.apis.io/microsoft-azure-stream-analytics/plans/microsoft-azure-stream-analytics-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/microsoft-azure-stream-analytics-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/microsoft-azure-stream-analytics/rate-limits/microsoft-azure-stream-analytics-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/microsoft-azure-stream-analytics-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/microsoft-azure-stream-analytics/finops/microsoft-azure-stream-analytics-finops.yml
  title: ''
  type: FinOps
  url: finops/microsoft-azure-stream-analytics-finops.yml
- group: company
  title: ''
  type: Website
  url: https://microsoft.com
- group: agent
  href: https://artifacts.apis.io/microsoft-azure-stream-analytics/agentic-access/microsoft-azure-stream-analytics-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-azure-stream-analytics-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-stream-analytics/security/microsoft-azure-stream-analytics-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/microsoft-azure-stream-analytics-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-stream-analytics/authentication/microsoft-azure-stream-analytics-authentication.yml
  title: ''
  type: Authentication
  url: authentication/microsoft-azure-stream-analytics-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Azure
- group: start
  title: ''
  type: Portal
  url: https://portal.azure.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://azure.microsoft.com/en-us/pricing/details/stream-analytics/
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/azure/stream-analytics/
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/azure/stream-analytics/stream-analytics-quick-create-portal
- group: operate
  title: ''
  type: StatusPage
  url: https://azure.status.microsoft/en-us/status
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.microsoft.com/en-us/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: operate
  title: ''
  type: Support
  url: https://support.microsoft.com/
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/azure-stream-analytics
- group: agent
  title: ''
  type: LlmsText
  url: https://portal.azure.com/llms.txt
- group: docs
  title: ''
  type: APIReference
  url: https://learn.microsoft.com/en-us/rest/api/streamanalytics/
- group: build
  title: ''
  type: CLI
  url: https://learn.microsoft.com/en-us/cli/azure/stream-analytics
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.microsoft.com/en-us
- group: company
  title: ''
  type: Blog
  url: https://azure.microsoft.com/en-us/blog/
created: '2026-03-13'
description: Azure Stream Analytics is Microsoft Azure's fully managed real-time analytics service. Its REST API, served through Azure Resource Manager at management.azure.com, manages streaming jobs, inputs (Event Hubs, IoT Hub, Blob storage), outputs, user-defined functions, SQL-like transformation queries, dedicated clusters, private endpoints and subscription quotas, with SDKs for .NET, Java, Python, JavaScript and Go and an Azure CLI extension.
finops:
- has_sources: true
  method: derived
  name: Microsoft Azure Stream Analytics Finops
  primary_unit: ''
  service_category: ''
  slug: microsoft-azure-stream-analytics-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-azure-stream-analytics.png
json_schemas:
- name: ClusterJobListResult
  property_count: 2
  slug: microsoft-azure-stream-analytics-cluster-job-list-result
- name: ClusterListResult
  property_count: 2
  slug: microsoft-azure-stream-analytics-cluster-list-result
- name: Cluster
  property_count: 8
  slug: microsoft-azure-stream-analytics-cluster
- name: FunctionListResult
  property_count: 2
  slug: microsoft-azure-stream-analytics-function-list-result
- name: FunctionRetrieveDefaultDefinitionParameters
  property_count: 1
  slug: microsoft-azure-stream-analytics-function-retrieve-default-definition-parameters
- name: Function
  property_count: 4
  slug: microsoft-azure-stream-analytics-function
- name: InputListResult
  property_count: 2
  slug: microsoft-azure-stream-analytics-input-list-result
- name: Input
  property_count: 4
  slug: microsoft-azure-stream-analytics-input
- name: OperationListResult
  property_count: 2
  slug: microsoft-azure-stream-analytics-operation-list-result
- name: OutputListResult
  property_count: 2
  slug: microsoft-azure-stream-analytics-output-list-result
- name: Output
  property_count: 4
  slug: microsoft-azure-stream-analytics-output
- name: PrivateEndpointListResult
  property_count: 2
  slug: microsoft-azure-stream-analytics-private-endpoint-list-result
- name: PrivateEndpoint
  property_count: 5
  slug: microsoft-azure-stream-analytics-private-endpoint
- name: ResourceTestStatus
  property_count: 2
  slug: microsoft-azure-stream-analytics-resource-test-status
- name: ScaleStreamingJobParameters
  property_count: 1
  slug: microsoft-azure-stream-analytics-scale-streaming-job-parameters
- name: StartStreamingJobParameters
  property_count: 2
  slug: microsoft-azure-stream-analytics-start-streaming-job-parameters
- name: StreamingJobListResult
  property_count: 2
  slug: microsoft-azure-stream-analytics-streaming-job-list-result
- name: StreamingJob
  property_count: 7
  slug: microsoft-azure-stream-analytics-streaming-job
- name: SubscriptionQuotasListResult
  property_count: 1
  slug: microsoft-azure-stream-analytics-subscription-quotas-list-result
- name: Transformation
  property_count: 4
  slug: microsoft-azure-stream-analytics-transformation
jsonld:
- class_count: 120
  name: Microsoft Azure Stream Analytics Context
  property_count: 123
  slug: microsoft-azure-stream-analytics-context
layout: provider
modified: '2026-11-05'
name: Azure Stream Analytics
nav: Providers
network: true
overview: 'Azure Stream Analytics publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Clusters API, Functions API, Inputs API, and 6 more. Tagged areas include Stream Processing, Real-Time Analytics, IoT, Event Processing, and Microsoft Azure.


  The Azure Stream Analytics catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Azure Stream Analytics'' developer surface includes CLI, changelog, authentication, developer portal, pricing, documentation, getting-started guide, and 40 more developer resources.'
plans:
- name: Microsoft Azure Stream Analytics Plans Pricing
  plan_count: 5
  slug: microsoft-azure-stream-analytics-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 6
  name: Microsoft Azure Stream Analytics Rate Limits
  slug: microsoft-azure-stream-analytics-rate-limits
rules:
- authorship: generated
  effective_rule_count: 95
  extends:
  - spectral:oas
  name: Azure Stream Analytics API Rules
  rule_count: 54
  severity_counts:
    error: 46
    hint: 0
    info: 3
    warn: 5
  slug: microsoft-azure-stream-analytics-rules
scopes:
- name: Microsoft Azure Stream Analytics Scopes
  scope_count: 1
  slug: microsoft-azure-stream-analytics-scopes
  summary_line: 1 scope · implicit
score:
  band: exemplar
  composite: 71.0
  coverage:
    artifact_dirs: 32
    catalog_earned: 89.8
    catalog_earned_first_party: 24.0
    catalog_gap: 25.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 23.2
  facets:
    access_clarity: 78.9
    contract_governance: 22.0
    contract_quality: 55.0
    developer_ergonomics: 70.8
    discoverability: 87.5
    operational_transparency: 76.3
  previous_composite: 47.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 45.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: rising
  upsert:
    applies: true
    score: 22.2
screenshot: https://apis.io/screenshots/microsoft-azure-stream-analytics/microsoft-azure-stream-analytics-2026-06-20T185440.png
security:
- kind: authentication
  name: Microsoft Azure Stream Analytics Authentication
  slug: microsoft-azure-stream-analytics-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Microsoft Azure Stream Analytics Domain Security
  slug: microsoft-azure-stream-analytics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Microsoft Azure Stream Analytics Vulnerability Disclosure
  slug: microsoft-azure-stream-analytics-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Microsoft Azure Stream Analytics Trust Center
  slug: microsoft-azure-stream-analytics-trust-center
  summary_line: GDPR
skill_count: 2
skills:
- name: run-streaming-job
  slug: microsoft-azure-stream-analytics-run-streaming-job
- name: scale-streaming-job
  slug: microsoft-azure-stream-analytics-scale-streaming-job
slug: microsoft-azure-stream-analytics
tags:
- Stream Processing
- Real-Time Analytics
- IoT
- Event Processing
- Microsoft Azure
- Streaming
website: https://microsoft.com
---
