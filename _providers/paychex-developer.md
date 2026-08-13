---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Paychex Developer Agentic Access
  operation_count: 5
  slug: paychex-developer-agentic-access
  summary_line: 5 operations · 1 acting
api_count: 3
apis:
- description: Companies available to the registered application.
  name: Paychex Companies API
  slug: paychex-developer-companies-api
- description: Time entry, punch, and time-worked submissions.
  name: Paychex Time Entries API
  slug: paychex-developer-time-entries-api
- description: Employees and contractors for a Paychex Flex company.
  name: Paychex Workers API
  slug: paychex-developer-workers-api
artifact_total: 45
collections:
- collection_type: open
  name: Paychex Payroll Companies API
  slug: open-paychex-payroll-companies
- collection_type: open
  name: Paychex Time API
  slug: open-paychex-time
- collection_type: open
  name: Paychex Workers API
  slug: open-paychex-workers
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/paychex-developer-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/paychex-developer-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/paychex-developer-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/paychex-developer-scopes.yml
- group: start
  title: ''
  type: Portal
  url: https://developer.paychex.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.paychex.com/documentation
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.paychex.com/getting-started/overview
- group: auth
  title: ''
  type: Authentication
  url: https://developer.paychex.com/getting-started/overview
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/paychex
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/paychex
- group: other
  title: ''
  type: X
  url: https://x.com/Paychex
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/Paychex
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/PaychexInc
- group: company
  title: ''
  type: Blog
  url: https://www.paychex.com/articles
- group: company
  title: ''
  type: Newsroom
  url: https://www.paychex.com/newsroom
- group: company
  title: ''
  type: InvestorRelations
  url: https://investor.paychex.com/
- group: operate
  title: ''
  type: SupportContact
  url: https://developer.paychex.com/support
- group: docs
  title: Paychex Payroll Companies OpenAPI
  type: OpenAPI
  url: openapi/_original/paychex-payroll-companies-openapi.yml
- group: docs
  title: Paychex Workers OpenAPI
  type: OpenAPI
  url: openapi/_original/paychex-workers-openapi.yml
- group: docs
  title: Paychex Time OpenAPI
  type: OpenAPI
  url: openapi/_original/paychex-time-openapi.yml
- group: docs
  title: Paychex Company JSON Schema
  type: JSONSchema
  url: json-schema/paychex-companies-company-schema.json
- group: docs
  title: Paychex Worker JSON Schema
  type: JSONSchema
  url: json-schema/paychex-workers-worker-schema.json
- group: design
  title: Paychex JSON-LD Context
  type: JSONLD
  url: json-ld/paychex-developer-context.jsonld
- group: commercial
  title: Paychex Plans and Pricing
  type: Plans
  url: plans/paychex-developer-plans-pricing.yml
- group: operate
  title: Paychex Rate Limits
  type: RateLimits
  url: rate-limits/paychex-developer-rate-limits.yml
- group: commercial
  title: Paychex FinOps Profile
  type: FinOps
  url: finops/paychex-developer-finops.yml
- group: design
  title: Paychex Vocabulary
  type: Vocabulary
  url: vocabulary/paychex-developer-vocabulary.yml
- group: design
  title: Paychex Spectral Rules
  type: SpectralRules
  url: rules/paychex-developer-rules.yml
created: '2026-05-25'
description: 'Paychex, Inc. (NASDAQ: PAYX) is a Rochester, New York-based provider of integrated payroll, human resources, retirement, insurance, and benefits outsourcing services for small- and medium-sized businesses, with developer APIs exposed through the Paychex Flex platform.'
examples:
- key_count: 1
  name: Paychex Companies Getcompany Example
  slug: paychex-companies-getcompany-example
- key_count: 2
  name: Paychex Companies Listcompanies Example
  slug: paychex-companies-listcompanies-example
- key_count: 2
  name: Paychex Time Createtimeentries Request Example
  slug: paychex-time-createtimeentries-request-example
- key_count: 3
  name: Paychex Time Createtimeentries Response Example
  slug: paychex-time-createtimeentries-response-example
- key_count: 1
  name: Paychex Workers Getcompanyworker Example
  slug: paychex-workers-getcompanyworker-example
- key_count: 2
  name: Paychex Workers Listcompanyworkers Example
  slug: paychex-workers-listcompanyworkers-example
features:
- description: Every API call is scoped to a company resource that the registered application has been granted explicit access to, enforcing tenant isolation across Paychex Flex clients.
  name: Company-Scoped Access
- description: List, retrieve, and update worker records — including personal information, work assignments, and pay rates — for hire-to-retire HR workflows.
  name: Worker Lifecycle Management
- description: Submit time entries, punches, and time-worked records from third-party time and attendance systems so they flow into Paychex Payroll processing.
  name: Time Data Ingest
