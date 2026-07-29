---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-aware
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
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Deepchecks Agentic Access
  operation_count: 12
  slug: deepchecks-agentic-access
  summary_line: 12 operations · 7 acting
api_count: 7
apis:
- description: The AGPL-3.0 licensed open-source Python package for continuous validation of tabular, computer-vision, and LLM/NLP data and models. Distributed via PyPI (pip install deepchecks); a Python library rat
  name: Deepchecks Open-Source Testing
  slug: open-source-testing
- description: Versions of an evaluation application.
  name: Deepchecks Application Versions API
  slug: deepchecks-application-versions-api
- description: Evaluation applications.
  name: Deepchecks Applications API
  slug: deepchecks-applications-api
- description: LLM interaction logging and retrieval.
  name: Deepchecks Interactions API
  slug: deepchecks-interactions-api
- description: LLM property definitions.
  name: Deepchecks Properties API
  slug: deepchecks-properties-api
- description: Raw tracing spans.
  name: Deepchecks Spans API
  slug: deepchecks-spans-api
- description: Backend metadata.
  name: Deepchecks System API
  slug: deepchecks-system-api
artifact_total: 14
collections:
- collection_type: open
  name: Deepchecks LLM Evaluation API
  slug: open-deepchecks
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/deepchecks-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/deepchecks-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/deepchecks-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/deepchecks
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/deepchecks
- group: company
  title: ''
  type: Website
  url: https://www.deepchecks.com
- group: docs
  title: ''
  type: Documentation
  url: https://llmdocs.deepchecks.com
- group: commercial
  title: ''
  type: Plans
  url: plans/deepchecks-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/deepchecks-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/deepchecks-finops.yml
created: '2026-06-20'
description: Deepchecks is an ML and LLM testing, evaluation, and monitoring platform. Its cloud LLM Evaluation product exposes a REST API for logging LLM interactions, managing applications and versions, retrieving annotations, and configuring evaluation properties, while its open-source Python packages provide continuous validation of tabular, computer-vision, and LLM data and models.
finops:
- name: Deepchecks Finops
  service_category: AI and Machine Learning
  slug: deepchecks-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/deepchecks.png
layout: provider
modified: '2026-06-20'
name: Deepchecks
nav: Providers
network: true
overview: 'Deepchecks publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Application Versions API, Applications API, Interactions API, and 3 more. Tagged areas include AI, LLM, Evaluation, Testing, and Monitoring.


  Deepchecks'' developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Deepchecks Plans Pricing
  plan_count: 4
  slug: deepchecks-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 4
  name: Deepchecks Rate Limits
  slug: deepchecks-rate-limits
score:
  band: thin
  composite: 37.4
  delta: -2.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 53.4
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 39.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/deepchecks/refs/heads/main/screenshots/deepchecks-2026-06-20T175801.png
security:
- kind: authentication
  name: Deepchecks Authentication
  slug: deepchecks-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Deepchecks Domain Security
  slug: deepchecks-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: deepchecks
tags:
- AI
- LLM
- Evaluation
- Testing
- Monitoring
website: https://www.deepchecks.com
---
