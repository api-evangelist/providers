---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 42.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 39
  human_in_the_loop: 2
  name: Astrocal Dev Agentic Access
  operation_count: 79
  slug: astrocal-dev-agentic-access
  summary_line: 79 operations · 39 acting · 2 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.astrocal.dev
  baseurl_source: declared
  description: The Activity API from Astrocal — 1 operation(s) for activity.
  name: Astrocal Activity API
  slug: astrocal-dev-activity-api
- baseURL: https://api.astrocal.dev
  baseurl_source: declared
  description: The API Keys API from Astrocal — 2 operation(s) for api keys.
  name: Astrocal API Keys API
  slug: astrocal-dev-api-keys-api
- baseURL: https://api.astrocal.dev
  baseurl_source: declared
  description: The Availability API from Astrocal — 2 operation(s) for availability.
  name: Astrocal Availability API
  slug: astrocal-dev-availability-api
- baseURL: https://api.astrocal.dev
  baseurl_source: declared
  description: The Booking Pages API from Astrocal — 2 operation(s) for booking pages.
  name: Astrocal Booking Pages API
  slug: astrocal-dev-booking-pages-api
- baseURL: https://api.astrocal.dev
  baseurl_source: declared
  description: The Bookings API from Astrocal — 7 operation(s) for bookings.
  name: Astrocal Bookings API
  slug: astrocal-dev-bookings-api
- baseURL: https://api.astrocal.dev
  baseurl_source: declared
  description: The Branding API from Astrocal — 2 operation(s) for branding.
  name: Astrocal Branding API
  slug: astrocal-dev-branding-api
- baseURL: https://api.astrocal.dev
  baseurl_source: declared
  description: The Calendars API from Astrocal — 7 operation(s) for calendars.
  name: Astrocal Calendars API
  slug: astrocal-dev-calendars-api
- baseURL: https://api.astrocal.dev
  baseurl_source: declared
  description: The Conferencing API from Astrocal — 4 operation(s) for conferencing.
  name: Astrocal Conferencing API
  slug: astrocal-dev-conferencing-api
- baseURL: https://api.astrocal.dev
  baseurl_source: declared
  description: The Event Type Hosts API from Astrocal — 2 operation(s) for event type hosts.
  name: Astrocal Event Type Hosts API
  slug: astrocal-dev-event-type-hosts-api
- baseURL: https://api.astrocal.dev
  baseurl_source: declared
  description: The Event Types API from Astrocal — 3 operation(s) for event types.
  name: Astrocal Event Types API
  slug: astrocal-dev-event-types-api
- baseURL: https://api.astrocal.dev
  baseurl_source: declared
  description: The Organizations API from Astrocal — 3 operation(s) for organizations.
  name: Astrocal Organizations API
  slug: astrocal-dev-organizations-api
- baseURL: https://api.astrocal.dev
  baseurl_source: declared
  description: The Payments API from Astrocal — 2 operation(s) for payments.
  name: Astrocal Payments API
  slug: astrocal-dev-payments-api
- baseURL: https://api.astrocal.dev
  baseurl_source: declared
  description: The Stripe API from Astrocal — 5 operation(s) for stripe.
  name: Astrocal Stripe API
  slug: astrocal-dev-stripe-api
- baseURL: https://api.astrocal.dev
  baseurl_source: declared
  description: The Subscription API from Astrocal — 4 operation(s) for subscription.
  name: Astrocal Subscription API
  slug: astrocal-dev-subscription-api
- baseURL: https://api.astrocal.dev
  baseurl_source: declared
  description: The Support API from Astrocal — 1 operation(s) for support.
  name: Astrocal Support API
  slug: astrocal-dev-support-api
- baseURL: https://api.astrocal.dev
  baseurl_source: declared
  description: The Team API from Astrocal — 6 operation(s) for team.
  name: Astrocal Team API
  slug: astrocal-dev-team-api
- baseURL: https://api.astrocal.dev
  baseurl_source: declared
  description: The Test Data API from Astrocal — 1 operation(s) for test data.
  name: Astrocal Test Data API
  slug: astrocal-dev-test-data-api
- baseURL: https://api.astrocal.dev
  baseurl_source: declared
  description: The Usage API from Astrocal — 2 operation(s) for usage.
  name: Astrocal Usage API
  slug: astrocal-dev-usage-api
- baseURL: https://api.astrocal.dev
  baseurl_source: declared
  description: The Waitlist API from Astrocal — 2 operation(s) for waitlist.
  name: Astrocal Waitlist API
  slug: astrocal-dev-waitlist-api
- baseURL: https://api.astrocal.dev
  baseurl_source: declared
  description: The Webhooks API from Astrocal — 6 operation(s) for webhooks.
  name: Astrocal Webhooks API
  slug: astrocal-dev-webhooks-api
