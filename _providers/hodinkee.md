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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 25.0
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: 'The agent-callable commerce surface of HODINKEE Shop. Two Model Context Protocol endpoints are served from shop.hodinkee.com and answered a real tools/list anonymously on 2026-08-22: /api/ucp/mcp impl'
  name: HODINKEE Shop Agent Commerce (UCP / MCP)
  slug: hodinkee-shop-agent-commerce-ucp-mcp
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://www.hodinkee.com/
- group: docs
  title: ''
  type: Documentation
  url: https://shop.hodinkee.com/agents.md
- group: agent
  title: ''
  type: MCPServer
  url: mcp/hodinkee-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hodinkee-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/hodinkee-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/hodinkee-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/hodinkee-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/hodinkee-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/hodinkee-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/hodinkee-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/hodinkee-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/hodinkee-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/hodinkee-lifecycle.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/hodinkee-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/hodinkee-packages.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hodinkee-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hodinkee
- group: operate
  title: ''
  type: Support
  url: https://www.hodinkee.com/pages/contact
- group: company
  title: ''
  type: Blog
  url: https://www.hodinkee.com/latest
- group: company
  title: ''
  type: BlogRSS
  url: https://www.hodinkee.com/articles/rss.xml
- group: start
  title: ''
  type: SignUp
  url: https://www.hodinkee.com/signup
- group: start
  title: ''
  type: Login
  url: https://shop.hodinkee.com/account/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.hodinkee.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hodinkee.com/privacy-policy
created: '2026-08-22'
description: 'Hodinkee is a New York-based watch media and e-commerce company founded in 2008, publishing editorial, video and its print Magazine at www.hodinkee.com and selling new and pre-owned watches, straps and accessories through HODINKEE Shop at shop.hodinkee.com. It was acquired by the Watches of Switzerland Group in October 2024. Hodinkee runs no developer program and publishes no OpenAPI, developer portal or API reference. Its one machine-readable integration surface is agentic commerce: the Shopify-hosted store serves a Universal Commerce Protocol merchant profile at /.well-known/ucp and two live, anonymously callable MCP endpoints for catalog search, cart and checkout, advertised from the store''s own robots.txt and llms.txt.'
image: https://www.hodinkee.com/favicon.png
layout: provider
mcp_servers:
- description: HODINKEE Shop (shop.hodinkee.com) exposes two live, anonymously reachable Model Context Protocol endpoints. Both answered a real JSON-RPC tools/list on 2026-08-22 with full inputSchema payloads — no O
  name: HODINKEE Shop MCP
  slug: hodinkee-shop-mcp
modified: '2026-08-22'
name: Hodinkee
nav: Providers
network: true
overview: 'Hodinkee publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Watches, Luxury Goods, E-Commerce, and Media.


  Hodinkee''s developer surface includes documentation, authentication, support, engineering blog, signup flow, and 20 more developer resources.'
plans:
- name: Hodinkee Plans Pricing
  plan_count: 0
  slug: hodinkee-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Hodinkee Rate Limits
  slug: hodinkee-rate-limits
scopes:
- name: Hodinkee Scopes
  scope_count: 0
  slug: hodinkee-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 23.0
  coverage:
    artifact_dirs: 18
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 30.4
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 23.0
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hodinkee/refs/heads/main/screenshots/hodinkee-2026-09-02T145738.png
security:
- kind: authentication
  name: Hodinkee Authentication
  slug: hodinkee-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Hodinkee Domain Security
  slug: hodinkee-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hodinkee
tags:
- Company
- Watches
- Luxury Goods
- E-Commerce
- Media
- Publishing
- Retail
- Agentic Commerce
- MCP
- Shopify
website: https://www.hodinkee.com/
---
