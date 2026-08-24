---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 57.2
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 54
  human_in_the_loop: 0
  name: Chili Piper Agentic Access
  operation_count: 73
  slug: chili-piper-agentic-access
  summary_line: 73 operations · 54 acting
api_count: 16
apis:
- description: Official hosted remote MCP server for Chili Piper, served over streamable HTTP at https://fire.chilipiper.com/api/fire-edge/v1/org/mcp. Supports OAuth (Admin, browser-based) and API-key bearer authent
  name: Chili Piper MCP Server
  slug: mcp
- description: The availability API from Chili Piper — 1 operation(s) for availability.
  name: Chili Piper Availability API
  slug: chili-piper-availability-api
- description: The chat API from Chili Piper — 1 operation(s) for chat.
  name: Chili Piper Chat API
  slug: chili-piper-chat-api
- description: The concierge API from Chili Piper — 4 operation(s) for concierge.
  name: Chili Piper Concierge API
  slug: chili-piper-concierge-api
- description: The distribution API from Chili Piper — 3 operation(s) for distribution.
  name: Chili Piper Distribution API
  slug: chili-piper-distribution-api
- description: The distro API from Chili Piper — 7 operation(s) for distro.
  name: Chili Piper Distro API
  slug: chili-piper-distro-api
- description: The handoff API from Chili Piper — 3 operation(s) for handoff.
  name: Chili Piper Handoff API
  slug: chili-piper-handoff-api
- description: The meeting-type API from Chili Piper — 4 operation(s) for meeting-type.
  name: Chili Piper Meeting Type API
  slug: chili-piper-meeting-type-api
- description: The meeting-type-reminder API from Chili Piper — 3 operation(s) for meeting-type-reminder.
  name: Chili Piper Meeting Type Reminder API
  slug: chili-piper-meeting-type-reminder-api
- description: The meetings API from Chili Piper — 4 operation(s) for meetings.
  name: Chili Piper Meetings API
  slug: chili-piper-meetings-api
- description: The rule API from Chili Piper — 2 operation(s) for rule.
  name: Chili Piper Rule API
  slug: chili-piper-rule-api
- description: The schedulingLinks API from Chili Piper — 13 operation(s) for schedulinglinks.
  name: Chili Piper Scheduling Links API
  slug: chili-piper-schedulinglinks-api
- description: The team API from Chili Piper — 5 operation(s) for team.
  name: Chili Piper Team API
  slug: chili-piper-team-api
- description: The tenant API from Chili Piper — 1 operation(s) for tenant.
  name: Chili Piper Tenant API
  slug: chili-piper-tenant-api
- description: The user API from Chili Piper — 4 operation(s) for user.
  name: Chili Piper User API
  slug: chili-piper-user-api
- description: The workspace API from Chili Piper — 4 operation(s) for workspace.
  name: Chili Piper Workspace API
  slug: chili-piper-workspace-api
artifact_total: 42
asyncapis:
- description: ''
  name: Chili Piper Webhooks
  slug: chili-piper-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Chili Piper — Inspector Actions Availability API
  slug: open-chili-piper-availability-api
- collection_type: open
  name: Chili Piper — Conversation Inspector Actions Chat API
  slug: open-chili-piper-chat-api
- collection_type: open
  name: Chili Piper Concierge API
  slug: open-chili-piper-concierge-api
- collection_type: open
  name: Chili Piper Distribution API
  slug: open-chili-piper-distribution-api
- collection_type: open
  name: Chili Piper Distro API
  slug: open-chili-piper-distro-api
- collection_type: open
  name: Chili Piper — Router Configuration Actions Handoff API
  slug: open-chili-piper-handoff-api
- collection_type: open
  name: Chili Piper Meeting Type API
  slug: open-chili-piper-meeting-type-api
- collection_type: open
  name: Chili Piper — Meeting Type Management Actions Meeting Type Reminder API
  slug: open-chili-piper-meeting-type-reminder-api
- collection_type: open
  name: Chili Piper Meetings API
  slug: open-chili-piper-meetings-api
- collection_type: open
  name: Chili Piper Rule API
  slug: open-chili-piper-rule-api
- collection_type: open
  name: Chili Piper Scheduling Links API
  slug: open-chili-piper-schedulinglinks-api
- collection_type: open
  name: Chili Piper Team API
  slug: open-chili-piper-team-api
- collection_type: open
  name: Chili Piper — Concierge Router Builder Actions Tenant API
  slug: open-chili-piper-tenant-api
- collection_type: open
  name: Chili Piper User API
  slug: open-chili-piper-user-api
