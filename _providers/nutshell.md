---
access_model:
  confidence: high
  label: Paid · Self-serve signup · Free trial
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - probed signup page
  trial: true
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 45.8
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 47
  human_in_the_loop: 0
  name: Nutshell Agentic Access
  operation_count: 116
  slug: nutshell-agentic-access
  summary_line: 116 operations · 47 acting
api_count: 27
apis:
- description: Nutshell's primary REST API — 87 paths and 112 operations across 24 resource families (accounts, contacts, leads, activities, notes, tasks, products, quotes, invoices, pipelines, tags, users and more)
  name: Nutshell REST API
  slug: rest-api
- description: Nutshell's original JSON-RPC API, available since 2010. Nutshell states it is no longer adding new endpoints to this API but continues to support existing customers, making it a maintenance-only surfa
  name: Nutshell Legacy JSON-RPC API
  slug: json-rpc
- description: 'A GraphQL endpoint served at https://app.nutshell.com/graphql. Nutshell''s API authentication guide names GraphQL alongside REST and JSON-RPC as an authenticated surface. Introspection is gated: an ano'
  name: Nutshell GraphQL API
  slug: graphql
- description: 'Companies and organizations you do business with (shown as Companies in the Nutshell UI): create, read, update, delete, undelete, list, custom fields, account types and industries. 13 operation(s) acr'
  name: Nutshell Accounts (Companies) API
  slug: nutshell-accounts-api
- description: Meetings, calls and logged interactions attached to Nutshell records, plus the activity type reference. 5 operation(s) across 3 path(s).
  name: Nutshell Activities API
  slug: nutshell-activities-api
- description: Email-marketing audiences — static lists of contacts used to organize people for marketing sends. 2 operation(s) across 1 path(s).
  name: Nutshell Audiences API
  slug: nutshell-audiences-api
- description: Competitor records and the lead-to-competitor relationships (competitor maps) attached to a lead. 6 operation(s) across 4 path(s).
  name: Nutshell Competitors API
  slug: nutshell-competitors-api
- description: 'People you do business with (shown as People in the Nutshell UI): create, read, update, delete, undelete, list and contact custom fields. 11 operation(s) across 8 path(s).'
  name: Nutshell Contacts (People) API
  slug: nutshell-contacts-api
- description: Marketing email editions — individual email sends and their metadata. 2 operation(s) across 2 path(s).
  name: Nutshell Editions API
  slug: nutshell-editions-api
- description: Individual email messages recorded against Nutshell records. 1 operation(s) across 1 path(s).
  name: Nutshell Emails API
  slug: nutshell-emails-api
- description: The Nutshell timeline/change-log feed, including a separate feed of deletion events. 2 operation(s) across 2 path(s).
  name: Nutshell Events (Timeline) API
  slug: nutshell-events-api
- description: Saved filters and lists used to scope list endpoints across the core Nutshell entities. 1 operation(s) across 1 path(s).
  name: Nutshell Filters API
  slug: nutshell-filters-api
- description: Nutshell Forms and their fields, including the field IDs used in each published form. 3 operation(s) across 3 path(s).
  name: Nutshell Forms API
  slug: nutshell-forms-api
- description: The industry reference list used to classify accounts. 1 operation(s) across 1 path(s).
  name: Nutshell Industries API
  slug: nutshell-industries-api
- description: Invoice documents, their status transitions and payment/completion metadata. 3 operation(s) across 3 path(s).
  name: Nutshell Invoices API
  slug: nutshell-invoices-api
- description: 'Sales opportunities: create, read, update, close, reopen, watch, stage and stageset assignment, installments, reports and lead custom fields. 25 operation(s) across 19 path(s).'
  name: Nutshell Leads API
  slug: nutshell-leads-api
- description: Market records used to segment Nutshell data. 2 operation(s) across 2 path(s).
  name: Nutshell Markets API
  slug: nutshell-markets-api
- description: Free-text notes attached to accounts, contacts and leads, with delete and undelete. 5 operation(s) across 3 path(s).
  name: Nutshell Notes API
  slug: nutshell-notes-api
