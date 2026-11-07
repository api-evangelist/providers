---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: templated
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 43.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 18
  human_in_the_loop: 0
  name: Microsoft Dynamics 365 Sales Agentic Access
  operation_count: 31
  slug: microsoft-dynamics-365-sales-agentic-access
  summary_line: 31 operations · 18 acting
api_count: 1
apis:
- description: OData v4.0 RESTful Web API for Microsoft Dataverse used to create, read, update, and delete Dynamics 365 Sales records (leads, opportunities, accounts, contacts, quotes, orders, invoices, products) an
  name: Microsoft Dataverse Web API (Dynamics 365 Sales)
  slug: dataverse-web-api
- baseURL: https://{org}.api.crm.dynamics.com/api/data/v9.2
  baseurl_source: declared
  description: Account (customer organization) records
  name: Microsoft Dynamics 365 Sales Accounts API
  phrasing_intents:
  - id: accounts_list
    intent: Search and list customer accounts
    question: How can I pull a list of all my customer accounts from Dynamics 365 Sales?
  - id: accounts_create
    intent: Create a new customer account
    question: How do I add a new company account to my CRM?
  - id: accounts_get
    intent: Look up a single account by ID
    question: How do I fetch the full details of one specific account?
  - id: accounts_update
    intent: Update an existing account
    question: How do I change the phone number or address on an existing account?
  - id: accounts_delete
    intent: Delete an account
    question: How do I permanently remove an account from the CRM?
  phrasing_ops: 5
  slug: microsoft-dynamics-365-sales-accounts-api
- baseURL: https://{org}.api.crm.dynamics.com/api/data/v9.2
  baseurl_source: declared
  description: The $batch API from Microsoft Dynamics 365 Sales — 1 operation(s) for $batch.
  name: Microsoft Dynamics 365 Sales $batch API
  phrasing_intents:
  - id: batch_execute
    intent: Run several CRM operations in one batch
    question: How can I send multiple Dynamics 365 Sales Web API requests in a single HTTP call?
  phrasing_ops: 1
  slug: microsoft-dynamics-365-sales-batch-api
- baseURL: https://{org}.api.crm.dynamics.com/api/data/v9.2
  baseurl_source: declared
  description: Contact (person) records
  name: Microsoft Dynamics 365 Sales Contacts API
  phrasing_intents:
  - id: contacts_list
    intent: Search and list contacts
    question: How do I get a list of the people in my CRM contacts?
  - id: contacts_create
    intent: Add a new contact
    question: How do I add a new person as a contact in Dynamics 365 Sales?
  - id: contacts_get
    intent: Look up a single contact by ID
    question: Where can I see everything stored on one contact?
  - id: contacts_update
    intent: Update an existing contact
    question: What's the way to correct details on a contact that already exists?
  - id: contacts_delete
    intent: Delete a contact
    question: How do I permanently remove a contact from the CRM?
  phrasing_ops: 5
  slug: microsoft-dynamics-365-sales-contacts-api
- baseURL: https://{org}.api.crm.dynamics.com/api/data/v9.2
  baseurl_source: declared
  description: Invoice records
  name: Microsoft Dynamics 365 Sales Invoices API
  phrasing_intents:
  - id: invoices_list
    intent: List invoices
    question: How do I see all invoices in Dynamics 365 Sales?
  - id: invoices_create
    intent: Create an invoice
    question: How do I create a new invoice record?
  phrasing_ops: 2
  slug: microsoft-dynamics-365-sales-invoices-api
- baseURL: https://{org}.api.crm.dynamics.com/api/data/v9.2
  baseurl_source: declared
  description: Sales lead records
  name: Microsoft Dynamics 365 Sales Leads API
  phrasing_intents:
  - id: leads_list
    intent: Search and list leads
    question: How do I get a list of my sales leads from Dynamics 365?
  - id: leads_create
    intent: Capture a new lead
    question: How do I add a new prospect as a lead?
  - id: leads_get
    intent: Look up a single lead by ID
    question: Where can I see the full record for one lead?
  - id: leads_update
    intent: Update an existing lead
    question: What's the way to correct details on a lead that already exists?
  - id: leads_delete
    intent: Delete a lead
    question: How do I permanently remove a lead?
  phrasing_ops: 5
  slug: microsoft-dynamics-365-sales-leads-api
