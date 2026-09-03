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
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.4
  scored_at: '2026-09-03'
api_count: 1
apis:
- baseURL: https://api.rasgoml.com
  baseurl_source: declared
  description: Table metadata operations
  name: Rasgo Metadata API
  slug: rasgo-metadata-api
artifact_total: 5
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Rasgo Metadata API
  slug: open-rasgo-metadata-api
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rasgo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.rasgoml.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.rasgoml.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.rasgoml.com/rasgo-docs/readme.md
- group: docs
  title: ''
  type: APIReference
  url: https://docs.rasgoml.com/rasgo-docs/api.md
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.rasgoml.com/rasgo-docs/set-up-rasgo.md
- group: start
  title: ''
  type: SignUp
  url: https://app.rasgoml.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.rasgoml.com/rasgo-docs/whats-new.md
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/rasgo-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/rasgo-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/rasgo-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/rasgo-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/rasgo-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/rasgo-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/rasgo-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/rasgo-changelog.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/rasgo-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Rasgo is an AI-powered Copilot for your data warehouse, letting teams query and analyze their data through natural-language interfaces while the data stays inside their existing warehouse. The Rasgo AI agent translates data-warehouse metadata into an LLM-friendly form and can be trained on a specific business domain through natural-language notes. It supports Snowflake and BigQuery (with Redshift and Delta Lake via Databricks on the roadmap) and integrates with OpenAI, Anthropic, Gemini, and dbt Cloud. Rasgo also offers a beta HTTP API (Enterprise plans and above) and an official Python SDK, pyrasgo, that grew out of its earlier data feature-engineering product line. Rasgo is backed by Insight Partners.
image: https://assets.website-files.com/6276a6c8de0316128b0a3844/6276a6c8de03160de50a38c5_rasgo-logo-inverted-rgb.svg
layout: provider
modified: '2026-07-20'
name: Rasgo
nav: Providers
network: true
overview: 'Rasgo publishes 1 API on the [APIs.io](https://apis.io/) network: Metadata API. Tagged areas include Company, Data Warehouse, Analytics, Artificial Intelligence, and Natural-Language.


  Rasgo''s developer surface includes documentation, API reference, getting-started guide, signup flow, changelog, authentication, and 12 more developer resources.'
random_paper: 15
score:
  band: thin
  composite: 36.7
  coverage:
    artifact_dirs: 14
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 6.6
    commercial_clarity: 6.6
    contract_governance: 4.5
    contract_quality: 53.7
    developer_ergonomics: 58.9
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 15.8
  previous_composite: 36.7
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/rasgo/refs/heads/main/screenshots/rasgo-2026-09-02T152909.png
security:
- kind: authentication
  name: Rasgo Authentication
  slug: rasgo-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Rasgo Domain Security
  slug: rasgo-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: rasgo
tags:
- Company
- Data Warehouse
- Analytics
- Artificial Intelligence
- Natural-Language
- Snowflake
- BigQuery
- Business Intelligence
- Metadata
- SQL
website: https://www.rasgoml.com/
---
