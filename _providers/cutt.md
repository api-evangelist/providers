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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-07-28'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://cutt.com
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cutt-domain-security.yml
created: '2026-07-17'
description: 'cutt (cutt.com) is a Chinese technology company surfaced from the published portfolio of Qiming Venture Partners and added to the API Evangelist network as an enrichment lead. As of the 2026-07-20 enrichment pass the company has no reachable public web presence: the cutt.com apex does not complete an HTTPS connection, www.cutt.com returns HTTP 404 for the site root and every probed path, and no developer, documentation, or API subdomain (api./developer./docs./ dev./open.) resolves. One surviving subdomain, zhiyue.cutt.com, issues a 301 redirect to api.zhiyueapp.cn — a live JSON API host fronted by an APISIX 3.4.1 gateway that returns an empty 200 body and publishes no documentation. The zhiyueapp.cn domain is registered to 北京简网生活圈科技有限公司 (Beijing Jianwang Life Circle Technology Co., Ltd.), which appears to be the operating entity behind the cutt.com property. The cutt.com domain itself was created in 2003 and remains registered through Alibaba Cloud Computing Ltd. (HiChina)
  with an April 2027 expiry, so the registration is maintained even though the public site is not being served. No OpenAPI, AsyncAPI, SDK, portal, changelog, status page, or /.well-known/ discovery document could be found on any reachable host. This profile therefore records probed infrastructure evidence only; it carries no fabricated API surface and should be revisited if the company restores a public developer presence.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cutt.png
layout: provider
modified: '2026-07-20'
name: cutt
nav: Providers
network: true
overview: cutt is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Venture Backed, Qiming Portfolio, China, and Portfolio Lead.
random_paper: 43
score:
  band: minimal
  composite: 6.1
  delta: -0.7
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 61.1
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: domain-security
  name: Cutt Domain Security
  slug: cutt-domain-security
  summary_line: no transport/DNS hardening detected
slug: cutt
tags:
- Company
- Venture Backed
- Qiming Portfolio
- China
- Portfolio Lead
- Unverified API Surface
- Dormant
website: https://cutt.com
---
