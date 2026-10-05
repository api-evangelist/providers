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
- description: API for Beginlearning services
  name: Beginlearning API
  slug: beginlearning-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/beginlearning/refs/heads/main/llms/beginlearning-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/beginlearning-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/beginlearning/refs/heads/main/hosts/beginlearning-hosts.yml
  title: ''
  type: Hosts
  url: hosts/beginlearning-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/beginlearning/refs/heads/main/vendors/beginlearning-vendors.yml
  title: ''
  type: Vendors
  url: vendors/beginlearning-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://www.beginlearning.com/signin
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/beginlearning/refs/heads/main/security/beginlearning-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/beginlearning-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.beginlearning.com
- group: company
  title: ''
  type: AboutUs
  url: https://www.beginlearning.com/about-us
- group: operate
  title: ''
  type: Support
  url: https://support.beginlearning.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.beginlearning.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.beginlearning.com/privacy-policy
coverage:
  checked: '2026-09-27'
  detail: OpenAPI spec endpoints on api.beginlearning.com return 403 Forbidden, indicating access is restricted.
  evidence:
  - status: 403
    url: https://api.beginlearning.com/openapi.json
  - status: 403
    url: https://api.beginlearning.com/openapi.yaml
  reason: partner-login
  state: gated
created: '2026-09-27'
description: Beginlearning provides award‑winning learning products for children ages 2‑10, offering digital apps, hands‑on kits, and educational resources. Their mission is to give every child the best start to achieving their fullest potential through play‑based learning, supporting parents and educators with tools and content that foster curiosity and growth.
image: https://static.beginlearning.com/deployedassets/63b70baf/static/img/begin/begin-logo.svg
layout: provider
modified: '2026-09-27'
name: Beginlearning
nav: Providers
network: true
overview: 'Beginlearning publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Children, Learning, DigitalApps, and Toys.


  Beginlearning''s developer surface includes support and 9 more developer resources.'
random_paper: 1
score:
  band: emerging
  composite: 13.5
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
    developer_ergonomics: 4.8
    discoverability: 64.3
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 13.7
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Beginlearning Domain Security
  slug: beginlearning-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: beginlearning
tags:
- Education
- Children
- Learning
- DigitalApps
- Toys
website: https://www.beginlearning.com
---
