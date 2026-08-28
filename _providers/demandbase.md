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
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 55.4
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 24
  human_in_the_loop: 0
  name: Demandbase Agentic Access
  operation_count: 54
  slug: demandbase-agentic-access
  summary_line: 54 operations · 24 acting
api_count: 10
apis:
- description: 'Company and contact intelligence: search and fetch companies and contacts, company news, logos, installed technologies and corporate hierarchy; synchronous and bulk matching; asynchronous bulk data re'
  name: Demandbase B2B API
  slug: demandbase-b2b-api
- description: Asynchronous export of Demandbase platform data — Account, Opportunity, Person, Activity, Campaign, Creative, Account List and Person List entities — to CSV or JSON behind a signed download URL. Field
  name: Demandbase Data Export API
  slug: demandbase-data-export-api
- description: Asynchronous import of customer data and intent activity into the Demandbase platform. Create an import job, submit a data file of up to 5 GB, poll the job, and manage custom activity types and CSV re
  name: Demandbase Data Import API
  slug: demandbase-data-import-api
- description: 'Beta. Company-level intent signals and research activity: query by company IDs, keyword set IDs or keywords over a date range, filtered by intent strength or number of people researching, with cursor-'
  name: Demandbase Intent API
  slug: demandbase-intent-api
- description: 'User administration for a Demandbase tenant: create, update, retrieve, list and delete users, with filters for departments, views, permission sets and workspaces. 5 operations.'
  name: Demandbase Admin API
  slug: demandbase-admin-api
- description: 'Credit usage reporting: returns a summary of credit consumption and entitlements for a given API category, the only runtime signal a consumer has for remaining quota. 1 operation.'
  name: Demandbase Usage API
  slug: demandbase-usage-api
- description: Manage custom data sources and their per-object field mappings so third-party systems can feed the Demandbase platform. 7 operations.
  name: Demandbase Custom Sources API
  slug: demandbase-custom-sources-api
- description: 'Token exchange for every other Demandbase API: POST an API Key Set client ID and client secret with grantType client_credentials and receive a bearer access token valid for 8 hours. 1 operation.'
  name: Demandbase Auth API
  slug: demandbase-auth-api
- description: Hosted remote Model Context Protocol server exposing Demandbase account, person, intent, buying-group, account-brief, global company/contact and reference capabilities to AI assistants. OAuth 2.1 auth
  name: Demandbase MCP Server
  slug: demandbase-mcp-server
- description: 'Real-time visitor identification: resolves a visitor IP address to a Demandbase company ID, firmographics and corporate hierarchy for web personalization, forms enrichment and analytics integrations. '
  name: Demandbase IP-API v3
  slug: demandbase-ip-api-v3
artifact_total: 28
asyncapis:
- description: ''
  name: Demandbase Webhooks
  slug: demandbase-webhooks
collections:
- collection_type: open
  name: Admin API
  slug: open-demandbase-admin
- collection_type: open
  name: Demandbase Auth API
  slug: open-demandbase-auth
- collection_type: open
  name: B2B API
  slug: open-demandbase-b2b
- collection_type: open
  name: Custom Sources API
  slug: open-demandbase-custom-sources
- collection_type: open
  name: Data Export API
  slug: open-demandbase-data-export
- collection_type: open
  name: Data Import API
  slug: open-demandbase-data-import
- collection_type: open
  name: Intent API
  slug: open-demandbase-intent
- collection_type: open
  name: Usage API
  slug: open-demandbase-usage
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/demandbase-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/demandbase-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/demandbase-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/demandbase-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/demandbase
- group: operate
  title: ''
  type: StatusPage
  url: https://status.demandbase.com/
- group: operate
  title: ''
  type: Support
  url: https://support.demandbase.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.demandbase.com/privacy-policy/
- group: company
  title: ''
  type: Blog
  url: https://www.demandbase.com/blog/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/demandbase/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/Demandbase
- group: start
  title: ''
  type: Portal
  url: https://developer.demandbase.com
- group: other
  title: ''
  type: KnowledgeBase
  url: https://kb.demandbase.com/hc/en-us
- group: company
  title: ''
  type: Partners
  url: https://partners.demandbase.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.demandbase.com/terms-of-use/
