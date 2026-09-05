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
    error_semantics: verified
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
  score: 23.9
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Mollybox Agentic Access
  operation_count: 8
  slug: mollybox-agentic-access
  summary_line: 8 operations · 4 acting
api_count: 1
apis:
- baseURL: http://www.mollybox.cn
  baseurl_source: declared
  description: The Admin API from MollyBox — 1 operation(s) for admin.
  name: MollyBox Admin API
  slug: mollybox-admin-api
- baseURL: http://www.mollybox.cn
  baseurl_source: declared
  description: The Health API from MollyBox — 1 operation(s) for health.
  name: MollyBox Health API
  slug: mollybox-health-api
- baseURL: http://www.mollybox.cn
  baseurl_source: declared
  description: The Me API from MollyBox — 1 operation(s) for me.
  name: MollyBox Me API
  slug: mollybox-me-api
- baseURL: http://www.mollybox.cn
  baseurl_source: declared
  description: The Resources API from MollyBox — 4 operation(s) for resources.
  name: MollyBox Resources API
  slug: mollybox-resources-api
artifact_total: 12
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Arcflow Admin API
  slug: open-mollybox-admin-api
- collection_type: open
  name: Arcflow Admin Health API
  slug: open-mollybox-health-api
- collection_type: open
  name: Arcflow Admin Me API
  slug: open-mollybox-me-api
- collection_type: open
  name: Arcflow Admin Resources API
  slug: open-mollybox-resources-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/mollybox-arcflow-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/mollybox-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://www.mollybox.cn/
- group: auth
  title: ''
  type: Authentication
  url: authentication/mollybox-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/mollybox-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/mollybox-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/mollybox-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/mollybox-conformance.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/mollybox-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mollybox-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mollybox-domain-security.yml
created: '2026-07-17'
description: MollyBox was added to the API Evangelist network as a consumer-sector portfolio lead of DCM Ventures. The domain mollybox.cn currently serves a live "Arcflow API" (v0.1.0) — a single-user, self-hosted resource-capture service built on FastAPI/uvicorn. It captures URL resources (auto-classified as github, x, wechat, or web), enriches their metadata, and tracks each item through a learning workflow (inbox, next, doing, done, archived), plus health and identity checks. All operations except the public health endpoint require an HTTP Bearer token. This profile reflects the real API discovered at the domain during enrichment.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mollybox.png
layout: provider
modified: '2026-07-20'
name: MollyBox
nav: Providers
network: true
overview: 'MollyBox publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Admin API, Health API, Me API, and 1 more. Tagged areas include Company, Consumer, Bookmarking, Resource Capture, and Read It Later.


  MollyBox''s developer surface includes authentication and 11 more developer resources.'
random_paper: 4
score:
  band: thin
  composite: 27.6
  coverage:
    artifact_dirs: 14
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 53.6
    developer_ergonomics: 30.4
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 27.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
security:
- kind: authentication
  name: Mollybox Authentication
  slug: mollybox-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Mollybox Domain Security
  slug: mollybox-domain-security
  summary_line: no transport/DNS hardening detected
slug: mollybox
tags:
- Company
- Consumer
- Bookmarking
- Resource Capture
- Read It Later
- FastAPI
- Self-Hosted
website: https://www.mollybox.cn/
---
