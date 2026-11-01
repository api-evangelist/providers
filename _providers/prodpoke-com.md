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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 5.6
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Paste a URL. ProdPoke launches a real browser to test your site — checking SEO, performance, accessibility, security, and UX. Free to start.
  name: ProdPoke API
  slug: prodpoke-api
artifact_total: 6
common:
- group: agent
  href: https://artifacts.apis.io/prodpoke-com/mcp/prodpoke-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/prodpoke-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/prodpoke-com/hosts/prodpoke-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/prodpoke-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/prodpoke-com/vendors/prodpoke-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/prodpoke-com-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://prodpoke.com/auth/login
- group: auth
  href: https://artifacts.apis.io/prodpoke-com/security/prodpoke-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/prodpoke-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://prodpoke.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://prodpoke.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://prodpoke.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://prodpoke.com/privacy
coverage:
  checked: '2026-10-31'
  detail: No public API documentation or machine‑readable contract was found on prodpoke.com or api.prodpoke.com.
  evidence:
  - status: 404
    url: https://prodpoke.com/openapi.json
  reason: no-developer-program
  state: none
created: '2026-10-31'
description: ProdPoke provides an automated website testing service that runs a real headless browser to evaluate any URL for bugs, SEO issues, performance bottlenecks, accessibility problems, security headers, and overall user‑experience quality. Developers can paste a site URL and receive a detailed QA report covering console errors, visual regressions, form validation, and compliance checks. The platform offers a free tier with five scans and paid credit packs for higher volume testing. It targets indie developers, small teams, and agencies seeking fast, AI‑assisted site audits without manual setup.
image: https://prodpoke.com/opengraph-image-1c1a04?14cb8d430d9b4396
layout: provider
mcp_servers:
- description: Remote MCP server at prodpoke.com requiring an API key.
  name: prodpoke-com MCP Server
  slug: prodpoke-com-mcp-yml
modified: '2026-10-31'
name: prodpoke-com
nav: Providers
network: true
overview: 'prodpoke-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Testing, Automation, QA, Developer Tools, and Web.


  prodpoke-com''s developer surface includes pricing and 8 more developer resources.'
random_paper: 8
rate_limits:
- limit_count: 0
  name: Prodpoke Com Rate Limits
  slug: prodpoke-com-rate-limits
scopes:
- name: Prodpoke Com Scopes
  scope_count: 0
  slug: prodpoke-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 15.9
  coverage:
    artifact_dirs: 19
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 56.7
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 23.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Prodpoke Com Authentication
  slug: prodpoke-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Prodpoke Com Domain Security
  slug: prodpoke-com-domain-security
  summary_line: TLSv1.3
slug: prodpoke-com
tags:
- Testing
- Automation
- QA
- Developer Tools
- Web
website: https://prodpoke.com/
---
