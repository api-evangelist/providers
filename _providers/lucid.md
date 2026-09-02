---
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
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 48.3
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 126
  human_in_the_loop: 1
  name: Lucid Agentic Access
  operation_count: 220
  slug: lucid-agentic-access
  summary_line: 220 operations · 126 acting · 1 human-in-the-loop
api_count: 4
apis:
- description: 'Lucid''s remote Model Context Protocol server. Connects AI clients (ChatGPT, Claude, Microsoft Copilot, Cursor) to Lucid documents so they can be searched, retrieved, edited, summarized and created in '
  name: Lucid MCP Server
  slug: lucid-mcp-server
- description: Retrieve information about the authenticated Lucid account.
  name: Lucid Accounts API
  slug: lucid-accounts-api
- description: Retrieve audit log events that record user and admin activity across the Lucid account.
  name: Lucid Audit Logs API
  slug: lucid-audit-logs-api
- description: Manage cloud infrastructure credentials, data sources, and architecture diagrams for AWS, Azure, and Google Cloud.
  name: Lucid Cloud API
  slug: lucid-cloud-api
- description: Create, retrieve, update, and delete collections within a data source. A collection is a named group of data items that share a common schema (similar to a database table).
  name: Lucid Collection API
  slug: lucid-collection-api
- description: Read and update metadata properties on a collection, such as display name and configuration.
  name: Lucid Collection Properties API
  slug: lucid-collection-properties-api
- description: The CreateDiagram API from Lucid — 1 operation(s) for creatediagram.
  name: Lucid Create Diagram API
  slug: lucid-creatediagram-api
- description: Create, retrieve, update, and delete individual data items within a collection. A data item is a single record conforming to the collection's schema.
  name: Lucid Data Item API
  slug: lucid-data-item-api
- description: Create, retrieve, update, and delete data sets. A data set is a top-level container that groups related data sources and their collections.
  name: Lucid Data Set API
  slug: lucid-data-set-api
- description: Manage access grants on data sets to control which users or applications can read or write data.
  name: Lucid Data Set Grant API
  slug: lucid-data-set-grant-api
- description: Read and update metadata properties on a data set, such as display name and configuration.
  name: Lucid Data Set Properties API
  slug: lucid-data-set-properties-api
- description: Create, retrieve, update, and delete data sources within a data set. A data source represents an external system whose data is synced into Lucid.
  name: Lucid Data Source API
  slug: lucid-data-source-api
- description: Create, import, copy, retrieve, update, search, export, and trash documents across the Lucid Suite, and access their contents.
  name: Lucid Document Access API
  slug: lucid-document-access-api
- description: Retrieve comment threads on a document, list comments within a thread, and post new comments to an existing thread.
  name: Lucid Document Comments API
  slug: lucid-document-comments-api
- description: Generate session tokens and render the embedded viewer iframe used to display Lucid documents in external applications.
  name: Lucid Document Embedding API
  slug: lucid-document-embedding-api
- description: Generate tokens and render an embedded document picker that lets users select Lucid documents from within your application.
  name: Lucid Document Picker API
  slug: lucid-document-picker-api
- description: Manage user and team collaborator access on individual documents, including granting, updating, and revoking collaboration roles.
  name: Lucid Documents Collaboration API
  slug: lucid-documents-collaboration-api
- description: Create, retrieve, update, and delete share links for documents to control external access.
  name: Lucid Documents Sharing API
  slug: lucid-documents-sharing-api
- description: Create, retrieve, delete, and change the version of embed instances on a document.
  name: Lucid Embedding Utils API
  slug: lucid-embedding-utils-api
- description: Create, retrieve, update, search, trash, and restore folders. Includes listing folder contents and root folder navigation.
  name: Lucid Folders API
  slug: lucid-folders-api
- description: Manage user, group, and team collaborator access on folders, including granting, updating, and revoking collaboration roles.
  name: Lucid Folders Collaboration API
  slug: lucid-folders-collaboration-api
- description: Create, retrieve, update, and delete share links for folders to control external access.
  name: Lucid Folders Sharing API
  slug: lucid-folders-sharing-api
- description: Endpoints that deal with org groups or teams (dependent on which bearer token is used).
  name: Lucid Groups API
  slug: lucid-groups-api
- description: Create and manage legal holds on a Lucid account. Legal holds prevent documents from being permanently deleted for users placed on hold.
  name: Lucid Legal Holds API
  slug: lucid-legal-holds-api
- description: View and manage product licenses assigned to users within a subscription.
  name: Lucid Licenses API
  slug: lucid-licenses-api
- description: Create, refresh, introspect, and revoke OAuth 2.0 access tokens used to authenticate API requests on behalf of a user.
  name: Lucid OAuth 2.0 Tokens API
  slug: lucid-oauth-2-0-tokens-api
- description: Retrieve current rate limit thresholds and quotas for the authenticated user.
  name: Lucid Rate Limits API
  slug: lucid-rate-limits-api
- description: Create and manage shared document repositories. Control repository membership by adding and removing users and groups.
  name: Lucid Repositories API
  slug: lucid-repositories-api
- description: Define and retrieve the schema for a collection, specifying the fields, types, and constraints for its data items.
  name: Lucid Schema API
  slug: lucid-schema-api
- description: Endpoints that deal with lucid resource schemas.
  name: Lucid Schemas API
  slug: lucid-schemas-api
- description: Retrieve the SCIM service provider configuration, describing supported operations, authentication schemes, and bulk/filter capabilities.
  name: Lucid Service Provider Config API
  slug: lucid-service-provider-config-api
