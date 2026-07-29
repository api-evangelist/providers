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
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 46.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 142
  human_in_the_loop: 2
  name: Onshape Agentic Access
  operation_count: 302
  slug: onshape-agentic-access
  summary_line: 302 operations · 142 acting · 2 human-in-the-loop
api_count: 42
apis:
- description: Manage user purchases, subscriptions, and consumables.
  name: Onshape Account API
  slug: onshape-account-api
- description: Create and manage enterprise aliases. (Enterprise admins only.)
  name: Onshape Alias API
  slug: onshape-alias-api
- description: Manage application preferences.
  name: Onshape APIApplication API
  slug: onshape-apiapplication-api
- description: Manage the application-specific metadata that associates application data with Onshape data.
  name: Onshape AppAssociativeData API
  slug: onshape-appassociativedata-api
- description: Access and modify application elements.
  name: Onshape AppElement API
  slug: onshape-appelement-api
- description: Create and manage assemblies.
  name: Onshape Assembly API
  slug: onshape-assembly-api
- description: Get billing plan data for applications.
  name: Onshape Billing API
  slug: onshape-billing-api
- description: Create, modify, and translate blob elements.
  name: Onshape BlobElement API
  slug: onshape-blobelement-api
- description: Create, read, update, and delete comments.
  name: Onshape Comment API
  slug: onshape-comment-api
- description: Access company information.
  name: Onshape Company API
  slug: onshape-company-api
- description: Create and manage documents.
  name: Onshape Document API
  slug: onshape-document-api
- description: Access, create, and translate drawings.
  name: Onshape Drawing API
  slug: onshape-drawing-api
- description: Access and manage Elements. Every Element in an Onshape document is represented by a tab.
  name: Onshape Element API
  slug: onshape-element-api
- description: Access valid export rules.
  name: Onshape ExportRule API
  slug: onshape-exportrule-api
- description: Access and manage Feature Studio Elements.
  name: Onshape FeatureStudio API
  slug: onshape-featurestudio-api
- description: Access and modify folder sharing permissions.
  name: Onshape Folder API
  slug: onshape-folder-api
- description: Access the list of things that can be inserted into a document.
  name: Onshape Insertable API
  slug: onshape-insertable-api
