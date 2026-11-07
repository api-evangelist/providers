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
  band: agent-ready
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: derived
    agentic_commerce: self
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Bolotstudio Com Agentic Access
  operation_count: 6
  slug: bolotstudio-com-agentic-access
  summary_line: 6 operations · 2 acting
api_count: 1
apis:
- baseURL: https://bolotstudio.com
  baseurl_source: declared
  description: The Authentication API from Bolot Studio — 1 operation(s) for authentication.
  name: Bolot Studio Authentication API
  slug: bolotstudio-com-authentication-api
- baseURL: https://bolotstudio.com
  baseurl_source: declared
  description: The Discovery API from Bolot Studio — 2 operation(s) for discovery.
  name: Bolot Studio Discovery API
  slug: bolotstudio-com-discovery-api
- baseURL: https://bolotstudio.com
  baseurl_source: declared
  description: The Feeds API from Bolot Studio — 1 operation(s) for feeds.
  name: Bolot Studio Feeds API
  slug: bolotstudio-com-feeds-api
- baseURL: https://bolotstudio.com
  baseurl_source: declared
  description: The Mcp API from Bolot Studio — 1 operation(s) for mcp.
  name: Bolot Studio MCP API
  slug: bolotstudio-com-mcp-api
- baseURL: https://bolotstudio.com
  baseurl_source: declared
  description: The Products API from Bolot Studio — 1 operation(s) for products.
  name: Bolot Studio Products API
  slug: bolotstudio-com-products-api
artifact_total: 13
common:
- group: agent
  href: https://artifacts.apis.io/bolotstudio-com/agentic-access/bolotstudio-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/bolotstudio-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/bolotstudio-com/rules/bolotstudio-com-rules.yml
  title: ''
  type: Spectral
  url: rules/bolotstudio-com-rules.yml
- group: design
  href: https://artifacts.apis.io/bolotstudio-com/json-ld/bolotstudio-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/bolotstudio-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/bolotstudio-com/vocabulary/bolotstudio-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bolotstudio-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/bolotstudio-com/data-model/bolotstudio-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bolotstudio-com-data-model.yml
- group: auth
  title: ''
  type: Security
  url: https://bolotstudio.com/en/pages/privacy-policy
- group: design
  href: https://artifacts.apis.io/bolotstudio-com/errors/bolotstudio-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/bolotstudio-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/bolotstudio-com/conformance/bolotstudio-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bolotstudio-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/bolotstudio-com/llms/bolotstudio-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bolotstudio-com-llms.txt
- group: other
  href: https://artifacts.apis.io/bolotstudio-com/a2a/bolotstudio-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/bolotstudio-com-a2a.yml
- group: auth
  href: https://artifacts.apis.io/bolotstudio-com/well-known/bolotstudio-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bolotstudio-com-security.txt
- group: auth
  href: https://artifacts.apis.io/bolotstudio-com/well-known/bolotstudio-com-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bolotstudio-com-api-security.txt
- group: agent
  href: https://artifacts.apis.io/bolotstudio-com/well-known/bolotstudio-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bolotstudio-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/bolotstudio-com/hosts/bolotstudio-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bolotstudio-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/bolotstudio-com/vendors/bolotstudio-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bolotstudio-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bolotstudio.com/en/pages/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bolotstudio.com/en/pages/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://bolotstudio.com/en/pages/press
- group: other
  title: ''
  type: Leadership
  url: https://bolotstudio.com/en/team
- group: company
  title: ''
  type: Blog
  url: https://bolotstudio.com/en/blog
- group: auth
  href: https://artifacts.apis.io/bolotstudio-com/authentication/bolotstudio-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bolotstudio-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/bolotstudio-com/security/bolotstudio-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/bolotstudio-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/bolotstudio-com/security/bolotstudio-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bolotstudio-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bolotstudio.com/
created: '2026-11-02'
description: Bolot Studio is a custom print shop offering personalised dye‑sublimation photo prints on aluminium and other materials. Customers can choose from a range of wall or desk formats, matte or glossy finishes, and customise designs for indoor display. The service is built on a Shopify‑based e‑commerce platform with international shipping and a focus on high‑quality, durable artwork.
image: https://bolotstudio.com/og-homepage.jpg
json_schemas:
- name: UCPManifest
  property_count: 6
  slug: bolotstudio-com-ucpmanifest
- name: UCPProduct
  property_count: 33
  slug: bolotstudio-com-ucpproduct
jsonld:
- class_count: 13
  name: Bolotstudio Com Context
  property_count: 63
  slug: bolotstudio-com-context
layout: provider
modified: '2026-11-02'
name: Bolot Studio
nav: Providers
network: true
overview: 'Bolot Studio publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Authentication API, Discovery API, Feeds API, and 2 more. Tagged areas include Print Shop, CustomPrints, E-Commerce, Photography, and Aluminium.


  The Bolot Studio catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Bolot Studio''s developer surface includes engineering blog, authentication, and 22 more developer resources.'
random_paper: 12
rules:
- authorship: generated
  effective_rule_count: 101
  extends:
  - spectral:oas
  name: Bolot Studio API Rules
  rule_count: 60
  severity_counts:
    error: 56
    hint: 0
    info: 3
    warn: 1
  slug: bolotstudio-com-rules
score:
  band: thin
  composite: 32.2
  coverage:
    artifact_dirs: 21
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 62.6
    developer_ergonomics: 13.1
    discoverability: 67.9
    operational_transparency: 5.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Bolotstudio Com Authentication
  slug: bolotstudio-com-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Bolotstudio Com Domain Security
  slug: bolotstudio-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Bolotstudio Com Vulnerability Disclosure
  slug: bolotstudio-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: bolotstudio-com
tags:
- Print Shop
- CustomPrints
- E-Commerce
- Photography
- Aluminium
website: https://bolotstudio.com/
---