artifact_total: 27
common:
- group: agent
  href: https://artifacts.apis.io/astrocal-dev/agentic-access/astrocal-dev-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/astrocal-dev-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/astrocal-dev/rate-limits/astrocal-dev-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/astrocal-dev-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/astrocal-dev/plans/astrocal-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/astrocal-dev-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/astrocal-dev/rules/astrocal-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/astrocal-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/astrocal-dev/vocabulary/astrocal-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/astrocal-dev-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/astrocal-dev/components/astrocal-dev-components.yml
  title: ''
  type: Components
  url: components/astrocal-dev-components.yml
- group: operate
  href: https://artifacts.apis.io/astrocal-dev/changelog/astrocal-dev-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/astrocal-dev-changelog.yml
- group: start
  href: https://artifacts.apis.io/astrocal-dev/sandbox/astrocal-dev-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/astrocal-dev-sandbox.yml
- group: auth
  href: https://artifacts.apis.io/astrocal-dev/authentication/astrocal-dev-authentication.yml
  title: ''
  type: Authentication
  url: authentication/astrocal-dev-authentication.yml
- group: design
  href: https://artifacts.apis.io/astrocal-dev/errors/astrocal-dev-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/astrocal-dev-problem-types.yml
- group: design
  href: https://artifacts.apis.io/astrocal-dev/conformance/astrocal-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/astrocal-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/astrocal-dev/llms/astrocal-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/astrocal-dev-llms.txt
- group: agent
  href: https://artifacts.apis.io/astrocal-dev/well-known/astrocal-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/astrocal-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/astrocal-dev/hosts/astrocal-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/astrocal-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/astrocal-dev/vendors/astrocal-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/astrocal-dev-vendors.yml
- group: build
  href: https://artifacts.apis.io/astrocal-dev/packages/astrocal-dev-packages.yml
  title: ''
  type: SDKs
  url: packages/astrocal-dev-packages.yml
- group: build
  href: https://artifacts.apis.io/astrocal-dev/packages/astrocal-dev-packages.yml
  title: ''
  type: Packages
  url: packages/astrocal-dev-packages.yml
- group: operate
  title: ''
  type: Support
  url: https://www.astrocal.dev/support
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.astrocal.dev/changelog
- group: docs
  title: ''
  type: APIReference
  url: https://www.astrocal.dev/docs/api-reference
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.astrocal.dev\
- group: auth
  href: https://artifacts.apis.io/astrocal-dev/security/astrocal-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/astrocal-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://astrocal.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://www.astrocal.dev/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://www.astrocal.dev/docs
- group: company
  title: ''
  type: Blog
  url: https://www.astrocal.dev/articles
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/astrocal-dev
- group: commercial
  title: ''
  type: Pricing
  url: https://www.astrocal.dev/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.astrocal.dev/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.astrocal.dev/privacy
- group: start
  title: ''
  type: SignUp
  url: https://www.astrocal.dev/signup
- group: start
  title: ''
  type: Login
  url: https://www.astrocal.dev/login
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://api.astrocal.dev/v1/openapi.json
  - status: 401
    url: https://api.astrocal.dev/mcp
  - status: 200
    url: https://astrocal.dev/
  reason: partner-login
  state: gated
created: '2026-11-01'
description: Astrocal provides a booking page and scheduling platform for small businesses, offering live booking in minutes, calendar sync, confirmations, reminders, Stripe payments, and a full developer API for integration.
image: https://www.astrocal.dev/opengraph-image?ccd96e5c8f398fae
layout: provider
modified: '2026-11-01'
name: Astrocal
nav: Providers
network: true
overview: 'Astrocal publishes 20 API contracts indexed on the [APIs.io](https://apis.io/) network, including Activity API, API Keys API, Availability API, and 17 more. Tagged areas include Scheduling, Booking, Small Business, and Payments.


  The Astrocal catalog on APIs.io includes 1 Spectral governance ruleset.


  Astrocal''s developer surface includes changelog, sandbox, authentication, support, API reference, documentation, getting-started guide, and 25 more developer resources.'
plans:
- name: Astrocal Dev Plans Pricing
  plan_count: 4
  slug: astrocal-dev-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 8
  name: Astrocal Dev Rate Limits
  slug: astrocal-dev-rate-limits
rules:
- authorship: generated
  effective_rule_count: 84
  extends:
  - spectral:oas
  name: Astrocal API Rules
  rule_count: 43
  severity_counts:
    error: 36
    hint: 0
    info: 2
    warn: 5
  slug: astrocal-dev-rules
scopes:
- name: Astrocal Dev Scopes
  scope_count: 0
  slug: astrocal-dev-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 47.7
  coverage:
    artifact_dirs: 26
    catalog_earned: 61.8
    catalog_earned_first_party: 24.0
    catalog_gap: 53.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -11.8
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 48.5
    developer_ergonomics: 48.8
    discoverability: 57.1
    operational_transparency: 42.1
  previous_composite: 59.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 20
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 27.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Astrocal Dev Authentication
  slug: astrocal-dev-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Astrocal Dev Domain Security
  slug: astrocal-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: astrocal-dev
tags:
- Scheduling
- Booking
- Small Business
- Payments
website: https://astrocal.dev/
---
