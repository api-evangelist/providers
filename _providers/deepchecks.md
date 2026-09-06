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
  score: 19.8
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Deepchecks Agentic Access
  operation_count: 12
  slug: deepchecks-agentic-access
  summary_line: 12 operations · 7 acting
api_count: 1
apis:
- description: The AGPL-3.0 licensed open-source Python package for continuous validation of tabular, computer-vision, and LLM/NLP data and models. Distributed via PyPI (pip install deepchecks); a Python library rat
  name: Deepchecks Open-Source Testing
  slug: open-source-testing
- baseURL: https://app.llm.deepchecks.com/api/v1
  baseurl_source: declared
  description: Versions of an evaluation application.
  name: Deepchecks Application Versions API
  slug: deepchecks-application-versions-api
- baseURL: https://app.llm.deepchecks.com/api/v1
  baseurl_source: declared
  description: Evaluation applications.
  name: Deepchecks Applications API
  slug: deepchecks-applications-api
- baseURL: https://app.llm.deepchecks.com/api/v1
  baseurl_source: declared
  description: LLM interaction logging and retrieval.
  name: Deepchecks Interactions API
  slug: deepchecks-interactions-api
- baseURL: https://app.llm.deepchecks.com/api/v1
  baseurl_source: declared
  description: LLM property definitions.
  name: Deepchecks Properties API
  slug: deepchecks-properties-api
- baseURL: https://app.llm.deepchecks.com/api/v1
  baseurl_source: declared
  description: Raw tracing spans.
  name: Deepchecks Spans API
  slug: deepchecks-spans-api
- baseURL: https://app.llm.deepchecks.com/api/v1
  baseurl_source: declared
  description: Backend metadata.
  name: Deepchecks System API
  slug: deepchecks-system-api
artifact_total: 21
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Deepchecks LLM Evaluation Application Versions API
  slug: open-deepchecks-application-versions-api
- collection_type: open
  name: Deepchecks LLM Evaluation Application Versions Applications API
  slug: open-deepchecks-applications-api
- collection_type: open
  name: Deepchecks LLM Evaluation Application Versions Interactions API
  slug: open-deepchecks-interactions-api
- collection_type: open
  name: Deepchecks LLM Evaluation Application Versions Properties API
  slug: open-deepchecks-properties-api
- collection_type: open
  name: Deepchecks LLM Evaluation Application Versions Spans API
  slug: open-deepchecks-spans-api
- collection_type: open
  name: Deepchecks LLM Evaluation Application Versions System API
  slug: open-deepchecks-system-api
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
overview: 'Deepchecks publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Application Versions API, Applications API, Interactions API, and 3 more. Tagged areas include Artificial Intelligence, LLM, Evaluation, Testing, and Monitoring.


  Deepchecks'' developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Deepchecks Plans Pricing
  plan_count: 4
  slug: deepchecks-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 4
  name: Deepchecks Rate Limits
  slug: deepchecks-rate-limits
score:
  band: thin
  composite: 35.3
  coverage:
    artifact_dirs: 9
    catalog_earned: 64.0
    catalog_earned_first_party: 0.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 47.3
    developer_ergonomics: 21.4
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 35.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.18.3
  scored_at: '2026-09-05'
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
- Artificial Intelligence
- LLM
- Evaluation
- Testing
- Monitoring
website: https://www.deepchecks.com
---
