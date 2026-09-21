---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 8.5
  scored_at: '2026-09-20'
api_count: 1
apis:
- description: An anonymous remote Model Context Protocol endpoint served on Agragene's own host and advertised in the company's llms.txt. Nine tools let an agent read business details, search site content, mint a v
  name: Agragene Site MCP
  slug: site-mcp
artifact_total: 6
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/agragene/refs/heads/main/security/agragene-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agragene-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.agragene.com/
- group: company
  title: ''
  type: About
  url: https://www.agragene.com/about
- group: company
  title: ''
  type: Blog
  url: https://www.agragene.com/news
- group: company
  title: ''
  type: BlogRSS
  url: https://www.agragene.com/blog-feed.xml
- group: operate
  title: ''
  type: FAQ
  url: https://www.agragene.com/faq
- group: operate
  title: ''
  type: Support
  url: mailto:info@agragene.com
- group: company
  title: ''
  type: Careers
  url: https://www.agragene.com/careers
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/agragene/refs/heads/main/llms/agragene-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agragene-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/agragene/refs/heads/main/mcp/agragene-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/agragene-mcp.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/agragene/refs/heads/main/authentication/agragene-authentication.yml
  title: ''
  type: Authentication
  url: authentication/agragene-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agragene/refs/heads/main/conventions/agragene-conventions.yml
  title: ''
  type: Conventions
  url: conventions/agragene-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agragene/refs/heads/main/conformance/agragene-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agragene-conformance.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/agragene/refs/heads/main/plans/agragene-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/agragene-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/agragene/refs/heads/main/rate-limits/agragene-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/agragene-rate-limits.yml
created: '2026-09-12'
description: Agragene is an agricultural biotechnology company using CRISPR-based genome engineering to build Precision-Guided Sterile Insect Technology (pgSIT), a modern evolution of the sterile insect technique that breeds insect lines producing only sterile males. Released into a field, those males mate with wild female crop pests and produce no viable offspring, giving growers season-long local pest suppression without chemical pesticides or irradiation. Founded in San Diego in 2017 and now headquartered in St. Louis, Missouri, the company's first product, KNOCKOUT-SWD, targets Spotted Wing Drosophila — a pest behind more than $500M in annual US berry losses — with a limited launch stated for 2027. Agragene has no developer program and publishes no API product; its only machine-readable surface is an anonymous Wix site MCP endpoint plus a company-authored llms.txt.
image: https://static.wixstatic.com/media/252b8c_d34caf2c23cc4a398147d692f5ee7fc2~mv2.png/v1/fit/w_2500,h_1330,al_c/252b8c_d34caf2c23cc4a398147d692f5ee7fc2~mv2.png
layout: provider
mcp_servers:
- description: Agragene serves a live, unauthenticated remote MCP endpoint at https://www.agragene.com/_api/mcp, advertised in the company's own /llms.txt under an "AI Agent Access" section. An anonymous JSON-RPC in
  name: Agragene Site MCP manifest
  slug: agragene-site-mcp-manifest
modified: '2026-09-12'
name: Agragene
nav: Providers
network: true
overview: 'Agragene publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Agriculture, AgTech, Biotechnology, Gene Editing, and Pest Control.


  Agragene''s developer surface includes engineering blog, FAQ, support, authentication, and 11 more developer resources.'
plans:
- name: Agragene Plans Pricing
  plan_count: 0
  slug: agragene-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Agragene Rate Limits
  slug: agragene-rate-limits
score:
  band: emerging
  composite: 14.0
  coverage:
    artifact_dirs: 11
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 75.9
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 14.0
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 21.3
  schema_version: 0.22.0
  scored_at: '2026-09-20'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Agragene Authentication
  slug: agragene-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Agragene Domain Security
  slug: agragene-domain-security
  summary_line: TLSv1.3 · HSTS
slug: agragene
tags:
- Agriculture
- AgTech
- Biotechnology
- Gene Editing
- Pest Control
- Sustainability
- Food and Beverage
- Life Sciences
- Company
website: https://www.agragene.com/
---
