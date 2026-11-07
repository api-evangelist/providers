---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: flavored
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 41.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 63
  human_in_the_loop: 6
  name: Gtm Agentic Access
  operation_count: 120
  slug: gtm-agentic-access
  summary_line: 120 operations · 63 acting · 6 human-in-the-loop
api_count: 8
apis:
- baseURL: https://api.gtm.ai/agent
  baseurl_source: declared
  description: Agent API V1
  name: Agent API
  slug: agent-api
- baseURL: https://api.gtm.ai/copilot
  baseurl_source: declared
  description: Copilot API V1
  name: Copilot API
  slug: copilot-api
- baseURL: https://api.gtm.ai/data
  baseurl_source: declared
  description: Data API V1
  name: Data API
  slug: data-api
- baseURL: https://api.gtm.ai/data-quality
  baseurl_source: declared
  description: Data Quality API V1
  name: Data Quality API
  slug: data-quality-api
- baseURL: https://api.gtm.ai/studio
  baseurl_source: declared
  description: GTM Studio API V1
  name: Studio API
  slug: studio-api
- baseURL: https://api.gtm.ai/marketing
  baseurl_source: declared
  description: Marketing API V1
  name: Marketing API
  slug: marketing-api
- baseURL: https://api.gtm.ai/platform
  baseurl_source: declared
  description: Platform API V1
  name: Platform API
  slug: platform-api
- baseURL: https://api.gtm.ai/vertical-datasets
  baseurl_source: declared
  description: Vertical Datasets API V1
  name: Vertical Datasets API
  slug: vertical-datasets-api
artifact_total: 69
common:
- group: other
  href: https://artifacts.apis.io/gtm/capabilities/gtm-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/gtm-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/gtm/agentic-access/gtm-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/gtm-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/gtm/rate-limits/gtm-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/gtm-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/gtm/plans/gtm-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/gtm-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/gtm/rules/gtm-rules.yml
  title: ''
  type: Spectral
  url: rules/gtm-rules.yml
- group: design
  href: https://artifacts.apis.io/gtm/json-ld/gtm-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/gtm-context.jsonld
- group: design
  href: https://artifacts.apis.io/gtm/vocabulary/gtm-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/gtm-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/gtm/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/gtm/data-model/gtm-data-model.yml
  title: ''
  type: DataModel
  url: data-model/gtm-data-model.yml
- group: build
  href: https://artifacts.apis.io/gtm/cli/gtm-cli.yml
  title: ''
  type: CLI
  url: cli/gtm-cli.yml
- group: design
  href: https://artifacts.apis.io/gtm/conventions/gtm-conventions.yml
  title: ''
  type: Conventions
  url: conventions/gtm-conventions.yml
- group: design
  href: https://artifacts.apis.io/gtm/errors/gtm-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/gtm-problem-types.yml
- group: design
  href: https://artifacts.apis.io/gtm/conformance/gtm-conformance.yml
  title: ''
  type: Conformance
  url: conformance/gtm-conformance.yml
- group: agent
  href: https://artifacts.apis.io/gtm/llms/gtm-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/gtm-llms.txt
- group: other
  href: https://artifacts.apis.io/gtm/a2a/gtm-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/gtm-a2a.yml
- group: agent
  href: https://artifacts.apis.io/gtm/mcp/gtm-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/gtm-mcp.yml
- group: agent
  href: https://artifacts.apis.io/gtm/well-known/gtm-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/gtm-well-known.yml
- group: other
  href: https://artifacts.apis.io/gtm/hosts/gtm-hosts.yml
  title: ''
  type: Hosts
  url: hosts/gtm-hosts.yml
- group: other
  href: https://artifacts.apis.io/gtm/vendors/gtm-vendors.yml
  title: ''
  type: Vendors
  url: vendors/gtm-vendors.yml
- group: auth
  href: https://artifacts.apis.io/gtm/scopes/gtm-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/gtm-scopes.yml
- group: auth
  href: https://artifacts.apis.io/gtm/authentication/gtm-authentication.yml
  title: ''
  type: Authentication
  url: authentication/gtm-authentication.yml
