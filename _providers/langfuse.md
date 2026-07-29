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
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.0
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 46
  human_in_the_loop: 0
  name: Langfuse Agentic Access
  operation_count: 96
  slug: langfuse-agentic-access
  summary_line: 96 operations · 46 acting
api_count: 28
apis:
- description: The AnnotationQueues API from Langfuse — 5 operation(s) for annotationqueues.
  name: Langfuse AnnotationQueues API
  slug: langfuse-annotationqueues-api
- description: The BlobStorageIntegrations API from Langfuse — 2 operation(s) for blobstorageintegrations.
  name: Langfuse BlobStorageIntegrations API
  slug: langfuse-blobstorageintegrations-api
- description: The Comments API from Langfuse — 2 operation(s) for comments.
  name: Langfuse Comments API
  slug: langfuse-comments-api
- description: The DatasetItems API from Langfuse — 2 operation(s) for datasetitems.
  name: Langfuse DatasetItems API
  slug: langfuse-datasetitems-api
- description: The DatasetRunItems API from Langfuse — 1 operation(s) for datasetrunitems.
  name: Langfuse DatasetRunItems API
  slug: langfuse-datasetrunitems-api
- description: The Datasets API from Langfuse — 4 operation(s) for datasets.
  name: Langfuse Datasets API
  slug: langfuse-datasets-api
- description: The Health API from Langfuse — 1 operation(s) for health.
  name: Langfuse Health API
  slug: langfuse-health-api
- description: The Ingestion API from Langfuse — 1 operation(s) for ingestion.
  name: Langfuse Ingestion API
  slug: langfuse-ingestion-api
- description: The LegacyMetricsV1 API from Langfuse — 1 operation(s) for legacymetricsv1.
  name: Langfuse LegacyMetricsV1 API
  slug: langfuse-legacymetricsv1-api
- description: The LegacyObservationsV1 API from Langfuse — 2 operation(s) for legacyobservationsv1.
  name: Langfuse LegacyObservationsV1 API
  slug: langfuse-legacyobservationsv1-api
- description: The LegacyScoreV1 API from Langfuse — 2 operation(s) for legacyscorev1.
  name: Langfuse LegacyScoreV1 API
  slug: langfuse-legacyscorev1-api
- description: The LlmConnections API from Langfuse — 2 operation(s) for llmconnections.
  name: Langfuse LlmConnections API
  slug: langfuse-llmconnections-api
- description: The Media API from Langfuse — 2 operation(s) for media.
  name: Langfuse Media API
  slug: langfuse-media-api
- description: The Metrics API from Langfuse — 1 operation(s) for metrics.
  name: Langfuse Metrics API
  slug: langfuse-metrics-api
- description: The Models API from Langfuse — 2 operation(s) for models.
  name: Langfuse Models API
  slug: langfuse-models-api
- description: The Observations API from Langfuse — 1 operation(s) for observations.
  name: Langfuse Observations API
  slug: langfuse-observations-api
- description: The Opentelemetry API from Langfuse — 1 operation(s) for opentelemetry.
  name: Langfuse Opentelemetry API
  slug: langfuse-opentelemetry-api
- description: The Organizations API from Langfuse — 4 operation(s) for organizations.
  name: Langfuse Organizations API
  slug: langfuse-organizations-api
- description: The Projects API from Langfuse — 4 operation(s) for projects.
  name: Langfuse Projects API
  slug: langfuse-projects-api
- description: The Prompts API from Langfuse — 2 operation(s) for prompts.
  name: Langfuse Prompts API
  slug: langfuse-prompts-api
- description: The PromptVersion API from Langfuse — 1 operation(s) for promptversion.
  name: Langfuse PromptVersion API
  slug: langfuse-promptversion-api
- description: The Scim API from Langfuse — 5 operation(s) for scim.
  name: Langfuse Scim API
  slug: langfuse-scim-api
- description: The ScoreConfigs API from Langfuse — 2 operation(s) for scoreconfigs.
  name: Langfuse ScoreConfigs API
  slug: langfuse-scoreconfigs-api
- description: The Scores API from Langfuse — 2 operation(s) for scores.
  name: Langfuse Scores API
  slug: langfuse-scores-api
- description: The Sessions API from Langfuse — 2 operation(s) for sessions.
  name: Langfuse Sessions API
  slug: langfuse-sessions-api
- description: The Trace API from Langfuse — 2 operation(s) for trace.
  name: Langfuse Trace API
  slug: langfuse-trace-api
- description: The UnstableEvaluationRules API from Langfuse — 2 operation(s) for unstableevaluationrules.
  name: Langfuse UnstableEvaluationRules API
  slug: langfuse-unstableevaluationrules-api
- description: The UnstableEvaluators API from Langfuse — 2 operation(s) for unstableevaluators.
  name: Langfuse UnstableEvaluators API
  slug: langfuse-unstableevaluators-api
artifact_total: 37
collections:
- collection_type: open
  name: langfuse
  slug: open-langfuse
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/langfuse-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/langfuse-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/langfuse-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/langfuse-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/langfuse-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/langfuse
- group: company
  title: ''
  type: Website
  url: https://langfuse.com/
- group: docs
  title: ''
  type: Documentation
  url: https://langfuse.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://api.reference.langfuse.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://langfuse.com/pricing
- group: build
  title: ''
  type: GitHub
  url: https://github.com/langfuse/langfuse
- group: commercial
  title: ''
  type: Plans
  url: plans/langfuse-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/langfuse-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/langfuse-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://api.reference.langfuse.com/llms.txt
created: '2026-05-08'
description: Langfuse is an open-source LLM engineering platform offering tracing, evaluations, prompt management, datasets, and metrics. The Langfuse API supports both self-hosted and multi-region cloud deployments (US, EU, Japan, HIPAA-compliant US) and integrates with LangChain, LlamaIndex, OpenTelemetry, and any LLM stack.
finops:
- name: Langfuse Finops
  service_category: AI
  slug: langfuse-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/langfuse.png
layout: provider
modified: '2026-05-19'
name: Langfuse
nav: Providers
network: true
overview: 'Langfuse publishes 28 APIs on the [APIs.io](https://apis.io/) network, including AnnotationQueues API, BlobStorageIntegrations API, Comments API, and 25 more. Tagged areas include AI, LLM, Observability, Open Source, and Evaluations.


  Langfuse''s developer surface includes authentication, documentation, API reference, pricing, GitHub presence, and 10 more developer resources.'
plans:
- name: Langfuse Plans Pricing
  plan_count: 5
  slug: langfuse-plans-pricing
random_paper: 53
rate_limits:
- limit_count: 4
  name: Langfuse Rate Limits
  slug: langfuse-rate-limits
score:
  band: thin
  composite: 40.3
  delta: -3.2
  facets:
    commercial_clarity: 57.9
    contract_quality: 45.1
    developer_ergonomics: 26.1
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 43.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 28
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/langfuse/refs/heads/main/screenshots/langfuse-2026-06-20T184307.png
security:
- kind: authentication
  name: Langfuse Authentication
  slug: langfuse-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Langfuse Domain Security
  slug: langfuse-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Langfuse Vulnerability Disclosure
  slug: langfuse-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Langfuse Trust Center
  slug: langfuse-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: langfuse
tags:
- AI
- LLM
- Observability
- Open Source
- Evaluations
website: https://langfuse.com/
---
