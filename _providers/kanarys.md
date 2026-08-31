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
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 0
common:
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/kanarysinc
coverage:
  checked: '2026-08-23'
  detail: Kanarys sold its IP and name to a chief-diversity-officer special-purpose vehicle in mid-2024 and its domain has since been abandoned — kanarys.com served the real site through 22 April 2026 and by 17 May 2026 became a GoDaddy parking lander that answers HTTP 200 with the same 114-byte redirect stub for every path, including a randomly generated control path, /openapi.json and /.well-known/agent-card.json.
  evidence:
  - status: 200
    url: https://kanarys.com/
  - status: 200
    url: https://kanarys.com/this-is-a-control-path-a7f3d9
  - status: 200
    url: https://kanarys.com/openapi.json
  - status: 200
    url: https://kanarys.com/.well-known/agent-card.json
  - status: 200
    url: https://kanarys.com/.well-known/security.txt
  - status: 200
    url: https://kanarys.com/sitemap.xml
  - status: 0
    url: https://api.kanarys.com/
  - status: 0
    url: https://docs.kanarys.com/
  - status: 0
    url: https://developer.kanarys.com/
  - status: 200
    url: https://api.github.com/orgs/Kanarysinc
  - status: 404
    url: https://pypi.org/pypi/kanarys/json
  - status: 404
    url: https://registry.npmjs.org/kanarys
  - status: 200
    url: https://www.linkedin.com/company/kanarysinc
  reason: defunct
  state: none
created: '2026-08-23'
description: 'Kanarys, Inc. was a Dallas, Texas workforce-analytics company founded in 2018 by Mandy Price, Star Carter and Bennie King. Its SaaS platform combined employee experience surveys, demographic and cultural data, anonymous employee reviews and peer benchmarking to give enterprise HR and diversity leaders analytics on workplace inclusion. Integration with customer HRIS, ATS and payroll systems was delivered as managed, per-customer connectors run by Kanarys staff rather than as a self-serve public API, and the company never published a developer portal, an OpenAPI or any other machine-readable contract. Kanarys raised a $5M Series A, counted 7-Eleven and Yum! Brands among its customers, and in mid-2024 sold its intellectual property and name to a special-purpose vehicle formed by a group of former chief diversity officers; co-founder Mandy Price left for the Draper Richards Kaplan Foundation in February 2025. The company now operates no public web surface: kanarys.com served the
  real site as recently as 22 April 2026 and is a GoDaddy parking lander as of 17 May 2026, and no successor domain resolves.'
layout: provider
modified: '2026-08-23'
name: Kanarys
nav: Providers
network: true
overview: Kanarys is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Human Resources, HR Technology, Workforce Analytics, and Employee Experience.
random_paper: 5
score:
  band: minimal
  composite: 4.6
  coverage:
    artifact_dirs: 1
    catalog_gap: 90.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.3
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 4.6
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
slug: kanarys
tags:
- Company
- Human Resources
- HR Technology
- Workforce Analytics
- Employee Experience
- Diversity Equity and Inclusion
- Survey
- Benchmarking
- Analytics
- Enterprise Software
---
