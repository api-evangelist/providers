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
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 38.5
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 39
  human_in_the_loop: 0
  name: Fini Agentic Access
  operation_count: 56
  slug: fini-agentic-access
  summary_line: 56 operations · 39 acting
api_count: 9
apis:
- description: The Agents API from Fini — 1 operation(s) for agents.
  name: Fini Agents API
  slug: fini-agents-api
- description: The Articles API from Fini — 6 operation(s) for articles.
  name: Fini Articles API
  slug: fini-articles-api
- description: The Conversations API from Fini — 3 operation(s) for conversations.
  name: Fini Conversations API
  slug: fini-conversations-api
- description: The Knowledge API from Fini — 5 operation(s) for knowledge.
  name: Fini Knowledge API
  slug: fini-knowledge-api
- description: The Knowledge Folders API from Fini — 4 operation(s) for knowledge folders.
  name: Fini Knowledge Folders API
  slug: fini-knowledge-folders-api
- description: The Prompts API from Fini — 3 operation(s) for prompts.
  name: Fini Prompts API
  slug: fini-prompts-api
- description: The Rules API from Fini — 6 operation(s) for rules.
  name: Fini Rules API
  slug: fini-rules-api
- description: The Sources API from Fini — 5 operation(s) for sources.
  name: Fini Sources API
  slug: fini-sources-api
- description: The Tags API from Fini — 5 operation(s) for tags.
  name: Fini Tags API
  slug: fini-tags-api
artifact_total: 15
common:
- group: company
  title: ''
  type: Website
  url: https://usefini.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.usefini.com/introduction
- group: docs
  title: ''
  type: Documentation
  url: https://docs.usefini.com/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://docs.usefini.com/en/api-reference/authentication
- group: company
  title: ''
  type: Blog
  url: https://www.usefini.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.usefini.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.usefini.com/company/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.usefini.com/security/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.usefini.com/security/privacy-policy
- group: auth
  title: ''
  type: Authentication
  url: authentication/fini-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/fini-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/fini-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/fini-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/fini-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/fini-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/fini-openapi-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/fini-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/fini-well-known.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/fini-agentic-access.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/fini-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/fini-trust-center.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/fini-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fini-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/fini-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/fini-vulnerability-disclosure.yml
created: '2026-07-17'
description: Fini AI provides self-improving AI agents for enterprise customer support across voice, chat, and email. Built on a RAGless retrieval engine, the Fini Agent Loop, a self-updating Knowledge Atlas, and Agentic Actions, Fini understands customer intent, retrieves the right data, and takes action — resolving up to 90% of support tickets at 99% accuracy. It is purpose-built for regulated industries such as fintech, banking, healthcare, insurance, and e-commerce, with PII redaction, audit trails, and guardrails. Fini exposes a public v2 REST API for managing agents, conversations, knowledge (sources, articles, folders), rules, tags, and prompts, and for driving the agent loop through its Generate Answer endpoint. Backed by Y Combinator (S22) and Matrix Partners.
image: https://mintcdn.com/fini/images/shared/logos/fini-light.png
layout: provider
mcp_servers:
- description: ''
  name: fini-mcp.yml
  slug: fini-mcpyml
modified: '2026-07-19'
name: Fini
nav: Providers
network: true
overview: 'Fini publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Agents API, Articles API, Conversations API, and 6 more. Tagged areas include Company, Artificial Intelligence, AI Agents, Customer Support, and Customer Experience.


  Fini''s developer surface includes documentation, API reference, engineering blog, pricing, signup flow, authentication, and 20 more developer resources.'
random_paper: 27
score:
  band: developing
  composite: 48.9
  delta: -0.9
  facets:
    commercial_clarity: 60.5
    contract_quality: 61.9
    developer_ergonomics: 40.8
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 10.5
  previous_composite: 49.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fini/refs/heads/main/screenshots/fini-2026-07-25T214529.png
security:
- kind: authentication
  name: Fini Authentication
  slug: fini-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Fini Domain Security
  slug: fini-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Fini Vulnerability Disclosure
  slug: fini-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Fini Trust Center
  slug: fini-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: fini
tags:
- Company
- Artificial Intelligence
- AI Agents
- Customer Support
- Customer Experience
- Knowledge Management
- Conversational AI
- Voice AI
- Helpdesk
- Regulated Industries
website: https://usefini.com
---
