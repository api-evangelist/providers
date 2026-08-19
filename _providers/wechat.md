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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: na
    error_semantics: false
    event_surface_described: derived
    idempotency: na
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.0
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Wechat Agentic Access
  operation_count: 3
  slug: wechat-agentic-access
  summary_line: 3 operations
api_count: 16
apis:
- description: Backend HTTPS/JSON APIs that Mini Program operators call from their own servers to authenticate user sessions (code2Session), mint access tokens, send customer service and template/subscription messag
  name: WeChat Mini Programs Server API
  slug: wechat-mini-programs-server-api
- description: Client-side JavaScript API exposed inside the WeChat runtime to Mini Programs and Mini Games. Covers network (wx.request, wx.downloadFile, wx.uploadFile), storage, UI / navigation, media (audio, video
  name: WeChat Mini Programs Client API
  slug: wechat-mini-programs-client-api
- description: WeChat Pay's third-generation REST API for mainland-China direct-connect merchants. Authenticates with merchant API certificates and platform-key signed requests over HTTPS/JSON. Covers JSAPI / Native
  name: WeChat Pay APIv3 (Direct-Connect Merchant)
  slug: wechat-pay-apiv3-direct-merchant
- description: WeChat Pay's APIv3 in "service provider" mode, used by payment platforms and ISVs to onboard and operate sub-merchants. Adds combined-order JSAPI/Native/App payments, sub-merchant onboarding ("特约商户进件"
  name: WeChat Pay APIv3 (Service Provider / Partner)
  slug: wechat-pay-apiv3-service-provider
- description: Cross-border WeChat Pay surface for international institutions and merchants accepting payments from WeChat users outside mainland China. Provides a "universal version for global institutions and merc
  name: WeChat Pay Global v3 API
  slug: wechat-pay-global-v3
- description: OAuth 2.0 authorization flow exposed by the WeChat Open Platform for native iOS, Android, and HarmonyOS apps. Apps redirect into WeChat to obtain an authorization code, then exchange it via `https://a
  name: WeChat Open Platform — Mobile App Login (OAuth 2.0)
  slug: wechat-open-platform-mobile-login
- description: Web-based OAuth 2.0 login that renders a WeChat QR code on third-party websites. End users scan the code in WeChat to authenticate; the website receives a code on its callback URL and exchanges it for
  name: WeChat Open Platform — Website Login (QR OAuth)
  slug: wechat-open-platform-website-login
- description: API surface that lets authorized ISVs operate Official Accounts and Mini Programs on behalf of merchant clients ("代商家调用接口"). Covers merchant authorization onboarding, developing Mini Programs on behal
  name: WeChat Open Platform — Third-Party Platform API
  slug: wechat-open-platform-third-party
- description: HTTPS/JSON APIs for WeChat Official Accounts (Subscription Accounts and Service Accounts) — the publishing surface used by media, brands, and businesses to reach WeChat followers. Surface includes use
  name: WeChat Official Accounts API
  slug: wechat-official-accounts-api
- description: Server API for Enterprise WeChat / WeCom — Tencent's enterprise collaboration suite. All calls are HTTPS/JSON, UTF-8 encoded, and require an access token. Covers Contacts management (members, departme
  name: WeChat Work (WeCom) API
  slug: wechat-work-api
- description: WeChat Cloud Hosting (微信云托管) is Tencent's cloud-native, ops-free container deployment service tightly integrated into the WeChat ecosystem. Documented as "a cloud-native, operations-free, highly avail
  name: WeChat Cloud Hosting API
  slug: wechat-cloud-hosting-api
- description: WeChat Channels (视频号) is WeChat's short-video and livestreaming product. The developer surface — exposed through the Mini Programs platform and Channels merchant tools — covers livestream room creatio
  name: WeChat Channels (Video Accounts) Developer Surface
  slug: wechat-channels-api
- description: WeChat Shop (微信小店) is WeChat's unified merchant storefront tying together Mini Programs, Channels livestreaming, Official Accounts, and WeChat Search. APIs cover product (SPU/SKU) management, order li
  name: WeChat Shop (微信小店) API
  slug: wechat-shop-api
- description: Application-level access token management.
  name: WeChat Access Token API
  slug: wechat-access-token-api
- description: Mini Program login and session exchange.
  name: WeChat Login API
  slug: wechat-login-api
- description: User identity (UnionID) lookups.
  name: WeChat User Information API
  slug: wechat-user-information-api
artifact_total: 42
asyncapis:
- description: AsyncAPI description of the publicly documented WeChat (Weixin) webhook surfaces. WeChat does not expose a public WebSocket / streaming endpoint for third-party developers — its event-driven surface i
  name: WeChat Webhooks (Official Accounts, WeChat Pay APIv3, WeCom)
  slug: wechat-webhooks-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: WeChat Mini Program Server API (subset) Access Token API
  slug: open-wechat-access-token-api
- collection_type: open
  name: WeChat Mini Program Server API (subset) Access Token Login API
  slug: open-wechat-login-api
- collection_type: open
  name: WeChat Mini Program Server API (subset) Access Token User Information API
  slug: open-wechat-user-information-api
- collection_type: open
  name: WeChat Mini Program Server API (subset)
  slug: open-wechat
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/wechat-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wechat-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.wechat.com/
- group: start
  title: ''
  type: Portal
  url: https://weixin.qq.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.weixin.qq.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.weixin.qq.com/doc/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.weixin.qq.com/miniprogram/en/dev/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.weixin.qq.com/miniprogram/en/dev/framework/quickstart/
- group: operate
  title: ''
  type: Support
  url: https://developers.weixin.qq.com/community/develop/doc
- group: other
  title: ''
  type: Hub
  url: https://developers.weixin.qq.com/community/
- group: start
  title: ''
  type: Console
  url: https://mp.weixin.qq.com/
- group: start
  title: ''
  type: Portal
  url: https://pay.weixin.qq.com/
- group: start
  title: ''
  type: Login
  url: https://pay.weixin.qq.com/index.php/core/home/login
- group: start
  title: ''
  type: Portal
  url: https://work.weixin.qq.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.work.weixin.qq.com/
- group: start
  title: ''
  type: Portal
  url: https://open.weixin.qq.com/
- group: start
  title: ''
  type: Portal
  url: https://channels.weixin.qq.com/
- group: start
  title: ''
  type: Portal
  url: https://cloud.weixin.qq.com/
- group: start
  title: ''
  type: Portal
  url: https://shop.weixin.qq.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/wechat-miniprogram
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/wechatpay-apiv3
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/wechat-miniprogram/miniprogram-demo
- group: build
  title: ''
  type: SDKs
  url: https://github.com/wechat-miniprogram/weui-miniprogram
- group: build
  title: ''
  type: SDKs
  url: https://github.com/wechat-miniprogram/api-typings
- group: build
  title: ''
  type: SDKs
  url: https://github.com/wechat-miniprogram/threejs-miniprogram
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Tencent/weui
- group: build
  title: ''
  type: SDKs
  url: https://github.com/wechatpay-apiv3/wechatpay-java
- group: build
  title: ''
  type: SDKs
  url: https://github.com/wechatpay-apiv3/wechatpay-go
- group: build
  title: ''
  type: SDKs
  url: https://github.com/wechatpay-apiv3/wechatpay-php
- group: build
  title: ''
  type: SDKs
  url: https://github.com/wechatpay-apiv3/wechatpay-apache-httpclient
- group: build
  title: ''
  type: SDKs
  url: https://github.com/wechatpay-apiv3/wechatpay-guzzle-middleware
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/wechatpay-apiv3/wechatpay-postman-script
- group: build
  title: ''
  type: CLI
  url: https://github.com/wechatpay-apiv3/CertificateDownloader
- group: operate
  title: ''
  type: IDESupport
  url: https://developers.weixin.qq.com/miniprogram/dev/devtools/devtools.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.weixin.qq.com/agreement?lang=en_US
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tencent.com/en-us/privacy-policy.html
- group: operate
  title: ''
  type: Support
  url: https://kf.qq.com/
- group: operate
  title: ''
  type: Support
  url: https://service.weixin.qq.com/
- group: other
  title: ''
  type: Notes
  url: ''
created: '2026-05-22'
description: WeChat (Weixin) is Tencent's flagship super-app, combining messaging, social, payments, mini-apps, official-account publishing, video, enterprise collaboration, and cloud hosting under a single identity. Its developer surface spans the WeChat Open Platform (third-party app login and authorization), Mini Programs (client and server APIs), Mini Games, Official Accounts and Service Accounts, WeChat Pay (APIv3 for mainland China and Global v3 for cross-border merchants), WeChat Work / WeCom (Enterprise WeChat), WeChat Channels (Video Accounts), WeChat Shop, and WeChat Cloud Hosting — addressing over a billion monthly active users primarily in China and across the WeChat international footprint.
features:
- WeChat Mini Programs framework (WXML / WXSS / JS) with native-app-grade APIs
- WeChat Mini Programs Server API on api.weixin.qq.com — code2Session, access tokens, subscribe / template / customer-service messages, content moderation, analytics, QR codes
- WeChat Pay APIv3 for direct-connect merchants — JSAPI / Native / App / H5 / Mini Program payments, refunds, transfers, profit sharing, Pay Score
- WeChat Pay APIv3 Service Provider mode for sub-merchant onboarding, combined orders, and partner-side profit sharing
- WeChat Pay Global v3 API for cross-border / international institutions and merchants
- WeChat Open Platform OAuth 2.0 login for native mobile (iOS, Android, HarmonyOS) — access tokens expire in 7200s, refresh tokens last 180 days
- WeChat Open Platform QR Login for third-party websites
- WeChat Open Platform Third-Party Platform API for ISVs operating Official Accounts and Mini Programs on behalf of merchants
- WeChat Official Accounts API — user info, template messages, materials, custom menus, QR with scene, JS-SDK
- WeChat Work / WeCom API on qyapi.weixin.qq.com — contacts, messaging, external contacts, OA, conversation archive, enterprise payments
- WeChat Cloud Hosting — containerized backend (Node.js / Go / Python / Java) with built-in WeChat API access, serverless MySQL, COS, CDN, gray deploys, logs
- WeChat Channels developer surface — livestream rooms, livestream commerce, Mini Program integration
- WeChat Shop API — SPU/SKU, orders, logistics, after-sales for the unified WeChat commerce graph
- Official Java / Go / PHP SDKs for WeChat Pay APIv3 under github.com/wechatpay-apiv3
- Postman script and CertificateDownloader CLI for WeChat Pay APIv3 onboarding
- 74 repos under github.com/wechat-miniprogram including miniprogram-demo (7.2k stars), weui-miniprogram (2.4k), api-typings (798), threejs-miniprogram (781), glass-easel component framework
- WeUI design library (github.com/Tencent/weui, 27.4k stars) — official UI components for WeChat web pages
image: https://res.wx.qq.com/op_res/9rSix1dhHfK4rW029eFr-aJZkUVtQrKZbZHsFRpeFx_aJ-mQIzZ8DvJZsI7AtZk9
layout: provider
modified: '2026-05-29'
name: WeChat
nav: Providers
network: true
overview: 'WeChat publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Pay APIv3 (Direct-Connect Merchant), Official Accounts API, Work (WeCom) API, and 3 more. Tagged areas include Messaging, Social, Payments, Mini Programs, and Mini Games.


  The WeChat catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  WeChat''s developer surface includes developer portal, documentation, API reference, getting-started guide, support, developer console, code examples, and 31 more developer resources.'
random_paper: 40
rules:
- effective_rule_count: 36
  extends:
  - spectral:asyncapi
  name: WeChat API Rules
  rule_count: 9
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 7
  slug: wechat-asyncapi-spectral-rules
score:
  band: developing
  composite: 48.6
  delta: 3.4
  facets:
    access_clarity: 57.1
    commercial_clarity: 57.1
    contract_governance: 13.6
    contract_quality: 60.7
    developer_ergonomics: 73.8
    discoverability: 64.8
    governance: 13.6
    operational_transparency: 5.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 45.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 21.9
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/wechat/refs/heads/main/screenshots/wechat-2026-06-20T201343.png
security:
- kind: domain-security
  name: Wechat Domain Security
  slug: wechat-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: wechat
tags:
- Messaging
- Social
- Payments
- Mini Programs
- Mini Games
- Official Accounts
- Enterprise Communication
- Cloud Hosting
- Video
- Identity
- China
- Super App
- Tencent
website: https://www.wechat.com/
---