- description: Manage non-geometric [items](https://cad.onshape.com/help/Content/Plans/items.htm). (Professional, Educator, and Enterprise accounts only.)
  name: Onshape Item API
  slug: onshape-item-api
- description: Work with the Onshape Material Library.
  name: Onshape Material API
  slug: onshape-material-api
- description: Access and modify metadata.
  name: Onshape Metadata API
  slug: onshape-metadata-api
- description: Access properties associated with metadata categories.
  name: Onshape MetadataCategory API
  slug: onshape-metadatacategory-api
- description: Manage the set of valid part numbers.
  name: Onshape NumberingScheme API
  slug: onshape-numberingscheme-api
- description: Get the OpenAPI specification for the Onshape API.
  name: Onshape OpenApi API
  slug: onshape-openapi-api
- description: Export Parts and access Part details.
  name: Onshape Part API
  slug: onshape-part-api
- description: Create valid part numbers.
  name: Onshape PartNumber API
  slug: onshape-partnumber-api
- description: Access and modify Part Studios.
  name: Onshape PartStudio API
  slug: onshape-partstudio-api
- description: Access information on how entities are structured within designs and documents.
  name: Onshape ProductStructure API
  slug: onshape-productstructure-api
- description: Create, access, and delete templates for properties tables.
  name: Onshape PropertiesTableTemplate API
  slug: onshape-propertiestabletemplate-api
- description: Access publication information.
  name: Onshape Publication API
  slug: onshape-publication-api
- description: 'Endpoints for creating , updating, and managing releases. See [API Guide: Release Management](https://onshape-public.github.io/docs/api-adv/relmgmt/).'
  name: Onshape ReleasePackage API
  slug: onshape-releasepackage-api
- description: 'Get revision information. See [API Guide: Release Management](https://onshape-public.github.io/docs/api-adv/relmgmt/)'
  name: Onshape Revision API
  slug: onshape-revision-api
- description: Access sketch information.
  name: Onshape Sketch API
  slug: onshape-sketch-api
- description: Work with Onshape standard content.
  name: Onshape StandardContent API
  slug: onshape-standardcontent-api
- description: Create, access, and modify Tasks and Action Items.
  name: Onshape Task API
  slug: onshape-task-api
- description: Access team information.
  name: Onshape Team API
  slug: onshape-team-api
- description: Access, modify, and delete thumbnails.
  name: Onshape Thumbnail API
  slug: onshape-thumbnail-api
- description: Import and export Onshape surfaces, parts, Part Studios, Assemblies, and subassemblies to/from other file formats (STL, PARASOLID, etc).
  name: Onshape Translation API
  slug: onshape-translation-api
- description: Access user information.
  name: Onshape User API
  slug: onshape-user-api
- description: Create, modify, and access variables.
  name: Onshape Variables API
  slug: onshape-variables-api
- description: Get all versions of the Onshape REST APIs.
  name: Onshape Version API
  slug: onshape-version-api
- description: Create and manage [webhooks](https://onshape-public.github.io/docs/app-dev/webhook/).
  name: Onshape Webhook API
  slug: onshape-webhook-api
- description: Access and modify workflows.
  name: Onshape Workflow API
  slug: onshape-workflow-api
artifact_total: 51
asyncapis:
- description: ''
  name: Onshape Events Webhooks
  slug: onshape-events-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/onshape-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/onshape-agentic-access.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/onshape-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/onshape-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/onshape-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/onshape-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/onshape-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/onshape-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/onshape-openapi-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/onshape-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.onshape.com/en/security
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/onshape-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/onshape-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.onshape.com/
- group: operate
  title: ''
  type: Deprecation
  url: https://onshape-public.github.io/docs/api-versions/
- group: design
  title: ''
  type: Conventions
  url: conventions/onshape-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/onshape-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/onshape-events-webhooks.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/onshape-rate-limits.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/onshape-changelog.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/onshape-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.onshape.com/en/security
- group: auth
  title: ''
  type: TrustCenter
  url: security/onshape-trust-center.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://cad.onshape.com/appstore/dev-portal
- group: docs
  title: ''
  type: Documentation
  url: https://onshape-public.github.io/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://cad.onshape.com/glassworks/explorer/
- group: start
  title: ''
  type: GettingStarted
  url: https://onshape-public.github.io/docs/api-intro/quickstart/
- group: operate
  title: ''
  type: Support
  url: https://onshape-public.github.io/docs/help/
- group: company
  title: ''
  type: Blog
  url: https://www.onshape.com/en/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/onshape-public
- group: commercial
  title: ''
  type: Pricing
  url: https://www.onshape.com/en/pricing
- group: start
  title: ''
  type: SignUp
  url: https://cad.onshape.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.onshape.com/en/legal/terms-of-use
created: '2026-07-17'
description: Onshape is a cloud-native computer-aided design (CAD) and product data management (PDM) platform, part of PTC, that runs entirely in a web browser with real-time collaboration, versioning, and configurations. Its public REST API (OpenAPI 3.0.1, base https://cad.onshape.com/api/v16) exposes documents, workspaces, versions and microversions, Part Studios, parts, assemblies, drawings, metadata, translations (CAD import/export), release management, and webhooks. Authentication is via OAuth 2.0 or HMAC-signed API keys, with offset/limit pagination and per-endpoint plus annual API call limits. Onshape was surfaced as an a16z portfolio company and enriched with its real developer surface by the API Evangelist pipeline.
image: https://github.com/onshape-public.png
layout: provider
mcp_servers:
- description: ''
  name: onshape-mcp.yml
  slug: onshape-mcpyml
modified: '2026-07-20'
name: Onshape
nav: Providers
network: true
overview: 'Onshape publishes 42 APIs on the [APIs.io](https://apis.io/) network, including Account API, Alias API, APIApplication API, and 39 more. Tagged areas include Company, CAD, PLM, Product Data Management, and Engineering.


  The Onshape catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Onshape''s developer surface includes authentication, changelog, documentation, API reference, getting-started guide, support, engineering blog, and 27 more developer resources.'
random_paper: 21
rate_limits:
- limit_count: 0
  name: Onshape Rate Limits
  slug: onshape-rate-limits
scopes:
- name: Onshape Scopes
  scope_count: 24
  slug: onshape-scopes
  summary_line: 24 scopes · authorizationCode
score:
  band: developing
  composite: 55.1
  delta: -2.4
  facets:
    commercial_clarity: 50.0
    contract_quality: 59.5
    developer_ergonomics: 62.5
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 63.2
  previous_composite: 57.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 42
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Onshape Authentication
  slug: onshape-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Onshape Domain Security
  slug: onshape-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Onshape Vulnerability Disclosure
  slug: onshape-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Onshape Trust Center
  slug: onshape-trust-center
  summary_line: SOC 2 Type 2
slug: onshape
tags:
- Company
- CAD
- PLM
- Product Data Management
- Engineering
- Manufacturing
- Design
- Cloud
- Developer Tools
website: https://cad.onshape.com/appstore/dev-portal
---
