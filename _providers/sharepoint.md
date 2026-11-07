---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - scopes
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 35.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Sharepoint Agentic Access
  operation_count: 15
  slug: sharepoint-agentic-access
  summary_line: 15 operations · 5 acting
api_count: 14
apis:
- description: Client-side object model for SharePoint that provides access to SharePoint objects through .NET managed or JavaScript libraries.
  name: SharePoint CSOM (Client-Side Object Model)
  slug: csom-client-side-object-model
- description: SharePoint webhooks provide a way to get notified about changes to SharePoint lists and document libraries.
  name: SharePoint Webhooks API
  slug: webhooks-api
- baseURL: https://{tenant}.sharepoint.com/_api/
  baseurl_source: declared
  description: File upload, download, and management
  name: Microsoft SharePoint Files API
  slug: sharepoint-files-api
- baseURL: https://{tenant}.sharepoint.com/_api/
  baseurl_source: declared
  description: List item operations
  name: Microsoft SharePoint Items API
  slug: sharepoint-items-api
- baseURL: https://{tenant}.sharepoint.com/_api/
  baseurl_source: declared
  description: List and library operations
  name: Microsoft SharePoint Lists API
  slug: sharepoint-lists-api
- baseURL: https://{tenant}.sharepoint.com/_api/
  baseurl_source: declared
  description: Search query operations
  name: Microsoft SharePoint Search API
  slug: sharepoint-search-api
- baseURL: https://{tenant}.sharepoint.com/_api/
  baseurl_source: declared
  description: Site and web operations
  name: Microsoft SharePoint Sites API
  slug: sharepoint-sites-api
- baseURL: https://{tenant}.sharepoint.com/_api/
  baseurl_source: declared
  description: User profile operations
  name: Microsoft SharePoint User Profiles API
  slug: sharepoint-user-profiles-api
- description: 'The Microsoft Graph SharePoint Sites API provides access to SharePoint sites, lists, and document libraries through the unified Microsoft Graph endpoint. It enables developers to manage site content, '
  name: Microsoft Graph SharePoint Sites API
  slug: graph-sites-api
- description: 'The SharePoint Search REST API provides full-text search capabilities across SharePoint content including sites, lists, libraries, and documents. It supports keyword query language, query refinement, '
  name: SharePoint Search REST API
  slug: search-api
- description: 'The SharePoint Framework (SPFx) is a development model for building client-side web parts, extensions, and adaptive card extensions for SharePoint and Microsoft Teams. It uses modern web technologies '
  name: SharePoint Framework (SPFx)
  slug: framework
- baseURL: https://{tenant}.sharepoint.com/_api/
  baseurl_source: declared
  description: The $batch API from Microsoft SharePoint — 1 operation(s) for $batch.
  name: Microsoft SharePoint $batch API
  slug: microsoft-sharepoint-batch-api
- baseURL: https://{tenant}.sharepoint.com/_api/
  baseurl_source: declared
  description: The ListItems API from Microsoft SharePoint — 2 operation(s) for listitems.
  name: Microsoft SharePoint ListItems API
  slug: microsoft-sharepoint-listitems-api
- baseURL: https://{tenant}.sharepoint.com/_api/
  baseurl_source: declared
  description: The Site API from Microsoft SharePoint — 1 operation(s) for site.
  name: Microsoft SharePoint Site API
  slug: microsoft-sharepoint-site-api
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
artifact_total: 112
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
- collection_type: open
  name: SharePoint REST Files API
  slug: open-sharepoint-files-api
- collection_type: open
  name: SharePoint REST Files Items API
  slug: open-sharepoint-items-api
- collection_type: open
  name: SharePoint REST Files Lists API
  slug: open-sharepoint-lists-api
- collection_type: open
  name: SharePoint REST Files Search API
  slug: open-sharepoint-search-api
- collection_type: open
  name: SharePoint REST Files Sites API
  slug: open-sharepoint-sites-api
- collection_type: open
  name: SharePoint REST Files User Profiles API
  slug: open-sharepoint-user-profiles-api
common:
- group: design
  href: https://artifacts.apis.io/sharepoint/rules/sharepoint-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/sharepoint-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/sharepoint/rules/sharepoint-rules.yml
  title: ''
  type: Spectral
  url: rules/sharepoint-rules.yml
- group: design
  href: https://artifacts.apis.io/sharepoint/rules/sharepoint-jsonschema-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/sharepoint-jsonschema-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/sharepoint/json-ld/sharepoint-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/sharepoint-context.jsonld
