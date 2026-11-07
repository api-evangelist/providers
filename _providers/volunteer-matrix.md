---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Volunteer Matrix native API provides programmatic access to volunteer scheduling and management features.
  name: Native API
  slug: native-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/volunteer-matrix/plans/volunteer-matrix-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/volunteer-matrix-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/volunteer-matrix/conformance/volunteer-matrix-conformance.yml
  title: ''
  type: Conformance
  url: conformance/volunteer-matrix-conformance.yml
- group: auth
  href: https://artifacts.apis.io/volunteer-matrix/well-known/volunteer-matrix-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/volunteer-matrix-security.txt
- group: agent
  href: https://artifacts.apis.io/volunteer-matrix/well-known/volunteer-matrix-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/volunteer-matrix-well-known.yml
- group: other
  href: https://artifacts.apis.io/volunteer-matrix/hosts/volunteer-matrix-hosts.yml
  title: ''
  type: Hosts
  url: hosts/volunteer-matrix-hosts.yml
- group: auth
  title: ''
  type: Security
  url: https://volunteermatrix.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://volunteermatrix.com/privacy
- group: start
  title: ''
  type: Login
  url: https://volunteermatrix.com/login
- group: auth
  href: https://artifacts.apis.io/volunteer-matrix/security/volunteer-matrix-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/volunteer-matrix-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/volunteer-matrix/security/volunteer-matrix-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/volunteer-matrix-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://volunteermatrix.com/
- group: docs
  title: ''
  type: Documentation
  url: https://volunteermatrix.com/api
- group: commercial
  title: ''
  type: Pricing
  url: https://volunteermatrix.com/pricing
- group: start
  title: ''
  type: GettingStarted
  url: https://volunteermatrix.com/about
- group: operate
  title: ''
  type: Support
  url: https://volunteermatrix.com/support
coverage:
  checked: '2026-10-27'
  detail: The API documentation page is a JavaScript‑rendered HTML site with no machine‑readable OpenAPI or other contract.
  evidence:
  - status: 200
    url: https://volunteermatrix.com/api
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-27'
description: Volunteer Matrix is a volunteer management platform built from over 20 years of experience helping nonprofits run reliable, repeatable volunteer programs. The SaaS solution streamlines volunteer recruitment, scheduling, communication, and reporting, enabling organizations to efficiently coordinate community involvement and maximize impact.
layout: provider
modified: '2026-10-27'
name: Volunteer Matrix
nav: Providers
network: true
overview: 'Volunteer Matrix is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Volunteer Management, Software-as-a-Service, Non-Profit, Community, and Platform.


  Volunteer Matrix''s developer surface includes documentation, pricing, getting-started guide, support, and 11 more developer resources.'
plans:
- name: Volunteer Matrix Plans Pricing
  plan_count: 1
  slug: volunteer-matrix-plans-pricing
random_paper: 22
score:
  band: emerging
  composite: 19.0
  coverage:
    artifact_dirs: 10
    catalog_earned: 38.0
    catalog_earned_first_party: 8.0
    catalog_gap: 77.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.0
  facets:
    access_clarity: 38.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 13.1
    discoverability: 53.6
    operational_transparency: 5.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 26.0
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/volunteer-matrix/volunteer-matrix-2026-11-03T145921.png
security:
- kind: domain-security
  name: Volunteer Matrix Domain Security
  slug: volunteer-matrix-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Volunteer Matrix Vulnerability Disclosure
  slug: volunteer-matrix-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: volunteer-matrix
tags:
- Volunteer Management
- Software-as-a-Service
- Non-Profit
- Community
- Platform
website: https://volunteermatrix.com/
---
