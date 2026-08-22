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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.0
  scored_at: '2026-08-19'
api_count: 5
apis:
- description: The API Authentication API from Unitary AI — 1 operation(s) for api authentication.
  name: Unitary AI API Authentication API
  slug: unitary-ai-api-authentication-api
- description: The Detoxify API from Unitary AI — 2 operation(s) for detoxify.
  name: Unitary AI Detoxify API
  slug: unitary-ai-detoxify-api
- description: The Items & Characteristics API from Unitary AI — 4 operation(s) for items & characteristics.
  name: Unitary AI Items & Characteristics API
  slug: unitary-ai-items-characteristics-api
- description: The moderation API from Unitary AI — 1 operation(s) for moderation.
  name: Unitary AI moderation API
  slug: unitary-ai-moderation-api
- description: The Policy Classification API from Unitary AI — 6 operation(s) for policy classification.
  name: Unitary AI Policy Classification API
  slug: unitary-ai-policy-classification-api
artifact_total: 16
asyncapis:
- description: ''
  name: Unitary Ai Webhooks
  slug: unitary-ai-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Unitary content classification API Authentication API
  slug: open-unitary-ai-api-authentication-api
- collection_type: open
  name: Unitary content classification API Authentication Detoxify API
  slug: open-unitary-ai-detoxify-api
- collection_type: open
  name: Unitary content classification API Authentication Items & Characteristics API
  slug: open-unitary-ai-items-characteristics-api
- collection_type: open
  name: Unitary content classification API Authentication moderation API
  slug: open-unitary-ai-moderation-api
- collection_type: open
  name: Unitary content classification API Authentication Policy Classification API
  slug: open-unitary-ai-policy-classification-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/unitary-ai-content-classification-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.unitary.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.unitary.ai/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.unitary.ai/get-started/readme
- group: docs
  title: ''
  type: APIReference
  url: https://docs.unitary.ai/api-references/policy-classification
- group: auth
  title: ''
  type: Authentication
  url: authentication/unitary-ai-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://www.unitary.ai/blog
- group: operate
  title: ''
  type: Support
  url: https://www.unitary.ai/contact-us
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/unitaryai
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.unitary.ai/privacy-policy
- group: auth
  title: ''
  type: TrustCenter
  url: security/unitary-ai-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/unitary-ai-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/unitary-ai-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/unitary-ai-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/unitary-ai-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/unitary-ai-docs-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/unitary-ai-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/unitary-ai-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/unitary-ai-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/unitary-ai-conventions.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/unitary-ai-webhooks.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/unitary-ai-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Unitary is a London-based, Creandum-backed AI company that provides multimodal content classification and moderation as an API, analyzing video, image, audio, and text in context to detect harmful or policy-violating content at a scale of tens of millions of videos per day. The Unitary API at api.unitary.ai offers policy classification, granular Items and Characteristics signals, Detoxify text-toxicity scoring, and a Virtual Moderator endpoint that blends AI agents with human review, with results delivered by signed webhooks or polling. The company also maintains the popular open-source Detoxify Python library, and has expanded into AI Virtual Agents that automate manual workflows across insurance, financial services, healthcare, and marketplaces.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/unitary-ai.png
layout: provider
mcp_servers:
- description: ''
  name: unitary-ai-mcp.yml
  slug: unitary-ai-mcpyml
modified: '2026-07-21'
name: Unitary AI
nav: Providers
network: true
overview: 'Unitary AI publishes 5 APIs on the [APIs.io](https://apis.io/) network, including API Authentication API, Detoxify API, Items & Characteristics API, and 2 more. Tagged areas include Company, Saas, Content Moderation, Trust And Safety, and Artificial Intelligence.


  The Unitary AI catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Unitary AI''s developer surface includes documentation, getting-started guide, API reference, authentication, engineering blog, support, and 17 more developer resources.'
random_paper: 19
score:
  band: thin
  composite: 33.9
  delta: -5.6
  facets:
    access_clarity: 18.4
    commercial_clarity: 18.4
    contract_governance: 16.7
    contract_quality: 58.3
    developer_ergonomics: 20.8
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 10.5
  previous_composite: 39.5
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
security:
- kind: authentication
  name: Unitary Ai Authentication
  slug: unitary-ai-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Unitary Ai Domain Security
  slug: unitary-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Unitary Ai Trust Center
  slug: unitary-ai-trust-center
  summary_line: trust center published
slug: unitary-ai
tags:
- Company
- Saas
- Content Moderation
- Trust And Safety
- Artificial Intelligence
- Machine Learning
- Computer Vision
- Video
- Virtual Agents
website: https://www.unitary.ai/
---
