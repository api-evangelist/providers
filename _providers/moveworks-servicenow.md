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
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 52.0
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Moveworks Servicenow Agentic Access
  operation_count: 5
  slug: moveworks-servicenow-agentic-access
  summary_line: 5 operations
api_count: 1
apis:
- description: Exported AI Assistant interaction records
  name: Moveworks (ServiceNow) Records API
  slug: moveworks-servicenow-records-api
artifact_total: 9
asyncapis:
- description: ''
  name: Moveworks Servicenow Webhooks
  slug: moveworks-servicenow-webhooks
collections:
- collection_type: postman
  name: Moveworks Data Records API
  slug: postman-moveworks-servicenow-records-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/moveworks-servicenow/overview
- group: company
  title: ''
  type: Website
  url: https://www.moveworks.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.moveworks.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.moveworks.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.moveworks.com/api-reference/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.moveworks.com/ai-assistant/getting-started/welcome-to-moveworks
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.moveworks.com/
- group: operate
  title: ''
  type: Support
  url: https://community.moveworks.com/
- group: company
  title: ''
  type: Blog
  url: https://www.moveworks.com/us/en/resources/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/moveworks
- group: operate
  title: ''
  type: Roadmap
  url: https://docs.moveworks.com/ai-assistant/getting-started/roadmap-release-notes
- group: commercial
  title: ''
  type: Pricing
  url: https://www.moveworks.com/us/en/pricing
- group: start
  title: ''
  type: SignUp
  url: https://developer.moveworks.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.moveworks.com/us/en/legal/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.moveworks.com/us/en/legal/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.moveworks.com
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/moveworks-servicenow-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/moveworks-servicenow-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://help.moveworks.com/docs/api-versioning-policy
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/moveworks-servicenow-webhooks.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/moveworks-servicenow-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/moveworks-servicenow-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/moveworks-servicenow-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.moveworks.com/us/en/platform/security
- group: auth
  title: ''
  type: TrustCenter
  url: security/moveworks-servicenow-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.moveworks.com/us/en/platform/security
- group: design
  title: ''
  type: Conformance
  url: conformance/moveworks-servicenow-conformance.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/moveworks-servicenow-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/moveworks-servicenow-agentic-access.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/moveworks-servicenow-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/moveworks-servicenow-well-known.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/moveworks-servicenow-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/moveworks-servicenow-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/moveworks-servicenow-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/moveworks-servicenow-sandbox.yml
- group: build
  title: ''
  type: Packages
  url: packages/moveworks-servicenow-packages.yml
created: '2026-07-17'
description: Moveworks is an enterprise AI assistant / agentic automation platform (acquired by ServiceNow) that lets employees resolve IT, HR, and other requests in natural language across Slack, Microsoft Teams, and 100+ enterprise systems. Its developer platform — Agent Studio, Creator Studio, and the AI Agent Marketplace — lets teams build and deploy plugins with triggers, slots, and actions, and connect to systems such as ServiceNow, Jira, Workday, and Salesforce. Moveworks exposes Bearer-authenticated REST APIs including a read-only OData Data API for exporting conversation and interaction data, an Events API, a Conversations API, webhook listeners, and customer-hosted gateways, plus an official hosted MCP server for its documentation. Surfaced originally as a Bain Capital Ventures portfolio company and enriched from Moveworks' public developer documentation.
image: https://github.com/moveworks.png
layout: provider
mcp_servers:
- description: ''
  name: moveworks-servicenow-mcp.yml
  slug: moveworks-servicenow-mcpyml
modified: '2026-07-20'
name: Moveworks (ServiceNow)
nav: Providers
network: true
overview: 'Moveworks (ServiceNow) publishes 1 API on the [APIs.io](https://apis.io/) network: Records API. Tagged areas include Company, Ai Infrastructure, AI Assistant, Agentic AI, and Enterprise Automation.


  The Moveworks (ServiceNow) catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Moveworks (ServiceNow)''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 30 more developer resources.'
random_paper: 64
score:
  band: strong
  composite: 64.4
  delta: 2.1
  facets:
    commercial_clarity: 60.5
    contract_quality: 70.3
    developer_ergonomics: 73.4
    discoverability: 87.0
    governance: 20.8
    operational_transparency: 68.4
  previous_composite: 62.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Moveworks Servicenow Authentication
  slug: moveworks-servicenow-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Moveworks Servicenow Domain Security
  slug: moveworks-servicenow-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Moveworks Servicenow Vulnerability Disclosure
  slug: moveworks-servicenow-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Moveworks Servicenow Trust Center
  slug: moveworks-servicenow-trust-center
  summary_line: SOC 2 Type 2, ISO 27001, HIPAA, GDPR, FedRAMP
slug: moveworks-servicenow
tags:
- Company
- Ai Infrastructure
- AI Assistant
- Agentic AI
- Enterprise Automation
- ITSM
- Conversational AI
- Developer Platform
website: https://www.moveworks.com/
---
