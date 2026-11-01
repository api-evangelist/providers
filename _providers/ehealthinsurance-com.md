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
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/ehealthinsurance-com/hosts/ehealthinsurance-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ehealthinsurance-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/ehealthinsurance-com/vendors/ehealthinsurance-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ehealthinsurance-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/ehealthinsurance-com/security/ehealthinsurance-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ehealthinsurance-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ehealthinsurance.com
created: '2026-10-24'
description: Ehealth is a health insurance technology platform offering digital tools for consumers to compare, purchase, and manage health insurance plans. The company provides APIs that enable integration of plan listings, enrollment assistance, and member services into third‑party applications, aiming to simplify the health insurance marketplace and improve user experience through modern web services.
layout: provider
modified: '2026-10-24'
name: Ehealth
nav: Providers
network: true
overview: Ehealth is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Insurance, Technology, and API.
random_paper: 23
score:
  band: minimal
  composite: 2.8
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 5.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Ehealthinsurance Com Domain Security
  slug: ehealthinsurance-com-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: ehealthinsurance-com
tags:
- Company
- Health
- Insurance
- Technology
- API
website: https://ehealthinsurance.com
---
