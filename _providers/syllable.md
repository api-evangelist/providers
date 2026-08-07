---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: flavored
    agent_skills: true
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 56.8
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 98
  human_in_the_loop: 0
  name: Syllable Agentic Access
  operation_count: 176
  slug: syllable-agentic-access
  summary_line: 176 operations · 98 acting
api_count: 1
apis:
- description: 'The Syllable Platform SDK REST API for building and operating AI agents across voice, SMS, email and chat channels. 176 operations across 107 paths cover agent configuration, prompt versioning, tools '
  name: Syllable Platform SDK API
  slug: syllable-platform-sdk
artifact_total: 7
asyncapis:
- description: ''
  name: Syllable Outbound Webhooks
  slug: syllable-outbound-webhooks
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/syllable-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/syllable-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/syllable-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://syllable.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.syllable.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.syllable.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.syllable.ai/api-reference/agents/agent-list
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.syllable.ai/sdk-guides/Overview
- group: operate
  title: ''
  type: Support
  url: https://syllable.ai/contact-us/
- group: company
  title: ''
  type: Blog
  url: https://syllable.ai/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/asksyllable
- group: commercial
  title: ''
  type: Pricing
  url: https://syllable.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://syllable.cloud/sign-up
- group: start
  title: ''
  type: Login
  url: https://syllable.cloud/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://syllable.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://syllable.ai/legal/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://syllable.statuspage.io
- group: auth
  title: ''
  type: Compliance
  url: https://trust.syllable.ai
- group: operate
  title: ''
  type: ChangeLog
  url: https://syllable.ai/release-notes/
- group: build
  title: ''
  type: Packages
  url: packages/syllable-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/syllable-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/syllable-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/syllable-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/syllable-tool-crosswalk.yml
- group: other
  title: ''
  type: AgentCard
  url: a2a/syllable-a2a.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/syllable-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/syllable-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/syllable-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/syllable-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/syllable-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/syllable-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/syllable-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/syllable-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/syllable-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/syllable-components.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/syllable-outbound-webhooks.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/syllable-changelog.yml
created: '2026-08-05'
description: Syllable is a Mountain View, California company (founded 2017) that operates an agentic platform for building, deploying and optimizing AI voice, SMS, email, web-chat and WhatsApp agents, with a strong focus on healthcare patient experience and contact-center automation. The Syllable Platform SDK exposes a REST API at api.syllable.cloud covering agents, prompts, tools, services, data sources, channels and channel targets, sessions and transcripts, outbound campaigns and batches, insights workflows, directory, dashboards, incidents, organizations, roles, permissions and users. First-party TypeScript and Python SDKs, a Go CLI, a documentation MCP server and a published A2A agent card make it an unusually agent-forward developer surface.
image: https://syllable.ai/figma/assets/syllable-social-share.png
layout: provider
mcp_servers:
- description: ''
  name: syllable-mcp.yml
  slug: syllable-mcpyml
modified: '2026-08-05'
name: Syllable
nav: Providers
network: true
overview: 'Syllable publishes 1 API on the [APIs.io](https://apis.io/) network: Platform SDK API. Tagged areas include Company, Artificial Intelligence, AI Agents, Voice, and Conversational AI.


  The Syllable catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Syllable''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 31 more developer resources.'
random_paper: 65
score:
  band: strong
  composite: 60.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 66.7
    developer_ergonomics: 87.0
    discoverability: 87.0
    governance: 20.8
    operational_transparency: 44.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 41.7
  schema_version: 0.9.1
  scored_at: '2026-08-06'
security:
- kind: authentication
  name: Syllable Authentication
  slug: syllable-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Syllable Domain Security
  slug: syllable-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Syllable Trust Center
  slug: syllable-trust-center
  summary_line: SOC 2 Type 2, HIPAA, HITRUST, GDPR
slug: syllable
tags:
- Company
- Artificial Intelligence
- AI Agents
- Voice
- Conversational AI
- Contact Center
- Healthcare
- Telephony
- SMS
- Customer Experience
website: https://syllable.ai/
---
