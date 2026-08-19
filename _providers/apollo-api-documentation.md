---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
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
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 48.8
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 54
  human_in_the_loop: 1
  name: Apollo Api Documentation Agentic Access
  operation_count: 80
  slug: apollo-api-documentation-agentic-access
  summary_line: 80 operations · 54 acting · 1 human-in-the-loop
api_count: 14
apis:
- description: Create, update, and search the companies your team tracks in Apollo. Harvested from the Apollo-published OpenAPI 3.1 specification — 8 operation(s).
  name: Apollo API Accounts
  slug: apollo-api-documentation-accounts-api
- description: Query saved analytics reports. Harvested from the Apollo-published OpenAPI 3.1 specification — 1 operation(s).
  name: Apollo API Analytics
  slug: apollo-api-documentation-analytics-api
- description: Log and update call records made inside or outside Apollo. Harvested from the Apollo-published OpenAPI 3.1 specification — 3 operation(s).
  name: Apollo API Calls
  slug: apollo-api-documentation-calls-api
- description: Create, update, and search the people your team saves in Apollo. Harvested from the Apollo-published OpenAPI 3.1 specification — 10 operation(s).
  name: Apollo API Contacts
  slug: apollo-api-documentation-contacts-api
- description: Search, export, and retrieve recorded conversations. Harvested from the Apollo-published OpenAPI 3.1 specification — 4 operation(s).
  name: Apollo API Conversations
  slug: apollo-api-documentation-conversations-api
- description: Create, update, and track deals in your pipeline. Harvested from the Apollo-published OpenAPI 3.1 specification — 5 operation(s).
  name: Apollo API Deals
  slug: apollo-api-documentation-deals-api
- description: The Emailer Messages surface of the Apollo API. Harvested from the Apollo-published OpenAPI 3.1 specification — 4 operation(s).
  name: Apollo API Emailer Messages
  slug: apollo-api-documentation-emailer-messages-api
- description: Enrich people and company records, individually or in bulk. Harvested from the Apollo-published OpenAPI 3.1 specification — 4 operation(s).
  name: Apollo API Enrichment
  slug: apollo-api-documentation-enrichment-api
- description: List, create, and update the fields and custom fields in your Apollo account. Harvested from the Apollo-published OpenAPI 3.1 specification — 4 operation(s).
  name: Apollo API Fields
  slug: apollo-api-documentation-fields-api
- description: Users, email accounts, lists, notes, usage stats, and webhook results. Harvested from the Apollo-published OpenAPI 3.1 specification — 12 operation(s).
  name: Apollo API Miscellaneous
  slug: apollo-api-documentation-miscellaneous-api
- description: Search Apollo's database of people, companies, news articles, and job postings. Harvested from the Apollo-published OpenAPI 3.1 specification — 6 operation(s).
  name: Apollo API Search
  slug: apollo-api-documentation-search-api
- description: Manage outreach sequences and the contacts enrolled in them. Harvested from the Apollo-published OpenAPI 3.1 specification — 12 operation(s).
  name: Apollo API Sequences
  slug: apollo-api-documentation-sequences-api
- description: Create and search tasks for your go-to-market workflows. Harvested from the Apollo-published OpenAPI 3.1 specification — 7 operation(s).
  name: Apollo API Tasks
  slug: apollo-api-documentation-tasks-api
- description: Apollo's hosted remote Model Context Protocol server. Streamable HTTP transport at https://mcp.apollo.io/mcp, OAuth 2.0 authorization with dynamic client registration, exposing Apollo search, enrichme
  name: Apollo MCP
  slug: apollo-api-documentation-mcp
artifact_total: 53
asyncapis:
- description: ''
  name: Apollo Api Documentation Webhooks
  slug: apollo-api-documentation-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Apollo API — Accounts
  slug: open-apollo-api-documentation-accounts-api
- collection_type: open
  name: Apollo API — Analytics
  slug: open-apollo-api-documentation-analytics-api
