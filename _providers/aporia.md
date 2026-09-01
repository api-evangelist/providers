---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-01'
api_count: 4
apis:
- description: Coralogix AI Guardrails is the post-acquisition continuation of Aporia's guardrails product, intercepting prompts and responses between applications and LLMs to enforce policies covering hallucination
  name: Coralogix AI Guardrails
  slug: coralogix-ai-guardrails
- description: Coralogix AI Observability combines Aporia's monitoring capabilities with Coralogix's logging and tracing backend to provide end-to-end visibility into LLM and agent applications, including agent disc
  name: Coralogix AI Observability
  slug: coralogix-ai-observability
- description: The original Aporia Guardrails product offered millisecond-latency policy enforcement on LLM prompts and responses with a library of pre-built detectors (hallucination, prompt injection, PII, toxicity
  name: Aporia Guardrails (Legacy)
  slug: aporia-guardrails-legacy
- description: Aporia ML Observability provided monitoring for classical ML models including drift detection, data quality checks, performance tracking, and custom monitors. Now consolidated into the Coralogix obser
  name: Aporia ML Observability (Legacy)
  slug: aporia-ml-observability-legacy
artifact_total: 26
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aporia-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.aporia.com/
- group: other
  title: ''
  type: CoralogixProduct
  url: https://coralogix.com/ai-observability-and-security/
- group: other
  title: ''
  type: AcquiredBy
  url: https://coralogix.com/
- group: company
  title: ''
  type: Blog
  url: https://www.aporia.com/learn/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/aporia/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aporia-ai
- group: docs
  title: ''
  type: Documentation
  url: https://gr-docs.aporia.com/
- group: other
  title: ''
  type: AcquisitionNotice
  url: ''
- group: agent
  title: ''
  type: LlmsText
  url: https://gr-docs.aporia.com/llms.txt
created: '2026-05-23'
description: Aporia was an AI guardrails and observability platform for production LLM and ML applications, known for low-latency guardrails covering hallucination, prompt injection, PII, toxicity, off-topic responses, and custom policies, alongside full ML monitoring for drift and data quality. Coralogix acquired Aporia in late 2024 and the Aporia guardrails technology is now offered as part of the Coralogix AI Observability and AI Guardrails product line, with the standalone Aporia.com experience consolidated into Coralogix's portfolio.
features:
- description: Low-latency policy enforcement on LLM prompts and responses with a library of pre-built detectors.
  name: LLM Guardrails
- description: Detect ungrounded or fabricated responses in RAG and general LLM applications.
  name: Hallucination Detection
- description: Identify direct and indirect prompt injection attempts.
  name: Prompt Injection Detection
- description: Screen prompts and responses for personally identifiable information.
  name: PII Detection
- description: Build organization-specific policies for restricted topics, competitor mentions, and brand-safe responses.
  name: Custom Policies
- description: Drift, data quality, performance, and custom monitor support for classical ML.
  name: ML Monitoring
- description: Native integration with Coralogix observability backend post-acquisition.
  name: Coralogix Integration
finops:
- name: Aporia Finops
  service_category: API
  slug: aporia-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/aporia.png
integrations:
- description: Guardrails for OpenAI Chat Completions and Assistants.
  name: OpenAI
- description: Guardrails for Anthropic Claude models.
  name: Anthropic
- description: Guardrails for Azure-hosted OpenAI deployments.
  name: Azure OpenAI
- description: Guardrails for models accessed through AWS Bedrock.
  name: AWS Bedrock
- description: Native integration for LangChain chains and agents.
  name: LangChain
- description: Integration for LlamaIndex RAG applications.
  name: LlamaIndex
- description: Native integration with Coralogix logging, tracing, and observability backend.
  name: Coralogix
layout: provider
modified: '2026-05-23'
name: Aporia
nav: Providers
network: true
overview: 'Aporia publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include AI Guardrails, ML Observability, LLM Monitoring, Coralogix, and Acquired.


  Aporia''s developer surface includes engineering blog, documentation, and 7 more developer resources.'
plans:
- name: Aporia Plans Pricing
  plan_count: 1
  slug: aporia-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 2
  name: Aporia Rate Limits
  slug: aporia-rate-limits
score:
  band: emerging
  composite: 15.7
  coverage:
    artifact_dirs: 7
    catalog_gap: 61.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 72.2
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 15.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 9.1
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/aporia/refs/heads/main/screenshots/aporia-2026-06-20T172312.png
security:
- kind: domain-security
  name: Aporia Domain Security
  slug: aporia-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aporia
tags:
- AI Guardrails
- ML Observability
- LLM Monitoring
- Coralogix
- Acquired
- Hallucination Detection
- Policy Enforcement
use_cases:
- description: Enforce policies on prompts and responses in production GenAI applications.
  name: LLM Application Guardrails
- description: Block ungrounded responses from retrieval-augmented generation pipelines.
  name: RAG Hallucination Prevention
- description: Prevent off-topic, competitor, or off-brand responses from customer-facing LLM apps.
  name: Brand Safety
- description: Detect distribution drift in classical ML models in production.
  name: ML Drift Monitoring
website: https://www.aporia.com/
---
