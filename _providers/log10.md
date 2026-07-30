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
- acting_count: 5
  human_in_the_loop: 0
  name: Log10 Agentic Access
  operation_count: 10
  slug: log10-agentic-access
  summary_line: 10 operations · 5 acting
api_count: 6
apis:
- description: API for submitting human and automated feedback on LLM completions, defining feedback tasks with structured scales, and accessing AutoFeedback predictions via GraphQL using completion identifiers.
  name: Log10 Feedback API
  slug: log10-feedback-api
- description: API for running automated evaluations and benchmarking logged completions across multiple LLM providers, generating performance reports and accuracy insights to support model selection and prompt opti
  name: Log10 Evaluation API
  slug: log10-evaluation-api
- description: Completions
  name: Log10 Completions API
  slug: log10-completions-api
- description: Feedback
  name: Log10 Feedback API
  slug: log10-feedback-api
- description: FeedbackTasks
  name: Log10 FeedbackTasks API
  slug: log10-feedbacktasks-api
- description: Sessions
  name: Log10 Sessions API
  slug: log10-sessions-api
artifact_total: 23
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/log10-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/log10-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/log10-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/log10-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://log10.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.log10.io
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/log10-io
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/log10-io
- group: company
  title: ''
  type: Blog
  url: https://log10.io/news
- group: commercial
  title: ''
  type: Pricing
  url: https://log10.io/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://trust.log10.io
- group: other
  title: ''
  type: X
  url: https://x.com/log10io
- group: commercial
  title: ''
  type: Plans
  url: plans/log10-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/log10-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/log10-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/log10-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/log10-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/completion.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/feedback.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/feedback-task.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/session.json
- group: company
  title: ''
  type: Blog
  url: blogs/blogs.json
created: 2026-06-13
description: Log10 is an LLMOps platform that provides REST API and SDK capabilities for capturing, logging, and managing LLM completions across major providers such as OpenAI, Anthropic, Google Gemini, Mistral, and Meta Llama. The platform enables engineering teams to debug prompt chains, run automated evaluations, collect human and AI-generated feedback, and benchmark model outputs at scale. Log10 supports session-based tracing, tag-based filtering, and cost tracking to help organizations optimize accuracy and operational efficiency of their generative AI applications. Developers can integrate via a Python SDK, TypeScript SDK, or directly via the REST and GraphQL API using an API token and organization ID.
examples:
- key_count: 4
  name: Create Completion
  slug: create-completion
- key_count: 4
  name: Create Session
  slug: create-session
- key_count: 4
  name: Upload Feedback
  slug: upload-feedback
finops:
- name: Log10 Finops
  service_category: ''
  slug: log10-finops
graphqls:
- description: 'Log10 exposes a GraphQL API for querying LLM completion data, retrieving feedback, and accessing auto-generated feedback (AutoFeedback) predictions. The API is used by the Log10 Python and TypeScript '
  name: Log10 GraphQL API
  slug: log10-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/log10.png
json_schemas:
- name: Completion
  property_count: 12
  slug: completion
- name: FeedbackTask
  property_count: 6
  slug: feedback-task
- name: Feedback
  property_count: 7
  slug: feedback
- name: Session
  property_count: 1
  slug: session
jsonld:
- class_count: 5
  name: Log10 Context
  property_count: 24
  slug: log10-context
layout: provider
modified: 2026-06-13
name: Log10
nav: Providers
network: true
overview: 'Log10 publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Feedback API, Completions API, and 3 more. Tagged areas include LLM, Logging, Observability, Evaluation, and Feedback.


  The Log10 catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Log10''s developer surface includes authentication, documentation, engineering blog, pricing, and 18 more developer resources.'
plans:
- name: Log10 Plans Pricing
  plan_count: 3
  slug: log10-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Log10 Rate Limits
  slug: log10-rate-limits
rules:
- name: Log10 API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: log10-jsonschema-spectral-rules
score:
  band: developing
  composite: 48.4
  delta: -4.7
  facets:
    commercial_clarity: 57.9
    contract_quality: 56.4
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 21.1
  previous_composite: 53.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/log10/refs/heads/main/screenshots/log10-2026-06-20T184646.png
security:
- kind: authentication
  name: Log10 Authentication
  slug: log10-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Log10 Domain Security
  slug: log10-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Log10 Trust Center
  slug: log10-trust-center
  summary_line: SOC 2, HIPAA
slug: log10
tags:
- LLM
- Logging
- Observability
- Evaluation
- Feedback
- Debugging
- LLMOps
- Artificial Intelligence
- Machine Learning
website: https://log10.io
---
