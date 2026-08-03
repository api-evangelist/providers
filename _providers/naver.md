---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
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
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-03'
api_count: 18
apis:
- description: 'Naver Search API returns search results across Naver''s catalogs: blog, news, book, encyclopedia, café article, knowledge-in (Kin), web document, image, shopping product, and academic document. Each ca'
  name: Naver Search Open API
  slug: search
- description: Papago is Naver's neural machine translation service. The Papago N2MT API performs text translation across Korean, English, Japanese, Chinese (Simplified / Traditional), Spanish, French, German, Russi
  name: Naver Papago Translation (N2MT) API
  slug: papago-translation
- description: Papago Language Detection identifies the source language of a text snippet, used to drive automatic translation routing.
  name: Naver Papago Language Detection API
  slug: papago-detect-language
- description: Naver Login is an OAuth 2.0 identity provider used by Korean web and mobile apps to authenticate users with their Naver account and access basic profile attributes.
  name: Naver Login (OAuth 2.0) API
  slug: login
- description: Datalab API exposes search-volume trend data for keywords across Naver Search and Naver Shopping over user-defined time windows, demographic slices, and category filters.
  name: Naver Datalab API
  slug: datalab
- description: The me2.do URL shortener API converts long URLs into Naver short links for sharing across messaging and social channels.
  name: Naver Shortener (me2.do) API
  slug: short-url
- description: The CAPTCHA API issues image-based human-verification challenges and validates user responses, used by Korean sites to prevent bot abuse.
  name: Naver CAPTCHA API
  slug: captcha
- description: SmartEditor 2 is Naver's embeddable rich-text editor for blog and CMS-style applications. The integration API exposes attachment uploads, image processing, and editor lifecycle.
  name: Naver SmartEditor 2 API
  slug: smarteditor
