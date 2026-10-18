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
- description: Digital health API providing caregiver support and health plan integration.
  name: Carallel API
  slug: carallel-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/carallelllc/refs/heads/main/hosts/carallelllc-hosts.yml
  title: ''
  type: Hosts
  url: hosts/carallelllc-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/carallelllc/refs/heads/main/vendors/carallelllc-vendors.yml
  title: ''
  type: Vendors
  url: vendors/carallelllc-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://carallel.com/terms-of-use-agreement/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://carallel.com/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://carallel.com/news
- group: company
  title: ''
  type: Blog
  url: https://carallel.com/category/article/blog/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/carallelllc/refs/heads/main/security/carallelllc-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/carallelllc-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://carallel.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://carallel.com
  - status: 403
    url: https://equityzen.com/company/carallelllc
  reason: no-developer-program
  state: none
created: '2026-10-06'
description: Carallelllc, operating as Carallel, provides digital health tools and personalized caregiver support for health plans, providers, and employers. Their platform combines technology with human guidance to identify caregivers, offer resources, and improve outcomes while reducing costs. The company focuses on empowering caregivers through a secure app, expert advice, and data-driven insights, aiming to enhance patient care and workforce wellbeing across the United States.
image: https://carallel.com/wp-content/uploads/2021/08/identify-icon.svg
layout: provider
modified: '2026-10-06'
name: Carallelllc
nav: Providers
network: true
overview: 'Carallelllc is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Digital Health, Caregiver Support, Health Plans, and Providers.


  Carallelllc''s developer surface includes engineering blog and 7 more developer resources.'
random_paper: 3
score:
  band: minimal
  composite: 10.4
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 58.9
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 10.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Carallelllc Domain Security
  slug: carallelllc-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: carallelllc
tags:
- Company
- Digital Health
- Caregiver Support
- Health Plans
- Providers
- Employers
website: https://carallel.com
---
