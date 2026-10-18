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
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/centrly/refs/heads/main/hosts/centrly-hosts.yml
  title: ''
  type: Hosts
  url: hosts/centrly-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/centrly/refs/heads/main/vendors/centrly-vendors.yml
  title: ''
  type: Vendors
  url: vendors/centrly-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.centrl.ai/legal/terms-of-use-for-guests/
- group: operate
  title: ''
  type: Support
  url: https://www.centrl.ai/contact/support/
- group: company
  title: ''
  type: Newsroom
  url: https://www.centrl.ai/company/news/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/centrly/refs/heads/main/security/centrly-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/centrly-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://centrl.ai/
coverage:
  checked: '2026-10-12'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract was found at the API host.
  evidence:
  - status: error
    url: https://api.centrl.ai/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-12'
description: Centrly is a technology company focused on providing advanced data integration and workflow automation solutions for enterprises. Founded with backing from leadout-capital, Centrally builds platforms that enable seamless connectivity between disparate SaaS applications, offering robust APIs, real-time synchronization, and customizable automation tools. The company aims to simplify complex data pipelines, improve operational efficiency, and empower businesses to orchestrate their digital ecosystems with greater agility and control.
layout: provider
modified: '2026-10-12'
name: Centrly
nav: Providers
network: true
overview: 'Centrly is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data Integration, Workflow Automation, Software-as-a-Service, and Enterprise.


  Centrly''s developer surface includes support and 6 more developer resources.'
random_paper: 21
score:
  band: minimal
  composite: 6.9
  coverage:
    artifact_dirs: 5
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 46.4
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Centrly Domain Security
  slug: centrly-domain-security
  summary_line: TLSv1.3 · DMARC
slug: centrly
tags:
- Company
- Data Integration
- Workflow Automation
- Software-as-a-Service
- Enterprise
website: https://centrl.ai/
---
