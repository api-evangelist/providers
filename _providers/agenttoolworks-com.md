---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.3
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: API services for verification, VAT checks, scrapers, and MCP servers as documented on the provider site.
  name: AgentToolWorks API
  slug: agenttoolworks-api
- baseURL: https://verifydesk.agenttoolworks.com
  baseurl_source: declared
  description: 'agenttoolworks-com API as documented publicly: 2 operations. Contract generated from the documentation by API Evangelist (2026-10-29); not the provider''s own document.'
  name: agenttoolworks-com API
  slug: agenttoolworks-com-api
artifact_total: 9
common:
- group: company
  title: ''
  type: Blog
  url: https://agenttoolworks.com/blog/france-e-invoicing-api
- group: commercial
  href: https://artifacts.apis.io/agenttoolworks-com/plans/agenttoolworks-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/agenttoolworks-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/agenttoolworks-com/rules/agenttoolworks-com-rules.yml
  title: ''
  type: Spectral
  url: rules/agenttoolworks-com-rules.yml
- group: design
  href: https://artifacts.apis.io/agenttoolworks-com/json-ld/agenttoolworks-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/agenttoolworks-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/agenttoolworks-com/vocabulary/agenttoolworks-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/agenttoolworks-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/agenttoolworks-com/data-model/agenttoolworks-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/agenttoolworks-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/agenttoolworks-com/authentication/agenttoolworks-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/agenttoolworks-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/agenttoolworks-com/conformance/agenttoolworks-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agenttoolworks-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/agenttoolworks-com/well-known/agenttoolworks-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agenttoolworks-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/agenttoolworks-com/hosts/agenttoolworks-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agenttoolworks-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/agenttoolworks-com/vendors/agenttoolworks-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agenttoolworks-com-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://agenttoolworks.com/status
- group: auth
  href: https://artifacts.apis.io/agenttoolworks-com/security/agenttoolworks-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agenttoolworks-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agenttoolworks.com/
- group: docs
  title: ''
  type: Documentation
  url: https://agenttoolworks.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://agenttoolworks.com/servers/verifydesk
- group: start
  title: ''
  type: GettingStarted
  url: https://agenttoolworks.com/signup
- group: commercial
  title: ''
  type: Pricing
  url: https://agenttoolworks.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agenttoolworks.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agenttoolworks.com/privacy
coverage:
  checked: '2026-10-29'
  detail: Provider docs list MCP servers but no OpenAPI, AsyncAPI, GraphQL, or WSDL contracts are publicly available.
  evidence:
  - status: 404
    url: https://api.agenttoolworks.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: AgentToolWorks provides verification and data tools for AI agents, offering services such as company verification, VAT number checks, sanction screening, and various web scrapers for platforms like Shopify, AliExpress, and Google Ads. Their platform includes live production calls, pricing details, documentation, and a free key for initial usage, targeting developers building AI agents that need reliable external data validation.
image: https://agenttoolworks.com/og.png
json_schemas:
- name: PostMcpRequest
  property_count: 5
  slug: agenttoolworks-com-post-mcp-request
- name: PostMcpResponse
  property_count: 17
  slug: agenttoolworks-com-post-mcp-response
jsonld:
- class_count: 2
  name: Agenttoolworks Com Context
  property_count: 22
  slug: agenttoolworks-com-context
layout: provider
modified: '2026-10-29'
name: agenttoolworks-com
nav: Providers
network: true
overview: 'agenttoolworks-com is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Verification, Data Tools, and Web Scraping.


  The agenttoolworks-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  agenttoolworks-com''s developer surface includes engineering blog, authentication, documentation, API reference, getting-started guide, pricing, and 14 more developer resources.'
plans:
- name: Agenttoolworks Com Plans Pricing
  plan_count: 3
  slug: agenttoolworks-com-plans-pricing
random_paper: 7
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: agenttoolworks-com API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: agenttoolworks-com-rules
score:
  band: thin
  composite: 30.1
  coverage:
    artifact_dirs: 18
    catalog_earned: 66.8
    catalog_earned_first_party: 12.0
    catalog_gap: 48.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.8
  facets:
    access_clarity: 47.4
    contract_governance: 22.0
    contract_quality: 23.5
    developer_ergonomics: 27.4
    discoverability: 57.1
    operational_transparency: 7.9
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 37.9
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/agenttoolworks-com/agenttoolworks-com-2026-11-03T120412.png
security:
- kind: authentication
  name: Agenttoolworks Com Authentication
  slug: agenttoolworks-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Agenttoolworks Com Domain Security
  slug: agenttoolworks-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: agenttoolworks-com
tags:
- Company
- Artificial Intelligence
- Verification
- Data Tools
- Web Scraping
website: https://agenttoolworks.com/
---