- description: Pipelines (stagesets) and their stages, plus a CSV export of lead movement through a pipeline. 3 operation(s) across 3 path(s).
  name: Nutshell Pipelines (Stagesets) API
  slug: nutshell-pipelines-api
- description: Product categories used to group the products attached to leads and quotes. 3 operation(s) across 2 path(s).
  name: Nutshell Product Categories API
  slug: nutshell-product-categories-api
- description: The product catalog and product maps — instances of a product attached to a lead with quantity and custom pricing. 8 operation(s) across 6 path(s).
  name: Nutshell Products API
  slug: nutshell-products-api
- description: Quote documents, their status transitions, and creating an invoice from a quote. 4 operation(s) across 4 path(s).
  name: Nutshell Quotes API
  slug: nutshell-quotes-api
- description: Lead sources — how leads arrive at your website and learn about your business. 4 operation(s) across 3 path(s).
  name: Nutshell Sources API
  slug: nutshell-sources-api
- description: Tags used to group leads, contacts and accounts, with delete and undelete. 4 operation(s) across 3 path(s).
  name: Nutshell Tags API
  slug: nutshell-tags-api
- description: Tasks assigned to Nutshell users, including assignee updates. 5 operation(s) across 2 path(s).
  name: Nutshell Tasks API
  slug: nutshell-tasks-api
- description: Sales territories used to scope ownership of Nutshell records. 1 operation(s) across 1 path(s).
  name: Nutshell Territories API
  slug: nutshell-territories-api
- description: Nutshell users in the instance. 2 operation(s) across 2 path(s).
  name: Nutshell Users API
  slug: nutshell-users-api
artifact_total: 60
asyncapis:
- description: ''
  name: Nutshell Webhooks
  slug: nutshell-webhooks
collections:
- collection_type: open
  name: Nutshell Accounts (Companies) API
  slug: open-nutshell-accounts-api
- collection_type: open
  name: Nutshell Activities API
  slug: open-nutshell-activities-api
- collection_type: open
  name: Nutshell Audiences API
  slug: open-nutshell-audiences-api
- collection_type: open
  name: Nutshell Competitors API
  slug: open-nutshell-competitors-api
- collection_type: open
  name: Nutshell Contacts (People) API
  slug: open-nutshell-contacts-api
- collection_type: open
  name: Nutshell Editions API
  slug: open-nutshell-editions-api
- collection_type: open
  name: Nutshell Emails API
  slug: open-nutshell-emails-api
- collection_type: open
  name: Nutshell Events (Timeline) API
  slug: open-nutshell-events-api
- collection_type: open
  name: Nutshell Filter API
  slug: open-nutshell-filters-api
- collection_type: open
  name: Nutshell Forms API
  slug: open-nutshell-forms-api
- collection_type: open
  name: Nutshell Industries API
  slug: open-nutshell-industries-api
- collection_type: open
  name: Nutshell Invoices API
  slug: open-nutshell-invoices-api
- collection_type: open
  name: Nutshell Leads API
  slug: open-nutshell-leads-api
- collection_type: open
  name: Nutshell Markets API
  slug: open-nutshell-markets-api
- collection_type: open
  name: Nutshell Notes API
  slug: open-nutshell-notes-api
- collection_type: open
  name: Nutshell Stagesets (Pipelines) API
  slug: open-nutshell-pipelines-api
- collection_type: open
  name: Nutshell ProductCategories API
  slug: open-nutshell-product-categories-api
- collection_type: open
  name: Nutshell Products API
  slug: open-nutshell-products-api
- collection_type: open
  name: Nutshell Quotes API
  slug: open-nutshell-quotes-api
- collection_type: open
  name: Nutshell Sources API
  slug: open-nutshell-sources-api
- collection_type: open
  name: Nutshell Tags API
  slug: open-nutshell-tags-api
- collection_type: open
  name: Nutshell Tasks API
  slug: open-nutshell-tasks-api
- collection_type: open
  name: Nutshell Territories API
  slug: open-nutshell-territories-api
- collection_type: open
  name: Nutshell Users API
  slug: open-nutshell-users-api
