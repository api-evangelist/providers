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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 50.2
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 19
  human_in_the_loop: 1
  name: Brainfish Agentic Access
  operation_count: 27
  slug: brainfish-agentic-access
  summary_line: 27 operations · 19 acting · 1 human-in-the-loop
api_count: 9
apis:
- description: AI agent operations for answer generation and streaming
  name: Brainfish Agents API
  slug: brainfish-agents-api
- description: Conversation thread analytics with filtering and pagination
  name: Brainfish Analytics API
  slug: brainfish-analytics-api
- description: Authentication and token validation operations
  name: Brainfish Authentication API
  slug: brainfish-authentication-api
- description: Catalog management operations. Create catalogs and sync content programmatically via the API.
  name: Brainfish Catalogs API
  slug: brainfish-catalogs-api
- description: Collection management operations including create, read, update, list, and delete
  name: Brainfish Collections API
  slug: brainfish-collections-api
- description: Conversation operations including follow-up question generation
  name: Brainfish Conversations API
  slug: brainfish-conversations-api
- description: Document management operations including create, read, update, list, and delete
  name: Brainfish Documents API
  slug: brainfish-documents-api
- description: Chat session search, detail, timeline, and AI-powered insights. A "session" is a chat conversation keyed by conversationId.
  name: Brainfish Sessions API
  slug: brainfish-sessions-api
- description: User-scoped operations. Generate answers personalized to a specific external/platform user with automatic attribute-based collection filtering.
  name: Brainfish Users API
  slug: brainfish-users-api
arazzos:
- description: Generate a cited AI answer for an end-user question, then generate suggested follow-up questions.
  name: Generate an answer and follow-up questions
  slug: brainfish-answer-and-followups
- description: Create a catalog, sync content into it, then read back its status.
  name: Create and sync an API catalog
  slug: brainfish-catalog-sync
- description: Validate the token, create a knowledge-base collection, then create a document inside it.
  name: Create a collection and add a document
  slug: brainfish-create-collection-and-document
artifact_total: 28
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Brainfish Public Agents API
  slug: open-brainfish-agents-api
- collection_type: open
  name: Brainfish Public Agents Analytics API
  slug: open-brainfish-analytics-api
- collection_type: open
  name: Brainfish Public Agents Authentication API
  slug: open-brainfish-authentication-api
- collection_type: open
  name: Brainfish Public Agents Catalogs API
  slug: open-brainfish-catalogs-api
- collection_type: open
  name: Brainfish Public Agents Collections API
  slug: open-brainfish-collections-api
- collection_type: open
  name: Brainfish Public Agents Conversations API
  slug: open-brainfish-conversations-api
- collection_type: open
  name: Brainfish Public Agents Documents API
  slug: open-brainfish-documents-api
- collection_type: open
  name: Brainfish Public Agents Sessions API
  slug: open-brainfish-sessions-api
- collection_type: open
  name: Brainfish Public Agents Users API
  slug: open-brainfish-users-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/brainfish-public-api-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.brainfi.sh
- group: docs
  title: ''
  type: Documentation
  url: https://docs.brainfi.sh
- group: docs
  title: ''
  type: APIReference
  url: https://docs.brainfi.sh/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://help.brainfi.sh
- group: operate
  title: ''
  type: Support
  url: https://help.brainfi.sh
- group: agent
  title: ''
  type: MCPServer
  url: mcp/brainfish-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Packages
  url: packages/brainfish-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/brainfish-packages.yml
- group: design
  title: ''
  type: Components
  url: components/brainfish-components.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/brainfish-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/brainfish-llms.txt
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/brainfish-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/brainfish-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.brainfi.sh
- group: auth
  title: ''
  type: TrustCenter
  url: security/brainfish-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.brainfi.sh/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/brainfish-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/brainfish-ai
- group: company
  title: ''
  type: Blog
  url: https://www.brainfishai.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.brainfishai.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.brainfi.sh
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.brainfishai.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.brainfishai.com/privacy-policy
- group: company
  title: ''
  type: Website
  url: https://www.brainfishai.com
created: '2026-07-17'
description: Brainfish is an AI product-support platform for B2B SaaS companies, built in Sydney and deployed globally with US/EU/AU data residency. Its AI support agents resolve customer tickets across chat, email, in-product, Slack and Teams, grounding every answer in the company's real product knowledge rather than training on customer data. Brainfish exposes a REST Public API (https://api.brainfi.sh) to programmatically manage the knowledge base (collections, documents, catalogs), generate cited AI answers and follow-up questions, and pull session analytics, plus a remote Model Context Protocol (MCP) server and an embeddable browser widget suite. Backed by Prosus Ventures.
image: https://www.brainfishai.com/og-default.png
layout: provider
mcp_servers:
- description: ''
  name: brainfish-mcp.yml
  slug: brainfish-mcpyml
modified: '2026-07-18'
name: Brainfish
nav: Providers
network: true
overview: 'Brainfish publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Agents API, Analytics API, Authentication API, and 6 more. Tagged areas include Company, AI, Customer Support, Knowledge Base, and Help Desk.


  Brainfish''s developer surface includes documentation, API reference, getting-started guide, support, changelog, engineering blog, pricing, and 19 more developer resources.'
random_paper: 56
rate_limits:
- limit_count: 2
  name: Brainfish Rate Limits
  slug: brainfish-rate-limits
score:
  band: strong
  composite: 58.9
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 63.7
    developer_ergonomics: 58.2
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 57.9
  previous_composite: 58.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: first-party
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/brainfish/refs/heads/main/screenshots/brainfish-2026-07-25T203705.png
security:
- kind: authentication
  name: Brainfish Authentication
  slug: brainfish-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Brainfish Domain Security
  slug: brainfish-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Brainfish Trust Center
  slug: brainfish-trust-center
  summary_line: SOC 2, ISO 27001
slug: brainfish
tags:
- Company
- AI
- Customer Support
- Knowledge Base
- Help Desk
- Agents
- Support Automation
- SaaS
website: https://www.brainfishai.com
---
