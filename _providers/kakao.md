---
access_model:
  confidence: medium
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 5
  human_in_the_loop: 1
  name: Kakao Agentic Access
  operation_count: 14
  slug: kakao-agentic-access
  summary_line: 14 operations · 5 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: Kakao Login is Korea's most widely used social-identity provider, built on OAuth 2.0 / OpenID Connect. The API issues access and refresh tokens, returns user profile attributes (nickname, profile imag
  name: Kakao Login (OAuth 2.0) API
  slug: kakao-login
- description: Kakao Sync extends Kakao Login with a one-click signup experience that simultaneously creates an in-app account and (optionally) adds a KakaoTalk Channel friendship for Korean services.
  name: Kakao Sync API
  slug: kakao-sync
- description: KakaoTalk Sharing lets external apps and websites share rich "Feed", "List", "Location", "Calendar", "Commerce", and custom-template messages into KakaoTalk chats.
  name: KakaoTalk Sharing API
  slug: kakaotalk-share
- description: KakaoTalk Message sends template-based messages from a Kakao-Linked app to the authenticated user themselves or to consenting KakaoTalk friends.
  name: KakaoTalk Message API
  slug: kakaotalk-message
- description: KakaoTalk Channel APIs manage a brand's Channel relationship with users — including add-friend status, Alimtalk-style notification messages (delivered via Kakao's BizMessage partners), and consult rou
  name: KakaoTalk Channel API
  slug: kakaotalk-channel
- description: Returns the list of KakaoTalk friends who have also signed into a Kakao-Linked app, for friend-picker, invite, and social-feature experiences subject to user consent.
  name: KakaoTalk Friends API
  slug: kakaotalk-friends
- description: KakaoStory APIs let apps publish posts and read user content on Kakao's social timeline product (legacy but still supported in Korea).
  name: KakaoStory API
  slug: kakaostory
- description: Kakao Local API offers address-to-coordinate (and reverse) geocoding, keyword and category place search, and administrative-region lookup for Korean addresses and POIs.
  name: Kakao Local API
  slug: local
- description: KakaoMap exposes Korean tile maps, markers, overlays, static maps, and roadview / panorama services for web and mobile applications.
  name: KakaoMap Web / JavaScript SDK
  slug: kakaomap-web
- description: KakaoNavi exposes driving directions, multi-waypoint route planning, ETA, and Future Driving directions (predictive ETA), and a native "Send to Kakao Navi" handoff for Korean mobile apps.
  name: KakaoNavi (Driving Directions) API
  slug: kakaonavi
- description: Daum Search API returns search results from Daum's web, vClip video, image, blog, book, café, and Q&A indexes, complementing Kakao Local for content discovery.
  name: Daum Search API
  slug: daum-search
- description: KakaoPay Online (also known as KakaoPay Easy-Pay) lets online merchants accept KakaoPay wallet payments for one-time and subscription purchases, with order create, approve, cancel, and refund operatio
  name: KakaoPay Online (Easy-Pay) API
  slug: kakaopay-online
- description: Subscription Payments API enables recurring KakaoPay billing for SaaS, content, and membership models — using a one-time SID (subscription ID) handshake followed by server-side recurring charge calls.
  name: KakaoPay Subscription Payments API
  slug: kakaopay-subscription
- description: KakaoPay PG is the full Korean payment-gateway product offering card, bank-transfer, point, and KakaoPay wallet acceptance for enterprise merchants.
  name: KakaoPay PG (Payment Gateway) API
  slug: kakaopay-pg
- description: KoGPT is Kakao Brain's Korean-language large language model. The KoGPT API provides text generation, summarization, paraphrasing, and classification for Korean text.
  name: KoGPT API
  slug: kogpt
- description: Karlo is Kakao Brain's diffusion-based text-to-image generation API, supporting Korean and English prompts and multiple aspect ratios.
  name: Karlo (Text-to-Image) API
  slug: karlo
- description: KakaoMobility's Business API powers KakaoT corporate mobility — letting enterprise platforms book Kakao T taxi rides, manage corporate accounts, and reconcile employee trips for expense and HR systems
  name: KakaoMobility Business API
  slug: kakaomobility-business
- baseURL: https://kapi.kakao.com
  baseurl_source: declared
  description: Kakao Login OAuth 2.0 authorization, token, and logout flows.
  name: Kakao OAuth API
  slug: kakao-oauth-api
- baseURL: https://kapi.kakao.com
  baseurl_source: declared
  description: OpenID Connect discovery, JWKS, and user info.
  name: Kakao OIDC API
  slug: kakao-oidc-api
