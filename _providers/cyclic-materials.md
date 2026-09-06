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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cyclic-materials-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cyclicmaterials.earth
- group: company
  title: ''
  type: About
  url: https://cyclicmaterials.earth/about-us
- group: company
  title: ''
  type: Blog
  url: https://cyclicmaterials.earth/resource-center
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cyclicmaterials.earth/privacy-policy
- group: operate
  title: ''
  type: Contact
  url: https://cyclicmaterials.earth/contact
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cyclic-materials/
- group: start
  title: ''
  type: SupplierPortal
  url: https://portal.cyclicmaterials.earth/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://www.hiive.com/securities/cyclic-materials-stock
coverage:
  checked: '2026-08-11'
  detail: Cyclic Materials sells recycled rare earth oxide and copper, not software — its entire public presence is an 85-page Webflow marketing site with no /api, /developers or /docs route, and its only application surface, portal.cyclicmaterials.earth, is an Auth0-gated supplier portal for scrap sellers whose /api/* routes are Next.js auth plumbing rather than a published API.
  evidence:
  - status: 404
    url: https://cyclicmaterials.earth/developers
  - status: 404
    url: https://cyclicmaterials.earth/openapi.json
  - status: 404
    url: https://cyclicmaterials.earth/llms.txt
  - status: 404
    url: https://cyclicmaterials.earth/.well-known/agent-card.json
  - status: 404
    url: https://portal.cyclicmaterials.earth/openapi.json
  - status: 400
    url: https://portal.cyclicmaterials.earth/api/auth/login
  reason: not-a-software-company
  state: none
created: '2026-08-11'
description: 'Cyclic Materials is a Kingston, Ontario cleantech company founded in 2021 that is building a circular supply chain for rare earth elements and other critical materials. It recovers neodymium-praseodymium (NdPr), samarium, gadolinium, terbium and dysprosium from end-of-life magnet-containing products — electric-vehicle motors, wind-turbine generators, MRI machines and e-waste — using its proprietary MagCycle magnet-separation and REEPure refining processes, and supplies recycled mixed rare earth oxide (rMREO) and recycled copper back into automotive, data-centre, defence and energy manufacturing. The company operates a REEPure commercial demonstration plant and a MagCycle pilot in Kingston, with a Centre of Excellence under construction there and campuses planned in Arizona and South Carolina. It is a materials producer, not a software vendor: it publishes no API, SDK, developer portal or machine-readable specification, and its only public application surface is an Auth0-gated
  supplier portal for recyclers, aggregators and core buyers.'
image: https://cdn.prod.website-files.com/6808fc19b9edb865ded52193/681cbe43f986db3eeda7cfc1_favicon-256.png
layout: provider
modified: '2026-08-11'
name: Cyclic Materials
nav: Providers
network: true
overview: 'Cyclic Materials is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Rare Earth Elements, Critical Minerals, Recycling, and Circular Economy.


  Cyclic Materials'' developer surface includes engineering blog and 8 more developer resources.'
random_paper: 0
score:
  band: minimal
  composite: 7.6
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 7.6
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cyclic-materials/refs/heads/main/screenshots/cyclic-materials-2026-09-02T145208.png
security:
- kind: domain-security
  name: Cyclic Materials Domain Security
  slug: cyclic-materials-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cyclic-materials
tags:
- Company
- Rare Earth Elements
- Critical Minerals
- Recycling
- Circular Economy
- Cleantech
- Advanced Materials
- Sustainability
website: https://cyclicmaterials.earth
---
