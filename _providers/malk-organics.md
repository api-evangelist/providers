---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
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
    agent_skills: true
    agentic_access: false
    agentic_commerce: platform
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: documented
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 33.3
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: MALK Organics's agent-facing commerce API, implemented via the Shopify Universal Commerce Protocol (UCP) over MCP and served from MALK's own host. Agents can search and look up the MALK product catalo
  name: MALK Organics Storefront Commerce (UCP / MCP)
  slug: malk-organics-storefront-commerce-ucp-mcp
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://malkorganics.com/
- group: agent
  title: ''
  type: MCPServer
  url: mcp/malk-organics-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/malk-organics-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/malk-organics-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/malk-organics-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/malk-organics-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/malk-organics-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/malk-organics-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/malk-organics-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/malk-organics-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/malk-organics-plans-pricing.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/malk-organics-domain-security.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/malk-organics-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/malk-organics-data-model.yml
- group: docs
  title: ''
  type: Documentation
  url: https://malkorganics.com/agents.md
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://malkorganics.com/policies/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://malkorganics.com/pages/terms-conditions
- group: operate
  title: ''
  type: Support
  url: https://malkorganics.com/pages/contact
- group: company
  title: ''
  type: Blog
  url: https://malkorganics.com/blogs/news
- group: start
  title: ''
  type: SignUp
  url: https://malkorganics.com/account/login
created: '2026-08-25'
description: 'MALK Organics is an Austin, Texas plant-based beverage company founded in 2015, making clean-label organic almond, oat, cashew, coconut and soy milks plus non-dairy creamers with six ingredients or less and no gums, oils or fillers, sold nationwide through Whole Foods, Target, Kroger, Publix, Albertsons, Costco, H-E-B, Sprouts, Wegmans, Erewhon and Amazon. MALK publishes no traditional developer program, but its Shopify-powered direct-to-consumer storefront at malkorganics.com exposes a real, live agent-commerce surface: a Universal Commerce Protocol (UCP) MCP server answering an anonymous tools/list with 13 catalog, cart, checkout and order tools; OpenID Connect / OAuth 2.0 Customer Accounts authentication; a /.well-known/ucp merchant profile; a hand-maintained /llms.txt AI content index authored by MALK marketing; and an /agents.md agent-instructions document. This profile captures that agent-native commerce surface.'
image: https://malkorganics.com/cdn/shop/files/malk_logo.svg
layout: provider
mcp_servers:
- description: ''
  name: MALK Organics MCP Server
  slug: malk-organics-mcp-server
modified: '2026-08-25'
name: MALK Organics
nav: Providers
network: true
overview: 'MALK Organics publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Retail, E-Commerce, and Food and Beverage.


  MALK Organics'' developer surface includes authentication, documentation, support, engineering blog, signup flow, and 16 more developer resources.'
plans:
- name: Malk Organics Plans Pricing
  plan_count: 0
  slug: malk-organics-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 1
  name: Malk Organics Rate Limits
  slug: malk-organics-rate-limits
scopes:
- name: Malk Organics Scopes
  scope_count: 4
  slug: malk-organics-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: thin
  composite: 26.5
  coverage:
    artifact_dirs: 16
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 21.1
  previous_composite: 26.5
  provenance:
    conformance: first-party
    mcp: first-party
    skills: unknown
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/malk-organics/refs/heads/main/screenshots/malk-organics-2026-09-02T150422.png
security:
- kind: authentication
  name: Malk Organics Authentication
  slug: malk-organics-authentication
  summary_line: oauth2/openIdConnect · 1 scheme
- kind: domain-security
  name: Malk Organics Domain Security
  slug: malk-organics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: malk-organics
tags:
- Company
- Consumer
- Retail
- E-Commerce
- Food and Beverage
- Consumer Packaged Goods
- Plant-Based
- Organic
- Direct to Consumer
- Agent Commerce
- MCP
- Shopify
website: https://malkorganics.com/
---
