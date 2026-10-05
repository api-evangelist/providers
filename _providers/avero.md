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
- description: Developer portal for Avero providing API documentation and resources.
  name: Avero API
  slug: avero-api
artifact_total: 3
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/avero/refs/heads/main/plans/avero-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/avero-plans-pricing.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/avero/refs/heads/main/well-known/avero-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/avero-status-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/avero/refs/heads/main/well-known/avero-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/avero-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avero/refs/heads/main/hosts/avero-hosts.yml
  title: ''
  type: Hosts
  url: hosts/avero-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avero/refs/heads/main/vendors/avero-vendors.yml
  title: ''
  type: Vendors
  url: vendors/avero-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://averoinc.com/legal-notice
- group: operate
  title: ''
  type: StatusPage
  url: http://status.averoinc.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://averoinc.com/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://login.averoinc.com/r/auth/login
- group: docs
  title: ''
  type: Documentation
  url: https://developer.averoinc.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/avero/refs/heads/main/security/avero-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/avero-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://averoinc.com
coverage:
  checked: 2026-09-26
  detail: Developer portal returns only a JavaScript SPA shell with no machine‑readable OpenAPI spec.
  evidence:
  - status: 404
    url: https://developer.averoinc.com/openapi.json
  - status: 404
    url: https://developer.averoinc.com/openapi.yaml
  - status: 200
    url: https://developer.averoinc.com/api-docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-26'
description: Avero provides a cloud‑based hospitality operations platform that helps restaurant operators, hotel groups, casinos and other food‑service businesses manage staff, inventory, sales and customer engagement. The solution offers real‑time dashboards, mobile logbooks, and analytics to improve efficiency and service quality across multiple locations.
layout: provider
modified: '2026-09-26'
name: Avero
nav: Providers
network: true
overview: 'Avero publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Hospitality, Restaurant, Software-as-a-Service, and Analytics.


  Avero''s developer surface includes documentation and 11 more developer resources.'
plans:
- name: Avero Plans Pricing
  plan_count: 3
  slug: avero-plans-pricing
random_paper: 13
score:
  band: emerging
  composite: 21.3
  coverage:
    artifact_dirs: 5
    catalog_earned: 37.0
    catalog_earned_first_party: 12.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 44.6
    operational_transparency: 15.8
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
  name: Avero Domain Security
  slug: avero-domain-security
  summary_line: TLSv1.3 · DMARC
slug: avero
tags:
- Hospitality
- Restaurant
- Software-as-a-Service
- Analytics
website: https://averoinc.com
---
