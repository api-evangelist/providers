---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 30.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Cover Genius Agentic Access
  operation_count: 8
  slug: cover-genius-agentic-access
  summary_line: 8 operations · 7 acting
api_count: 1
apis:
- description: HTTP POST webhook callbacks notifying partner listener URLs of policy lifecycle events (BOOKING_CREATED, BOOKING_UPDATED, BOOKING_CANCELLED, and renewal events), HMAC-SHA256 signed for verification.
  name: XCover Webhooks and Events
  slug: xcover-webhooks
- baseURL: https://api.xcover.com/x
  baseurl_source: declared
  description: The Bookings API from Cover Genius — 5 operation(s) for bookings.
  name: Cover Genius Bookings API
  slug: cover-genius-bookings-api
- baseURL: https://api.xcover.com/x
  baseurl_source: declared
  description: The Offers API from Cover Genius — 2 operation(s) for offers.
  name: Cover Genius Offers API
  slug: cover-genius-offers-api
artifact_total: 13
collections:
- collection_type: open
  name: Cover Genius XCover Bookings API
  slug: open-cover-genius-bookings-api
- collection_type: open
  name: Cover Genius XCover Bookings Offers API
  slug: open-cover-genius-offers-api
- collection_type: open
  name: Cover Genius XCover API
  slug: open-cover-genius
common:
- group: other
  href: https://artifacts.apis.io/cover-genius/capabilities/cover-genius-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/cover-genius-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/cover-genius/agentic-access/cover-genius-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/cover-genius-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/cover-genius/security/cover-genius-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cover-genius-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/cover-genius/authentication/cover-genius-authentication.yml
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
  href: https://artifacts.apis.io/cover-genius/plans/cover-genius-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cover-genius-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/cover-genius/rate-limits/cover-genius-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/cover-genius-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/cover-genius/finops/cover-genius-finops.yml
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
- has_sources: true
  method: generated
  name: Cover Genius Finops
  primary_unit: ''
  service_category: Insurance and Financial Services
  slug: cover-genius-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cover-genius.png
layout: provider
modified: '2026-06-20'
name: Cover Genius
nav: Providers
network: true
overview: 'Cover Genius publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network, including Bookings API, Offers API, and 1 more. Tagged areas include Insurance, Insurtech, Embedded Insurance, Protection, and Claims.


  The Cover Genius catalog on APIs.io includes 1 Spectral governance ruleset.


  Cover Genius'' developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Cover Genius Plans Pricing
  plan_count: 1
  slug: cover-genius-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 3
  name: Cover Genius Rate Limits
  slug: cover-genius-rate-limits
rules:
- authorship: generated
  effective_rule_count: 101
  extends:
  - spectral:oas
  name: Cover Genius API Rules
  rule_count: 60
  severity_counts:
    error: 58
    hint: 0
    info: 1
    warn: 1
  slug: cover-genius-rules
score:
  band: thin
  composite: 27.9
  coverage:
    artifact_dirs: 17
    catalog_earned: 46.5
    catalog_earned_first_party: 0.0
    catalog_gap: 68.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 5.3
    contract_governance: 13.6
    contract_quality: 51.1
    developer_ergonomics: 32.1
    discoverability: 66.1
    operational_transparency: 7.9
  previous_composite: 27.9
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
    score: 10.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/cover-genius/cover-genius-2026-06-20T175139.png
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
