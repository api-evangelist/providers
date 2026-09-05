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
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://www.vatn.com/
- group: company
  title: ''
  type: About
  url: https://www.vatn.com/about
- group: company
  title: ''
  type: Blog
  url: https://www.vatn.com/news
- group: operate
  title: ''
  type: Support
  url: https://www.vatn.com/contact
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Vatn-Systems
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/vatnsystems/
- group: company
  title: ''
  type: Twitter
  url: https://x.com/vatnsystems
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vatn-systems-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/vatn-systems-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/vatn-systems-plans-pricing.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/vatn-systems-llms.txt
coverage:
  checked: '2026-09-02'
  detail: Vatn's FUSE product page advertises an "Open source protocol for pushing results into custom topside applications" and PARse is offered as a third-party integration license, but neither protocol, schema nor repository is published anywhere - github.com/Vatn-Systems has zero public repos - and the only route to either is the "Request a Demo" / "Contact Sales" / "Become a Supplier" Google Form on a Webflow marketing site with no developer section.
  evidence:
  - status: 200
    url: https://www.vatn.com/fuse-data-fusion
  - status: 404
    url: https://www.vatn.com/openapi.json
  - status: 404
    url: https://www.vatn.com/.well-known/agent-card.json
  - status: 404
    url: https://www.vatn.com/llms.txt
  - status: 200
    url: https://api.github.com/orgs/Vatn-Systems/repos
  reason: sales-gate
  state: gated
created: '2026-09-02'
description: Vatn Systems is a Bristol, Rhode Island defense technology company founded in 2023 that designs and manufactures low-cost, modular autonomous underwater vehicles (UUVs/AUVs) and the autonomy, navigation and acoustic-processing software that runs on them. Its product line spans the Skelmir S6 (6-inch, man-portable, swarm-capable) and Skelmir S12 (12.75-inch medium-class) vehicles, Eyra 5.1 and Eyra 8.0 passive hydrophone arrays, and four software systems - INStinct (maritime inertial navigation for GPS-denied operation), PARse (embedded acoustic signal processing on ARM), FUSE (multi-sensor tracking, distributed as a Docker image) and AEsir (TAK-native sensor fusion and mission planning). Mission planning is delivered through an ATAK/CivTAK/MilTAK/WinTAK plugin and Fathom, a browser-based mission planner and vehicle configurator. Vatn raised a $60M Series A in December 2025 (total funding $76.5M) and acquired Crewless Marine. It publishes no public developer portal, API reference
  or machine-readable contract; every integration surface is reached through a demo request or supplier form.
image: https://cdn.prod.website-files.com/69e61f7946f26d81602ead45/6a23169440288fd66c322f74_webclip-vatn.jpg
layout: provider
modified: '2026-09-02'
name: Vatn Systems
nav: Providers
network: true
overview: 'Vatn Systems is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Defense, Autonomous Systems, Maritime, and Robotics.


  Vatn Systems'' developer surface includes engineering blog, support, and 9 more developer resources.'
plans:
- name: Vatn Systems Plans Pricing
  plan_count: 0
  slug: vatn-systems-plans-pricing
random_paper: 18
score:
  band: minimal
  composite: 9.3
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 18.2
    operational_transparency: 5.3
  previous_composite: 9.3
  provenance:
    conformance: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
security:
- kind: domain-security
  name: Vatn Systems Domain Security
  slug: vatn-systems-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: vatn-systems
tags:
- Company
- Defense
- Autonomous Systems
- Maritime
- Robotics
- Underwater Vehicles
- Navigation
- Sensor Fusion
- Hardware
website: https://www.vatn.com/
---
