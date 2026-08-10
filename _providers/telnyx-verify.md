---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Telnyx Verify Agentic Access
  operation_count: 17
  slug: telnyx-verify-agentic-access
  summary_line: 17 operations · 11 acting
api_count: 3
apis:
- description: Carrier, caller-name (CNAM), and portability intelligence for a phone number.
  name: Telnyx Verify API Number Lookup API
  slug: telnyx-verify-number-lookup-api
- description: Trigger and check OTP / 2FA verifications over SMS, call, flash call, and WhatsApp.
  name: Telnyx Verify API Verify API
  slug: telnyx-verify-verify-api
- description: Reusable per-channel verification configuration and message templates.
  name: Telnyx Verify API Verify Profiles API
  slug: telnyx-verify-verify-profiles-api
artifact_total: 10
collections:
- collection_type: open
  name: Telnyx Verify and Number Lookup API
  slug: open-telnyx-verify
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/telnyx-verify-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/telnyx-verify-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/telnyx-verify-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/team-telnyx
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/telnyx
- group: company
  title: ''
  type: Website
  url: https://telnyx.com/products/verify-api
- group: docs
  title: ''
  type: Documentation
  url: https://developers.telnyx.com/docs/identity/verify/quickstart
- group: commercial
  title: ''
  type: Plans
  url: plans/telnyx-verify-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/telnyx-verify-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/telnyx-verify-finops.yml
created: '2026-07-11'
description: Telnyx Verify API is a phone-number verification and two-factor authentication (2FA / OTP) product, paired with Telnyx Number Lookup for number intelligence (carrier, line type, caller name / CNAM, and portability). Verify sends a one-time passcode over SMS, voice call, flash call, or WhatsApp and checks the code the user enters - by verification ID or by phone number - with reusable per-channel Verify Profiles and message templates, plus verification webhooks and built-in anti-fraud controls against SMS pumping and brute-force attacks. Number Lookup returns carrier and caller data for an E.164 number for routing, validation, lead enrichment, and fraud workflows. Both run on the Telnyx API v2 (https://api.telnyx.com/v2) with Bearer API-key auth. This is a product-specific treatment of the parent Telnyx cloud-communications (CPaaS) platform, whose full voice / messaging / numbers / fax / wireless surface is documented in the `telnyx` catalog entry.
finops:
- name: Telnyx Verify Finops
  service_category: Identity and Communications
  slug: telnyx-verify-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/telnyx-verify.png
layout: provider
modified: '2026-07-11'
name: Telnyx Verify API
nav: Providers
network: true
overview: 'Telnyx Verify API publishes 3 APIs on the [APIs.io](https://apis.io/) network: Number Lookup API, Verify API, and Verify Profiles API. Tagged areas include Number Verification, Phone Verification, OTP, 2FA, and Lookup.


  Telnyx Verify API''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Telnyx Verify Plans Pricing
  plan_count: 3
  slug: telnyx-verify-plans-pricing
random_paper: 106
rate_limits:
- limit_count: 4
  name: Telnyx Verify Rate Limits
  slug: telnyx-verify-rate-limits
score:
  band: thin
  composite: 36.4
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 63.6
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 36.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 16.7
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
security:
- kind: authentication
  name: Telnyx Verify Authentication
  slug: telnyx-verify-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Telnyx Verify Domain Security
  slug: telnyx-verify-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: telnyx-verify
tags:
- Number Verification
- Phone Verification
- OTP
- 2FA
- Lookup
- Verify
- Number Lookup
- CNAM
- Identity
- Anti-Fraud
website: https://telnyx.com/products/verify-api
---
