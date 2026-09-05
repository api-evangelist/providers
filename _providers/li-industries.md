---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
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
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/li-industries-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.li-ind.com/
- group: company
  title: ''
  type: About
  url: https://www.li-ind.com/about-us
- group: company
  title: ''
  type: Blog
  url: https://www.li-ind.com/press
- group: company
  title: ''
  type: Careers
  url: https://www.li-ind.com/careers
- group: other
  title: ''
  type: Team
  url: https://www.li-ind.com/team
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/li-industries
coverage:
  checked: '2026-08-25'
  detail: Li Industries manufactures physical lithium-ion battery cathode material and recycling equipment — its entire public web presence is an 8-URL Webflow marketing site (home, about, careers, team, press, two press posts and one job listing, per its own sitemap.xml) with no developer, docs or API page, no GitHub organization, and no api/developer/docs/app/portal subdomain in DNS.
  evidence:
  - status: 200
    url: https://www.li-ind.com/sitemap.xml
  - status: 404
    url: https://www.li-ind.com/openapi.json
  - status: 404
    url: https://www.li-ind.com/.well-known/agent-card.json
  - status: 404
    url: https://www.li-ind.com/llms.txt
  - status: 404
    url: https://api.github.com/orgs/li-industries
  reason: not-a-software-company
  state: none
created: '2026-08-25'
description: 'Li Industries is a critical battery materials company developing next-generation lithium-ion battery recycling and closed-loop materials production technology. Its patented direct recycling process separates and purifies electrode components from spent lithium-ion batteries — including lithium iron phosphate (LFP) chemistries — to produce commercial-grade cathode active material without the environmental cost and poor economics of conventional smelting or hydrometallurgical routes. The company serves battery manufacturers, cathode producers, recyclers and battery collection operations, and in 2024 was selected for a $55 million U.S. Department of Energy award under the Bipartisan Infrastructure Law to advance closed-loop LFP recycling and manufacturing. Li Industries is headquartered in Pineville, North Carolina, with an engineering center in Charlotte, North Carolina and an R&D center in Blacksburg, Virginia. It is a materials and manufacturing company: it ships physical battery
  material, not software, and publishes no public API, SDK or developer program.'
image: https://cdn.prod.website-files.com/5fa2f1a99eac342b40a20eef/5fa2f3238dff3b97b7849b80_logo_li_Industries%20copy.png
layout: provider
modified: '2026-08-25'
name: Li Industries
nav: Providers
network: true
overview: 'Li Industries is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Battery Recycling, Lithium-Ion Batteries, Battery Materials, and Cathode Active Material.


  Li Industries'' developer surface includes engineering blog and 6 more developer resources.'
random_paper: 12
score:
  band: minimal
  composite: 3.8
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 3.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 8.1
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/li-industries/refs/heads/main/screenshots/li-industries-2026-09-02T150247.png
security:
- kind: domain-security
  name: Li Industries Domain Security
  slug: li-industries-domain-security
  summary_line: TLSv1.3 · HSTS
slug: li-industries
tags:
- Company
- Battery Recycling
- Lithium-Ion Batteries
- Battery Materials
- Cathode Active Material
- Circular Economy
- Clean Energy
- Advanced Manufacturing
website: https://www.li-ind.com/
---
