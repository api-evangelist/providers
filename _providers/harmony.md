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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.4
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Harmony Agentic Access
  operation_count: 9
  slug: harmony-agentic-access
  summary_line: 9 operations · 5 acting
api_count: 1
apis:
- baseURL: https://api.harmony.io/service-desk
  baseurl_source: declared
  description: The tickets API from Harmony — 6 operation(s) for tickets.
  name: Harmony tickets API
  slug: harmony-tickets-api
arazzos:
- description: Create a service-desk ticket, read it back, triage it, and audit the change.
  name: Harmony — create and triage an IT ticket
  slug: harmony-create-and-triage-ticket
artifact_total: 9
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: service-desk tickets API
  slug: open-harmony-tickets-api
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/harmony-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/harmony-service-desk-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/harmony-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.harmony.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.harmony.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.harmony.io/api-references/api-documentation/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.harmony.io/getting-started/welcome
- group: operate
  title: ''
  type: Support
  url: mailto:support@harmony.io
- group: company
  title: ''
  type: Blog
  url: https://harmony.io/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/harmonyso
- group: commercial
  title: ''
  type: TermsOfService
  url: https://harmony.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://harmony.io/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.harmony.io/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.harmony.io/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/harmony-llms.txt
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/harmony-lifecycle.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/harmony-create-and-triage-ticket.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/harmony-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/harmony-authentication.yml
created: '2026-07-17'
description: Harmony is an agentic enterprise service management (ESM) platform that gives every employee an always-on AI expert for IT, HR, finance, procurement, and legal service requests inside Slack and Microsoft Teams. Its AI agents autonomously resolve requests — password and MFA resets, application access, device recovery, employee onboarding and offboarding — using a context graph that connects each employee's identity, devices, applications, and history, often resolving issues before a ticket is opened. Harmony exposes a public REST Service Desk API for programmatically listing, creating, updating, querying, and bulk-updating tickets along with their custom fields and activity history. Founded in 2025 by Nitzan Shapira and Ran Ribenzaft and backed by Lightspeed Venture Partners.
image: https://harmony.io/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: Harmony MCP Server
  slug: harmony-mcp-server
modified: '2026-07-19'
name: Harmony
nav: Providers
network: true
overview: 'Harmony publishes 1 API on the [APIs.io](https://apis.io/) network: tickets API. Tagged areas include ITSM, Service Desk, Ticketing, Enterprise Service Management, and AI Agents.


  Harmony''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, and 14 more developer resources.'
random_paper: 10
rate_limits:
- limit_count: 2
  name: Harmony Rate Limits
  slug: harmony-rate-limits
score:
  band: developing
  composite: 44.4
  coverage:
    artifact_dirs: 17
    catalog_gap: 70.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 4.5
    contract_quality: 54.4
    developer_ergonomics: 58.9
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 39.5
  previous_composite: 44.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/harmony/refs/heads/main/screenshots/harmony-2026-07-25T220731.png
security:
- kind: authentication
  name: Harmony Authentication
  slug: harmony-authentication
  summary_line: http/apiKey · 2 schemes
- kind: domain-security
  name: Harmony Domain Security
  slug: harmony-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: harmony
tags:
- ITSM
- Service Desk
- Ticketing
- Enterprise Service Management
- AI Agents
- IT Automation
- Help Desk
- Identity
- Company
website: https://docs.harmony.io/
---
