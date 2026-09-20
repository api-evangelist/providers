---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: platform
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.6
  scored_at: '2026-09-19'
api_count: 1
apis:
- description: The agent-facing commerce surface of the Fruitist (Agrovision) direct-to-consumer store. It is a Universal Commerce Protocol 2026-08-25 service exposed over MCP at https://shop.fruitist.com/api/ucp/mc
  name: Fruitist Store UCP Commerce MCP
  slug: agrovision-ucp-commerce
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://www.fruitist.com/
- group: operate
  title: ''
  type: Contact
  url: https://www.fruitist.com/contact
- group: operate
  title: ''
  type: Support
  url: https://www.fruitist.com/contact
- group: company
  title: ''
  type: Blog
  url: https://www.fruitist.com/news
- group: commercial
  title: ''
  type: TermsOfService
  url: https://shop.fruitist.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://shop.fruitist.com/policies/privacy-policy
- group: start
  title: ''
  type: SignUp
  url: https://shop.fruitist.com/account
- group: commercial
  title: ''
  type: Pricing
  url: https://shop.fruitist.com/collections/all
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/agrovision/refs/heads/main/mcp/agrovision-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/agrovision-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/agrovision/refs/heads/main/llms/agrovision-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agrovision-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/agrovision/refs/heads/main/well-known/agrovision-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agrovision-well-known.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agrovision/refs/heads/main/conformance/agrovision-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agrovision-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/agrovision/refs/heads/main/authentication/agrovision-authentication.yml
  title: ''
  type: Authentication
  url: authentication/agrovision-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/agrovision/refs/heads/main/scopes/agrovision-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/agrovision-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agrovision/refs/heads/main/conventions/agrovision-conventions.yml
  title: ''
  type: Conventions
  url: conventions/agrovision-conventions.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/agrovision/refs/heads/main/rate-limits/agrovision-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/agrovision-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/agrovision/refs/heads/main/plans/agrovision-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/agrovision-plans-pricing.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/agrovision/refs/heads/main/security/agrovision-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agrovision-domain-security.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agrovision/refs/heads/main/lifecycle/agrovision-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/agrovision-lifecycle.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/agrovision/refs/heads/main/packages/agrovision-packages.yml
  title: ''
  type: Packages
  url: packages/agrovision-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/agrovision/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-09-13'
description: 'Agrovision — rebranded to Fruitist in April 2025 — is a vertically integrated premium superfruit company founded in 2012 and headquartered in Century City, California, with a second office in San Isidro, Peru. It farms, packs, ships and markets jumbo blueberries, raspberries, blackberries and cherries across ten microclimates in Peru, Mexico, Morocco, Chile, Oregon, Egypt and China, selling into 12,500+ retail doors in 28 countries through Costco, Walmart, Whole Foods, Trader Joe''s, Sprouts and Wakefern. It is a grower and consumer-brand business, not a software vendor: it publishes no developer program, no API reference and no machine-readable API contract of its own. The one agent-callable surface it operates is its Shopify direct-to-consumer store at shop.fruitist.com, which serves a live Universal Commerce Protocol (UCP) MCP endpoint, an llms.txt/agents.md pair and Shopify customer-account OpenID Connect discovery documents on the company''s own host.'
image: https://cdn.prod.website-files.com/67eb354a3bfe8fdee496f42f/67ec64d28ebae3f8761dd62f_e6fc4a7ca608233e7083f589ede8cac1_og.jpeg
layout: provider
mcp_servers:
- description: ''
  name: Fruitist Store UCP Commerce MCP
  slug: fruitist-store-ucp-commerce-mcp
modified: '2026-09-13'
name: Agrovision
nav: Providers
network: true
overview: 'Agrovision publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Agriculture, Food and Beverage, Consumer Packaged Goods, and Agriculture Technology.


  Agrovision''s developer surface includes support, engineering blog, signup flow, pricing, authentication, and 16 more developer resources.'
plans:
- name: Agrovision Plans Pricing
  plan_count: 0
  slug: agrovision-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 1
  name: Agrovision Rate Limits
  slug: agrovision-rate-limits
scopes:
- name: Agrovision Scopes
  scope_count: 0
  slug: agrovision-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 25.6
  coverage:
    artifact_dirs: 15
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 20.8
    discoverability: 75.9
    operational_transparency: 21.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 25.6
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-19'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Agrovision Authentication
  slug: agrovision-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Agrovision Domain Security
  slug: agrovision-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: agrovision
tags:
- Company
- Agriculture
- Food and Beverage
- Consumer Packaged Goods
- Agriculture Technology
- E-Commerce
- Retail
- Supply Chain
- Agentic Commerce
- Universal Commerce Protocol
website: https://www.fruitist.com/
---
