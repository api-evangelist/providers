---
access_model:
  confidence: medium
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
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
    mcp_server: verified
    openapi_examples: documented
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.3
  scored_at: '2026-09-25'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Tonic Ai Agentic Access
  operation_count: 4
  slug: tonic-ai-agentic-access
  summary_line: 4 operations · 1 acting
api_count: 1
apis:
- description: REST API for Tonic Structural - de-identify, subset, and synthesize structured and semi-structured data. Authentication via API token in the Authorization header (Authorization Apikey <token>). API to
  name: Tonic Structural REST API
  slug: structural-api
- description: REST API for Tonic Textual - de-identify, redact, and synthesize unstructured data, free-text, and files. Authentication via API key in the Authorization header. Backed by a Python SDK (tonic-textual)
  name: Tonic Textual REST API
  slug: textual-api
- description: Tonic Validate is an open-source RAG evaluation framework and metrics platform for measuring retrieval-augmented generation quality. Used via a Python SDK that reports runs to the Tonic Validate web U
  name: Tonic Validate
  slug: validate
- description: Tonic Fabricate generates synthetic relational data, free-text, and mockable APIs from a schema definition. Used through the Fabricate web app and project APIs.
  name: Tonic Fabricate
  slug: fabricate
- baseURL: https://app.tonic.ai
  baseurl_source: declared
  description: The Generate Data API from Tonic.ai — 2 operation(s) for generate data.
  name: Tonic.ai Generate Data API
  slug: tonic-ai-generate-data-api
- baseURL: https://app.tonic.ai
  baseurl_source: declared
  description: The Table Relationships API from Tonic.ai — 1 operation(s) for table relationships.
  name: Tonic.ai Table Relationships API
  slug: tonic-ai-table-relationships-api
- baseURL: https://app.tonic.ai
  baseurl_source: declared
  description: The Workspaces API from Tonic.ai — 1 operation(s) for workspaces.
  name: Tonic.ai Workspaces API
  slug: tonic-ai-workspaces-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Tonic Structural REST Generate Data API
  slug: open-tonic-ai-generate-data-api
- collection_type: open
  name: Tonic Structural REST Generate Data Table Relationships API
  slug: open-tonic-ai-table-relationships-api
- collection_type: open
  name: Tonic Structural REST Generate Data Workspaces API
  slug: open-tonic-ai-workspaces-api
- collection_type: open
  name: Tonic Structural REST API
  slug: open-tonic-ai
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/TonicAI/tonic_validate/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/TonicAI/tonic_validate/releases
- group: commercial
  title: ''
  type: License
  url: https://github.com/TonicAI/tonic_validate/blob/main/LICENSE
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/tonic-ai/refs/heads/main/agentic-access/tonic-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/tonic-ai-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/tonic-ai/refs/heads/main/security/tonic-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tonic-ai-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/tonic-ai/refs/heads/main/authentication/tonic-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/tonic-ai-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.tonic.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tonic.ai/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/TonicAI
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tonicfakedata
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/tonic-ai/refs/heads/main/plans/tonic-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/tonic-ai-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/tonic-ai/refs/heads/main/rate-limits/tonic-ai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/tonic-ai-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/tonic-ai/refs/heads/main/finops/tonic-ai-finops.yml
  title: ''
  type: FinOps
  url: finops/tonic-ai-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.tonic.ai/llms.txt
created: '2026-05-23'
description: Tonic.ai builds developer-data products for de-identifying, subsetting, and synthesizing data for AI and software teams. The portfolio includes Tonic Structural (structured/semi-structured data), Tonic Textual (unstructured free-text and files), Tonic Validate (RAG evaluation), and Tonic Fabricate (relational synthetic data and mock APIs). Each product ships its own REST API and SDKs.
finops:
- name: Tonic Ai Finops
  service_category: API
  slug: tonic-ai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tonic-ai.png
layout: provider
modified: '2026-05-23'
name: Tonic.ai
nav: Providers
network: true
overview: 'Tonic.ai publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Generate Data API, Table Relationships API, Workspaces API, and 4 more. Tagged areas include Synthetic Data, De-Identification, Privacy, Unstructured Data, and RAG Evaluation.


  Tonic.ai''s developer surface includes authentication, documentation, GitHub presence, and 11 more developer resources.'
plans:
- name: Tonic Ai Plans Pricing
  plan_count: 1
  slug: tonic-ai-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 2
  name: Tonic Ai Rate Limits
  slug: tonic-ai-rate-limits
score:
  band: thin
  composite: 34.2
  coverage:
    artifact_dirs: 13
    catalog_earned: 54.4
    catalog_earned_first_party: 0.0
    catalog_gap: 60.6
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.3
  facets:
    access_clarity: 26.8
    contract_governance: 0.0
    contract_quality: 45.6
    developer_ergonomics: 35.7
    discoverability: 75.0
    operational_transparency: 40.0
  open_source:
    applies: true
    score: 25.0
  previous_composite: 36.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/tonic-ai/refs/heads/main/screenshots/tonic-ai-2026-06-20T195451.png
security:
- kind: authentication
  name: Tonic Ai Authentication
  slug: tonic-ai-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Tonic Ai Domain Security
  slug: tonic-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tonic-ai
tags:
- Synthetic Data
- De-Identification
- Privacy
- Unstructured Data
- RAG Evaluation
- REST
- SDK
- Developer Tools
website: https://www.tonic.ai/
---
