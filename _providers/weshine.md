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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-24'
api_count: 1
apis:
- description: 'The Weshine (闪萌) Expression API (表情API) is a business-to-business GIF/animated-sticker service with three interfaces: a hot/trending interface (热门接口), a real-time search interface (搜索接口) supporting gi'
  name: Weshine Expression API
  slug: weshine-expression-api
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/weshine-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/weshine-llms.txt
- group: company
  title: ''
  type: Website
  url: http://www.weshineapp.com/
created: '2026-07-17'
description: Weshine (闪萌, Shanmeng), operated by Beijing Shanqu Information Technology Co., Ltd (北京闪趣信息技术有限公司), is a Chinese GIF and animated-sticker (表情) search engine. It offers a business-to-business "Expression API" (表情API) with three documented interfaces — a hot/trending interface (热门接口) that returns trending GIFs by category refreshed hourly, a real-time search interface (搜索接口) supporting gif/webp/mp4 and multi-dimensional ranking, and a "magic image" interface (神配图接口) that semantically matches a phrase to a background GIF and composites a caption onto it. The platform reports 800M+ users covered, 300M+ daily searches, and 200M+ animated images sent per day, powering social apps, input methods (including its own KK Keyboard), and browsers. API access is via business partnership; no public self-serve developer portal, OpenAPI specification, or SDK is published.
image: http://www.weshineapp.com/favicon.ico
layout: provider
modified: '2026-07-21'
name: Weshine
nav: Providers
network: true
overview: Weshine publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, GIF, Stickers, and Search.
random_paper: 20
score:
  band: minimal
  composite: 6.7
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 66.7
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.7
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
security:
- kind: domain-security
  name: Weshine Domain Security
  slug: weshine-domain-security
  summary_line: TLSv1.2
slug: weshine
tags:
- Company
- Consumer
- GIF
- Stickers
- Search
- Image
- Media
- Emoji
- Content
website: http://www.weshineapp.com/
---