- description: All APIs are protected by an OAuth 2.0 client_credentials flow tied to a registered Paychex partner or client application; there is no end-user OAuth dance.
  name: OAuth 2.0 Client Credentials
- description: Production access is gated behind partner registration and Paychex approval; sandbox credentials are issued during integration review rather than via self-serve signup.
  name: Partner-Approved Integrations
- description: APIs read and write against the same Paychex Flex platform used by ~800,000 payroll clients, so changes flow through the same payroll, HR, and benefits engines.
  name: Paychex Flex Native
finops:
- name: Paychex Developer Finops
  service_category: Human Capital Management
  slug: paychex-developer-finops
image: https://raw.githubusercontent.com/api-evangelist/paychex-developer/refs/heads/main/image.png
integrations:
- description: Native integration with Paychex Flex — the cloud HR, payroll, time, and benefits platform that the developer APIs sit on top of.
  name: Paychex Flex
- description: Native time and attendance product whose data model is exposed (and writable) via the Paychex Time API for third-party time vendors.
  name: Paychex Time
- description: Professional Employer Organization (PEO) co-employment services that share the same underlying worker and company records exposed via the developer APIs.
  name: Paychex HR PEO
- description: Partner marketplace where vetted ISVs publish integrations built on the Paychex developer APIs.
  name: Paychex Marketplace
- description: Paychex completed its $4.1B acquisition of Paycor in 2025, expanding the HCM surface area covered by the broader Paychex platform.
  name: Paycor (Acquired 2025)
json_schemas:
- name: Paychex Company
  property_count: 7
  slug: paychex-companies-company
- name: Paychex Time Entry
  property_count: 7
  slug: paychex-time-timeentry
- name: Paychex Worker
  property_count: 7
  slug: paychex-workers-worker
json_structures:
- name: Paychex Companies Company Structure
  property_count: 7
  slug: paychex-companies-company-structure
- name: Paychex Workers Worker Structure
  property_count: 6
  slug: paychex-workers-worker-structure
jsonld:
- class_count: 8
  name: Paychex Companies Context
  property_count: 0
  slug: paychex-companies-context
- class_count: 23
  name: Paychex Developer Context
  property_count: 0
  slug: paychex-developer-context
- class_count: 19
  name: Paychex Workers Context
  property_count: 0
  slug: paychex-workers-context
layout: provider
modified: '2026-05-25'
name: Paychex
nav: Providers
network: true
overview: 'Paychex publishes 3 APIs on the [APIs.io](https://apis.io/) network: Companies API, Time Entries API, and Workers API. Tagged areas include Benefits, HCM, HR, Paychex Flex, and Payroll.


  The Paychex catalog on APIs.io includes 3 JSON-LD contexts and 2 Spectral governance rulesets.


  Paychex''s developer surface includes authentication, developer portal, documentation, getting-started guide, YouTube channel, engineering blog, and 22 more developer resources.'
plans:
- name: Paychex Developer Plans Pricing
  plan_count: 2
  slug: paychex-developer-plans-pricing
random_paper: 85
rate_limits:
- limit_count: 4
  name: Paychex Developer Rate Limits
  slug: paychex-developer-rate-limits
rules:
- name: Paychex API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: paychex-developer-jsonschema-spectral-rules
- name: Paychex API Rules
  rule_count: 9
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 5
  slug: paychex-developer-rules
scopes:
- name: Paychex Developer Scopes
  scope_count: 0
  slug: paychex-developer-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 52.8
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 73.1
    developer_ergonomics: 41.3
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 36.8
  previous_composite: 52.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/paychex-developer/refs/heads/main/screenshots/paychex-developer-2026-06-20T191450.png
security:
- kind: authentication
  name: Paychex Developer Authentication
  slug: paychex-developer-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Paychex Developer Domain Security
  slug: paychex-developer-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: paychex-developer
tags:
- Benefits
- HCM
- HR
- Paychex Flex
- Payroll
- Time and Attendance
- Workforce
- Fortune 1000
use_cases:
- description: Keep an external HRIS or workforce-management system in sync with Paychex Flex by listing companies, mirroring workers, and reconciling pay and assignment changes.
  name: HRIS and Payroll Sync
- description: Push punches, time entries, and time-worked totals from third-party time tracking tools into Paychex Payroll so labor data drives paychecks automatically.
  name: Time and Attendance Integration
- description: Trigger downstream onboarding workflows — provisioning, benefits, equipment — when a new worker is created or activated in Paychex Flex.
  name: Onboarding Automation
- description: ISVs and vertical SaaS platforms surface Paychex payroll inside their own product, using the developer APIs to read companies and workers and feed payroll inputs.
  name: Embedded Payroll for Partners
- description: Pull worker, company, and time data into BI and people-analytics stacks for headcount, labor cost, and compliance reporting.
  name: Analytics and Workforce Reporting
website: https://developer.paychex.com/
---
