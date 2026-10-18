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
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: Purolator developer portal provides REST API catalogue for shipping services.
  name: Purolator Shipping API
  slug: purolator-shipping-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/purolator/refs/heads/main/hosts/purolator-hosts.yml
  title: ''
  type: Hosts
  url: hosts/purolator-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/purolator/refs/heads/main/vendors/purolator-vendors.yml
  title: ''
  type: Vendors
  url: vendors/purolator-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.purolator.com/en/terms-and-conditions-service
- group: operate
  title: ''
  type: Support
  url: https://www.purolator.com/en/support/contact-us/confirm
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://community.purolator.com/en/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://www.purolator.com/en/media/23081/edit?destination=/en/node/16/latest
- group: start
  title: ''
  type: Login
  url: https://community.purolator.com/en/user/login
- group: start
  title: ''
  type: DeveloperPortal
  url: https://ship.purolator.com/developer/restapicatalogue?lang=en
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/purolator/refs/heads/main/security/purolator-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/purolator-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.purolator.com
coverage:
  checked: '2026-10-13'
  detail: Developer portal page returns HTML with JavaScript and no machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://ship.purolator.com/developer/restapicatalogue?lang=en
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-13'
description: Purolator is a leading North American courier and logistics company offering a comprehensive suite of shipping, freight, and supply chain solutions for businesses and consumers. Their services include domestic and international parcel delivery, freight transportation, customs brokerage, and e‑commerce integrations, supported by a robust online platform and developer resources. Purolator emphasizes reliability, tracking visibility, and flexible delivery options across Canada, the United States, and worldwide.
image: https://www.purolator.com/themes/custom/purolator_theme/logo.png
layout: provider
modified: '2026-10-13'
name: Purolator
nav: Providers
network: true
overview: 'Purolator is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Shipping, Logistics, Couriers, and Freight.


  Purolator''s developer surface includes support and 9 more developer resources.'
random_paper: 10
score:
  band: emerging
  composite: 15.4
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 58.9
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Purolator Domain Security
  slug: purolator-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: purolator
tags:
- Company
- Shipping
- Logistics
- Couriers
- Freight
website: https://www.purolator.com
---
