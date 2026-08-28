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
  scored_at: '2026-08-26'
api_count: 2
apis:
- description: REST API for accessing iSpot.tv TV and video ad measurement data — airing occurrence, estimated spend, household and person-level impressions, attention metrics, OTT/streaming impressions, TV conversi
  name: iSpot REST API v4
  slug: ispot-rest-api-v4
- description: Server-side and client-side measurement ingest endpoints. A 1x1 GIF pixel accepts OTT/CTV/digital impression events (pi.ispot.tv) and TV conversion events (pt.ispot.tv) keyed by a client-specific trac
  name: iSpot Impression & TV Conversion Pixel API v2
  slug: ispot-impression-tv-conversion-pixel-api-v2
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: http://www.ispot.tv/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.ispot.tv/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.ispot.tv/documentation/api
- group: docs
  title: ''
  type: APIReference
  url: https://developer.ispot.tv/api/v4
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.ispot.tv/quickstarts/api
- group: start
  title: ''
  type: Login
  url: https://login.ispot.tv/
- group: operate
  title: ''
  type: Support
  url: https://www.ispot.tv/contact-us
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ispot-tv
- group: commercial
  title: ''
  type: Pricing
  url: https://www.ispot.tv/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.ispot.tv/hub/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ispot.tv/hub/agreements/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ispot.tv/hub/agreements/privacy/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.ispot.tv/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ispottv-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ispottv-domain-security.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.ispot.tv
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.ispot.tv/releases/api/v4/notes
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/ispottv-changelog.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ispottv-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ispottv-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/ispottv-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ispottv-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ispottv-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/ispottv-plans-pricing.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ispottv-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/ispottv-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/ispottv-packages.yml
- group: design
  title: ''
  type: Components
  url: components/ispottv-components.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/ispottv-sandbox.yml
created: '2026-07-17'
description: iSpot.tv is a TV and video advertising measurement company that provides end-to-end measurement unifying creative assessment, audience measurement, and outcome attribution across linear TV and streaming. Its platform draws on data from tens of millions of smart TVs and set-top boxes to track ad occurrences, impressions, share of voice, creative effectiveness, and return on ad spend for advertisers, agencies, and networks. iSpot exposes its data programmatically through the iSpot REST API (v4), documented at a dedicated developer portal with quickstarts, an API reference, a Python sample, an interactive API demo tool, and release notes. iSpot.tv is backed by Insight Partners and was added to the API Evangelist network from that portfolio.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ispottv.png
layout: provider
modified: '2026-08-13'
name: iSpot.tv
nav: Providers
network: true
overview: 'iSpot.tv publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, TV Advertising, Advertising Measurement, Analytics, and Attribution.


  iSpot.tv''s developer surface includes documentation, API reference, getting-started guide, support, pricing, engineering blog, changelog, and 22 more developer resources.'
plans:
- name: Ispottv Plans Pricing
  plan_count: 0
  slug: ispottv-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 21
  name: Ispottv Rate Limits
  slug: ispottv-rate-limits
score:
  band: developing
  composite: 39.7
  delta: 0.0
  facets:
    access_clarity: 46.1
    commercial_clarity: 46.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 60.7
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 65.8
  previous_composite: 39.7
  provenance:
    conformance: first-party
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ispottv/refs/heads/main/screenshots/ispottv-2026-07-25T222949.png
security:
- kind: authentication
  name: Ispottv Authentication
  slug: ispottv-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Ispottv Domain Security
  slug: ispottv-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Ispottv Trust Center
  slug: ispottv-trust-center
  summary_line: trust center published
slug: ispottv
tags:
- Company
- TV Advertising
- Advertising Measurement
- Analytics
- Attribution
- Media
- Marketing
- Streaming
website: http://www.ispot.tv/
---
