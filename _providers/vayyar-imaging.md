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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 23.4
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: 'Agent-facing commerce surface of the Walabot DIY storefront (walabot.com, a Shopify store operated by Vayyar): unauthenticated read-only product JSON endpoints (/products/{handle}.json, /collections/{'
  name: Walabot Storefront Agent Commerce (UCP)
  slug: walabot-storefront-agent-commerce-ucp
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vayyar-imaging-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://vayyar.com
- group: company
  title: ''
  type: Blog
  url: https://vayyar.com/blog/
- group: docs
  title: ''
  type: Documentation
  url: https://api.walabot.com
- group: docs
  title: ''
  type: APIReference
  url: https://api.walabot.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Vayyar
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://vayyar.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://walabot.com/pages/terms-and-conditions
- group: operate
  title: ''
  type: Support
  url: https://walabot.com/pages/contact-us
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/vayyar-imaging-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/vayyar-imaging-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/vayyar-imaging-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/vayyar-imaging-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/vayyar-imaging-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/vayyar-imaging-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/vayyar-imaging-packages.yml
created: '2026-07-17'
description: Vayyar Imaging is an Israeli sensor company whose 4D imaging radar-on-chip technology senses, monitors, and images people and objects without cameras. Its RF sensors power Vayyar Care touchless fall detection for elderly care, automotive in-cabin monitoring, smart buildings, public safety, robotics, and the consumer Walabot DIY in-wall imager. Vayyar's developer surface today centers on the Walabot SDK documentation (api.walabot.com) and the Walabot storefront's agent-commerce endpoints (llms.txt, UCP, and a hosted MCP endpoint on walabot.com).
image: https://vayyar.com/wp-content/uploads/2022/08/vayyar-logo.png
layout: provider
mcp_servers:
- description: ''
  name: vayyar-imaging-mcp.yml
  slug: vayyar-imaging-mcpyml
modified: '2026-07-21'
name: Vayyar Imaging
nav: Providers
network: true
overview: 'Vayyar Imaging publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Sensors, Radar, Imaging, and IoT.


  Vayyar Imaging''s developer surface includes engineering blog, documentation, API reference, support, authentication, and 11 more developer resources.'
random_paper: 23
scopes:
- name: Vayyar Imaging Scopes
  scope_count: 4
  slug: vayyar-imaging-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 27.7
  delta: -2.8
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 41.3
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 5.3
  previous_composite: 30.5
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 52.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Vayyar Imaging Authentication
  slug: vayyar-imaging-authentication
  summary_line: oauth2/openIdConnect/none · 1 scheme
- kind: domain-security
  name: Vayyar Imaging Domain Security
  slug: vayyar-imaging-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: vayyar-imaging
tags:
- Company
- Sensors
- Radar
- Imaging
- IoT
- Healthcare
- Elderly Care
- Automotive
- Smart Home
website: https://vayyar.com
---
