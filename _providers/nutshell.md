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
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 47
  human_in_the_loop: 0
  name: Nutshell Agentic Access
  operation_count: 116
  slug: nutshell-agentic-access
  summary_line: 116 operations · 47 acting
api_count: 7
apis:
- description: Nutshell's original JSON-RPC API, available since 2010. Nutshell states it is no longer adding new endpoints to this API but continues to support existing customers, making it a maintenance-only surfa
  name: Nutshell Legacy JSON-RPC API
  slug: json-rpc
- description: 'A GraphQL endpoint served at https://app.nutshell.com/graphql. Nutshell''s API authentication guide names GraphQL alongside REST and JSON-RPC as an authenticated surface. Introspection is gated: an ano'
  name: Nutshell GraphQL API
  slug: graphql
- baseURL: https://app.nutshell.com/rest
  baseurl_source: declared
  description: Meetings, calls and logged interactions attached to Nutshell records, plus the activity type reference. 5 operation(s) across 3 path(s).
  name: Nutshell Activities API
  slug: nutshell-activities-api
- baseURL: https://app.nutshell.com/rest
  baseurl_source: declared
  description: Email-marketing audiences — static lists of contacts used to organize people for marketing sends. 2 operation(s) across 1 path(s).
  name: Nutshell Audiences API
  slug: nutshell-audiences-api
- baseURL: https://app.nutshell.com/rest
  baseurl_source: declared
  description: Competitor records and the lead-to-competitor relationships (competitor maps) attached to a lead. 6 operation(s) across 4 path(s).
  name: Nutshell Competitors API
  slug: nutshell-competitors-api
- baseURL: https://app.nutshell.com/rest
  baseurl_source: declared
  description: Marketing email editions — individual email sends and their metadata. 2 operation(s) across 2 path(s).
  name: Nutshell Editions API
  slug: nutshell-editions-api
- baseURL: https://app.nutshell.com/rest
  baseurl_source: declared
  description: Individual email messages recorded against Nutshell records. 1 operation(s) across 1 path(s).
  name: Nutshell Emails API
  slug: nutshell-emails-api
- baseURL: https://app.nutshell.com/rest
  baseurl_source: declared
  description: Nutshell Forms and their fields, including the field IDs used in each published form. 3 operation(s) across 3 path(s).
  name: Nutshell Forms API
  slug: nutshell-forms-api
- baseURL: https://app.nutshell.com/rest
  baseurl_source: declared
  description: The industry reference list used to classify accounts. 1 operation(s) across 1 path(s).
  name: Nutshell Industries API
  slug: nutshell-industries-api
- baseURL: https://app.nutshell.com/rest
  baseurl_source: declared
  description: Invoice documents, their status transitions and payment/completion metadata. 3 operation(s) across 3 path(s).
  name: Nutshell Invoices API
  slug: nutshell-invoices-api
- baseURL: https://app.nutshell.com/rest
  baseurl_source: declared
  description: 'Sales opportunities: create, read, update, close, reopen, watch, stage and stageset assignment, installments, reports and lead custom fields. 25 operation(s) across 19 path(s).'
  name: Nutshell Leads API
  slug: nutshell-leads-api
- baseURL: https://app.nutshell.com/rest
  baseurl_source: declared
  description: Market records used to segment Nutshell data. 2 operation(s) across 2 path(s).
  name: Nutshell Markets API
  slug: nutshell-markets-api
- baseURL: https://app.nutshell.com/rest
  baseurl_source: declared
  description: Free-text notes attached to accounts, contacts and leads, with delete and undelete. 5 operation(s) across 3 path(s).
  name: Nutshell Notes API
  slug: nutshell-notes-api
- baseURL: https://app.nutshell.com/rest
  baseurl_source: declared
  description: The product catalog and product maps — instances of a product attached to a lead with quantity and custom pricing. 8 operation(s) across 6 path(s).
  name: Nutshell Products API
  slug: nutshell-products-api
- baseURL: https://app.nutshell.com/rest
  baseurl_source: declared
  description: Quote documents, their status transitions, and creating an invoice from a quote. 4 operation(s) across 4 path(s).
  name: Nutshell Quotes API
  slug: nutshell-quotes-api