- description: The Naver Maps Web API embeds Korean street-level mapping, markers, polylines, and geocoding in third-party web applications. (Naver Cloud Platform's Maps API hosts the production-grade map and direct
  name: Naver Maps (Web) API
  slug: maps-web
- description: Naver Cloud Platform Maps exposes geocoding, reverse geocoding, directions (driving / walking / public transit), static map images, and the dynamic JavaScript map tile service for Korean addresses and
  name: Naver Cloud Platform Maps API
  slug: maps
- description: The Papago service group on Naver Cloud Platform packages production-grade NMT translation, language detection, Korean name romanization, and Papago Image Translation.
  name: Naver Cloud Platform Papago APIs
  slug: papago
- description: CLOVA OCR detects and extracts text from images and documents — supporting general OCR, document-template OCR for IDs / receipts / business cards, and structured key / value extraction.
  name: Naver Cloud CLOVA OCR API
  slug: clova-ocr
- description: CLOVA Speech provides Korean-first speech-to-text (STT) and Korean speech synthesis (TTS / Premium Voice) APIs for contact-center, captioning, and voice-app workloads.
  name: Naver Cloud CLOVA Speech API
  slug: clova-speech
- description: HyperCLOVA X is Naver's Korean-language large language model. The HyperCLOVA X API exposes chat completion, embeddings, summarization, and tool-use endpoints for Korean-first generative AI application
  name: Naver Cloud HyperCLOVA X API
  slug: hyperclova-x
- description: SENS (Simple & Easy Notification Service) sends SMS, LMS, MMS, Alimtalk (KakaoTalk channel), Friend Talk, and push notifications to Korean recipients.
  name: Naver Cloud SENS Messaging API
  slug: sens
- description: Object Storage is Naver Cloud Platform's S3-compatible object store for unstructured data, with public read / versioning / lifecycle / CDN-origin support.
  name: Naver Cloud Object Storage API
  slug: object-storage
- description: Server is Naver Cloud Platform's IaaS compute service, with VPC and Classic deployments, GPU and bare-metal options, and standard create / scale / snapshot / image management APIs.
  name: Naver Cloud Server (Compute) API
  slug: server
- description: CDN+ and Global Edge are Naver Cloud Platform's Korean and global content delivery services, with cache configuration, purge, and traffic-reporting APIs.
  name: Naver Cloud CDN+ / Global Edge API
  slug: cdn-plus
artifact_total: 22
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/naver-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.navercorp.com/
- group: start
  title: ''
  type: ConsumerPortal
  url: https://www.naver.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.naver.com/main/
- group: other
  title: ''
  type: NaverCloudPlatform
  url: https://www.ncloud.com/
- group: docs
  title: ''
  type: NaverCloudDocs
  url: https://api.ncloud-docs.com/docs/home
- group: other
  title: ''
  type: HyperCLOVAStudio
  url: https://clovastudio.ncloud.com/
- group: other
  title: ''
  type: PapagoConsumer
  url: https://papago.naver.com/
- group: other
  title: ''
  type: NaverMaps
  url: https://map.naver.com/
- group: other
  title: ''
  type: NaverShopping
  url: https://shopping.naver.com/
- group: other
  title: ''
  type: NaverPay
  url: https://new-m.pay.naver.com/
- group: other
  title: ''
  type: NaverWebtoon
  url: https://comic.naver.com/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/naver
- group: company
  title: ''
  type: TechBlog
  url: https://d2.naver.com/home
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/naver-corporation/
- group: company
  title: ''
  type: InvestorRelations
  url: https://www.navercorp.com/en/investment
- group: company
  title: ''
  type: Newsroom
  url: https://www.navercorp.com/en/news
- group: company
  title: ''
  type: Careers
  url: https://recruit.navercorp.com/
- group: company
  title: ''
  type: Blog
  url: https://d2.naver.com/d2.atom
created: '2026-05-23'
description: 'Naver Corp. is South Korea''s largest internet company, operating the Naver search portal, Naver Webtoon, Naver Pay, Naver Maps, Naver Shopping, WORKS Mobile, and the LINE messenger platform (jointly with SoftBank via LY Corporation). Naver runs two distinct public developer surfaces: Naver Developers (developers.naver.com) which hosts Naver''s classic Open APIs — Search (blog, news, book, encyclopedia, café, knowledge, web, image, shop, doc), Papago N2MT translation, Naver Login (OAuth 2.0), Naver Maps geocoding and static map, Datalab trend, CAPTCHA, and SmartEditor; and Naver Cloud Platform (www.ncloud.com) — Naver''s IaaS / PaaS offering with Compute (Server, Container, Functions), Storage (Object, Block, File), Network (VPC, CDN+, Global Edge), AI (CLOVA Speech, CLOVA OCR, Papago, HyperCLOVA X), Maps, SENS (SMS / push messaging), Cloud Search, and Certificate Manager.'
finops:
- name: Naver Finops
  service_category: API
  slug: naver-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/naver.png
layout: provider
modified: '2026-05-23'
name: Naver
nav: Providers
network: true
overview: 'Naver publishes 18 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Search, Translation, Maps, Cloud Platform, and AI.


  Naver''s developer surface includes GitHub presence, engineering blog, and 17 more developer resources.'
plans:
- name: Naver Plans Pricing
  plan_count: 1
  slug: naver-plans-pricing
random_paper: 65
rate_limits:
- limit_count: 2
  name: Naver Rate Limits
  slug: naver-rate-limits
score:
  band: emerging
  composite: 17.2
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 17.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 8.3
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/naver/refs/heads/main/screenshots/naver-2026-06-20T190102.png
security:
- kind: domain-security
  name: Naver Domain Security
  slug: naver-domain-security
  summary_line: TLSv1.3 · DMARC
slug: naver
tags:
- Search
- Translation
- Maps
- Cloud Platform
- AI
- Korea
- OAuth2
- SMS
- OCR
- Webtoon
website: https://www.navercorp.com/
---
