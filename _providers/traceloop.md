---
access_model:
  confidence: medium
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.8
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 41
  human_in_the_loop: 0
  name: Traceloop Agentic Access
  operation_count: 44
  slug: traceloop-agentic-access
  summary_line: 44 operations · 41 acting
api_count: 1
apis:
- baseURL: https://api.traceloop.com
  baseurl_source: declared
  description: The auto-monitor-setups API from Traceloop — 2 operation(s) for auto-monitor-setups.
  name: Traceloop auto-monitor-setups API
  slug: traceloop-auto-monitor-setups-api
- baseURL: https://api.traceloop.com
  baseurl_source: declared
  description: The evaluators API from Traceloop — 36 operation(s) for evaluators.
  name: Traceloop evaluators API
  slug: traceloop-evaluators-api
- baseURL: https://api.traceloop.com
  baseurl_source: declared
  description: The metrics API from Traceloop — 2 operation(s) for metrics.
  name: Traceloop metrics API
  slug: traceloop-metrics-api
- baseURL: https://api.traceloop.com
  baseurl_source: declared
  description: The organizations API from Traceloop — 1 operation(s) for organizations.
  name: Traceloop organizations API
  slug: traceloop-organizations-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Traceloop auto-monitor-setups API
  slug: open-traceloop-auto-monitor-setups-api
- collection_type: open
  name: Traceloop auto-monitor-setups evaluators API
  slug: open-traceloop-evaluators-api
- collection_type: open
  name: Traceloop auto-monitor-setups metrics API
  slug: open-traceloop-metrics-api
- collection_type: open
  name: Traceloop auto-monitor-setups organizations API
  slug: open-traceloop-organizations-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/traceloop-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/traceloop-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/traceloop-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.traceloop.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.traceloop.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/traceloop
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/traceloop
- group: company
  title: ''
  type: Blog
  url: https://www.traceloop.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.traceloop.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.traceloop.com/
- group: other
  title: ''
  type: X
  url: https://twitter.com/traceloopdev
- group: commercial
  title: ''
  type: Plans
  url: plans/traceloop-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/traceloop-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/traceloop-finops.yml
created: 2026-06-13
description: Traceloop is an LLM reliability and observability platform built on OpenTelemetry that provides full visibility into every prompt, response, and failure across AI pipelines. The platform enables teams to monitor LLM quality in production, detect model drift and hallucinations, run automated evaluations via LLM-as-a-judge, and enforce quality gates in CI/CD workflows. Traceloop exposes a REST API for managing auto-monitor setups, running 40+ built-in evaluators (safety, faithfulness, PII, toxicity, structural validation), querying metrics and span warehouse data, and administering organizations and environments. The open-source OpenLLMetry SDK integrates in one line of code across Python, TypeScript, Go, and Ruby with support for 20+ LLM providers and major orchestration frameworks.
finops:
- name: Traceloop Finops
  service_category: ''
  slug: traceloop-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/traceloop.png
json_schemas:
- name: Traceloop API Schemas
  property_count: 0
  slug: traceloop
jsonld:
- class_count: 36
  name: Traceloop Context
  property_count: 37
  slug: traceloop-context
layout: provider
modified: 2026-06-13
name: Traceloop
nav: Providers
network: true
overview: 'Traceloop publishes 4 APIs on the [APIs.io](https://apis.io/) network, including auto-monitor-setups API, evaluators API, metrics API, and 1 more. Tagged areas include LLM Observability, OpenTelemetry, AI Monitoring, Tracing, and Evaluation.


  The Traceloop catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Traceloop''s developer surface includes authentication, documentation, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Traceloop Plans Pricing
  plan_count: 2
  slug: traceloop-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 5
  name: Traceloop Rate Limits
  slug: traceloop-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Traceloop API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: traceloop-jsonschema-spectral-rules
score:
  band: developing
  composite: 43.9
  coverage:
    artifact_dirs: 15
    catalog_earned: 85.3
    catalog_earned_first_party: 0.0
    catalog_gap: 29.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 25.0
    contract_quality: 66.3
    developer_ergonomics: 23.8
    discoverability: 68.5
    governance: 25.0
    operational_transparency: 36.8
  previous_composite: 43.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/traceloop/refs/heads/main/screenshots/traceloop-2026-06-20T195517.png
security:
- kind: authentication
  name: Traceloop Authentication
  slug: traceloop-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Traceloop Domain Security
  slug: traceloop-domain-security
  summary_line: TLSv1.3 · DMARC
slug: traceloop
tags:
- LLM Observability
- OpenTelemetry
- AI Monitoring
- Tracing
- Evaluation
- LLM Gateway
- Prompt Management
- Machine-Learning
website: https://www.traceloop.com/
---
