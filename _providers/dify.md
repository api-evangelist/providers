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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 10
  human_in_the_loop: 3
  name: Dify Agentic Access
  operation_count: 13
  slug: dify-agentic-access
  summary_line: 13 operations · 10 acting · 3 human-in-the-loop
api_count: 7
apis:
- description: Dify is an open-source platform for building AI applications. We combine Backend-as-a-Service and LLMOps to streamline the development of generative AI solutions, making it accessible to both develope
  name: Dify
  slug: dify
- description: The Chat API from Dify — 2 operation(s) for chat.
  name: Dify Chat API
  slug: dify-chat-api
- description: The Completion API from Dify — 2 operation(s) for completion.
  name: Dify Completion API
  slug: dify-completion-api
- description: The Conversations API from Dify — 3 operation(s) for conversations.
  name: Dify Conversations API
  slug: dify-conversations-api
- description: The Datasets API from Dify — 2 operation(s) for datasets.
  name: Dify Datasets API
  slug: dify-datasets-api
- description: The Files API from Dify — 1 operation(s) for files.
  name: Dify Files API
  slug: dify-files-api
- description: The Workflows API from Dify — 3 operation(s) for workflows.
  name: Dify Workflows API
  slug: dify-workflows-api
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Dify Chat API
  slug: open-dify-chat-api
- collection_type: open
  name: Dify Chat Completion API
  slug: open-dify-completion-api
- collection_type: open
  name: Dify Chat Conversations API
  slug: open-dify-conversations-api
- collection_type: open
  name: Dify Chat Datasets API
  slug: open-dify-datasets-api
- collection_type: open
  name: Dify Chat Files API
  slug: open-dify-files-api
- collection_type: open
  name: Dify Chat Workflows API
  slug: open-dify-workflows-api
- collection_type: open
  name: Dify API
  slug: open-dify
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/dify-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/dify-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dify-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/dify-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/langgenius
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/langgenius
- group: company
  title: ''
  type: Website
  url: https://dify.ai/
- group: commercial
  title: ''
  type: Pricing
  url: https://dify.ai/pricing
- group: other
  title: ''
  type: Marketplace
  url: https://marketplace.dify.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.dify.ai/
- group: company
  title: ''
  type: Blog
  url: https://dify.ai/blog
- group: operate
  title: ''
  type: RoadMap
  url: https://roadmap.dify.ai/roadmap
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dify.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dify.ai/privacy
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.dify.ai/llms.txt
created: '2025-02-08'
description: Dify is an open-source platform for building AI applications. We combine Backend-as-a-Service and LLMOps to streamline the development of generative AI solutions, making it accessible to both developers and non-technical innovators.
finops:
- name: Dify Finops
  service_category: API
  slug: dify-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dify.png
layout: provider
modified: '2026-04-28'
name: Dify
nav: Providers
network: true
overview: 'Dify publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Chat API, Completion API, Conversations API, and 3 more. Tagged areas include Artificial Intelligence, Backend-As-A-Service, and LLMOps.


  Dify''s developer surface includes authentication, pricing, documentation, engineering blog, and 11 more developer resources.'
plans:
- name: Dify Plans Pricing
  plan_count: 3
  slug: dify-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 5
  name: Dify Rate Limits
  slug: dify-rate-limits
score:
  band: thin
  composite: 36.4
  delta: -0.7
  facets:
    access_clarity: 55.3
    commercial_clarity: 55.3
    contract_governance: 0.0
    contract_quality: 49.0
    developer_ergonomics: 23.8
    discoverability: 63.0
    governance: 0.0
    operational_transparency: 15.8
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 37.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dify/refs/heads/main/screenshots/dify-2026-06-20T180051.png
security:
- kind: authentication
  name: Dify Authentication
  slug: dify-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Dify Domain Security
  slug: dify-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Dify Trust Center
  slug: dify-trust-center
  summary_line: SOC 2
slug: dify
tags:
- Artificial Intelligence
- Backend-As-A-Service
- LLMOps
website: https://dify.ai/
---
