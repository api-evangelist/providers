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
- group: company
  title: ''
  type: Website
  url: https://www.qunnect.inc/
- group: other
  title: ''
  type: Products
  url: https://www.qunnect.inc/products
- group: company
  title: ''
  type: Blog
  url: https://www.qunnect.inc/blog
- group: operate
  title: ''
  type: Support
  url: https://www.qunnect.inc/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.qunnect.inc/files/privacy-policy.pdf
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Qunnect
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/qunnectinc
- group: auth
  title: ''
  type: DomainSecurity
  url: security/qunnect-domain-security.yml
coverage:
  checked: '2026-08-26'
  detail: Qunnect sells physical quantum-networking hardware — the Qu-Source entangled photon-pair generator, the Qu-Mem quantum memory and the rack-mounted Carina suite — and its five-page marketing site (Home, How it Works, Products, Blog, Contact) has no developer, docs, or API section at all; the software that orchestrates Carina across a live network is Cisco's quantum networking stack, not a Qunnect-published interface.
  evidence:
  - status: 200
    url: https://www.qunnect.inc/
  - status: 200
    url: https://www.qunnect.inc/carina
  - status: 404
    url: https://www.qunnect.inc/openapi.json
  - status: 404
    url: https://api.qunnect.inc/
  - status: 404
    url: https://developer.qunnect.inc/
  - status: 404
    url: https://docs.qunnect.inc/
  - status: 404
    url: https://www.qunnect.inc/llms.txt
  - status: 404
    url: https://www.qunnect.inc/.well-known/agent-card.json
  - status: 200
    url: https://api.github.com/orgs/Qunnect/repos
  reason: not-a-software-company
  state: none
created: '2026-08-26'
description: 'Qunnect Inc. is a quantum networking hardware company headquartered at the Brooklyn Navy Yard in New York, founded in 2017 by Mehdi Namazi and Mael Flament and led by CEO Noel Goddard. Qunnect builds room-temperature, rack-mountable devices that turn existing telecommunications fiber into scalable quantum networks without cryogenics or vacuum systems: the Qu-Source polarization-entangled photon-pair generator, the Qu-Mem atom-based quantum memory, and the turnkey Carina product suite, which combines entangled photon generation, single-photon counting detection and adaptive polarization compensation in a single rack unit for fiber spans up to 100 km. Carina deployments include New York City, Berlin, Montana State University and the ABQ-Net network in New Mexico. Qunnect is backed by Airbus Ventures, Cisco Investments and Quantonation. The company sells physical quantum networking hardware to research, defense and telecommunications customers and publishes no public API, SDK,
  or developer program.'
image: https://kinlane-productions2.s3.amazonaws.com/api-evangelist-site/company/qunnect.png
layout: provider
modified: '2026-08-26'
name: Qunnect
nav: Providers
network: true
overview: 'Qunnect is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Quantum Networking, Quantum Computing, Hardware, and Telecommunications.


  Qunnect''s developer surface includes engineering blog, support, and 6 more developer resources.'
random_paper: 10
score:
  band: minimal
  composite: 6.5
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
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 6.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 13.9
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/qunnect/refs/heads/main/screenshots/qunnect-2026-09-02T152716.png
security:
- kind: domain-security
  name: Qunnect Domain Security
  slug: qunnect-domain-security
  summary_line: TLSv1.3 · HSTS
slug: qunnect
tags:
- Company
- Quantum Networking
- Quantum Computing
- Hardware
- Telecommunications
- Photonics
- Networking
- Deep Tech
website: https://www.qunnect.inc/
---
