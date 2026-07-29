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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 6
  human_in_the_loop: 1
  name: Prelude So Agentic Access
  operation_count: 7
  slug: prelude-so-agentic-access
  summary_line: 7 operations · 6 acting · 1 human-in-the-loop
api_count: 4
apis:
- description: Phone number intelligence - line type, carrier, and flags.
  name: Prelude Lookup API
  slug: prelude-so-lookup-api
- description: Send transactional messages over SMS, RCS, and WhatsApp.
  name: Prelude Transactional API
  slug: prelude-so-transactional-api
- description: Create and check one-time passcode (OTP) verifications.
  name: Prelude Verification API
  slug: prelude-so-verification-api
- description: Anti-fraud risk prediction and outcome feedback.
  name: Prelude Watch API
  slug: prelude-so-watch-api
artifact_total: 10
collections:
- collection_type: open
  name: Prelude API v2
  slug: open-prelude-so
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/prelude-so-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/prelude-so-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/prelude-so
- group: company
  title: ''
  type: Website
  url: https://prelude.so
- group: docs
  title: ''
  type: Documentation
  url: https://docs.prelude.so
- group: commercial
  title: ''
  type: Plans
  url: plans/prelude-so-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/prelude-so-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/prelude-so-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://prelude.so/blog
created: '2026-07-11'
description: Prelude is a phone and email verification API - "the trust layer between your signups and your business." Its Verify API creates and checks one-time passcodes (OTP) across SMS, WhatsApp, RCS, Viber, and voice in 230+ countries, with smart multi-provider routing and built-in anti-fraud. Alongside Verify, Prelude offers Notify (transactional messaging), Lookup / Intel (phone number intelligence - line type, carrier, ported and temporary flags, CNAM), and Watch (anti-fraud risk prediction and feedback). The public REST API v2 lives at https://api.prelude.dev/v2 with Bearer API-key auth and official SDKs for Python, Node.js, Java, and Go. Prelude positions itself as a developer-first alternative to Twilio Verify.
finops:
- name: Prelude So Finops
  service_category: Identity and Anti-Fraud
  slug: prelude-so-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/prelude-so.png
layout: provider
modified: '2026-07-11'
name: Prelude
nav: Providers
network: true
overview: 'Prelude publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Lookup API, Transactional API, Verification API, and 1 more. Tagged areas include Number Verification, Phone Verification, OTP, Authentication, and Anti-Fraud.


  Prelude''s developer surface includes authentication, documentation, engineering blog, and 6 more developer resources.'
plans:
- name: Prelude So Plans Pricing
  plan_count: 3
  slug: prelude-so-plans-pricing
random_paper: 64
rate_limits:
- limit_count: 3
  name: Prelude So Rate Limits
  slug: prelude-so-rate-limits
score:
  band: thin
  composite: 34.2
  delta: -7.6
  facets:
    commercial_clarity: 39.5
    contract_quality: 60.2
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 41.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 8.3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
security:
- kind: authentication
  name: Prelude So Authentication
  slug: prelude-so-authentication
  summary_line: http · 1 scheme
slug: prelude-so
tags:
- Number Verification
- Phone Verification
- OTP
- Authentication
- Anti-Fraud
- Two-Factor Authentication
- SMS
- Phone Number Lookup
website: https://prelude.so
---
