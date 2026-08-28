---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 32
  human_in_the_loop: 0
  name: Snov Io Agentic Access
  operation_count: 65
  slug: snov-io-agentic-access
  summary_line: 65 operations · 32 acting
api_count: 17
apis:
- description: Verify the deliverability and validity of up to 10 email addresses per request using a two-step async API. Returns validity status, MX record checks, and disposable email detection results.
  name: Snov.io Email Verification API
  slug: snovio-email-verification-api
- description: Create, update, delete, and manage multi-channel outreach campaigns programmatically. Supports email step content management, recipient management, campaign state changes, and full analytics reporting
  name: Snov.io Campaigns API
  slug: snovio-campaigns-api
- description: Add, search, and manage prospect records and lists within Snov.io. Supports custom fields, list creation, CRM pipeline management, and do-not-email suppression list operations.
  name: Snov.io Prospect Management API
  slug: snovio-prospect-management-api
- description: Create and manage email warm-up campaigns to improve deliverability scores. Supports full CRUD operations on warm-up campaigns and provides statistical reporting on warm-up progress.
  name: Snov.io Email Warm-up API
  slug: snovio-email-warm-up-api
- description: Subscribe to real-time event notifications from the Snov.io platform. Supports listing, creating, updating, and deleting webhook subscriptions for automated event-driven integrations.
  name: Snov.io Webhooks API
  slug: snovio-webhooks-api
- description: OAuth 2.0 token management
  name: Snov.io Authentication API
  slug: snov-io-authentication-api
- description: Create and manage multi-channel outreach campaigns
  name: Snov.io Campaigns API
  slug: snov-io-campaigns-api
- description: CRM pipeline and stage management
  name: Snov.io CRM Pipeline API
  slug: snov-io-crm-pipeline-api
- description: Search for company information and email addresses by domain
  name: Snov.io Domain Search API
  slug: snov-io-domain-search-api
- description: Manage sender email accounts
  name: Snov.io Email Accounts API
  slug: snov-io-email-accounts-api
- description: Find email addresses by name, LinkedIn, or domain
  name: Snov.io Email Finder API
  slug: snov-io-email-finder-api
- description: Verify email deliverability and validity
  name: Snov.io Email Verification API
  slug: snov-io-email-verification-api
- description: Manage email warm-up campaigns for improved deliverability
  name: Snov.io Email Warm-up API
  slug: snov-io-email-warm-up-api
- description: Manage prospect records and lists
  name: Snov.io Prospects API
  slug: snov-io-prospects-api
- description: User account management
  name: Snov.io User API
  slug: snov-io-user-api
- description: Real-time event webhook subscriptions
  name: Snov.io Webhooks API
  slug: snov-io-webhooks-api
- description: 'First-party remote Model Context Protocol server exposing 100+ Snov.io actions to AI assistants — prospect search and enrichment, list and folder management, email verification, Sales CRM (pipelines, '
  name: Snov.io Outreach MCP Server
  slug: snov-io-mcp-server
artifact_total: 46
asyncapis:
- description: ''
  name: Snov Io Webhooks
  slug: snov-io-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Snov.io Authentication API
  slug: open-snov-io-authentication-api
- collection_type: open
  name: Snov.io Authentication Campaigns API
  slug: open-snov-io-campaigns-api
- collection_type: open
  name: Snov.io Authentication CRM Pipeline API
  slug: open-snov-io-crm-pipeline-api
- collection_type: open
  name: Snov.io Authentication Domain Search API
  slug: open-snov-io-domain-search-api
- collection_type: open
  name: Snov.io Authentication Email Accounts API
  slug: open-snov-io-email-accounts-api
- collection_type: open
  name: Snov.io Authentication Email Finder API
  slug: open-snov-io-email-finder-api
- collection_type: open
  name: Snov.io Authentication Email Verification API
  slug: open-snov-io-email-verification-api
- collection_type: open
  name: Snov.io Authentication Email Verifier API
  slug: open-snov-io-email-verifier-api
- collection_type: open
  name: Snov.io Authentication Email Warm-up API
  slug: open-snov-io-email-warm-up-api
- collection_type: open
  name: Snov.io Authentication Enrichment API
  slug: open-snov-io-enrichment-api
- collection_type: open
  name: Snov.io Authentication Prospects API
  slug: open-snov-io-prospects-api
- collection_type: open
  name: Snov.io Authentication Sender Accounts API
  slug: open-snov-io-sender-accounts-api
- collection_type: open
  name: Snov.io Authentication User API
  slug: open-snov-io-user-api
- collection_type: open
  name: Snov.io Authentication Warm-up API
  slug: open-snov-io-warm-up-api
- collection_type: open
  name: Snov.io Authentication Webhooks API
  slug: open-snov-io-webhooks-api
- collection_type: open
  name: Snov.io API
  slug: open-snov
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/snov-io-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/snov-io-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/snov-io-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://snov.io/
- group: docs
  title: ''
  type: Documentation
  url: https://snov.io/api
- group: other
  title: ''
  type: Knowledgebase
  url: https://snov.io/knowledgebase/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/devsnovio
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/snovio
- group: company
  title: ''
  type: Blog
  url: https://snov.io/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://snov.io/pricing
