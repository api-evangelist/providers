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
    protected_resource_metadata: documented
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 4.7
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/unremind-me/plans/unremind-me-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/unremind-me-plans-pricing.yml
- group: auth
  title: ''
  type: Security
  url: https://unremind.me/terms
- group: agent
  href: https://artifacts.apis.io/unremind-me/llms/unremind-me-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/unremind-me-llms.txt
- group: auth
  href: https://artifacts.apis.io/unremind-me/well-known/unremind-me-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/unremind-me-security.txt
- group: agent
  href: https://artifacts.apis.io/unremind-me/well-known/unremind-me-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/unremind-me-well-known.yml
- group: other
  href: https://artifacts.apis.io/unremind-me/hosts/unremind-me-hosts.yml
  title: ''
  type: Hosts
  url: hosts/unremind-me-hosts.yml
- group: other
  href: https://artifacts.apis.io/unremind-me/vendors/unremind-me-vendors.yml
  title: ''
  type: Vendors
  url: vendors/unremind-me-vendors.yml
- group: auth
  href: https://artifacts.apis.io/unremind-me/security/unremind-me-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/unremind-me-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/unremind-me/security/unremind-me-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/unremind-me-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://unremind.me/
- group: commercial
  title: ''
  type: Pricing
  url: https://unremind.me/pricing/
- group: operate
  title: ''
  type: Support
  url: https://unremind.me/support/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://unremind.me/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://unremind.me/privacy/
- group: start
  title: ''
  type: SignUp
  url: https://unremind.me/register/
coverage:
  checked: '2026-10-30'
  detail: Provider's website returns HTML pages without machine‑readable OpenAPI or other specs.
  evidence:
  - status: 200
    url: https://unremind.me/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-30'
description: UnRemind is a context‑aware reminder and task engine that delivers notifications only when they make sense for the user. By leveraging location, device, and calendar data, UnRemind waits for the right moment—such as being near a specific place or having free time—before firing a reminder. The platform offers geofenced triggers, AI‑powered assistance, and integrates with existing calendars and task managers, all while remaining ad‑free and privacy‑focused. Currently in private beta, UnRemind aims to enhance productivity without requiring users to abandon their preferred tools.
layout: provider
modified: '2026-10-30'
name: unremind-me
nav: Providers
network: true
overview: 'unremind-me is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Productivity, Reminders, Context-Aware, and Artificial Intelligence.


  unremind-me''s developer surface includes pricing, support, signup flow, and 12 more developer resources.'
plans:
- name: Unremind Me Plans Pricing
  plan_count: 6
  slug: unremind-me-plans-pricing
random_paper: 17
score:
  band: emerging
  composite: 17.0
  coverage:
    artifact_dirs: 11
    catalog_earned: 37.0
    catalog_earned_first_party: 12.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.2
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 51.8
    operational_transparency: 5.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 23.2
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/unremind-me/unremind-me-2026-11-03T145454.png
security:
- kind: domain-security
  name: Unremind Me Domain Security
  slug: unremind-me-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Unremind Me Vulnerability Disclosure
  slug: unremind-me-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: unremind-me
tags:
- Company
- Productivity
- Reminders
- Context-Aware
- Artificial Intelligence
website: https://unremind.me/
---
