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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/2eyesvision-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.2eyesvision.com/
- group: company
  title: ''
  type: Blog
  url: https://www.2eyesvision.com/2eyes-knowledge-hub/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.2eyesvision.com/feed/
- group: operate
  title: ''
  type: Support
  url: https://www.2eyesvision.com/contact/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.2eyesvision.com/privacy-policy/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/2eyesvision-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/2eyesvision-plans-pricing.yml
coverage:
  checked: '2026-09-05'
  detail: 2EyesVision sells SimVis Gekko, a CE/UKCA/FCC-marked binocular visual simulator controlled from a wireless iPad, as a finished clinical instrument - the whole public site, including the provider's own 240-line llms.txt page index, contains zero occurrences of the word "API", there is no developer, docs or api subdomain (all NXDOMAIN), no GitHub organization, and no package on any registry.
  evidence:
  - status: 200
    url: https://www.2eyesvision.com/llms.txt
  - status: 404
    url: https://www.2eyesvision.com/openapi.json
  - status: 404
    url: https://www.2eyesvision.com/.well-known/api-catalog
  - status: 404
    url: https://api.github.com/orgs/2eyesvision
  reason: no-developer-program
  state: none
created: '2026-09-05'
description: '2EyesVision (2Eyes Vision, S.L.) is a Madrid, Spain based ophthalmic and optical technologies company, founded as a spin-off of the Spanish National Research Council (CSIC) out of the Visual Optics and Biophotonics Lab. It designs, manufactures and sells SimVis Gekko, a binocular visual simulator built on tunable liquid-lens temporal multiplexing that lets a patient experience premium presbyopia and cataract corrections - monofocal, EDOF, trifocal, monovision and mix-and-match intraocular lens designs - before implantation or refractive surgery. The device is CE, UKCA and FCC marked, is controlled from a wireless iPad, is cloud-connected for remote app and lens-simulation updates, and is distributed across 18 countries on 4 continents. 2EyesVision publishes no public API, SDK, webhook surface or developer program: the product is an end-user clinical instrument, and the only machine-readable document it serves is an SEO-generated llms.txt.'
image: https://www.2eyesvision.com/wp-content/uploads/2023/02/2EyesVision_-Isotipo-sobre-naranja-evo.jpeg
layout: provider
modified: '2026-09-05'
name: 2Eyes Vision
nav: Providers
network: true
overview: '2Eyes Vision is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical Devices, Ophthalmology, Vision Care, and Optics.


  2Eyes Vision''s developer surface includes engineering blog, support, and 6 more developer resources.'
plans:
- name: 2Eyesvision Plans Pricing
  plan_count: 0
  slug: 2eyesvision-plans-pricing
random_paper: 18
score:
  band: minimal
  composite: 8.3
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 12.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
security:
- kind: domain-security
  name: 2Eyesvision Domain Security
  slug: 2eyesvision-domain-security
  summary_line: TLSv1.3
slug: 2eyesvision
tags:
- Company
- Medical Devices
- Ophthalmology
- Vision Care
- Optics
- Health
- Simulation
- Spain
website: https://www.2eyesvision.com/
---
