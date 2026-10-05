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
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-04'
api_count: 1
apis:
- description: Aptimiz provides digital solutions for agricultural time‑tracking and farm management. Documentation is available at the website but no machine‑readable contract was found.
  name: Aptimiz API
  slug: aptimiz-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aptimiz/refs/heads/main/vendors/aptimiz-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aptimiz-vendors.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aptimiz/refs/heads/main/hosts/aptimiz-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aptimiz-hosts.yml
- group: docs
  title: ''
  type: Documentation
  url: https://dev.aptimiz.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aptimiz/refs/heads/main/security/aptimiz-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aptimiz-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aptimiz.com
- group: start
  title: ''
  type: GettingStarted
  url: https://aptimiz.com/a-propos/
- group: operate
  title: ''
  type: Support
  url: https://aptimiz.com/contact/
- group: commercial
  title: ''
  type: Pricing
  url: https://aptimiz.com/prerequis-techniques/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aptimiz.com/cgv/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aptimiz.com/politique-de-confidentialite/
coverage:
  checked: 2026-09-25
  detail: Documentation pages are HTML only and no OpenAPI/AsyncAPI/GraphQL contract could be located.
  evidence:
  - status: 200
    url: https://aptimiz.com
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-25'
description: Aptimiz provides digital solutions for agricultural time‑tracking and farm management, offering connected devices and software to monitor labor, equipment, traceability, and crop activities. Their platform helps growers optimize operations, ensure regulatory compliance, and improve decision‑making through real‑time data.
layout: provider
modified: '2026-09-25'
name: Aptimiz
nav: Providers
network: true
overview: 'Aptimiz publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Agriculture, Farm Management, Time Tracking, Connected Devices, and Compliance.


  Aptimiz''s developer surface includes documentation, getting-started guide, support, pricing, and 6 more developer resources.'
random_paper: 18
score:
  band: emerging
  composite: 16.6
  coverage:
    artifact_dirs: 5
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 53.6
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aptimiz Domain Security
  slug: aptimiz-domain-security
  summary_line: TLSv1.3 · DMARC
slug: aptimiz
tags:
- Agriculture
- Farm Management
- Time Tracking
- Connected Devices
- Compliance
website: https://aptimiz.com
---
