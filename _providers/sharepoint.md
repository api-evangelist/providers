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
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 57.7
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Sharepoint Agentic Access
  operation_count: 15
  slug: sharepoint-agentic-access
  summary_line: 15 operations · 5 acting
api_count: 8
apis:
- description: Client-side object model for SharePoint that provides access to SharePoint objects through .NET managed or JavaScript libraries.
  name: SharePoint CSOM (Client-Side Object Model)
  slug: csom-client-side-object-model
- description: SharePoint webhooks provide a way to get notified about changes to SharePoint lists and document libraries.
  name: SharePoint Webhooks API
  slug: webhooks-api
- description: File upload, download, and management
  name: Microsoft SharePoint Files API
  slug: sharepoint-files-api
- description: List item operations
  name: Microsoft SharePoint Items API
  slug: sharepoint-items-api
- description: List and library operations
  name: Microsoft SharePoint Lists API
  slug: sharepoint-lists-api
- description: Search query operations
  name: Microsoft SharePoint Search API
  slug: sharepoint-search-api
- description: Site and web operations
  name: Microsoft SharePoint Sites API
  slug: sharepoint-sites-api
- description: User profile operations
  name: Microsoft SharePoint User Profiles API
  slug: sharepoint-user-profiles-api
arazzos:
- description: Find an item by title and create it only when missing, then read it back.
  name: SharePoint Ensure a List Item Exists
  slug: sharepoint-ensure-list-item-workflow
- description: Create, read, update, verify, and delete a list item as an end-to-end conformance run.
  name: SharePoint List Item Full Lifecycle
  slug: sharepoint-list-item-lifecycle-workflow
- description: Create a list only if it does not already exist, read it back, and seed an item.
  name: SharePoint Provision a List and Seed Its First Item
  slug: sharepoint-provision-list-workflow
- description: Run a search query, take the top hit's path, and fetch the document bytes.
  name: SharePoint Search for a Document and Download It
  slug: sharepoint-search-and-download-workflow
- description: Escalate from a cheap reachability probe to identity, site detail, and visible lists.
  name: SharePoint Verify Site Connection and Identity
  slug: sharepoint-site-connection-check-workflow
- description: Walk a site from its title down through lists, recent items, and library files.
  name: SharePoint Site Content Inventory
  slug: sharepoint-site-content-inventory-workflow
- description: Survey a library folder, upload a file with overwrite, then read the bytes back.
  name: SharePoint Upload a Document and Verify It
  slug: sharepoint-upload-document-workflow
artifact_total: 95
collections:
- collection_type: postman
  name: SharePoint REST Files API
  slug: postman-sharepoint-files-api
- collection_type: postman
  name: SharePoint REST Files Items API
  slug: postman-sharepoint-items-api
- collection_type: postman
  name: SharePoint REST Files Lists API
  slug: postman-sharepoint-lists-api
- collection_type: postman
  name: SharePoint REST Files Search API
  slug: postman-sharepoint-search-api
- collection_type: postman
  name: SharePoint REST Files Sites API
  slug: postman-sharepoint-sites-api
- collection_type: postman
  name: SharePoint REST Files User Profiles API
  slug: postman-sharepoint-user-profiles-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/microsoft-sharepoint/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sharepoint-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sharepoint-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/sharepoint-scopes.yml
- group: build
  title: ''
  type: Packages
  url: packages/sharepoint-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/sharepoint-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/sharepoint-security.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/sharepoint-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sharepoint-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/sharepoint-rest-api-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/sharepoint-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/sharepoint-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sharepoint-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sharepoint-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/sharepoint-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/sharepoint-trust-center.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/sharepoint-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/sharepoint-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/sharepoint-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/sharepoint-cli.yml
- group: design
  title: ''
  type: Components
  url: components/sharepoint-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/sharepoint-data-model.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sharepoint-site-connection-check-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sharepoint-provision-list-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sharepoint-ensure-list-item-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sharepoint-list-item-lifecycle-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sharepoint-upload-document-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sharepoint-search-and-download-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sharepoint-site-content-inventory-workflow.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SharePoint
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sharepoint
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.microsoft.com/en-us/sharepoint
- group: build
  title: ''
  type: Code Samples
  url: https://pnp.github.io/
- group: operate
  title: ''
  type: Community
  url: https://techcommunity.microsoft.com/t5/sharepoint/ct-p/SharePoint
- group: operate
  title: ''
  type: Support
  url: https://support.microsoft.com/en-us/sharepoint
