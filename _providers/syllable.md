---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.9
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 98
  human_in_the_loop: 0
  name: Syllable Agentic Access
  operation_count: 176
  slug: syllable-agentic-access
  summary_line: 176 operations · 98 acting
api_count: 1
apis:
- description: 'Operations related to agent configuration. When a user interacts with the Syllable system, they do so by communicating with an agent. An agent is linked to a prompt, a custom message, and one or more '
  name: Syllable Agents API
  slug: syllable-agents-api
- description: Operations for testing agents with live text. These endpoints allow sending messages to an agent and receiving its responses.
  name: Syllable Agents.test API
  slug: syllable-agents-test-api
- description: The bridge_phrases API from Syllable — 2 operation(s) for bridge_phrases.
  name: Syllable Bridge Phrases API
  slug: syllable-bridge-phrases-api
- description: Operations related to channel configuration. A channel is an organization-level point of communication, like a phone number or a web chat. A channel can be associated with an agent by creating a chann
  name: Syllable Channels API
  slug: syllable-channels-api
- description: 'Operations related to channel target configuration. A channel target links a channel to an agent, allowing users to communicate with the agent through that channel. For more information, see [Console '
  name: Syllable Channels.targets API
  slug: syllable-channels-targets-api
- description: Operations related to Twilio channel configuration.
  name: Syllable Channels.twilio API
  slug: syllable-channels-twilio-api
- description: Operations related to setting up phone numbers in Twilio for use in channels.
  name: Syllable Channels.twilio.numbers API
  slug: syllable-channels-twilio-numbers-api
- description: The conversation-config API from Syllable — 1 operation(s) for conversation-config.
  name: Syllable Conversation Config API
  slug: syllable-conversation-config-api
- description: Operations related to conversations. A conversation is a record of messages between a user and an agent, and is composed of one or more sessions.
  name: Syllable Conversations API
  slug: syllable-conversations-api
- description: Operations related to custom message configuration. A custom message is a pre-configured message delivered by an agent as a greeting at the beginning of a conversation. Multiple agents can use the sam
  name: Syllable Custom Messages API
  slug: syllable-custom-messages-api
- description: Operations related to dashboards. Currently the API/SDK only supports fetching basic information about dashboards.
  name: Syllable Dashboards API
  slug: syllable-dashboards-api
- description: 'Operations related to data sources. A data source is a blob of text that can be made available to an agent''s general info tools to provide more context to the agent when generating its responses. For '
  name: Syllable Data Sources API
  slug: syllable-data-sources-api
- description: Operations related to directory
  name: Syllable Directory API
  slug: syllable-directory-api
- description: Operations related to events. An event represents a specific occurrence during a session. Currently the API/SDK only supports fetching logged events.
  name: Syllable Events API
  slug: syllable-events-api
- description: Operations related to incidents.
  name: Syllable Incidents API
  slug: syllable-incidents-api
- description: Operations related to insights results. An insight is a tool that processes conversation data to extract information and generate reports.
  name: Syllable Insights API
  slug: syllable-insights-api
- description: Operations related to insights upload folders. An insight folder is used to upload call recordings for insight workflow analysis.
  name: Syllable Insights.folders API
  slug: syllable-insights-folders-api
- description: Operations related to insights tool configurationss. An insight is a tool that processes conversation data to extract information and generate reports.
  name: Syllable Insights.tools API
  slug: syllable-insights-tools-api
- description: Operations related to insights workflows. An workflow is series of tool invocations that processes conversation data to extract information and generate reports.
  name: Syllable Insights.workflows API
  slug: syllable-insights-workflows-api
- description: Operations related to language groups. A language group is a collection of language, voice, and DTMF configuration that can be linked to an agent to define the languages and voices it supports. For mo
  name: Syllable Language Groups API
  slug: syllable-language-groups-api
- description: Operations related to organizations.
  name: Syllable Organizations API
  slug: syllable-organizations-api
- description: The organizations.sip_ip_ranges API from Syllable — 2 operation(s) for organizations.sip_ip_ranges.
  name: Syllable Organizations.sip Ip Ranges API
  slug: syllable-organizations-sip-ip-ranges-api
- description: Operations related to outbound campaign batches
  name: Syllable Outbound.batches API
  slug: syllable-outbound-batches-api
