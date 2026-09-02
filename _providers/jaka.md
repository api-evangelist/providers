---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jaka-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.jaka.com/en/index
created: '2026-07-17'
description: JAKA (Shanghai JAKA Robotics Co., Ltd.) is a collaborative robot (cobot) manufacturer founded in 2014 and headquartered in Shanghai, China, with origins in robotics research at Shanghai University. The company designs and builds lightweight, human-collaborative industrial robot arms — including its JAKA Zu series and MiniCobo — used across manufacturing, 3C electronics, automotive, healthcare, education, and commercial service applications. JAKA robots are programmed through the company's on-device control software and a robot SDK (C++/Python) that communicates with the robot controller over TCP/IP on the local network, rather than a public cloud web API. As of this profile JAKA does not publish a public developer portal, OpenAPI definition, or hosted REST/MCP API surface; this repository is a company profile in the API Evangelist network.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/jaka.png
layout: provider
modified: '2026-07-19'
name: JAKA
nav: Providers
network: true
overview: JAKA is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Frontier Tech, Robotics, Collaborative Robots, and Cobots.
random_paper: 8
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 2
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.0
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/jaka/refs/heads/main/screenshots/jaka-2026-07-25T223052.png
security:
- kind: domain-security
  name: Jaka Domain Security
  slug: jaka-domain-security
  summary_line: TLSv1.3 · DMARC
slug: jaka
tags:
- Company
- Frontier Tech
- Robotics
- Collaborative Robots
- Cobots
- Industrial Automation
- Manufacturing
- Hardware
website: https://www.jaka.com/en/index
---