- baseURL: https://{org}.api.crm.dynamics.com/api/data/v9.2
  baseurl_source: declared
  description: Sales opportunity records
  name: Microsoft Dynamics 365 Sales Opportunities API
  phrasing_intents:
  - id: opportunities_list
    intent: List sales opportunities
    question: How do I see all the deals in my Dynamics 365 Sales pipeline?
  - id: opportunities_create
    intent: Create a sales opportunity
    question: How do I add a new deal to the pipeline?
  - id: opportunities_get
    intent: Look up a single opportunity by ID
    question: Where can I see the full record for one deal?
  - id: opportunities_update
    intent: Update an existing opportunity
    question: What's the way to correct details on a deal already in the pipeline?
  - id: opportunities_delete
    intent: Delete an opportunity
    question: How do I permanently remove a deal from the pipeline?
  phrasing_ops: 5
  slug: microsoft-dynamics-365-sales-opportunities-api
- baseURL: https://{org}.api.crm.dynamics.com/api/data/v9.2
  baseurl_source: declared
  description: Product records
  name: Microsoft Dynamics 365 Sales Products API
  phrasing_intents:
  - id: products_list
    intent: List products in the catalog
    question: How do I see every product in my Dynamics 365 Sales catalog?
  - id: products_create
    intent: Add a product to the catalog
    question: How do I add a new product I sell to the catalog?
  phrasing_ops: 2
  slug: microsoft-dynamics-365-sales-products-api
- baseURL: https://{org}.api.crm.dynamics.com/api/data/v9.2
  baseurl_source: declared
  description: Sales quote records
  name: Microsoft Dynamics 365 Sales Quotes API
  phrasing_intents:
  - id: quotes_list
    intent: List sales quotes
    question: How do I see all quotes sent to customers in Dynamics 365 Sales?
  - id: quotes_create
    intent: Create a sales quote
    question: How do I create a new quote for a customer?
  phrasing_ops: 2
  slug: microsoft-dynamics-365-sales-quotes-api
- baseURL: https://{org}.api.crm.dynamics.com/api/data/v9.2
  baseurl_source: declared
  description: Activity tasks
  name: Microsoft Dynamics 365 Sales Tasks API
  phrasing_intents:
  - id: tasks_list
    intent: List follow-up tasks
    question: How do I see all tasks in Dynamics 365 Sales?
  - id: tasks_create
    intent: Create a follow-up task
    question: How do I create a follow-up task for a sales rep?
  phrasing_ops: 2
  slug: microsoft-dynamics-365-sales-tasks-api
- description: Microsoft's hosted Model Context Protocol server for Dynamics 365 Sales. Exposes 20 sales tools to any MCP-capable agent — lead and account research, competitor research, engagement summaries, lead qu
  name: Dynamics 365 Sales MCP Server
  slug: dynamics-365-sales-mcp-server
- baseURL: https://{org}.api.crm.dynamics.com/api/data/v9.2
  baseurl_source: declared
  description: Sales order records
  name: Microsoft Dynamics 365 Sales Sales Orders API
  phrasing_intents:
  - id: salesorders_list
    intent: List sales orders
    question: How do I see all sales orders in Dynamics 365 Sales?
  - id: salesorders_create
    intent: Create a sales order
    question: How do I record a new customer order?
  phrasing_ops: 2
  slug: microsoft-dynamics-365-sales-sales-orders-api
artifact_total: 43
asyncapis:
- description: ''
  name: Microsoft Dynamics 365 Sales Webhooks
  slug: microsoft-dynamics-365-sales-webhooks
