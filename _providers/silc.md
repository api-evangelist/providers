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
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/silc-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/silc-llms.txt
- group: company
  title: ''
  type: Website
  url: https://silc.com/
- group: company
  title: ''
  type: About
  url: https://silc.com/about-us/
- group: other
  title: ''
  type: Products
  url: https://silc.com/products/
- group: company
  title: ''
  type: Blog
  url: https://silc.com/press-releases/
- group: company
  title: ''
  type: BlogFeeds
  url: https://silc.com/feed/
- group: company
  title: ''
  type: News
  url: https://silc.com/silc-in-the-news/
- group: other
  title: ''
  type: Events
  url: https://silc.com/events/
- group: operate
  title: ''
  type: ContactUs
  url: https://silc.com/contact-us/
- group: company
  title: ''
  type: Careers
  url: https://silc.com/join-us/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://silc.com/privacy-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/silctech/
coverage:
  checked: '2026-08-05'
  detail: SiLC Technologies is a silicon-photonics LiDAR chipmaker whose entire public web presence is a 15-page WordPress marketing site (sitemap enumerated) with no developers, docs, support, downloads or SDK page, and no docs./developer./api. subdomain in DNS; product briefs are handed out through a "Request Product Brief" sales form rather than a developer portal.
  evidence:
  - status: 404
    url: https://silc.com/developers/
  - status: 404
    url: https://silc.com/openapi.json
  - status: 404
    url: https://silc.com/.well-known/agent-card.json
  - status: 404
    url: https://silc.com/llms.txt
  - status: 200
    url: https://silc.com/wp-sitemap-posts-page-1.xml
  reason: no-developer-program
  state: none
created: '2026-08-05'
description: 'SiLC Technologies is a silicon photonics company headquartered in Monrovia, California that builds integrated single-chip FMCW (frequency-modulated continuous-wave) LiDAR — coherent 4D vision systems that capture depth, instantaneous velocity via micro-Doppler, and dual-polarization intensity from one photonic chip. Its Eyeonic product family spans Eyeonic Trace Ultra (a Class 1 laser line scanner for industrial automation and inspection), Eyeonic Vista (an ultra-long-range perimeter security and counter-UAS vision system with detection beyond 2 km), and Eyeonic Edge (high-precision 4D inspection of large objects). The company sells sensors, modules and vision chips to industrial and AI robotics, perimeter security, and mobility customers. It was founded by Dr. Mehdi Asghari and is backed in part by Honda. SiLC ships hardware, not software services: as of this profile it publishes no public developer program, API, SDK, documentation portal, or machine-readable specification.'
image: https://silc.com/wp-content/uploads/2026/04/LOGO.png
layout: provider
modified: '2026-08-05'
name: SiLC
nav: Providers
network: true
overview: 'SiLC is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Silicon Photonics, LiDAR, Machine Vision, and Sensors.


  SiLC''s developer surface includes engineering blog, product news, and 11 more developer resources.'
random_paper: 7
score:
  band: minimal
  composite: 5.5
  coverage:
    artifact_dirs: 3
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
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
  previous_composite: 5.5
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Silc Domain Security
  slug: silc-domain-security
  summary_line: TLSv1.3 · DMARC
slug: silc
tags:
- Company
- Silicon Photonics
- LiDAR
- Machine Vision
- Sensors
- Semiconductors
- Robotics
- Perimeter Security
- Computer-Vision
- Hardware
website: https://silc.com/
---
