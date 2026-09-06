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
- group: company
  title: ''
  type: Website
  url: https://transitionbio.com/
- group: company
  title: ''
  type: About
  url: https://transitionbio.com/about-us/
- group: company
  title: ''
  type: Blog
  url: https://transitionbio.com/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://transitionbio.com/feed/
- group: operate
  title: ''
  type: Support
  url: https://transitionbio.com/contact-us/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/transitionbio
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/transition-bio-inc/
- group: company
  title: ''
  type: Careers
  url: https://transitionbio.com/careers/
- group: company
  title: ''
  type: Partners
  url: https://transitionbio.com/collaborate/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/transition-bio-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/transition-bio-domain-security.yml
coverage:
  checked: '2026-08-30'
  detail: Transition Bio is a preclinical therapeutics developer whose product is drug candidates, not software; its entire web presence is an 11-page WordPress marketing site with no developer section, and every contract-discovery path (/openapi.json, /swagger.json, /api-docs, /graphql, /llms.txt and all seven /.well-known/ paths) returned 404, while api./docs./developer. transitionbio.com are wildcard DNS to the same shared host serving that marketing site.
  evidence:
  - status: 404
    url: https://transitionbio.com/openapi.json
  - status: 404
    url: https://transitionbio.com/swagger.json
  - status: 404
    url: https://transitionbio.com/api-docs
  - status: 404
    url: https://transitionbio.com/graphql
  - status: 404
    url: https://transitionbio.com/llms.txt
  - status: 404
    url: https://transitionbio.com/.well-known/agent-card.json
  - status: 404
    url: https://transitionbio.com/.well-known/api-catalog
  - status: 200
    url: https://transitionbio.com/
  reason: not-a-software-company
  state: none
created: '2026-08-30'
description: 'Transition Bio is a preclinical drug discovery company built on biomolecular condensate science, operating as a joint spin-out of the University of Cambridge and Harvard University with sites in Cambridge, Massachusetts and Cambridge, United Kingdom. The company combines droplet-microfluidics high-throughput molecular screening with a machine learning engine to identify and optimize small molecules that modulate intrinsically disordered proteins and the condensates they form, an approach the company has described as its Condensomics platform. It was seeded in November 2020 and closed a $50 million Series A in June 2022 led by Northpond Ventures with Taiho Ventures, Bristol Myers Squibb and Magnetic Ventures participating, and in November 2025 announced a collaboration with Voyager Therapeutics on small molecules targeting TDP-43 in ALS and frontotemporal dementia. Transition Bio is a therapeutics developer rather than a software or data vendor: it publishes no developer portal,
  no API documentation and no machine-readable API contract on any host it controls.'
image: https://transitionbio.com/wp-content/uploads/2022/04/logo.png
layout: provider
modified: '2026-08-30'
name: Transition Bio
nav: Providers
network: true
overview: 'Transition Bio is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Drug Discovery, Life Sciences, and Machine-Learning.


  Transition Bio''s developer surface includes engineering blog, support, and 9 more developer resources.'
random_paper: 9
score:
  band: minimal
  composite: 5.1
  coverage:
    artifact_dirs: 6
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
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 5.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/transition-bio/refs/heads/main/screenshots/transition-bio-2026-09-02T164130.png
security:
- kind: domain-security
  name: Transition Bio Domain Security
  slug: transition-bio-domain-security
  summary_line: TLSv1.3 · DMARC
slug: transition-bio
tags:
- Company
- Biotechnology
- Drug Discovery
- Life Sciences
- Machine-Learning
- Artificial Intelligence
- Microfluidics
- Proteomics
- Therapeutics
- Neurodegeneration
website: https://transitionbio.com/
---
