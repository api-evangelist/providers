---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: verified
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.7
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Cover Genius Agentic Access
  operation_count: 8
  slug: cover-genius-agentic-access
  summary_line: 8 operations · 7 acting
api_count: 3
apis:
- description: HTTP POST webhook callbacks notifying partner listener URLs of policy lifecycle events (BOOKING_CREATED, BOOKING_UPDATED, BOOKING_CANCELLED, and renewal events), HMAC-SHA256 signed for verification.
  name: XCover Webhooks and Events
  slug: xcover-webhooks
- description: The Bookings API from Cover Genius — 5 operation(s) for bookings.
  name: Cover Genius Bookings API
  slug: cover-genius-bookings-api
- description: The Offers API from Cover Genius — 2 operation(s) for offers.
  name: Cover Genius Offers API
  slug: cover-genius-offers-api
artifact_total: 10
collections:
- collection_type: open
  name: Cover Genius XCover API
  slug: open-cover-genius
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cover-genius-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cover-genius-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cover-genius-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cover-genius
- group: company
  title: ''
  type: Website
  url: https://www.covergenius.com
- group: docs
  title: ''
  type: Documentation
  url: https://partner-docs.covergenius.com
- group: commercial
  title: ''
  type: Plans
  url: plans/cover-genius-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cover-genius-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/cover-genius-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://covergenius.com/resources/blog/
created: '2026-06-20'
description: Cover Genius is an insurtech company providing embedded insurance and protection at the point of sale. The XCover distribution API lets partners create insurance offers, confirm bookings, modify and cancel policies, and receive policy lifecycle webhooks, while the XClaim API handles claims intake and instant payments.
finops:
- name: Cover Genius Finops
  service_category: Insurance and Financial Services
  slug: cover-genius-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cover-genius.png
layout: provider
modified: '2026-06-20'
name: Cover Genius
nav: Providers
network: true
overview: 'Cover Genius publishes 2 APIs on the [APIs.io](https://apis.io/) network: Bookings API and Offers API. Tagged areas include Insurance, Insurtech, Embedded Insurance, Protection, and Claims.


  Cover Genius'' developer surface includes authentication, documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Cover Genius Plans Pricing
  plan_count: 1
  slug: cover-genius-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 3
  name: Cover Genius Rate Limits
  slug: cover-genius-rate-limits
score:
  band: thin
  composite: 33.9
  delta: -3.4
  facets:
    commercial_clarity: 28.9
    contract_quality: 60.2
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 37.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 18.2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cover-genius/refs/heads/main/screenshots/cover-genius-2026-06-20T175139.png
security:
- kind: authentication
  name: Cover Genius Authentication
  slug: cover-genius-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Cover Genius Domain Security
  slug: cover-genius-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cover-genius
tags:
- Insurance
- Insurtech
- Embedded Insurance
- Protection
- Claims
website: https://www.covergenius.com
---