- group: auth
  href: https://artifacts.apis.io/gtm/security/gtm-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/gtm-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://gtm.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://gtm.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://docs.gtm.ai/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://gtm.ai/docs/mcp/getting-started
- group: commercial
  title: ''
  type: Pricing
  url: https://gtm.ai/pricing
- group: start
  title: ''
  type: Sandbox
  url: https://gtm.ai/playground
- group: operate
  title: ''
  type: ChangeLog
  url: https://gtm.ai/releases
created: '2026-10-20'
description: ZoomInfo provides a comprehensive suite of B2B data APIs that deliver company, contact, and intent information to power sales, marketing, and recruiting workflows. The platform aggregates millions of firmographic and technographic records, enabling users to enrich CRM data, build lead lists, and automate outreach. With robust search, enrichment, and intent signals, ZoomInfo helps businesses accelerate revenue generation and improve data quality across the customer lifecycle.
image: https://gtm.ai/opengraph-image
json_schemas:
- name: AccountSummaryQuestionRequest
  property_count: 1
  slug: gtm-account-summary-question-request
- name: AgentDetailResponse
  property_count: 1
  slug: gtm-agent-detail-response
- name: AgentRunsListResponse
  property_count: 3
  slug: gtm-agent-runs-list-response
- name: AgentStreamEvent
  property_count: 4
  slug: gtm-agent-stream-event
- name: AgentsListResponse
  property_count: 3
  slug: gtm-agents-list-response
- name: AudienceModelCreate
  property_count: 1
  slug: gtm-audience-model-create
- name: AudienceModel
  property_count: 1
  slug: gtm-audience-model
- name: AudienceModelUpdate
  property_count: 1
  slug: gtm-audience-model-update
- name: AudienceUploadModelCreate
  property_count: 1
  slug: gtm-audience-upload-model-create
- name: AudienceUploadModel
  property_count: 1
  slug: gtm-audience-upload-model
- name: AudiencesJsonApiList
  property_count: 3
  slug: gtm-audiences-json-api-list
- name: BulkRowUpsertListApiModel
  property_count: 1
  slug: gtm-bulk-row-upsert-list-api-model
- name: CompanyInsightsByTypeResponse
  property_count: 1
  slug: gtm-company-insights-by-type-response
- name: CompanySearchResponse
  property_count: 3
  slug: gtm-company-search-response
- name: ContentInteractionResponse
  property_count: 1
  slug: gtm-content-interaction-response
- name: ContentInteractionUpsertRequest
  property_count: 1
  slug: gtm-content-interaction-upsert-request
- name: ContentInteractionUpsertResponse
  property_count: 2
  slug: gtm-content-interaction-upsert-response
- name: CustomerBuyerPersonaUpsert
  property_count: 1
  slug: gtm-customer-buyer-persona-upsert
- name: CustomerCompetitorUpsert
  property_count: 1
  slug: gtm-customer-competitor-upsert
- name: DataQualityRequest
  property_count: 1
  slug: gtm-data-quality-request
- name: DataQualityResponse
  property_count: 1
  slug: gtm-data-quality-response
- name: EarningsCallSearchResponse
  property_count: 3
  slug: gtm-earnings-call-search-response
- name: ExecuteExportRequestBody
  property_count: 1
  slug: gtm-execute-export-request-body
- name: ExecutionResponse
  property_count: 1
  slug: gtm-execution-response
- name: ExportsListResponse
  property_count: 3
  slug: gtm-exports-list-response
- name: FinancialFilingSearchResponse
  property_count: 3
  slug: gtm-financial-filing-search-response
- name: FolderJsonApiList
  property_count: 3
  slug: gtm-folder-json-api-list
- name: GetAudiencesResponse
  property_count: 3
  slug: gtm-get-audiences-response
- name: GetRowsJsonApiModel
  property_count: 3
  slug: gtm-get-rows-json-api-model
- name: IdealCompanySegmentUpsert
  property_count: 1
  slug: gtm-ideal-company-segment-upsert
- name: IntentEnrichResponse
  property_count: 3
  slug: gtm-intent-enrich-response
- name: IntentSearchResponse
  property_count: 3
  slug: gtm-intent-search-response
- name: JobPostSearchResponse
  property_count: 3
  slug: gtm-job-post-search-response
