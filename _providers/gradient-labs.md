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
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Gradient Labs Agentic Access
  operation_count: 11
  slug: gradient-labs-agentic-access
  summary_line: 11 operations · 10 acting
api_count: 1
apis:
- description: Define and execute business tools the AI agent can call.
  name: Gradient Labs Actions & Tools API
  slug: gradient-labs-actions-tools-api
- description: Start, read, and manage the lifecycle of AI-agent conversations.
  name: Gradient Labs Conversations API
  slug: gradient-labs-conversations-api
- description: Assign conversations between the AI agent and human participants.
  name: Gradient Labs Hand-off API
  slug: gradient-labs-hand-off-api
- description: Manage knowledge-base articles that ground the AI agent.
  name: Gradient Labs Knowledge API
  slug: gradient-labs-knowledge-api
- description: Add inbound messages to a conversation.
  name: Gradient Labs Messages API
  slug: gradient-labs-messages-api
- description: The Gradient Labs API API from Gradient Labs — 0 operation(s) for gradient labs api.
  name: Gradient Labs Gradient Labs API
  slug: gradient-labs-gradient-labs-api-api
artifact_total: 19
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Gradient Labs Actions & Tools API
  slug: open-gradient-labs-actions-tools-api
- collection_type: open
  name: Gradient Labs Actions & Tools Conversations API
  slug: open-gradient-labs-conversations-api
- collection_type: open
  name: Gradient Labs Actions & Tools Hand-off API
  slug: open-gradient-labs-hand-off-api
- collection_type: open
  name: Gradient Labs Actions & Tools Knowledge API
  slug: open-gradient-labs-knowledge-api
- collection_type: open
  name: Gradient Labs Actions & Tools Messages API
  slug: open-gradient-labs-messages-api
- collection_type: open
  name: Gradient Labs API
  slug: open-gradient-labs
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/gradient-labs-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gradient-labs-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/gradient-labs-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/gradient-labs-ai
- group: company
  title: ''
  type: Website
  url: https://www.gradient-labs.ai
- group: docs
  title: ''
  type: Documentation
  url: https://api-docs.gradient-labs.ai/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/gradientlabs-ai
- group: commercial
  title: ''
  type: Plans
  url: plans/gradient-labs-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/gradient-labs-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/gradient-labs-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://blog.gradient-labs.ai/feed
created: '2026-07-01'
description: Gradient Labs builds "Otto", an AI customer support agent that autonomously handles complex, end-to-end support conversations for regulated and financial services businesses. The API lets you start and drive conversations, stream customer messages, hand off to human agents, execute business actions/tools, and manage the knowledge base the agent reasons over, with signed webhooks delivering the agent's outbound messages and events.
finops:
- name: Gradient Labs Finops
  service_category: AI and Machine Learning
  slug: gradient-labs-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gradient-labs.png
layout: provider
modified: '2026-07-01'
name: Gradient Labs
nav: Providers
network: true
overview: 'Gradient Labs publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Actions & Tools API, Conversations API, Hand-off API, and 3 more. Tagged areas include Artificial Intelligence, Customer-Support, AI Agent, Conversations, and Financial-Services.


  Gradient Labs'' developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Gradient Labs Plans Pricing
  plan_count: 1
  slug: gradient-labs-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 2
  name: Gradient Labs Rate Limits
  slug: gradient-labs-rate-limits
score:
  band: emerging
  composite: 23.0
  coverage:
    artifact_dirs: 10
    catalog_gap: 59.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 13.9
    developer_ergonomics: 19.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 23.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 5
      marker_coverage: 100.0
      total: 5
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gradient-labs/refs/heads/main/screenshots/gradient-labs-2026-07-25T220209.png
security:
- kind: authentication
  name: Gradient Labs Authentication
  slug: gradient-labs-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Gradient Labs Domain Security
  slug: gradient-labs-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: gradient-labs
tags:
- Artificial Intelligence
- Customer-Support
- AI Agent
- Conversations
- Financial-Services
- Regulated
website: https://www.gradient-labs.ai
---
