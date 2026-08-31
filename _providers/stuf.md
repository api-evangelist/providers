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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/stuf-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.stufstorage.com/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/stuf-llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.stufstorage.com/blog
- group: operate
  title: ''
  type: Support
  url: https://support.stufstorage.com/hc/en-us/categories/45138030216340-Stuf-Storage-Member-Help-Center
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/stuf-storage
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.stufstorage.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.stufstorage.com/privacy-policy
coverage:
  checked: '2026-08-29'
  detail: Stuf Storage is a consumer self-storage operator with no developer program of any kind — /developers, /developer, /api, /docs, /api-docs, /openapi.json and /swagger.json all return 404 on www.stufstorage.com, the sitemap lists no developer or API page, no api./developer./docs. subdomain resolves in DNS, and the github.com/stuf-storage organization is real but has zero public repos.
  evidence:
  - status: 404
    url: https://www.stufstorage.com/developers
  - status: 404
    url: https://www.stufstorage.com/openapi.json
  - status: 404
    url: https://www.stufstorage.com/.well-known/agent-card.json
  - status: 0
    url: https://api.stufstorage.com/
  - status: 200
    url: https://www.stufstorage.com/llms.txt
  - status: 200
    url: https://github.com/stuf-storage
  reason: no-developer-program
  state: none
created: '2026-08-29'
description: Stuf is a next-generation, tech-enabled self-storage operator that partners with commercial real estate owners to convert underutilized space — basements, garages and retail vacancies — into modern neighborhood storage facilities. Stuf runs 36 facilities across seven US metros (New York City, Los Angeles, the San Francisco Bay Area, Seattle, Atlanta, Boston and Washington, DC). Members search and book units online, pay month-to-month with all-inclusive pricing and no hidden fees, and open facility doors with a digital key issued through the Stuf Member Dashboard. Stuf publishes no public developer program, API, or machine-readable API contract; the one machine-readable surface it does serve is a substantial, actively maintained llms.txt at https://www.stufstorage.com/llms.txt, alongside an AI-crawler-permissive robots.txt.
image: https://www.stufstorage.com/stuf-family-move-in-og.jpg
layout: provider
modified: '2026-08-29'
name: Stuf Storage
nav: Providers
network: true
overview: 'Stuf Storage is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Self Storage, Real-Estate, PropTech, and Logistics.


  Stuf Storage''s developer surface includes engineering blog, support, and 6 more developer resources.'
plans:
- name: Stuf Plans Pricing
  plan_count: 0
  slug: stuf-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Stuf Rate Limits
  slug: stuf-rate-limits
score:
  band: emerging
  composite: 11.7
  coverage:
    artifact_dirs: 5
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 11.7
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: domain-security
  name: Stuf Domain Security
  slug: stuf-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: stuf
tags:
- Company
- Self Storage
- Real-Estate
- PropTech
- Logistics
- Consumer; Marketplace
- Urban Infrastructure
- Internet of Things
website: https://www.stufstorage.com/
---
