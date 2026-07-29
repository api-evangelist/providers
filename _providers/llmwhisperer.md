---
access_model:
  confidence: high
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
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
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Llmwhisperer Agentic Access
  operation_count: 8
  slug: llmwhisperer-agentic-access
  summary_line: 8 operations · 4 acting
api_count: 5
apis:
- description: The Extraction API from LLMWhisperer — 1 operation(s) for extraction.
  name: LLMWhisperer Extraction API
  slug: llmwhisperer-extraction-api
- description: The Highlights API from LLMWhisperer — 1 operation(s) for highlights.
  name: LLMWhisperer Highlights API
  slug: llmwhisperer-highlights-api
- description: The Retrieve API from LLMWhisperer — 1 operation(s) for retrieve.
  name: LLMWhisperer Retrieve API
  slug: llmwhisperer-retrieve-api
- description: The Status API from LLMWhisperer — 1 operation(s) for status.
  name: LLMWhisperer Status API
  slug: llmwhisperer-status-api
- description: The Webhooks API from LLMWhisperer — 1 operation(s) for webhooks.
  name: LLMWhisperer Webhooks API
  slug: llmwhisperer-webhooks-api
artifact_total: 12
collections:
- collection_type: open
  name: LLMWhisperer API
  slug: open-llmwhisperer
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/llmwhisperer-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/llmwhisperer-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/llmwhisperer-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Zipstack
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/unstract
- group: company
  title: ''
  type: Website
  url: https://unstract.com/llmwhisperer/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.unstract.com/llmwhisperer/
- group: commercial
  title: ''
  type: Plans
  url: plans/llmwhisperer-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/llmwhisperer-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/llmwhisperer-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://unstract.com/feed/
created: '2026-06-20'
description: LLMWhisperer is a document-to-text extraction API from Unstract (Zipstack) that turns complex PDFs, scanned documents, and images into clean, layout-preserving text ready for large language models. It exposes an asynchronous REST API (v2) - submit a document to /whisper, poll /whisper-status, then retrieve the extracted text via /whisper-retrieve - plus line-level highlight coordinates and webhook callbacks. Authentication is via the unstract-key header.
finops:
- name: Llmwhisperer Finops
  service_category: AI and Machine Learning
  slug: llmwhisperer-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/llmwhisperer.png
layout: provider
modified: '2026-06-20'
name: LLMWhisperer
nav: Providers
network: true
overview: 'LLMWhisperer publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Extraction API, Highlights API, Retrieve API, and 2 more. Tagged areas include AI, LLM, Document Extraction, OCR, and Text Extraction.


  LLMWhisperer''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Llmwhisperer Plans Pricing
  plan_count: 3
  slug: llmwhisperer-plans-pricing
random_paper: 30
rate_limits:
- limit_count: 3
  name: Llmwhisperer Rate Limits
  slug: llmwhisperer-rate-limits
score:
  band: thin
  composite: 38.8
  delta: -2.3
  facets:
    commercial_clarity: 39.5
    contract_quality: 57.5
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 41.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/llmwhisperer/refs/heads/main/screenshots/llmwhisperer-2026-06-20T184627.png
security:
- kind: authentication
  name: Llmwhisperer Authentication
  slug: llmwhisperer-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Llmwhisperer Domain Security
  slug: llmwhisperer-domain-security
  summary_line: TLSv1.3 · DMARC
slug: llmwhisperer
tags:
- AI
- LLM
- Document Extraction
- OCR
- Text Extraction
website: https://unstract.com/llmwhisperer/
---
