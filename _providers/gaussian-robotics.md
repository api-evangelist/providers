---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 12.6
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: REST API for the Gausium Cloud platform. Authenticated with OAuth 2.0 bearer tokens (custom open-access grant), it exposes robot information, robot status, task reports, robot maps and subareas, robot
  name: Gausium Cloud Open API
  slug: gausium-cloud-open-api
artifact_total: 4
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer-us.gs-robot.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer-us.gs-robot.com/en_US/General%20Introduction
- group: docs
  title: ''
  type: APIReference
  url: https://developer-us.gs-robot.com/en_US/Robot%20Information%20Service/List%20Robots
- group: start
  title: ''
  type: GettingStarted
  url: https://developer-us.gs-robot.com/en_US/Be%20A%20Developer%20And%20Create%20A%20Key
- group: start
  title: ''
  type: SignUp
  url: https://service.gs-robot.com/developer
- group: company
  title: ''
  type: Blog
  url: https://gausium.com/blog/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://gausium.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://gausium.com/terms-of-use/
- group: operate
  title: ''
  type: Support
  url: https://gausium.com/contact/
- group: company
  title: ''
  type: Website
  url: https://gausium.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer-us.gs-robot.com/en_US/Release%20Notes
- group: agent
  title: ''
  type: MCPServer
  url: mcp/gaussian-robotics-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/gaussian-robotics-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/gaussian-robotics-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/gaussian-robotics-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/gaussian-robotics-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/gaussian-robotics-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/gaussian-robotics-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/gaussian-robotics-changelog.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gaussian-robotics-domain-security.yml
created: '2026-07-17'
description: Gaussian Robotics (Gausium) is an autonomous cleaning and service robotics company founded in 2013 and headquartered in Shanghai, with more than 6,500 customers across 70+ countries. Its commercial floor-care and delivery robots (Scrubber 50/75, Phantas, Beetle, Omnie, Vacuum 40) are built on AI, 3D LiDAR and SLAM navigation. Gausium publishes a public developer platform and the Gausium Cloud Open API (openapi.gs-robot.com), a REST API secured with OAuth 2.0 bearer tokens that lets facilities and partners list robots, query robot status and task reports, retrieve maps and subareas, issue robot commands, dispatch temporary cleaning tasks, and integrate the fleet with building IoT and elevator-control systems.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gaussian-robotics.png
layout: provider
mcp_servers:
- description: ''
  name: gaussian-robotics-mcp.yml
  slug: gaussian-robotics-mcpyml
modified: '2026-07-19'
name: Gaussian Robotics
nav: Providers
network: true
overview: 'Gaussian Robotics publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Frontier Tech, Robotics, Autonomous Robots, and Cleaning Robots.


  Gaussian Robotics'' developer surface includes documentation, API reference, getting-started guide, signup flow, engineering blog, support, changelog, and 13 more developer resources.'
random_paper: 134
score:
  band: thin
  composite: 29.5
  delta: -0.6
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 57.1
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 23.7
  previous_composite: 30.1
  provenance:
    conformance: derived
    mcp: first-party
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gaussian-robotics/refs/heads/main/screenshots/gaussian-robotics-2026-07-25T215503.png
security:
- kind: authentication
  name: Gaussian Robotics Authentication
  slug: gaussian-robotics-authentication
  summary_line: oauth2/http · 2 schemes
- kind: domain-security
  name: Gaussian Robotics Domain Security
  slug: gaussian-robotics-domain-security
  summary_line: TLSv1.3 · HSTS
slug: gaussian-robotics
tags:
- Company
- Frontier Tech
- Robotics
- Autonomous Robots
- Cleaning Robots
- IoT
- Fleet Management
- Robot Operations
website: https://gausium.com/
---