- description: Operations related to outbound message campaigns
  name: Syllable Outbound.campaigns API
  slug: syllable-outbound-campaigns-api
- description: Operations related to permissions. A permission is a specific capability or access level granted to a user within the Syllable system. Permissions are used to control access to various features and fu
  name: Syllable Permissions API
  slug: syllable-permissions-api
- description: Operations related to prompts. A prompt defines the behavior of an agent by delivering instructions to the LLM about how the agent should behave. A prompt can be linked to one or more agents. A prompt
  name: Syllable Prompts API
  slug: syllable-prompts-api
- description: The pronunciations API from Syllable — 3 operation(s) for pronunciations.
  name: Syllable Pronunciations API
  slug: syllable-pronunciations-api
- description: Operations related to roles. A role is a collection of permissions that can be assigned to users to control their access to various features within the Syllable system.
  name: Syllable Roles API
  slug: syllable-roles-api
- description: Operations related to service configuration. A service is a collection of tools. You can specify an authentication method and values on a service, and any linked tools will use that auth information t
  name: Syllable Services API
  slug: syllable-services-api
- description: The session_debug API from Syllable — 3 operation(s) for session_debug.
  name: Syllable Session Debug API
  slug: syllable-session-debug-api
- description: Operations related to labeling sessions with evaluations of quality and descriptions of issues the user encountered or other details. For more information, see [Console docs](https://docs.syllable.ai/
  name: Syllable Session Labels API
  slug: syllable-session-labels-api
- description: Operations related to sessions. A session is a building block of a conversation. For more information, see [Console docs](https://docs.syllable.ai/workspaces/Sessions).
  name: Syllable Sessions API
  slug: syllable-sessions-api
- description: The sessions.full-summary API from Syllable — 1 operation(s) for sessions.full-summary.
  name: Syllable Sessions.full Summary API
  slug: syllable-sessions-full-summary-api
- description: The sessions.latency API from Syllable — 1 operation(s) for sessions.latency.
  name: Syllable Sessions.latency API
  slug: syllable-sessions-latency-api
- description: The sessions.timeline API from Syllable — 1 operation(s) for sessions.timeline.
  name: Syllable Sessions.timeline API
  slug: syllable-sessions-timeline-api
- description: The sessions.transcript API from Syllable — 1 operation(s) for sessions.transcript.
  name: Syllable Sessions.transcript API
  slug: syllable-sessions-transcript-api
- description: The takeouts API from Syllable — 3 operation(s) for takeouts.
  name: Syllable Takeouts API
  slug: syllable-takeouts-api
- description: 'Operations related to tool configuration. A tool is a function that an agent can call to perform actions like accessing databases, making API calls, or processing data. For an agent to have access to '
  name: Syllable Tools API
  slug: syllable-tools-api
- description: The users API from Syllable — 4 operation(s) for users.
  name: Syllable Users API
  slug: syllable-users-api
- description: The V1 API from Syllable — 4 operation(s) for v1.
  name: Syllable V1 API
  slug: syllable-v1-api
- description: The voice_groups API from Syllable — 3 operation(s) for voice_groups.
  name: Syllable Voice Groups API
  slug: syllable-voice-groups-api
artifact_total: 89
asyncapis:
- description: ''
  name: Syllable Outbound Webhooks
  slug: syllable-outbound-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: SyllableSDK Agents API
  slug: open-syllable-agents-api
- collection_type: open
  name: SyllableSDK Agents.test API
  slug: open-syllable-agents-test-api
- collection_type: open
  name: SyllableSDK Bridge Phrases API
  slug: open-syllable-bridge-phrases-api
- collection_type: open
  name: SyllableSDK Channels API
  slug: open-syllable-channels-api
- collection_type: open
  name: SyllableSDK Channels.targets API
  slug: open-syllable-channels-targets-api
- collection_type: open
  name: SyllableSDK Channels.twilio API
  slug: open-syllable-channels-twilio-api
- collection_type: open
  name: SyllableSDK Channels.twilio.numbers API
  slug: open-syllable-channels-twilio-numbers-api
- collection_type: open
  name: SyllableSDK Conversation Config API
  slug: open-syllable-conversation-config-api
- collection_type: open
  name: SyllableSDK Conversations API
  slug: open-syllable-conversations-api
- collection_type: open
  name: SyllableSDK Custom Messages API
  slug: open-syllable-custom-messages-api
- collection_type: open
  name: SyllableSDK Dashboards API
  slug: open-syllable-dashboards-api
- collection_type: open
  name: SyllableSDK Data Sources API
  slug: open-syllable-data-sources-api
- collection_type: open
  name: SyllableSDK Directory API
  slug: open-syllable-directory-api
- collection_type: open
  name: SyllableSDK Events API
  slug: open-syllable-events-api
- collection_type: open
  name: SyllableSDK Incidents API
  slug: open-syllable-incidents-api
- collection_type: open
  name: SyllableSDK Insights API
  slug: open-syllable-insights-api
- collection_type: open
  name: SyllableSDK Insights.folders API
  slug: open-syllable-insights-folders-api
- collection_type: open
  name: SyllableSDK Insights.tools API
  slug: open-syllable-insights-tools-api
- collection_type: open
  name: SyllableSDK Insights.workflows API
  slug: open-syllable-insights-workflows-api
- collection_type: open
  name: SyllableSDK Language Groups API
  slug: open-syllable-language-groups-api
- collection_type: open
  name: SyllableSDK Organizations API
  slug: open-syllable-organizations-api
- collection_type: open
  name: SyllableSDK Organizations.sip Ip Ranges API
  slug: open-syllable-organizations-sip-ip-ranges-api
- collection_type: open
  name: SyllableSDK Outbound.batches API
  slug: open-syllable-outbound-batches-api
- collection_type: open
  name: SyllableSDK Outbound.campaigns API
  slug: open-syllable-outbound-campaigns-api
- collection_type: open
  name: SyllableSDK Permissions API
  slug: open-syllable-permissions-api
- collection_type: open
  name: SyllableSDK Prompts API
  slug: open-syllable-prompts-api
- collection_type: open
  name: SyllableSDK Pronunciations API
  slug: open-syllable-pronunciations-api
- collection_type: open
  name: SyllableSDK Roles API
  slug: open-syllable-roles-api
- collection_type: open
  name: SyllableSDK Services API
  slug: open-syllable-services-api
- collection_type: open
  name: SyllableSDK Session Debug API
  slug: open-syllable-session-debug-api
- collection_type: open
  name: SyllableSDK Session Labels API
  slug: open-syllable-session-labels-api
- collection_type: open
  name: SyllableSDK Sessions API
  slug: open-syllable-sessions-api
- collection_type: open
  name: SyllableSDK Sessions.full Summary API
  slug: open-syllable-sessions-full-summary-api
- collection_type: open
  name: SyllableSDK Sessions.latency API
  slug: open-syllable-sessions-latency-api
- collection_type: open
  name: SyllableSDK Sessions.timeline API
  slug: open-syllable-sessions-timeline-api
- collection_type: open
  name: SyllableSDK Sessions.transcript API
  slug: open-syllable-sessions-transcript-api
- collection_type: open
  name: SyllableSDK Takeouts API
  slug: open-syllable-takeouts-api
- collection_type: open
  name: SyllableSDK Tools API
  slug: open-syllable-tools-api
- collection_type: open
  name: SyllableSDK Users API
  slug: open-syllable-users-api
- collection_type: open
  name: SyllableSDK V1 API
  slug: open-syllable-v1-api
- collection_type: open
  name: SyllableSDK Voice Groups API
  slug: open-syllable-voice-groups-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/syllable-sdk-overlay.yaml
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
  name: Syllable MCP Server
  slug: syllable-mcp-server
modified: '2026-08-05'
name: Syllable
nav: Providers
network: true
overview: 'Syllable publishes 41 APIs on the [APIs.io](https://apis.io/) network, including Agents API, Agents.test API, Bridge Phrases API, and 38 more. Tagged areas include Company, Artificial Intelligence, AI Agents, Voice, and Conversational AI.


  The Syllable catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Syllable''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 32 more developer resources.'
random_paper: 16
score:
  band: strong
  composite: 62.8
  coverage:
    artifact_dirs: 24
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 18.2
    contract_quality: 66.0
    developer_ergonomics: 85.7
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 42.1
  previous_composite: 62.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 41
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 41.7
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/syllable/refs/heads/main/screenshots/syllable-2026-08-17T082225.png
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
