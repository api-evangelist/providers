---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 43.9
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 23
  human_in_the_loop: 0
  name: China Mobile Agentic Access
  operation_count: 45
  slug: china-mobile-agentic-access
  summary_line: 45 operations · 23 acting
api_count: 6
apis:
- description: The OneNET Studio application API is the one China Mobile surface with a complete, anonymously readable request-and-response contract. It is an action-dispatched gateway — every call is https://openap
  name: OneNET Studio Application API
  slug: onenet-studio-application-api
- description: '语音通话 (Voice Call Service) is China Mobile''s publicly documented voice capability on the OneNET gateway, reached at https://openapi.heclouds.com/vcs?action={voiceNotify|dialNotify}&version=2. Click to '
  name: OneNET Voice Call Service (VCS) API
  slug: onenet-voice-call-service
- description: 'OneNET is China Mobile''s IoT PaaS, operated by its CMIOT subsidiary, for device connection, device management, data storage and data visualisation. It is the company''s most genuinely developer-facing '
  name: OneNET IoT Open Platform API
  slug: onenet-iot-platform
- description: The 物联卡能力开放平台 (IoT Card Capability Open Platform) exposes cellular M2M SIM lifecycle and subscriber-information operations to enterprise IoT customers. Interface documentation is published openly — th
  name: China Mobile IoT Card Capability Open Platform API
  slug: iot-card-capability-platform
- description: The 通信能力开放平台 (Communication Capability Open Platform) is China Mobile's commercial network-capability channel and the surface where its Open Gateway work actually meets buyers. Its published developer
  name: China Mobile Communication Capability Open Platform
  slug: communication-capability-platform
- description: 中国移动互联网能力开放平台 at dev.10086.cn is the operator's application-facing capability marketplace, describing itself as offering 移动认证/号码认证 (mobile and number authentication), 大数据服务 (big data services), 通信能力 (
  name: China Mobile Internet Capability Open Platform
  slug: internet-capability-open-platform
artifact_total: 11
asyncapis:
- description: 'OneNET pushes events to application servers over plain HTTP(S) POST. Two distinct outbound surfaces are documented anonymously: the platform-wide 数据推送 (HTTP data push) service, which delivers rule-eng'
  name: China Mobile OneNET event and callback surface
  slug: china-mobile-onenet-asyncapi
- description: ''
  name: China Mobile Onenet Webhooks
  slug: china-mobile-onenet-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.chinamobileltd.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://open.iot.10086.cn/
- group: start
  title: ''
  type: Portal
  url: https://dev.10086.cn/
- group: docs
  title: ''
  type: Documentation
  url: https://open.iot.10086.cn/doc/
- group: docs
  title: ''
  type: APIReference
  url: https://open.iot.10086.cn/doc/iot_platform/book/api/introduce.html
- group: start
  title: ''
  type: GettingStarted
  url: https://open.iot.10086.cn/doc/easy-manual
- group: operate
  title: ''
  type: Support
  url: https://open.iot.10086.cn/servicesupport/workorder/list
- group: operate
  title: ''
  type: HelpCenter
  url: https://open.iot.10086.cn/doc/problem
- group: commercial
  title: ''
  type: Pricing
  url: https://open.iot.10086.cn/doc/introduce/book/fee.html
- group: start
  title: ''
  type: SignUp
  url: https://open.iot.10086.cn/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://open.iot.10086.cn/about/serviceprot/
- group: start
  title: ''
  type: Console
  url: https://open.iot.10086.cn/console
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cmri
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/cm-heclouds
- group: operate
  title: ''
  type: ChangeLog
  url: https://open.iot.10086.cn/doc/iot_platform/book/release/update_log.html
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/china-mobile-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/china-mobile-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/china-mobile-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/china-mobile-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/china-mobile-packages.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/china-mobile-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/china-mobile-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/china-mobile-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/china-mobile-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/china-mobile-conformance.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/china-mobile-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/china-mobile-data-model.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/china-mobile-onenet-asyncapi.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/china-mobile-onenet-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/china-mobile-llms.txt
created: '2026-07-25'
description: China Mobile Limited is the world's largest mobile network operator by subscribers, serving approximately 1,005 million mobile customers and 110 million gigabit broadband customers across all 31 provinces of mainland China plus Hong Kong, with roaming into more than 200 countries. Listed on the Hong Kong Stock Exchange and the Shanghai Stock Exchange and majority-owned by state-held China Mobile Communications Group, it runs mobile, broadband, cellular IoT, satellite internet, data centre, cloud and AI businesses on annual revenue of about RMB 1,050.2 billion. In the network-API value chain China Mobile sits squarely on the operator side, not the aggregator side. It joined the GSMA Open Gateway initiative in June 2023, sponsors and maintains several CAMARA APIs upstream (Click to Dial, the Model as a Service family, High-throughput Elastic Network, Facial Recognition, and co-sponsors Network Slice Booking), and in October 2024 secured GSMA Open Gateway certification for its
  Network-as-a-Service platform after its Quality on Demand API passed 63 conformance tests on ZTE NEF/SCEF exposure functions. None of that is callable from the open internet. Its API posture is partner-gated and domestic — the capability platforms at dev.10086.cn, ct.open.10086.cn and api.iot.10086.cn publish real product and interface documentation but issue credentials only to registered mainland enterprise customers under contract, and China Mobile is not a shareholder in Aduna, so it reaches developers through its own Chinese-language capability marketplaces rather than through the global CPaaS or aggregator channel. The one genuinely self-serve surface is OneNET, its IoT PaaS, which publishes open developer documentation and a live token-authenticated device API.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-25'
name: China Mobile
nav: Providers
network: true
overview: 'China Mobile publishes 2 APIs on the [APIs.io](https://apis.io/) network: OneNET Studio Application API and OneNET Voice Call Service (VCS) API. Tagged areas include Telecommunications, China, Mobile Network Operator, Network APIs, and CAMARA.


  The China Mobile catalog on APIs.io includes 2 event-driven AsyncAPI specifications.


  China Mobile''s developer surface includes developer portal, documentation, API reference, getting-started guide, support, pricing, signup flow, and 24 more developer resources.'
random_paper: 32
score:
  band: developing
  composite: 42.9
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 25.0
    developer_ergonomics: 64.7
    discoverability: 83.3
    governance: 20.8
    operational_transparency: 28.9
  previous_composite: 42.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 55.6
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/china-mobile/refs/heads/main/screenshots/china-mobile-2026-08-07T163418.png
security:
- kind: authentication
  name: China Mobile Authentication
  slug: china-mobile-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: China Mobile Domain Security
  slug: china-mobile-domain-security
  summary_line: TLSv1.2 · HSTS
slug: china-mobile
tags:
- Telecommunications
- China
- Mobile Network Operator
- Network APIs
- CAMARA
- GSMA Open Gateway
- IoT
- 5G
- Broadband
- Quality on Demand
- Number Authentication
- Satellite
website: https://www.chinamobileltd.com/
---
