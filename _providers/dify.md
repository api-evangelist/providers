---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
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
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 10
  human_in_the_loop: 3
  name: Dify Agentic Access
  operation_count: 13
  slug: dify-agentic-access
  summary_line: 13 operations · 10 acting · 3 human-in-the-loop
api_count: 1
apis:
- description: Dify is an open-source platform for building AI applications. We combine Backend-as-a-Service and LLMOps to streamline the development of generative AI solutions, making it accessible to both develope
  name: Dify
  slug: dify
- baseURL: https://api.dify.ai/v1
  baseurl_source: spec
  description: The Chat API from Dify — 2 operation(s) for chat.
  name: Dify Chat API
  slug: dify-chat-api
- baseURL: https://api.dify.ai/v1
  baseurl_source: spec
  description: The Completion API from Dify — 2 operation(s) for completion.
  name: Dify Completion API
  slug: dify-completion-api
- baseURL: https://api.dify.ai/v1
  baseurl_source: spec
  description: The Conversations API from Dify — 3 operation(s) for conversations.
  name: Dify Conversations API
  slug: dify-conversations-api
- baseURL: https://api.dify.ai/v1
  baseurl_source: spec
  description: The Datasets API from Dify — 2 operation(s) for datasets.
  name: Dify Datasets API
  slug: dify-datasets-api
- baseURL: https://api.dify.ai/v1
  baseurl_source: spec
  description: The Files API from Dify — 1 operation(s) for files.
  name: Dify Files API
  slug: dify-files-api
- baseURL: https://api.dify.ai/v1
  baseurl_source: spec
  description: The Workflows API from Dify — 3 operation(s) for workflows.
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
overview: 'Dify publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Chat API, Completion API, Conversations API, and 3 more. Tagged areas include Artificial Intelligence, Backend-as-a-Service, and LLMOps.


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
  composite: 35.5
  coverage:
    artifact_dirs: 11
    catalog_earned: 36.0
    catalog_earned_first_party: 0.0
    catalog_gap: 79.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 55.3
    commercial_clarity: 55.3
    contract_governance: 0.0
    contract_quality: 47.6
    developer_ergonomics: 23.8
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 15.8
  previous_composite: 35.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.18.3
  scored_at: '2026-09-04'
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
- Backend-as-a-Service
- LLMOps
website: https://dify.ai/
---