- baseURL: https://app.nutshell.com/rest
  baseurl_source: declared
  description: Lead sources — how leads arrive at your website and learn about your business. 4 operation(s) across 3 path(s).
  name: Nutshell Sources API
  slug: nutshell-sources-api
- baseURL: https://app.nutshell.com/rest
  baseurl_source: declared
  description: Tags used to group leads, contacts and accounts, with delete and undelete. 4 operation(s) across 3 path(s).
  name: Nutshell Tags API
  slug: nutshell-tags-api
- baseURL: https://app.nutshell.com/rest
  baseurl_source: declared
  description: Tasks assigned to Nutshell users, including assignee updates. 5 operation(s) across 2 path(s).
  name: Nutshell Tasks API
  slug: nutshell-tasks-api
- baseURL: https://app.nutshell.com/rest
  baseurl_source: declared
  description: Sales territories used to scope ownership of Nutshell records. 1 operation(s) across 1 path(s).
  name: Nutshell Territories API
  slug: nutshell-territories-api
- baseURL: https://app.nutshell.com/rest
  baseurl_source: declared
  description: Nutshell users in the instance. 2 operation(s) across 2 path(s).
  name: Nutshell Users API
  slug: nutshell-users-api
- baseURL: https://app.nutshell.com/rest
  baseurl_source: declared
  description: The Accounts (Companies) API from Nutshell — 10 operation(s) for accounts (companies).
  name: Nutshell Accounts (Companies) API
  slug: nutshell-accounts-companies-api
- baseURL: https://app.nutshell.com/rest
  baseurl_source: declared
  description: The Contacts (People) API from Nutshell — 8 operation(s) for contacts (people).
  name: Nutshell Contacts (People) API
  slug: nutshell-contacts-people-api
- baseURL: https://app.nutshell.com/rest
  baseurl_source: declared
  description: The Events (Timeline) API from Nutshell — 2 operation(s) for events (timeline).
  name: Nutshell Events (Timeline) API
  slug: nutshell-events-timeline-api
- baseURL: https://app.nutshell.com/rest
  baseurl_source: declared
  description: The Filter API from Nutshell — 1 operation(s) for filter.
  name: Nutshell Filter API
  slug: nutshell-filter-api
- baseURL: https://app.nutshell.com/rest
  baseurl_source: declared
  description: The ProductCategories API from Nutshell — 2 operation(s) for productcategories.
  name: Nutshell Product Categories API
  slug: nutshell-productcategories-api
- baseURL: https://app.nutshell.com/rest
  baseurl_source: declared
  description: The Stagesets (Pipelines) API from Nutshell — 3 operation(s) for stagesets (pipelines).
  name: Nutshell Stagesets (Pipelines) API
  slug: nutshell-stagesets-pipelines-api
artifact_total: 59
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
- group: other
  title: ''
  type: Overlay
  url: overlays/nutshell-accounts-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/nutshell-contacts-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/nutshell-events-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/nutshell-filters-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/nutshell-pipelines-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/nutshell-product-categories-overlay.yaml
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
  name: Nutshell MCP server
  slug: nutshell-mcp-server
modified: '2026-08-13'
name: Nutshell
nav: Providers
network: true
overview: 'Nutshell publishes 24 APIs on the [APIs.io](https://apis.io/) network, including Activities API, Audiences API, Competitors API, and 21 more. Tagged areas include CRM, Sales, Pipeline Management, Email Marketing, and Contact Management.


  The Nutshell catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Nutshell''s developer surface includes documentation, API reference, getting-started guide, quickstart, support, engineering blog, pricing, and 42 more developer resources.'
plans:
- name: Nutshell Plans Pricing
  plan_count: 5
  slug: nutshell-plans-pricing
random_paper: 18
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
  composite: 59.2
  coverage:
    artifact_dirs: 24
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 18.2
    contract_quality: 59.6
    developer_ergonomics: 53.0
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 38.2
  previous_composite: 59.2
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
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
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
