---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Poolside Ai Agentic Access
  operation_count: 3
  slug: poolside-ai-agentic-access
  summary_line: 3 operations · 2 acting
api_count: 4
apis:
- description: Poolside's own admin API (/poolside/v1) for automating user and team administration on a deployment - create/get/update/delete users, and add, remove, or replace team membership - as an alternative or
  name: Poolside Identity Management API
  slug: poolside-identity-management-api
- description: SCIM 2.0 provisioning endpoint (/scim) for connecting an external identity provider (Okta, Entra ID, etc.) to automatically provision and deprovision Poolside users on a deployment.
  name: Poolside SCIM API
  slug: poolside-scim-api
- description: The chat API from Poolside — 2 operation(s) for chat.
  name: Poolside chat API
  slug: poolside-ai-chat-api
- description: The models API from Poolside — 1 operation(s) for models.
  name: Poolside models API
  slug: poolside-ai-models-api
artifact_total: 11
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/poolside-ai-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/poolside-ai-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/poolside-ai-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/poolside-ai-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/poolsideai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/poolsideai
- group: company
  title: ''
  type: Website
  url: https://poolside.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.poolside.ai/
- group: commercial
  title: ''
  type: Plans
  url: plans/poolside-ai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/poolside-ai-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/poolside-ai-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://poolside.ai/blog
created: '2026-07-02'
description: Poolside is an AI foundation model lab (founded 2023 by former GitHub CTO Jason Warner and Eiso Kant) building open-weight foundation models - the Laguna family - purpose-built for agentic software engineering. Poolside does not run a shared public SaaS API the way OpenAI or Groq do. Instead it publishes a full, public API reference (docs.poolside.ai) for an OpenAI-compatible inference API plus an admin/identity API, but the API itself only comes alive once a customer has a provisioned Poolside deployment - into their own AWS/Azure/Google Cloud VPC, on customer-owned NVIDIA GPU clusters via Helm, or fully air-gapped on-prem. There is no public signup page, free tier, or published pricing; access is arranged directly with Poolside's sales team. Separately, Poolside's smaller open-weight model, Laguna XS 2.1, can be called by anyone through third-party inference hosts such as OpenRouter, which is the closest thing to a public, self-serve way to hit a Poolside model over HTTP.
finops:
- name: Poolside Ai Finops
  service_category: AI and Machine Learning
  slug: poolside-ai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/poolside-ai.png
layout: provider
modified: '2026-07-02'
name: Poolside
nav: Providers
network: true
overview: 'Poolside publishes 2 APIs on the [APIs.io](https://apis.io/) network: chat API and models API. Tagged areas include AI, LLM, Foundation Models, Agentic Coding, and Software Engineering.


  Poolside''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Poolside Ai Plans Pricing
  plan_count: 3
  slug: poolside-ai-plans-pricing
random_paper: 39
rate_limits:
- limit_count: 3
  name: Poolside Ai Rate Limits
  slug: poolside-ai-rate-limits
score:
  band: thin
  composite: 41.9
  delta: 0.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 53.1
    developer_ergonomics: 21.7
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 41.9
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Poolside Ai Authentication
  slug: poolside-ai-authentication
  summary_line: http · 1 scheme
- kind: vulnerability-disclosure
  name: Poolside Ai Vulnerability Disclosure
  slug: poolside-ai-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Poolside Ai Trust Center
  slug: poolside-ai-trust-center
  summary_line: SOC 2, ISO 27001
slug: poolside-ai
tags:
- AI
- LLM
- Foundation Models
- Agentic Coding
- Software Engineering
- Enterprise
- On-Prem
- Open Weights
website: https://poolside.ai/
---
