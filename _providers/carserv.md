---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 12.6
  scored_at: '2026-07-28'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://carserv.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CarServ
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/CarServ/public_api_client
- group: build
  title: ''
  type: Packages
  url: packages/carserv-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/carserv-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/carserv-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/carserv-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/carserv-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/carserv-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/carserv-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/carserv-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/carserv-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/carserv-llms.txt
created: '2026-07-17'
description: 'CarServ was auto repair shop management software — marketed as "the operating system for auto repair" — used by single-site shops and multi-location repair groups to run repair orders, Digital Vehicle Inspections, technician and service advisor workflows, customer communication and payments. The company was backed by Techstars. It is no longer operating: carserv.com returned HTTP 410 Gone through late 2024 and now resolves to a registrar parking page delegated to Afternic name servers. CarServ shipped a read-only JSON:API v2 "Public API" covering repair orders, customers, vehicles, appointments, inspections, operations and their part, labor and sublet line items, authenticated by exchanging an API key and secret for a JWT bearer token. No OpenAPI definition, developer portal or documentation survives; this profile reconstructs the historical API contract from the company''s own open-source Ruby client library, which remains public on GitHub.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/carserv.png
layout: provider
modified: '2026-07-20'
name: CarServ
nav: Providers
network: true
overview: 'CarServ is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Automotive, Auto Repair, Shop Management, and Vehicle Inspection.


  CarServ''s developer surface includes authentication and 12 more developer resources.'
random_paper: 20
score:
  band: minimal
  composite: 11.4
  delta: 0.5
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 17.4
    discoverability: 68.5
    governance: 3.1
    operational_transparency: 5.3
  previous_composite: 10.9
  provenance:
    conformance: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/carserv/refs/heads/main/screenshots/carserv-2026-07-25T204649.png
security:
- kind: authentication
  name: Carserv Authentication
  slug: carserv-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Carserv Domain Security
  slug: carserv-domain-security
  summary_line: TLSv1.3
slug: carserv
tags:
- Company
- Automotive
- Auto Repair
- Shop Management
- Vehicle Inspection
- Field Service
- SaaS
- JSON API
- Defunct
website: https://carserv.com/
---
