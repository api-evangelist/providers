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
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 24.7
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: ModRetro's agent-facing commerce API. A remote Model Context Protocol server implementing the Universal Commerce Protocol shopping service (versions 2026-04-08 and 2026-01-23), exposing 13 tools acros
  name: ModRetro Agent Commerce API (UCP over MCP)
  slug: modretro-agent-commerce-api-ucp-over-mcp
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/modretro-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://modretro.com/
- group: docs
  title: ''
  type: Documentation
  url: https://modretro.com/agents.md
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/modretro-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/modretro-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/modretro-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/modretro-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/modretro-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/modretro-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/modretro-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/modretro-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/modretro-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/modretro-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/modretro-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/modretro-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/modretro-changelog.yml
- group: build
  title: ''
  type: Packages
  url: packages/modretro-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/modretro-plans-pricing.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ModRetro
- group: operate
  title: ''
  type: Support
  url: https://support.modretro.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.modretro.com/
- group: operate
  title: ''
  type: Community
  url: https://forums.modretro.com/
- group: company
  title: ''
  type: Blog
  url: https://modretro.com/blogs/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://modretro.com/blogs/blog.atom
- group: commercial
  title: ''
  type: Pricing
  url: https://modretro.com/collections/all
- group: start
  title: ''
  type: SignUp
  url: https://modretro.com/customer_authentication/redirect?locale=en&region_country=US
- group: commercial
  title: ''
  type: TermsOfService
  url: https://modretro.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://modretro.com/policies/privacy-policy
created: '2026-08-26'
description: 'ModRetro Inc. designs and sells modern recreations of classic game consoles — the Chromatic, an FPGA-based Game Boy-compatible handheld, and the M64, a Nintendo 64-style console — along with physical cartridges, controllers and accessories. It is a consumer hardware company, not a software vendor, and it publishes no developer portal, no OpenAPI and no SDKs. It does, however, run a live agent-facing commerce API: its Shopify storefront at modretro.com serves a Universal Commerce Protocol (UCP 2026-04-08) merchant profile at /.well-known/ucp and a remote Model Context Protocol server at /api/ucp/mcp exposing 13 catalog, cart, checkout and order tools, advertised from its own robots.txt, /agents.md and /llms.txt, with idempotency required on checkout completion and an explicit human-approval rule on payment. Separately, ModRetro publishes the Chromatic''s FPGA and MCU design files on GitHub under GPL-3.0 with a dated firmware changelog.'
image: https://modretro.com/cdn/shop/files/MR_SocialShare_ModRetro.png?v=1780328409&width=1200
layout: provider
mcp_servers:
- description: ''
  name: ModRetro MCP Server
  slug: modretro-mcp-server
modified: '2026-08-26'
name: ModRetro
nav: Providers
network: true
overview: 'ModRetro publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer Electronics, Gaming, Retro Gaming, and Hardware.


  ModRetro''s developer surface includes documentation, authentication, changelog, support, engineering blog, pricing, signup flow, and 22 more developer resources.'
plans:
- name: Modretro Plans Pricing
  plan_count: 0
  slug: modretro-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 2
  name: Modretro Rate Limits
  slug: modretro-rate-limits
scopes:
- name: Modretro Scopes
  scope_count: 4
  slug: modretro-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: thin
  composite: 29.9
  coverage:
    artifact_dirs: 17
    catalog_gap: 70.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 30.4
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 39.5
  previous_composite: 29.9
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Modretro Authentication
  slug: modretro-authentication
  summary_line: openIdConnect/oauth2/http · 3 schemes
- kind: domain-security
  name: Modretro Domain Security
  slug: modretro-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: modretro
tags:
- Company
- Consumer Electronics
- Gaming
- Retro Gaming
- Hardware
- E-Commerce
- Agentic Commerce
- MCP
- Universal Commerce Protocol
- Open Source Hardware
website: https://modretro.com/
---
