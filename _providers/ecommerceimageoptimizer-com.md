---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 36.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://ecommerceimageoptimizer.com
  baseurl_source: declared
  description: Resize, compress and watermark product images via a synchronous API.
  name: Ecom Image Optimizer API
  slug: ecom-image-optimizer-api
artifact_total: 5
common:
- group: commercial
  href: https://artifacts.apis.io/ecommerceimageoptimizer-com/plans/ecommerceimageoptimizer-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ecommerceimageoptimizer-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/ecommerceimageoptimizer-com/vocabulary/ecommerceimageoptimizer-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/ecommerceimageoptimizer-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/ecommerceimageoptimizer-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/ecommerceimageoptimizer-com/conformance/ecommerceimageoptimizer-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ecommerceimageoptimizer-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/ecommerceimageoptimizer-com/mcp/ecommerceimageoptimizer-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/ecommerceimageoptimizer-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/ecommerceimageoptimizer-com/well-known/ecommerceimageoptimizer-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ecommerceimageoptimizer-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/ecommerceimageoptimizer-com/hosts/ecommerceimageoptimizer-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ecommerceimageoptimizer-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/ecommerceimageoptimizer-com/vendors/ecommerceimageoptimizer-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ecommerceimageoptimizer-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ecommerceimageoptimizer.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ecommerceimageoptimizer.com/privacy
- group: auth
  href: https://artifacts.apis.io/ecommerceimageoptimizer-com/security/ecommerceimageoptimizer-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ecommerceimageoptimizer-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ecommerceimageoptimizer.com/
- group: docs
  title: ''
  type: Documentation
  url: https://ecommerceimageoptimizer.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://ecommerceimageoptimizer.com/pricing
- group: start
  title: ''
  type: GettingStarted
  url: https://ecommerceimageoptimizer.com/tools
- group: docs
  title: ''
  type: APIReference
  url: https://ecommerceimageoptimizer.com/docs
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://ecommerceimageoptimizer.com/v1/openapi.json
  - status: 401
    url: https://ecommerceimageoptimizer.com/api/mcp
  - status: 200
    url: https://ecommerceimageoptimizer.com/
  reason: partner-login
  state: gated
created: '2026-11-06'
description: Ecom Image Optimizer provides a free API for e‑commerce platforms to resize, compress, watermark and convert product images. It supports formats like WebP and AVIF, offers batch processing, presets, and metadata optimization. The service targets Shopify, Amazon, Etsy, PrestaShop, and other online stores, delivering up to 500 free calls per month with bearer‑key authentication and an OpenAPI 3.1 specification.
image: https://ecommerceimageoptimizer.com/opengraph-image?8302a2083b758cbb
layout: provider
mcp_servers:
- description: Remote MCP server at ecommerceimageoptimizer.com requiring an API key.
  name: Ecom Image Optimizer MCP Server
  slug: ecommerceimageoptimizer-com-mcp-yml
modified: '2026-11-06'
name: Ecom Image Optimizer
nav: Providers
network: true
overview: 'Ecom Image Optimizer is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Image Optimization, E-Commerce, Free, and OpenAPI.


  Ecom Image Optimizer''s developer surface includes documentation, pricing, getting-started guide, API reference, and 12 more developer resources.'
plans:
- name: Ecommerceimageoptimizer Com Plans Pricing
  plan_count: 6
  slug: ecommerceimageoptimizer-com-plans-pricing
random_paper: 10
score:
  band: thin
  composite: 35.2
  coverage:
    artifact_dirs: 13
    catalog_earned: 45.3
    catalog_earned_first_party: 12.0
    catalog_gap: 69.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 8.3
    contract_quality: 33.7
    developer_ergonomics: 30.4
    discoverability: 56.7
    operational_transparency: 0.0
  provenance:
    conformance: derived
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Ecommerceimageoptimizer Com Domain Security
  slug: ecommerceimageoptimizer-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: optimize-image
  slug: ecommerceimageoptimizer-com-optimize-image
slug: ecommerceimageoptimizer-com
tags:
- Image Optimization
- E-Commerce
- Free
- OpenAPI
website: https://ecommerceimageoptimizer.com/
---
