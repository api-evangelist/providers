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
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
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
  score: 2.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Can Tap Verified Com Agentic Access
  operation_count: 10
  slug: can-tap-verified-com-agentic-access
  summary_line: 10 operations · 3 acting
api_count: 1
apis:
- description: Canadian business directory, NFC tap analytics, and free dofollow backlink platform.
  name: CAN-TAP Verified API
  slug: can-tap-verified-api
artifact_total: 5
common:
- group: agent
  href: https://artifacts.apis.io/can-tap-verified-com/agentic-access/can-tap-verified-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/can-tap-verified-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/can-tap-verified-com/plans/can-tap-verified-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/can-tap-verified-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/can-tap-verified-com/rules/can-tap-verified-com-rules.yml
  title: ''
  type: Spectral
  url: rules/can-tap-verified-com-rules.yml
- group: design
  href: https://artifacts.apis.io/can-tap-verified-com/errors/can-tap-verified-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/can-tap-verified-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/can-tap-verified-com/conformance/can-tap-verified-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/can-tap-verified-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/can-tap-verified-com/llms/can-tap-verified-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/can-tap-verified-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/can-tap-verified-com/well-known/can-tap-verified-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/can-tap-verified-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/can-tap-verified-com/hosts/can-tap-verified-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/can-tap-verified-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/can-tap-verified-com/vendors/can-tap-verified-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/can-tap-verified-com-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://can-tap-verified.com/privacy
- group: auth
  href: https://artifacts.apis.io/can-tap-verified-com/security/can-tap-verified-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/can-tap-verified-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://can-tap-verified.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://can-tap-verified.com/how-it-works
- group: operate
  title: ''
  type: Support
  url: https://can-tap-verified.com/contact
- group: commercial
  title: ''
  type: Pricing
  url: https://can-tap-verified.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://can-tap-verified.com/terms
created: '2026-11-04'
description: CAN-TAP Verified provides Canadian businesses with a verified door badge, a counter tap stand, and an online business record that customers can check. The service offers NFC tap‑to‑review hardware and a searchable evidence profile, enabling easy verification and reputation management across Google Business and other platforms.
image: https://can-tap-verified.com/og/home.png
layout: provider
modified: '2026-11-04'
name: CAN-TAP Verified
nav: Providers
network: true
overview: 'CAN-TAP Verified is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Canadian, Business, Verification, NFC, and Reputation.


  The CAN-TAP Verified catalog on APIs.io includes 1 Spectral governance ruleset.


  CAN-TAP Verified''s developer surface includes getting-started guide, support, pricing, and 13 more developer resources.'
plans:
- name: Can Tap Verified Com Plans Pricing
  plan_count: 3
  slug: can-tap-verified-com-plans-pricing
random_paper: 11
rules:
- authorship: generated
  effective_rule_count: 71
  extends:
  - spectral:oas
  name: CAN-TAP Verified API Rules
  rule_count: 30
  severity_counts:
    error: 28
    hint: 0
    info: 1
    warn: 1
  slug: can-tap-verified-com-rules
score:
  band: emerging
  composite: 19.9
  coverage:
    artifact_dirs: 13
    catalog_earned: 53.5
    catalog_earned_first_party: 12.0
    catalog_gap: 61.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 47.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 8.3
    discoverability: 66.1
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Can Tap Verified Com Domain Security
  slug: can-tap-verified-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: can-tap-verified-com
tags:
- Canadian
- Business
- Verification
- NFC
- Reputation
website: https://can-tap-verified.com/
---