- description: The Sharing API from Lucid — 1 operation(s) for sharing.
  name: Lucid Sharing API
  slug: lucid-sharing-api
- description: List and retrieve product subscriptions on the account.
  name: Lucid Subscriptions API
  slug: lucid-subscriptions-api
- description: Create, retrieve, update, archive, and restore teams. Manage team membership by adding and removing users.
  name: Lucid Teams API
  slug: lucid-teams-api
- description: Transfer ownership of a user's documents, folders, custom shape libraries, and Lucidscale objects to another user within the same account.
  name: Lucid Transfer Content API
  slug: lucid-transfer-content-api
- description: Retrieve metadata for Lucid document links to power rich previews, and serve direct iframe embeds for Lucid documents in external applications.
  name: Lucid Unfurling API
  slug: lucid-unfurling-api
- description: Retrieve, create, and search for users within the authenticated account. Includes user profile access.
  name: Lucid Users API
  slug: lucid-users-api
artifact_total: 48
collections:
- collection_type: open
  name: Lucid Data API
  slug: open-lucid-data-api
- collection_type: open
  name: Lucid REST API
  slug: open-lucid-rest-api
- collection_type: open
  name: Lucid SCIM API
  slug: open-lucid-scim-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/lucid-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/lucid-rest-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/lucid-data-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/lucid-scim-api-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/lucid-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/lucid-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lucid-domain-security.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/lucid-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/lucid-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://lucid.co/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.lucid.co/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.lucid.co/docs/welcome
- group: docs
  title: ''
  type: APIReference
  url: https://developer.lucid.co/reference/api
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.lucid.co/docs/welcome
- group: operate
  title: ''
  type: Support
  url: https://community.lucid.co/lucid-for-developers-6
- group: company
  title: ''
  type: Blog
  url: https://lucid.co/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/lucidsoftware
- group: commercial
  title: ''
  type: Pricing
  url: https://lucid.app/pricing/lucidchart
- group: start
  title: ''
  type: SignUp
  url: https://lucid.app/users/login?activate=lucidchart
- group: commercial
  title: ''
  type: TermsOfService
  url: https://lucid.co/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://lucid.co/privacy
- group: auth
  title: ''
  type: Compliance
  url: https://lucid.co/security
- group: auth
  title: ''
  type: Security
  url: https://lucid.co/security
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/lucid-vulnerability-disclosure.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.lucid.co/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/lucid-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/lucid-changelog.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/lucid-well-known.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/lucid-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/lucid-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/lucid-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/lucid-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/lucid-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/lucid-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/lucid-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/lucid-cli.yml
- group: design
  title: ''
  type: Components
  url: components/lucid-components.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/lucid-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/lucid-mcp.yml
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/lucid_stock/
created: '2026-08-01'
description: 'Lucid Software Inc. is the visual collaboration company behind the Lucid Suite — Lucidchart (intelligent diagramming), Lucidspark (virtual whiteboarding) and Lucidscale (cloud visualization) — plus the Lucid Cloud, Process and Enterprise Shield accelerators and airfocus. The Lucid Developer Platform at developer.lucid.co publishes three OpenAPI-described surfaces: the Lucid REST API on api.lucid.co for documents, folders, sharing, embeds, comments, teams, repositories, legal holds, licenses and audit logs; the Lucid Data API on data.lucid.app for the structured data sets, collections, schemas and data items that back data-linked diagrams; and a SCIM 2.0 API on users.lucid.app for enterprise user and group provisioning. Lucid also ships an in-editor Extension API (lucid-extension-sdk plus the lucid-package CLI), an Embed SDK, and an OAuth-gated remote MCP server at mcp.lucid.app that lets AI clients search, read, edit and create Lucid documents. Lucid is privately held and trades
  on secondary markets.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lucidchart.png
layout: provider
mcp_servers:
- description: ''
  name: Lucid MCP Server
  slug: lucid-mcp-server
modified: '2026-08-01'
name: Lucid
nav: Providers
network: true
overview: 'Lucid publishes 36 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Audit Logs API, Cloud API, and 33 more. Tagged areas include Visual Collaboration, Diagramming, Whiteboarding, Productivity, and Software-as-a-Service.


  Lucid''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 34 more developer resources.'
random_paper: 4
rate_limits:
- limit_count: 5
  name: Lucid Rate Limits
  slug: lucid-rate-limits
scopes:
- name: Lucid Scopes
  scope_count: 143
  slug: lucid-scopes
  summary_line: 143 scopes · authorizationCode
score:
  band: strong
  composite: 61.3
  coverage:
    artifact_dirs: 24
    catalog_gap: 63.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 4.5
    contract_quality: 63.9
    developer_ergonomics: 73.2
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 76.3
  previous_composite: 61.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 94.4
      total: 36
    mcp: first-party
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lucid/refs/heads/main/screenshots/lucid-2026-08-07T171817.png
security:
- kind: authentication
  name: Lucid Authentication
  slug: lucid-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Lucid Domain Security
  slug: lucid-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Lucid Vulnerability Disclosure
  slug: lucid-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Lucid Trust Center
  slug: lucid-trust-center
  summary_line: SOC 2 Type II, ISO/IEC 27001:2022, ISO/IEC 27701, ISO/IEC 42001 (AI management systems), CSA STAR, PCI DSS, FedRAMP Moderate, TX-RAMP, IRAP (Australia), GDPR, CCPA
slug: lucid
tags:
- Visual Collaboration
- Diagramming
- Whiteboarding
- Productivity
- Software-as-a-Service
- Cloud Visualization
- SCIM
- Identity
- Data
- MCP
website: https://lucid.co/
---
