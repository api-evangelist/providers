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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
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
  score: 0.0
  scored_at: '2026-08-10'
api_count: 1
apis:
- description: Implement OTP flow quickly
  name: GetOTP
  slug: getotp
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/getotp-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://otp.dev/en/docs/
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Implement OTP flow quickly
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/getotp.png
layout: provider
modified: '2026-05-28'
name: GetOTP
nav: Providers
network: true
overview: GetOTP publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Authentication And Authorization and Public APIs.
random_paper: 79
score:
  band: minimal
  composite: 5.7
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.7
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/getotp/refs/heads/main/screenshots/getotp-2026-06-20T181808.png
security:
- kind: domain-security
  name: Getotp Domain Security
  slug: getotp-domain-security
  summary_line: TLSv1.3 · DMARC
slug: getotp
tags:
- Authentication And Authorization
- Public APIs
website: https://otp.dev/en/docs/
---
