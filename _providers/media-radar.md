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
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: The MediaRadar Client API delivers MediaRadar brand, contacts and advertising data to existing clients over REST. It is fronted by Azure API Management and documented through the MediaRadar Client API
  name: MediaRadar Client API
  slug: mediaradar-client-api
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://www.mediaradar.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api-portal.mediaradar.com/
- group: start
  title: ''
  type: SignUp
  url: https://api-portal.mediaradar.com/signin
- group: company
  title: ''
  type: Blog
  url: https://www.mediaradar.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.mediaradar.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.mediaradar.com/privacy
- group: auth
  title: ''
  type: Authentication
  url: authentication/media-radar-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/media-radar-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/media-radar-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.mediaradar.com/
- group: operate
  title: ''
  type: Support
  url: https://www.mediaradar.com/customer-support
- group: design
  title: ''
  type: Conformance
  url: conformance/media-radar-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/media-radar-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/media-radar-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/media-radar-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/media-radar-rate-limits.yml
coverage:
  checked: '2026-08-12'
  detail: The MediaRadar Client API Portal is an Azure API Management developer portal whose catalog is published to signed-in clients only — its own management endpoint returns an empty collection anonymously (GET /developer/apis?api-version=2022-04-01-preview -> 200 {"value":[],"nextLink":null}), so no endpoint, schema or quota is readable without a MediaRadar client account.
  evidence:
  - status: 200
    url: https://api-portal.mediaradar.com/developer/apis?api-version=2022-04-01-preview
  - status: 200
    url: https://api-portal.mediaradar.com/developer/products?api-version=2022-04-01-preview
  - status: 404
    url: https://api.mediaradar.com/openapi.json
  - status: 404
    url: https://api-portal.mediaradar.com/openapi.json
  - status: 404
    url: https://www.mediaradar.com/.well-known/agent-card.json
  reason: customer-only-docs
  state: gated
created: '2026-07-17'
description: MediaRadar (now incorporating the data and capabilities of Vivvix) is a marketing and advertising intelligence platform that tracks advertising investment, creative, and brand activity across streaming and linear TV, digital and programmatic, social, retail media, out-of-home, radio, podcast, and print. It serves brands, agencies, publishers, platforms, and consultancies with competitive, commercial, creative, market, and political ad intelligence used to inform mission-critical marketing and sales decisions. MediaRadar delivers its data through a web UX, data feeds, and a client REST API. The MediaRadar Client API Portal is a private Azure API Management developer portal gated behind client sign-in; API endpoints and schemas are not published publicly, and integrations authenticate with a per-client API Key. This profile was surfaced as a portfolio company of Bain Capital Ventures and enriched by the API Evangelist pipeline.
image: https://www.mediaradar.com/hubfs/Website%20Featured%20Image.png
layout: provider
modified: '2026-08-12'
name: Media Radar
nav: Providers
network: true
overview: 'Media Radar publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Commerce, Advertising Intelligence, Marketing Intelligence, and Competitive Intelligence.


  Media Radar''s developer surface includes signup flow, engineering blog, authentication, support, and 12 more developer resources.'
plans:
- name: Media Radar Plans Pricing
  plan_count: 0
  slug: media-radar-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Media Radar Rate Limits
  slug: media-radar-rate-limits
score:
  band: emerging
  composite: 23.9
  coverage:
    artifact_dirs: 11
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 23.9
  provenance:
    conformance: first-party
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/media-radar/refs/heads/main/screenshots/media-radar-2026-08-07T172326.png
security:
- kind: authentication
  name: Media Radar Authentication
  slug: media-radar-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Media Radar Domain Security
  slug: media-radar-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Media Radar Trust Center
  slug: media-radar-trust-center
  summary_line: SOC 2 Type I
slug: media-radar
tags:
- Company
- Commerce
- Advertising Intelligence
- Marketing Intelligence
- Competitive Intelligence
- Advertising
- Media
- Data
website: https://www.mediaradar.com/
---
