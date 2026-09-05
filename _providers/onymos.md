---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.0
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: Asynchronous document-image enhancement REST API. POST /api/enhance accepts a base64-encoded image plus a preset (document, auto-crop, photo or watermark) and returns a result_url immediately; GET /ap
  name: Onymos DocEnhance API
  slug: onymos-docenhance-api
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://onymos.com/
- group: docs
  title: ''
  type: APIReference
  url: https://onymos.com/api/onymos-docenhance-endpoints/
- group: docs
  title: ''
  type: Documentation
  url: https://onymos.com/api/onymos-access-functions/
- group: operate
  title: ''
  type: Support
  url: https://onymos.com/contact-us/
- group: company
  title: ''
  type: Blog
  url: https://onymos.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://onymos.com/blog/feed/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://onymos.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://onymos.com/privacy-policy/
- group: auth
  title: ''
  type: Compliance
  url: https://onymos.com/security/
- group: build
  title: ''
  type: Packages
  url: packages/onymos-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/onymos-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/onymos-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/onymos-conformance.yml
- group: design
  title: ''
  type: Components
  url: components/onymos-components.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/onymos-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/onymos-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/onymos-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/onymos-llms.txt
- group: auth
  title: ''
  type: TrustCenter
  url: security/onymos-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/onymos-domain-security.yml
created: '2026-08-26'
description: 'Onymos is a Menlo Park, California software company that sells "Features-as-a-Service" (FaaS) — pre-built, pro-code application components that enterprise engineering teams drop into their own web, mobile and IoT apps instead of building commodity functionality from scratch. The catalog spans Access (social/OAuth 2.0 login), Biometrics, Chat, Contacts, DataStore, DeepLink, Location/geofencing, Media, Notification, Payments, Share, and a document-intelligence family — DocEnhance (image enhancement and OCR pre-processing), DocID (client-side document classification) and DocKnow (intelligent document processing). Onymos is built on a "No-Data Architecture": the software runs inside the customer''s own cloud or on-premises environment and Onymos never stores, sees, or accesses customer data, and customers may license the source code outright. Developers consume the features through JavaScript/TypeScript SDK objects (OnymosAccess, OnymosChat, OnymosUtil, OnymosPayment, OnymosDocID
  and siblings) across React, Angular, Ionic, Cordova, React Native, Flutter, Swift, Kotlin, Java, Python and Go. DocEnhance additionally exposes a documented asynchronous REST surface. Onymos states it is SOC 2 certified and HIPAA compliant, and it concentrates on healthcare, life sciences and laboratory workflows.'
image: https://onymos.com/wp-content/uploads/2021/05/onymos-social.jpg
layout: provider
modified: '2026-08-26'
name: Onymos
nav: Providers
network: true
overview: 'Onymos publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Features as a Service, SDK, Application Development, Mobile, and Document Processing.


  Onymos'' developer surface includes API reference, documentation, support, engineering blog, authentication, and 15 more developer resources.'
plans:
- name: Onymos Plans Pricing
  plan_count: 0
  slug: onymos-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Onymos Rate Limits
  slug: onymos-rate-limits
score:
  band: thin
  composite: 26.2
  coverage:
    artifact_dirs: 14
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 66.7
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 26.2
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 37.5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/onymos/refs/heads/main/screenshots/onymos-2026-09-02T150854.png
security:
- kind: authentication
  name: Onymos Authentication
  slug: onymos-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Onymos Domain Security
  slug: onymos-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Onymos Trust Center
  slug: onymos-trust-center
  summary_line: SOC 2, HIPAA
slug: onymos
tags:
- Features as a Service
- SDK
- Application Development
- Mobile
- Document Processing
- Intelligent Document Processing
- OCR
- Healthcare
- Life Sciences
- Authentication
- Chat
- Push Notifications
- Geolocation
- Payments
- IoT
- No-Data Architecture
- Components
website: https://onymos.com/
---
