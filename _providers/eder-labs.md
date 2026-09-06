---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.9
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Eder Labs Agentic Access
  operation_count: 7
  slug: eder-labs-agentic-access
  summary_line: 7 operations · 6 acting
api_count: 1
apis:
- baseURL: http://localhost:8000/api/v1
  baseurl_source: declared
  description: Getting content into a user's memory
  name: Eder Labs Ingestion API
  slug: eder-labs-ingestion-api
- baseURL: http://localhost:8000/api/v1
  baseurl_source: declared
  description: Service metadata
  name: Eder Labs Meta API
  slug: eder-labs-meta-api
- baseURL: http://localhost:8000/api/v1
  baseurl_source: declared
  description: Retrieving memory via RAG and structured insights
  name: Eder Labs Query API
  slug: eder-labs-query-api
- baseURL: http://localhost:8000/api/v1
  baseurl_source: declared
  description: User (memory namespace) lifecycle
  name: Eder Labs Users API
  slug: eder-labs-users-api
artifact_total: 11
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Persona Ingestion API
  slug: open-eder-labs-ingestion-api
- collection_type: open
  name: Persona Ingestion Meta API
  slug: open-eder-labs-meta-api
- collection_type: open
  name: Persona Ingestion Query API
  slug: open-eder-labs-query-api
- collection_type: open
  name: Persona Ingestion Users API
  slug: open-eder-labs-users-api
common:
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/eder-labs-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/eder-labs-persona-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.eder.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.buildpersona.ai/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.buildpersona.ai/quickstart
- group: build
  title: ''
  type: GitHub
  url: https://github.com/saxenauts/persona
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/eder-labs-llms.txt
- group: operate
  title: ''
  type: Support
  url: https://github.com/saxenauts/persona/issues
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.eder.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.eder.io/privacy
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/eder-labs-domain-security.yml
created: '2026-07-17'
description: Eder Labs builds infrastructure for using personal data in safer, more human ways. Its current focus is Persona, an open-source (MIT) user-memory system for AI agents that turns a person's digital footprint into a Graph-Vector hybrid personal knowledge graph (Neo4j graph plus vector embeddings) and answers natural-language RAG queries or returns structured insights over that memory. Eder Labs also develops Fluid, a platform for exchanging sensitive intelligence and running data science inside secure enclaves without compromising trust. Persona ships as a self-hosted FastAPI service with a small REST API for creating users, ingesting content, and querying memory. Eder Labs is backed by Accel.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/eder-labs.png
layout: provider
modified: '2026-07-19'
name: Eder Labs
nav: Providers
network: true
overview: 'Eder Labs publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Ingestion API, Meta API, Query API, and 1 more. Tagged areas include Company, Cloud Saas, AI Agents, Memory, and Knowledge Graph.


  Eder Labs'' developer surface includes documentation, getting-started guide, GitHub presence, support, and 8 more developer resources.'
random_paper: 18
score:
  band: thin
  composite: 31.0
  coverage:
    artifact_dirs: 16
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 47.4
    developer_ergonomics: 35.1
    discoverability: 66.7
    governance: 4.5
    operational_transparency: 5.3
  previous_composite: 31.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 100.0
      total: 4
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/eder-labs/refs/heads/main/screenshots/eder-labs-2026-07-25T212819.png
security:
- kind: domain-security
  name: Eder Labs Domain Security
  slug: eder-labs-domain-security
  summary_line: TLSv1.3 · HSTS
slug: eder-labs
tags:
- Company
- Cloud Saas
- AI Agents
- Memory
- Knowledge Graph
- Personalization
- Data Privacy
- Open-Source
- Developer Tools
- RAG
website: https://www.eder.io/
---
