---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://pachama.com'', ''status'': 301, ''note'': ''declared website redirects to https://www.carbon-direct.com/ — a different registrable domain (pachama.com -> carbon-direct.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/carbon-direct/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pachama-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://pachama.com
- group: company
  title: ''
  type: SuccessorWebsite
  url: https://carbon-direct.com
- group: other
  title: ''
  type: AcquisitionAnnouncement
  url: https://www.carbon-direct.com/press/carbon-direct-acquires-pachama
- group: other
  title: ''
  type: Technology
  url: https://pachama.com/technology
- group: other
  title: ''
  type: Marketplace
  url: https://pachama.com/marketplace
- group: other
  title: ''
  type: Projects
  url: https://pachama.com/projects
- group: other
  title: ''
  type: ForBuyers
  url: https://pachama.com/buyers
- group: other
  title: ''
  type: ForProjectDevelopers
  url: https://pachama.com/originators
- group: other
  title: ''
  type: Science
  url: https://pachama.com/science
- group: other
  title: ''
  type: Research
  url: https://pachama.com/research
- group: company
  title: ''
  type: Blog
  url: https://pachama.com/blog
- group: operate
  title: ''
  type: FAQ
  url: https://pachama.com/faq
- group: company
  title: ''
  type: About
  url: https://pachama.com/about
- group: company
  title: ''
  type: Careers
  url: https://pachama.com/careers
- group: company
  title: ''
  type: Press
  url: https://pachama.com/press
- group: operate
  title: ''
  type: Contact
  url: https://pachama.com/contact
- group: build
  title: ''
  type: GitHub
  url: https://github.com/pachama
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/pachama
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/pachamainc
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@pachama
- group: company
  title: ''
  type: CrunchbaseProfile
  url: https://www.crunchbase.com/organization/pachama
created: '2026-05-24'
description: Pachama is a San Francisco–based climate technology company founded in 2018 that built a satellite- and machine-learning-powered platform for monitoring, reporting, and verification (MRV) of nature-based carbon projects — including forest conservation, reforestation, afforestation, and improved forest management. Pachama combined satellite imagery, LiDAR, remote sensing, and deep-learning models to measure aboveground biomass, detect deforestation, and track project performance against verified baselines, surfacing that intelligence through an online marketplace where corporate buyers (including Microsoft, Shopify, Salesforce, Flexport.org, Mercado Libre, Boom Supersonic, and Nespresso) could discover and purchase high-integrity carbon credits. In November 2025, Pachama was acquired by Carbon Direct, and its proprietary digital MRV platform and forest-carbon science team were folded into Carbon Direct's science-backed carbon management offering; pachama.com now redirects to
  carbon-direct.com. Throughout its life as an independent company Pachama operated a buyer marketplace and discussed plans for a partner API to embed project selection and retirement data into third-party products, but never shipped a public, self-service developer API, SDK, or open OpenAPI specification — its GitHub organization contains only forks and archived internal tooling.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pachama.png
layout: provider
modified: '2026-05-24'
name: Pachama
nav: Providers
network: true
overview: 'Pachama is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Carbon Credits, Carbon Removal, Carbon Markets, Nature-Based Solutions, and Forest Carbon.


  Pachama''s developer surface includes engineering blog, FAQ, GitHub presence, YouTube channel, and 19 more developer resources.'
random_paper: 1
score:
  band: minimal
  composite: 5.7
  coverage:
    artifact_dirs: 3
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
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 5.7
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pachama/refs/heads/main/screenshots/pachama-2026-06-20T191321.png
security:
- kind: domain-security
  name: Pachama Domain Security
  slug: pachama-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: pachama
tags:
- Carbon Credits
- Carbon Removal
- Carbon Markets
- Nature-Based Solutions
- Forest Carbon
- Reforestation
- Afforestation
- REDD Plus
- MRV
- Monitoring Reporting Verification
- Satellite Imagery
- Remote Sensing
- Machine-Learning
- Biomass Estimation
- Climate Tech
- Sustainability
- ESG
- Voluntary Carbon Market
website: https://pachama.com
---
