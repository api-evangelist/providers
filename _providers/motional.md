---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 6.7
  scored_at: '2026-07-23'
api_count: 2
apis:
- description: nuScenes is a large-scale public dataset for autonomous driving released by Motional (formerly nuTonomy). It contains 1,000 driving scenes from Boston and Singapore, with full sensor suites (6 cameras
  name: nuScenes Dataset
  slug: nuscenes
- description: Open-source materials for Motional's Automated Vehicle Cybersecurity Development Lifecycle, intended to share AV-industry cybersecurity practices with the broader research and engineering community.
  name: AVCDL - Automated Vehicle Cybersecurity Development Lifecycle
  slug: avcdl
artifact_total: 7
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/motional-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/motional-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://motional.com
- group: company
  title: ''
  type: AboutUs
  url: https://motional.com/about
- group: company
  title: ''
  type: Newsroom
  url: https://motional.com/newsroom
- group: company
  title: ''
  type: News
  url: https://motional.com/news
- group: company
  title: ''
  type: Blog
  url: https://motional.com/news
- group: other
  title: ''
  type: TechnicallySpeaking
  url: https://motional.com/technicallyspeaking
- group: company
  title: ''
  type: PressKit
  url: https://motional.com/press-kit
- group: other
  title: ''
  type: Safety
  url: https://motional.com/safety
- group: other
  title: ''
  type: Technology
  url: https://motional.com/technology
- group: other
  title: ''
  type: Vehicles
  url: https://motional.com/vehicles
- group: other
  title: ''
  type: OpenDataset
  url: https://www.nuscenes.org
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/nutonomy
- group: company
  title: ''
  type: Careers
  url: https://motional.com/careers
- group: operate
  title: ''
  type: Contact
  url: https://motional.com/contact
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/motional
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/motionaldrive
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@MotionalDrive
created: '2026-05-23'
description: Motional is a Boston-headquartered autonomous-vehicle company formed as a joint venture between Hyundai Motor Group and Aptiv. Its core product is an all-electric IONIQ 5 robotaxi built on a Hyundai E-GMP platform with Motional's full Level 4 autonomous driving stack and a sensor suite including lidar, radar, and cameras. Motional operates commercial robotaxi service in Las Vegas in partnership with Uber, Uber Eats, and Lyft, with additional operations in Boston, Pittsburgh, Santa Monica, Singapore, and Seoul. The company's most influential developer artifact is nuScenes, the open large-scale multimodal autonomous-driving dataset originally released by nuTonomy (a Motional predecessor), now a de facto benchmark for 3D perception research. Motional also publishes the nuscenes-devkit Python library and AVCDL cybersecurity development lifecycle materials on GitHub. Motional does not publish a traditional public developer API; the developer surface is research-dataset access plus
  open-source devkits.
finops:
- name: Motional Finops
  service_category: API
  slug: motional-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/motional.png
layout: provider
modified: '2026-05-23'
name: Motional
nav: Providers
network: true
overview: 'Motional publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Autonomous Vehicles, Robotaxi, Self-Driving, Hyundai, and Aptiv.


  Motional''s developer surface includes product news, engineering blog, YouTube channel, and 16 more developer resources.'
plans:
- name: Motional Plans Pricing
  plan_count: 1
  slug: motional-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 2
  name: Motional Rate Limits
  slug: motional-rate-limits
score:
  band: emerging
  composite: 18.9
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 2.2
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 18.9
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/motional/refs/heads/main/screenshots/motional-2026-06-20T185823.png
security:
- kind: domain-security
  name: Motional Domain Security
  slug: motional-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Motional Vulnerability Disclosure
  slug: motional-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: motional
tags:
- Autonomous Vehicles
- Robotaxi
- Self-Driving
- Hyundai
- Aptiv
- Open Dataset
- nuScenes
- Lidar
website: https://motional.com
---
