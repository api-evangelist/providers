---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  - sandbox
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
  schema_version: '0.2'
  score: 21.0
  scored_at: '2026-09-23'
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
  href: https://raw.githubusercontent.com/api-evangelist/aito-technologies/refs/heads/main/authentication/aito-technologies-authentication.yml
  title: ''
  type: Authentication
  url: authentication/aito-technologies-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aito-technologies/refs/heads/main/security/aito-technologies-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aito-technologies-domain-security.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aito-technologies/refs/heads/main/conventions/aito-technologies-conventions.yml
  title: ''
  type: Conventions
  url: conventions/aito-technologies-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aito-technologies/refs/heads/main/errors/aito-technologies-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/aito-technologies-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aito-technologies/refs/heads/main/lifecycle/aito-technologies-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/aito-technologies-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://aitostatus.statuspage.io
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aito-technologies/refs/heads/main/mcp/aito-technologies-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/aito-technologies-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aito-technologies/refs/heads/main/llms/aito-technologies-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aito-technologies-llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/aito-technologies/refs/heads/main/packages/aito-technologies-packages.yml
  title: ''
  type: Packages
  url: packages/aito-technologies-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/aito-technologies/refs/heads/main/packages/aito-technologies-packages.yml
  title: ''
  type: SDKs
  url: packages/aito-technologies-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/aito-technologies/refs/heads/main/cli/aito-technologies-cli.yml
  title: ''
  type: CLI
  url: cli/aito-technologies-cli.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aito-technologies/refs/heads/main/conformance/aito-technologies-conformance.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/aito-technologies/refs/heads/main/data-model/aito-technologies-data-model.yml
  title: ''
  type: DataModel
  url: data-model/aito-technologies-data-model.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aito-technologies/refs/heads/main/overlays/aito-technologies-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/aito-technologies-openapi-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aito-technologies/refs/heads/main/agentic-access/aito-technologies-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/aito-technologies-agentic-access.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aito-technologies/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/aito-technologies/refs/heads/main/sandbox/aito-technologies-sandbox.yml
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
random_paper: 20
score:
  band: developing
  composite: 49.4
  coverage:
    artifact_dirs: 21
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 47.4
    contract_governance: 18.2
    contract_quality: 45.1
    developer_ergonomics: 80.4
    discoverability: 75.9
    operational_transparency: 18.4
  previous_composite: 49.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-23'
  trend: flat
  upsert:
    applies: true
    score: 11.1
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
