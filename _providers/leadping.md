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
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.3
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Two remote Model Context Protocol servers. A public read-only documentation server at https://leadping.ai/docs/mcp answers anonymous tools/list with search, virtual-filesystem and feedback tools. An a
  name: Leadping MCP Servers
  slug: leadping-mcp-servers
- description: Outbound HTTPS webhook deliveries fired by Leadping automations, signed with the Standard Webhooks specification (HMAC-SHA256 over {webhook-id}.{webhook-timestamp}.{body}, whsec_ signing secret). Lead
  name: Leadping Webhook Events
  slug: leadping-webhook-events
- description: Provides lead, communication, conversion, and organization performance analytics. Use these endpoints to measure activity over time, compare outcomes, and power operational dashboards and reporting wo
  name: Leadping Analytics API
  slug: leadping-analytics-api
- description: 'Manages automated lead follow-up workflows and their execution history. Use these endpoints to configure SMS automation steps, preview eligible leads, run workflows, and inspect individual automation '
  name: Leadping Automations API
  slug: leadping-automations-api
- description: Provides call event records for auditing, diagnostics, and reporting. Use these endpoints to search and inspect lifecycle events emitted as Leadping calls are initiated, connected, completed, or fail.
  name: Leadping Call Events API
  slug: leadping-callevents-api
- description: Manages outbound Leadping calls and active call-control workflows. Use these endpoints to initiate or cancel a call, retrieve call state, and transfer an active call within supported telephony flows.
  name: Leadping Calls API
  slug: leadping-calls-api
- description: Accepts public contact and website inquiry submissions for Leadping. Use these endpoints to send a structured support or sales inquiry from an application or submit the Leadping website contact form.
  name: Leadping Contact API
  slug: leadping-contact-api
- description: Provides lead conversation timelines and inbox-oriented conversation views. Use these endpoints to list recent conversations and retrieve the cross-channel communication history associated with a lead
  name: Leadping Conversations API
  slug: leadping-conversations-api
- description: Provides a unified record of Leadping activity across communication channels. Use these endpoints to retrieve event timelines, search event history, inspect event details, and record supported applica
  name: Leadping Events API
  slug: leadping-events-api
- description: Captures Leadping product feedback and supports administrative triage. Users can submit feedback, while authorized staff can search, inspect, classify, and update feedback throughout the review proces
  name: Leadping Feedback API
  slug: leadping-feedback-api
- description: Manages lead intake, records, assignment, routing, and lifecycle operations. Use these endpoints to ingest leads from trusted sources, search and update lead records, manage ownership and tags, and ar
  name: Leadping Leads API
  slug: leadping-leads-api
- description: Manages the auditable history of lead status transitions. Use these endpoints to change a lead's status, correct transition records, search status history, and export status activity for reporting.
  name: Leadping Lead Status Changes API
  slug: leadping-leadstatuschanges-api
- description: Manages the lead statuses used to classify and track leads throughout their lifecycle. Use these endpoints to list, create, update, and archive organization-specific lead statuses for consistent pipel
  name: Leadping Lead Statuses API
  slug: leadping-leadstatuses-api
- description: Manages user notifications, announcements, and push-notification installations. Use these endpoints to retrieve notification feeds and unread counts, update read state, and register or remove client p
  name: Leadping Notifications API
  slug: leadping-notifications-api
- description: Manages Leadping organizations, memberships, invitations, settings, and API credentials. Use these endpoints to maintain organization profiles and branding, manage members and invitations, configure o
  name: Leadping Organizations API
  slug: leadping-organizations-api
- description: Reports outbound delivery pacing and sending capacity for the current organization. Use these endpoints to determine whether outbound communications can proceed and to understand active throttles, lim
  name: Leadping Outbound Delivery API
  slug: leadping-outbounddelivery-api
- description: Manages organization payment methods and billing invoices. Use these endpoints to add, confirm, inspect, and remove payment methods or retrieve invoices associated with the current organization's bill
  name: Leadping Payment Methods API
  slug: leadping-paymentmethods-api
- description: Manages phone-number discovery, purchasing, assignment, configuration, and compliance. Use these endpoints to search available numbers, manage owned numbers and caller identity, configure messaging or
  name: Leadping Phone Numbers API
  slug: leadping-phonenumbers-api
- description: Sends and manages SMS and MMS communications through Leadping. Use these endpoints to send messages, upload MMS media, and cancel eligible scheduled messages while preserving conversation and delivery
  name: Leadping Sms API
  slug: leadping-sms-api
- description: 'Provides SMS and MMS event records for delivery tracking and diagnostics. Use these endpoints to search and inspect message lifecycle events, including outbound delivery updates and inbound messaging '
  name: Leadping Sms Events API
  slug: leadping-smsevents-api
- description: 'Manages lead sources, intake credentials, routing defaults, and attribution. Use these endpoints to create and configure sources, search source records, inspect source activity, rotate intake access, '
  name: Leadping Sources API
  slug: leadping-sources-api
- description: Manages recipient suppression state for compliant Leadping communication workflows. Use these endpoints to check contact eligibility, record or release suppressions, and review suppression history bef
  name: Leadping Suppressions API
  slug: leadping-suppressions-api
- description: Manages organization-defined tags for categorizing and routing leads. Use these endpoints to list, create, update, and archive reusable tags that support lead filtering, automation, assignment, and re
  name: Leadping Tags API
  slug: leadping-tags-api
- description: Provides shared authentication and bootstrap data for Leadping telephony clients. Use this endpoint to obtain the scoped credentials and configuration required to initialize supported calling experien
  name: Leadping Telephony API
  slug: leadping-telephony-api
