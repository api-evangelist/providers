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
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: documented
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 40.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 11
  human_in_the_loop: 11
  name: Catalogapi Com Agentic Access
  operation_count: 29
  slug: catalogapi-com-agentic-access
  summary_line: 29 operations · 11 acting · 11 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.catalogapi.com/api/v2
  baseurl_source: declared
  description: Cart management operations
  name: catalogapi-com Cart API
  slug: catalogapi-com-cart-api
- baseURL: https://api.catalogapi.com/api/v2
  baseurl_source: declared
  description: Catalog browsing and search operations
  name: catalogapi-com Catalog API
  slug: catalogapi-com-catalog-api
- baseURL: https://api.catalogapi.com/api/v2
  baseurl_source: declared
  description: Server checks
  name: catalogapi-com Health API
  slug: catalogapi-com-health-api
- baseURL: https://api.catalogapi.com/api/v2
  baseurl_source: declared
  description: Order management operations
  name: catalogapi-com Order API
  slug: catalogapi-com-order-api
artifact_total: 21
common:
- group: agent
  href: https://artifacts.apis.io/catalogapi-com/agentic-access/catalogapi-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/catalogapi-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/catalogapi-com/rules/catalogapi-com-rules.yml
  title: ''
  type: Spectral
  url: rules/catalogapi-com-rules.yml
- group: design
  href: https://artifacts.apis.io/catalogapi-com/json-ld/catalogapi-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/catalogapi-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/catalogapi-com/vocabulary/catalogapi-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/catalogapi-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/catalogapi-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/catalogapi-com/data-model/catalogapi-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/catalogapi-com-data-model.yml
- group: start
  href: https://artifacts.apis.io/catalogapi-com/sandbox/catalogapi-com-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/catalogapi-com-sandbox.yml
- group: auth
  title: ''
  type: Compliance
  url: https://catalogapi.com:443/
- group: auth
  href: https://artifacts.apis.io/catalogapi-com/authentication/catalogapi-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/catalogapi-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/catalogapi-com/errors/catalogapi-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/catalogapi-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/catalogapi-com/conformance/catalogapi-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/catalogapi-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/catalogapi-com/llms/catalogapi-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/catalogapi-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/catalogapi-com/mcp/catalogapi-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/catalogapi-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/catalogapi-com/well-known/catalogapi-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/catalogapi-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/catalogapi-com/hosts/catalogapi-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/catalogapi-com-hosts.yml
- group: start
  title: ''
  type: SignUp
  url: https://catalogapi.com/users/register
- group: auth
  title: ''
  type: Security
  url: https://catalogapi.com/security
- group: start
  title: ''
  type: DeveloperPortal
  url: https://catalogapi.com/developers/ai-agents
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/catalogapi
- group: auth
  href: https://artifacts.apis.io/catalogapi-com/security/catalogapi-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/catalogapi-com-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/catalogapi-com/security/catalogapi-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/catalogapi-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/catalogapi-com/security/catalogapi-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/catalogapi-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://catalogapi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://catalogapi.com/api/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://catalogapi.com/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://catalogapi.com/privacy
created: '2026-10-30'
description: CatalogAPI provides a global rewards and gift card API that enables businesses to integrate a vast catalog of over 2 million reward options across 120+ countries. The platform simplifies vendor management, fulfillment, and multilingual, multi‑currency support, offering an easy, inexpensive solution for employee, customer, and partner incentive programs. With a single integration, users can search, browse, and order physical or digital rewards worldwide, backed by robust API documentation and pricing plans.
image: https://catalogapi.com/images/catalogapi-og.png
json_schemas:
- name: CartViewResponse
  property_count: 5
  slug: catalogapi-com-cart-view-response
- name: DirectOrderRequest
  property_count: 5
  slug: catalogapi-com-direct-order-request
- name: ItemDetailsResponse
  property_count: 4
  slug: catalogapi-com-item-details-response
- name: ItemsSearchRequest
  property_count: 9
  slug: catalogapi-com-items-search-request
- name: ItemsSearchResponse
  property_count: 10
  slug: catalogapi-com-items-search-response
- name: OrderTrackResponse
  property_count: 3
  slug: catalogapi-com-order-track-response
jsonld:
- class_count: 59
  name: Catalogapi Com Context
  property_count: 162
  slug: catalogapi-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.catalogapi.com.
  name: catalogapi-com MCP Server
  slug: catalogapi-com-mcp-yml
modified: '2026-10-30'
name: catalogapi-com
nav: Providers
network: true
overview: 'catalogapi-com publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Cart API, Catalog API, Health API, and 1 more. Tagged areas include Company, Rewards, Gift Cards, and Global.


  The catalogapi-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  catalogapi-com''s developer surface includes sandbox, authentication, signup flow, documentation, pricing, and 21 more developer resources.'
random_paper: 17
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: catalogapi-com API Rules
  rule_count: 15
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 1
  slug: catalogapi-com-rules
score:
  band: developing
  composite: 40.8
  coverage:
    artifact_dirs: 23
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.7
  facets:
    access_clarity: 28.9
    contract_governance: 35.6
    contract_quality: 68.9
    developer_ergonomics: 30.4
    discoverability: 56.7
    operational_transparency: 7.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - global
  previous_composite: 50.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 2
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 24.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/catalogapi-com/catalogapi-com-2026-11-03T123506.png
security:
- kind: authentication
  name: Catalogapi Com Authentication
  slug: catalogapi-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Catalogapi Com Domain Security
  slug: catalogapi-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Catalogapi Com Vulnerability Disclosure
  slug: catalogapi-com-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Catalogapi Com Trust Center
  slug: catalogapi-com-trust-center
  summary_line: SOC 2, HIPAA, GDPR
skill_count: 3
skills:
- name: catalogapi-com-add-to-cart-and-order
  slug: catalogapi-com-add-to-cart-and-order
- name: catalogapi-com-list-items-and-details
  slug: catalogapi-com-list-items-and-details
- name: catalogapi-com-place-and-track-order
  slug: catalogapi-com-place-and-track-order
slug: catalogapi-com
tags:
- Company
- Rewards
- Gift Cards
- Global
website: https://catalogapi.com/
---
