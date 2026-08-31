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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/usa-rare-earth-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.usare.com/
- group: company
  title: ''
  type: About
  url: https://www.usare.com/about/
- group: operate
  title: ''
  type: Contact
  url: https://www.usare.com/contact/
- group: company
  title: ''
  type: Newsroom
  url: https://www.usare.com/newsroom/
- group: operate
  title: ''
  type: PressReleases
  url: https://investors.usare.com/news-events/news-releases
- group: company
  title: ''
  type: BlogFeeds
  url: https://www.usare.com/feed/
- group: company
  title: ''
  type: Investors
  url: https://investors.usare.com/
- group: company
  title: ''
  type: Careers
  url: https://careers.usare.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/usarareearth
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.usare.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.usare.com/standard-terms-and-conditions-of-usa-rare-earth-llc/
coverage:
  checked: '2026-08-05'
  detail: USA Rare Earth makes physical goods — sintered NdFeB magnets and rare earth oxides/metals — and www.usare.com is a WordPress marketing site whose only machine-readable endpoint is the /wp-json index; every spec and /.well-known/ path 404s and the site's own WordPress REST content routes answer 401 rest_forbidden, so there is no developer surface to profile.
  evidence:
  - status: 404
    url: https://www.usare.com/openapi.json
  - status: 404
    url: https://www.usare.com/.well-known/agent-card.json
  - status: 401
    url: https://www.usare.com/wp-json/wp/v2/posts
  - status: 404
    url: https://www.usare.com/llms.txt
  - status: 404
    url: https://investors.usare.com/llms.txt
  reason: not-a-software-company
  state: none
created: '2026-08-05'
description: 'USA Rare Earth, Inc. (Nasdaq: USAR) is an American critical-minerals and advanced-materials company building a domestic mine-to-magnet rare earth supply chain. It operates a 310,000 sq. ft. sintered neodymium-iron-boron (NdFeB) permanent magnet manufacturing facility in Stillwater, Oklahoma, and holds the Round Top heavy rare earth and critical minerals deposit in Hudspeth County, West Texas. The company produces rare earth elements, oxides, metals and sintered permanent magnets for defense, automotive, robotics, industrial and clean-energy customers, with the stated aim of reducing U.S. dependence on offshore rare earth processing and magnet production. It is a materials producer and manufacturer, not a software or data company, and publishes no public developer program, API, or machine-readable interface.'
image: https://www.usare.com/wp-content/uploads/2026/03/usare-main-logo.png
layout: provider
modified: '2026-08-05'
name: USA Rare Earth
nav: Providers
network: true
overview: USA Rare Earth is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Rare Earth, Critical Minerals, Advanced Materials, and Permanent Magnets.
random_paper: 12
score:
  band: minimal
  composite: 9.1
  coverage:
    artifact_dirs: 2
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 9.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 18.9
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: domain-security
  name: Usa Rare Earth Domain Security
  slug: usa-rare-earth-domain-security
  summary_line: TLSv1.3 · DMARC
slug: usa-rare-earth
tags:
- Company
- Rare Earth
- Critical Minerals
- Advanced Materials
- Permanent Magnets
- Mining
- Manufacturing
- Supply Chain
- Defense
- Energy
website: https://www.usare.com/
---
