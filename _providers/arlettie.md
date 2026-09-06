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
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 27.7
  scored_at: '2026-09-05'
api_count: 2
apis:
- description: Live, unauthenticated Model Context Protocol endpoint on the Les échappées storefront implementing the Universal Commerce Protocol (UCP) 2026-04-08. tools/list returns 13 tools with full JSON Schema i
  name: Arlettie Les échappées UCP/MCP Agent Commerce
  slug: arlettie-les-echappees-ucp-mcp
- description: The Shopify Storefront GraphQL API and public JSON endpoints on the Les échappées storefront. Introspection answers unauthenticated at /api/2026-04/graphql.json (424 types; shop.name returns "Arlettie
  name: Arlettie Les échappées Storefront Data API
  slug: arlettie-les-echappees-storefront
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/arlettie-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.arlettie.com/
- group: docs
  title: ''
  type: Documentation
  url: https://lesechappees.arlettie.com/agents.md
- group: company
  title: ''
  type: Blog
  url: https://www.arlettie.com/us/en/articles
- group: operate
  title: ''
  type: Support
  url: https://www.arlettie.com/us/en/contact
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.arlettie.com/us/en/faq
- group: start
  title: ''
  type: SignUp
  url: https://www.arlettie.com/us/en/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.arlettie.com/us/en/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.arlettie.com/us/en/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/arlettie
- group: other
  title: ''
  type: OnlineStore
  url: https://lesechappees.arlettie.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://fr.linkedin.com/company/arlettie
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/arlettieparis/
- group: company
  title: ''
  type: Facebook
  url: https://fr-fr.facebook.com/ArlettieParis
- group: other
  title: ''
  type: Pinterest
  url: https://www.pinterest.fr/arlettieparis/
- group: agent
  title: ''
  type: MCPServer
  url: mcp/arlettie-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/arlettie-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/arlettie-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/arlettie-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/arlettie-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/arlettie-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/arlettie-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/arlettie-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/arlettie-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/arlettie-lifecycle.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/arlettie-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/arlettie-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/arlettie-data-model.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/arlettie-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/arlettie-packages.yml
created: '2026-08-17'
description: 'Arlettie is a Paris-founded (1994) operator of invitation-only luxury and contemporary fashion private sales — "ventes privées" / sample sales — running showroom events in Paris, London, Milan and New York for more than 220 brand partners, alongside its online outlet store "Les échappées". Its machine-readable surface is not a developer program: it is an agent-commerce surface on the Les échappées storefront, which runs on Shopify and therefore serves a live unauthenticated UCP/MCP endpoint, agent instructions at /agents.md and /llms.txt, RFC 8414 + RFC 9728 OAuth discovery documents, and an introspectable Storefront GraphQL API — all on hosts Arlettie controls.'
image: https://static.arlettie.com/website/header-logo-paris.svg
layout: provider
mcp_servers:
- description: ''
  name: Arlettie MCP Server
  slug: arlettie-mcp-server
modified: '2026-08-17'
name: Arlettie
nav: Providers
network: true
overview: 'Arlettie publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Retail, E-Commerce, and Fashion.


  Arlettie''s developer surface includes documentation, engineering blog, support, signup flow, authentication, and 26 more developer resources.'
plans:
- name: Arlettie Plans Pricing
  plan_count: 0
  slug: arlettie-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 2
  name: Arlettie Rate Limits
  slug: arlettie-rate-limits
scopes:
- name: Arlettie Scopes
  scope_count: 4
  slug: arlettie-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: thin
  composite: 27.9
  coverage:
    artifact_dirs: 17
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
    operational_transparency: 31.6
  previous_composite: 27.9
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/arlettie/refs/heads/main/screenshots/arlettie-2026-09-02T144124.png
security:
- kind: authentication
  name: Arlettie Authentication
  slug: arlettie-authentication
  summary_line: none/oauth2/openIdConnect/apiKey · 4 schemes
- kind: domain-security
  name: Arlettie Domain Security
  slug: arlettie-domain-security
  summary_line: TLSv1.3 · HSTS
slug: arlettie
tags:
- Company
- Consumer
- Retail
- E-Commerce
- Fashion
- Luxury
- Private Sales
- Marketplace
- Shopify
- Agent Commerce
- MCP
- UCP
website: https://www.arlettie.com/
---
