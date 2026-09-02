---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 5.4
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/inhabitr-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://inhabitr.com/home
- group: company
  title: ''
  type: Blog
  url: https://inhabitr.ai/blog-news
- group: commercial
  title: ''
  type: TermsOfService
  url: https://inhabitr.ai/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://inhabitr.com/privacy-policy
- group: start
  title: ''
  type: SignUp
  url: https://inhabitr.com/register
- group: start
  title: ''
  type: Login
  url: https://inhabitr.com/login
- group: operate
  title: ''
  type: Support
  url: https://inhabitr.ai/contact-us
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/inhabitr-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/inhabitr-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/inhabitr-rate-limits.yml
coverage:
  checked: '2026-08-23'
  detail: Inhabitr ships no developer surface at all — inhabitr.com is a Slim/PHP furniture-rental storefront that 302s /openapi.json, /api-docs, /docs, /graphql and /llms.txt to /home, and inhabitr.ai returns an honest 404 for every one of them, with no api./docs./developer. subdomain resolving on either domain and no github.com/inhabitr organization.
  evidence:
  - status: 302
    url: https://inhabitr.com/openapi.json
  - status: 404
    url: https://inhabitr.ai/openapi.json
  - status: 404
    url: https://inhabitr.ai/llms.txt
  - status: 404
    url: https://inhabitr.ai/.well-known/agent-card.json
  - status: 0
    url: https://api.inhabitr.com/
  reason: no-developer-program
  state: none
created: '2026-08-23'
description: Inhabitr is a Chicago-founded furnishing company that operates an AI-assisted furniture rental and procurement platform for commercial real estate and residential customers. Its business side (inhabitr.ai) furnishes hospitality, multifamily, student housing, short-term rental, co-living, senior living and office properties end to end — design, sourcing, procurement, delivery, installation and asset tracking — while its consumer storefront (inhabitr.com) rents furniture, sets and decor to households on flexible terms with a browser-based Home Designer tool. The company describes real-time connectivity to warehouses, manufacturers and retailers as the "furniture cloud" behind its bidding and fulfillment, but it publishes no public developer program, API documentation, or machine-readable contract of any kind as of this profiling pass.
image: https://inhabitr.ai/logo.png
layout: provider
modified: '2026-08-23'
name: Inhabitr
nav: Providers
network: true
overview: 'Inhabitr is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Furniture Rental, Commercial Real Estate, Property Technology, and Hospitality.


  Inhabitr''s developer surface includes engineering blog, signup flow, support, and 8 more developer resources.'
plans:
- name: Inhabitr Plans Pricing
  plan_count: 0
  slug: inhabitr-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Inhabitr Rate Limits
  slug: inhabitr-rate-limits
score:
  band: minimal
  composite: 10.6
  coverage:
    artifact_dirs: 6
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 17.1
    commercial_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 10.6
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Inhabitr Domain Security
  slug: inhabitr-domain-security
  summary_line: TLSv1.3 · DMARC
slug: inhabitr
tags:
- Company
- Furniture Rental
- Commercial Real Estate
- Property Technology
- Hospitality
- Multifamily
- Interior Design
- Procurement
- E-Commerce
- Furnishing
website: https://inhabitr.com/home
---
