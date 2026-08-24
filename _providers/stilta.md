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
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 8.5
  scored_at: '2026-08-24'
api_count: 1
apis:
- description: First-party backend API for the Stilta / Patrona patent search platform. Live and rate-limited (600 req window observed) but undocumented publicly — no OpenAPI, no developer docs (docs_url is null; /o
  name: Stilta Platform API
  slug: stilta-platform-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/stilta-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.stilta.com/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/stilta-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.stilta.com
- group: start
  title: ''
  type: Login
  url: https://auth.stilta.com/en/login
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.stilta.com/dpa/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.stilta.com/dpa/terms
- group: operate
  title: ''
  type: Support
  url: https://www.stilta.com/contact-us
- group: company
  title: ''
  type: Blog
  url: https://www.stilta.com/news-page
- group: company
  title: ''
  type: Careers
  url: https://www.stilta.com/careers
- group: agent
  title: ''
  type: WellKnown
  url: well-known/stilta-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/stilta-authentication.yml
created: '2026-07-17'
description: Stilta is an agentic AI platform for high-stakes patent and intellectual property work, backed by a16z, NVIDIA, and Y Combinator (W26). Its agents automate evidence gathering and analysis across 180M+ patents, scientific literature, and archived web content to deliver source-cited invalidity analysis, infringement analysis, and freedom-to-operate assessments for in-house IP teams and intellectual property law firms. The platform markets a defensible first answer in roughly seventeen minutes, fully autonomous, with citations pulled from original documents. Stilta exposes a first-party backend API (api.stilta.com, "Patrona Patent Search Platform API") and a PropelAuth-based OpenID Connect identity surface at auth.stilta.com, but does not publish public developer documentation, an OpenAPI specification, or SDKs at this time. This profile was surfaced as an a16z / Y Combinator portfolio company and enriched from Stilta's public web surface.
image: https://www.stilta.com/favicon.ico
layout: provider
modified: '2026-07-21'
name: Stilta
nav: Providers
network: true
overview: 'Stilta publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Patents, Intellectual Property, Legal Tech, and Artificial Intelligence.


  Stilta''s developer surface includes support, engineering blog, authentication, and 9 more developer resources.'
random_paper: 6
score:
  band: emerging
  composite: 20.4
  delta: 0.0
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 79.6
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 20.4
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
security:
- kind: authentication
  name: Stilta Authentication
  slug: stilta-authentication
  summary_line: openIdConnect/oauth2 · 2 schemes
- kind: domain-security
  name: Stilta Domain Security
  slug: stilta-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Stilta Trust Center
  slug: stilta-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: stilta
tags:
- Company
- Patents
- Intellectual Property
- Legal Tech
- Artificial Intelligence
- Agentic AI
- Patent Search
- Prior Art
website: https://www.stilta.com
---
