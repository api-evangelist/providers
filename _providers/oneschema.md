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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: verified
    openapi_examples: partial
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 62.6
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 91
  human_in_the_loop: 0
  name: Oneschema Agentic Access
  operation_count: 156
  slug: oneschema-agentic-access
  summary_line: 156 operations · 91 acting
api_count: 28
apis:
- description: Manage AWS Secrets Manager account connections
  name: Oneschema AWS Secrets Manager Accounts API
  slug: oneschema-aws-secrets-manager-accounts-api
- description: Manage secret references within AWS Secrets Manager accounts
  name: Oneschema AWS Secrets Manager Secrets API
  slug: oneschema-aws-secrets-manager-secrets-api
- description: Manage Azure Key Vault account connections
  name: Oneschema Azure Key Vault Accounts API
  slug: oneschema-azure-key-vault-accounts-api
- description: Manage secret references within Azure Key Vault accounts
  name: Oneschema Azure Key Vault Secrets API
  slug: oneschema-azure-key-vault-secrets-api
- description: Legacy Code Hook operations
  name: Oneschema Code Hooks (Legacy) API
  slug: oneschema-code-hooks-legacy-api
- description: Event webhook operations
  name: Oneschema Event Webhooks API
  slug: oneschema-event-webhooks-api
- description: FileFeed Folder operations
  name: Oneschema FileFeed Folders API
  slug: oneschema-filefeed-folders-api
- description: Saved column mappings for FileFeeds
  name: Oneschema FileFeed Mappings API
  slug: oneschema-filefeed-mappings-api
- description: FileFeeds operations
  name: Oneschema FileFeeds API
  slug: oneschema-filefeeds-api
- description: FileFeeds Embed Sessions operations
  name: Oneschema FileFeeds Embed Sessions API
  slug: oneschema-filefeeds-embed-sessions-api
- description: FileFeeds Imports operations
  name: Oneschema FileFeeds Imports API
  slug: oneschema-filefeeds-imports-api
- description: Headless Importer operations
  name: Oneschema Headless Importer API
  slug: oneschema-headless-importer-api
- description: Importer Embed Event operations
  name: Oneschema Importer Embed Events API
  slug: oneschema-importer-embed-events-api
- description: Importer Embed operations
  name: Oneschema Importer Embeds API
  slug: oneschema-importer-embeds-api
- description: Importer Webhook operations
  name: Oneschema Importer Webhooks API
  slug: oneschema-importer-webhooks-api
- description: Read-only MCP operations for API specs and product guides
  name: Oneschema MCP Server API
  slug: oneschema-mcp-server-api
- description: Manage immutable commit snapshots of a Multi FileFeed's transforms. Commits are created by sending a transforms payload. The endpoint atomically replaces the HEAD and creates an immutable snapshot. Im
  name: Oneschema Multi FileFeed Commits API
  slug: oneschema-multi-filefeed-commits-api
- description: Multi FileFeed Folder operations
  name: Oneschema Multi FileFeed Folders API
  slug: oneschema-multi-filefeed-folders-api
- description: 'Multi FileFeed Imports operations. NOTE: These endpoints are served under the `/v0/multi-file-feeds/` path prefix. The legacy `/v0/workflows/` prefix is still supported for backward compatibility but '
  name: Oneschema Multi FileFeed Imports API
  slug: oneschema-multi-filefeed-imports-api
- description: Manage the transforms (flowgraph nodes) of a Multi FileFeed. The HEAD is the mutable, editable version of the flowgraph. Commits are immutable snapshots of the HEAD at a point in time. Imports run aga
  name: Oneschema Multi FileFeed Transforms API
  slug: oneschema-multi-filefeed-transforms-api
- description: Multi FileFeed operations
  name: Oneschema Multi FileFeeds API
  slug: oneschema-multi-filefeeds-api
- description: S3 Accounts connected to OneSchema
  name: Oneschema S3 Accounts API
  slug: oneschema-s3-accounts-api
- description: SFTP Accounts
  name: Oneschema SFTP Accounts API
  slug: oneschema-sftp-accounts-api
- description: Sheets operations
  name: Oneschema Sheets API
  slug: oneschema-sheets-api
- description: Template Hooks operations
  name: Oneschema Template Hooks API
  slug: oneschema-template-hooks-api
- description: Template operations
  name: Oneschema Templates API
  slug: oneschema-templates-api
- description: Sheet operations within Workspaces
  name: Oneschema Workspace Sheets API
  slug: oneschema-workspace-sheets-api
- description: Workspace operations
  name: Oneschema Workspaces API
  slug: oneschema-workspaces-api
artifact_total: 92
asyncapis:
- description: ''
  name: Oneschema Webhooks
  slug: oneschema-webhooks
