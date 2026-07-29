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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Refuel Ai Agentic Access
  operation_count: 1
  slug: refuel-ai-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 2
apis:
- description: Autolabel is the open-source Python library (pip install refuel-autolabel) to label, clean, and enrich text datasets with any LLM (OpenAI, Anthropic, Google, HuggingFace, vLLM, Refuel-hosted). It is a
  name: Refuel Autolabel (Open Source)
  slug: refuel-autolabel-oss
- description: The Applications API from Refuel — 1 operation(s) for applications.
  name: Refuel Applications API
  slug: refuel-ai-applications-api
artifact_total: 11
collections:
- collection_type: open
  name: Refuel Cloud API
  slug: open-refuel-ai
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/refuel-ai-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/refuel-ai-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/refuel-ai-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/refuel-ai-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/refuel-ai-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/refuel-ai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/refuel-ai
- group: company
  title: ''
  type: Website
  url: https://www.refuel.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.refuel.ai
- group: commercial
  title: ''
  type: Plans
  url: plans/refuel-ai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/refuel-ai-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/refuel-ai-finops.yml
created: '2026-06-21'
description: Refuel is an AI data-labeling and data-enrichment platform that uses LLMs to label, clean, structure, and enrich enterprise datasets. Refuel Cloud exposes a REST API where datasets, tasks, and deployed applications transform new data in realtime, and the open-source autolabel library lets teams run the same LLM labeling workflows in their own environment.
finops:
- name: Refuel Ai Finops
  service_category: AI and Machine Learning
  slug: refuel-ai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/refuel-ai.png
layout: provider
modified: '2026-06-21'
name: Refuel
nav: Providers
network: true
overview: 'Refuel publishes 1 API on the [APIs.io](https://apis.io/) network: Applications API. Tagged areas include AI, LLM, Data Labeling, Data Enrichment, and Autolabel.


  Refuel''s developer surface includes authentication, documentation, and 10 more developer resources.'
plans:
- name: Refuel Ai Plans Pricing
  plan_count: 3
  slug: refuel-ai-plans-pricing
random_paper: 80
rate_limits:
- limit_count: 2
  name: Refuel Ai Rate Limits
  slug: refuel-ai-rate-limits
score:
  band: thin
  composite: 39.6
  delta: -1.9
  facets:
    commercial_clarity: 47.4
    contract_quality: 63.6
    developer_ergonomics: 19.6
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 41.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Refuel Ai Authentication
  slug: refuel-ai-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Refuel Ai Domain Security
  slug: refuel-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Refuel Ai Vulnerability Disclosure
  slug: refuel-ai-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Refuel Ai Trust Center
  slug: refuel-ai-trust-center
  summary_line: SOC 2, GDPR
slug: refuel-ai
tags:
- AI
- LLM
- Data Labeling
- Data Enrichment
- Autolabel
website: https://www.refuel.ai
---
