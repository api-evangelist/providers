---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.9
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 23
  human_in_the_loop: 0
  name: China Mobile Agentic Access
  operation_count: 45
  slug: china-mobile-agentic-access
  summary_line: 45 operations · 23 acting
api_count: 2
apis:
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
- baseURL: https://openapi.heclouds.com
  baseurl_source: declared
  description: The Application Development API from China Mobile — 35 operation(s) for application development.
  name: China Mobile Application Development API
  slug: china-mobile-application-development-api
- baseURL: https://openapi.heclouds.com
  baseurl_source: declared
  description: The Device Management API from China Mobile — 9 operation(s) for device management.
  name: China Mobile Device Management API
  slug: china-mobile-device-management-api
- baseURL: https://openapi.heclouds.com
  baseurl_source: declared
  description: 语音通话 — voice notification and click-to-dial
  name: China Mobile Voice Call Service API
  slug: china-mobile-voice-call-service-api
artifact_total: 14
asyncapis:
- description: 'OneNET pushes events to application servers over plain HTTP(S) POST. Two distinct outbound surfaces are documented anonymously: the platform-wide 数据推送 (HTTP data push) service, which delivers rule-eng'
  name: China Mobile OneNET event and callback surface
  slug: china-mobile-onenet-asyncapi
- description: ''
  name: China Mobile Onenet Webhooks
  slug: china-mobile-onenet-webhooks
collections:
- collection_type: open
  name: China Mobile OneNET Studio Application API
  slug: open-china-mobile-onenet-studio
- collection_type: open
  name: China Mobile OneNET Voice Call Service (VCS) API
  slug: open-china-mobile-vcs
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/china-mobile-onenet-studio-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/china-mobile-vcs-overlay.yaml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/china-mobile-mcp.yml
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
overview: 'China Mobile publishes 3 APIs on the [APIs.io](https://apis.io/) network: Application Development API, Device Management API, and Voice Call Service API. Tagged areas include Telecommunications, China, Mobile Network Operator, Network APIs, and CAMARA.


  The China Mobile catalog on APIs.io includes 2 event-driven AsyncAPI specifications.


  China Mobile''s developer surface includes developer portal, documentation, API reference, getting-started guide, support, pricing, signup flow, and 27 more developer resources.'
random_paper: 16
score:
  band: developing
  composite: 41.9
  coverage:
    artifact_dirs: 20
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 22.0
    developer_ergonomics: 70.8
    discoverability: 59.3
    governance: 18.2
    operational_transparency: 26.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - china
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - greater-china
  previous_composite: 41.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 55.6
  schema_version: 0.18.3
  scored_at: '2026-09-05'
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
