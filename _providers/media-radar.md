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
api_count: 0
artifact_total: 3
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
created: '2026-07-17'
description: MediaRadar (now incorporating the data and capabilities of Vivvix) is a marketing and advertising intelligence platform that tracks advertising investment, creative, and brand activity across streaming and linear TV, digital and programmatic, social, retail media, out-of-home, radio, podcast, and print. It serves brands, agencies, publishers, platforms, and consultancies with competitive, commercial, creative, market, and political ad intelligence used to inform mission-critical marketing and sales decisions. MediaRadar delivers its data through a web UX, data feeds, and a client REST API. The MediaRadar Client API Portal is a private Azure API Management developer portal gated behind client sign-in; API endpoints and schemas are not published publicly, and integrations authenticate with a per-client API Key. This profile was surfaced as a portfolio company of Bain Capital Ventures and enriched by the API Evangelist pipeline.
image: https://www.mediaradar.com/hubfs/Website%20Featured%20Image.png
layout: provider
modified: '2026-07-20'
name: Media Radar
nav: Providers
network: true
overview: 'Media Radar is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Commerce, Advertising Intelligence, Marketing Intelligence, and Competitive Intelligence.


  Media Radar''s developer surface includes signup flow, engineering blog, authentication, and 7 more developer resources.'
random_paper: 34
score:
  band: emerging
  composite: 19.3
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 0.0
    developer_ergonomics: 21.7
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 19.3
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
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
