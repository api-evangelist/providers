---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Matomo Agentic Access
  operation_count: 4
  slug: matomo-agentic-access
  summary_line: 4 operations · 2 acting
api_count: 5
apis:
- description: The Matomo Live API provides real-time access to visitor data including the most recent visits, visitor profiles, and live counters showing current visitors on the site. It enables developers to build
  name: Matomo Live API
  slug: live-api
- description: The Matomo Goals API allows developers to manage and retrieve data about conversion goals. It supports creating, updating, and deleting goals, as well as retrieving goal conversion metrics, revenue da
  name: Matomo Goals API
  slug: goals-api
- description: The Matomo Segments API enables developers to create and manage saved segments for filtering analytics data. Segments allow filtering visits and actions by any combination of visitor properties, behav
  name: Matomo Segments API
  slug: segments-api
- description: The Index.php API from Matomo — 1 operation(s) for index.php.
  name: Matomo Index.php API
  slug: matomo-index-php-api
- description: The Matomo.php API from Matomo — 1 operation(s) for matomo.php.
  name: Matomo Matomo.php API
  slug: matomo-matomo-php-api
artifact_total: 15
collections:
- collection_type: open
  name: Matomo Tracking API
  slug: open-matomo-tracking
- collection_type: open
  name: Matomo Reporting API
  slug: open-matomo
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/matomo-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/matomo-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/matomo-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/matomo-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/matomo-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/matomo
- group: company
  title: ''
  type: Website
  url: https://matomo.org
- group: docs
  title: ''
  type: Documentation
  url: https://developer.matomo.org
- group: docs
  title: ''
  type: APIDocumentation
  url: https://developer.matomo.org/api-reference/reporting-api
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.matomo.org/guides/getting-started-part-1
- group: company
  title: ''
  type: Blog
  url: https://matomo.org/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://matomo.org/pricing
- group: build
  title: ''
  type: GitHub
  url: https://github.com/matomo-org/matomo
- group: start
  title: ''
  type: Login
  url: https://matomo.org/login
- group: start
  title: ''
  type: Signup
  url: https://matomo.org/start-free-analytics-trial
- group: operate
  title: ''
  type: Support
  url: https://matomo.org/support
- group: operate
  title: ''
  type: Forums
  url: https://forum.matomo.org
- group: other
  title: ''
  type: Marketplace
  url: https://plugins.matomo.org
- group: other
  title: ''
  type: SelfHosted
  url: https://matomo.org/matomo-on-premise
- group: operate
  title: ''
  type: ChangeLog
  url: https://matomo.org/changelog
- group: build
  title: ''
  type: SDKs
  url: https://developer.matomo.org/api-reference/tracking-api-clients
- group: commercial
  title: ''
  type: TermsOfService
  url: https://matomo.org/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://matomo.org/privacy-policy
created: '2026-03-26'
description: Matomo is an open source web analytics platform that provides comprehensive website and application usage analytics with full data ownership. Formerly known as Piwik, it offers an alternative to Google Analytics with on-premise or cloud hosting options, ensuring complete control over analytics data and compliance with privacy regulations including GDPR.
finops:
- name: Matomo Finops
  service_category: API
  slug: matomo-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/matomo.png
layout: provider
modified: '2026-05-30'
name: Matomo
nav: Providers
network: true
overview: 'Matomo publishes 2 APIs on the [APIs.io](https://apis.io/) network: Index.php API and Matomo.php API. Tagged areas include Analytics, Data Ownership, Open Source, Privacy, and Self-Hosted.


  Matomo''s developer surface includes authentication, documentation, getting-started guide, engineering blog, pricing, GitHub presence, signup flow, and 16 more developer resources.'
plans:
- name: Matomo Plans Pricing
  plan_count: 3
  slug: matomo-plans-pricing
random_paper: 41
rate_limits:
- limit_count: 5
  name: Matomo Rate Limits
  slug: matomo-rate-limits
score:
  band: developing
  composite: 56.0
  delta: 0.0
  facets:
    commercial_clarity: 92.1
    contract_quality: 55.8
    developer_ergonomics: 50.0
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 56.0
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/matomo/refs/heads/main/screenshots/matomo-2026-06-20T185037.png
security:
- kind: authentication
  name: Matomo Authentication
  slug: matomo-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Matomo Domain Security
  slug: matomo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Matomo Vulnerability Disclosure
  slug: matomo-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Matomo Trust Center
  slug: matomo-trust-center
  summary_line: ISO 27001, GDPR
slug: matomo
tags:
- Analytics
- Data Ownership
- Open Source
- Privacy
- Self-Hosted
- Web Analytics
website: https://matomo.org
---