- group: other
  title: ''
  type: X
  url: https://x.com/snov_io
- group: auth
  title: ''
  type: Authentication
  url: https://snov.io/knowledgebase/how-to-use-snov-io-api/
- group: commercial
  title: ''
  type: Plans
  url: plans/snov-io-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/snov-io-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/snov-io-finops.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/snov-io-scopes.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/snov-io-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/snov-io-tool-crosswalk.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/snov-io-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/snov-io-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/snov-io-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/snov-io-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/snov-io-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/snov-io-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/snov-io-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/snov-io-trust-center.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/snov-io-trust-center.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/snov-io-data-model.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/snov-io-changelog.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/snov-io-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: docs
  title: ''
  type: GraphQL
  url: graphql/snov-io-graphql.md
- group: docs
  title: ''
  type: APIReference
  url: https://snov.io/api
- group: start
  title: ''
  type: DeveloperPortal
  url: https://snov.io/api
- group: start
  title: ''
  type: GettingStarted
  url: https://snov.io/knowledgebase/how-to-use-snov-io-api/
- group: operate
  title: ''
  type: Support
  url: https://snov.io/contact-us
- group: operate
  title: ''
  type: HelpCenter
  url: https://snov.io/knowledgebase/
- group: start
  title: ''
  type: SignUp
  url: https://app.snov.io/register
- group: start
  title: ''
  type: Login
  url: https://app.snov.io/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://snov.io/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://snov.io/privacy-policy
- group: auth
  title: ''
  type: SecurityCenter
  url: https://snov.io/security-center
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://snov.io/release-notes
created: '2026-06-12'
description: Snov.io is a sales automation and lead generation platform serving over 300,000 companies across 180+ countries. The platform provides a REST API enabling developers to programmatically access email finding, domain search, email verification, drip campaign management, and LinkedIn prospect automation. Authentication uses OAuth 2.0 client credentials to obtain short-lived Bearer tokens, and all API operations consume credits from the account balance. The API covers the full sales outreach lifecycle from prospect discovery and contact enrichment through multi-channel campaign execution and CRM pipeline management. Snov.io also operates a first-party remote Model Context Protocol server at https://mcp.snov.io/mcp, documented as exposing more than 100 actions to AI assistants and gated by a separate OAuth authorization code flow with PKCE and dynamic client registration. The two surfaces are disjoint — campaigns, warm-up, sender accounts and webhooks are REST-only, while Sales CRM
  writes and all LinkedIn outreach actions are reachable only over MCP.
finops:
- name: Snov Io Finops
  service_category: ''
  slug: snov-io-finops
graphqls:
- description: Snov.io is a sales automation and lead generation platform serving over 300,000 companies across 180+ countries. Its REST API covers the full outreach lifecycle — prospect discovery, email finding, em
  name: Snov.io GraphQL Schema
  slug: snov-io-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/snov-io.png
jsonld:
- class_count: 11
  name: Snov Io Context
  property_count: 28
  slug: snov-io-context
layout: provider
mcp_servers:
- description: Snov.io ships a first-party REMOTE Model Context Protocol server at https://mcp.snov.io/mcp. It is a hosted HTTP endpoint an MCP client POSTs to directly — there is no npx package, no stdio binary and
  name: Snov.io Outreach MCP Server
  slug: snovio-outreach-mcp-server
modified: '2026-08-13'
name: Snov.io
nav: Providers
network: true
overview: 'Snov.io publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Campaigns API, CRM Pipeline API, and 8 more. Tagged areas include Sales Automation, Email Finder, Email Verification, Lead Generation, and Drip Campaigns.


  The Snov.io catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 JSON-LD context.


  Snov.io''s developer surface includes authentication, documentation, engineering blog, pricing, changelog, API reference, getting-started guide, and 36 more developer resources.'
plans:
- name: Snov Io Plans Pricing
  plan_count: 7
  slug: snov-io-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 3
  name: Snov Io Rate Limits
  slug: snov-io-rate-limits
scopes:
- name: Snov Io Scopes
  scope_count: 0
  slug: snov-io-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: exemplar
  composite: 67.8
  delta: 0.0
  facets:
    access_clarity: 93.4
    commercial_clarity: 93.4
    contract_governance: 30.3
    contract_quality: 75.1
    developer_ergonomics: 58.9
    discoverability: 74.1
    governance: 30.3
    operational_transparency: 57.9
  previous_composite: 67.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
    mcp: first-party
    skills: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/snov-io/refs/heads/main/screenshots/snov-io-2026-06-20T194107.png
security:
- kind: authentication
  name: Snov Io Authentication
  slug: snov-io-authentication
  summary_line: oauth2/http · 3 schemes
- kind: domain-security
  name: Snov Io Domain Security
  slug: snov-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Snov Io Trust Center
  slug: snov-io-trust-center
  summary_line: GDPR, LOA (Letter of Authorization), CCPA / Do Not Sell My Personal Information
slug: snov-io
tags:
- Sales Automation
- Email Finder
- Email Verification
- Lead Generation
- Drip Campaigns
- CRM
- LinkedIn Automation
- Prospect Management
- Data Enrichment
- Cold Email
website: https://snov.io/
---
