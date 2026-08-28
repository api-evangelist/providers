---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
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
  score: 5.4
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: Toutiao account OAuth 2.0 and user-profile API, served from the open.snssdk.com host and documented on the Douyin Open Platform under the toutiao-or-xigua permission section. Supports the authorizatio
  name: Toutiao Open API (OAuth + User Profile)
  slug: toutiao-open-api-oauth-user-profile
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/toutiao-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.toutiao.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://open.toutiao.com/
- group: docs
  title: ''
  type: Documentation
  url: https://open.douyin.com/platform/resource/docs/develop/permission/toutiao-or-xigua/OAuth2.0/
- group: docs
  title: ''
  type: APIReference
  url: https://open.douyin.com/platform/resource/docs/ability/content-management/toutiao-publish-solution/
- group: start
  title: ''
  type: SignUp
  url: https://mp.toutiao.com/auth/page/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.toutiao.com/user_agreement/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.toutiao.com/privacy_protection/
- group: auth
  title: ''
  type: Authentication
  url: authentication/toutiao-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/toutiao-scopes.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/toutiao-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/toutiao-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/toutiao-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/toutiao-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/toutiao-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/toutiao-llms.txt
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/toutiao_stock/
coverage:
  checked: '2026-08-05'
  detail: ByteDance documents the Toutiao OAuth and user-profile API publicly on the Douyin Open Platform and the endpoints answer live on open.snssdk.com, but no OpenAPI, AsyncAPI, GraphQL SDL, Postman collection or JSON Schema is published on any Toutiao, snssdk or ByteDance host — and open.douyin.com returns a 200 HTML single-page-app shell for /openapi.json and every /.well-known/ path, byte-identical to a nonexistent control path, so there is nothing for a machine to fetch.
  evidence:
  - status: 200
    url: https://open.snssdk.com/oauth/access_token/
  - status: 404
    url: https://open.snssdk.com/openapi.json
  - status: 200
    url: https://open.douyin.com/platform/resource/docs/develop/permission/toutiao-or-xigua/OAuth2.0/
  - status: 200
    url: https://open.douyin.com/openapi.json
  - status: 404
    url: https://www.toutiao.com/.well-known/agent-card.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-08-05'
description: 'Toutiao (今日头条) is ByteDance''s AI-driven content recommendation platform, launched in 2012, aggregating news, articles, short video and micro-posts into a personalized feed for hundreds of millions of readers in China. Creators publish through 头条号 (Toutiao Hao) accounts on mp.toutiao.com, and third-party developers integrate through the ByteDance open-platform stack: Toutiao account OAuth 2.0 and user-profile APIs served from open.snssdk.com and documented on the Douyin Open Platform under the toutiao-or-xigua section, a content-sync and video publishing surface available to approved applications, mini-programs via the ByteDance mini-app developer platform, and advertising APIs that have since migrated from ad.toutiao.com to OceanEngine (巨量引擎). Toutiao publishes no OpenAPI, AsyncAPI, llms.txt or A2A agent card; its developer program is registration- and approval-gated and its documentation is client-side rendered in Chinese.'
image: https://sf3-cdn-tos.douyinstatic.com/obj/eden-cn/uhbfnupkbps/toutiao_favicon.ico
layout: provider
modified: '2026-08-05'
name: Toutiao
nav: Providers
network: true
overview: 'Toutiao publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, News, Content, Media, and Social.


  Toutiao''s developer surface includes documentation, API reference, signup flow, authentication, and 13 more developer resources.'
random_paper: 17
scopes:
- name: Toutiao Scopes
  scope_count: 1
  slug: toutiao-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: emerging
  composite: 21.9
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 38.1
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 21.9
  provenance:
    conformance: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: authentication
  name: Toutiao Authentication
  slug: toutiao-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Toutiao Domain Security
  slug: toutiao-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: toutiao
tags:
- Company
- News
- Content
- Media
- Social
- Recommendation
- Publishing
- ByteDance
- China
- Authentication
website: https://www.toutiao.com/
---
