---
agent_readiness:
  band: agent-aware
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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/getflex-com/llms/getflex-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/getflex-com-llms.txt
- group: other
  href: https://artifacts.apis.io/getflex-com/hosts/getflex-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/getflex-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/getflex-com/vendors/getflex-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/getflex-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://getflex.com/legal/terms-referral-program
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://getflex.com/legal/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://getflex.com/legal/pricing-updates-faq
- group: company
  title: ''
  type: Newsroom
  url: https://getflex.com/blog-page/newsroom
- group: company
  title: ''
  type: Blog
  url: https://getflex.com/blog
- group: docs
  title: ''
  type: Documentation
  url: https://help.getflex.com/
- group: auth
  href: https://artifacts.apis.io/getflex-com/security/getflex-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/getflex-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.getflex.com
coverage:
  checked: '2026-10-22'
  detail: No public API documentation or machine‑readable contract was found on getflex.com.
  evidence:
  - status: 404
    url: https://getflex.com/openapi.json
  reason: not-a-software-company
  state: none
created: '2026-10-22'
description: Flex is a financial‑technology bill‑payment app that lets consumers split rent, mortgage, car payments and everyday bills such as utilities, phone, internet and insurance. Users choose a second payment date while Flex pays the biller the full amount up‑front. The service includes a monthly membership fee, processing and split fees, and can report on‑time rent payments to the major credit bureaus.
image: https://cdn.prod.website-files.com/69a1b0e50ebde6e2633ccfc5/69cd3d7f3d608d02b4a2858a_logo-seo%20(1)%201.svg
layout: provider
modified: '2026-10-22'
name: Flex
nav: Providers
network: true
overview: 'Flex is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Bill Splitting, Rent Payments, Mortgage Payments, Car Payments, and Utilities.


  Flex''s developer surface includes pricing, engineering blog, documentation, and 8 more developer resources.'
random_paper: 11
score:
  band: emerging
  composite: 13.4
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 11.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Getflex Com Domain Security
  slug: getflex-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: getflex-com
tags:
- Bill Splitting
- Rent Payments
- Mortgage Payments
- Car Payments
- Utilities
- Financial Technology
- Credit Reporting
website: https://www.getflex.com
---
