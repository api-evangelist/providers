---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Humanloop Agentic Access
  operation_count: 20
  slug: humanloop-agentic-access
  summary_line: 20 operations · 8 acting
api_count: 1
apis:
- description: The Humanloop REST API and SDKs covered prompts, tools, datasets, evaluations, evaluators, and logs for LLM applications. Developers called prompt endpoints from production to capture logs, ran evalua
  name: Humanloop LLM Platform API
  slug: llm-platform
- description: The Datasets API from Humanloop — 2 operation(s) for datasets.
  name: Humanloop Datasets API
  slug: humanloop-datasets-api
- description: The Evaluators API from Humanloop — 2 operation(s) for evaluators.
  name: Humanloop Evaluators API
  slug: humanloop-evaluators-api
- description: The Logs API from Humanloop — 2 operation(s) for logs.
  name: Humanloop Logs API
  slug: humanloop-logs-api
- description: The Prompts API from Humanloop — 4 operation(s) for prompts.
  name: Humanloop Prompts API
  slug: humanloop-prompts-api
- description: The Sessions API from Humanloop — 2 operation(s) for sessions.
  name: Humanloop Sessions API
  slug: humanloop-sessions-api
- description: The Tools API from Humanloop — 2 operation(s) for tools.
  name: Humanloop Tools API
  slug: humanloop-tools-api
artifact_total: 21
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Humanloop Datasets API
  slug: open-humanloop-datasets-api
- collection_type: open
  name: Humanloop Datasets Evaluators API
  slug: open-humanloop-evaluators-api
- collection_type: open
  name: Humanloop Datasets Logs API
  slug: open-humanloop-logs-api
- collection_type: open
  name: Humanloop Datasets Prompts API
  slug: open-humanloop-prompts-api
- collection_type: open
  name: Humanloop Datasets Sessions API
  slug: open-humanloop-sessions-api
- collection_type: open
  name: Humanloop Datasets Tools API
  slug: open-humanloop-tools-api
- collection_type: open
  name: Humanloop API
  slug: open-humanloop
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/anthropic/
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/humanloop-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/humanloop-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/humanloop-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://humanloop.com
- group: docs
  title: ''
  type: Documentation
  url: https://humanloop.com/docs
- group: company
  title: ''
  type: Blog
  url: https://humanloop.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/humanloop
- group: docs
  title: ''
  type: MigrationGuide
  url: https://humanloop.com/docs/guides/migrating-from-humanloop
- group: other
  title: ''
  type: MediaKit
  url: https://humanloop.com/media-kit
- group: commercial
  title: ''
  type: TermsOfService
  url: https://humanloop.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://humanloop.com/privacy
- group: company
  title: ''
  type: Twitter
  url: https://x.com/humanloop
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/humanloop
- group: agent
  title: ''
  type: LlmsText
  url: https://humanloop.com/llms.txt
created: '2026-05-23'
description: Humanloop was an LLM development platform for managing prompts, datasets, evaluations, and production observability of LLM applications, used by AI product teams at companies like Duolingo and Gusto. The platform offered a collaborative prompt editor, versioned prompts and tools, evaluation runs (LLM-as-judge and code-based), dataset management, online evaluators, and full request logging across OpenAI, Anthropic, Google, and other providers, with Python and TypeScript SDKs and a REST API. In 2025 the Humanloop team was acquired by Anthropic and the company has announced it is sunsetting the standalone platform; an official migration guide is published for existing customers. This record captures the historical API surface for archival and discovery purposes.
finops:
- name: Humanloop Finops
  service_category: API
  slug: humanloop-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/humanloop.png
layout: provider
modified: '2026-05-23'
name: Humanloop
nav: Providers
network: true
overview: 'Humanloop publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Datasets API, Evaluators API, Logs API, and 3 more. Tagged areas include LLM Platform, Prompt Management, Evaluations, LLM Ops, and Observability.


  Humanloop''s developer surface includes authentication, documentation, engineering blog, and 12 more developer resources.'
plans:
- name: Humanloop Plans Pricing
  plan_count: 1
  slug: humanloop-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 2
  name: Humanloop Rate Limits
  slug: humanloop-rate-limits
score:
  band: thin
  composite: 38.6
  coverage:
    artifact_dirs: 11
    catalog_gap: 59.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 46.9
    developer_ergonomics: 31.0
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 39.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/humanloop/refs/heads/main/screenshots/humanloop-2026-06-20T182933.png
security:
- kind: authentication
  name: Humanloop Authentication
  slug: humanloop-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Humanloop Domain Security
  slug: humanloop-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: humanloop
tags:
- LLM Platform
- Prompt Management
- Evaluations
- LLM Ops
- Observability
- Datasets
- Prompts
- Tools
- Logs
- Multi-Provider
- Sunsetting
- Acquired
website: https://humanloop.com
---
