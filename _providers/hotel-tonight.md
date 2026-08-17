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
  scored_at: '2026-08-17'
api_count: 1
apis:
- description: Auth-gated partner/agent API portal for HotelTonight hotel supply and booking operations. Requires partner-agent credentials; no public OpenAPI is published.
  name: HotelTonight Partner API
  slug: hoteltonight-partner-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.hoteltonight.com
- group: operate
  title: ''
  type: Support
  url: https://www.hoteltonight.com/customer-support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.hoteltonight.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hoteltonight.com/terms-of-use/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hoteltonight
- group: auth
  title: ''
  type: Security
  url: https://www.hoteltonight.com/terms-of-use/security
- group: auth
  title: ''
  type: Compliance
  url: https://www.hoteltonight.com/terms-of-use/security
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/hotel-tonight-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hotel-tonight-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/hotel-tonight-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hotel-tonight-llms.txt
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api-docs.hoteltonight.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api-docs.hoteltonight.com/
- group: start
  title: ''
  type: SignUp
  url: https://www.hoteltonight.com/hotel-partners
- group: auth
  title: ''
  type: Authentication
  url: authentication/hotel-tonight-authentication.yml
created: '2026-07-17'
description: HotelTonight is a last-minute hotel booking service founded in 2010 in San Francisco and acquired by Airbnb in 2019 for a reported $400 million. Through its mobile app and website it offers curated same-day and near-term deals on boutique, independent, and chain hotels across thousands of cities worldwide, with more than 15 million app downloads. Its developer surface is a partner/agent-facing portal (api-docs.hoteltonight.com) rather than a publicly documented API; this profile is maintained in the API Evangelist network as an enrichment lead.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hotel-tonight.png
layout: provider
modified: '2026-08-08'
name: Hotel Tonight
nav: Providers
network: true
overview: 'Hotel Tonight publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Travel, Hotels, and Booking.


  Hotel Tonight''s developer surface includes support, documentation, signup flow, authentication, and 11 more developer resources.'
random_paper: 9
score:
  band: emerging
  composite: 26.1
  delta: 0.0
  facets:
    commercial_clarity: 42.1
    contract_quality: 0.0
    developer_ergonomics: 32.6
    discoverability: 75.9
    governance: 12.5
    operational_transparency: 15.8
  previous_composite: 26.1
  provenance:
    conformance: first-party
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hotel-tonight/refs/heads/main/screenshots/hotel-tonight-2026-07-25T221516.png
security:
- kind: authentication
  name: Hotel Tonight Authentication
  slug: hotel-tonight-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Hotel Tonight Domain Security
  slug: hotel-tonight-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Hotel Tonight Vulnerability Disclosure
  slug: hotel-tonight-vulnerability-disclosure
  summary_line: disclosure policy published
slug: hotel-tonight
tags:
- Company
- Consumer
- Travel
- Hotels
- Booking
- Hospitality
- Mobile
- Airbnb
website: https://www.hoteltonight.com
---
