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
- acting_count: 8
  human_in_the_loop: 0
  name: Humanloop Agentic Access
  operation_count: 20
  slug: humanloop-agentic-access
  summary_line: 20 operations · 8 acting
api_count: 7
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
artifact_total: 14
collections:
- collection_type: open
  name: Humanloop API
  slug: open-humanloop
common:
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


  Humanloop''s developer surface includes authentication, documentation, engineering blog, and 11 more developer resources.'
plans:
- name: Humanloop Plans Pricing
  plan_count: 1
  slug: humanloop-plans-pricing
random_paper: 31
rate_limits:
- limit_count: 2
  name: Humanloop Rate Limits
  slug: humanloop-rate-limits
score:
  band: thin
  composite: 38.5
  delta: -2.1
  facets:
    commercial_clarity: 50.0
    contract_quality: 53.4
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 40.6
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
