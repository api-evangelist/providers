---
access_model:
  confidence: medium
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
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: self
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 73.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 16
  human_in_the_loop: 0
  name: Adadiamonds Com Agentic Access
  operation_count: 41
  slug: adadiamonds-com-agentic-access
  summary_line: 41 operations · 16 acting
api_count: 1
apis:
- baseURL: https://www.adadiamonds.com
  baseurl_source: declared
  description: The Agentic checkout (ACP) API from Ada Diamonds — 4 operation(s) for agentic checkout (acp).
  name: Ada Diamonds Agentic checkout (ACP) API
  slug: adadiamonds-com-agentic-checkout-acp-api
- baseURL: https://www.adadiamonds.com
  baseurl_source: declared
  description: The Agentic checkout (hosted link) API from Ada Diamonds — 1 operation(s) for agentic checkout (hosted link).
  name: Ada Diamonds Agentic checkout (hosted link) API
  slug: adadiamonds-com-agentic-checkout-hosted-link-api
- baseURL: https://www.adadiamonds.com
  baseurl_source: declared
  description: The Agentic checkout (UCP) API from Ada Diamonds — 4 operation(s) for agentic checkout (ucp).
  name: Ada Diamonds Agentic checkout (UCP) API
  slug: adadiamonds-com-agentic-checkout-ucp-api
- baseURL: https://www.adadiamonds.com
  baseurl_source: declared
  description: The Agentic commerce discovery API from Ada Diamonds — 3 operation(s) for agentic commerce discovery.
  name: Ada Diamonds Agentic commerce discovery API
  slug: adadiamonds-com-agentic-commerce-discovery-api
- baseURL: https://www.adadiamonds.com
  baseurl_source: declared
  description: Consultation requests.
  name: Ada Diamonds Appointments API
  slug: adadiamonds-com-appointments-api
- baseURL: https://www.adadiamonds.com
  baseurl_source: declared
  description: Batched reads and asynchronous catalog exports.
  name: Ada Diamonds Bulk API
  slug: adadiamonds-com-bulk-api
- baseURL: https://www.adadiamonds.com
  baseurl_source: declared
  description: Diamonds, engagement rings, and jewelry.
  name: Ada Diamonds Catalog API
  slug: adadiamonds-com-catalog-api
- baseURL: https://www.adadiamonds.com
  baseurl_source: declared
  description: Published guides and company information.
  name: Ada Diamonds Content API
  slug: adadiamonds-com-content-api
- baseURL: https://www.adadiamonds.com
  baseurl_source: declared
  description: API roots and credential checks.
  name: Ada Diamonds Discovery API
  slug: adadiamonds-com-discovery-api
- baseURL: https://www.adadiamonds.com
  baseurl_source: declared
  description: The MCP API from Ada Diamonds — 1 operation(s) for mcp.
  name: Ada Diamonds MCP API
  slug: adadiamonds-com-mcp-api
- baseURL: https://www.adadiamonds.com
  baseurl_source: declared
  description: Self-serve credentials.
  name: Ada Diamonds Onboarding API
  slug: adadiamonds-com-onboarding-api
- baseURL: https://www.adadiamonds.com
  baseurl_source: declared
  description: The Search API from Ada Diamonds — 1 operation(s) for search.
  name: Ada Diamonds Search API
  slug: adadiamonds-com-search-api
artifact_total: 32
asyncapis:
- description: ''
  name: Adadiamonds Com Webhooks
  slug: adadiamonds-com-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/adadiamonds-com/agentic-access/adadiamonds-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/adadiamonds-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/adadiamonds-com/plans/adadiamonds-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/adadiamonds-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/adadiamonds-com/rules/adadiamonds-com-rules.yml
  title: ''
  type: Spectral
  url: rules/adadiamonds-com-rules.yml
- group: design
  href: https://artifacts.apis.io/adadiamonds-com/json-ld/adadiamonds-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/adadiamonds-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/adadiamonds-com/vocabulary/adadiamonds-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/adadiamonds-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/adadiamonds-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/adadiamonds-com/asyncapi/adadiamonds-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/adadiamonds-com-webhooks.yml
- group: design
  href: https://artifacts.apis.io/adadiamonds-com/data-model/adadiamonds-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/adadiamonds-com-data-model.yml
- group: build
  href: https://artifacts.apis.io/adadiamonds-com/cli/adadiamonds-com-cli.yml
  title: ''
  type: CLI
  url: cli/adadiamonds-com-cli.yml
- group: design
  href: https://artifacts.apis.io/adadiamonds-com/conventions/adadiamonds-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/adadiamonds-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/adadiamonds-com/conventions/adadiamonds-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/adadiamonds-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/adadiamonds-com/authentication/adadiamonds-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/adadiamonds-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/adadiamonds-com/errors/adadiamonds-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/adadiamonds-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/adadiamonds-com/conformance/adadiamonds-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/adadiamonds-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/adadiamonds-com/llms/adadiamonds-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/adadiamonds-com-llms.txt
