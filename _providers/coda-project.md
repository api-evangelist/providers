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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 57.0
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 102
  human_in_the_loop: 4
  name: Coda Project Agentic Access
  operation_count: 212
  slug: coda-project-agentic-access
  summary_line: 212 operations · 102 acting · 4 human-in-the-loop
api_count: 32
apis:
- description: At this time, the API exposes some limited information about your account. However, `/whoami` is a good endpoint to hit to verify that you're hitting the API correctly and that your token is working a
  name: Coda Project Account API
  slug: coda-project-account-api
- description: This API offers analytics data for your docs and Packs over time.
  name: Coda Project Analytics API
  slug: coda-project-analytics-api
- description: View and revoke individual user API tokens within an organization.
  name: Coda Project API Tokens API
  slug: coda-project-api-tokens-api
- description: This API allows you to trigger automations.
  name: Coda Project Automations API
  slug: coda-project-automations-api
- description: 'While columns in Superhuman Docs have user-friendly names, they also have immutable IDs that are used when reading and writing rows. These endpoints let you query the columns in a table and get basic '
  name: Coda Project Columns API
  slug: coda-project-columns-api
- description: Controls provide a user-friendly way to input a value that can affect other parts of the doc. This API lets you list controls and get their current values.
  name: Coda Project Controls API
  slug: coda-project-controls-api
- description: The CustomDocDomains API from Coda Project — 3 operation(s) for customdocdomains.
  name: Coda Project CustomDocDomains API
  slug: coda-project-customdocdomains-api
- description: Export docs for backup or ingestion into a DLP or eDiscovery system.
  name: Coda Project Doc Export API
  slug: coda-project-doc-export-api
- description: This API lets you manage sharing and permissions for your docs.
  name: Coda Project Doc Permissions API
  slug: coda-project-doc-permissions-api
- description: Documents are foundational, top-level collaborative projects that contain pages. The API lets you list and search your documents.
  name: Coda Project Docs API
  slug: coda-project-docs-api
- description: Provides access to audit events within an organization.
  name: Coda Project Events API
  slug: coda-project-events-api
- description: This API lets you manage sharing and permissions for your folders.
  name: Coda Project Folder Permissions API
  slug: coda-project-folder-permissions-api
- description: Folders contain docs and enable folder members to access those docs.
  name: Coda Project Folders API
  slug: coda-project-folders-api
- description: Formulas can be great for performing one-off computations, or used with tables and other formulas to compute a single value. With this API, you can discover formulas in a doc and obtain computed resul
  name: Coda Project Formulas API
  slug: coda-project-formulas-api
- description: The Go Links API from Coda Project — 1 operation(s) for go links.
  name: Coda Project Go Links API
  slug: coda-project-go-links-api
- description: This API lets you enumerate groups and group membership.
  name: Coda Project Groups API
  slug: coda-project-groups-api
- description: Legal holds are used to ensure a given set of docs cannot be deleted and enables simplified export management of doc content.
  name: Coda Project LegalHolds API
  slug: coda-project-legalholds-api
- description: These endpoints wouldn't fit anywhere else, but you may find them useful when working with Superhuman Docs.
  name: Coda Project Miscellaneous API
  slug: coda-project-miscellaneous-api
- description: This API enables viewing and modifying user information at the Organization level.
  name: Coda Project Organization Users API
  slug: coda-project-organization-users-api
- description: Organizations are where Enterprise-level policy is set for users and workspaces.
  name: Coda Project Organizations API
  slug: coda-project-organizations-api
- description: Pack configurations control fine grained access, scopes, feature sets, shareability of docs with installed Packs, and more settings.
  name: Coda Project Pack Configurations API
  slug: coda-project-pack-configurations-api
- description: Pack controls govern access to Packs within an organization.
  name: Coda Project Pack Controls API
  slug: coda-project-pack-controls-api
- description: Packs are integrations connecting Superhuman Docs to external data sources.
  name: Coda Project Packs API
  slug: coda-project-packs-api
- description: Pages in Superhuman Docs offer canvases containing rich text, tables, controls, and other objects.
  name: Coda Project Pages API
  slug: coda-project-pages-api
- description: This API lets you manage sharing and permissions for your docs.
  name: Coda Project Permissions API
  slug: coda-project-permissions-api
- description: Import preferences control how external entities are imported (exempt, owner, location), scoped to an organization and importer.
  name: Coda Project Preferences API
  slug: coda-project-preferences-api
- description: Documents can be published publicly and associated with categories to help the world discover them. This API lets you manage the publishing settings of your docs.
  name: Coda Project Publishing API
  slug: coda-project-publishing-api
- description: You'll likely use this part of the API the most. These endpoints let you retrieve row data from tables in Superhuman Docs as well as create, upsert, update, and delete them. Most of these endpoints wo
  name: Coda Project Rows API
  slug: coda-project-rows-api
