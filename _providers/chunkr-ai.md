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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.0
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Chunkr Ai Agentic Access
  operation_count: 16
  slug: chunkr-ai-agentic-access
  summary_line: 16 operations · 6 acting
api_count: 1
apis:
- baseURL: https://api.chunkr.ai
  baseurl_source: declared
  description: Upload and manage files referenced by tasks.
  name: Chunkr Files API
  slug: chunkr-ai-files-api
- baseURL: https://api.chunkr.ai
  baseurl_source: declared
  description: Liveness and metadata utilities.
  name: Chunkr Health API
  slug: chunkr-ai-health-api
- baseURL: https://api.chunkr.ai
  baseurl_source: declared
  description: Create, poll, list, cancel, and delete parse and extract tasks.
  name: Chunkr Tasks API
  slug: chunkr-ai-tasks-api
artifact_total: 15
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Chunkr Files API
  slug: open-chunkr-ai-files-api
- collection_type: open
  name: Chunkr Files Health API
  slug: open-chunkr-ai-health-api
- collection_type: open
  name: Chunkr Files Tasks API
  slug: open-chunkr-ai-tasks-api
- collection_type: open
  name: Chunkr API
  slug: open-chunkr-ai
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/chunkr-ai-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/chunkr-ai-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/chunkr-ai-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/chunkr-ai-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/lumina-ai-inc
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/chunkr
- group: company
  title: ''
  type: Website
  url: https://chunkr.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.chunkr.ai
- group: commercial
  title: ''
  type: Plans
  url: plans/chunkr-ai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/chunkr-ai-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/chunkr-ai-finops.yml
created: '2026-06-20'
description: Chunkr is an open-source document intelligence platform that turns complex documents (PDF, Office, images) into RAG- and LLM-ready data. The Chunkr Cloud API at api.chunkr.ai performs layout analysis, OCR, segmentation, and chunking, and runs proprietary in-house vision models; the AGPL-3.0 open-source release (lumina-ai-inc/chunkr) can be self-hosted via Docker.
finops:
- name: Chunkr Ai Finops
  service_category: AI and Machine Learning
  slug: chunkr-ai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/chunkr-ai.png
layout: provider
modified: '2026-06-20'
name: Chunkr
nav: Providers
network: true
overview: 'Chunkr publishes 3 APIs on the [APIs.io](https://apis.io/) network: Files API, Health API, and Tasks API. Tagged areas include Document Parsing, OCR, Chunking, RAG, and Document Intelligence.


  Chunkr''s developer surface includes authentication, documentation, and 9 more developer resources.'
plans:
- name: Chunkr Ai Plans Pricing
  plan_count: 6
  slug: chunkr-ai-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 4
  name: Chunkr Ai Rate Limits
  slug: chunkr-ai-rate-limits
score:
  band: developing
  composite: 40.2
  coverage:
    artifact_dirs: 9
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 51.0
    developer_ergonomics: 33.3
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 40.2
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
screenshot: https://raw.githubusercontent.com/api-evangelist/chunkr-ai/refs/heads/main/screenshots/chunkr-ai-2026-06-20T174340.png
security:
- kind: authentication
  name: Chunkr Ai Authentication
  slug: chunkr-ai-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Chunkr Ai Domain Security
  slug: chunkr-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Chunkr Ai Trust Center
  slug: chunkr-ai-trust-center
  summary_line: SOC 2, HIPAA
slug: chunkr-ai
tags:
- Document Parsing
- OCR
- Chunking
- RAG
- Document Intelligence
website: https://chunkr.ai
---
