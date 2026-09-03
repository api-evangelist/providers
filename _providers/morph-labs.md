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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Morph Labs Agentic Access
  operation_count: 3
  slug: morph-labs-agentic-access
  summary_line: 3 operations · 3 acting
api_count: 1
apis:
- description: Infinibranch microVM (Firecracker) sandbox infrastructure for agents - a user-scoped API for managing instances and snapshots with sub-250ms branch, snapshot, and restore, command exec (including SSE)
  name: Morph Cloud Sandboxes API
  slug: morph-cloud-sandboxes-api
- baseURL: https://api.morphllm.com/v1
  baseurl_source: declared
  description: The Apply API from Morph — 1 operation(s) for apply.
  name: Morph Apply API
  slug: morph-labs-apply-api
- baseURL: https://api.morphllm.com/v1
  baseurl_source: declared
  description: The Embeddings API from Morph — 1 operation(s) for embeddings.
  name: Morph Embeddings API
  slug: morph-labs-embeddings-api
- baseURL: https://api.morphllm.com/v1
  baseurl_source: declared
  description: The Rerank API from Morph — 1 operation(s) for rerank.
  name: Morph Rerank API
  slug: morph-labs-rerank-api
artifact_total: 15
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Morph Apply API
  slug: open-morph-labs-apply-api
- collection_type: open
  name: Morph Apply Embeddings API
  slug: open-morph-labs-embeddings-api
- collection_type: open
  name: Morph Apply Rerank API
  slug: open-morph-labs-rerank-api
- collection_type: open
  name: Morph API
  slug: open-morph-labs
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/morph-labs-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/morph-labs-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/morph-labs-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/morphllm
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/morph-labs
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/morph-labs
- group: company
  title: ''
  type: Website
  url: https://morphllm.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.morphllm.com
- group: commercial
  title: ''
  type: Plans
  url: plans/morph-labs-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/morph-labs-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/morph-labs-finops.yml
created: '2026-06-20'
description: Morph builds fast models that improve AI coding agents. Its OpenAI-compatible API serves the Apply (Fast Apply) model that deterministically merges LLM-generated code edits into source files at 10,500+ tokens/second, plus code embeddings and reranking. Morph Cloud adds Infinibranch microVM sandboxes that snapshot, branch, and restore entire VM states in under 250ms for agent workloads.
finops:
- name: Morph Labs Finops
  service_category: AI and Machine Learning
  slug: morph-labs-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/morph-labs.png
layout: provider
modified: '2026-06-20'
name: Morph
nav: Providers
network: true
overview: 'Morph publishes 3 APIs on the [APIs.io](https://apis.io/) network: Apply API, Embeddings API, and Rerank API. Tagged areas include Artificial Intelligence, Code Editing, Fast Apply, Embeddings, and Sandboxes.


  Morph''s developer surface includes authentication, documentation, and 9 more developer resources.'
plans:
- name: Morph Labs Plans Pricing
  plan_count: 6
  slug: morph-labs-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 4
  name: Morph Labs Rate Limits
  slug: morph-labs-rate-limits
score:
  band: thin
  composite: 39.1
  coverage:
    artifact_dirs: 9
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 53.1
    developer_ergonomics: 33.3
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 39.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/morph-labs/refs/heads/main/screenshots/morph-labs-2026-06-20T185812.png
security:
- kind: authentication
  name: Morph Labs Authentication
  slug: morph-labs-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Morph Labs Domain Security
  slug: morph-labs-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: morph-labs
tags:
- Artificial Intelligence
- Code Editing
- Fast Apply
- Embeddings
- Sandboxes
website: https://morphllm.com/
---