- collection_type: open
  name: Chili Piper Workspace API
  slug: open-chili-piper-workspace-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/chili-piper-agentic-access.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/chili-piper-availability-inspector-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.chilipiper.com/
- group: docs
  title: ''
  type: Documentation
  url: https://help.chilipiper.com/hc/en-us
- group: docs
  title: ''
  type: APIReference
  url: https://help.chilipiper.com/hc/en-us/articles/35576029581971-Edge-API-References
- group: start
  title: ''
  type: GettingStarted
  url: https://help.chilipiper.com/hc/en-us/articles/30935152032275-Using-Concierge-via-the-Edge-API
- group: operate
  title: ''
  type: Support
  url: https://help.chilipiper.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.chilipiper.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Chili-Piper
- group: commercial
  title: ''
  type: Pricing
  url: https://www.chilipiper.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.chilipiper.com/get-started
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.chilipiper.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.chilipiper.com/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.chilipiper.com/
- group: auth
  title: ''
  type: Compliance
  url: https://www.chilipiper.com/security
- group: auth
  title: ''
  type: Security
  url: https://github.com/Chili-Piper/mcp-assets/blob/main/SECURITY.md
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/chili-piper-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/chili-piper-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/chili-piper-packages.yml
- group: design
  title: ''
  type: Components
  url: components/chili-piper-components.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/chili-piper-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/chili-piper-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/chili-piper-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/chili-piper-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/chili-piper-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/chili-piper-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/chili-piper-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/chili-piper-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/chili-piper-vulnerability-disclosure.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/chili-piper-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/chili-piper-webhooks.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/chili-piper-changelog.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.chilipiper.com/
- group: agent
  title: ''
  type: MCPServer
  url: mcp/chili-piper-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/chili-piper-tool-crosswalk.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/chili-piper-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/chili-piper-rate-limits.yml
created: '2026-08-09'
description: Chili Piper is a demand conversion platform for B2B go-to-market teams, founded in 2016 by Alina and Nicolas Vandenberghe and headquartered in New York. Its products - Concierge, Distro, Handoff, Chat AI, Web Experiences, Re-engagement and ChiliCal - turn inbound website visitors and form submissions into booked meetings by qualifying, enriching, routing and scheduling leads against Salesforce or HubSpot ownership, territory and round-robin distribution logic. For developers, Chili Piper publishes the Edge API (https://fire.chilipiper.com/api/fire-edge), a bearer-token REST surface covering users, workspaces, teams, routing rules, distributions, meetings, meeting types, scheduling links, handoff and Concierge routing; a hosted remote MCP server with 55 documented tools; official Agent Skills and ChatGPT GPT actions published under the Chili-Piper GitHub organization; a Concierge JavaScript embed distributed on npm; and custom webhooks for booked, updated and cancelled meetings.
image: https://cdn.prod.website-files.com/61c9fe00acd90d7271f7014e/63d787acdbdc86179f01ed1a_Favicon%20(1).png
layout: provider
mcp_servers:
- description: ''
  name: Chili Piper MCP Server
  slug: chili-piper-mcp-server
modified: '2026-08-13'
name: Chili Piper
nav: Providers
network: true
overview: 'Chili Piper publishes 15 APIs on the [APIs.io](https://apis.io/) network, including Availability API, Chat API, Concierge API, and 12 more. Tagged areas include Scheduling, Lead Routing, Meetings, Sales, and Marketing.


  The Chili Piper catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Chili Piper''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 31 more developer resources.'
plans:
- name: Chili Piper Plans Pricing
  plan_count: 4
  slug: chili-piper-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Chili Piper Rate Limits
  slug: chili-piper-rate-limits
scopes:
- name: Chili Piper Scopes
  scope_count: 0
  slug: chili-piper-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 66.0
  delta: 0.0
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 16.7
    contract_quality: 68.2
    developer_ergonomics: 61.9
    discoverability: 92.6
    governance: 16.7
    operational_transparency: 52.6
  previous_composite: 66.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
    mcp: first-party
    skills: first-party
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/chili-piper/refs/heads/main/screenshots/chili-piper-2026-08-17T080410.png
security:
- kind: authentication
  name: Chili Piper Authentication
  slug: chili-piper-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Chili Piper Domain Security
  slug: chili-piper-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Chili Piper Vulnerability Disclosure
  slug: chili-piper-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Chili Piper Trust Center
  slug: chili-piper-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: chili-piper
tags:
- Scheduling
- Lead Routing
- Meetings
- Sales
- Marketing
- CRM
- Demand Conversion
- Appointment Booking
- Revenue Operations
- Calendar
- Agents
- MCP
website: https://www.chilipiper.com/
---