- group: other
  href: https://artifacts.apis.io/adadiamonds-com/a2a/adadiamonds-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/adadiamonds-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/adadiamonds-com/mcp/adadiamonds-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/adadiamonds-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/adadiamonds-com/well-known/adadiamonds-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/adadiamonds-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/adadiamonds-com/hosts/adadiamonds-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/adadiamonds-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/adadiamonds-com/vendors/adadiamonds-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/adadiamonds-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/adadiamonds-com/packages/adadiamonds-com-packages.yml
  title: ''
  type: SDKs
  url: packages/adadiamonds-com-packages.yml
- group: build
  href: https://artifacts.apis.io/adadiamonds-com/packages/adadiamonds-com-packages.yml
  title: ''
  type: Packages
  url: packages/adadiamonds-com-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.adadiamonds.com/terms
- group: start
  title: ''
  type: Sandbox
  url: https://www.adadiamonds.com/sandbox
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.adadiamonds.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.adadiamonds.com/pricing.md
- group: company
  title: ''
  type: Newsroom
  url: https://www.adadiamonds.com/press
- group: docs
  title: ''
  type: APIReference
  url: https://www.adadiamonds.com/developers
- group: auth
  href: https://artifacts.apis.io/adadiamonds-com/scopes/adadiamonds-com-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/adadiamonds-com-scopes.yml
- group: auth
  href: https://artifacts.apis.io/adadiamonds-com/security/adadiamonds-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/adadiamonds-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://adadiamonds.com/
created: '2026-10-31'
description: Ada Diamonds is a New York‑based jeweler specializing in lab‑grown diamond engagement rings and fine jewelry. The company offers custom‑made pieces crafted with premium lab diamonds curated by experts, providing high quality at accessible prices. Their online store showcases a wide selection of settings, styles, and metal options, catering to customers seeking sustainable and ethically sourced gemstones for special occasions.
image: https://www.adadiamonds.com/api/og/?title=Lab%20Diamond%20Engagement%20%26%20Wedding%20Rings
json_schemas:
- name: AcpCheckoutSession
  property_count: 18
  slug: adadiamonds-com-acp-checkout-session
- name: AcpFeedProduct
  property_count: 27
  slug: adadiamonds-com-acp-feed-product
- name: CheckoutLink
  property_count: 11
  slug: adadiamonds-com-checkout-link
- name: Job
  property_count: 12
  slug: adadiamonds-com-job
- name: UcpCheckoutRequest
  property_count: 4
  slug: adadiamonds-com-ucp-checkout-request
- name: UcpCheckout
  property_count: 14
  slug: adadiamonds-com-ucp-checkout
jsonld:
- class_count: 62
  name: Adadiamonds Com Context
  property_count: 209
  slug: adadiamonds-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at www.adadiamonds.com.
  name: Ada Diamonds MCP Server
  slug: adadiamonds-com-mcp-yml
modified: '2026-10-31'
name: Ada Diamonds
nav: Providers
network: true
overview: 'Ada Diamonds publishes 12 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agentic checkout (ACP) API, Agentic checkout (hosted link) API, Agentic checkout (UCP) API, and 9 more. Tagged areas include Jewelry, Lab Diamonds, Engagement Rings, New York, and E-Commerce.


  The Ada Diamonds catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Ada Diamonds'' developer surface includes CLI, authentication, sandbox, pricing, API reference, and 26 more developer resources.'
plans:
- name: Adadiamonds Com Plans Pricing
  plan_count: 1
  slug: adadiamonds-com-plans-pricing
random_paper: 17
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: Ada Diamonds API Rules
  rule_count: 15
  severity_counts:
    error: 12
    hint: 0
    info: 2
    warn: 1
  slug: adadiamonds-com-rules
scopes:
- name: Adadiamonds Com Scopes
  scope_count: 6
  slug: adadiamonds-com-scopes
  summary_line: 6 scopes · authorizationCode/clientCredentials
score:
  band: developing
  composite: 45.3
  coverage:
    artifact_dirs: 26
    catalog_earned: 70.8
    catalog_earned_first_party: 8.0
    catalog_gap: 44.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.3
  facets:
    access_clarity: 36.8
    contract_governance: 22.0
    contract_quality: 73.6
    developer_ergonomics: 35.1
    discoverability: 65.8
    operational_transparency: 7.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 50.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Adadiamonds Com Authentication
  slug: adadiamonds-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Adadiamonds Com Domain Security
  slug: adadiamonds-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 5
skills:
- name: adadiamonds-com-acp-checkout
  slug: adadiamonds-com-acp-checkout
- name: adadiamonds-com-bulk-export-catalog
  slug: adadiamonds-com-bulk-export-catalog
- name: adadiamonds-com-onboarding
  slug: adadiamonds-com-onboarding
- name: adadiamonds-com-search
  slug: adadiamonds-com-search
- name: adadiamonds-com-ucp-complete-purchase
  slug: adadiamonds-com-ucp-complete-purchase
slug: adadiamonds-com
tags:
- Jewelry
- Lab Diamonds
- Engagement Rings
- New York
- E-Commerce
website: https://adadiamonds.com/
---
