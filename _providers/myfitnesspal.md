---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.3
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: Partner REST API for reading and writing a consenting user's food and exercise diary, body measurements, and profile, plus webhook subscriptions for data-change notifications. OAuth 2.0 authorization-
  name: MyFitnessPal API v2
  slug: myfitnesspal-api-v2
artifact_total: 7
asyncapis:
- description: Webhook notifications delivered by MyFitnessPal to partner applications when a subscribed user's data changes. A single POST may batch notifications about multiple items belonging to multiple users (u
  name: MyFitnessPal Subscription Notifications
  slug: myfitnesspal-notifications-asyncapi
common:
- group: company
  title: ''
  type: Website
  url: http://www.myfitnesspal.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://myfitnesspalapi.com
- group: docs
  title: ''
  type: Documentation
  url: https://myfitnesspalapi.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://myfitnesspalapi.com/docs
- group: company
  title: ''
  type: Blog
  url: https://blog.myfitnesspal.com
- group: operate
  title: ''
  type: Support
  url: https://support.myfitnesspal.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.myfitnesspal.com/premium
- group: start
  title: ''
  type: SignUp
  url: https://www.myfitnesspal.com/account/create
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.myfitnesspal.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.myfitnesspal.com/privacy-policy
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/myfitnesspal-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/myfitnesspal-well-known.yml
- group: auth
  title: ''
  type: Security
  url: https://bugcrowd.com/engagements/myfitnesspal-mbb
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/myfitnesspal-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/myfitnesspal-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/myfitnesspal-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/myfitnesspal-llms.txt
created: '2026-07-17'
description: MyFitnessPal is a nutrition and fitness tracking platform built around a food diary, calorie counting, a large branded-food and barcode database, exercise logging, weight and body measurements, and goal setting. Its partner-facing REST API (v2, hosted at api.myfitnesspal.com) lets approved applications read and write a consenting user's diary (food and exercise), body measurements, and profile, and subscribe to webhook notifications when that data changes. Access uses OAuth 2.0 authorization-code grants with the diary, measurements, private-exercises, and subscriptions scopes. The developer program is currently closed to new applicants. This profile was surfaced as a portfolio lead and enriched by the API Evangelist pipeline.
image: https://www.myfitnesspal.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: MyFitnessPal MCP Server
  slug: myfitnesspal-mcp-server
modified: '2026-07-20'
name: MyFitnessPal
nav: Providers
network: true
overview: 'MyFitnessPal publishes 1 API on the [APIs.io](https://apis.io/) network: API v2. Tagged areas include Company, Consumer, Health and Fitness, Nutrition, and Fitness Tracking.


  The MyFitnessPal catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  MyFitnessPal''s developer surface includes documentation, API reference, engineering blog, support, pricing, signup flow, and 11 more developer resources.'
random_paper: 9
scopes:
- name: Myfitnesspal Scopes
  scope_count: 4
  slug: myfitnesspal-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: developing
  composite: 46.8
  delta: 5.8
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 4.5
    contract_quality: 42.6
    developer_ergonomics: 47.0
    discoverability: 87.0
    governance: 4.5
    operational_transparency: 18.4
  previous_composite: 41.0
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 60.0
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/myfitnesspal/refs/heads/main/screenshots/myfitnesspal-2026-08-07T184519.png
security:
- kind: authentication
  name: Myfitnesspal Authentication
  slug: myfitnesspal-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Myfitnesspal Domain Security
  slug: myfitnesspal-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Myfitnesspal Vulnerability Disclosure
  slug: myfitnesspal-vulnerability-disclosure
  summary_line: Bugcrowd · security.txt · contact published
slug: myfitnesspal
tags:
- Company
- Consumer
- Health and Fitness
- Nutrition
- Fitness Tracking
- Food Diary
- Wellness
- Webhook
- Authentication
website: http://www.myfitnesspal.com
---