- description: The Tables API from Coda Project — 2 operation(s) for tables.
  name: Coda Project Tables API
  slug: coda-project-tables-api
- description: The Webhooks API from Coda Project — 3 operation(s) for webhooks.
  name: Coda Project Webhooks API
  slug: coda-project-webhooks-api
- description: This API enables viewing and modifying user membership within a workspace. It is accessible both to organization admins and workspace admins for the respective workspaces.
  name: Coda Project Workspace Users API
  slug: coda-project-workspace-users-api
- description: This API allows you to list and view your organization's workspaces.
  name: Coda Project Workspaces API
  slug: coda-project-workspaces-api
arazzos:
- description: ''
  name: _Index
  slug: _index
- description: Create a doc, add a page, then upsert rows and wait for the async mutation to complete.
  name: Create a Coda doc and populate a table
  slug: coda-project-create-doc-and-populate
- description: Validate the token, find a doc and table, and read its rows.
  name: List and read Coda doc rows
  slug: coda-project-list-and-read-rows
- description: Resolve key columns, upsert rows idempotently, await the mutation, and verify.
  name: Upsert and reconcile Coda table rows
  slug: coda-project-upsert-rows
artifact_total: 77
asyncapis:
- description: ''
  name: Coda Project Webhooks
  slug: coda-project-webhooks
collections:
- collection_type: postman
  name: Superhuman Docs Admin Account API
  slug: postman-coda-project-account-api
- collection_type: postman
  name: Superhuman Docs Admin Account Analytics API
  slug: postman-coda-project-analytics-api
- collection_type: postman
  name: Superhuman Docs Admin Account API Tokens API
  slug: postman-coda-project-api-tokens-api
- collection_type: postman
  name: Superhuman Docs Admin Account Automations API
  slug: postman-coda-project-automations-api
- collection_type: postman
  name: Superhuman Docs Admin Account Columns API
  slug: postman-coda-project-columns-api
- collection_type: postman
  name: Superhuman Docs Admin Account Controls API
  slug: postman-coda-project-controls-api
- collection_type: postman
  name: Superhuman Docs Admin Account CustomDocDomains API
  slug: postman-coda-project-customdocdomains-api
- collection_type: postman
  name: Superhuman Docs Admin Account Doc Export API
  slug: postman-coda-project-doc-export-api
- collection_type: postman
  name: Superhuman Docs Admin Account Doc Permissions API
  slug: postman-coda-project-doc-permissions-api
- collection_type: postman
  name: Superhuman Admin Account Docs API
  slug: postman-coda-project-docs-api
- collection_type: postman
  name: Superhuman Docs Admin Account Events API
  slug: postman-coda-project-events-api
- collection_type: postman
  name: Superhuman Docs Admin Account Folder Permissions API
  slug: postman-coda-project-folder-permissions-api
- collection_type: postman
  name: Superhuman Docs Admin Account Folders API
  slug: postman-coda-project-folders-api
- collection_type: postman
  name: Superhuman Docs Admin Account Formulas API
  slug: postman-coda-project-formulas-api
- collection_type: postman
  name: Superhuman Docs Admin Account Go Links API
  slug: postman-coda-project-go-links-api
- collection_type: postman
  name: Superhuman Docs Admin Account Groups API
  slug: postman-coda-project-groups-api
- collection_type: postman
  name: Superhuman Docs Admin Account LegalHolds API
  slug: postman-coda-project-legalholds-api
- collection_type: postman
  name: Superhuman Docs Admin Account Miscellaneous API
  slug: postman-coda-project-miscellaneous-api
- collection_type: postman
  name: Superhuman Docs Admin Account Organization Users API
  slug: postman-coda-project-organization-users-api
- collection_type: postman
  name: Superhuman Docs Admin Account Organizations API
  slug: postman-coda-project-organizations-api
- collection_type: postman
  name: Superhuman Docs Admin Account Pack Configurations API
  slug: postman-coda-project-pack-configurations-api
- collection_type: postman
  name: Superhuman Docs Admin Account Pack Controls API
  slug: postman-coda-project-pack-controls-api
- collection_type: postman
  name: Superhuman Docs Admin Account Packs API
  slug: postman-coda-project-packs-api
- collection_type: postman
  name: Superhuman Docs Admin Account Pages API
  slug: postman-coda-project-pages-api
- collection_type: postman
  name: Superhuman Docs Admin Account Permissions API
  slug: postman-coda-project-permissions-api
- collection_type: postman
  name: Superhuman Docs Admin Account Preferences API
  slug: postman-coda-project-preferences-api
- collection_type: postman
  name: Superhuman Docs Admin Account Publishing API
  slug: postman-coda-project-publishing-api
