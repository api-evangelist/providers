---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.0
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: The Maxim REST API provides programmatic access to prompts, workflows, agents, datasets, evaluators, test runs, logging, tracing, models, alerts, and log repositories. It supports OpenTelemetry-compat
  name: Maxim AI API
  slug: maxim-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/maxim-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/maxim-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.getmaxim.ai
- group: docs
  title: ''
  type: Documentation
  url: https://www.getmaxim.ai/docs
- group: company
  title: ''
  type: Blog
  url: https://www.getmaxim.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/maximhq
- group: commercial
  title: ''
  type: Pricing
  url: https://www.getmaxim.ai/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.getmaxim.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.getmaxim.ai/privacy
- group: other
  title: ''
  type: X
  url: https://x.com/getmaximai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/maxim-ai
created: '2026-05-23'
description: Maxim AI is an end-to-end platform for the simulation, evaluation, and observability of AI agents and LLM applications. It provides distributed tracing, 50+ pre-built evaluators, offline and online evaluations, no-code agent and workflow builders, prompt versioning, dataset management, and real-time monitoring dashboards. Maxim targets engineering and quality teams shipping production AI features and is available as cloud-hosted SaaS, hybrid (VPC peering), or self-hosted (zero-touch VPC isolation). The company monetizes through tiered SaaS plans and enterprise licenses.
finops:
- name: Maxim Finops
  service_category: API
  slug: maxim-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/maxim.png
layout: provider
modified: '2026-05-23'
name: Maxim AI
nav: Providers
network: true
overview: 'Maxim AI publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, LLM, Agents, Observability, and Evaluation.


  Maxim AI''s developer surface includes documentation, engineering blog, pricing, and 8 more developer resources.'
plans:
- name: Maxim Plans Pricing
  plan_count: 1
  slug: maxim-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 2
  name: Maxim Rate Limits
  slug: maxim-rate-limits
score:
  band: emerging
  composite: 25.8
  coverage:
    artifact_dirs: 6
    catalog_earned: 56.0
    catalog_earned_first_party: 0.0
    catalog_gap: 59.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 25.8
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/maxim/refs/heads/main/screenshots/maxim-2026-06-20T185048.png
security:
- kind: domain-security
  name: Maxim Domain Security
  slug: maxim-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Maxim Trust Center
  slug: maxim-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: maxim
tags:
- Artificial Intelligence
- LLM
- Agents
- Observability
- Evaluation
- Simulation
- Tracing
- Prompts
- Datasets
- Monitoring
- Voice
- OpenTelemetry
website: https://www.getmaxim.ai
---
