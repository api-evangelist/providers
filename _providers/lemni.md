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
- description: API documented at Lemni Docs, but no machine‑readable contract found.
  name: Lemni API
  slug: lemni-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/lemni/plans/lemni-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/lemni-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/lemni/changelog/lemni-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/lemni-changelog.yml
- group: design
  href: https://artifacts.apis.io/lemni/conformance/lemni-conformance.yml
  title: ''
  type: Conformance
  url: conformance/lemni-conformance.yml
- group: other
  href: https://artifacts.apis.io/lemni/hosts/lemni-hosts.yml
  title: ''
  type: Hosts
  url: hosts/lemni-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.lemni.com/terms
- group: operate
  title: ''
  type: Support
  url: https://www.lemni.com/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.lemni.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.lemni.com/pricing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/lemni
- group: docs
  title: ''
  type: Documentation
  url: https://www.lemni.com/docs
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.lemni.com/changelog
- group: company
  title: ''
  type: Blog
  url: https://www.lemni.com/blog
- group: auth
  href: https://artifacts.apis.io/lemni/security/lemni-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/lemni-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.lemni.com/
coverage:
  checked: '2026-10-29'
  detail: Docs are rendered via JavaScript, preventing machine‑readable spec extraction.
  evidence:
  - status: 200
    url: https://www.lemni.com/docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-29'
description: Lemni provides a platform to set up custom AI agents quickly, enabling businesses to personalize customer interactions across channels such as phone, email, and proactive outreach. The service promises to scale interactions without increasing headcount, offering a free trial and emphasizing ease of deployment for enterprises seeking to enhance support and engagement.
image: https://framerusercontent.com/images/IW4lA3BsX0eWCvbLZ7DqGIcvrvk.png
layout: provider
modified: '2026-10-29'
name: Lemni
nav: Providers
network: true
overview: 'Lemni is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Customer Engagement, Software-as-a-Service, Automation, and Platform.


  Lemni''s developer surface includes changelog, support, pricing, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Lemni Plans Pricing
  plan_count: 1
  slug: lemni-plans-pricing
random_paper: 5
score:
  band: emerging
  composite: 18.1
  coverage:
    artifact_dirs: 12
    catalog_earned: 40.0
    catalog_earned_first_party: 8.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.7
  facets:
    access_clarity: 36.8
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 8.3
    discoverability: 57.1
    operational_transparency: 10.5
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 24.8
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
    score: 13.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/lemni/lemni-2026-11-03T134808.png
security:
- kind: domain-security
  name: Lemni Domain Security
  slug: lemni-domain-security
  summary_line: TLSv1.3 · HSTS
slug: lemni
tags:
- Artificial Intelligence
- Customer Engagement
- Software-as-a-Service
- Automation
- Platform
website: https://www.lemni.com/
---
