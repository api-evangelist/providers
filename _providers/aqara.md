---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: platform
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 33.8
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 40
  human_in_the_loop: 6
  name: Aqara Agentic Access
  operation_count: 74
  slug: aqara-agentic-access
  summary_line: 74 operations · 40 acting · 6 human-in-the-loop
api_count: 4
apis:
- baseURL_template: '{host}/open/api/v1'
  baseurl_source: spec_template
  description: APIs for automation creation, editing, query, deletion, and capability query
  name: Aqara Automation API
  slug: aqara-automation-api
- baseURL_template: '{host}/v4.0/open/api'
  baseurl_source: spec_template
  description: Device query, property read/write, and command execution APIs
  name: Aqara Device API
  slug: aqara-device-api
- baseURL_template: '{host}/open/api/v1'
  baseurl_source: spec_template
  description: APIs for managing gateway subdevice pairing, binding, and unbinding operations
  name: Aqara Gateway API
  slug: aqara-gateway-api
- baseURL_template: '{host}/v4.0/open/api'
  baseurl_source: spec_template
  description: Space management APIs
  name: Aqara Space API
  slug: aqara-space-api
- baseURL_template: '{host}/open/api/v1'
  baseurl_source: spec_template
  description: Studio statistics query API
  name: Aqara Studio API
  slug: aqara-studio-api
artifact_total: 28
asyncapis:
- description: 'This document describes the asynchronous messages exchanged between the client and the Studio WebSocket service: - The client sends authentication, heartbeat, subscribe, and unsubscribe requests. - St'
  name: Studio WebSocket API
  slug: data-export-api-en
- description: 本文件描述客户端与 Studio WebSocket 服务之间的异步消息： - 客户端发送鉴权、心跳、订阅、取消订阅请求。 - Studio 返回请求响应，并在订阅命中或设备事件发生时主动推送消息。 - 本契约覆盖设备、Trait 和对象事件订阅，不覆盖 SubscribeEventRequest、UnsubscribeEventRequest 等独立告警事件订阅。 - Studio 局域网 St
  name: Studio WebSocket API
  slug: data-export-api-zh
- description: 第三方接收端视角。Studio Open 向配置的 endpoint 发送 HTTP/1.1 POST。 支持 HTTP/HTTPS，HTTPS 必须验证证书；不跟随重定向。地址禁止 query、fragment 和 userinfo，保留路径中的连续斜杠和已有百分号转义。 业务正文只推送 v1，完整 Schema 复用 WebSocket。实时 best-effort，无持久化消息队列、历史补发
  name: Studio HTTP Push Receiver API
  slug: http-push-zh
common:
- group: agent
  href: https://artifacts.apis.io/aqara/agentic-access/aqara-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/aqara-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/aqara/rules/aqara-rules.yml
  title: ''
  type: Spectral
  url: rules/aqara-rules.yml
- group: design
  href: https://artifacts.apis.io/aqara/json-ld/aqara-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/aqara-context.jsonld
- group: design
  href: https://artifacts.apis.io/aqara/vocabulary/aqara-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/aqara-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/aqara/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/aqara/data-model/aqara-data-model.yml
  title: ''
  type: DataModel
  url: data-model/aqara-data-model.yml
- group: auth
  href: https://artifacts.apis.io/aqara/authentication/aqara-authentication.yml
  title: ''
  type: Authentication
  url: authentication/aqara-authentication.yml
- group: design
  href: https://artifacts.apis.io/aqara/errors/aqara-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/aqara-problem-types.yml
- group: design
  href: https://artifacts.apis.io/aqara/conformance/aqara-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aqara-conformance.yml
- group: agent
  href: https://artifacts.apis.io/aqara/llms/aqara-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aqara-llms.txt
- group: agent
  href: https://artifacts.apis.io/aqara/well-known/aqara-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aqara-well-known.yml
- group: other
  href: https://artifacts.apis.io/aqara/hosts/aqara-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aqara-hosts.yml
- group: other
  href: https://artifacts.apis.io/aqara/vendors/aqara-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aqara-vendors.yml