collections:
- collection_type: open
  name: Microsoft Dataverse Web API (Dynamics 365 Sales) Accounts API
  slug: open-microsoft-dynamics-365-sales-accounts-api
- collection_type: open
  name: Microsoft Dataverse Web API (Dynamics 365 Sales) Accounts $batch API
  slug: open-microsoft-dynamics-365-sales-batch-api
- collection_type: open
  name: Microsoft Dataverse Web API (Dynamics 365 Sales) Accounts Contacts API
  slug: open-microsoft-dynamics-365-sales-contacts-api
- collection_type: open
  name: Microsoft Dataverse Web API (Dynamics 365 Sales) Accounts Invoices API
  slug: open-microsoft-dynamics-365-sales-invoices-api
- collection_type: open
  name: Microsoft Dataverse Web API (Dynamics 365 Sales) Accounts Leads API
  slug: open-microsoft-dynamics-365-sales-leads-api
- collection_type: open
  name: Microsoft Dataverse Web API (Dynamics 365 Sales) Accounts Opportunities API
  slug: open-microsoft-dynamics-365-sales-opportunities-api
- collection_type: open
  name: Microsoft Dataverse Web API (Dynamics 365 Sales) Accounts Products API
  slug: open-microsoft-dynamics-365-sales-products-api
- collection_type: open
  name: Microsoft Dataverse Web API (Dynamics 365 Sales) Accounts Quotes API
  slug: open-microsoft-dynamics-365-sales-quotes-api
- collection_type: open
  name: Microsoft Dataverse Web API (Dynamics 365 Sales) Accounts SalesOrders API
  slug: open-microsoft-dynamics-365-sales-salesorders-api
- collection_type: open
  name: Microsoft Dataverse Web API (Dynamics 365 Sales) Accounts Tasks API
  slug: open-microsoft-dynamics-365-sales-tasks-api
- collection_type: open
  name: Microsoft Dataverse Web API (Dynamics 365 Sales)
  slug: open-microsoft-dynamics-365-sales
common:
- group: commercial
  href: https://artifacts.apis.io/microsoft-dynamics-365-sales/finops/microsoft-dynamics-365-sales-finops.yml
  title: ''
  type: FinOps
  url: finops/microsoft-dynamics-365-sales-finops.yml
- group: design
  href: https://artifacts.apis.io/microsoft-dynamics-365-sales/rules/microsoft-dynamics-365-sales-rules.yml
  title: ''
  type: Spectral
  url: rules/microsoft-dynamics-365-sales-rules.yml
- group: design
  href: https://artifacts.apis.io/microsoft-dynamics-365-sales/json-ld/microsoft-dynamics-365-sales-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/microsoft-dynamics-365-sales-context.jsonld
- group: design
  href: https://artifacts.apis.io/microsoft-dynamics-365-sales/vocabulary/microsoft-dynamics-365-sales-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/microsoft-dynamics-365-sales-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/microsoft-dynamics-365-sales/conventions/microsoft-dynamics-365-sales-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/microsoft-dynamics-365-sales-conventions.yml
- group: other
  href: https://artifacts.apis.io/microsoft-dynamics-365-sales/hosts/microsoft-dynamics-365-sales-hosts.yml
  title: ''
  type: Hosts
  url: hosts/microsoft-dynamics-365-sales-hosts.yml
- group: build
  href: https://artifacts.apis.io/microsoft-dynamics-365-sales/integrations/microsoft-dynamics-365-sales-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/microsoft-dynamics-365-sales-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/microsoft-dynamics-365-sales/vendors/microsoft-dynamics-365-sales-vendors.yml
  title: ''
  type: Vendors
  url: vendors/microsoft-dynamics-365-sales-vendors.yml
- group: other
  title: ''
  type: Leadership
  url: https://news.microsoft.com/leadership