- description: Provides organization wallet and billing transaction records. Use these endpoints to search transaction history, inspect individual charges or credits, review transaction summaries, and issue administ
  name: Leadping Transactions API
  slug: leadping-transactions-api
- description: Provides billable usage records for Leadping services. Use these endpoints to review messaging and calling consumption, inspect usage summaries, and reconcile provider activity for an organization.
  name: Leadping Usage API
  slug: leadping-usage-api
- description: Creates and delivers user-requested exports of Leadping account data. Use these endpoints to request an export, monitor its preparation status, and download the completed archive through a time-limite
  name: Leadping User Data Exports API
  slug: leadping-userdataexports-api
- description: Manages the current Leadping user's profile, preferences, setup, and account workflows. Use these endpoints to retrieve and update user data, configure communication and compliance preferences, comple
  name: Leadping Users API
  slug: leadping-users-api
- description: Manages organization wallet balances, funding, and credit activity. Use these endpoints to inspect wallet state and history, configure wallet behavior, add funds, and record credits or adjustments.
  name: Leadping Wallets API
  slug: leadping-wallets-api
artifact_total: 39
asyncapis:
- description: ''
  name: Leadping Webhooks
  slug: leadping-webhooks
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/leadping-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://leadping.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://leadping.ai/docs/developers/overview
- group: docs
  title: ''
  type: Documentation
  url: https://leadping.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://leadping.ai/docs/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://leadping.ai/docs/get-started
- group: operate
  title: ''
  type: Support
  url: https://leadping.ai/contact
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/leadpingai
- group: commercial
  title: ''
  type: Pricing
  url: https://leadping.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://leadping.ai/authentication/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://leadping.ai/docs/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://leadping.ai/docs/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.leadping.ai
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/leadping-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://api.leadping.ai/changelog.json
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/leadping-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/leadping-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/leadping-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/leadping-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/leadping-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/leadping-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/leadping-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/leadping-plans-pricing.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/leadping-finops.json
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/leadping-vocabulary.json
- group: build
  title: ''
  type: Packages
  url: packages/leadping-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/leadping-packages.yml
- group: build
  title: ''
  type: SDKs
  url: https://leadping.ai/docs/sdks/overview
- group: agent
  title: ''
  type: MCPServer
  url: mcp/leadping-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/leadping-tool-crosswalk.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/leadping-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/leadping-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://leadping.ai/llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/leadping-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: https://leadping.ai/.well-known/api-catalog
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/leadping-security.txt
- group: auth
  title: ''
  type: Security
  url: security/leadping-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/leadping-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/leadping-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/leadping-trust-center.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/leadping-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://leadping.ai/docs/compliance
- group: other
  title: ''
  type: Overlay
  url: overlays/leadping-api-overlay.yaml
- group: other
  title: ''
  type: APIsJSON
  url: https://api.leadping.ai/apis.json
created: '2026-08-18'
description: Leadping is a lead-management and responsible-outreach platform for teams that need to move a new inbound lead from source to first touch without stitching together separate tools. It captures leads from approved sources, routes and assigns them, runs follow-up automations, sends SMS and MMS, places and transfers calls, keeps conversation and event history together, enforces recipient suppression and opt-out handling, tracks A2P 10DLC carrier registration and phone-number warmup, requires TrustedForm consent evidence where a source needs it, and reports usage, billing and analytics. The 137-operation REST API is published as an OpenAPI 3.1.1 contract with six Kiota-generated first-party SDKs, two remote MCP servers, Standard Webhooks signing, and an unusually complete machine-readable discovery surface including APIs.json, an RFC 9727 API catalog, RFC 9728 protected-resource metadata, llms.txt and an agent-skill index.
image: https://leadping.ai/img/favicon/leadpinglogo1024x1024.png
layout: provider
mcp_servers:
- description: ''
  name: Leadping MCP Server
  slug: leadping-mcp-server
- description: ''
  name: Leadping MCP Server
  slug: leadping-mcp-server-2
- description: ''
  name: Leadping MCP Server
  slug: leadping-mcp-server-3
modified: '2026-08-18'
name: Leadping
nav: Providers
network: true
overview: 'Leadping publishes 27 APIs on the [APIs.io](https://apis.io/) network, including Analytics API, Automations API, Call Events API, and 24 more. Tagged areas include Lead Management, Sales & marketing automation, SMS Messaging, A2P 10DLC, and CPaaS.


  The Leadping catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Leadping''s developer surface includes documentation, API reference, getting-started guide, support, pricing, signup flow, changelog, and 38 more developer resources.'
plans:
- name: Leadping Plans Pricing
  plan_count: 2
  slug: leadping-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 4
  name: Leadping Rate Limits
  slug: leadping-rate-limits
score:
  band: exemplar
  composite: 69.4
  coverage:
    artifact_dirs: 21
    catalog_gap: 66.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 81.6
    commercial_clarity: 81.6
    contract_governance: 33.3
    contract_quality: 66.5
    developer_ergonomics: 63.7
    discoverability: 63.0
    governance: 33.3
    operational_transparency: 68.4
  previous_composite: 69.4
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 27
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 59.7
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Leadping Authentication
  slug: leadping-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Leadping Domain Security
  slug: leadping-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Leadping Vulnerability Disclosure
  slug: leadping-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Leadping Trust Center
  slug: leadping-trust-center
  summary_line: trust center published
slug: leadping
tags:
- Lead Management
- Sales & marketing automation
- SMS Messaging
- A2P 10DLC
- CPaaS
- Communications
- Voice/calling
- Compliance & consent
- agent-native
- MCP
- Lead intake
- Conversations
- Automations
- Suppression & opt-out
- Webhook
website: https://leadping.ai/
---
