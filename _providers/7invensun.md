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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/7invensun-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.7invensun.com/
- group: company
  title: ''
  type: Blog
  url: https://www.7invensun.com/newsRepublic
- group: operate
  title: ''
  type: Support
  url: https://www.7invensun.com/lxwm
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.7invensun.com/yszc
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/7invensun
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/7invensun-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/7invensun-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/7invensun-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/7invensun-rate-limits.yml
coverage:
  checked: '2026-09-05'
  detail: The only HTTP API host 7Invensun runs, api.7invensun.com, answers HTTP 401 with the body "请登录" (please log in) on every path including its root and every /.well-known/ path, and no public reference, portal or spec for it is published anywhere — developer., docs. and open.7invensun.com do not resolve, and the aSeeVR device SDK is handed to registered customers and OEM partners from a download center rather than documented publicly.
  evidence:
  - status: 401
    url: https://api.7invensun.com/
  - status: 401
    url: https://api.7invensun.com/v3/api-docs
  - status: 404
    url: https://www.7invensun.com/llms.txt
  - status: 404
    url: https://www.7invensun.com/apis.json
  reason: customer-only-docs
  state: gated
created: '2026-09-05'
description: 7Invensun Technology (Beijing 7invensun Technology Co., Ltd. / 北京七鑫易维信息技术有限公司) is a Beijing-based eye-tracking company founded in 2009 that develops eye-tracking hardware, gaze-estimation algorithms and device SDKs. Its aSee product family spans glasses-style, desktop and high-speed research eye trackers (aSee Glasses, aSee Glasses Elite, aSee Pro, aSee Pro Plus, aSee A series), aSee VR modules embedded in XR headsets, an aSee Mobile developer accessory, and eye-controlled communication aids for people with ALS, high paraplegia and cerebral palsy. The company packages these into solutions for in-vehicle driver monitoring (DMS), spatial computing and XR foveated rendering, phone and tablet gaze interaction, and safety monitoring, and states it serves more than 1,000 customers across research and education, healthcare, energy, transport and aerospace. Its developer surface is a native device SDK distributed from its own download center and through OEM agreements, not a public
  web API.
image: https://img.wanwang.xin/sitefiles10185/10185530/%E7%BD%91%E7%AB%99icon.png
layout: provider
modified: '2026-09-05'
name: 7Invensun Technology
nav: Providers
network: true
overview: '7Invensun Technology is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Eye Tracking, Computer Vision, Artificial Intelligence, and Hardware.


  7Invensun Technology''s developer surface includes engineering blog, support, and 8 more developer resources.'
plans:
- name: 7Invensun Plans Pricing
  plan_count: 0
  slug: 7invensun-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: 7Invensun Rate Limits
  slug: 7invensun-rate-limits
score:
  band: minimal
  composite: 7.9
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 5.3
    commercial_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 3.6
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  schema_version: 0.18.3
  scored_at: '2026-09-05'
security:
- kind: domain-security
  name: 7Invensun Domain Security
  slug: 7invensun-domain-security
  summary_line: TLSv1.3
slug: 7invensun
tags:
- Company
- Eye Tracking
- Computer Vision
- Artificial Intelligence
- Hardware
- Virtual Reality
- Augmented Reality
- Assistive Technology
- Automotive
- China
website: https://www.7invensun.com/
---