- collection_type: open
  name: Apollo API — Calls
  slug: open-apollo-api-documentation-calls-api
- collection_type: open
  name: Apollo API — Contacts
  slug: open-apollo-api-documentation-contacts-api
- collection_type: open
  name: Apollo API — Conversations
  slug: open-apollo-api-documentation-conversations-api
- collection_type: open
  name: Apollo API — Deals
  slug: open-apollo-api-documentation-deals-api
- collection_type: open
  name: Apollo API — Emailer Messages
  slug: open-apollo-api-documentation-emailer-messages-api
- collection_type: open
  name: Apollo API — Enrichment
  slug: open-apollo-api-documentation-enrichment-api
- collection_type: open
  name: Apollo API — Fields
  slug: open-apollo-api-documentation-fields-api
- collection_type: open
  name: Apollo API — Miscellaneous
  slug: open-apollo-api-documentation-miscellaneous-api
- collection_type: open
  name: Apollo API — Search
  slug: open-apollo-api-documentation-search-api
- collection_type: open
  name: Apollo API — Sequences
  slug: open-apollo-api-documentation-sequences-api
- collection_type: open
  name: Apollo API — Tasks
  slug: open-apollo-api-documentation-tasks-api
- collection_type: open
  name: Apollo.io API
  slug: open-apollo-api-documentation
common:
- group: auth
  title: ''
  type: Authentication
  url: authentication/apollo-api-documentation-authentication.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/apollo-api-documentation-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/apollo-api-documentation-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apollo-api-documentation-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://www.apollo.io/magazine
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apolloio
- group: docs
  title: ''
  type: Documentation
  url: https://docs.apollo.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.apollo.io/docs/build-with-apollo
- group: docs
  title: ''
  type: APIReference
  url: https://docs.apollo.io/reference/apollo-api
- group: auth
  title: ''
  type: Authentication
  url: https://docs.apollo.io/reference/authentication
- group: operate
  title: ''
  type: RateLimits
  url: https://docs.apollo.io/reference/rate-limits
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.apollo.io/llms.txt
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/apollo-api-documentation-apollo-rest-api-openapi.json
- group: build
  title: ''
  type: Packages
  url: packages/apollo-api-documentation-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/apollo-api-documentation-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/apollo-api-documentation-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/apollo-api-documentation-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/apollo-api-documentation-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/apollo-api-documentation-enrichment-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/apollo-api-documentation-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.apollo.io/
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/apollo-api-documentation-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/apollo-api-documentation-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.apollo.io
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/apollo-api-documentation-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/apollo-api-documentation-conventions.yml
- group: build
  title: ''
  type: CLI
  url: cli/apollo-api-documentation-cli.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/apollo-api-documentation-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/apollo-api-documentation-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/apollo-api-documentation-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/apollo-api-documentation-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/apollo-api-documentation-finops.yml
- group: build
  title: ''
  type: PostmanCollection
  url: collections/apollo-api-documentation.postman_collection.json
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.apollo.io/
- group: start
  title: ''
  type: Quickstart
  url: https://docs.apollo.io/docs/create-api-key
- group: operate
  title: ''
  type: Support
  url: https://www.apollo.io/contact
- group: operate
  title: ''
  type: FAQ
  url: https://docs.apollo.io/docs/developer-faqs
- group: learn
  title: ''
  type: Tutorials
  url: https://docs.apollo.io/docs/capabilities
- group: commercial
  title: ''
  type: Pricing
  url: https://www.apollo.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.apollo.io/sign-up