- name: LoanStatementSearchResponse
  property_count: 3
  slug: gtm-loan-statement-search-response
- name: ManagedServiceProviderSearchResponse
  property_count: 3
  slug: gtm-managed-service-provider-search-response
- name: NewsEnrichResponse
  property_count: 3
  slug: gtm-news-enrich-response
- name: NormalizeConfigJsonApiModelCreate
  property_count: 1
  slug: gtm-normalize-config-json-api-model-create
- name: NormalizeConfigListJsonApiModel
  property_count: 3
  slug: gtm-normalize-config-list-json-api-model
- name: OrgChartEnrichResponse
  property_count: 3
  slug: gtm-org-chart-enrich-response
- name: OrganizationOfferingUpsert
  property_count: 1
  slug: gtm-organization-offering-upsert
- name: ProductReviewSearchResponse
  property_count: 3
  slug: gtm-product-review-search-response
- name: PulsesListResponse
  property_count: 3
  slug: gtm-pulses-list-response
- name: RowUpsertListApiModel
  property_count: 1
  slug: gtm-row-upsert-list-api-model
- name: ScoopEnrichResponse
  property_count: 3
  slug: gtm-scoop-enrich-response
- name: ScoreConfigListJsonApiModel
  property_count: 3
  slug: gtm-score-config-list-json-api-model
- name: SegmentConfigListJsonApiModel
  property_count: 3
  slug: gtm-segment-config-list-json-api-model
- name: StartAgentRunRequestBody
  property_count: 1
  slug: gtm-start-agent-run-request-body
- name: UpsertRowsJsonApiModel
  property_count: 1
  slug: gtm-upsert-rows-json-api-model
jsonld:
- class_count: 120
  name: Gtm Context
  property_count: 155
  slug: gtm-context
layout: provider
mcp_servers:
- description: Remote MCP server at docs.gtm.ai.
  name: ZoomInfo MCP Server
  slug: gtm-mcp-yml
modified: '2026-10-20'
name: ZoomInfo
nav: Providers
network: true
overview: 'ZoomInfo publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agent API, Copilot API, Data API, and 5 more. Tagged areas include Company, B2B, Data, and Sales.


  The ZoomInfo catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ZoomInfo''s developer surface includes CLI, authentication, documentation, API reference, getting-started guide, pricing, sandbox, and 22 more developer resources.'
plans:
- name: Gtm Plans Pricing
  plan_count: 1
  slug: gtm-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 9
  name: Gtm Rate Limits
  slug: gtm-rate-limits
rules:
- authorship: generated
  effective_rule_count: 60
  extends:
  - spectral:oas
  name: ZoomInfo API Rules
  rule_count: 19
  severity_counts:
    error: 16
    hint: 0
    info: 2
    warn: 1
  slug: gtm-rules
scopes:
- name: Gtm Scopes
  scope_count: 28
  slug: gtm-scopes
  summary_line: 28 scopes · authorizationCode
score:
  band: developing
  composite: 50.3
  coverage:
    artifact_dirs: 26
    catalog_earned: 80.8
    catalog_earned_first_party: 20.0
    catalog_gap: 34.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.2
  facets:
    access_clarity: 26.3
    contract_governance: 22.0
    contract_quality: 72.1
    developer_ergonomics: 38.7
    discoverability: 71.7
    operational_transparency: 39.5
  previous_composite: 54.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 8
    mcp: first-party
    skills: derived
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
    score: 33.3
screenshot: https://apis.io/screenshots/gtm/gtm-2026-11-03T133125.png
security:
- kind: authentication
  name: Gtm Authentication
  slug: gtm-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Gtm Domain Security
  slug: gtm-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 4
skills:
- name: gtm-account-summary-query
  slug: gtm-account-summary-query
- name: gtm-data-exports-execute-and-retrieve
  slug: gtm-data-exports-execute-and-retrieve
- name: gtm-manage-customer-settings
  slug: gtm-manage-customer-settings
- name: gtm-manage-product
  slug: gtm-manage-product
slug: gtm
tags:
- Company
- B2B
- Data
- Sales
website: https://gtm.ai/
---