- group: build
  href: https://artifacts.apis.io/aqara/packages/aqara-packages.yml
  title: ''
  type: SDKs
  url: packages/aqara-packages.yml
- group: build
  href: https://artifacts.apis.io/aqara/packages/aqara-packages.yml
  title: ''
  type: Packages
  url: packages/aqara-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.aqara.com/en/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aqara.com/en/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://www.aqara.com/en/about-us/news/
- group: start
  title: ''
  type: GettingStarted
  url: http://docs.aqara.com/docs/aqara-studio/overview/introduction
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aqara
- group: auth
  href: https://artifacts.apis.io/aqara/security/aqara-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aqara-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.aqara.com/en/
- group: docs
  title: ''
  type: Documentation
  url: https://www.aqara.com/en/
- group: company
  title: ''
  type: Blog
  url: https://www.aqara.com/en/blog
- group: other
  title: ''
  type: BrandStory
  url: https://www.aqara.com/en/about-us/brand-story/
- group: operate
  title: ''
  type: ContactUs
  url: https://www.aqara.com/en/about-us/contact-us/
created: '2026-10-28'
description: Aqara provides smart home automation devices and solutions, including sensors, hubs, controllers, cameras, door locks, lighting, and curtain controllers. Their platform integrates with Apple Home, Google Assistant, and other ecosystems, offering a unified app for device management and automation. Aqara focuses on privacy, security, and easy setup for consumers worldwide.
json_schemas:
- name: AutomationCapabilitiesResponse
  property_count: 0
  slug: aqara-automation-capabilities-response
- name: CommandExecuteAwaitResponse
  property_count: 0
  slug: aqara-command-execute-await-response
- name: CreateAutomationRequest
  property_count: 4
  slug: aqara-create-automation-request
- name: CreateSpaceRequest
  property_count: 3
  slug: aqara-create-space-request
- name: DeviceDefinitionsResponse
  property_count: 0
  slug: aqara-device-definitions-response
- name: DevicesResponse
  property_count: 0
  slug: aqara-devices-response
- name: SpacesResponse
  property_count: 0
  slug: aqara-spaces-response
- name: SubdeviceJoinRequest
  property_count: 3
  slug: aqara-subdevice-join-request
- name: TraitExecuteResponse
  property_count: 0
  slug: aqara-trait-execute-response
- name: TraitValueResponse
  property_count: 0
  slug: aqara-trait-value-response
- name: UpdateAutomationRequest
  property_count: 5
  slug: aqara-update-automation-request
jsonld:
- class_count: 74
  name: Aqara Context
  property_count: 116
  slug: aqara-context
layout: provider
modified: '2026-10-28'
name: Aqara
nav: Providers
network: true
overview: 'Aqara publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Automation API, Device API, Gateway API, and 2 more. Tagged areas include Smart Home, IoT, Consumer Electronics, Home Automation, and Security.


  The Aqara catalog on APIs.io includes 3 event-driven AsyncAPI specifications, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Aqara''s developer surface includes authentication, getting-started guide, documentation, engineering blog, and 22 more developer resources.'
random_paper: 14
rules:
- authorship: generated
  effective_rule_count: 59
  extends:
  - spectral:oas
  name: Aqara API Rules
  rule_count: 18
  severity_counts:
    error: 16
    hint: 0
    info: 1
    warn: 1
  slug: aqara-rules
score:
  band: developing
  composite: 41.1
  coverage:
    artifact_dirs: 22
    catalog_earned: 58.8
    catalog_earned_first_party: 0.0
    catalog_gap: 56.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 68.7
    developer_ergonomics: 44.6
    discoverability: 60.7
    operational_transparency: 5.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Aqara Authentication
  slug: aqara-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Aqara Domain Security
  slug: aqara-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 4
skills:
- name: aqara-control-device-command
  slug: aqara-control-device-command
- name: aqara-create-automation
  slug: aqara-create-automation
- name: aqara-manage-spaces
  slug: aqara-manage-spaces
- name: aqara-subdevice-join
  slug: aqara-subdevice-join
slug: aqara
tags:
- Smart Home
- IoT
- Consumer Electronics
- Home Automation
- Security
website: https://www.aqara.com/en/
---
