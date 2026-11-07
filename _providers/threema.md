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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Threema provides secure messaging APIs for integration, described on their website.
  name: Threema API
  slug: threema-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/threema/plans/threema-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/threema-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/threema/conformance/threema-conformance.yml
  title: ''
  type: Conformance
  url: conformance/threema-conformance.yml
- group: agent
  href: https://artifacts.apis.io/threema/llms/threema-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/threema-llms.txt
- group: auth
  href: https://artifacts.apis.io/threema/well-known/threema-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/threema-security.txt
- group: agent
  href: https://artifacts.apis.io/threema/well-known/threema-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/threema-well-known.yml
- group: other
  href: https://artifacts.apis.io/threema/hosts/threema-hosts.yml
  title: ''
  type: Hosts
  url: hosts/threema-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://threema.com/en/tos
- group: operate
  title: ''
  type: Support
  url: https://threema.com/en/support/work
- group: start
  title: ''
  type: SignUp
  url: https://threema.com/en/signup
- group: auth
  title: ''
  type: Security
  url: https://threema.com/en/why-threema/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://threema.com/en/privacy-note
- group: commercial
  title: ''
  type: Pricing
  url: https://threema.com/en/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://threema.com/en/press
- group: operate
  title: ''
  type: ChangeLog
  url: https://threema.com/en/changelog
- group: company
  title: ''
  type: Blog
  url: https://threema.com/en/blog
- group: auth
  href: https://artifacts.apis.io/threema/security/threema-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/threema-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/threema/security/threema-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/threema-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://threema.com/
coverage:
  checked: '2026-10-27'
  detail: Threema website provides only HTML documentation without a machine‑readable OpenAPI spec.
  evidence:
  - status: 404
    url: https://threema.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-27'
description: Threema is a secure messaging platform based in Switzerland that provides end‑to‑end encrypted communication for individuals and businesses. It offers products such as Threema Work, Threema OnPrem, and Threema Private, all GDPR‑compliant and designed for high‑security environments like public authorities, healthcare, and finance. The service emphasizes data sovereignty, zero‑knowledge security, and compliance with regulations such as NIS2 and DORA, making it a trusted alternative to mainstream messengers.
layout: provider
modified: '2026-10-27'
name: Threema
nav: Providers
network: true
overview: 'Threema is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Messaging, Security, Privacy, and GDPR.


  Threema''s developer surface includes support, signup flow, pricing, changelog, engineering blog, and 13 more developer resources.'
plans:
- name: Threema Plans Pricing
  plan_count: 3
  slug: threema-plans-pricing
random_paper: 22
score:
  band: emerging
  composite: 22.4
  coverage:
    artifact_dirs: 12
    catalog_earned: 42.0
    catalog_earned_first_party: 12.0
    catalog_gap: 73.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.5
  facets:
    access_clarity: 53.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 3.6
    discoverability: 61.6
    operational_transparency: 13.2
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - switzerland
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 29.9
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/threema/threema-2026-11-03T144712.png
security:
- kind: domain-security
  name: Threema Domain Security
  slug: threema-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Threema Vulnerability Disclosure
  slug: threema-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: threema
tags:
- Company
- Messaging
- Security
- Privacy
- GDPR
website: https://threema.com/
---
