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
  href: https://artifacts.apis.io/accertify/vendors/accertify-vendors.yml
  title: ''
  type: Vendors
  url: vendors/accertify-vendors.yml
- group: agent
  href: https://artifacts.apis.io/accertify/llms/accertify-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/accertify-llms.txt
- group: other
  href: https://artifacts.apis.io/accertify/hosts/accertify-hosts.yml
  title: ''
  type: Hosts
  url: hosts/accertify-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.accertify.com/terms-and-conditions/
- group: company
  title: ''
  type: Newsroom
  url: https://www.accertify.com/resources/resource-category/news/page/1/
- group: company
  title: ''
  type: Blog
  url: https://www.accertify.com/resources/resource-category/blog/page/1/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.accertify.com/
- group: auth
  href: https://artifacts.apis.io/accertify/security/accertify-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/accertify-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.accertify.com/
- group: auth
  href: https://artifacts.apis.io/accertify/security/accertify-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/accertify-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.accertify.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://developer.accertify.com/mcp
  - status: 200
    url: https://www.accertify.com/
  reason: no-developer-program
  state: none
created: '2026-10-26'
description: Accertify provides a leading fraud prevention and risk management platform, offering APIs and services that help businesses detect and prevent fraudulent transactions, manage chargebacks, and secure payment processes across industries such as e‑commerce, financial services, and gaming.
image: https://www.accertify.com/wp-content/uploads/2026/05/More-Yes-Say-it-with-Confidence.png
layout: provider
modified: '2026-10-26'
name: Accertify
nav: Providers
network: true
overview: 'Accertify is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fraud, Payments, RiskManagement, and API.


  Accertify''s developer surface includes engineering blog, documentation, and 9 more developer resources.'
random_paper: 18
score:
  band: minimal
  composite: 7.9
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 50.0
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
  name: Accertify Domain Security
  slug: accertify-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: accertify
tags:
- Company
- Fraud
- Payments
- RiskManagement
- API
- FinTech
website: https://www.accertify.com/
---
