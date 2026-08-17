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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 25
  human_in_the_loop: 0
  name: Extend Ai Agentic Access
  operation_count: 41
  slug: extend-ai-agentic-access
  summary_line: 41 operations · 25 acting
api_count: 9
apis:
- description: The Batch API from Extend — 5 operation(s) for batch.
  name: Extend Batch API
  slug: extend-ai-batch-api
- description: The Classify API from Extend — 4 operation(s) for classify.
  name: Extend Classify API
  slug: extend-ai-classify-api
- description: The Evaluations API from Extend — 4 operation(s) for evaluations.
  name: Extend Evaluations API
  slug: extend-ai-evaluations-api
- description: The Extract API from Extend — 6 operation(s) for extract.
  name: Extend Extract API
  slug: extend-ai-extract-api
- description: The Files API from Extend — 3 operation(s) for files.
  name: Extend Files API
  slug: extend-ai-files-api
- description: The Parse API from Extend — 3 operation(s) for parse.
  name: Extend Parse API
  slug: extend-ai-parse-api
- description: The Split API from Extend — 3 operation(s) for split.
  name: Extend Split API
  slug: extend-ai-split-api
- description: The Workflow Runs API from Extend — 3 operation(s) for workflow runs.
  name: Extend Workflow Runs API
  slug: extend-ai-workflow-runs-api
- description: The Workflows API from Extend — 2 operation(s) for workflows.
  name: Extend Workflows API
  slug: extend-ai-workflows-api
artifact_total: 27
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Extend Batch API
  slug: open-extend-ai-batch-api
- collection_type: open
  name: Extend Batch Classify API
  slug: open-extend-ai-classify-api
- collection_type: open
  name: Extend Batch Evaluations API
  slug: open-extend-ai-evaluations-api
- collection_type: open
  name: Extend Batch Extract API
  slug: open-extend-ai-extract-api
- collection_type: open
  name: Extend Batch Files API
  slug: open-extend-ai-files-api
- collection_type: open
  name: Extend Batch Parse API
  slug: open-extend-ai-parse-api
- collection_type: open
  name: Extend Batch Split API
  slug: open-extend-ai-split-api
- collection_type: open
  name: Extend Batch Workflow Runs API
  slug: open-extend-ai-workflow-runs-api
- collection_type: open
  name: Extend Batch Workflows API
  slug: open-extend-ai-workflows-api
- collection_type: open
  name: Extend API
  slug: open-extend-ai
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/extend-ai-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/extend-ai-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/extend-ai-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/extend-ai-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/extend-ai
- group: company
  title: ''
  type: Website
  url: https://www.extend.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.extend.ai
- group: commercial
  title: ''
  type: Plans
  url: plans/extend-ai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/extend-ai-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/extend-ai-finops.yml
created: '2026-06-20'
description: Extend is an intelligent document processing platform that turns documents into high quality, structured data. Its REST API at api.extend.ai exposes parsing, extraction, classification, and splitting processors, durable multi-step workflows, evaluation sets, and batch processing for automating document-heavy operations.
finops:
- name: Extend Ai Finops
  service_category: AI and Machine Learning
  slug: extend-ai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/extend-ai.png
layout: provider
modified: '2026-06-20'
name: Extend
nav: Providers
network: true
overview: 'Extend publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Batch API, Classify API, Evaluations API, and 6 more. Tagged areas include Document Processing, Document AI, Intelligent Document Processing, OCR, and Extraction.


  Extend''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Extend Ai Plans Pricing
  plan_count: 3
  slug: extend-ai-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 5
  name: Extend Ai Rate Limits
  slug: extend-ai-rate-limits
score:
  band: thin
  composite: 38.4
  delta: 0.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 53.9
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 38.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/extend-ai/refs/heads/main/screenshots/extend-ai-2026-06-20T180945.png
security:
- kind: authentication
  name: Extend Ai Authentication
  slug: extend-ai-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Extend Ai Domain Security
  slug: extend-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Extend Ai Trust Center
  slug: extend-ai-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: extend-ai
tags:
- Document Processing
- Document AI
- Intelligent Document Processing
- OCR
- Extraction
- Classification
website: https://www.extend.ai
---
