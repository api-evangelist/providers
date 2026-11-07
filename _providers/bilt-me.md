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
- description: Bilt provides a mobile app builder platform; API details are described in their documentation pages.
  name: Bilt API
  slug: bilt-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/bilt-me/plans/bilt-me-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bilt-me-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/bilt-me/changelog/bilt-me-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/bilt-me-changelog.yml
- group: auth
  title: ''
  type: Security
  url: https://bilt.me/aup
- group: design
  href: https://artifacts.apis.io/bilt-me/conformance/bilt-me-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bilt-me-conformance.yml
- group: agent
  href: https://artifacts.apis.io/bilt-me/llms/bilt-me-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bilt-me-llms.txt
- group: auth
  href: https://artifacts.apis.io/bilt-me/well-known/bilt-me-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bilt-me-security.txt
- group: agent
  href: https://artifacts.apis.io/bilt-me/well-known/bilt-me-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bilt-me-well-known.yml
- group: other
  href: https://artifacts.apis.io/bilt-me/hosts/bilt-me-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bilt-me-hosts.yml
- group: other
  href: https://artifacts.apis.io/bilt-me/vendors/bilt-me-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bilt-me-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bilt.me/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bilt.me/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://bilt.me/pricing
- group: start
  title: ''
  type: Login
  url: https://app.bilt.me/login
- group: operate
  title: ''
  type: ChangeLog
  url: https://bilt.me/changelog
- group: company
  title: ''
  type: Blog
  url: https://bilt.me/blog
- group: docs
  title: ''
  type: Documentation
  url: https://help.bilt.me/
- group: auth
  href: https://artifacts.apis.io/bilt-me/security/bilt-me-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/bilt-me-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/bilt-me/security/bilt-me-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bilt-me-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bilt.me/
coverage:
  checked: '2026-11-02'
  detail: Provider's documentation pages are rendered via JavaScript, preventing machine‑readable contract discovery.
  evidence:
  - status: 200
    url: https://help.bilt.me/
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-02'
description: Bilt is a small Estonian company building an AI‑powered mobile app builder. Their platform lets anyone describe an app idea and receive a production‑ready native iOS and Android app, eliminating the need for traditional development. The service targets startups and businesses seeking rapid, cost‑effective mobile presence without coding.
image: https://bilt.me/og-image.png
layout: provider
modified: '2026-11-02'
name: Bilt
nav: Providers
network: true
overview: 'Bilt is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Mobile, Artificial Intelligence, No-Code, App Builder, and Estonia.


  Bilt''s developer surface includes changelog, pricing, engineering blog, documentation, and 15 more developer resources.'
plans:
- name: Bilt Me Plans Pricing
  plan_count: 5
  slug: bilt-me-plans-pricing
random_paper: 10
score:
  band: emerging
  composite: 22.2
  coverage:
    artifact_dirs: 11
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 53.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 6.0
    discoverability: 57.1
    operational_transparency: 13.2
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
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bilt Me Domain Security
  slug: bilt-me-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Bilt Me Vulnerability Disclosure
  slug: bilt-me-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: bilt-me
tags:
- Mobile
- Artificial Intelligence
- No-Code
- App Builder
- Estonia
website: https://bilt.me/
---
