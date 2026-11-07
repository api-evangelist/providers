---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Platfone Com Agentic Access
  operation_count: 18
  slug: platfone-com-agentic-access
  summary_line: 18 operations · 5 acting
api_count: 1
apis:
- baseURL: https://temp-number-api.com/api/v1
  baseurl_source: declared
  description: Activation report related operations.
  name: platfone-com Activation Report API
  slug: platfone-com-activation-report-api
- baseURL: https://temp-number-api.com/api/v1
  baseurl_source: declared
  description: The catalog includes endpoints used to retrieve lists of countries and services available for activation. The list of services is regularly updated, with new services added to the catalog as they beco
  name: platfone-com Catalog API
  slug: platfone-com-catalog-api
- baseURL: https://temp-number-api.com/api/v1
  baseurl_source: declared
  description: 'The section includes endpoints for obtaining prices for activation. Various services have different activation costs, which also depend on the country of the mobile number being ordered. **All prices '
  name: platfone-com Prices API
  slug: platfone-com-prices-api
- baseURL: https://temp-number-api.com/api/v1
  baseurl_source: declared
  description: SMS activation is a process used in registration, verification, or activation of user accounts, services, or software via SMS text message. This API may be used to automate the activation by receiving
  name: platfone-com SMS Activation API
  slug: platfone-com-sms-activation-api
- baseURL: https://temp-number-api.com/api/v1
  baseurl_source: declared
  description: User account related operations.
  name: platfone-com User API
  slug: platfone-com-user-api
- baseURL: https://temp-number-api.com/api/v1
  baseurl_source: declared
  description: Webhooks provide real-time notifications when significant state changes occur within the system. They enable external systems to react to updates without polling the API. For more details on setting u
  name: platfone-com Webhooks 📡 API
  slug: platfone-com-webhooks-api
artifact_total: 22
asyncapis:
- description: ''
  name: Platfone Com Webhooks
  slug: platfone-com-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/platfone-com/agentic-access/platfone-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/platfone-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/platfone-com/rate-limits/platfone-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/platfone-com-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/platfone-com/rules/platfone-com-rules.yml
  title: ''
  type: Spectral
  url: rules/platfone-com-rules.yml
- group: design
  href: https://artifacts.apis.io/platfone-com/json-ld/platfone-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/platfone-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/platfone-com/vocabulary/platfone-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/platfone-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/platfone-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/platfone-com/asyncapi/platfone-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/platfone-com-webhooks.yml
- group: design
  href: https://artifacts.apis.io/platfone-com/data-model/platfone-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/platfone-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/platfone-com/errors/platfone-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/platfone-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/platfone-com/conformance/platfone-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/platfone-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/platfone-com/llms/platfone-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/platfone-com-llms.txt
- group: build
  href: https://artifacts.apis.io/platfone-com/mcp/platfone-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/platfone-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/platfone-com/mcp/platfone-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/platfone-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/platfone-com/hosts/platfone-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/platfone-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/platfone-com/vendors/platfone-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/platfone-com-vendors.yml
- group: start
  title: ''
  type: SignUp
  url: https://platfone.com/auth/create-account
- group: start
  title: ''
  type: GettingStarted
  url: https://platfone.com/docs/start-here/llms.txt
- group: auth
  href: https://artifacts.apis.io/platfone-com/security/platfone-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/platfone-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://platfone.com/
- group: docs
  title: ''
  type: Documentation
  url: https://platfone.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://platfone.com/docs/api/overview/
- group: operate
  title: ''
  type: Support
  url: https://platfone.com/contact-us?type=support
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/platfone-com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://platfone.com/compliance#terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://platfone.com/compliance#privacy
created: '2026-10-30'
description: PlatFone provides a global platform of temporary phone numbers across 100+ countries, offering powerful SMS activation APIs, white‑label solutions, and retail platforms. It supports manual users, developers, and site owners with features like on‑demand number purchase, price‑quality preferences, automated activation via a reliable REST API, and built‑in quality filters. Competitive volume‑discount pricing and a simple web console enable quick refunds and spend tracking.
image: https://platfone.com/favicon.ico
json_schemas:
- name: Activation Report
  property_count: 3
  slug: platfone-com-activation-report-request-body
jsonld:
- class_count: 19
  name: Platfone Com Context
  property_count: 41
  slug: platfone-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.platfone.com requiring an API key.
  name: platfone-com MCP Server
  slug: platfone-com-mcp-yml
modified: '2026-10-30'
name: platfone-com
nav: Providers
network: true
overview: 'platfone-com publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Activation Report API, Catalog API, Prices API, and 3 more. Tagged areas include Company, Telecommunications, SMS, and Temporary-Numbers.


  The platfone-com catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  platfone-com''s developer surface includes signup flow, getting-started guide, documentation, API reference, support, and 20 more developer resources.'
random_paper: 21
rate_limits:
- limit_count: 3
  name: Platfone Com Rate Limits
  slug: platfone-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: platfone-com API Rules
  rule_count: 17
  severity_counts:
    error: 16
    hint: 0
    info: 1
    warn: 0
  slug: platfone-com-rules
scopes:
- name: Platfone Com Scopes
  scope_count: 0
  slug: platfone-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 39.4
  coverage:
    artifact_dirs: 31
    catalog_earned: 65.4
    catalog_earned_first_party: 12.0
    catalog_gap: 49.6
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.4
  facets:
    access_clarity: 17.1
    contract_governance: 19.7
    contract_quality: 71.3
    developer_ergonomics: 18.5
    discoverability: 56.7
    operational_transparency: 42.1
  previous_composite: 47.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 26.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/platfone-com/platfone-com-2026-11-03T141304.png
security:
- kind: authentication
  name: Platfone Com Authentication
  slug: platfone-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Platfone Com Domain Security
  slug: platfone-com-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 6
skills:
- name: cancel-activation
  slug: platfone-com-cancel_activation
- name: check-price
  slug: platfone-com-check_price
- name: check-sms
  slug: platfone-com-check_sms
- name: get-balance
  slug: platfone-com-get_balance
- name: order-number
  slug: platfone-com-order_number
- name: retry-activation
  slug: platfone-com-retry_activation
slug: platfone-com
tags:
- Company
- Telecommunications
- SMS
- Temporary-Numbers
website: https://platfone.com/
---