- group: design
  href: https://artifacts.apis.io/sharepoint/vocabulary/sharepoint-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/sharepoint-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/sharepoint/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.microsoft.com/en-us/trust-center
- group: operate
  title: ''
  type: Deprecation
  url: https://learn.microsoft.com/en-us/graph/versioning-and-support#deprecation
- group: build
  href: https://artifacts.apis.io/sharepoint/mcp/sharepoint-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/sharepoint-tool-crosswalk.yml
- group: other
  href: https://artifacts.apis.io/sharepoint/hosts/sharepoint-hosts.yml
  title: ''
  type: Hosts
  url: hosts/sharepoint-hosts.yml
- group: build
  href: https://artifacts.apis.io/sharepoint/integrations/sharepoint-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/sharepoint-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/sharepoint/vendors/sharepoint-vendors.yml
  title: ''
  type: Vendors
  url: vendors/sharepoint-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://www.microsoft.com/security
- group: other
  title: ''
  type: Leadership
  url: https://news.microsoft.com/leadership
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/adaptive-cards/sdk/rendering-cards/android/getting-started
- group: commercial
  href: https://artifacts.apis.io/sharepoint/plans/sharepoint-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/sharepoint-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/sharepoint/rate-limits/sharepoint-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/sharepoint-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/sharepoint/finops/sharepoint-finops.yml
  title: ''
  type: FinOps
  url: finops/sharepoint-finops.yml
- group: start
  title: ''
  type: Portal
  url: https://portal.azure.com/
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/sharepoint/dev/
- group: build
  title: ''
  type: SDKs
  url: https://learn.microsoft.com/en-us/sharepoint/dev/sp-add-ins/complete-basic-operations-using-sharepoint-rest-endpoints
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.microsoft.com/en-us/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: company
  title: ''
  type: Blog
  url: https://techcommunity.microsoft.com/t5/s/gxcuf89792/rss/board?board.id=SPBlog
- group: company
  title: ''
  type: Website
  url: https://www.microsoft.com/
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/microsoft-sharepoint/overview
- group: agent
  href: https://artifacts.apis.io/sharepoint/agentic-access/sharepoint-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/sharepoint-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/sharepoint/authentication/sharepoint-authentication.yml
  title: ''
  type: Authentication
  url: authentication/sharepoint-authentication.yml
- group: auth
  href: https://artifacts.apis.io/sharepoint/scopes/sharepoint-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/sharepoint-scopes.yml
- group: build
  href: https://artifacts.apis.io/sharepoint/packages/sharepoint-packages.yml
  title: ''
  type: Packages
  url: packages/sharepoint-packages.yml
- group: agent
  href: https://artifacts.apis.io/sharepoint/well-known/sharepoint-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/sharepoint-well-known.yml
- group: auth
  href: https://artifacts.apis.io/sharepoint/well-known/sharepoint-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/sharepoint-security.txt
- group: agent
  href: https://artifacts.apis.io/sharepoint/mcp/sharepoint-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/sharepoint-mcp.yml
- group: agent
  href: https://artifacts.apis.io/sharepoint/llms/sharepoint-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/sharepoint-llms.txt
- group: other
  href: https://artifacts.apis.io/sharepoint/overlays/sharepoint-rest-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/sharepoint-rest-api-overlay.yaml
- group: design
  href: https://artifacts.apis.io/sharepoint/conformance/sharepoint-conformance.yml
  title: ''
  type: Conformance
  url: conformance/sharepoint-conformance.yml
- group: design
  href: https://artifacts.apis.io/sharepoint/errors/sharepoint-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/sharepoint-problem-types.yml
- group: design
  href: https://artifacts.apis.io/sharepoint/lifecycle/sharepoint-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/sharepoint-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/sharepoint/security/sharepoint-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sharepoint-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/sharepoint/security/sharepoint-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/sharepoint-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/sharepoint/security/sharepoint-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/sharepoint-trust-center.yml
- group: start
  href: https://artifacts.apis.io/sharepoint/sandbox/sharepoint-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/sharepoint-sandbox.yml
- group: design
  href: https://artifacts.apis.io/sharepoint/conventions/sharepoint-conventions.yml
  title: ''
  type: Conventions
  url: conventions/sharepoint-conventions.yml
- group: operate
  href: https://artifacts.apis.io/sharepoint/changelog/sharepoint-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/sharepoint-changelog.yml
