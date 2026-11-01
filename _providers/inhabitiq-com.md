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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/inhabitiq-com/hosts/inhabitiq-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/inhabitiq-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/inhabitiq-com/vendors/inhabitiq-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/inhabitiq-com-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://inhabit.com/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://inhabit.com/news/
- group: other
  title: ''
  type: Leadership
  url: https://inhabit.com/about/leadership/
- group: company
  title: ''
  type: Blog
  url: https://inhabit.com/blog/
- group: auth
  href: https://artifacts.apis.io/inhabitiq-com/security/inhabitiq-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/inhabitiq-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://inhabitiq.com/
coverage:
  checked: '2026-10-22'
  detail: The developer site renders content via JavaScript, preventing machine-readable spec discovery.
  evidence:
  - status: 200
    url: https://inhabit.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-22'
description: Inhabit is a global PropTech software company that provides property management and accounting software, along with related solutions such as payments, CRM, resident screening, utility billing, compliance, and digital marketing. Its products serve residential and vacation property managers, owners, and operators worldwide. The company offers both native integrations within its PMS and API‑based options for third‑party systems.
image: https://inhabit.com/wp-content/uploads/2022/03/property-management-software.png
layout: provider
modified: '2026-10-22'
name: Inhabit
nav: Providers
network: true
overview: 'Inhabit is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Property Management, Payments, CRM, Resident Screening, and Utility Billing.


  Inhabit''s developer surface includes engineering blog and 7 more developer resources.'
random_paper: 21
score:
  band: minimal
  composite: 6.2
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 51.8
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 8.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Inhabitiq Com Domain Security
  slug: inhabitiq-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: inhabitiq-com
tags:
- Property Management
- Payments
- CRM
- Resident Screening
- Utility Billing
- Compliance
- Vacation
- Residential
website: https://inhabitiq.com/
---