- group: other
  href: https://artifacts.apis.io/microsoft-dynamics-365-sales/capabilities/microsoft-dynamics-365-sales-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/microsoft-dynamics-365-sales-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/microsoft-dynamics-365-sales/overlays/microsoft-dynamics-365-sales-salesorders-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/microsoft-dynamics-365-sales-salesorders-api-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/microsoft-dynamics-365-sales/agentic-access/microsoft-dynamics-365-sales-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-dynamics-365-sales-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-dynamics-365-sales/security/microsoft-dynamics-365-sales-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/microsoft-dynamics-365-sales-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-dynamics-365-sales/security/microsoft-dynamics-365-sales-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/microsoft-dynamics-365-sales-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-dynamics-365-sales/security/microsoft-dynamics-365-sales-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/microsoft-dynamics-365-sales-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-dynamics-365-sales/authentication/microsoft-dynamics-365-sales-authentication.yml
  title: ''
  type: Authentication
  url: authentication/microsoft-dynamics-365-sales-authentication.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-dynamics-365-sales/scopes/microsoft-dynamics-365-sales-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-dynamics-365-sales-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/MicrosoftDocs
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/microsoft-dynamics-365-sales
- group: company
  title: ''
  type: Website
  url: https://www.microsoft.com/en-us/dynamics-365/products/sales
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/dynamics365/sales/
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/power-apps/developer/data-platform/webapi/overview
- group: commercial
  title: ''
  type: Pricing
  url: https://www.microsoft.com/en-us/dynamics-365/products/sales/pricing
- group: start
  title: ''
  type: SignUp
  url: https://dynamics.microsoft.com/en-us/sales/overview/
- group: company
  title: ''
  type: Blog
  url: https://www.microsoft.com/en-us/dynamics-365/blog/feed/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://learn.microsoft.com/en-us/power-apps/developer/data-platform/overview
- group: docs
  title: ''
  type: APIReference
  url: https://learn.microsoft.com/en-us/power-apps/developer/data-platform/webapi/reference/about
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/power-apps/developer/data-platform/webapi/perform-operations-web-api
- group: operate
  title: ''
  type: Support
  url: https://www.microsoft.com/en-us/dynamics-365/support
- group: operate
  title: ''
  type: Community
  url: https://community.dynamics.com/forums/thread/?groupid=d365sales
- group: operate
  title: ''
  type: Roadmap
  url: https://learn.microsoft.com/en-us/dynamics365/release-plans/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.microsoft.com/en-us/servicesagreement/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: operate
  title: ''
  type: SLA
  url: https://www.microsoft.com/licensing/docs/view/Service-Level-Agreements-SLA-for-Online-Services
- group: build
  href: https://artifacts.apis.io/microsoft-dynamics-365-sales/packages/microsoft-dynamics-365-sales-packages.yml
  title: ''
  type: Packages
  url: packages/microsoft-dynamics-365-sales-packages.yml
- group: build
  href: https://artifacts.apis.io/microsoft-dynamics-365-sales/packages/microsoft-dynamics-365-sales-packages.yml
  title: ''
  type: SDKs
  url: packages/microsoft-dynamics-365-sales-packages.yml
- group: build
  href: https://artifacts.apis.io/microsoft-dynamics-365-sales/cli/microsoft-dynamics-365-sales-cli.yml
  title: ''
  type: CLI
  url: cli/microsoft-dynamics-365-sales-cli.yml
- group: agent
  href: https://artifacts.apis.io/microsoft-dynamics-365-sales/mcp/microsoft-dynamics-365-sales-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/microsoft-dynamics-365-sales-mcp.yml
- group: build
  href: https://artifacts.apis.io/microsoft-dynamics-365-sales/mcp/microsoft-dynamics-365-sales-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/microsoft-dynamics-365-sales-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/microsoft-dynamics-365-sales/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/microsoft-dynamics-365-sales/llms/microsoft-dynamics-365-sales-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/microsoft-dynamics-365-sales-llms.txt
