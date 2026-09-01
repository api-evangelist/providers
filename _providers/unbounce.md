---
access_model:
  confidence: high
  label: Published pricing, API access on request
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://unbounce.com/pricing/
  - https://developer.unbounce.com/getting_started/
  - plans/unbounce-plans-pricing.yml
  trial: true
  try_now: true
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: na
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: true
    idempotency: na
    mcp_server: documented
    openapi_examples: documented
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 59.6
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Unbounce Agentic Access
  operation_count: 21
  slug: unbounce-agentic-access
  summary_line: 21 operations
api_count: 1
apis:
- description: REST API for Unbounce providing programmatic access to accounts, sub-accounts, domains, pages, page groups, and leads. Authentication uses OAuth 2.0 Authorization Code flow with Bearer access tokens a
  name: Unbounce REST API
  slug: rest-api
- description: Official hosted Model Context Protocol server for Unbounce. Exposes 37 tools that create, edit, publish, A/B-test and report on Unbounce landing pages and variants directly from an AI assistant. Autho
  name: Unbounce MCP Server
  slug: mcp-server
- description: Account and sub-account resources
  name: Unbounce Accounts API
  slug: unbounce-accounts-api
- description: Domains attached to sub-accounts
  name: Unbounce Domains API
  slug: unbounce-domains-api
- description: Lead submissions captured by pages
  name: Unbounce Leads API
  slug: unbounce-leads-api
- description: API meta-information
  name: Unbounce Meta API
  slug: unbounce-meta-api
- description: Logical page groupings
  name: Unbounce PageGroups API
  slug: unbounce-pagegroups-api
- description: Landing pages and form fields
  name: Unbounce Pages API
  slug: unbounce-pages-api
- description: Users in the account
  name: Unbounce Users API
  slug: unbounce-users-api
artifact_total: 64
asyncapis:
- description: ''
  name: Unbounce Webhooks
  slug: unbounce-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Unbounce REST Accounts API
  slug: open-unbounce-accounts-api
- collection_type: open
  name: Unbounce REST Accounts Domains API
  slug: open-unbounce-domains-api
- collection_type: open
  name: Unbounce REST Accounts Leads API
  slug: open-unbounce-leads-api
- collection_type: open
  name: Unbounce REST Accounts Meta API
  slug: open-unbounce-meta-api
- collection_type: open
  name: Unbounce REST Accounts PageGroups API
  slug: open-unbounce-pagegroups-api
- collection_type: open
  name: Unbounce REST Accounts Pages API
  slug: open-unbounce-pages-api
- collection_type: open
  name: Unbounce REST Accounts Users API
  slug: open-unbounce-users-api
- collection_type: open
  name: Unbounce REST API
  slug: open-unbounce
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/unbounce/agent-plugins/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/unbounce-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/unbounce-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/unbounce-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/unbounce-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/unbounce-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/unbounce-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/unbounce
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/unbounce
- group: company
  title: ''
  type: Website
  url: https://unbounce.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.unbounce.com/
- group: docs
  title: ''
  type: Documentation
  url: https://documentation.unbounce.com/
- group: docs
  title: ''
  type: API Documentation
  url: https://developer.unbounce.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://unbounce.com/pricing/
- group: start
  title: ''
  type: Signup
  url: https://unbounce.com/lp/free-trial/
- group: start
  title: ''
  type: Login
  url: https://app.unbounce.com/sign_in
- group: company
  title: ''
  type: Blog
  url: https://unbounce.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://documentation.unbounce.com/
- group: operate
  title: ''
  type: Community
  url: https://community.unbounce.com/
- group: other
  title: ''
  type: RAML
  url: raml/unbounce-api-v0.4.raml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/_index.yml
- group: build
  title: ''
  type: Examples
  url: examples/_index.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/unbounce-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/unbounce-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/unbounce-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/unbounce-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/unbounce-packages.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/unbounce-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/unbounce-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/unbounce-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://unbounce.com/security/
- group: auth
  title: ''
  type: Security
  url: https://unbounce.com/security/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/unbounce-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.unbounce.com
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/unbounce-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/unbounce-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/unbounce-webhooks.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/unbounce-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/unbounce-rate-limits.yml
- group: start
  title: ''
  type: Console
  url: https://developer.unbounce.com/console.html
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.unbounce.com/getting_started/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.unbounce.com/api_reference/
- group: start
  title: ''
  type: SignUp
  url: https://unbounce.com/lp/free-trial/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://unbounce.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://unbounce.com/privacy/
created: '2026-05-11'
description: Unbounce is a landing page, popup, and sticky bar builder with conversion rate optimization features including drag-and-drop design, A/B testing, AI copywriting (Smart Copy), and AI traffic routing (Smart Traffic) for marketers, agencies, SaaS, and ecommerce. The platform integrates with HubSpot, Salesforce, Google Analytics, and other marketing platforms to capture, qualify, and route leads. The Unbounce REST API provides programmatic access to pages, leads, sub-accounts, and domains using an API key over HTTP Basic or OAuth 2.0 Authorization Code, described by a published RAML 0.8 definition. Unbounce also operates an official hosted Model Context Protocol server at mcp.unbounce.com with 37 tools — the only public write surface for pages, variants, publishing and traffic — plus three Agent Skills shipped in its own agent-plugin marketplace.
examples:
- key_count: 6
  name: Unbounce Accounts Account_Get
  slug: unbounce-accounts-account_get
