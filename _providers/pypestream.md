---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 37.8
  scored_at: '2026-08-26'
api_count: 7
apis:
- description: Programmatic access to Pypestream automation, conversation and agent data. Retrieves single and multiple agent records, session metadata and conversation transcripts over a bounded time window. Availa
  name: Pypestream Reporting API
  slug: reporting-api
- description: Builds integrations between Pypestream and a contact center. Escalates conversations from a Pype or a messaging channel to a live agent, checks agent availability and wait time, exchanges messages and
  name: Pypestream Contact Center API
  slug: contact-center-api
- description: The middleware layer behind the Contact Center API, exposing Settings, Integrations and Conversations operations. The published contract declares an empty servers[] block; the sibling Contact Center A
  name: Pypestream Middleware API
  slug: middleware-api
- description: Lets developers build interfaces and connect messaging channels so end users can engage a Pypestream microapp. Creates an anonymous user session, starts and ends an engagement and sends messages, pair
  name: Pypestream Engagement API
  slug: engagement-api
- description: Product analytics over Pypestream datasets -- events, persons, cohorts, actions, annotations, dashboards, insights (trend, funnel, retention, path), KPIs and property definitions -- plus batch exports
  name: Pypestream Analytics API
  slug: analytics-api
- description: The client-side JavaScript SDK for embedding the Pypestream conversational AI chat interface in a web page, in window or inline mode. Pypestream documents the SDK's methods, configuration and event ha
  name: Pypestream JavaScript SDK API
  slug: javascript-sdk
- description: A single-operation contract for aggregate dashboard report data. Published in Pypestream's own API registry, but every servers[] entry points at an unbranded Vercel preview deployment (analytics-eight
  name: Pypestream Insights API
  slug: insights-api
artifact_total: 16
asyncapis:
- description: ''
  name: Pypestream Contact Center Webhooks
  slug: pypestream-contact-center-webhooks
- description: Bidirectional event stream backing the Pypestream Engagement API. The client creates an anonymous user, opens a WebSocket, joins the chat channel `chat:{CHAT_ID}`, starts the engagement over REST, and
  name: Pypestream Engagement API WebSocket
  slug: pypestream-engagement-api-asyncapi
common:
- group: company
  title: ''
  type: Website
  url: https://www.pypestream.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.pypestream.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.pypestream.com/docs/welcome
- group: docs
  title: ''
  type: APIReference
  url: https://developers.pypestream.com/reference/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.pypestream.com/reference/overview
- group: auth
  title: ''
  type: Authentication
  url: authentication/pypestream-authentication.yml
- group: operate
  title: ''
  type: Support
  url: https://support.pypestream.com/
- group: company
  title: ''
  type: Blog
  url: https://www.pypestream.ai/resources
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pypestream
- group: operate
  title: ''
  type: StatusPage
  url: https://status.pypestream.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.pypestream.ai/privacy
- group: start
  title: ''
  type: SignUp
  url: https://platform.pypestream.com/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/pypestream-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/pypestream-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/pypestream-tool-crosswalk.yml
- group: build
  title: ''
  type: Packages
  url: packages/pypestream-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/pypestream-packages.yml
- group: design
  title: ''
  type: Components
  url: components/pypestream-components.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/pypestream-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/pypestream-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/pypestream-trust-center.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/pypestream-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pypestream-domain-security.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/pypestream-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/pypestream-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/pypestream-conventions.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/pypestream-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/pypestream-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/pypestream-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/pypestream-plans-pricing.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-26'
description: Pypestream is a New York based enterprise conversational and agentic AI company, founded in 2015, whose platform deploys voice and chat AI agents ("Pypes" and microapps) into Fortune 500 contact centers across insurance, health insurance, telecom and travel. Pypestream publishes a self-serve developer portal at developers.pypestream.com carrying six distinct OpenAPI-described surfaces -- a Reporting API for conversation and agent data, a Contact Center API and Middleware API for live agent escalation, an Engagement API with a Phoenix Channels WebSocket event stream for embedding chat in any channel, an Analytics API for product analytics and warehouse batch exports, and an OpenAPI-documented client-side JavaScript SDK for embedding the chat widget.
image: https://www.pypestream.ai/pypestream-logo-black.webp
layout: provider
mcp_servers:
- description: ''
  name: Pypestream Documentation MCP Server
  slug: pypestream-documentation-mcp-server
modified: '2026-08-26'
name: Pypestream
nav: Providers
network: true
overview: 'Pypestream publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Reporting API, Contact Center API, Middleware API, and 4 more. Tagged areas include Company, Conversational AI, Agentic AI, Contact Center, and Customer Service.


  The Pypestream catalog on APIs.io includes 2 event-driven AsyncAPI specifications.


  Pypestream''s developer surface includes documentation, API reference, getting-started guide, authentication, support, engineering blog, signup flow, and 24 more developer resources.'
plans:
- name: Pypestream Plans Pricing
  plan_count: 0
  slug: pypestream-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 2
  name: Pypestream Rate Limits
  slug: pypestream-rate-limits
score:
  band: developing
  composite: 43.8
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 16.7
    contract_quality: 55.2
    developer_ergonomics: 51.8
    discoverability: 83.3
    governance: 16.7
    operational_transparency: 47.4
  provenance:
    conformance: derived
    mcp: first-party
    skills: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
security:
- kind: authentication
  name: Pypestream Authentication
  slug: pypestream-authentication
  summary_line: apiKey/http · 4 schemes
- kind: domain-security
  name: Pypestream Domain Security
  slug: pypestream-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Pypestream Vulnerability Disclosure
  slug: pypestream-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Pypestream Trust Center
  slug: pypestream-trust-center
  summary_line: read_from_source, claims, note
slug: pypestream
tags:
- Company
- Conversational AI
- Agentic AI
- Contact Center
- Customer Service
- Customer Engagement
- Chatbots
- Voice AI
- Messaging
- Analytics
- Enterprise Software
website: https://www.pypestream.ai/
---