- group: commercial
  title: ''
  type: Pricing
  url: https://www.microsoft.com/en-us/microsoft-365/sharepoint/compare-sharepoint-plans
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cloud.microsoft/
created: '2024'
description: Microsoft SharePoint is a web-based collaborative platform that integrates with Microsoft Office. It provides enterprise content management, document management, and collaboration capabilities.
examples:
- key_count: 1
  name: Sharepoint File Collection Example
  slug: sharepoint-file-collection-example
- key_count: 9
  name: Sharepoint File Example
  slug: sharepoint-file-example
- key_count: 1
  name: Sharepoint List Collection Example
  slug: sharepoint-list-collection-example
- key_count: 6
  name: Sharepoint List Create Request Example
  slug: sharepoint-list-create-request-example
- key_count: 9
  name: Sharepoint List Example
  slug: sharepoint-list-example
- key_count: 1
  name: Sharepoint List Item Collection Example
  slug: sharepoint-list-item-collection-example
- key_count: 2
  name: Sharepoint List Item Create Request Example
  slug: sharepoint-list-item-create-request-example
- key_count: 6
  name: Sharepoint List Item Example
  slug: sharepoint-list-item-example
- key_count: 1
  name: Sharepoint Search Result Example
  slug: sharepoint-search-result-example
- key_count: 7
  name: Sharepoint User Profile Example
  slug: sharepoint-user-profile-example
- key_count: 9
  name: Sharepoint Web Example
  slug: sharepoint-web-example
features:
- description: Create, read, update, and delete SharePoint sites and subsites.
  name: Sites and Webs
- description: Full CRUD operations on lists, document libraries, and list items.
  name: Lists and Libraries
- description: Upload, download, check in/out, and manage documents and file versions.
  name: Document Management
- description: Create folder hierarchies and manage files within document libraries.
  name: Folders and Files
- description: Manage site, list, and item-level permissions with role assignments.
  name: Permissions and Security
- description: Full-text search across sites, documents, and content using the Search REST API.
  name: Search
- description: Access user profile properties, people search, and organizational data.
  name: User Profiles
- description: Manage content types, site columns, and metadata schemas.
  name: Content Types
- description: Subscribe to change notifications for lists and libraries via webhooks.
  name: Webhooks
- description: Access SharePoint data through Microsoft Graph API for unified Microsoft 365 integration.
  name: Microsoft Graph Integration
- description: Combine multiple REST operations into a single batch request.
  name: Batch Requests
- description: Filter, select, expand, and order data using OData query operators.
  name: OData Query Support
finops:
- name: Sharepoint Finops
  service_category: Collaboration / Document Management SaaS
  slug: sharepoint-finops
image: /assets/icons/sharepoint.png
integrations:
- description: Native integration with Teams, OneDrive, Outlook, and other Microsoft 365 apps.
  name: Microsoft 365
- description: Unified API access to SharePoint alongside all Microsoft 365 services.
  name: Microsoft Graph
- description: Power Apps, Power Automate, and Power BI integration for low-code solutions.
  name: Power Platform
- description: Azure AD for authentication, Azure Functions for serverless processing.
  name: Azure
- description: SharePoint powers file storage and document collaboration in Microsoft Teams.
  name: Teams
json_schemas:
- name: FileCollection
  property_count: 1
  slug: sharepoint-file-collection
- name: File
  property_count: 9
  slug: sharepoint-file
- name: ListCollection
  property_count: 1
  slug: sharepoint-list-collection
- name: ListCreateRequest
  property_count: 6
  slug: sharepoint-list-create-request
- name: ListItemCollection
  property_count: 1
  slug: sharepoint-list-item-collection
- name: ListItemCreateRequest
  property_count: 2
  slug: sharepoint-list-item-create-request
- name: ListItem
  property_count: 6
  slug: sharepoint-list-item
- name: List
  property_count: 9
  slug: sharepoint-list
- name: SearchResult
  property_count: 1
  slug: sharepoint-search-result
- name: UserProfile
  property_count: 7
  slug: sharepoint-user-profile
- name: Web
  property_count: 9
  slug: sharepoint-web
json_structures:
- name: Sharepoint File Collection Structure
  property_count: 1
  slug: sharepoint-file-collection-structure
- name: Sharepoint File Structure
  property_count: 9
  slug: sharepoint-file-structure
- name: Sharepoint List Collection Structure
  property_count: 1
  slug: sharepoint-list-collection-structure
- name: Sharepoint List Create Request Structure
  property_count: 6
  slug: sharepoint-list-create-request-structure
