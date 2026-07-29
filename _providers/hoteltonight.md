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
    asyncapi_events: false
    auth_clarity: true
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
  score: 9.0
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: Private partner/agent API used by hotels to manage inventory, rates, and availability with HotelTonight. Access is gated behind partner credentials (HTTP Basic auth); no public OpenAPI specification i
  name: HotelTonight Partner API
  slug: hoteltonight-partner-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/hoteltonight-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.hoteltonight.com/terms-of-use/security
- group: company
  title: ''
  type: Website
  url: https://www.hoteltonight.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api-docs.hoteltonight.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api-docs.hoteltonight.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hoteltonight
- group: operate
  title: ''
  type: Support
  url: https://www.hoteltonight.com/customer-support
- group: start
  title: ''
  type: SignUp
  url: https://www.hoteltonight.com/hotel-partners
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.hoteltonight.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hoteltonight.com/terms-of-use/privacy-policy
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hoteltonight-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/hoteltonight-authentication.yml
created: '2026-07-17'
description: HotelTonight is a last-minute hotel booking service, now part of Airbnb, that lets travelers discover and reserve same-day and near-term hotel deals across thousands of properties worldwide through its consumer mobile apps and website. For hotels, HotelTonight operates a partner (extranet) program and a private agent/partner API used to manage inventory, rates, and availability. The API surface is gated behind partner authentication (HTTP Basic auth at the partner documentation portal and an agent sign-in at api.hoteltonight.com); HotelTonight does not publish an open, self-service developer API, an OpenAPI/Swagger spec, first-party client SDKs, or a public /.well-known discovery surface. This API Evangelist profile was surfaced as a Battery Ventures portfolio company and enriched by probing the provider's real public surfaces.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hoteltonight.png
layout: provider
modified: '2026-07-19'
name: HotelTonight
nav: Providers
network: true
overview: 'HotelTonight publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Travel, Hotels, Booking, and Hospitality.


  HotelTonight''s developer surface includes documentation, support, signup flow, authentication, and 8 more developer resources.'
random_paper: 9
score:
  band: emerging
  composite: 22.3
  delta: -2.4
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 32.6
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 15.8
  previous_composite: 24.7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hoteltonight/refs/heads/main/screenshots/hoteltonight-2026-07-25T221516.png
security:
- kind: authentication
  name: Hoteltonight Authentication
  slug: hoteltonight-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Hoteltonight Domain Security
  slug: hoteltonight-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Hoteltonight Vulnerability Disclosure
  slug: hoteltonight-vulnerability-disclosure
  summary_line: disclosure policy published
slug: hoteltonight
tags:
- Company
- Travel
- Hotels
- Booking
- Hospitality
- Partner API
- Airbnb
website: https://www.hoteltonight.com
---
