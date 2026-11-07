---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 44.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 20
  human_in_the_loop: 0
  name: Cartviral Com Agentic Access
  operation_count: 34
  slug: cartviral-com-agentic-access
  summary_line: 34 operations · 20 acting
api_count: 1
apis:
- baseURL: https://app.cartviral.com/api/v1
  baseurl_source: declared
  description: The Account API from CartViral — 1 operation(s) for account.
  name: CartViral Account API
  slug: cartviral-com-account-api
- baseURL: https://app.cartviral.com/api/v1
  baseurl_source: declared
  description: The Carousels API from CartViral — 1 operation(s) for carousels.
  name: CartViral Carousels API
  slug: cartviral-com-carousels-api
- baseURL: https://app.cartviral.com/api/v1
  baseurl_source: declared
  description: The Characters API from CartViral — 2 operation(s) for characters.
  name: CartViral Characters API
  slug: cartviral-com-characters-api
- baseURL: https://app.cartviral.com/api/v1
  baseurl_source: declared
  description: The Clips API from CartViral — 2 operation(s) for clips.
  name: CartViral Clips API
  slug: cartviral-com-clips-api
- baseURL: https://app.cartviral.com/api/v1
  baseurl_source: declared
  description: The Create API from CartViral — 10 operation(s) for create.
  name: CartViral Create API
  slug: cartviral-com-create-api
- baseURL: https://app.cartviral.com/api/v1
  baseurl_source: declared
  description: The Creations API from CartViral — 2 operation(s) for creations.
  name: CartViral Creations API
  slug: cartviral-com-creations-api
- baseURL: https://app.cartviral.com/api/v1
  baseurl_source: declared
  description: The Media API from CartViral — 1 operation(s) for media.
  name: CartViral Media API
  slug: cartviral-com-media-api
- baseURL: https://app.cartviral.com/api/v1
  baseurl_source: declared
  description: The Offers API from CartViral — 2 operation(s) for offers.
  name: CartViral Offers API
  slug: cartviral-com-offers-api
- baseURL: https://app.cartviral.com/api/v1
  baseurl_source: declared
  description: The Photos API from CartViral — 1 operation(s) for photos.
  name: CartViral Photos API
  slug: cartviral-com-photos-api
- baseURL: https://app.cartviral.com/api/v1
  baseurl_source: declared
  description: The Pitches API from CartViral — 1 operation(s) for pitches.
  name: CartViral Pitches API
  slug: cartviral-com-pitches-api
- baseURL: https://app.cartviral.com/api/v1
  baseurl_source: declared
  description: The Products API from CartViral — 4 operation(s) for products.
  name: CartViral Products API
  slug: cartviral-com-products-api
- baseURL: https://app.cartviral.com/api/v1
  baseurl_source: declared
  description: The Static Ads API from CartViral — 1 operation(s) for static ads.
  name: CartViral Static Ads API
  slug: cartviral-com-static-ads-api
artifact_total: 21
common:
- group: agent
  href: https://artifacts.apis.io/cartviral-com/agentic-access/cartviral-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/cartviral-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/cartviral-com/plans/cartviral-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cartviral-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/cartviral-com/rules/cartviral-com-rules.yml
  title: ''
  type: Spectral
  url: rules/cartviral-com-rules.yml
- group: design
  href: https://artifacts.apis.io/cartviral-com/json-ld/cartviral-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/cartviral-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/cartviral-com/vocabulary/cartviral-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/cartviral-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/cartviral-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/cartviral-com/data-model/cartviral-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cartviral-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/cartviral-com/errors/cartviral-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/cartviral-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/cartviral-com/conformance/cartviral-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cartviral-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/cartviral-com/llms/cartviral-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cartviral-com-llms.txt
- group: build
  href: https://artifacts.apis.io/cartviral-com/mcp/cartviral-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/cartviral-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/cartviral-com/mcp/cartviral-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/cartviral-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/cartviral-com/well-known/cartviral-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cartviral-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/cartviral-com/hosts/cartviral-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cartviral-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/cartviral-com/vendors/cartviral-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cartviral-com-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://cartviral.com/help
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://app.cartviral.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://cartviral.com/pricing
- group: start
  title: ''
  type: Login
  url: https://app.cartviral.com/web/login
- group: docs
  title: ''
  type: Documentation
  url: https://cartviral.com/guides
- group: docs
  title: ''
  type: APIReference
  url: https://cartviral.com/api
- group: auth
  href: https://artifacts.apis.io/cartviral-com/scopes/cartviral-com-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/cartviral-com-scopes.yml
- group: auth
  href: https://artifacts.apis.io/cartviral-com/authentication/cartviral-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cartviral-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/cartviral-com/security/cartviral-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cartviral-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cartviral.com/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://app.cartviral.com/mcp
  - status: 200
    url: https://cartviral.com/
  reason: partner-login
  state: gated
created: '2026-11-03'
description: CartViral is an AI content engine for e‑commerce sellers that generates product videos, UGC ads, photos, carousels and short clips for platforms like TikTok, Reels and Shorts. Users simply paste a product link or upload photos, and the service creates multiple video formats, ad hooks and social media assets, offering a free tier with three AI‑generated clips. The platform aims to streamline advertising creation for online stores, leveraging AI to produce engaging visual content quickly and at scale.
image: https://cartviral.com/og/index.jpg?v=b9d46bc0
jsonld:
- class_count: 1
  name: Cartviral Com Context
  property_count: 1
  slug: cartviral-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at app.cartviral.com.
  name: CartViral MCP Server
  slug: cartviral-com-mcp-yml
modified: '2026-11-03'
name: CartViral
nav: Providers
network: true
overview: 'CartViral publishes 12 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Carousels API, Characters API, and 9 more. Tagged areas include Company, Artificial Intelligence, E-Commerce, Video Generation, and Marketing.


  The CartViral catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  CartViral''s developer surface includes support, pricing, documentation, API reference, authentication, and 20 more developer resources.'
plans:
- name: Cartviral Com Plans Pricing
  plan_count: 4
  slug: cartviral-com-plans-pricing
random_paper: 12
rules:
- authorship: generated
  effective_rule_count: 102
  extends:
  - spectral:oas
  name: CartViral API Rules
  rule_count: 61
  severity_counts:
    error: 58
    hint: 0
    info: 1
    warn: 2
  slug: cartviral-com-rules
scopes:
- name: Cartviral Com Scopes
  scope_count: 1
  slug: cartviral-com-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: thin
  composite: 38.7
  coverage:
    artifact_dirs: 21
    catalog_earned: 59.8
    catalog_earned_first_party: 12.0
    catalog_gap: 55.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 48.7
    contract_governance: 22.0
    contract_quality: 54.8
    developer_ergonomics: 24.4
    discoverability: 65.0
    operational_transparency: 0.0
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
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 26.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Cartviral Com Authentication
  slug: cartviral-com-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Cartviral Com Domain Security
  slug: cartviral-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: cartviral-com-create-product-clips
  slug: cartviral-com-create-product-clips
slug: cartviral-com
tags:
- Company
- Artificial Intelligence
- E-Commerce
- Video Generation
- Marketing
website: https://cartviral.com/
---
