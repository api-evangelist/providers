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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: API for SFI Solution accounting platform, documented at the company website.
  name: SFI Solution API
  slug: sfi-solution-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/sfisolution/plans/sfisolution-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/sfisolution-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/sfisolution/hosts/sfisolution-hosts.yml
  title: ''
  type: Hosts
  url: hosts/sfisolution-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sfisolution.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sfisolution.com/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://sfisolution.com/pricing
- group: start
  title: ''
  type: Login
  url: https://probook.sfisolution.com/login
- group: auth
  href: https://artifacts.apis.io/sfisolution/security/sfisolution-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sfisolution-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sfisolution.com/
coverage:
  checked: '2026-10-21'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found on any discovered host.
  evidence:
  - status: 0
    url: https://api.sfisolution.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-21'
description: SFI Solution provides modern accounting software with built-in reconciliation, serving accountants and businesses with end‑to‑end bookkeeping, invoicing, tax, and financial reporting. Their platform integrates bank data, supports VAT/GST, and offers AI‑driven transaction matching, targeting enterprise clients and offering a free trial.
layout: provider
modified: '2026-10-21'
name: SFI Solution
nav: Providers
network: true
overview: 'SFI Solution is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Accounting, Software, Software-as-a-Service, and Finance.


  SFI Solution''s developer surface includes pricing and 7 more developer resources.'
plans:
- name: Sfisolution Plans Pricing
  plan_count: 3
  slug: sfisolution-plans-pricing
random_paper: 15
score:
  band: emerging
  composite: 20.4
  coverage:
    artifact_dirs: 8
    catalog_earned: 42.0
    catalog_earned_first_party: 12.0
    catalog_gap: 73.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 53.6
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Sfisolution Domain Security
  slug: sfisolution-domain-security
  summary_line: TLSv1.3 · DMARC
slug: sfisolution
tags:
- Company
- Accounting
- Software
- Software-as-a-Service
- Finance
website: https://sfisolution.com/
---