- group: start
  title: ''
  type: Signup
  url: https://www.demandbase.com/products/data/api-integration/api-trial/
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/demandbase-vocabulary.yml
- group: build
  title: ''
  type: Packages
  url: packages/demandbase-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/demandbase-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/demandbase-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/demandbase-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/demandbase-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/demandbase-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/demandbase-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.demandbase.com/
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/demandbase-error-codes.yml
- group: design
  title: ''
  type: ErrorCodes
  url: errors/demandbase-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/demandbase-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://developer.demandbase.com/docs/migrating-from-legacy-tokens-to-api-keysets
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/demandbase-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/demandbase-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/demandbase-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/demandbase-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/demandbase-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/demandbase-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/demandbase-plans-pricing.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/demandbase-finops.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.demandbase.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.demandbase.com/docs/welcome
- group: docs
  title: ''
  type: APIReference
  url: https://developer.demandbase.com/reference/generate_access_token
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.demandbase.com/docs/api-getting-started
- group: commercial
  title: ''
  type: Pricing
  url: https://www.demandbase.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://www.demandbase.com/products/data/api-integration/api-trial/
- group: start
  title: ''
  type: Login
  url: https://web.demandbase.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.demandbase.com/hc/en-us
- group: build
  title: ''
  type: SDK
  url: https://pypi.org/project/demandbase-sdk/
- group: operate
  title: ''
  type: Contact
  url: https://www.demandbase.com/company/contact-us/
created: '2024-01-20'
description: Demandbase is a B2B go-to-market platform that unifies account intelligence, intent data, advertising, orchestration, personalization and sales intelligence into a single pipeline engine. Its developer surface is eight OpenAPI-documented REST APIs on uapi.demandbase.com — B2B company/contact intelligence, Data Export, Data Import, Admin, Intent (beta), Usage, Custom Sources and Auth — plus a hosted, OAuth-protected Model Context Protocol server that exposes account, person, intent, buying-group and account-brief capabilities to AI assistants, an official Python SDK, and a change-subscription webhook surface.
finops:
- name: Demandbase Finops
  service_category: B2B Marketing / Sales Intelligence
  slug: demandbase-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/demandbase.png
layout: provider
mcp_servers:
- description: ''
  name: Demandbase MCP Server
  slug: demandbase-mcp-server
modified: '2026-08-13'
name: Demandbase
nav: Providers
network: true
overview: 'Demandbase publishes 8 APIs on the [APIs.io](https://apis.io/) network, including B2B API, Data Export API, Data Import API, and 5 more. Tagged areas include Account Based Marketing, Advertising, AI Agents, B2B Marketing, and Company Data.


  The Demandbase catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Demandbase''s developer surface includes authentication, support, engineering blog, developer portal, signup flow, changelog, documentation, and 41 more developer resources.'
plans:
- name: Demandbase Plans Pricing
  plan_count: 0
  slug: demandbase-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 15
  name: Demandbase Rate Limits
  slug: demandbase-rate-limits
scopes:
- name: Demandbase Scopes
  scope_count: 4
  slug: demandbase-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: strong
  composite: 63.2
  delta: -0.1
  facets:
    access_clarity: 68.4
    commercial_clarity: 68.4
    contract_governance: 34.1
    contract_quality: 64.2
    developer_ergonomics: 55.4
    discoverability: 92.6
    governance: 34.1
    operational_transparency: 69.7
  previous_composite: 63.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 87.5
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: first-party
    skills: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/demandbase/refs/heads/main/screenshots/demandbase-2026-06-20T175908.png
security:
- kind: authentication
  name: Demandbase Authentication
  slug: demandbase-authentication
  summary_line: http/oauth2 · 1 scheme
- kind: domain-security
  name: Demandbase Domain Security
  slug: demandbase-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Demandbase Trust Center
  slug: demandbase-trust-center
  summary_line: SOC 2, ISO 27001
slug: demandbase
tags:
- Account Based Marketing
- Advertising
- AI Agents
- B2B Marketing
- Company Data
- Contact Data
- Data Enrichment
- Intent Data
- MCP
- Personalization
- Sales Intelligence
- Technographics
website: https://developer.demandbase.com
---
