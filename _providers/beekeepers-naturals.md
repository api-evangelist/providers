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
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 33.6
  scored_at: '2026-09-05'
api_count: 2
apis:
- description: 'Agent-facing commerce API for the Beekeeper''s Naturals storefront, exposed over the Model Context Protocol as the Universal Commerce Protocol (UCP) Shopping service. The endpoint is advertised by the '
  name: Beekeeper's Naturals UCP Shopping MCP API
  slug: beekeepers-naturals-ucp-shopping-mcp
- description: 'Read-only JSON representations of the Beekeeper''s Naturals storefront catalog, documented by the store''s own agent instructions: product detail at /products/{handle}.json and collection listings at /c'
  name: Beekeeper's Naturals Storefront Product JSON
  slug: beekeepers-naturals-storefront-json
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://www.beekeepersnaturals.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.beekeepersnaturals.com/agents.md
- group: docs
  title: ''
  type: Documentation
  url: https://www.beekeepersnaturals.com/agents.md
- group: docs
  title: ''
  type: APIReference
  url: https://ucp.dev/2026-04-08/services/shopping/mcp.openrpc.json
- group: start
  title: ''
  type: GettingStarted
  url: https://www.beekeepersnaturals.com/agents.md
- group: operate
  title: ''
  type: Support
  url: https://help.beekeepersnaturals.com/en-US
- group: company
  title: ''
  type: Blog
  url: https://www.beekeepersnaturals.com/blogs/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.beekeepersnaturals.com/collections/all
- group: start
  title: ''
  type: SignUp
  url: https://www.beekeepersnaturals.com/account/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.beekeepersnaturals.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.beekeepersnaturals.com/policies/privacy-policy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/beekeepers-naturals-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/beekeepers-naturals-well-known.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/beekeepers-naturals-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/beekeepers-naturals-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/beekeepers-naturals-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/beekeepers-naturals-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/beekeepers-naturals-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/beekeepers-naturals-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/beekeepers-naturals-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/beekeepers-naturals-domain-security.yml
created: '2026-08-02'
description: 'Beekeeper''s Naturals is a direct-to-consumer bee-derived wellness and supplement brand founded in 2017 by Carly Stein Kremer, selling propolis throat sprays, B.LXR royal-jelly brain fuel, superfood honey, bee pollen and kids'' immunity products through beekeepersnaturals.com and retail partners. The company has no traditional developer program, but its Shopify-hosted storefront publishes a genuine machine-readable agent surface: a Universal Commerce Protocol (UCP) merchant profile at /.well-known/ucp, a live MCP endpoint at /api/ucp/mcp implementing the UCP Shopping service (catalog search, cart, checkout, order), an agent instruction document at /agents.md mirrored to /llms.txt, an agentic-discovery sitemap, OIDC/OAuth discovery for Shopify customer accounts, and read-only storefront product/collection JSON endpoints.'
image: https://www.beekeepersnaturals.com/cdn/shop/files/BestSeller-1200x630.webp?v=1776441784
layout: provider
mcp_servers:
- description: ''
  name: Beekeeper's Naturals MCP Server
  slug: beekeepers-naturals-mcp-server
modified: '2026-08-02'
name: Beekeeper's Naturals
nav: Providers
network: true
overview: 'Beekeeper''s Naturals publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Retail, E-Commerce, Consumer Packaged Goods, and Health and Wellness.


  Beekeeper''s Naturals'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 15 more developer resources.'
random_paper: 17
scopes:
- name: Beekeepers Naturals Scopes
  scope_count: 4
  slug: beekeepers-naturals-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: thin
  composite: 36.6
  coverage:
    artifact_dirs: 13
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 64.3
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 36.6
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 52.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/beekeepers-naturals/refs/heads/main/screenshots/beekeepers-naturals-2026-08-07T162251.png
security:
- kind: authentication
  name: Beekeepers Naturals Authentication
  slug: beekeepers-naturals-authentication
  summary_line: openIdConnect/oauth2/none · 3 schemes
- kind: domain-security
  name: Beekeepers Naturals Domain Security
  slug: beekeepers-naturals-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: beekeepers-naturals
tags:
- Company
- Retail
- E-Commerce
- Consumer Packaged Goods
- Health and Wellness
- Supplements
- Shopify
- Agentic Commerce
- Universal Commerce Protocol
- MCP
website: https://www.beekeepersnaturals.com/
---