collections:
- collection_type: postman
  name: OneSchema AWS Secrets Manager AWS Secrets Manager Accounts API
  slug: postman-oneschema-aws-secrets-manager-accounts-api
- collection_type: postman
  name: OneSchema AWS Secrets Manager AWS Secrets Manager Accounts AWS Secrets Manager Secrets API
  slug: postman-oneschema-aws-secrets-manager-secrets-api
- collection_type: postman
  name: OneSchema AWS Secrets Manager AWS Secrets Manager Accounts Azure Key Vault Accounts API
  slug: postman-oneschema-azure-key-vault-accounts-api
- collection_type: postman
  name: OneSchema AWS Secrets Manager AWS Secrets Manager Accounts Azure Key Vault Secrets API
  slug: postman-oneschema-azure-key-vault-secrets-api
- collection_type: postman
  name: OneSchema AWS Secrets Manager AWS Secrets Manager Accounts Code Hooks (Legacy) API
  slug: postman-oneschema-code-hooks-legacy-api
- collection_type: postman
  name: OneSchema AWS Secrets Manager AWS Secrets Manager Accounts Event Webhooks API
  slug: postman-oneschema-event-webhooks-api
- collection_type: postman
  name: OneSchema AWS Secrets Manager AWS Secrets Manager Accounts FileFeed Folders API
  slug: postman-oneschema-filefeed-folders-api
- collection_type: postman
  name: OneSchema AWS Secrets Manager AWS Secrets Manager Accounts FileFeed Mappings API
  slug: postman-oneschema-filefeed-mappings-api
- collection_type: postman
  name: OneSchema AWS Secrets Manager AWS Secrets Manager Accounts FileFeeds API
  slug: postman-oneschema-filefeeds-api
- collection_type: postman
  name: OneSchema AWS Secrets Manager AWS Secrets Manager Accounts FileFeeds Embed Sessions API
  slug: postman-oneschema-filefeeds-embed-sessions-api
- collection_type: postman
  name: OneSchema AWS Secrets Manager AWS Secrets Manager Accounts FileFeeds Imports API
  slug: postman-oneschema-filefeeds-imports-api
- collection_type: postman
  name: OneSchema AWS Secrets Manager AWS Secrets Manager Accounts Headless Importer API
  slug: postman-oneschema-headless-importer-api
- collection_type: postman
  name: OneSchema AWS Secrets Manager AWS Secrets Manager Accounts Importer Embed Events API
  slug: postman-oneschema-importer-embed-events-api
- collection_type: postman
  name: OneSchema AWS Secrets Manager AWS Secrets Manager Accounts Importer Embeds API
  slug: postman-oneschema-importer-embeds-api
- collection_type: postman
  name: OneSchema AWS Secrets Manager AWS Secrets Manager Accounts Importer Webhooks API
  slug: postman-oneschema-importer-webhooks-api
- collection_type: postman
  name: OneSchema AWS Secrets Manager AWS Secrets Manager Accounts MCP Server API
  slug: postman-oneschema-mcp-server-api
- collection_type: postman
  name: OneSchema AWS Secrets Manager AWS Secrets Manager Accounts Multi FileFeed Commits API
  slug: postman-oneschema-multi-filefeed-commits-api
- collection_type: postman
  name: OneSchema AWS Secrets Manager AWS Secrets Manager Accounts Multi FileFeed Folders API
  slug: postman-oneschema-multi-filefeed-folders-api
- collection_type: postman
  name: OneSchema AWS Secrets Manager AWS Secrets Manager Accounts Multi FileFeed Imports API
  slug: postman-oneschema-multi-filefeed-imports-api
- collection_type: postman
  name: OneSchema AWS Secrets Manager AWS Secrets Manager Accounts Multi FileFeed Transforms API
  slug: postman-oneschema-multi-filefeed-transforms-api
- collection_type: postman
  name: OneSchema AWS Secrets Manager AWS Secrets Manager Accounts Multi FileFeeds API
  slug: postman-oneschema-multi-filefeeds-api
- collection_type: postman
  name: OneSchema AWS Secrets Manager AWS Secrets Manager Accounts S3 Accounts API
  slug: postman-oneschema-s3-accounts-api
- collection_type: postman
  name: OneSchema AWS Secrets Manager AWS Secrets Manager Accounts SFTP Accounts API
  slug: postman-oneschema-sftp-accounts-api
- collection_type: postman
  name: OneSchema AWS Secrets Manager AWS Secrets Manager Accounts Sheets API
  slug: postman-oneschema-sheets-api
- collection_type: postman
  name: OneSchema AWS Secrets Manager AWS Secrets Manager Accounts Template Hooks API
  slug: postman-oneschema-template-hooks-api
- collection_type: postman
  name: OneSchema AWS Secrets Manager AWS Secrets Manager Accounts Templates API
  slug: postman-oneschema-templates-api
