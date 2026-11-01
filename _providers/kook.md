---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 26.1
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 34
  human_in_the_loop: 1
  name: Kook Agentic Access
  operation_count: 51
  slug: kook-agentic-access
  summary_line: 51 operations · 34 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://www.kookapp.cn/api/v3
  baseurl_source: declared
  description: 使用Websocket或Webhook将Bot连接至服务器
  name: KOOK 将Bot连接到 KOOK 服务器 API
  slug: kook-bot-kook-api
- baseURL: https://www.kookapp.cn/api/v3
  baseurl_source: declared
  description: '{''$ref'': ''./descriptions/_index.yaml#/event''}'
  name: KOOK 事件通知介绍 API
  slug: kook-default-api
- baseURL: https://www.kookapp.cn/api/v3
  baseurl_source: declared
  description: Gateway接口
  name: KOOK Gateway接口 API
  slug: kook-gateway-api
- baseURL: https://www.kookapp.cn/api/v3
  baseurl_source: declared
  description: '{''$ref'': ''./descriptions/_index.yaml#/kmarkdown-card''}'
  name: KOOK K Markdown与卡片消息 API
  slug: kook-kmarkdown-api
artifact_total: 8
asyncapis:
- description: ''
  name: Kook Webhooks
  slug: kook-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/kook/agentic-access/kook-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/kook-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/kook/rules/kook-rules.yml
  title: ''
  type: Spectral
  url: rules/kook-rules.yml
- group: design
  href: https://artifacts.apis.io/kook/vocabulary/kook-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/kook-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/kook/asyncapi/kook-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/kook-webhooks.yml
- group: design
  href: https://artifacts.apis.io/kook/conformance/kook-conformance.yml
  title: ''
  type: Conformance
  url: conformance/kook-conformance.yml
- group: other
  href: https://artifacts.apis.io/kook/hosts/kook-hosts.yml
  title: ''
  type: Hosts
  url: hosts/kook-hosts.yml
- group: start
  title: ''
  type: Login
  url: https://www.kookapp.cn/app/login
- group: docs
  title: ''
  type: Documentation
  url: https://developer.kookapp.cn/
- group: auth
  href: https://artifacts.apis.io/kook/security/kook-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/kook-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.kookapp.cn/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.kookapp.cn/developer.html
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.kookapp.cn
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.kookapp.cn/protocol.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.kookapp.cn/privacy.html
- group: operate
  title: ''
  type: Contact
  url: https://www.kookapp.cn/contact.html
- group: company
  title: ''
  type: Careers
  url: https://www.kookapp.cn/join.html
created: '2026-10-26'
description: KOOK is a voice communication platform designed for gamers and communities, offering high-quality audio, low latency, and features such as server creation, screen sharing, and noise reduction. It supports PC, Android, iOS, and web clients, enabling users to create themed servers for gaming, music, reading, language exchange, and more, fostering seamless real-time interaction across devices.
image: https://img.kookapp.cn/assets/logo_1024.png
layout: provider
modified: '2026-10-26'
name: KOOK
nav: Providers
network: true
overview: 'KOOK publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including 将Bot连接到 KOOK 服务器 API, 事件通知介绍 API, Gateway接口 API, and 1 more. Tagged areas include Company, Voice Communication, Gaming, Community, and Real-time.


  The KOOK catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  KOOK''s developer surface includes documentation and 15 more developer resources.'
random_paper: 4
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: KOOK API Rules
  rule_count: 11
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 2
  slug: kook-rules
score:
  band: thin
  composite: 34.2
  coverage:
    artifact_dirs: 13
    catalog_earned: 42.8
    catalog_earned_first_party: 0.0
    catalog_gap: 72.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 22.0
    contract_quality: 47.0
    developer_ergonomics: 23.8
    discoverability: 66.1
    operational_transparency: 7.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Kook Domain Security
  slug: kook-domain-security
  summary_line: TLSv1.2
slug: kook
tags:
- Company
- Voice Communication
- Gaming
- Community
- Real-time
website: https://www.kookapp.cn/
---
