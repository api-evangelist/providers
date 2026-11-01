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
  href: https://artifacts.apis.io/central-payments/hosts/central-payments-hosts.yml
  title: ''
  type: Hosts
  url: hosts/central-payments-hosts.yml
- group: other
  href: https://artifacts.apis.io/central-payments/vendors/central-payments-vendors.yml
  title: ''
  type: Vendors
  url: vendors/central-payments-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://support.central-payments.com/hc/en-us
- group: auth
  href: https://artifacts.apis.io/central-payments/security/central-payments-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/central-payments-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://central-payments.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://central-payments.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://central-payments.com/terms-of-use
- group: company
  title: ''
  type: Blog
  url: https://central-payments.com/insights
- group: operate
  title: ''
  type: Contact
  url: https://central-payments.com/contact-us
coverage:
  checked: '2026-10-20'
  detail: The website provides only marketing pages with no machine‑readable API specification.
  evidence:
  - status: 200
    url: https://central-payments.com
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-20'
description: Central Payments provides embedded finance solutions, offering configurable card products, funds movement, and program management for brands and banks. Their platform simplifies integration with compliance, oversight, and settlement services, delivering a unified API for payments, regulatory adherence, and customizable financial products. With a focus on transparency and innovation, Central Payments aims to streamline financial services for businesses, ensuring secure, efficient, and scalable payment experiences.
image: http://static1.squarespace.com/static/66cc982cdb1dd02811d78158/t/688cc545a926fc7765d8a2ea/1771431163074/CP-Logo_Stacked_Black.jpg?format=1500w
layout: provider
modified: '2026-10-20'
name: Central Payments
nav: Providers
network: true
overview: 'Central Payments is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Payments, EmbeddedFinance, and API.


  Central Payments'' developer surface includes support, engineering blog, and 7 more developer resources.'
random_paper: 15
score:
  band: minimal
  composite: 9.4
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 12.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Central Payments Domain Security
  slug: central-payments-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: central-payments
tags:
- Company
- Fintech
- Payments
- EmbeddedFinance
- API
website: https://central-payments.com/
---