- name: Sharepoint List Item Collection Structure
  property_count: 1
  slug: sharepoint-list-item-collection-structure
- name: Sharepoint List Item Create Request Structure
  property_count: 2
  slug: sharepoint-list-item-create-request-structure
- name: Sharepoint List Item Structure
  property_count: 6
  slug: sharepoint-list-item-structure
- name: Sharepoint List Structure
  property_count: 9
  slug: sharepoint-list-structure
- name: Sharepoint Search Result Structure
  property_count: 1
  slug: sharepoint-search-result-structure
- name: Sharepoint User Profile Structure
  property_count: 7
  slug: sharepoint-user-profile-structure
- name: Sharepoint Web Structure
  property_count: 9
  slug: sharepoint-web-structure
jsonld:
- class_count: 11
  name: Sharepoint Context
  property_count: 35
  slug: sharepoint-context
layout: provider
mcp_servers:
- description: ''
  name: sharepoint-mcp.yml
  slug: sharepoint-mcpyml
modified: '2026-06-20'
name: Microsoft SharePoint
nav: Providers
network: true
overview: 'Microsoft SharePoint publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Files API, Items API, Lists API, and 3 more. Tagged areas include Collaboration, Document Management, Enterprise Content Management, Intranet, and Microsoft.


  The Microsoft SharePoint catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Microsoft SharePoint''s developer surface includes authentication, sandbox, changelog, CLI, support, pricing, and 31 more developer resources.'
plans:
- name: Sharepoint Plans Pricing
  plan_count: 5
  slug: sharepoint-plans-pricing
random_paper: 40
rate_limits:
- limit_count: 27
  name: Sharepoint Rate Limits
  slug: sharepoint-rate-limits
rules:
- name: Microsoft SharePoint API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: sharepoint-jsonschema-spectral-rules
- name: Microsoft SharePoint API Rules
  rule_count: 20
  severity_counts:
    error: 14
    hint: 0
    info: 1
    warn: 5
  slug: sharepoint-spectral-rules
scopes:
- name: Sharepoint Scopes
  scope_count: 5
  slug: sharepoint-scopes
  summary_line: 5 scopes · authorizationCode
score:
  band: developing
  composite: 51.0
  delta: 0.0
  facets:
    commercial_clarity: 57.9
    contract_quality: 22.6
    developer_ergonomics: 50.0
    discoverability: 64.8
    governance: 69.8
    operational_transparency: 68.4
  previous_composite: 51.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 6
      marker_coverage: 100.0
      total: 6
    mcp: first-party
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sharepoint/refs/heads/main/screenshots/sharepoint-2026-06-20T193748.png
security:
- kind: authentication
  name: Sharepoint Authentication
  slug: sharepoint-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Sharepoint Domain Security
  slug: sharepoint-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Sharepoint Vulnerability Disclosure
  slug: sharepoint-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Sharepoint Trust Center
  slug: sharepoint-trust-center
  summary_line: SOC 1 Type 2, SOC 2 Type 2, SOC 3, ISO 27001, ISO 27017, ISO 27018, ISO 27701, ISO 22301, ISO 9001, FedRAMP High, HIPAA / HITECH, HITRUST CSF, PCI DSS, GDPR, CSA STAR
slug: sharepoint
solutions:
- description: Cloud-hosted SharePoint as part of Microsoft 365 with REST and Graph APIs.
  name: SharePoint Online
- description: On-premises SharePoint with REST, CSOM, and server-side object model.
  name: SharePoint Server
- description: Modern client-side development framework for building web parts and extensions.
  name: SharePoint Framework (SPFx)
tags:
- Collaboration
- Document Management
- Enterprise Content Management
- Intranet
- Microsoft
use_cases:
- description: Automate document upload, metadata tagging, and approval workflows.
  name: Document Automation
- description: Programmatically manage site pages, news posts, and navigation.
  name: Intranet Content Management
- description: Sync SharePoint list data with external databases and applications.
  name: Data Integration
- description: Migrate content between SharePoint sites or from file shares to SharePoint.
  name: Migration
- description: Build SPFx web parts and extensions with SharePoint Framework.
  name: Custom Applications
- description: Manage retention policies, sensitivity labels, and audit logs.
  name: Compliance and Governance
- description: Build custom search experiences with facets, refiners, and result types.
  name: Search Integration
- description: Trigger and manage automated workflows based on SharePoint events.
  name: Power Automate Flows
website: https://developer.microsoft.com/en-us/sharepoint
---
