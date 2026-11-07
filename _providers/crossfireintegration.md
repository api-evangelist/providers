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
  score: 10.8
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/crossfireintegration/plans/crossfireintegration-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/crossfireintegration-plans-pricing.yml
- group: auth
  title: ''
  type: Compliance
  url: https://crossfireintegration.com/security
- group: agent
  href: https://artifacts.apis.io/crossfireintegration/well-known/crossfireintegration-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/crossfireintegration-well-known.yml
- group: other
  href: https://artifacts.apis.io/crossfireintegration/hosts/crossfireintegration-hosts.yml
  title: ''
  type: Hosts
  url: hosts/crossfireintegration-hosts.yml
- group: other
  href: https://artifacts.apis.io/crossfireintegration/vendors/crossfireintegration-vendors.yml
  title: ''
  type: Vendors
  url: vendors/crossfireintegration-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://crossfireintegration.com/terms-of-use/
- group: auth
  title: ''
  type: Security
  url: https://crossfireintegration.com/security/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://crossfireintegration.com/privacy-policy/
- group: auth
  href: https://artifacts.apis.io/crossfireintegration/security/crossfireintegration-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/crossfireintegration-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/crossfireintegration/security/crossfireintegration-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/crossfireintegration-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://crossfireintegration.com/
- group: docs
  title: ''
  type: Documentation
  url: https://crossfireintegration.com/resources/insights/
- group: start
  title: ''
  type: GettingStarted
  url: https://crossfireintegration.com/about-us/
- group: operate
  title: ''
  type: Support
  url: https://crossfireintegration.com/contact-us/
- group: company
  title: ''
  type: Blog
  url: https://crossfireintegration.com/resources/insights/
- group: commercial
  title: ''
  type: Pricing
  url: https://crossfireintegration.com/plans/
coverage:
  checked: '2026-10-20'
  detail: The developer pages are rendered via JavaScript and no machine‑readable spec was discovered.
  evidence:
  - status: 200
    url: https://crossfireintegration.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-20'
description: Sandfield provides EDI and API integration solutions as a managed iPaaS platform. It offers services including managed EDI, custom API development, Peppol eInvoicing, enterprise service bus, and a customer portal. Targeting suppliers, manufacturers, retailers, and logistics providers, Sandfield enables end‑to‑end supply‑chain automation and integration visibility across trading partners and systems.
layout: provider
modified: '2026-10-20'
name: Sandfield
nav: Providers
network: true
overview: 'Sandfield is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Integration, EDI, and Supply Chain.


  Sandfield''s developer surface includes documentation, getting-started guide, support, engineering blog, pricing, and 11 more developer resources.'
plans:
- name: Crossfireintegration Plans Pricing
  plan_count: 3
  slug: crossfireintegration-plans-pricing
random_paper: 4
score:
  band: emerging
  composite: 19.4
  coverage:
    artifact_dirs: 10
    catalog_earned: 32.0
    catalog_earned_first_party: 12.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.3
  facets:
    access_clarity: 59.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 35.7
    operational_transparency: 5.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 28.7
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/crossfireintegration/crossfireintegration-2026-11-03T125643.png
security:
- kind: domain-security
  name: Crossfireintegration Domain Security
  slug: crossfireintegration-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: trust-center
  name: Crossfireintegration Trust Center
  slug: crossfireintegration-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: crossfireintegration
tags:
- Company
- Integration
- EDI
- Supply Chain
website: https://crossfireintegration.com/
---
