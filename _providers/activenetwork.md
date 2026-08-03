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
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 9.0
  scored_at: '2026-08-03'
api_count: 1
apis:
- description: Read-only search over Active.com's public activity assets (events, races, tournaments, classes) with location, date-range, category, topic, and boolean-operator filtering. Returns JSON via HTTP GET; a
  name: ACTIVE Network Activity Search API v2
  slug: active-network-activity-search-api-v2
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.activenetwork.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.active.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.active.com/docs/Home
- group: docs
  title: ''
  type: APIReference
  url: https://developer.active.com/docs/v2_Activity_API_Search
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.active.com/member/register
- group: start
  title: ''
  type: SignUp
  url: https://developer.active.com/member/register
- group: start
  title: ''
  type: Login
  url: https://www.activenetwork.com/product-login
- group: operate
  title: ''
  type: Support
  url: https://www.activenetwork.com/support
- group: operate
  title: ''
  type: HelpCenter
  url: https://developer.active.com/help_center
- group: company
  title: ''
  type: Blog
  url: https://www.activenetwork.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.activenetwork.com/information/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.activenetwork.com/information/privacy-policy
- group: auth
  title: ''
  type: Authentication
  url: authentication/activenetwork-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/activenetwork-conventions.yml
- group: build
  title: ''
  type: Packages
  url: packages/activenetwork-packages.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/activenetwork-domain-security.yml
created: '2026-07-17'
description: ACTIVE Network is an activity and participant management software company serving more than 6,300 organizations across camps, classes, endurance events, parks and recreation, resorts and ski, swim, team sports, universities, and YMCAs. Its product suite includes ACTIVENet recreation management, Camp & Class Manager, ACTIVEWorks Endurance event management, Payment Manager, JumpForward NCAA compliance, and RTP|One resort management. For developers, ACTIVE Network operates a Mashery-hosted developer program exposing a family of read-only Activity Distribution APIs (Activity, Activity Search v2, Campground) that surface Active.com event, race, class, and campground data via simple api_key-authenticated HTTP GET requests.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/activenetwork.png
layout: provider
modified: '2026-07-17'
name: ACTIVE Network
nav: Providers
network: true
overview: 'ACTIVE Network publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Activities, Events, Recreation, and Registration.


  ACTIVE Network''s developer surface includes documentation, API reference, getting-started guide, signup flow, support, engineering blog, authentication, and 9 more developer resources.'
random_paper: 84
score:
  band: emerging
  composite: 24.1
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 52.2
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 24.1
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/activenetwork/refs/heads/main/screenshots/activenetwork-2026-07-25T181528.png
security:
- kind: authentication
  name: Activenetwork Authentication
  slug: activenetwork-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Activenetwork Domain Security
  slug: activenetwork-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: activenetwork
tags:
- Company
- Activities
- Events
- Recreation
- Registration
- Endurance
- Campgrounds
- Sports
- Search
website: https://www.activenetwork.com
---
