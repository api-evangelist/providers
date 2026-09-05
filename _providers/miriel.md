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
    error_semantics: false
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
  score: 18.2
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 21
  human_in_the_loop: 0
  name: Miriel Agentic Access
  operation_count: 21
  slug: miriel-agentic-access
  summary_line: 21 operations · 21 acting
api_count: 7
apis:
- baseURL: https://api.prod.miriel.ai
  baseurl_source: declared
  description: The Documents API from Miriel — 8 operation(s) for documents.
  name: Miriel Documents API
  slug: miriel-documents-api
- baseURL: https://api.prod.miriel.ai
  baseurl_source: declared
  description: The Learn API from Miriel — 1 operation(s) for learn.
  name: Miriel Learn API
  slug: miriel-learn-api
- baseURL: https://api.prod.miriel.ai
  baseurl_source: declared
  description: The Monitoring API from Miriel — 2 operation(s) for monitoring.
  name: Miriel Monitoring API
  slug: miriel-monitoring-api
- baseURL: https://api.prod.miriel.ai
  baseurl_source: declared
  description: The Policies API from Miriel — 3 operation(s) for policies.
  name: Miriel Policies API
  slug: miriel-policies-api
- baseURL: https://api.prod.miriel.ai
  baseurl_source: declared
  description: The Projects API from Miriel — 3 operation(s) for projects.
  name: Miriel Projects API
  slug: miriel-projects-api
- baseURL: https://api.prod.miriel.ai
  baseurl_source: declared
  description: The Query API from Miriel — 1 operation(s) for query.
  name: Miriel Query API
  slug: miriel-query-api
- baseURL: https://api.prod.miriel.ai
  baseurl_source: declared
  description: The Users API from Miriel — 3 operation(s) for users.
  name: Miriel Users API
  slug: miriel-users-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Miriel Context Engine Documents API
  slug: open-miriel-documents-api
- collection_type: open
  name: Miriel Context Engine Documents Learn API
  slug: open-miriel-learn-api
- collection_type: open
  name: Miriel Context Engine Documents Monitoring API
  slug: open-miriel-monitoring-api
- collection_type: open
  name: Miriel Context Engine Documents Policies API
  slug: open-miriel-policies-api
- collection_type: open
  name: Miriel Context Engine Documents Projects API
  slug: open-miriel-projects-api
- collection_type: open
  name: Miriel Context Engine Documents Query API
  slug: open-miriel-query-api
- collection_type: open
  name: Miriel Context Engine Documents Users API
  slug: open-miriel-users-api
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://miriel.ai/docs
- group: docs
  title: ''
  type: Documentation
  url: https://miriel.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://miriel.ai/docs
- group: company
  title: ''
  type: Blog
  url: https://miriel.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/miriel-ai
- group: start
  title: ''
  type: SignUp
  url: https://app.miriel.ai
- group: start
  title: ''
  type: Login
  url: https://app.miriel.ai
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/miriel-llms.txt
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/miriel-openapi.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/miriel-overlay.yaml
- group: auth
  title: ''
  type: Authentication
  url: authentication/miriel-authentication.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/miriel-agentic-access.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/miriel-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/miriel-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/miriel-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/miriel-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/miriel-packages.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/miriel-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/miriel-well-known.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/miriel-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.miriel.ai
- group: auth
  title: ''
  type: DomainSecurity
  url: security/miriel-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://miriel.ai
created: '2026-07-17'
description: 'Miriel is the context engine and platform for AI-native development. It gives AI apps and agents the context they need in real time through a simple API: developers connect a data source with the learn operation and retrieve relevant context with the query operation, backed by LLM, vector, and knowledge-graph retrieval. Every interaction is encrypted and permissions are managed at the token level (per-user grants and policies). Built by a team with backgrounds across Google, Tesla, Facebook, and Posit, Miriel handles intelligent indexing and retrieval tailored to each source, plus Labs projects (Nora, Floodlight) and tools like Autodev and NexusBuild. Backed by Foundry Group.'
image: https://miriel.ai/MirielLogoWhiteNoTextOnBlue.svg
layout: provider
modified: '2026-07-20'
name: Miriel
nav: Providers
network: true
overview: 'Miriel publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Documents API, Learn API, Monitoring API, and 4 more. Tagged areas include Company, Artificial Intelligence, Context Engine, Retrieval, and RAG.


  Miriel''s developer surface includes documentation, API reference, engineering blog, signup flow, authentication, and 19 more developer resources.'
random_paper: 12
score:
  band: emerging
  composite: 24.8
  coverage:
    artifact_dirs: 17
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 4.5
    contract_quality: 12.9
    developer_ergonomics: 49.4
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 24.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 8
      marker_coverage: 100.0
      total: 8
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/miriel/refs/heads/main/screenshots/miriel-2026-08-07T183723.png
security:
- kind: authentication
  name: Miriel Authentication
  slug: miriel-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Miriel Domain Security
  slug: miriel-domain-security
  summary_line: TLSv1.3 · DMARC
slug: miriel
tags:
- Company
- Artificial Intelligence
- Context Engine
- Retrieval
- RAG
- Knowledge Graph
- Vector Search
- Agents
- LLM
- Developer Tools
website: https://miriel.ai
---
