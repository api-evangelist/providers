---
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/bsportsolution/refs/heads/main/plans/bsportsolution-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bsportsolution-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bsportsolution/refs/heads/main/conformance/bsportsolution-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bsportsolution-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bsportsolution/refs/heads/main/llms/bsportsolution-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bsportsolution-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bsportsolution/refs/heads/main/well-known/bsportsolution-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bsportsolution-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bsportsolution/refs/heads/main/hosts/bsportsolution-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bsportsolution-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bsportsolution/refs/heads/main/vendors/bsportsolution-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bsportsolution-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://pro.bsport.io/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://pro.bsport.io/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://pro.bsport.io/pricing
- group: company
  title: ''
  type: Blog
  url: https://pro.bsport.io/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://pro.bsport.io/blog/the-complete-guide-to-onboarding-new-studio-members
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bsportsolution/refs/heads/main/security/bsportsolution-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bsportsolution-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://pro.bsport.io
- group: docs
  title: ''
  type: Documentation
  url: https://pro.bsport.io/features/public-api
coverage:
  checked: 2026-10-06 'Bsportsolution provides a cloud‑based platform for boutique fitness studios, offering class scheduling, booking, payments, membership management, marketing tools, and performance dashboards. The solution supports multi‑location franchises, integrates with popular payment gateways, and includes a public API for developers to build custom integrations and extensions.'
  detail: Public API page renders via JavaScript and provides no machine‑readable spec.
  evidence:
  - status: 200
    url: https://pro.bsport.io/features/public-api
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-06'
description: bsport provides a boutique studio management platform that automates class scheduling, booking, payments, membership management, team payroll, and marketing tools. It serves yoga, pilates, indoor cycling, dance, boxing, martial arts, bootcamp, HIIT and other fitness studios, including multi‑location and franchise operations.
image: https://cdn.prod.website-files.com/69b9945989b426c38041ecbc/69b9945989b426c38041ecd5_Open%20graph%201200x630.png
layout: provider
modified: '2026-10-06'
name: Bsportsolution
nav: Providers
network: true
overview: 'Bsportsolution is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fitness, Software-as-a-Service, Scheduling, and Payments.


  Bsportsolution''s developer surface includes pricing, engineering blog, getting-started guide, documentation, and 10 more developer resources.'
plans:
- name: Bsportsolution Plans Pricing
  plan_count: 5
  slug: bsportsolution-plans-pricing
random_paper: 19
score:
  band: emerging
  composite: 24.7
  coverage:
    artifact_dirs: 8
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 55.4
    operational_transparency: 0.0
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 17.0
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bsportsolution Domain Security
  slug: bsportsolution-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: bsportsolution
tags:
- Company
- Fitness
- Software-as-a-Service
- Scheduling
- Payments
website: https://pro.bsport.io
---
