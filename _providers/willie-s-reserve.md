---
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
    error_semantics: false
    event_surface_described: false
    idempotency: derived
    mcp_server: platform
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.8
  scored_at: '2026-09-25'
api_count: 1
apis:
- description: A live Model Context Protocol server implementing the Universal Commerce Protocol shopping service for the Willie's Reserve store. Thirteen tools cover catalog search and lookup, cart lifecycle, check
  name: Willie's Reserve Commerce Agent API (UCP/MCP)
  slug: willies-reserve-commerce-agent-api-ucpmcp
artifact_total: 7
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/willie-s-reserve/refs/heads/main/security/willie-s-reserve-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/willie-s-reserve-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://williesreserve.com/
- group: docs
  title: ''
  type: Documentation
  url: https://williesreserve.com/agents.md
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/willie-s-reserve/refs/heads/main/mcp/willie-s-reserve-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/willie-s-reserve-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/willie-s-reserve/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/willie-s-reserve/refs/heads/main/llms/willie-s-reserve-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/willie-s-reserve-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/willie-s-reserve/refs/heads/main/well-known/willie-s-reserve-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/willie-s-reserve-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/willie-s-reserve/refs/heads/main/authentication/willie-s-reserve-authentication.yml
  title: ''
  type: Authentication
  url: authentication/willie-s-reserve-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/willie-s-reserve/refs/heads/main/scopes/willie-s-reserve-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/willie-s-reserve-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/willie-s-reserve/refs/heads/main/conformance/willie-s-reserve-conformance.yml
  title: ''
  type: Conformance
  url: conformance/willie-s-reserve-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/willie-s-reserve/refs/heads/main/conventions/willie-s-reserve-conventions.yml
  title: ''
  type: Conventions
  url: conventions/willie-s-reserve-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/willie-s-reserve/refs/heads/main/conventions/willie-s-reserve-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/willie-s-reserve-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/willie-s-reserve/refs/heads/main/data-model/willie-s-reserve-data-model.yml
  title: ''
  type: DataModel
  url: data-model/willie-s-reserve-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/willie-s-reserve/refs/heads/main/lifecycle/willie-s-reserve-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/willie-s-reserve-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/willie-s-reserve/refs/heads/main/rate-limits/willie-s-reserve-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/willie-s-reserve-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/willie-s-reserve/refs/heads/main/plans/willie-s-reserve-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/willie-s-reserve-plans-pricing.yml
- group: operate
  title: ''
  type: Support
  url: https://williesreserve.com/pages/contact
- group: company
  title: ''
  type: Blog
  url: https://williesreserve.com/blogs/news
- group: commercial
  title: ''
  type: TermsOfService
  url: https://williesreserve.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://williesreserve.com/policies/privacy-policy
created: '2026-09-04'
description: 'Willie''s Reserve is the cannabis brand founded around Willie Nelson''s name and legacy, selling premium cannabis products direct to consumers from williesreserve.com. It is a consumer products company rather than a software vendor, and it publishes no developer program, no OpenAPI and no SDKs. It does, however, operate a real and unusually complete agent commerce surface: a live, anonymously reachable Model Context Protocol endpoint at /api/ucp/mcp implementing the Universal Commerce Protocol shopping service, a machine-readable UCP merchant profile at /.well-known/ucp, an /agents.md instruction document mirrored at /llms.txt, a dedicated agentic-discovery sitemap, and robots.txt policy language requiring human approval before any agent completes a payment.'
image: https://williesreserve.com/cdn/shop/files/Willies_Reserve_Logo_Registered_3b1bc386-c7d8-4a5e-bba7-06a4c76be9e4.png?v=1773762321
layout: provider
mcp_servers:
- description: Willie's Reserve serves a live, anonymously reachable Model Context Protocol server at https://williesreserve.com/api/ucp/mcp implementing the Universal Commerce Protocol (UCP) shopping service. A too
  name: Willie's Reserve Commerce MCP Server (UCP)
  slug: willies-reserve-commerce-mcp-server-ucp
modified: '2026-09-04'
name: Willie's Reserve
nav: Providers
network: true
overview: 'Willie''s Reserve publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cannabis, Consumer Products, Retail, and E-Commerce.


  Willie''s Reserve''s developer surface includes documentation, authentication, support, engineering blog, and 16 more developer resources.'
plans:
- name: Willie S Reserve Plans Pricing
  plan_count: 0
  slug: willie-s-reserve-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Willie S Reserve Rate Limits
  slug: willie-s-reserve-rate-limits
scopes:
- name: Willie S Reserve Scopes
  scope_count: 0
  slug: willie-s-reserve-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 23.8
  coverage:
    artifact_dirs: 15
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 2.7
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 75.0
    operational_transparency: 0.0
  previous_composite: 21.1
  provenance:
    conformance: first-party
    mcp: platform-generated
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Willie S Reserve Authentication
  slug: willie-s-reserve-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Willie S Reserve Domain Security
  slug: willie-s-reserve-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: willie-s-reserve
tags:
- Company
- Cannabis
- Consumer Products
- Retail
- E-Commerce
- Agentic Commerce
- MCP
- Universal Commerce Protocol
- Shopify
website: https://williesreserve.com/
---