- group: agent
  href: https://artifacts.apis.io/microsoft-dynamics-365-sales/well-known/microsoft-dynamics-365-sales-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/microsoft-dynamics-365-sales-well-known.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-dynamics-365-sales/well-known/microsoft-dynamics-365-sales-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/microsoft-dynamics-365-sales-security.txt
- group: auth
  title: ''
  type: Security
  url: https://www.microsoft.com/en-us/msrc/cvd
- group: auth
  title: ''
  type: Compliance
  url: https://www.microsoft.com/en-us/trust-center/compliance/compliance-overview
- group: design
  href: https://artifacts.apis.io/microsoft-dynamics-365-sales/conformance/microsoft-dynamics-365-sales-conformance.yml
  title: ''
  type: Conformance
  url: conformance/microsoft-dynamics-365-sales-conformance.yml
- group: design
  href: https://artifacts.apis.io/microsoft-dynamics-365-sales/conventions/microsoft-dynamics-365-sales-conventions.yml
  title: ''
  type: Conventions
  url: conventions/microsoft-dynamics-365-sales-conventions.yml
- group: design
  href: https://artifacts.apis.io/microsoft-dynamics-365-sales/errors/microsoft-dynamics-365-sales-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/microsoft-dynamics-365-sales-problem-types.yml
- group: design
  href: https://artifacts.apis.io/microsoft-dynamics-365-sales/data-model/microsoft-dynamics-365-sales-data-model.yml
  title: ''
  type: DataModel
  url: data-model/microsoft-dynamics-365-sales-data-model.yml
- group: design
  href: https://artifacts.apis.io/microsoft-dynamics-365-sales/lifecycle/microsoft-dynamics-365-sales-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/microsoft-dynamics-365-sales-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cloud.microsoft/
- group: operate
  title: ''
  type: Deprecation
  url: https://learn.microsoft.com/en-us/power-platform/important-changes-coming
- group: operate
  href: https://artifacts.apis.io/microsoft-dynamics-365-sales/changelog/microsoft-dynamics-365-sales-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/microsoft-dynamics-365-sales-changelog.yml
- group: start
  href: https://artifacts.apis.io/microsoft-dynamics-365-sales/sandbox/microsoft-dynamics-365-sales-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/microsoft-dynamics-365-sales-sandbox.yml
- group: design
  href: https://artifacts.apis.io/microsoft-dynamics-365-sales/asyncapi/microsoft-dynamics-365-sales-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/microsoft-dynamics-365-sales-webhooks.yml
- group: commercial
  href: https://artifacts.apis.io/microsoft-dynamics-365-sales/plans/microsoft-dynamics-365-sales-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/microsoft-dynamics-365-sales-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/microsoft-dynamics-365-sales/rate-limits/microsoft-dynamics-365-sales-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/microsoft-dynamics-365-sales-rate-limits.yml
created: '2026-05-11'
description: Microsoft Dynamics 365 Sales is Microsoft's enterprise CRM application for managing leads, opportunities, accounts, contacts, sales pipelines, forecasts, and customer relationships, built on the Microsoft Dataverse platform and integrated with Microsoft 365, Teams, Copilot, and Power Platform. Developers programmatically interact with Dynamics 365 Sales data through the Dataverse Web API, an OData v4.0 RESTful interface that exposes every table, action, and function in a Sales environment. The Dataverse Web API uses OAuth 2.0 (Microsoft Entra ID) Bearer token authentication and is reached at a per-environment endpoint such as https://{org}.api.crm.dynamics.com/api/data/v9.2/.
finops:
- has_sources: true
  method: derived
  name: Microsoft Dynamics 365 Sales Finops
  primary_unit: user
  service_category: ''
  slug: microsoft-dynamics-365-sales-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-dynamics-365-sales.png
json_schemas:
- name: AccountCollection
  property_count: 3
  slug: microsoft-dynamics-365-sales-account-collection
- name: Account
  property_count: 17
  slug: microsoft-dynamics-365-sales-account