- group: build
  href: https://artifacts.apis.io/sharepoint/cli/sharepoint-cli.yml
  title: ''
  type: CLI
  url: cli/sharepoint-cli.yml
- group: design
  href: https://artifacts.apis.io/sharepoint/components/sharepoint-components.yml
  title: ''
  type: Components
  url: components/sharepoint-components.yml
- group: design
  href: https://artifacts.apis.io/sharepoint/data-model/sharepoint-data-model.yml
  title: ''
  type: DataModel
  url: data-model/sharepoint-data-model.yml
- group: design
  href: https://artifacts.apis.io/sharepoint/arazzo/sharepoint-site-connection-check-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/sharepoint-site-connection-check-workflow.yml
- group: design
  href: https://artifacts.apis.io/sharepoint/arazzo/sharepoint-provision-list-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/sharepoint-provision-list-workflow.yml
- group: design
  href: https://artifacts.apis.io/sharepoint/arazzo/sharepoint-ensure-list-item-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/sharepoint-ensure-list-item-workflow.yml
- group: design
  href: https://artifacts.apis.io/sharepoint/arazzo/sharepoint-list-item-lifecycle-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/sharepoint-list-item-lifecycle-workflow.yml
- group: design
  href: https://artifacts.apis.io/sharepoint/arazzo/sharepoint-upload-document-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/sharepoint-upload-document-workflow.yml
- group: design
  href: https://artifacts.apis.io/sharepoint/arazzo/sharepoint-search-and-download-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/sharepoint-search-and-download-workflow.yml
- group: design
  href: https://artifacts.apis.io/sharepoint/arazzo/sharepoint-site-content-inventory-workflow.yml
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
  type: CodeExamples
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
- has_sources: true
  method: generated
  name: Sharepoint Finops
  primary_unit: ''
  service_category: Collaboration / Document Management SaaS
  slug: sharepoint-finops
  template: false
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
- name: GenericObject
  property_count: 0
  slug: sharepoint-generic-object
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
- description: Remote MCP server at agent365.svc.cloud.microsoft over HTTP requiring OAuth; 35 tools listed.
  name: Work IQ SharePoint
  slug: work-iq-sharepoint
modified: '2026-11-05'
name: Microsoft SharePoint
nav: Providers
network: true
overview: 'Microsoft SharePoint is listed with 14 APIs on the [APIs.io](https://apis.io/) network, including Files API, Items API, Lists API, and 11 more. Tagged areas include Collaboration, Document Management, Enterprise Content Management, Intranet, and Microsoft.


  The Microsoft SharePoint catalog on APIs.io includes 1 JSON-LD context and 3 Spectral governance rulesets.


  Microsoft SharePoint''s developer surface includes getting-started guide, developer portal, documentation, engineering blog, authentication, sandbox, changelog, and 55 more developer resources.'
plans:
- name: Sharepoint Plans Pricing
  plan_count: 5
  slug: sharepoint-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 27
  name: Sharepoint Rate Limits
  slug: sharepoint-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Microsoft SharePoint — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: sharepoint-jsonschema-spectral-rules
- authorship: generated
  effective_rule_count: 99
  extends:
  - spectral:oas
  name: Microsoft SharePoint API Rules
  rule_count: 58
  severity_counts:
    error: 54
    hint: 0
    info: 2
    warn: 2
  slug: sharepoint-rules
- authorship: generated
  effective_rule_count: 60
  extends:
  - spectral:oas
  name: Microsoft SharePoint API Rules
  rule_count: 19
  severity_counts:
    error: 13
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
  band: strong
  composite: 58.5
  coverage:
    artifact_dirs: 42
    catalog_earned: 65.0
    catalog_earned_first_party: 0.0
    catalog_gap: 50.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 7.1
  facets:
    access_clarity: 50.0
    contract_governance: 31.8
    contract_quality: 42.2
    developer_ergonomics: 81.5
    discoverability: 71.7
    operational_transparency: 52.6
  previous_composite: 51.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 7
      marker_coverage: 70.0
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
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/sharepoint/sharepoint-2026-06-20T193748.png
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
skill_count: 3
skills:
- name: sharepoint-manage-list-items
  slug: sharepoint-manage-list-items
- name: sharepoint-search-content
  slug: sharepoint-search-content
- name: sharepoint-upload-and-download-files
  slug: sharepoint-upload-and-download-files
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
website: https://www.microsoft.com/
---
