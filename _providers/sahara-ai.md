---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.3
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Sahara Ai Agentic Access
  operation_count: 4
  slug: sahara-ai-agentic-access
  summary_line: 4 operations · 1 acting
api_count: 2
apis:
- description: Discover models and compute providers available on the network.
  name: Sahara AI Discovery API
  slug: sahara-ai-discovery-api
- description: OpenAI-compatible chat completion inference.
  name: Sahara AI Inference API
  slug: sahara-ai-inference-api
artifact_total: 9
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Sahara AI Compute Discovery API
  slug: open-sahara-ai-discovery-api
- collection_type: open
  name: Sahara AI Compute Discovery Inference API
  slug: open-sahara-ai-inference-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/sahara-ai-compute-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://saharaai.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.saharaai.com/developer-platform/main/explore
- group: docs
  title: ''
  type: Documentation
  url: https://docs.saharaai.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.saharaai.com/developer-docs-ai-developer-portal/api-documentation
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.saharaai.com/developer-docs-ai-developer-portal/quick-start-guide
- group: company
  title: ''
  type: Blog
  url: https://saharaai.com/blog
- group: operate
  title: ''
  type: Support
  url: https://saharaai.com/community
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SaharaAI-Agents
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.saharaai.com/developer-docs-ai-developer-portal/credits-and-billing
- group: start
  title: ''
  type: SignUp
  url: https://app.saharaai.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://saharaai.com/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://saharaai.com/legal/privacy-policy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sahara-ai-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/sahara-ai-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/sahara-ai-mcp.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/sahara-ai-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/sahara-ai-conventions.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sahara-ai-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sahara-ai-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sahara-ai-authentication.yml
created: '2026-07-17'
description: 'Sahara AI is a decentralized AI platform (backed by Pantera Capital) building infrastructure for the agentic economy: an AI Developer Platform for building agents, managing datasets, and accessing compute; an AI Marketplace for publishing and monetizing AI solutions; a Data Services Platform for collecting, labeling, and validating training data; consumer agents such as Sorin (autonomous trading); and the Sahara blockchain with the $SAHARA token for settlement and governance. Its developer-facing surface is an OpenAI-compatible Compute API that routes inference across multiple upstream providers (OpenAI, Lepton, Together, and others) alongside model- and provider-discovery endpoints, authenticated with an API key.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sahara-ai.png
layout: provider
mcp_servers:
- description: ''
  name: sahara-ai-mcp.yml
  slug: sahara-ai-mcpyml
modified: '2026-07-21'
name: Sahara AI
nav: Providers
network: true
overview: 'Sahara AI publishes 2 APIs on the [APIs.io](https://apis.io/) network: Discovery API and Inference API. Tagged areas include Company, Crypto, Artificial Intelligence, Machine Learning, and Agents.


  Sahara AI''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, signup flow, and 15 more developer resources.'
random_paper: 126
score:
  band: developing
  composite: 45.5
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 62.7
    developer_ergonomics: 56.0
    discoverability: 75.9
    governance: 11.5
    operational_transparency: 5.3
  previous_composite: 45.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
security:
- kind: authentication
  name: Sahara Ai Authentication
  slug: sahara-ai-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Sahara Ai Domain Security
  slug: sahara-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sahara-ai
tags:
- Company
- Crypto
- Artificial Intelligence
- Machine Learning
- Agents
- Compute
- Blockchain
- Inference
- Data
website: https://saharaai.com/
---