- collection_type: postman
  name: OneSchema AWS Secrets Manager AWS Secrets Manager Accounts Workspace Sheets API
  slug: postman-oneschema-workspace-sheets-api
- collection_type: postman
  name: OneSchema AWS Secrets Manager AWS Secrets Manager Accounts Workspaces API
  slug: postman-oneschema-workspaces-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: OneSchema AWS Secrets Manager AWS Secrets Manager Accounts API
  slug: open-oneschema-aws-secrets-manager-accounts-api
- collection_type: open
  name: OneSchema AWS Secrets Manager AWS Secrets Manager Accounts AWS Secrets Manager Secrets API
  slug: open-oneschema-aws-secrets-manager-secrets-api
- collection_type: open
  name: OneSchema AWS Secrets Manager AWS Secrets Manager Accounts Azure Key Vault Accounts API
  slug: open-oneschema-azure-key-vault-accounts-api
- collection_type: open
  name: OneSchema AWS Secrets Manager AWS Secrets Manager Accounts Azure Key Vault Secrets API
  slug: open-oneschema-azure-key-vault-secrets-api
- collection_type: open
  name: OneSchema AWS Secrets Manager AWS Secrets Manager Accounts Code Hooks (Legacy) API
  slug: open-oneschema-code-hooks-legacy-api
- collection_type: open
  name: OneSchema AWS Secrets Manager AWS Secrets Manager Accounts Event Webhooks API
  slug: open-oneschema-event-webhooks-api
- collection_type: open
  name: OneSchema AWS Secrets Manager AWS Secrets Manager Accounts FileFeed Folders API
  slug: open-oneschema-filefeed-folders-api
- collection_type: open
  name: OneSchema AWS Secrets Manager AWS Secrets Manager Accounts FileFeed Mappings API
  slug: open-oneschema-filefeed-mappings-api
- collection_type: open
  name: OneSchema AWS Secrets Manager AWS Secrets Manager Accounts FileFeeds API
  slug: open-oneschema-filefeeds-api
- collection_type: open
  name: OneSchema AWS Secrets Manager AWS Secrets Manager Accounts FileFeeds Embed Sessions API
  slug: open-oneschema-filefeeds-embed-sessions-api
- collection_type: open
  name: OneSchema AWS Secrets Manager AWS Secrets Manager Accounts FileFeeds Imports API
  slug: open-oneschema-filefeeds-imports-api
- collection_type: open
  name: OneSchema AWS Secrets Manager AWS Secrets Manager Accounts Headless Importer API
  slug: open-oneschema-headless-importer-api
- collection_type: open
  name: OneSchema AWS Secrets Manager AWS Secrets Manager Accounts Importer Embed Events API
  slug: open-oneschema-importer-embed-events-api
- collection_type: open
  name: OneSchema AWS Secrets Manager AWS Secrets Manager Accounts Importer Embeds API
  slug: open-oneschema-importer-embeds-api
- collection_type: open
  name: OneSchema AWS Secrets Manager AWS Secrets Manager Accounts Importer Webhooks API
  slug: open-oneschema-importer-webhooks-api
- collection_type: open
  name: OneSchema AWS Secrets Manager AWS Secrets Manager Accounts MCP Server API
  slug: open-oneschema-mcp-server-api
- collection_type: open
  name: OneSchema AWS Secrets Manager AWS Secrets Manager Accounts Multi FileFeed Commits API
  slug: open-oneschema-multi-filefeed-commits-api
- collection_type: open
  name: OneSchema AWS Secrets Manager AWS Secrets Manager Accounts Multi FileFeed Folders API
  slug: open-oneschema-multi-filefeed-folders-api
- collection_type: open
  name: OneSchema AWS Secrets Manager AWS Secrets Manager Accounts Multi FileFeed Imports API
  slug: open-oneschema-multi-filefeed-imports-api
- collection_type: open
  name: OneSchema AWS Secrets Manager AWS Secrets Manager Accounts Multi FileFeed Transforms API
  slug: open-oneschema-multi-filefeed-transforms-api
- collection_type: open
  name: OneSchema AWS Secrets Manager AWS Secrets Manager Accounts Multi FileFeeds API
  slug: open-oneschema-multi-filefeeds-api
- collection_type: open
  name: OneSchema AWS Secrets Manager AWS Secrets Manager Accounts S3 Accounts API
  slug: open-oneschema-s3-accounts-api
- collection_type: open
  name: OneSchema AWS Secrets Manager AWS Secrets Manager Accounts SFTP Accounts API
  slug: open-oneschema-sftp-accounts-api
- collection_type: open
  name: OneSchema AWS Secrets Manager AWS Secrets Manager Accounts Sheets API
  slug: open-oneschema-sheets-api
