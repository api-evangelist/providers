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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-09-23'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.agrifulsoftware.com/
- group: start
  title: ''
  type: Login
  url: https://app.agrifulsoftware.com/
- group: operate
  title: ''
  type: Support
  url: https://www.agrifulsoftware.com/about/contacts-agriful-software
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.agrifulsoftware.com/about/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.agrifulsoftware.com/about/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Agriful-Software
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/agriful-software
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/agriful/refs/heads/main/llms/agriful-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agriful-llms.txt
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/agriful/refs/heads/main/plans/agriful-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/agriful-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/agriful/refs/heads/main/rate-limits/agriful-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/agriful-rate-limits.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/agriful/refs/heads/main/packages/agriful-packages.yml
  title: ''
  type: Packages
  url: packages/agriful-packages.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/agriful/refs/heads/main/security/agriful-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agriful-domain-security.yml
coverage:
  checked: '2026-09-12'
  detail: 'Agriful sells an end-user produce ERP with no developer program at all: there is no /developers or /docs path, docs.agrifulsoftware.com and developers.agrifulsoftware.com do not resolve, its GitHub organization has zero public repositories, and the only live machine surface is the RedwoodJS GraphQL endpoint at api.agrifulsoftware.com/graphql that backs its own single-page app — which answers anonymously but has introspection disabled in production and is documented nowhere.'
  evidence:
  - status: 200
    url: https://api.agrifulsoftware.com/graphql
  - status: 404
    url: https://api.agrifulsoftware.com/openapi.json
  - status: 404
    url: https://www.agrifulsoftware.com/openapi.json
  - status: 404
    url: https://www.agrifulsoftware.com/developers
  - status: 404
    url: https://www.agrifulsoftware.com/pricing
  - status: 404
    url: https://www.agrifulsoftware.com/.well-known/api-catalog
  - status: 200
    url: https://api.github.com/orgs/Agriful-Software/repos
  reason: no-developer-program
  state: none
created: '2026-09-12'
description: Agriful (Agriful Software Inc.) is a cloud ERP for the fresh produce industry, founded in 2022 by Patrick Crowley (CEO) and Deep Randhawa (CTO) and backed by Fractal Software and Reservoir Ventures. Its web platform runs sales and purchase order entry, live inventory control, lot-level traceability for FSMA and PTI compliance, produce-specific AR/AP accounting and grower settlements, and customizable reporting for produce brokers, marketers, packer-shippers, wholesalers and distributors. As of this profile Agriful publishes no developer program, API reference, OpenAPI or GraphQL schema, SDK, CLI, Postman collection or webhook catalog. The single live machine surface on its domain is the RedwoodJS GraphQL endpoint at api.agrifulsoftware.com/graphql that backs its own single-page application; it answers anonymous requests but has introspection disabled in production and is documented nowhere.
image: https://cdn.prod.website-files.com/6349c3dd59bbe2626264d298/6410a0ce0f67d016f4ee9010_Agriful%20-%20webclip.png
layout: provider
modified: '2026-09-12'
name: Agriful
nav: Providers
network: true
overview: 'Agriful is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Agriculture, Fresh Produce, Food Supply Chain, Traceability, and ERP.


  Agriful''s developer surface includes support and 11 more developer resources.'
plans:
- name: Agriful Plans Pricing
  plan_count: 0
  slug: agriful-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Agriful Rate Limits
  slug: agriful-rate-limits
score:
  band: emerging
  composite: 11.8
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
    operational_transparency: 2.6
  previous_composite: 11.8
  schema_version: 0.22.0
  scored_at: '2026-09-23'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Agriful Domain Security
  slug: agriful-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: agriful
tags:
- Agriculture
- Fresh Produce
- Food Supply Chain
- Traceability
- ERP
- Inventory Management
- Order Management
- Accounting
- Software-as-a-Service
- Company
website: https://www.agrifulsoftware.com/
---
