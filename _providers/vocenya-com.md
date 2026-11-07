---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 39.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Vocenya API for managing calls, leads, bookings, chats, and webhooks.
  name: Vocenya API
  slug: vocenya-api
artifact_total: 7
common:
- group: operate
  href: https://artifacts.apis.io/vocenya-com/rate-limits/vocenya-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/vocenya-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/vocenya-com/plans/vocenya-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/vocenya-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/vocenya-com/conventions/vocenya-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/vocenya-com-conventions.yml
- group: start
  href: https://artifacts.apis.io/vocenya-com/sandbox/vocenya-com-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/vocenya-com-sandbox.yml
- group: auth
  href: https://artifacts.apis.io/vocenya-com/authentication/vocenya-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/vocenya-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/vocenya-com/scopes/vocenya-com-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/vocenya-com-scopes.yml
- group: design
  href: https://artifacts.apis.io/vocenya-com/errors/vocenya-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/vocenya-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/vocenya-com/conformance/vocenya-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/vocenya-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/vocenya-com/llms/vocenya-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/vocenya-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/vocenya-com/well-known/vocenya-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/vocenya-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/vocenya-com/hosts/vocenya-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/vocenya-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/vocenya-com/vendors/vocenya-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/vocenya-com-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.vocenya.com
- group: auth
  title: ''
  type: Security
  url: https://vocenya.com/security
- group: operate
  title: ''
  type: ChangeLog
  url: https://vocenya.com/changelog
- group: start
  title: ''
  type: SignUp
  url: https://vocenya.com/register
- group: auth
  href: https://artifacts.apis.io/vocenya-com/security/vocenya-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/vocenya-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/vocenya-com/security/vocenya-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/vocenya-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://vocenya.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://vocenya.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://vocenya.com/developers
- group: docs
  title: ''
  type: APIReference
  url: https://vocenya.com/docs/api.json
- group: start
  title: ''
  type: GettingStarted
  url: https://vocenya.com/developers
- group: operate
  title: ''
  type: Support
  url: https://vocenya.com/contact
- group: company
  title: ''
  type: Blog
  url: https://vocenya.com/blog
- group: operate
  title: ''
  type: Roadmap
  url: https://vocenya.com/roadmap
- group: commercial
  title: ''
  type: Pricing
  url: https://vocenya.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://vocenya.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://vocenya.com/privacy
created: '2026-10-29'
description: Vocenya provides AI-powered receptionist and AI agents that answer calls, chats, and follow‑up interactions 24/7 for small businesses, with the option to involve skilled human agents when needed. Features include AI‑driven call handling, website chat, WhatsApp, outbound AI calling, appointment booking, and a talent marketplace for human support. Backed by GH Business Solutions, Vocenya offers HIPAA‑mode compliance and integrates with existing phone numbers.
image: https://vocenya.com/images/og-default.png
layout: provider
modified: '2026-10-29'
name: vocenya-com
nav: Providers
network: true
overview: 'vocenya-com is listed with 1 API on the [APIs.io](https://apis.io/) network: Vocenya API. Tagged areas include Artificial Intelligence, Communications, Customer Service, Automation, and Voice.


  vocenya-com''s developer surface includes sandbox, authentication, changelog, signup flow, documentation, API reference, getting-started guide, and 22 more developer resources.'
plans:
- name: Vocenya Com Plans Pricing
  plan_count: 4
  slug: vocenya-com-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 4
  name: Vocenya Com Rate Limits
  slug: vocenya-com-rate-limits
scopes:
- name: Vocenya Com Scopes
  scope_count: 11
  slug: vocenya-com-scopes
  summary_line: 11 scopes
score:
  band: developing
  composite: 44.6
  coverage:
    artifact_dirs: 25
    catalog_earned: 61.0
    catalog_earned_first_party: 24.0
    catalog_gap: 54.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -12.6
  facets:
    access_clarity: 53.9
    contract_governance: 18.2
    contract_quality: 24.0
    developer_ergonomics: 41.7
    discoverability: 73.2
    operational_transparency: 55.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 57.2
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 33.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/vocenya-com/vocenya-com-2026-11-03T145908.png
security:
- kind: authentication
  name: Vocenya Com Authentication
  slug: vocenya-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Vocenya Com Domain Security
  slug: vocenya-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Vocenya Com Vulnerability Disclosure
  slug: vocenya-com-vulnerability-disclosure
  summary_line: no policy recorded
slug: vocenya-com
tags:
- Artificial Intelligence
- Communications
- Customer Service
- Automation
- Voice
website: https://vocenya.com/
---