- key_count: 2
  name: Unbounce Accounts Accounts_Get
  slug: unbounce-accounts-accounts_get
- key_count: 2
  name: Unbounce Accounts Pages_Get
  slug: unbounce-accounts-pages_get
- key_count: 2
  name: Unbounce Accounts Sub_Accounts_Get
  slug: unbounce-accounts-sub_accounts_get
- key_count: 4
  name: Unbounce Domains Domain_Get
  slug: unbounce-domains-domain_get
- key_count: 2
  name: Unbounce Domains Pages_Get
  slug: unbounce-domains-pages_get
- key_count: 9
  name: Unbounce Lead_Deletion_Request Lead_Deletion_Request_Get
  slug: unbounce-lead_deletion_request-lead_deletion_request_get
- key_count: 8
  name: Unbounce Leads Lead_Get
  slug: unbounce-leads-lead_get
- key_count: 2
  name: Unbounce Page_Groups Pages_Get
  slug: unbounce-page_groups-pages_get
- key_count: 2
  name: Unbounce Pages Form_Fields_Get
  slug: unbounce-pages-form_fields_get
- key_count: 2
  name: Unbounce Pages Leads_Get
  slug: unbounce-pages-leads_get
- key_count: 14
  name: Unbounce Pages Page_Get
  slug: unbounce-pages-page_get
- key_count: 2
  name: Unbounce Pages Pages_Get
  slug: unbounce-pages-pages_get
- key_count: 2
  name: Unbounce Sub_Accounts Domains_Get
  slug: unbounce-sub_accounts-domains_get
- key_count: 2
  name: Unbounce Sub_Accounts Page_Groups_Get
  slug: unbounce-sub_accounts-page_groups_get
- key_count: 2
  name: Unbounce Sub_Accounts Pages_Get
  slug: unbounce-sub_accounts-pages_get
- key_count: 6
  name: Unbounce Sub_Accounts Sub_Account_Get
  slug: unbounce-sub_accounts-sub_account_get
- key_count: 5
  name: Unbounce Users Self_Get
  slug: unbounce-users-self_get
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/unbounce.png
json_schemas:
- name: Unbounce Account
  property_count: 5
  slug: unbounce-account
- name: Unbounce Accounts
  property_count: 2
  slug: unbounce-accounts
- name: Unbounce Api_Root
  property_count: 4
  slug: unbounce-api_root
- name: Unbounce Domain
  property_count: 3
  slug: unbounce-domain
- name: Unbounce Domains
  property_count: 2
  slug: unbounce-domains
- name: Unbounce Error_V3.1
  property_count: 0
  slug: unbounce-error_v3.1
- name: Unbounce Form_Fields
  property_count: 2
  slug: unbounce-form_fields
- name: Unbounce Lead
  property_count: 8
  slug: unbounce-lead
- name: Unbounce Lead_Deletion_Request
  property_count: 8
  slug: unbounce-lead_deletion_request
- name: Unbounce Lead_Deletion_Request_Query
  property_count: 4
  slug: unbounce-lead_deletion_request_query
- name: Unbounce Leads
  property_count: 2
  slug: unbounce-leads
- name: Unbounce New_Lead
  property_count: 3
  slug: unbounce-new_lead
- name: Unbounce Page
  property_count: 14
  slug: unbounce-page
- name: Unbounce Page_Groups
  property_count: 2
  slug: unbounce-page_groups
- name: Unbounce Pages
  property_count: 2
  slug: unbounce-pages
- name: Unbounce Sub_Account
  property_count: 7
  slug: unbounce-sub_account
- name: Unbounce Sub_Accounts
  property_count: 2
  slug: unbounce-sub_accounts
- name: Unbounce User
  property_count: 5
  slug: unbounce-user
layout: provider
mcp_servers:
- description: ''
  name: Unbounce MCP Server
  slug: unbounce-mcp-server
modified: '2026-08-13'
name: Unbounce
nav: Providers
network: true
overview: 'Unbounce publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Domains API, Leads API, and 4 more. Tagged areas include Landing Pages, Conversion Rate Optimization, Marketing, A/B Testing, and Lead Generation.


  The Unbounce catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Unbounce''s developer surface includes authentication, documentation, pricing, signup flow, engineering blog, support, code examples, and 39 more developer resources.'
plans:
- name: Unbounce Plans Pricing
  plan_count: 6
  slug: unbounce-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 1
  name: Unbounce Rate Limits
  slug: unbounce-rate-limits
scopes:
- name: Unbounce Scopes
  scope_count: 2
  slug: unbounce-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: strong
  composite: 65.6
  coverage:
    artifact_dirs: 27
    catalog_gap: 58.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 85.5
    commercial_clarity: 85.5
    contract_governance: 18.2
    contract_quality: 62.3
    developer_ergonomics: 71.4
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 73.7
  previous_composite: 65.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: first-party
    skills: first-party
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/unbounce/refs/heads/main/screenshots/unbounce-2026-06-20T200015.png
security:
- kind: authentication
  name: Unbounce Authentication
  slug: unbounce-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: Unbounce Domain Security
  slug: unbounce-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Unbounce Vulnerability Disclosure
  slug: unbounce-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Unbounce Trust Center
  slug: unbounce-trust-center
  summary_line: PCI DSS
slug: unbounce
tags:
- Landing Pages
- Conversion Rate Optimization
- Marketing
- A/B Testing
- Lead Generation
- Marketing Automation
website: https://unbounce.com
---
