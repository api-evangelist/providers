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
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/coheed/refs/heads/main/plans/coheed-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/coheed-plans-pricing.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/coheed/refs/heads/main/llms/coheed-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/coheed-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/coheed/refs/heads/main/hosts/coheed-hosts.yml
  title: ''
  type: Hosts
  url: hosts/coheed-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/coheed/refs/heads/main/vendors/coheed-vendors.yml
  title: ''
  type: Vendors
  url: vendors/coheed-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://www.coheed.nl/login
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/coheed/refs/heads/main/security/coheed-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/coheed-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://coheed.nl/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.coheed.nl/en/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.coheed.nl/en/blogs
- group: operate
  title: ''
  type: Contact
  url: https://www.coheed.nl/en/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.coheed.nl/en/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.coheed.nl/en/terms
coverage:
  checked: '2026-10-16'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract found on api.coheed.nl.
  evidence:
  - status: 0
    url: https://api.coheed.nl/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-16'
description: Coheed provides a cloud platform for orders, planning, and invoices that always match. Their solutions synchronize ERP, CRM, and SCM data flows, ensuring teams have accurate records across the lead‑to‑cash process. Features include data integration, data quality checks, insights, and automated agents that improve operations with human‑in‑the‑loop approval. Use cases cover predictive customer lifetime value, lead‑to‑quote automation, order exception monitoring, and dynamic inventory optimization, targeting logistics, B2B commerce, wholesale, and manufacturing industries.
image: https://www.coheed.nl/nl/opengraph-image
layout: provider
modified: '2026-10-16'
name: Coheed
nav: Providers
network: true
overview: 'Coheed is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, ERP, CRM, SCM, and Data Integration.


  Coheed''s developer surface includes pricing, engineering blog, and 10 more developer resources.'
plans:
- name: Coheed Plans Pricing
  plan_count: 2
  slug: coheed-plans-pricing
random_paper: 0
score:
  band: emerging
  composite: 19.0
  coverage:
    artifact_dirs: 9
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 55.4
    operational_transparency: 0.0
  provenance:
    mcp: unknown
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
  name: Coheed Domain Security
  slug: coheed-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: coheed
tags:
- Company
- ERP
- CRM
- SCM
- Data Integration
- Automation
website: https://coheed.nl/
---
