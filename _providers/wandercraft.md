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
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wandercraft-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://en.wandercraft.eu/
- group: company
  title: ''
  type: About
  url: https://en.wandercraft.eu/about-us
- group: other
  title: ''
  type: Products
  url: https://en.wandercraft.eu/eve
- group: company
  title: ''
  type: News
  url: https://en.wandercraft.eu/news
- group: company
  title: ''
  type: Blog
  url: https://en.wandercraft.eu/news
- group: company
  title: ''
  type: PressKit
  url: https://en.wandercraft.eu/press-kit
- group: company
  title: ''
  type: Newsletter
  url: https://en.wandercraft.eu/newsletter
- group: other
  title: ''
  type: Research
  url: https://en.wandercraft.eu/ressources-cliniques
- group: operate
  title: ''
  type: Contact
  url: https://en.wandercraft.eu/form
- group: company
  title: ''
  type: Careers
  url: https://www.welcometothejungle.com/en/companies/wandercraft/jobs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Wandercraft
- group: other
  title: ''
  type: OpenSource
  url: https://github.com/Wandercraft
- group: commercial
  title: ''
  type: TermsOfService
  url: https://en.wandercraft.eu/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://en.wandercraft.eu/donnees-personnelles
- group: commercial
  title: ''
  type: LegalNotice
  url: https://en.wandercraft.eu/mentions-legales
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/wandercraft/
- group: company
  title: ''
  type: Twitter
  url: https://x.com/WandercraftHQ
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/channel/UCWmhQuUMF87d-vSrRe1-_9A
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/wandercraft.official/
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/wandercraft.eu/
- group: company
  title: ''
  type: Investors
  url: https://forgeglobal.com/wandercraft_stock/
- group: build
  title: ''
  type: Packages
  url: packages/wandercraft-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/wandercraft-llms.txt
coverage:
  checked: '2026-09-04'
  detail: Wandercraft sells regulated hardware — the Atalante X and Eve self-balancing exoskeletons and the Calvin-40 industrial humanoid — with its control software embedded in the device and no software product sold separately, so there is nothing to expose as an API; the Webflow site's 334-URL sitemap has no developer, API or status page, no api./developer./docs./dev./app./portal. subdomain of wandercraft.eu resolves in DNS at all, and the company's single public GitHub repository is a 2022 maintenance fork of a third-party FTDI C library.
  evidence:
  - status: 404
    url: https://en.wandercraft.eu/openapi.json
  - status: 404
    url: https://en.wandercraft.eu/llms.txt
  - status: 404
    url: https://en.wandercraft.eu/.well-known/agent-card.json
  - status: 404
    url: https://en.wandercraft.eu/graphql
  - status: 404
    url: https://www.wandercraft.eu/apis.json
  - status: 200
    url: https://www.wandercraft.eu/sitemap.xml
  - status: 200
    url: https://github.com/Wandercraft
  reason: not-a-software-company
  state: none
created: '2026-09-04'
description: 'Wandercraft is a robotics company founded in 2012 by Nicolas Simon, Matthieu Masselin and Jean-Louis Constanza, dual-headquartered in Paris and New York with 175+ AI, robotics and industrial staff. It designs, manufactures and sells self-balancing robotic exoskeletons and humanoid robots. Atalante X is a hands-free, self-balancing overground rehabilitation exoskeleton with 12 motors, used in more than 100 rehabilitation and research centers, CE-marked in 2019 and FDA-cleared for stroke (2022), spinal cord injury (2024) and multiple sclerosis (2025). Eve is the personal self-balancing exoskeleton for wheelchair users, FDA-cleared and commercially launching in the United States in 2026. Calvin-40 is the industrial humanoid built on the same full-body control stack for part handling, flow logistics, picking and kitting in factories and warehouses, deployed at Renault''s Douai plant. Renault Group took a stake and joined as industrial partner alongside the June 2025 Series D. Wandercraft
  publishes no public API, developer portal, SDK or machine-readable contract of any kind: the product is regulated medical-device and industrial hardware, its control software is embedded in the device, and its only public code surface is a single maintenance fork of a third-party C library on GitHub.'
image: https://cdn.prod.website-files.com/6a5e1730e4dc3d8a81f2d73d/6a7a06edf834b58b4bb563de_62372edf8e3d0c45948853f5_webclip.png
layout: provider
modified: '2026-09-04'
name: Wandercraft
nav: Providers
network: true
overview: 'Wandercraft is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Robotics, Exoskeleton, Humanoid Robots, and Medical Devices.


  Wandercraft''s developer surface includes product news, engineering blog, YouTube channel, and 21 more developer resources.'
random_paper: 14
score:
  band: minimal
  composite: 10.2
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 5.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
security:
- kind: domain-security
  name: Wandercraft Domain Security
  slug: wandercraft-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: wandercraft
tags:
- Company
- Robotics
- Exoskeleton
- Humanoid Robots
- Medical Devices
- Rehabilitation
- Healthcare
- Physical AI
- Industrial Automation
- Mobility
- Assistive Technology
- Deep Tech
- France
website: https://en.wandercraft.eu/
---