- collection_type: postman
  name: Superhuman Docs Admin Account Rows API
  slug: postman-coda-project-rows-api
- collection_type: postman
  name: Superhuman Docs Admin Account Tables API
  slug: postman-coda-project-tables-api
- collection_type: postman
  name: Superhuman Docs Admin Account Webhooks API
  slug: postman-coda-project-webhooks-api
- collection_type: postman
  name: Superhuman Docs Admin Account Workspace Users API
  slug: postman-coda-project-workspace-users-api
- collection_type: postman
  name: Superhuman Docs Admin Account Workspaces API
  slug: postman-coda-project-workspaces-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/coda-project/overview
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/coda-project-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/coda-project-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/coda-project-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/coda-project-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/coda-project-scopes.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/coda-project-trust-center.yml
- group: auth
  title: ''
  type: Security
  url: https://hackerone.com/coda_bbp
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/coda-project-rate-limits.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://coda.io/developers
- group: docs
  title: ''
  type: Documentation
  url: https://coda.io/developers/apis/v1
- group: docs
  title: ''
  type: APIReference
  url: https://coda.io/developers/apis/v1
- group: start
  title: ''
  type: GettingStarted
  url: https://coda.io/developers/apis/v1#section/Using-the-API
- group: operate
  title: ''
  type: Support
  url: https://help.coda.io/
- group: company
  title: ''
  type: Blog
  url: https://coda.io/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/coda
- group: commercial
  title: ''
  type: Pricing
  url: https://coda.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://coda.io/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://coda.io/trust/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://coda.io/trust/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.coda.io
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/codaio/coda-workspace
- group: build
  title: ''
  type: Packages
  url: packages/coda-project-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/coda-project-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/coda-project-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/coda-project-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/coda-project-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/coda-project-security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/coda-project-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/coda-project-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/coda-project-trust-center.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/coda-project-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/coda-project-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/coda-project-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/coda-project-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/coda-project-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/coda-project-list-and-read-rows.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/coda-project-create-doc-and-populate.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/coda-project-upsert-rows.yml
created: '2026-07-17'
description: Coda Project, Inc. is the maker of Coda (now branded Superhuman Docs), an all-in-one collaborative workspace that blends the flexibility of a document, the structure of a spreadsheet, the power of applications, and the intelligence of AI into a single canvas. Founded in 2014 by Shishir Mehrotra and Alex DeNeui and used by tens of thousands of teams, Coda exposes a RESTful Docs API that lets developers list and search docs, create and copy docs, discover pages, tables, formulas, and controls, and read, insert, upsert, update, and delete rows. A separate Admin API provides programmatic organization administration — workspaces, users, groups, legal holds, audit events, webhooks, and Pack governance. Coda also ships a first-party Packs SDK and CLI for extending the platform, an official remote MCP server for AI clients, OAuth 2.0 with dynamic client registration, and a public Postman workspace.
image: https://sanity-images.imgix.net/production/6b46953798756d87bc1ad579a32d2af427ba6d3d-1200x628.png
layout: provider
mcp_servers:
- description: ''
  name: coda-project-mcp.yml
  slug: coda-project-mcpyml
modified: '2026-07-18'
name: Coda Project
nav: Providers
network: true
overview: 'Coda Project publishes 32 APIs on the [APIs.io](https://apis.io/) network, including Account API, Analytics API, API Tokens API, and 29 more. Tagged areas include Company, Productivity, Documents, Spreadsheets, and Collaboration.


  The Coda Project catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Coda Project''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 33 more developer resources.'
random_paper: 71
rate_limits:
- limit_count: 3
  name: Coda Project Rate Limits
  slug: coda-project-rate-limits
scopes:
- name: Coda Project Scopes
  scope_count: 1
  slug: coda-project-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: exemplar
  composite: 66.2
  delta: 4.1
  facets:
    commercial_clarity: 60.5
    contract_quality: 72.9
    developer_ergonomics: 79.9
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 71.1
  previous_composite: 62.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 32
    mcp: first-party
    skills: derived
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/coda-project/refs/heads/main/screenshots/coda-project-2026-07-25T205859.png
security:
- kind: authentication
  name: Coda Project Authentication
  slug: coda-project-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Coda Project Domain Security
  slug: coda-project-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Coda Project Vulnerability Disclosure
  slug: coda-project-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Coda Project Trust Center
  slug: coda-project-trust-center
  summary_line: SOC 2 Type II, SOC 3, ISO 27001, ISO 27017, ISO 27018, HIPAA, GDPR, CCPA
slug: coda-project
tags:
- Company
- Productivity
- Documents
- Spreadsheets
- Collaboration
- No-Code
- Workspace
- AI
- Content Management
- SaaS
website: https://coda.io/developers
---
