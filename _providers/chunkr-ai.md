---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.3
  scored_at: '2026-11-06'
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
- baseURL: https://api.chunkr.ai
  baseurl_source: declared
  description: The Chunkr API API from Chunkr — 0 operation(s) for chunkr api.
  name: Chunkr Chunkr API
  slug: chunkr-ai-chunkr-api-api
- baseURL: https://api.chunkr.ai
  baseurl_source: declared
  description: The Extras API from Chunkr — 1 operation(s) for extras.
  name: Chunkr Extras API
  slug: chunkr-ai-extras-api
- baseURL: https://api.chunkr.ai
  baseurl_source: declared
  description: Endpoints for managing webhooks
  name: Chunkr Webhook API
  slug: chunkr-ai-webhook-api
artifact_total: 18
collections:
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
- group: company
  title: ''
  type: BlogRSS
  url: https://chunkr.ai/rss.xml
- group: agent
  href: https://artifacts.apis.io/chunkr-ai/agentic-access/chunkr-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/chunkr-ai-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/chunkr-ai/security/chunkr-ai-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/chunkr-ai-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/chunkr-ai/security/chunkr-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/chunkr-ai-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/chunkr-ai/authentication/chunkr-ai-authentication.yml
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
  href: https://artifacts.apis.io/chunkr-ai/plans/chunkr-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/chunkr-ai-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/chunkr-ai/rate-limits/chunkr-ai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/chunkr-ai-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/chunkr-ai/finops/chunkr-ai-finops.yml
  title: ''
  type: FinOps
  url: finops/chunkr-ai-finops.yml
created: '2026-06-20'
description: Chunkr is an open-source document intelligence platform that turns complex documents (PDF, Office, images) into RAG- and LLM-ready data. The Chunkr Cloud API at api.chunkr.ai performs layout analysis, OCR, segmentation, and chunking, and runs proprietary in-house vision models; the AGPL-3.0 open-source release (lumina-ai-inc/chunkr) can be self-hosted via Docker.
finops:
- has_sources: true
  method: generated
  name: Chunkr Ai Finops
  primary_unit: ''
  service_category: AI and Machine Learning
  slug: chunkr-ai-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/chunkr-ai.png
layout: provider
modified: '2026-10-06'
name: Chunkr
nav: Providers
network: true
overview: 'Chunkr publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Files API, Health API, Tasks API, and 3 more. Tagged areas include Document Parsing, OCR, Chunking, RAG, and Document Intelligence.


  The Chunkr catalog on APIs.io includes 1 Spectral governance ruleset.


  Chunkr''s developer surface includes authentication, documentation, and 10 more developer resources.'
plans:
- name: Chunkr Ai Plans Pricing
  plan_count: 6
  slug: chunkr-ai-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 4
  name: Chunkr Ai Rate Limits
  slug: chunkr-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 112
  extends:
  - spectral:oas
  name: Chunkr API Rules
  rule_count: 71
  severity_counts:
    error: 62
    hint: 0
    info: 6
    warn: 3
  slug: chunkr-ai-rules
score:
  band: thin
  composite: 31.6
  coverage:
    artifact_dirs: 15
    catalog_earned: 47.5
    catalog_earned_first_party: 0.0
    catalog_gap: 67.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.7
  facets:
    access_clarity: 15.8
    contract_governance: 13.6
    contract_quality: 53.3
    developer_ergonomics: 29.8
    discoverability: 66.1
    operational_transparency: 10.5
  previous_composite: 30.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 50.0
      total: 10
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/chunkr-ai/chunkr-ai-2026-06-20T174340.png
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