- group: start
  title: ''
  type: Login
  url: https://app.apollo.io/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.apollo.io/terms/api
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.apollo.io/privacy-policy
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.apollo.io/
created: '2025-07-10'
description: Apollo.io is a sales intelligence and engagement platform. Its REST API provides programmatic access to a database of over 240 million contacts and 30 million companies, covering people and organization enrichment (single and bulk), people/company/news search, and go-to-market workflow management across accounts, contacts, deals, sequences, emails, tasks, calls, conversations, lists and custom fields. Apollo users authenticate with an API key in the x-api-key header; partners building on behalf of mutual users authenticate with OAuth 2.0. Apollo publishes a complete OpenAPI 3.1 specification, a hosted remote MCP server at mcp.apollo.io, and a first-party CLI.
features:
- description: Enrich contact records with data from Apollo's 210M+ contact database.
  name: People Enrichment
- description: Enrich company records with data from Apollo's 35M+ company database.
  name: Organization Enrichment
- description: Search Apollo's contact database to find and identify sales prospects.
  name: People Search
- description: Search Apollo's company database for target accounts and job postings.
  name: Organization Search
- description: Manage accounts, contacts, deals, and sequences via the REST API.
  name: CRM Integration
- description: Partners use OAuth 2.0 to build integrations accessing Apollo data on behalf of customers.
  name: OAuth 2.0 Partner Integration
- description: Interactive API testing capability built directly into the documentation.
  name: Interactive Try It
- description: Query analytics reports for performance metrics via the API.
  name: Analytics Reporting
finops:
- name: Apollo Api Documentation Finops
  service_category: API
  slug: apollo-api-documentation-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apollo-api-documentation.png
integrations:
- description: Partner integration protocol for accessing Apollo data on behalf of customers.
  name: OAuth 2.0
- description: Direct API key access for customers building internal integrations.
  name: API Key Authentication
layout: provider
mcp_servers:
- description: ''
  name: apollo-api-documentation-mcp.yml
  slug: apollo-api-documentation-mcpyml
modified: '2026-08-14'
name: Apollo API Documentation
nav: Providers
network: true
overview: 'Apollo API Documentation publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Apollo API Accounts, Apollo API Analytics, Apollo API Calls, and 10 more. Tagged areas include API Documentation, Sales Intelligence, Data Enrichment, People Search, and Company Search.


  The Apollo API Documentation catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Apollo API Documentation''s developer surface includes authentication, engineering blog, documentation, getting-started guide, API reference, CLI, quickstart, and 38 more developer resources.'
plans:
- name: Apollo Api Documentation Plans Pricing
  plan_count: 4
  slug: apollo-api-documentation-plans-pricing
random_paper: 69
rate_limits:
- limit_count: 17
  name: Apollo Api Documentation Rate Limits
  slug: apollo-api-documentation-rate-limits
scopes:
- name: Apollo Api Documentation Scopes
  scope_count: 0
  slug: apollo-api-documentation-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 62.3
  delta: -2.7
  facets:
    access_clarity: 100.0
    commercial_clarity: 100.0
    contract_governance: 16.7
    contract_quality: 69.9
    developer_ergonomics: 45.8
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 42.1
  previous_composite: 65.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 25
    mcp: first-party
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apollo-api-documentation/refs/heads/main/screenshots/apollo-api-documentation-2026-06-20T172307.png
security:
- kind: authentication
  name: Apollo Api Documentation Authentication
  slug: apollo-api-documentation-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Apollo Api Documentation Domain Security
  slug: apollo-api-documentation-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Apollo Api Documentation Trust Center
  slug: apollo-api-documentation-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: apollo-api-documentation
tags:
- API Documentation
- Sales Intelligence
- Data Enrichment
- People Search
- Company Search
- Sales Engagement
- CRM
- MCP
- Agents
- Go-To-Market
use_cases:
- description: Access Apollo's contact and company database for prospecting and outreach.
  name: Sales Intelligence
- description: Enrich CRM records with contact and organization data at scale.
  name: Data Enrichment Pipelines
- description: Build third-party integrations using OAuth 2.0 to access Apollo data for mutual customers.
  name: Partner Integrations
- description: Automate sales workflows including sequences, tasks, and deal management.
  name: Workflow Automation
website: https://docs.apollo.io/
---