jsonld:
- class_count: 2
  name: Microsoft Dynamics 365 Sales Context
  property_count: 17
  slug: microsoft-dynamics-365-sales-context
layout: provider
mcp_servers:
- description: Remote MCP server at agent365.svc.cloud.microsoft requiring OAuth; 20 tools listed.
  name: Microsoft Dynamics 365 Sales MCP Server
  slug: microsoft-dynamics-365-sales-mcp-yml
modified: '2026-08-13'
name: Microsoft Dynamics 365 Sales
nav: Providers
network: true
overview: 'Microsoft Dynamics 365 Sales publishes 12 API contracts indexed on the [APIs.io](https://apis.io/) network, including Accounts API, $batch API, Contacts API, and 9 more. Tagged areas include CRM, Sales, Dynamics 365, Microsoft, and Dataverse.


  The Microsoft Dynamics 365 Sales catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Microsoft Dynamics 365 Sales'' developer surface includes authentication, documentation, pricing, signup flow, engineering blog, API reference, getting-started guide, and 50 more developer resources.'
plans:
- name: Microsoft Dynamics 365 Sales Plans Pricing
  plan_count: 5
  slug: microsoft-dynamics-365-sales-plans-pricing
- name: Microsoft Dynamics 365 Sales Price Estimates
  plan_count: 0
  slug: microsoft-dynamics-365-sales-price-estimates
random_paper: 3
rate_limits:
- limit_count: 4
  name: Microsoft Dynamics 365 Sales Rate Limits
  slug: microsoft-dynamics-365-sales-rate-limits
rules:
- authorship: generated
  effective_rule_count: 102
  extends:
  - spectral:oas
  name: Microsoft Dynamics 365 Sales API Rules
  rule_count: 61
  severity_counts:
    error: 57
    hint: 0
    info: 1
    warn: 3
  slug: microsoft-dynamics-365-sales-rules
scopes:
- name: Microsoft Dynamics 365 Sales Scopes
  scope_count: 2
  slug: microsoft-dynamics-365-sales-scopes
  summary_line: 2 scopes · authorizationCode/clientCredentials
score:
  band: exemplar
  composite: 77.5
  coverage:
    artifact_dirs: 37
    catalog_earned: 86.8
    catalog_earned_first_party: 24.0
    catalog_gap: 28.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 3.5
  facets:
    access_clarity: 86.8
    contract_governance: 35.6
    contract_quality: 66.8
    developer_ergonomics: 80.4
    discoverability: 76.7
    operational_transparency: 89.5
  previous_composite: 74.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 45.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/microsoft-dynamics-365-sales/microsoft-dynamics-365-sales-2026-06-20T185455.png
security:
- kind: authentication
  name: Microsoft Dynamics 365 Sales Authentication
  slug: microsoft-dynamics-365-sales-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Microsoft Dynamics 365 Sales Domain Security
  slug: microsoft-dynamics-365-sales-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Microsoft Dynamics 365 Sales Vulnerability Disclosure
  slug: microsoft-dynamics-365-sales-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Microsoft Dynamics 365 Sales Trust Center
  slug: microsoft-dynamics-365-sales-trust-center
  summary_line: GDPR
skill_count: 4
skills:
- name: microsoft-dynamics-365-sales-bulk-sync
  slug: microsoft-dynamics-365-sales-bulk-sync
- name: microsoft-dynamics-365-sales-lead-to-opportunity
  slug: microsoft-dynamics-365-sales-lead-to-opportunity
- name: microsoft-dynamics-365-sales-mcp-sales-insights
  slug: microsoft-dynamics-365-sales-mcp-sales-insights
- name: microsoft-dynamics-365-sales-quote-to-invoice
  slug: microsoft-dynamics-365-sales-quote-to-invoice
slug: microsoft-dynamics-365-sales
tags:
- CRM
- Sales
- Dynamics 365
- Microsoft
- Dataverse
- OData
- Sales Automation
website: https://www.microsoft.com/en-us/dynamics-365/products/sales
---
