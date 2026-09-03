---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: flavored
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: true
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 52.4
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Nylas Agentic Access
  operation_count: 22
  slug: nylas-agentic-access
  summary_line: 22 operations · 8 acting
api_count: 2
apis:
- baseURL: https://api.us.nylas.com
  baseurl_source: declared
  description: 'Application-level administration: Nylas applications, API keys, custom domains, connectors and connector credentials, workspaces, and the rules, policies and lists that govern them.'
  name: Nylas Admin API
  slug: nylas-admin-api
- baseURL: https://api.us.nylas.com
  baseurl_source: declared
  description: Authentication. Hosted OAuth 2.1 authorization and token exchange, custom (non-OAuth) grant creation for Agent Accounts, token refresh and revocation, and ID token validation.
  name: Nylas Auth API
  slug: nylas-auth-api
- baseURL: https://api.us.nylas.com
  baseurl_source: declared
  description: Calendars. List and manage a grant's calendars, query free/busy availability across participants, and read room and resource calendars.
  name: Nylas Calendars API
  slug: nylas-calendars-api
- baseURL: https://api.us.nylas.com
  baseurl_source: declared
  description: Contacts. Read, create, update and delete a grant's contacts and contact groups.
  name: Nylas Contacts API
  slug: nylas-contacts-api
- baseURL: https://api.us.nylas.com
  baseurl_source: declared
  description: Drafts. Compose, update, send and delete drafts, manage attachments, and generate draft bodies and replies with Smart Compose.
  name: Nylas Drafts API
  slug: nylas-drafts-api
- baseURL: https://api.us.nylas.com
  baseurl_source: declared
  description: Events. Create, update, delete and list calendar events, including recurring events, group events and RSVP handling.
  name: Nylas Events API
  slug: nylas-events-api
- baseURL: https://api.us.nylas.com
  baseurl_source: declared
  description: Grants. A grant represents one authenticated mailbox and calendar. List, retrieve and delete grants, and inspect grant state and scopes.
  name: Nylas Grants API
  slug: nylas-grants-api
- baseURL: https://api.us.nylas.com
  baseurl_source: declared
  description: Messages. List, search, read, update and delete email messages. Send immediately, schedule a send and cancel a scheduled send, with folders, signatures and attachments alongside.
  name: Nylas Messages API
  slug: nylas-messages-api
- baseURL: https://api.us.nylas.com
  baseurl_source: declared
  description: Scheduler. Booking configurations, scheduling sessions, availability lookups and booking lifecycle management for hosted and component-based booking flows.
  name: Nylas Scheduling API
  slug: nylas-scheduling-api
- baseURL: https://api.us.nylas.com
  baseurl_source: declared
  description: Threads. List, search, read and update email threads, and manage thread-level folders and state.
  name: Nylas Threads API
  slug: nylas-threads-api
- baseURL: https://api.us.nylas.com
  baseurl_source: declared
  description: 'Change notifications. Nylas pushes events for messages, threads, calendars, events, grants and Notetaker over three interchangeable transports carrying the same payloads: HTTPS webhooks, Google Cloud '
  name: Nylas Notifications API
  slug: nylas-notifications-api
- baseURL: https://api.us.nylas.com
  baseurl_source: declared
  description: Meeting notetaker. Send a notetaker to a Google Meet, Microsoft Teams or Zoom call, then retrieve the recording, transcript, summary and action items. Available grant-scoped, or standalone with no con
  name: Nylas Notetaker API
  slug: nylas-notetaker-api
- baseURL: https://api.us.nylas.com
  baseurl_source: declared
  description: The Templates and Workflows API from Nylas — 12 operation(s) for templates and workflows.
  name: Nylas Templates and Workflows API
  slug: nylas-templates-and-workflows-api
artifact_total: 35
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Nylas API (v3) Admin API
  slug: open-nylas-admin-api
- collection_type: open
  name: Nylas API (v3) Admin Auth API
  slug: open-nylas-auth-api
- collection_type: open
  name: Nylas API (v3) Admin Calendars API
  slug: open-nylas-calendars-api
- collection_type: open
  name: Nylas API (v3) Admin Contacts API
  slug: open-nylas-contacts-api
- collection_type: open
  name: Nylas API (v3) Admin Drafts API
  slug: open-nylas-drafts-api
- collection_type: open
  name: Nylas API (v3) Admin Events API
  slug: open-nylas-events-api
- collection_type: open
  name: Nylas API (v3) Admin Grants API
  slug: open-nylas-grants-api
- collection_type: open
  name: Nylas API (v3) Admin Messages API
  slug: open-nylas-messages-api
- collection_type: open
  name: Nylas API (v3) Admin Scheduling API
  slug: open-nylas-scheduling-api
- collection_type: open
  name: Nylas API (v3) Admin Threads API
  slug: open-nylas-threads-api
- collection_type: open
  name: Nylas API (v3)
  slug: open-nylas
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/nylas-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/nylas-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/nylas-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/nylas-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nylas-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/nylas-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/nylas
- group: company
  title: ''
  type: Website
  url: https://www.nylas.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.nylas.com/
- group: company
  title: ''
  type: Blog
  url: https://www.nylas.com/blog/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/nylas
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.nylas.com/legal/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.nylas.com/legal/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.nylas.com/
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.nylas.com/llms.txt
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.nylas.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.nylas.com/docs/reference/api/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.nylas.com/docs/reference/notifications/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.nylas.com/docs/reference/ui/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.nylas.com/docs/v3/getting-started/
- group: build
  title: ''
  type: SDKs
  url: https://github.com/nylas/nylas-nodejs
