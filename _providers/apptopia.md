---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 7.9
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: Real-time REST API exposing raw mobile app-store data — apps, publishers, parent companies, SDKs, download/revenue/usage estimates, ratings, top charts, and advertising intelligence across iTunes, Goo
  name: Apptopia Data API
  slug: apptopia-data-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://apptopia.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.apptopia.com/
- group: docs
  title: ''
  type: Documentation
  url: https://dev.apptopia.com/
- group: docs
  title: ''
  type: APIReference
  url: https://dev.apptopia.com/
- group: auth
  title: ''
  type: Authentication
  url: authentication/apptopia-authentication.yml
- group: operate
  title: ''
  type: Support
  url: https://help.apptopia.com/knowledge
- group: commercial
  title: ''
  type: Pricing
  url: https://apptopia.com/en/pricing-investors/
- group: start
  title: ''
  type: Login
  url: https://apptopia.com/users/sign_in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://apptopia.com/en/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://apptopia.com/en/privacy/
- group: auth
  title: ''
  type: Compliance
  url: https://apptopia.com/en/our-compliance
- group: company
  title: ''
  type: Blog
  url: https://apptopia.com/en/insights/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apptopia
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/apptopia-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apptopia-domain-security.yml
created: '2026-07-17'
description: Apptopia is a mobile app market-intelligence company that delivers investor-grade estimates of app downloads, revenue, usage, ratings, SDK adoption, and advertising activity across the iTunes App Store, Google Play, Tencent, Xiaomi, and Mobile 360 stores. Its data is derived from a real-user device panel and is trusted by financial institutions, ad-tech firms, and app publishers to track competitors, size markets, and validate investment theses. The Apptopia Data API exposes the raw dataset behind these estimates as JSON over HTTPS, organized into directory, discovery, time-series, entity-lookup, search, and data-export endpoints, authenticated with JSON Web Tokens.
image: https://apptopia.com/en/wp-content/uploads/2026/04/Group-10-1.png
layout: provider
modified: '2026-07-18'
name: Apptopia
nav: Providers
network: true
overview: 'Apptopia publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Mobile, App Store Intelligence, Market Intelligence, and Alternative Data.


  Apptopia''s developer surface includes documentation, API reference, authentication, support, pricing, engineering blog, and 9 more developer resources.'
random_paper: 1
rate_limits:
- limit_count: 4
  name: Apptopia Rate Limits
  slug: apptopia-rate-limits
score:
  band: thin
  composite: 31.9
  coverage:
    artifact_dirs: 13
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 46.1
    commercial_clarity: 46.1
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 45.2
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 42.1
  previous_composite: 31.9
  provenance:
    conformance: derived
    mcp: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apptopia/refs/heads/main/screenshots/apptopia-2026-07-25T200850.png
security:
- kind: authentication
  name: Apptopia Authentication
  slug: apptopia-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Apptopia Domain Security
  slug: apptopia-domain-security
  summary_line: TLSv1.2 · DMARC
slug: apptopia
tags:
- Company
- Mobile
- App Store Intelligence
- Market Intelligence
- Alternative Data
- Analytics
- Consumer Insights
- Advertising
website: https://apptopia.com
---
