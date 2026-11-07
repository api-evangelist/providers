---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 24.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Digital Product Passport REST API for the TracePass platform.
  name: TracePass API
  slug: tracepass-api
artifact_total: 6
common:
- group: start
  title: ''
  type: GettingStarted
  url: https://www.tracepass.eu/docs/quickstart
- group: commercial
  href: https://artifacts.apis.io/tracepass-eu/plans/tracepass-eu-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/tracepass-eu-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/tracepass-eu/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.tracepass.eu/trust
- group: auth
  href: https://artifacts.apis.io/tracepass-eu/security/tracepass-eu-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/tracepass-eu-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/tracepass-eu/conformance/tracepass-eu-conformance.yml
  title: ''
  type: Conformance
  url: conformance/tracepass-eu-conformance.yml
- group: agent
  href: https://artifacts.apis.io/tracepass-eu/llms/tracepass-eu-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/tracepass-eu-llms.txt
- group: auth
  href: https://artifacts.apis.io/tracepass-eu/well-known/tracepass-eu-tracepass-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/tracepass-eu-tracepass-security.txt
- group: auth
  href: https://artifacts.apis.io/tracepass-eu/well-known/tracepass-eu-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/tracepass-eu-security.txt
- group: agent
  href: https://artifacts.apis.io/tracepass-eu/well-known/tracepass-eu-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/tracepass-eu-well-known.yml
- group: other
  href: https://artifacts.apis.io/tracepass-eu/hosts/tracepass-eu-hosts.yml
  title: ''
  type: Hosts
  url: hosts/tracepass-eu-hosts.yml
- group: other
  href: https://artifacts.apis.io/tracepass-eu/vendors/tracepass-eu-vendors.yml
  title: ''
  type: Vendors
  url: vendors/tracepass-eu-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://app.tracepass.eu/login
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.tracepass.eu/regulatory/changelog
- group: auth
  href: https://artifacts.apis.io/tracepass-eu/security/tracepass-eu-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/tracepass-eu-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/tracepass-eu/security/tracepass-eu-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/tracepass-eu-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/tracepass-eu/security/tracepass-eu-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tracepass-eu-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tracepass.eu/
- group: docs
  title: ''
  type: Documentation
  url: https://www.tracepass.eu/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://www.tracepass.eu/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tracepass.eu/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tracepass.eu/privacy
created: '2026-10-30'
description: TracePass provides an AI‑powered Digital Product Passport (DPP) platform for EU manufacturers. It enables uploading product data to generate GS1 Digital Link passports for batteries, textiles, electronics and other categories, complying with upcoming EU regulations such as Regulation (EU) 2023/1542. The service offers AI‑driven data extraction, compliance guidance, and a user‑friendly portal for managing product passports across lifecycles.
image: https://www.tracepass.eu/opengraph-image
layout: provider
modified: '2026-10-30'
name: tracepass-eu
nav: Providers
network: true
overview: 'tracepass-eu is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Digital Product Passport, EU-Regulation, and Sustainability.


  tracepass-eu''s developer surface includes getting-started guide, changelog, documentation, pricing, and 18 more developer resources.'
plans:
- name: Tracepass Eu Plans Pricing
  plan_count: 7
  slug: tracepass-eu-plans-pricing
random_paper: 5
score:
  band: thin
  composite: 28.6
  coverage:
    artifact_dirs: 14
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.3
  facets:
    access_clarity: 65.8
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 17.1
    discoverability: 73.2
    operational_transparency: 18.4
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 37.9
  provenance:
    conformance: derived
    mcp: unknown
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/tracepass-eu/tracepass-eu-2026-11-03T144941.png
security:
- kind: domain-security
  name: Tracepass Eu Domain Security
  slug: tracepass-eu-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Tracepass Eu Vulnerability Disclosure
  slug: tracepass-eu-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Tracepass Eu Trust Center
  slug: tracepass-eu-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
skill_count: 1
skills:
- name: passport-management
  slug: tracepass-eu-passport-management
slug: tracepass-eu
tags:
- Company
- Artificial Intelligence
- Digital Product Passport
- EU-Regulation
- Sustainability
website: https://tracepass.eu/
---