- collection_type: open
  name: OneSchema AWS Secrets Manager AWS Secrets Manager Accounts Template Hooks API
  slug: open-oneschema-template-hooks-api
- collection_type: open
  name: OneSchema AWS Secrets Manager AWS Secrets Manager Accounts Templates API
  slug: open-oneschema-templates-api
- collection_type: open
  name: OneSchema AWS Secrets Manager AWS Secrets Manager Accounts Workspace Sheets API
  slug: open-oneschema-workspace-sheets-api
- collection_type: open
  name: OneSchema AWS Secrets Manager AWS Secrets Manager Accounts Workspaces API
  slug: open-oneschema-workspaces-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/oneschema-aws-secrets-manager-overlay.yaml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/oneschema/overview
- group: auth
  title: ''
  type: DomainSecurity
  url: security/oneschema-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/oneschema-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/oneschema-authentication.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.oneschema.co/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.oneschema.co/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.oneschema.co/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.oneschema.co/docs/getting-started
- group: company
  title: ''
  type: Blog
  url: https://www.oneschema.co/blog
- group: operate
  title: ''
  type: Support
  url: mailto:support@oneschema.co
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/oneschema
- group: commercial
  title: ''
  type: Pricing
  url: https://www.oneschema.co/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.oneschema.co/signup
- group: start
  title: ''
  type: Login
  url: https://app.oneschema.co/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.oneschema.co/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.oneschema.co/privacy-notice
- group: build
  title: ''
  type: Packages
  url: packages/oneschema-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/oneschema-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/oneschema-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/oneschema-security.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/oneschema-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/oneschema-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/oneschema-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.oneschema.co/security
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/oneschema-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/oneschema-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.oneschema.co
- group: design
  title: ''
  type: Conventions
  url: conventions/oneschema-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/oneschema-changelog.yml
- group: design
  title: ''
  type: Components
  url: components/oneschema-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/oneschema-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/oneschema-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/oneschema-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/oneschema-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.oneschema.co/security
- group: auth
  title: ''
  type: TrustCenter
  url: security/oneschema-trust-center.yml
created: '2026-07-17'
description: OneSchema is an embeddable data onboarding and file-import platform for developers. Its core Importer embeds a guided CSV and spreadsheet upload experience — file upload, header detection, AI-assisted column mapping, and row-level validation against reusable Templates — directly inside a customer-facing product, so end users import clean, schema-compliant data in minutes. Beyond the embedded Importer, OneSchema offers Multi FileFeeds for automating recurring, transformation-heavy file ingestion pipelines (SFTP, S3, Google Drive/Sheets, Salesforce, SQL sources; AI file and PDF transforms; validation and delivery), a REST API at api.oneschema.co for headless importer sessions, templates, sheets, webhooks and connections, first-party JavaScript/React/Angular/Vue SDKs, and a hosted MCP server for AI coding assistants.
image: https://cdn.prod.website-files.com/62902d243ad8aef519be0d3e/62902d243ad8ae4014be0e97_oneschema-256.png
layout: provider
mcp_servers:
- description: ''
  name: oneschema-mcp.yml
  slug: oneschema-mcpyml
modified: '2026-07-20'
name: Oneschema
nav: Providers
network: true
overview: 'Oneschema publishes 28 APIs on the [APIs.io](https://apis.io/) network, including AWS Secrets Manager Accounts API, AWS Secrets Manager Secrets API, Azure Key Vault Accounts API, and 25 more. Tagged areas include Company, Data Onboarding, CSV Import, Data Validation, and File Processing.


  The Oneschema catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Oneschema''s developer surface includes authentication, documentation, API reference, getting-started guide, engineering blog, support, pricing, and 31 more developer resources.'
random_paper: 2
score:
  band: strong
  composite: 63.0
  delta: -0.9
  facets:
    access_clarity: 53.9
    commercial_clarity: 53.9
    contract_governance: 30.3
    contract_quality: 72.1
    developer_ergonomics: 78.0
    discoverability: 81.5
    governance: 30.3
    operational_transparency: 52.6
  previous_composite: 63.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 28
    mcp: first-party
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/oneschema/refs/heads/main/screenshots/oneschema-2026-08-07T190340.png
security:
- kind: authentication
  name: Oneschema Authentication
  slug: oneschema-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Oneschema Domain Security
  slug: oneschema-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Oneschema Vulnerability Disclosure
  slug: oneschema-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Oneschema Trust Center
  slug: oneschema-trust-center
  summary_line: SOC 2 Type II, SOC 3, HIPAA, GDPR, CCPA
slug: oneschema
tags:
- Company
- Data Onboarding
- CSV Import
- Data Validation
- File Processing
- ETL
- Data Integration
- Embeddable UI
- Spreadsheets
- Developer Tools
- AI Data Transformation
website: https://docs.oneschema.co/
---
