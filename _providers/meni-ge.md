---
access_model:
  confidence: medium
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
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.2
  scored_at: '2026-11-06'
api_count: 3
apis:
- description: Public API documented at the Meni.ge developer portal. Provides endpoints for POS, inventory, CRM, hospitality, e‑commerce and AI‑enhanced operations.
  name: Meni.ge API
  slug: meni-ge-api
artifact_total: 6
common:
- group: commercial
  href: https://artifacts.apis.io/meni-ge/plans/meni-ge-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/meni-ge-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/meni-ge/rules/meni-ge-rules.yml
  title: ''
  type: Spectral
  url: rules/meni-ge-rules.yml
- group: design
  href: https://artifacts.apis.io/meni-ge/json-ld/meni-ge-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/meni-ge-context.jsonld
- group: design
  href: https://artifacts.apis.io/meni-ge/vocabulary/meni-ge-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/meni-ge-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/meni-ge/data-model/meni-ge-data-model.yml
  title: ''
  type: DataModel
  url: data-model/meni-ge-data-model.yml
- group: auth
  href: https://artifacts.apis.io/meni-ge/authentication/meni-ge-authentication.yml
  title: ''
  type: Authentication
  url: authentication/meni-ge-authentication.yml
- group: design
  href: https://artifacts.apis.io/meni-ge/errors/meni-ge-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/meni-ge-problem-types.yml
- group: design
  href: https://artifacts.apis.io/meni-ge/conformance/meni-ge-conformance.yml
  title: ''
  type: Conformance
  url: conformance/meni-ge-conformance.yml
- group: agent
  href: https://artifacts.apis.io/meni-ge/llms/meni-ge-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/meni-ge-llms.txt
- group: agent
  href: https://artifacts.apis.io/meni-ge/well-known/meni-ge-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/meni-ge-well-known.yml
- group: other
  href: https://artifacts.apis.io/meni-ge/hosts/meni-ge-hosts.yml
  title: ''
  type: Hosts
  url: hosts/meni-ge-hosts.yml
- group: other
  href: https://artifacts.apis.io/meni-ge/vendors/meni-ge-vendors.yml
  title: ''
  type: Vendors
  url: vendors/meni-ge-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://meni.ge/apps/support
- group: auth
  title: ''
  type: Security
  url: https://meni.ge/en/security
- group: start
  title: ''
  type: Login
  url: https://admin.meni.ge/ka/login
- group: operate
  title: ''
  type: ChangeLog
  url: https://meni.ge/docs/whats-new
- group: auth
  href: https://artifacts.apis.io/meni-ge/security/meni-ge-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/meni-ge-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://meni.ge/
- group: docs
  title: ''
  type: Documentation
  url: https://meni.ge/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://meni.ge/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://meni.ge/docs/getting-started
- group: company
  title: ''
  type: Blog
  url: https://meni.ge/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://meni.ge/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://meni.ge/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://meni.ge/privacy
coverage:
  detail: Documentation pages are rendered via JavaScript, preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://meni.ge/docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-30'
description: Meni.ge provides an all‑in‑one business workspace covering POS, inventory, CRM, hospitality, e‑commerce and AI‑enhanced operations. It unifies ordering, payments, staff management, bookings, delivery and analytics in a single cloud platform, offering free starter plans and paid tiers for multi‑location enterprises.
image: https://meni.ge/images/redesign/dashboard-tablet-scene.jpg
jsonld:
- class_count: 9
  name: Meni Ge Context
  property_count: 63
  slug: meni-ge-context
layout: provider
modified: '2026-10-30'
name: meni-ge
nav: Providers
network: true
overview: 'meni-ge publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Point-of-Sale, Inventory, CRM, and Hospitality.


  The meni-ge catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  meni-ge''s developer surface includes authentication, support, changelog, documentation, API reference, getting-started guide, engineering blog, and 18 more developer resources.'
plans:
- name: Meni Ge Plans Pricing
  plan_count: 4
  slug: meni-ge-plans-pricing
random_paper: 2
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: meni-ge API Rules
  rule_count: 14
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 1
  slug: meni-ge-rules
score:
  band: thin
  composite: 32.4
  coverage:
    artifact_dirs: 20
    catalog_earned: 63.8
    catalog_earned_first_party: 12.0
    catalog_gap: 51.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.3
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 16.9
    developer_ergonomics: 29.8
    discoverability: 69.6
    operational_transparency: 13.2
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 42.7
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/meni-ge/meni-ge-2026-11-03T135452.png
security:
- kind: authentication
  name: Meni Ge Authentication
  slug: meni-ge-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Meni Ge Domain Security
  slug: meni-ge-domain-security
  summary_line: TLSv1.3 · DMARC
slug: meni-ge
tags:
- Company
- Point-of-Sale
- Inventory
- CRM
- Hospitality
- E-Commerce
website: https://meni.ge/
---
