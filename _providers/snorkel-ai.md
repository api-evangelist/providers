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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 18.0
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: The Snorkel Flow Python SDK (snorkelflow) drives the platform programmatically, connecting to a customer's Snorkel Flow instance via SnorkelFlowContext and an API key. The snorkelflow.client module wr
  name: Snorkel Flow SDK / Platform
  slug: snorkel-flow-sdk-platform
- description: SDK surface (snorkelflow.studio, snorkelflow.lfs, snorkelflow.operators, snorkelflow.templates) for authoring code-based and template-based labeling functions, transformation and slicing functions, an
  name: Programmatic Labeling
  slug: programmatic-labeling
- description: Platform and SDK capabilities for assessing model performance across data splits, running error and slice analysis, and building expert-curated benchmarks. Largely delivered in-platform and through th
  name: Evaluation
  slug: evaluation
- description: The free, open-source snorkel Python library (Apache-2.0) for programmatically building and managing training data with weak supervision - labeling functions, the LabelModel, transformation functions,
  name: Open-Source Snorkel Library
  slug: open-source-snorkel-library
artifact_total: 13
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Snorkel Flow Platform API
  slug: open-snorkel-ai
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/snorkel-ai-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/snorkel-ai-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/snorkel-ai-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/snorkel-ai-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/snorkel-team
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/snorkel-ai
- group: company
  title: ''
  type: Website
  url: https://snorkel.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.snorkel.ai
- group: commercial
  title: ''
  type: Plans
  url: plans/snorkel-ai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/snorkel-ai-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/snorkel-ai-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://snorkel.ai/feed/
created: '2026-06-21'
description: Snorkel AI is a data-development / AI data platform built on the open-source Snorkel weak-supervision library. The enterprise Snorkel Flow platform supports programmatic labeling, data curation, model training, and evaluation, and is driven programmatically through a Python SDK that targets a per-instance REST API rather than a single public hosted endpoint. Snorkel also delivers Expert Data-as-a-Service for frontier-model training and evaluation data.
finops:
- name: Snorkel Ai Finops
  service_category: AI and Machine Learning
  slug: snorkel-ai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/snorkel-ai.png
layout: provider
modified: '2026-06-21'
name: Snorkel AI
nav: Providers
network: true
overview: 'Snorkel AI publishes 3 APIs on the [APIs.io](https://apis.io/) network: Snorkel Flow SDK / Platform, Programmatic Labeling, and Evaluation. Tagged areas include Artificial Intelligence, Data Development, Programmatic Labeling, Weak Supervision, and Evaluation.


  Snorkel AI''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Snorkel Ai Plans Pricing
  plan_count: 3
  slug: snorkel-ai-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 3
  name: Snorkel Ai Rate Limits
  slug: snorkel-ai-rate-limits
score:
  band: thin
  composite: 34.2
  coverage:
    artifact_dirs: 8
    catalog_gap: 56.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 32.7
    developer_ergonomics: 31.0
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 34.8
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: authentication
  name: Snorkel Ai Authentication
  slug: snorkel-ai-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Snorkel Ai Domain Security
  slug: snorkel-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Snorkel Ai Vulnerability Disclosure
  slug: snorkel-ai-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Snorkel Ai Trust Center
  slug: snorkel-ai-trust-center
  summary_line: SOC 2, HIPAA
slug: snorkel-ai
tags:
- Artificial Intelligence
- Data Development
- Programmatic Labeling
- Weak Supervision
- Evaluation
- SDK
website: https://snorkel.ai
---
