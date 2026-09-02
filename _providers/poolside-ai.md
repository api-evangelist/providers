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
    error_semantics: verified
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
  score: 25.5
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Poolside Ai Agentic Access
  operation_count: 3
  slug: poolside-ai-agentic-access
  summary_line: 3 operations · 2 acting
api_count: 1
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
artifact_total: 14
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: OpenAI Compatible chat API
  slug: open-poolside-ai-chat-api
- collection_type: open
  name: OpenAI Compatible chat models API
  slug: open-poolside-ai-models-api
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
overview: 'Poolside publishes 2 APIs on the [APIs.io](https://apis.io/) network: chat API and models API. Tagged areas include Artificial Intelligence, LLM, Foundation Models, Agentic Coding, and Software Engineering.


  Poolside''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Poolside Ai Plans Pricing
  plan_count: 3
  slug: poolside-ai-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 3
  name: Poolside Ai Rate Limits
  slug: poolside-ai-rate-limits
score:
  band: thin
  composite: 37.7
  coverage:
    artifact_dirs: 9
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 48.6
    developer_ergonomics: 23.8
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 37.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.18.0
  scored_at: '2026-09-01'
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
- Artificial Intelligence
- LLM
- Foundation Models
- Agentic Coding
- Software Engineering
- Enterprise
- On-Prem
- Open Weights
website: https://poolside.ai/
---
