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
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-24'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://www.authy.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.twilio.com/en-us/user-authentication-identity/verify
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/twilio
- group: operate
  title: ''
  type: Support
  url: https://help.twilio.com
- group: build
  title: ''
  type: Packages
  url: packages/authy-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/authy-packages.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/authy-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/authy-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/authy-domain-security.yml
created: '2026-07-17'
description: Authy is a two-factor authentication (2FA) product originally built by Authy Inc. and acquired by Twilio in 2015. It provided a consumer authenticator app (TOTP soft tokens, encrypted cloud backup, and multi-device sync) alongside a developer-facing Authy API for one-time passwords over SMS and voice, soft tokens, and push authentication. Twilio has since folded the Authy developer API into the Twilio Verify API, deprecated and archived the first-party Authy client SDKs, and discontinued the Authy desktop applications in 2024. The consumer Authy mobile app remains available. New integrations are directed to Twilio Verify. This profile was surfaced as a portfolio-company lead and is enriched here from Authy's remaining public surface (marketing site, archived GitHub organization, and deprecated SDK registries).
image: https://avatars.githubusercontent.com/u/109142?v=4
layout: provider
modified: '2026-07-18'
name: Authy
nav: Providers
network: true
overview: 'Authy is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Authentication, Two-Factor Authentication, 2FA, and Identity.


  Authy''s developer surface includes documentation, support, and 7 more developer resources.'
random_paper: 9
score:
  band: emerging
  composite: 11.0
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 13.2
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 11.0
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/authy/refs/heads/main/screenshots/authy-2026-07-25T201810.png
security:
- kind: domain-security
  name: Authy Domain Security
  slug: authy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: authy
tags:
- Company
- Authentication
- Two-Factor Authentication
- 2FA
- Identity
- Security
- One-Time Password
- TOTP
- Verification
- Push Authentication
website: https://www.authy.com
---
