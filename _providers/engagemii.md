---
agent_readiness:
  band: human-only
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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.5
  scored_at: '2026-10-03'
api_count: 1
apis:
- description: API for Engagemii Citation Watch providing AI visibility scores and data.
  name: Engagemii API
  slug: engagemii-api
artifact_total: 4
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/engagemii/refs/heads/main/plans/engagemii-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/engagemii-plans-pricing.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/engagemii/refs/heads/main/llms/engagemii-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/engagemii-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/engagemii/refs/heads/main/mcp/engagemii-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/engagemii-mcp.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/engagemii/refs/heads/main/hosts/engagemii-hosts.yml
  title: ''
  type: Hosts
  url: hosts/engagemii-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/engagemii/refs/heads/main/vendors/engagemii-vendors.yml
  title: ''
  type: Vendors
  url: vendors/engagemii-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.engagemii.com/
- group: company
  title: ''
  type: Newsroom
  url: https://engagemii.com/aeo/scores/media
- group: start
  title: ''
  type: Login
  url: https://app.engagemii.com/brands/login
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/engagemii/refs/heads/main/security/engagemii-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/engagemii-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://engagemii.com/
- group: docs
  title: ''
  type: Documentation
  url: https://engagemii.com/docs
- group: start
  title: ''
  type: DeveloperPortal
  url: https://engagemii.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://engagemii.com/aeo/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://engagemii.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://engagemii.com/privacy
- group: company
  title: ''
  type: Blog
  url: https://engagemii.com/blog
- group: company
  title: ''
  type: About
  url: https://engagemii.com/about
coverage:
  detail: Documentation pages return a JavaScript challenge preventing machine access.
  evidence:
  - status: 403
    url: https://engagemii.com/docs
  - status: 403
    url: https://engagemii.com/aeo/pricing
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-25'
description: Engagemii Citation Watch provides a free AI visibility scoring platform that tracks and analyzes how businesses appear in AI answer engines. It offers real‑time AEO scores, detailed fix kits, bot monitoring, and a public dataset of AI‑visibility metrics. The service includes a searchable index, research reports, and tools for improving AI‑driven discoverability across the web.
image: https://engagemii.com/opengraph-image?619102bd60f3ff99
layout: provider
mcp_servers:
- description: ''
  name: Engagemii Citation Watch MCP Server
  slug: engagemii-citation-watch-mcp-server
modified: '2026-09-25'
name: Engagemii Citation Watch
nav: Providers
network: true
overview: 'Engagemii Citation Watch publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Visibility, Analytics, and Free.


  Engagemii Citation Watch''s developer surface includes documentation, pricing, engineering blog, and 14 more developer resources.'
plans:
- name: Engagemii Plans Pricing
  plan_count: 2
  slug: engagemii-plans-pricing
random_paper: 10
score:
  band: thin
  composite: 26.7
  coverage:
    artifact_dirs: 8
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 76.7
    operational_transparency: 15.8
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Engagemii Domain Security
  slug: engagemii-domain-security
  summary_line: TLSv1.3 · DMARC
slug: engagemii
tags:
- Company
- Artificial Intelligence
- Visibility
- Analytics
- Free
website: https://engagemii.com/
---
