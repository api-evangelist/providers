---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 50.2
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Mailersend Agentic Access
  operation_count: 16
  slug: mailersend-agentic-access
  summary_line: 16 operations · 7 acting
api_count: 1
apis:
- description: MailerSend API v1 provides RESTful endpoints for sending emails (single, bulk, scheduled), templates, domains, recipients, suppression lists, webhooks, analytics, SMS, and inbound routing.
  name: MailerSend API
  slug: mailersend-api
- description: The Bulk Email API from MailerSend — 2 operation(s) for bulk email.
  name: MailerSend Bulk Email API
  slug: mailersend-bulk-email-api
- description: The Domains API from MailerSend — 2 operation(s) for domains.
  name: MailerSend Domains API
  slug: mailersend-domains-api
- description: The Email API from MailerSend — 1 operation(s) for email.
  name: MailerSend Email API
  slug: mailersend-email-api
- description: The Messages API from MailerSend — 2 operation(s) for messages.
  name: MailerSend Messages API
  slug: mailersend-messages-api
- description: The Sender Identities API from MailerSend — 1 operation(s) for sender identities.
  name: MailerSend Sender Identities API
  slug: mailersend-sender-identities-api
- description: The Templates API from MailerSend — 2 operation(s) for templates.
  name: MailerSend Templates API
  slug: mailersend-templates-api
- description: The Webhooks API from MailerSend — 2 operation(s) for webhooks.
  name: MailerSend Webhooks API
  slug: mailersend-webhooks-api
artifact_total: 27
asyncapis:
- description: ''
  name: Mailersend Webhooks
  slug: mailersend-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: MailerSend Bulk Email API
  slug: open-mailersend-bulk-email-api
- collection_type: open
  name: MailerSend Bulk Email Domains API
  slug: open-mailersend-domains-api
- collection_type: open
  name: MailerSend Bulk Email API
  slug: open-mailersend-email-api
- collection_type: open
  name: MailerSend Bulk Email Messages API
  slug: open-mailersend-messages-api
- collection_type: open
  name: MailerSend Bulk Email Sender Identities API
  slug: open-mailersend-sender-identities-api
- collection_type: open
  name: MailerSend Bulk Email Templates API
  slug: open-mailersend-templates-api
- collection_type: open
  name: MailerSend Bulk Email Webhooks API
  slug: open-mailersend-webhooks-api
- collection_type: open
  name: MailerSend API
  slug: open-mailersend
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/mailersend-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mailersend-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mailersend-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mailersend
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mailersend
- group: company
  title: ''
  type: Website
  url: https://www.mailersend.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.mailersend.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/mailersend-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/mailersend-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/mailersend-finops.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.mailersend.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.mailersend.com/api/v1/email
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.mailersend.com/sdk
- group: operate
  title: ''
  type: Support
  url: https://www.mailersend.com/help
- group: commercial
  title: ''
  type: Pricing
  url: https://www.mailersend.com/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.mailersend.com/legal/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.mailersend.com/
- group: build
  title: ''
  type: Packages
  url: packages/mailersend-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/mailersend-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/mailersend-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/mailersend-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/mailersend-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mailersend-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/mailersend-well-known.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/mailersend-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/mailersend-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/mailersend-problem-types.yml
- group: design
  title: ''
  type: ErrorCodes
  url: errors/mailersend-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/mailersend-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/mailersend-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/mailersend-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/mailersend-webhooks.yml
created: '2026-05-08'
description: MailerSend is a transactional email and SMS platform built for developers. Its v1 REST API covers email sending (single, bulk to 500 objects per request, and scheduled up to 72 hours out), SMTP relay, templates, sending domains and DNS verification, sender identities, recipients and five suppression lists, inbound routing, activity and analytics, email verification, DMARC and blocklist monitoring, SMS, and account/token administration. Authentication is a domain-scoped bearer token drawn from a 30-value scope vocabulary. MailerSend ships six official SDKs, an official Laravel driver, a Go CLI with an interactive TUI, a remote OAuth-protected MCP server exposing 127 tools, and its own published Agent Skill — but no machine-readable API contract and no idempotency guarantee.
finops:
- name: Mailersend Finops
  service_category: Email
  slug: mailersend-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mailersend.png
layout: provider
mcp_servers:
- description: ''
  name: MailerSend MCP Server
  slug: mailersend-mcp-server
modified: '2026-08-13'
name: MailerSend
nav: Providers
network: true
overview: 'MailerSend publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Bulk Email API, Domains API, Email API, and 4 more. Tagged areas include Email, Transactional Email, SMTP, Marketing, and Communications.


  The MailerSend catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  MailerSend''s developer surface includes authentication, documentation, API reference, getting-started guide, support, pricing, CLI, and 26 more developer resources.'
plans:
- name: Mailersend Plans Pricing
  plan_count: 5
  slug: mailersend-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 5
  name: Mailersend Rate Limits
  slug: mailersend-rate-limits
scopes:
- name: Mailersend Scopes
  scope_count: 30
  slug: mailersend-scopes
  summary_line: 30 scopes
score:
  band: strong
  composite: 61.3
  coverage:
    artifact_dirs: 23
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.2
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 4.5
    contract_quality: 59.1
    developer_ergonomics: 76.2
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 57.9
  previous_composite: 61.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 52.8
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mailersend/refs/heads/main/screenshots/mailersend-2026-06-20T184858.png
security:
- kind: authentication
  name: Mailersend Authentication
  slug: mailersend-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: Mailersend Domain Security
  slug: mailersend-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 1
skills:
- name: MailerSend
  slug: mailersend
slug: mailersend
tags:
- Email
- Transactional Email
- SMTP
- Marketing
- Communications
- SMS
- Messaging
- Templates
- Webhook
- Email Verification
- Deliverability
- Analytics
- MCP
website: https://www.mailersend.com/
---
