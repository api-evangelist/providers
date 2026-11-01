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
api_count: 1
apis:
- description: API documentation for GigaSpaces products and services.
  name: Gigaspaces API
  slug: gigaspaces-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/gigaspaces/vendors/gigaspaces-vendors.yml
  title: ''
  type: Vendors
  url: vendors/gigaspaces-vendors.yml
- group: agent
  href: https://artifacts.apis.io/gigaspaces/llms/gigaspaces-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/gigaspaces-llms.txt
- group: other
  href: https://artifacts.apis.io/gigaspaces/hosts/gigaspaces-hosts.yml
  title: ''
  type: Hosts
  url: hosts/gigaspaces-hosts.yml
- group: docs
  title: ''
  type: Documentation
  url: https://docs.gigaspaces.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Gigaspaces
- group: auth
  href: https://artifacts.apis.io/gigaspaces/security/gigaspaces-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/gigaspaces-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://gigaspaces.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.gigaspaces.com/privacy-policy/index.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.gigaspaces.com/terms-of-use/index.html
coverage:
  checked: '2026-10-20'
  detail: Documentation pages are rendered via JavaScript and no machine‑readable OpenAPI spec was found.
  evidence:
  - status: 200
    url: https://docs.gigaspaces.com/latest/landing.html
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-20'
description: GigaSpaces provides an in‑memory data grid, digital integration hub, and the Zaphira platform that protects enterprise systems from AI‑agent workloads. The company offers XAP for high‑performance Java applications, DIH for integration, and Zaphira for managing agentic traffic, helping customers modernize and secure mission‑critical workloads.
image: https://www.gigaspaces.com/assets/images/hero-social.png
layout: provider
modified: '2026-10-20'
name: Gigaspaces
nav: Providers
network: true
overview: 'Gigaspaces is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, In-Memory, Data Grid, Integration, and Artificial Intelligence.


  Gigaspaces'' developer surface includes documentation and 8 more developer resources.'
random_paper: 15
score:
  band: emerging
  composite: 12.2
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 57.1
    operational_transparency: 5.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 10.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Gigaspaces Domain Security
  slug: gigaspaces-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: gigaspaces
tags:
- Company
- In-Memory
- Data Grid
- Integration
- Artificial Intelligence
- Enterprise
website: https://gigaspaces.com/
---
