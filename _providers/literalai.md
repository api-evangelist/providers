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
    openapi_examples: verified
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Literalai Agentic Access
  operation_count: 1
  slug: literalai-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- baseURL: https://cloud.getliteral.ai/api/graphql
  baseurl_source: declared
  description: The Graph QL API from Literal AI — 1 operation(s) for graph ql.
  name: Literal AI Graph QL API
  slug: literalai-graph-ql-api
artifact_total: 11
collections:
- collection_type: open
  name: Literal AI GraphQL API
  slug: open-literalai-graphql-api
- collection_type: open
  name: Literal AI API
  slug: open-literalai
common:
- group: agent
  href: https://artifacts.apis.io/literalai/agentic-access/literalai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/literalai-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/literalai/security/literalai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/literalai-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/literalai/authentication/literalai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/literalai-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Chainlit
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/chainlit
- group: company
  title: ''
  type: Website
  url: https://www.literalai.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.literalai.com
- group: commercial
  href: https://artifacts.apis.io/literalai/plans/literalai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/literalai-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/literalai/rate-limits/literalai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/literalai-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/literalai/finops/literalai-finops.yml
  title: ''
  type: FinOps
  url: finops/literalai-finops.yml
created: '2026-06-20'
description: Literal AI is the collaborative observability, evaluation, and analytics platform for building production-grade LLM applications, from the Chainlit team. Its API is GraphQL (POST /api/graphql) consumed through Python and TypeScript SDKs, capturing threads, steps, generations, datasets, experiments, prompts, and scores, with an additional OpenTelemetry (OTLP) ingestion path for traces.
finops:
- has_sources: true
  method: generated
  name: Literalai Finops
  primary_unit: ''
  service_category: AI and Machine Learning
  slug: literalai-finops
  template: false
graphqls:
- description: Representative GraphQL schema for the [Literal AI](https://www.literalai.com/) LLM
  name: Literal AI GraphQL API
  slug: literalai-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/literalai.png
layout: provider
modified: '2026-06-20'
name: Literal AI
nav: Providers
network: true
overview: 'Literal AI publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Graph QL API. Tagged areas include Artificial Intelligence, LLM, Observability, Evaluation, and Monitoring.


  The Literal AI catalog on APIs.io includes 1 Spectral governance ruleset.


  Literal AI''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Literalai Plans Pricing
  plan_count: 3
  slug: literalai-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 5
  name: Literalai Rate Limits
  slug: literalai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 91
  extends:
  - spectral:oas
  name: Literal AI API Rules
  rule_count: 50
  severity_counts:
    error: 48
    hint: 0
    info: 1
    warn: 1
  slug: literalai-rules
score:
  band: thin
  composite: 28.7
  coverage:
    artifact_dirs: 15
    catalog_earned: 47.5
    catalog_earned_first_party: 0.0
    catalog_gap: 67.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 7.9
    contract_governance: 13.6
    contract_quality: 52.7
    developer_ergonomics: 28.6
    discoverability: 66.1
    operational_transparency: 10.5
  previous_composite: 28.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/literalai/literalai-2026-06-20T184606.png
security:
- kind: authentication
  name: Literalai Authentication
  slug: literalai-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Literalai Domain Security
  slug: literalai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: literalai
tags:
- Artificial Intelligence
- LLM
- Observability
- Evaluation
- Monitoring
website: https://www.literalai.com
---