- group: build
  title: ''
  type: SDKs
  url: https://github.com/nylas/nylas-python
- group: build
  title: ''
  type: SDKs
  url: https://github.com/nylas/nylas-ruby
- group: build
  title: ''
  type: SDKs
  url: https://github.com/nylas/nylas-java
- group: build
  title: ''
  type: CLI
  url: https://cli.nylas.com/
- group: build
  title: ''
  type: Postman
  url: https://developer.nylas.com/docs/v3/api-references/postman/
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/trynylas/workspace/nylas-api/overview
- group: agent
  title: ''
  type: AgentSkills
  url: https://developer.nylas.com/.well-known/agent-skills/index.json
- group: operate
  title: ''
  type: Support
  url: https://developer.nylas.com/docs/support/
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.nylas.com/docs/changelogs/
- group: operate
  title: ''
  type: DeprecationPolicy
  url: https://developer.nylas.com/docs/support/product-lifecycle/
- group: auth
  title: ''
  type: Security
  url: https://www.nylas.com/security/
- group: auth
  title: ''
  type: Compliance
  url: https://trust.nylas.com/public
- group: design
  title: ''
  type: Webhooks
  url: https://developer.nylas.com/docs/v3/notifications/
- group: design
  title: ''
  type: ErrorCodes
  url: https://developer.nylas.com/docs/api/errors/
- group: operate
  title: ''
  type: RateLimits
  url: https://developer.nylas.com/docs/dev-guide/platform/rate-limits/
- group: design
  title: ''
  type: Idempotency
  url: https://developer.nylas.com/docs/v3/email/idempotent-send/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.nylas.com/pricing/
- group: start
  title: ''
  type: Signup
  url: https://dashboard-v3.nylas.com/register
- group: agent
  title: ''
  type: MCPServer
  url: https://mcp.us.nylas.com
- group: agent
  title: ''
  type: MCPServer
  url: mcp/nylas-mcp.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/nylas-vocabulary.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/nylas-conformance.yml
- group: other
  title: ''
  type: AgentCard
  url: a2a/nylas-a2a.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: https://developer.nylas.com/.well-known/security.txt
- group: other
  title: ''
  type: ContentSignal
  url: https://developer.nylas.com/robots.txt
- group: other
  title: ''
  type: APICatalog
  url: https://developer.nylas.com/.well-known/api-catalog
- group: agent
  title: ''
  type: WellKnown
  url: well-known/nylas-well-known.yml
created: '2025-02-06'
description: Nylas connects your application to every email inbox and calendar in the world. The Nylas v3 platform provides REST APIs for email, calendar, contacts, scheduling, meeting notetaking, authentication, and administration across Google, Microsoft, Exchange, iCloud, Yahoo and any IMAP provider. Official SDKs cover Node.js, Python, Ruby and Kotlin/Java, alongside a CLI, a hosted MCP server, and Agent Accounts that provision a Nylas-hosted mailbox and calendar for autonomous agents without requiring an OAuth flow.
finops:
- name: Nylas Finops
  service_category: API
  slug: nylas-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nylas.png
layout: provider
mcp_servers:
- description: ''
  name: Nylas MCP Server
  slug: nylas-mcp-server
- description: Nylas operates an official remote MCP server fronting the Nylas v3 email, calendar and contacts APIs, deployed per region at https://mcp.us.nylas.com and https://mcp.eu.nylas.com. Transport is streama
  name: Nylas MCP Server manifest
  slug: nylas-mcp-server-manifest
modified: '2026-04-28'
name: Nylas
nav: Providers
network: true
overview: 'Nylas publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Admin API, Auth API, Calendars API, and 10 more. Tagged areas include Calendar, Communications, Contacts, Email, and Messaging.


  Nylas'' developer surface includes authentication, documentation, engineering blog, API reference, getting-started guide, CLI, support, and 41 more developer resources.'
plans:
- name: Nylas Plans Pricing
  plan_count: 5
  slug: nylas-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 10
  name: Nylas Rate Limits
  slug: nylas-rate-limits
score:
  band: exemplar
  composite: 76.3
  coverage:
    artifact_dirs: 17
    catalog_gap: 46.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.8
  facets:
    access_clarity: 100.0
    commercial_clarity: 100.0
    contract_governance: 33.3
    contract_quality: 59.1
    developer_ergonomics: 92.9
    discoverability: 87.0
    governance: 33.3
    operational_transparency: 78.9
  previous_composite: 75.5
  provenance:
    agentic_access: derived
    conformance: unknown
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 13
    mcp: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nylas/refs/heads/main/screenshots/nylas-2026-06-20T190645.png
security:
- kind: authentication
  name: Nylas Authentication
  slug: nylas-authentication
  summary_line: http · 3 schemes
- kind: domain-security
  name: Nylas Domain Security
  slug: nylas-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Nylas Vulnerability Disclosure
  slug: nylas-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Nylas Trust Center
  slug: nylas-trust-center
  summary_line: SOC 2 Type II, ISO 27001, ISO 27701, HIPAA, GDPR, CCPA, CPRA, CSA STAR Level 1, PCI-DSS SAQ A, Data Privacy Framework, GLBA Privacy Rule, ADA Tier 2 CASA Verified
slug: nylas
tags:
- Calendar
- Communications
- Contacts
- Email
- Messaging
- Scheduling
website: https://www.nylas.com/
---
