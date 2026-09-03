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
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.0
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 27
  human_in_the_loop: 0
  name: Aito Technologies Agentic Access
  operation_count: 34
  slug: aito-technologies-agentic-access
  summary_line: 34 operations · 27 acting
api_count: 1
apis:
- baseURL: https://shared.aito.ai
  baseurl_source: declared
  description: The data API from Aito Technologies — 7 operation(s) for data.
  name: Aito Technologies data API
  slug: aito-technologies-data-api
- baseURL: https://shared.aito.ai
  baseurl_source: declared
  description: The query API from Aito Technologies — 15 operation(s) for query.
  name: Aito Technologies query API
  slug: aito-technologies-query-api
- baseURL: https://shared.aito.ai
  baseurl_source: declared
  description: The schema API from Aito Technologies — 5 operation(s) for schema.
  name: Aito Technologies schema API
  slug: aito-technologies-schema-api
artifact_total: 10
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Aito Technologies data API
  slug: open-aito-technologies-data-api
- collection_type: open
  name: Aito Technologies data query API
  slug: open-aito-technologies-query-api
- collection_type: open
  name: Aito Technologies data schema API
  slug: open-aito-technologies-schema-api
common:
- group: auth
  title: ''
  type: Authentication
  url: authentication/aito-technologies-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aito-technologies-domain-security.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/aito-technologies-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/aito-technologies-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/aito-technologies-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://aitostatus.statuspage.io
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/aito-technologies-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/aito-technologies-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/aito-technologies-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/aito-technologies-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/aito-technologies-cli.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/aito-technologies-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://aito.ai/trust/security/
- group: auth
  title: ''
  type: TrustCenter
  url: https://aito.ai/trust/
- group: design
  title: ''
  type: DataModel
  url: data-model/aito-technologies-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/aito-technologies-openapi-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/aito-technologies-agentic-access.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/aito-technologies-sandbox.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://aito.releasenotes.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://aito.ai/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://aito.ai/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://aito.ai/docs/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://aito.ai/docs/
- group: operate
  title: ''
  type: Support
  url: https://aito.ai/join-slack/
- group: company
  title: ''
  type: Blog
  url: https://aito.ai/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AitoDotAI
- group: commercial
  title: ''
  type: Pricing
  url: https://aito.ai/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://console.aito.ai/account/authentication/?signUp=true
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aito.ai/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aito.ai/privacy-policy/
- group: company
  title: ''
  type: Website
  url: https://aito.ai
created: '2026-07-17'
description: Aito Technologies (Aito.ai, legal entity Episto Oy of Vantaa, Finland) builds a predictive database that delivers instant, calibrated machine-learning predictions from live business data with no model training. Its REST Query API exposes a SQL-like JSON interface for prediction, recommendation, similarity search, classification, pattern matching, and statistical relation over your own tables, alongside schema and data-management endpoints. Aito powers predictive accounting (GL coding, invoice routing, fraud detection), predictive ERP, and predictive e-commerce, and is delivered as an EU-hosted cloud service (Ireland, eu-west-1) or a self-hosted Docker container. Authentication is an x-api-key header with read-only and read/write key types.
image: https://console.aito.ai/aito-favicon-128.png
layout: provider
modified: '2026-07-17'
name: Aito Technologies
nav: Providers
network: true
overview: 'Aito Technologies publishes 3 APIs on the [APIs.io](https://apis.io/) network: data API, query API, and schema API. Tagged areas include Company, Predictive Database, Machine-Learning, Artificial Intelligence, and Recommendations.


  Aito Technologies'' developer surface includes authentication, CLI, sandbox, changelog, documentation, API reference, getting-started guide, and 25 more developer resources.'
random_paper: 15
score:
  band: developing
  composite: 48.9
  coverage:
    artifact_dirs: 20
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 18.2
    contract_quality: 44.7
    developer_ergonomics: 80.4
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 48.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/aito-technologies/refs/heads/main/screenshots/aito-technologies-2026-07-25T195452.png
security:
- kind: authentication
  name: Aito Technologies Authentication
  slug: aito-technologies-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Aito Technologies Domain Security
  slug: aito-technologies-domain-security
  summary_line: TLSv1.3 · DMARC
slug: aito-technologies
tags:
- Company
- Predictive Database
- Machine-Learning
- Artificial Intelligence
- Recommendations
- Search
- Predictive Analytics
- Automation
- Data
website: https://aito.ai
---
