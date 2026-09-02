---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
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
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.9
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 42
  human_in_the_loop: 0
  name: Braintrust Data Agentic Access
  operation_count: 69
  slug: braintrust-data-agentic-access
  summary_line: 69 operations · 42 acting
api_count: 1
apis:
- description: The ACL API from Braintrust — 4 operation(s) for acl.
  name: Braintrust ACL API
  slug: braintrust-data-acl-api
- description: The AI Proxy API from Braintrust — 3 operation(s) for ai proxy.
  name: Braintrust AI Proxy API
  slug: braintrust-data-ai-proxy-api
- description: The Credentials API from Braintrust — 3 operation(s) for credentials.
  name: Braintrust Credentials API
  slug: braintrust-data-credentials-api
- description: The Datasets API from Braintrust — 6 operation(s) for datasets.
  name: Braintrust Datasets API
  slug: braintrust-data-datasets-api
- description: The Evals API from Braintrust — 1 operation(s) for evals.
  name: Braintrust Evals API
  slug: braintrust-data-evals-api
- description: The Experiments API from Braintrust — 6 operation(s) for experiments.
  name: Braintrust Experiments API
  slug: braintrust-data-experiments-api
- description: The Functions API from Braintrust — 3 operation(s) for functions.
  name: Braintrust Functions API
  slug: braintrust-data-functions-api
- description: The Logs API from Braintrust — 3 operation(s) for logs.
  name: Braintrust Logs API
  slug: braintrust-data-logs-api
- description: The Organization API from Braintrust — 3 operation(s) for organization.
  name: Braintrust Organization API
  slug: braintrust-data-organization-api
- description: The Project Configuration API from Braintrust — 4 operation(s) for project configuration.
  name: Braintrust Project Configuration API
  slug: braintrust-data-project-configuration-api
- description: The Projects API from Braintrust — 2 operation(s) for projects.
  name: Braintrust Projects API
  slug: braintrust-data-projects-api
- description: The Prompts API from Braintrust — 2 operation(s) for prompts.
  name: Braintrust Prompts API
  slug: braintrust-data-prompts-api
artifact_total: 34
asyncapis:
- description: AsyncAPI description of Braintrust's documented HTTP Server-Sent Events (SSE) streams. Braintrust does NOT expose a WebSocket API. Streaming is delivered as one-way HTTP SSE over the same REST endpoin
  name: Braintrust Streaming (SSE) API
  slug: braintrust-data-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Braintrust REST ACL API
  slug: open-braintrust-data-acl-api
- collection_type: open
  name: Braintrust REST ACL AI Proxy API
  slug: open-braintrust-data-ai-proxy-api
- collection_type: open
  name: Braintrust REST ACL Credentials API
  slug: open-braintrust-data-credentials-api
- collection_type: open
  name: Braintrust REST ACL Datasets API
  slug: open-braintrust-data-datasets-api
- collection_type: open
  name: Braintrust REST ACL Evals API
  slug: open-braintrust-data-evals-api
- collection_type: open
  name: Braintrust REST ACL Experiments API
  slug: open-braintrust-data-experiments-api
- collection_type: open
  name: Braintrust REST ACL Functions API
  slug: open-braintrust-data-functions-api
- collection_type: open
  name: Braintrust REST ACL Logs API
  slug: open-braintrust-data-logs-api
- collection_type: open
  name: Braintrust REST ACL Organization API
  slug: open-braintrust-data-organization-api
- collection_type: open
  name: Braintrust REST ACL Project Configuration API
  slug: open-braintrust-data-project-configuration-api
- collection_type: open
  name: Braintrust REST ACL Projects API
  slug: open-braintrust-data-projects-api
- collection_type: open
  name: Braintrust REST ACL Prompts API
  slug: open-braintrust-data-prompts-api
- collection_type: open
  name: Braintrust REST API
  slug: open-braintrust-data
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/braintrust-data-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/braintrust-data-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/braintrust-data-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/braintrustdata
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/braintrustdata
- group: company
  title: ''
  type: Website
  url: https://www.braintrust.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://www.braintrust.dev/docs
- group: commercial
  title: ''
  type: Plans
  url: plans/braintrust-data-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/braintrust-data-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/braintrust-data-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.braintrust.dev/blog
created: '2026-06-20'
description: Braintrust (braintrust.dev) is an end-to-end platform for building, evaluating, and observing AI applications. Its REST API at api.braintrust.dev exposes projects, experiments, datasets, logs/spans, prompts, functions and scorers, evals, and full organization/ACL management, plus an OpenAI-compatible AI proxy, all authenticated with a Bearer API key.
finops:
- name: Braintrust Data Finops
  service_category: AI and Machine Learning
  slug: braintrust-data-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/braintrust-data.png
layout: provider
modified: '2026-06-20'
name: Braintrust
nav: Providers
network: true
overview: 'Braintrust publishes 12 APIs on the [APIs.io](https://apis.io/) network, including ACL API, AI Proxy API, Credentials API, and 9 more. Tagged areas include Artificial Intelligence, LLM, Evaluation, Observability, and LLMOps.


  The Braintrust catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Braintrust''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Braintrust Data Plans Pricing
  plan_count: 3
  slug: braintrust-data-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 7
  name: Braintrust Data Rate Limits
  slug: braintrust-data-rate-limits
rules:
- effective_rule_count: 31
  extends:
  - spectral:asyncapi
  name: Braintrust API Rules
  rule_count: 4
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 3
  slug: braintrust-data-asyncapi-spectral-rules
score:
  band: developing
  composite: 43.8
  coverage:
    artifact_dirs: 12
    catalog_gap: 47.3
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.2
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 11.4
    contract_quality: 64.3
    developer_ergonomics: 35.7
    discoverability: 68.5
    governance: 11.4
    operational_transparency: 34.2
  previous_composite: 44.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/braintrust-data/refs/heads/main/screenshots/braintrust-data-2026-06-20T173631.png
security:
- kind: authentication
  name: Braintrust Data Authentication
  slug: braintrust-data-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Braintrust Data Domain Security
  slug: braintrust-data-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: braintrust-data
tags:
- Artificial Intelligence
- LLM
- Evaluation
- Observability
- LLMOps
website: https://www.braintrust.dev/
---