- baseURL: https://kapi.kakao.com
  baseurl_source: declared
  description: Manage Kakao Sync service-terms consent.
  name: Kakao Service Terms API
  slug: kakao-service-terms-api
- baseURL: https://kapi.kakao.com
  baseurl_source: declared
  description: Logged-in user information, scopes, and account linking.
  name: Kakao User API
  slug: kakao-user-api
artifact_total: 33
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Kakao Login REST OAuth API
  slug: open-kakao-oauth-api
- collection_type: open
  name: Kakao Login REST OAuth OIDC API
  slug: open-kakao-oidc-api
- collection_type: open
  name: Kakao Login REST OAuth Service Terms API
  slug: open-kakao-service-terms-api
- collection_type: open
  name: Kakao Login REST OAuth User API
  slug: open-kakao-user-api
- collection_type: open
  name: Kakao Login REST API
  slug: open-kakao
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/kakao-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/kakao-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kakao-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/kakao-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.kakaocorp.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.kakao.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.kakao.com/docs
- group: other
  title: ''
  type: KakaoTalk
  url: https://www.kakaocorp.com/page/service/service/KakaoTalk
- group: other
  title: ''
  type: KakaoMapWeb
  url: https://apis.map.kakao.com/
- group: other
  title: ''
  type: KakaoPayDevelopers
  url: https://developers.kakaopay.com/
- group: other
  title: ''
  type: KakaoMobility
  url: https://www.kakaomobility.com/
- group: other
  title: ''
  type: KakaoCloud
  url: https://www.kakaocloud.com/
- group: other
  title: ''
  type: KakaoBrain
  url: https://www.kakaobrain.com/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/kakao
- group: company
  title: ''
  type: TechBlog
  url: https://tech.kakao.com/
- group: company
  title: ''
  type: InvestorRelations
  url: https://www.kakaocorp.com/page/ir/
- group: company
  title: ''
  type: Newsroom
  url: https://www.kakaocorp.com/page/detail
- group: company
  title: ''
  type: Careers
  url: https://careers.kakao.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/kakaocorp/
- group: company
  title: ''
  type: Blog
  url: https://tech.kakao.com/feed/
created: '2026-05-23'
description: Kakao Corp. is the South Korean technology group behind KakaoTalk — the dominant mobile messenger in Korea — along with KakaoPay (payments), Kakao Bank (digital bank), KakaoMobility (taxi, navigation, parking), KakaoMap, Kakao Games, Kakao Entertainment (Melon, Kakao Webtoon, Daum), and KakaoCloud. Kakao runs its public developer platform at developers.kakao.com, exposing REST APIs for Kakao Login (OAuth 2.0), Kakao Sync, KakaoTalk Share / Message / Friend Picker / Channel, KakaoStory, KakaoNavi, KakaoMap, Local search, Daum Search, KakaoPay (PG / online easy-pay), and KoGPT generative AI. KakaoMobility and Kakao Enterprise / KakaoCloud each operate additional partner- facing developer surfaces.
finops:
- name: Kakao Finops
  service_category: API
  slug: kakao-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kakao.png
layout: provider
modified: '2026-05-23'
name: Kakao
nav: Providers
network: true
overview: 'Kakao publishes 4 APIs on the [APIs.io](https://apis.io/) network, including OAuth API, OIDC API, Service Terms API, and 1 more. Tagged areas include Messaging, Maps, Navigation, Payments, and Search.


  Kakao''s developer surface includes authentication, documentation, GitHub presence, engineering blog, and 16 more developer resources.'
plans:
- name: Kakao Plans Pricing
  plan_count: 1
  slug: kakao-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 2
  name: Kakao Rate Limits
  slug: kakao-rate-limits
score:
  band: thin
  composite: 33.9
  coverage:
    artifact_dirs: 11
    catalog_earned: 56.0
    catalog_earned_first_party: 0.0
    catalog_gap: 59.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 53.1
    developer_ergonomics: 33.3
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 33.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 18.8
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kakao/refs/heads/main/screenshots/kakao-2026-06-20T183903.png
security:
- kind: authentication
  name: Kakao Authentication
  slug: kakao-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Kakao Domain Security
  slug: kakao-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: kakao
tags:
- Messaging
- Maps
- Navigation
- Payments
- Search
- Korea
- Identity
- Authentication
- KakaoTalk
- LLM
website: https://www.kakaocorp.com/
---
