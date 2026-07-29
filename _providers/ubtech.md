---
access_model:
  confidence: medium
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.5
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: Receive data from remote device.
  name: UBTech subscriptions API
  slug: ubtech-subscriptions-api
artifact_total: 6
asyncapis:
- description: ''
  name: Ubtech Yanshee Subscriptions Webhooks
  slug: ubtech-yanshee-subscriptions-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://ubtrobot.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://yandev.ubtrobot.com/
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/UBTEDU/Yan_ADK/tree/master/docs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/UBTEDU
- group: company
  title: ''
  type: Blog
  url: https://www.ubtrobot.com/en/about/news
- group: operate
  title: ''
  type: Support
  url: https://www.ubtrobot.com/en/support/downloads
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ubtrobot.com/en/privacy/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ubtrobot.com/en/privacy/term-of-use
- group: auth
  title: ''
  type: Security
  url: https://www.ubtrobot.com/en/privacy/loophole/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ubtech-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ubtech-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/ubtech-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/ubtech-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/ubtech-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ubtech-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/ubtech-yanshee-openadk-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/ubtech-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ubtech-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/ubtech-changelog.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ubtech-conventions.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ubtech-authentication.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/ubtech-yanshee-subscriptions-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: UBTech Robotics is a Shenzhen-based robotics company building humanoid robots (the Walker series), commercial service robots (Cruzr, CADEBOT), AI education robots and kits (Yanshee, uKit, UGOT, Jimu), and consumer smart hardware (Alpha robots, AIRROBO). Its developer surface centers on the Yanshee educational humanoid, an open Raspberry Pi-based robot that exposes a device-local REST API (Yanshee Open ADK, Swagger 2.0) with an on-robot Swagger UI, a push-based subscription event surface, and Python, C, and Arduino SDKs published through the UBTEDU GitHub organization.
image: https://avatars.githubusercontent.com/u/32864785?v=4
layout: provider
mcp_servers:
- description: ''
  name: ubtech-mcp.yml
  slug: ubtech-mcpyml
modified: '2026-07-21'
name: UBTech
nav: Providers
network: true
overview: 'UBTech publishes 1 API on the [APIs.io](https://apis.io/) network: subscriptions API. Tagged areas include Company, Robotics, Humanoid Robots, Education Technology, and Artificial Intelligence.


  The UBTech catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  UBTech''s developer surface includes documentation, engineering blog, support, changelog, authentication, and 18 more developer resources.'
random_paper: 19
score:
  band: thin
  composite: 41.4
  delta: -3.6
  facets:
    commercial_clarity: 21.1
    contract_quality: 51.6
    developer_ergonomics: 45.1
    discoverability: 87.0
    governance: 11.5
    operational_transparency: 39.5
  previous_composite: 45.0
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Ubtech Authentication
  slug: ubtech-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Ubtech Domain Security
  slug: ubtech-domain-security
  summary_line: TLSv1.2 · DMARC
- kind: vulnerability-disclosure
  name: Ubtech Vulnerability Disclosure
  slug: ubtech-vulnerability-disclosure
  summary_line: Hackerone
slug: ubtech
tags:
- Company
- Robotics
- Humanoid Robots
- Education Technology
- Artificial Intelligence
- Consumer Electronics
- Service Robots
website: https://ubtrobot.com
---
