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
- description: API for Carver Edison providing data integration and device control for renewable energy management.
  name: Carver Edison API
  slug: carver-edison-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/carver-edison/refs/heads/main/llms/carver-edison-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/carver-edison-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/carver-edison/refs/heads/main/hosts/carver-edison-hosts.yml
  title: ''
  type: Hosts
  url: hosts/carver-edison-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/carver-edison/refs/heads/main/vendors/carver-edison-vendors.yml
  title: ''
  type: Vendors
  url: vendors/carver-edison-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://carveredison.com/newsroom/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/carveredison
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/carver-edison/refs/heads/main/security/carver-edison-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/carver-edison-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://carveredison.com/
- group: docs
  title: ''
  type: Documentation
  url: https://carveredison.com/platform/
- group: company
  title: ''
  type: Blog
  url: https://carveredison.com/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://carveredison.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://carveredison.com/privacy/
coverage:
  checked: '2026-10-07'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract found at the API host.
  evidence:
  - status: 0
    url: https://api.carveredison.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-07'
description: Carver Edison is a technology company focused on innovative solutions in the energy sector. The firm develops advanced hardware and software platforms for renewable energy management, offering APIs for data integration, device control, and analytics. While detailed public information is limited, the company positions itself as a partner for enterprises seeking to modernize energy infrastructure and improve operational efficiency. Carver Edison provides tools to reduce stock‑based compensation expense, minimize dilution, and enhance earnings per share for finance teams, while also delivering employee equity participation solutions for HR and total‑rewards groups. Its platform integrates with existing ERP and payroll systems, delivering real‑time insights and automated workflows for equity plan administration.
image: https://carveredison.com/assets/og/home-card.png
layout: provider
modified: '2026-10-07'
name: Carver Edison
nav: Providers
network: true
overview: 'Carver Edison is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Finance, Equity, Software-as-a-Service, Platform, and Stock-Compensation.


  Carver Edison''s developer surface includes documentation, engineering blog, and 9 more developer resources.'
random_paper: 10
score:
  band: emerging
  composite: 13.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 66.1
    operational_transparency: 5.3
  provenance:
    mcp: derived
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
  name: Carver Edison Domain Security
  slug: carver-edison-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: carver-edison
tags:
- Finance
- Equity
- Software-as-a-Service
- Platform
- Stock-Compensation
website: https://carveredison.com/
---