common:
- group: company
  title: ''
  type: Website
  url: https://www.nutshell.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.nutshell.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.nutshell.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://developers.nutshell.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.nutshell.com/docs/getting-started
- group: start
  title: ''
  type: Quickstart
  url: https://developers.nutshell.com/docs/quickstart
- group: operate
  title: ''
  type: Support
  url: https://support.nutshell.com
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.nutshell.com
- group: company
  title: ''
  type: Blog
  url: https://www.nutshell.com/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://www.nutshell.com/feed
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/nutshellcrm
- group: commercial
  title: ''
  type: Pricing
  url: https://www.nutshell.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.nutshell.com/signup
- group: start
  title: ''
  type: Login
  url: https://app.nutshell.com/auth
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.nutshell.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.nutshell.com/legal/privacy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/nutshell-llc
- group: operate
  title: ''
  type: StatusPage
  url: https://status.nutshell.com
- group: design
  title: ''
  type: Webhooks
  url: https://developers.nutshell.com/docs/working-with-webhooks
- group: auth
  title: ''
  type: Compliance
  url: https://www.nutshell.com/security
- group: agent
  title: ''
  type: LlmsText
  url: https://developers.nutshell.com/llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/nutshell-llms.txt
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/nutshell-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/nutshell-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/nutshell-scopes.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nutshell-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/nutshell-trust-center.yml
- group: build
  title: ''
  type: Packages
  url: packages/nutshell-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/nutshell-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/nutshell-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/nutshell-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/nutshell-tool-crosswalk.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/nutshell-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/nutshell-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/nutshell-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/nutshell-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/nutshell-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/nutshell-sandbox.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/nutshell-changelog.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/nutshell-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/nutshell-rate-limits.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/nutshell-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-05-11'
description: Nutshell is a CRM and email-marketing platform for small and mid-sized B2B sales teams, combining pipeline management, contact and company records, activity tracking, reporting, sales automation and built-in outbound email campaigns in one workspace with mobile and desktop clients. For developers Nutshell publishes a documented REST API of 112 operations across 24 resource families at app.nutshell.com/rest, an authenticated GraphQL endpoint, a legacy JSON-RPC API kept alive for existing integrations, an outbound webhook firehose, read-only SQL access on the Enterprise plan, and a remote, OAuth-protected MCP server at app.nutshell.com/mcp that exposes read-only CRM context to AI assistants.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nutshell.png
layout: provider
mcp_servers:
- description: ''
  name: nutshell-mcp.yml
  slug: nutshell-mcpyml
modified: '2026-08-13'
name: Nutshell
nav: Providers
network: true
overview: 'Nutshell publishes 25 APIs on the [APIs.io](https://apis.io/) network, including REST API, Accounts (Companies) API, Activities API, and 22 more. Tagged areas include CRM, Sales, Pipeline Management, Email Marketing, and Contact Management.


  The Nutshell catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Nutshell''s developer surface includes documentation, API reference, getting-started guide, quickstart, support, engineering blog, pricing, and 36 more developer resources.'
plans:
- name: Nutshell Plans Pricing
  plan_count: 5
  slug: nutshell-plans-pricing
random_paper: 134
rate_limits:
- limit_count: 0
  name: Nutshell Rate Limits
  slug: nutshell-rate-limits
scopes:
- name: Nutshell Scopes
  scope_count: 0
  slug: nutshell-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 61.3
  delta: -5.1
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 30.3
    contract_quality: 62.0
    developer_ergonomics: 53.0
    discoverability: 81.5
    governance: 30.3
    operational_transparency: 38.2
  previous_composite: 66.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 24
    mcp: first-party
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/nutshell/refs/heads/main/screenshots/nutshell-2026-06-20T190536.png
security:
- kind: authentication
  name: Nutshell Authentication
  slug: nutshell-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Nutshell Domain Security
  slug: nutshell-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Nutshell Trust Center
  slug: nutshell-trust-center
  summary_line: SOC 2, GDPR
slug: nutshell
tags:
- CRM
- Sales
- Pipeline Management
- Email Marketing
- Contact Management
- Sales Automation
- Lead Management
- Marketing Automation
- MCP
- B2B
website: https://www.nutshell.com
---
