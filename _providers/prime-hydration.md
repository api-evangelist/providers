---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: true
    agentic_commerce: platform
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 32.6
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Prime Hydration Agentic Access
  operation_count: 13
  slug: prime-hydration-agentic-access
  summary_line: 13 operations
api_count: 1
apis:
- description: 'The agent-facing commerce surface of the PRIME online store. Served from drinkprime.com, it implements the Universal Commerce Protocol (UCP) shopping service over MCP transport: a discovery document a'
  name: PRIME Storefront Agentic Commerce API (UCP / MCP)
  slug: prime-storefront-agentic-commerce-api-ucp-mcp
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://drinkprime.com/
- group: docs
  title: ''
  type: Documentation
  url: https://drinkprime.com/agents.md
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/prime-hydration-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/prime-hydration-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/prime-hydration-domain-security.yml
- group: operate
  title: ''
  type: Support
  url: https://drinkprime.com/pages/contact-us
- group: company
  title: ''
  type: Blog
  url: https://drinkprime.com/blogs/news
- group: start
  title: ''
  type: Login
  url: https://drinkprime.com/account/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://drinkprime.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://drinkprime.com/policies/privacy-policy
created: '2026-08-26'
description: 'Prime Hydration, LLC is an American beverage company founded in 2022 by Logan Paul and Olajide "KSI" Olatunji, manufacturing sports and hydration drinks, zero-sugar hydration, energy drinks, hydration sticks and protein shakes sold direct-to-consumer at drinkprime.com and through retail distribution across North America, Europe, Australia and the Middle East. Prime is not a software company and publishes no developer program, SDK or REST API. Its machine-readable surface is its own storefront: the drinkprime.com store implements the Universal Commerce Protocol (UCP) natively on Shopify, publishing a UCP merchant profile at /.well-known/ucp, an anonymous MCP endpoint at /api/ucp/mcp exposing thirteen catalog, cart, checkout and order tools, an agent-instruction document at /agents.md mirrored to /llms.txt, and Shopify Customer Accounts OAuth 2.0 / OpenID Connect metadata. Agent-driven purchase is explicitly permitted; agent-completed payment without contemporaneous buyer approval
  is explicitly forbidden.'
image: https://drinkprime.com/cdn/shop/files/PRIME_Social_Sharing_Image_1200x.png?v=1734715820
layout: provider
mcp_servers:
- description: ''
  name: PRIME Storefront UCP Shopping MCP Server
  slug: prime-storefront-ucp-shopping-mcp-server
modified: '2026-08-26'
name: Prime Hydration
nav: Providers
network: true
overview: 'Prime Hydration publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Beverages, Consumer Packaged Goods, Food and Beverage, and Retail.


  Prime Hydration''s developer surface includes documentation, support, engineering blog, and 7 more developer resources.'
plans:
- name: Prime Hydration Plans Pricing
  plan_count: 0
  slug: prime-hydration-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Prime Hydration Rate Limits
  slug: prime-hydration-rate-limits
scopes:
- name: Prime Hydration Scopes
  scope_count: 0
  slug: prime-hydration-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 21.4
  coverage:
    artifact_dirs: 17
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 30.4
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 21.4
  provenance:
    agentic_access: first-party
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/prime-hydration/refs/heads/main/screenshots/prime-hydration-2026-09-02T152025.png
security:
- kind: authentication
  name: Prime Hydration Authentication
  slug: prime-hydration-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Prime Hydration Domain Security
  slug: prime-hydration-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: prime-hydration
tags:
- Company
- Beverages
- Consumer Packaged Goods
- Food and Beverage
- Retail
- E-Commerce
- Direct to Consumer
- Agentic Commerce
- Universal Commerce Protocol
- MCP
- Shopify
- Sports Nutrition
website: https://drinkprime.com/
---
