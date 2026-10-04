---
access_model:
  confidence: high
  label: Paid · 14-day free trial · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - https://www.archbee.com/pricing
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
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 58.5
  scored_at: '2026-10-03'
agentic_access:
- acting_count: 21
  human_in_the_loop: 1
  name: Archbee Agentic Access
  operation_count: 31
  slug: archbee-agentic-access
  summary_line: 31 operations · 21 acting · 1 human-in-the-loop
api_count: 11
apis:
- description: 'Archbee''s Model Context Protocol server, shipped in two deployments: a hosted remote endpoint at https://api.archbee.com/api/public-mcp-ds/sse that an MCP client connects to over OAuth 2.1 (dynamic cl'
  name: Archbee MCP Server
  slug: archbee-mcp-server
- baseURL: https://api.archbee.com/api/public-api
  baseurl_source: declared
  description: Magic-link access requests for gated portals
  name: Archbee Access Control API
  phrasing_intents:
  - id: requestMagicLinkAccess
    intent: Request magic-link access to a docs space
    question: How can a reader ask to be let into a magic-link protected Archbee docs portal?
  phrasing_ops: 1
  slug: archbee-access-control-api
- baseURL: https://api.archbee.com/api/public-api
  baseurl_source: declared
  description: Sync and inspect an imported OpenAPI reference
  name: Archbee API Reference API
  phrasing_intents:
  - id: infoOpenApiDocument
    intent: Get info about an imported OpenAPI tree
    question: How do I see details about an OpenAPI reference I already imported into my docs?
  - id: syncOpenApiDocument
    intent: Import or re-sync an OpenAPI file as API reference
    question: How do I push an updated OpenAPI spec so my API reference docs refresh?
  phrasing_ops: 2
  slug: archbee-api-reference-api
- baseURL: https://api.archbee.com/api/public-api
  baseurl_source: declared
  description: Create, read, update, delete and search documents
  name: Archbee Documents API
  phrasing_intents:
  - id: deleteDocument
    intent: Permanently delete a document
    question: How do I permanently remove a doc from my documentation?
  - id: getDocument
    intent: Retrieve a document's content
    question: How do I fetch the contents of a single Archbee doc by its id?
  - id: updateCreateDocument
    intent: Create or update a document
    question: How do I write new markdown content into a doc, creating it if it doesn't exist yet?
  - id: searchDocument
    intent: Search documents or ask the docs AI
    question: How can I search across my docs by keyword or title?
  - id: importContent
    intent: Import markdown files as new docs
    question: How do I import an existing markdown file as a new doc?
  phrasing_ops: 5
  slug: archbee-documents-api
- baseURL: https://api.archbee.com/api/public-api
  baseurl_source: declared
  description: Upload, list, move, replace and delete File Manager files
  name: Archbee File Manager API
  phrasing_intents:
  - id: deleteAFileManagerFile
    intent: Delete a file or folder from the File Manager
    question: How do I delete an uploaded asset from the File Manager?
  - id: listFileManagerFiles
    intent: List files and folders in the File Manager
    question: What images and files have been uploaded to my File Manager?
  - id: moveAFileManagerFile
    intent: Move a File Manager file to another folder
    question: How do I move an uploaded image into a different folder?
  - id: overwriteAFileManagerFile
    intent: Replace an existing File Manager file
    question: How do I swap out an image everywhere it's embedded without changing its URL?
  - id: uploadSingleFile
    intent: Upload a new file to the File Manager
    question: How do I upload a new file to the Archbee File Manager?
  phrasing_ops: 5
  slug: archbee-file-manager-api
- baseURL: https://api.archbee.com/api/public-api
  baseurl_source: declared
  description: Team member and access management
  name: Archbee Members API
  phrasing_intents:
  - id: listMembers
    intent: List members of a documentation space
    question: Who has access to a particular documentation space?
  phrasing_ops: 1
  slug: archbee-members-api
- baseURL: https://api.archbee.com/api/public-api
  baseurl_source: declared
  description: Organization-level export and display rules
  name: Archbee Organization API
  phrasing_intents:
  - id: organizationDisplayRules
    intent: Export an organization's display rules
    question: How do I get a list of all display rules set up for my team?
  - id: organizationExport
    intent: Export all of an organization's data
    question: How do I back up all my team's spaces, documents and assets from Archbee?
  phrasing_ops: 2
  slug: archbee-organization-api
- baseURL: https://api.archbee.com/api/public-api
  baseurl_source: declared
  description: Page content management
  name: Archbee Pages API
  phrasing_intents:
  - id: listPages
    intent: List pages in a documentation space
    question: What pages exist in a given docs space?
  - id: createPage
    intent: Create a page in a documentation space
    question: How do I add a new page to a docs space?
  phrasing_ops: 2
  slug: archbee-pages-api
- baseURL: https://api.archbee.com/api/public-api
  baseurl_source: declared
  description: Grouping of documentation spaces
  name: Archbee Space Groups API
  phrasing_intents:
  - id: createSpaceGroup
    intent: Create a space group
    question: How do I create a group to organize several documentation spaces?
  - id: deleteSpaceGroup
    intent: Delete a space group
    question: How do I remove a space group I no longer need?
  phrasing_ops: 2
  slug: archbee-space-groups-api
- baseURL: https://api.archbee.com/api/public-api
  baseurl_source: declared
  description: Documentation space management
  name: Archbee Spaces API
  phrasing_intents:
  - id: listSpaces
    intent: List documentation spaces
    question: Which documentation spaces can I access?
  - id: createSpace
    intent: Create a space with name and visibility
    question: How do I create a docs space and set whether it's public or private?
  - id: getSpace
    intent: Get a documentation space's details
    question: How do I look up the details of one specific docs space?
  - id: deleteSpace
    intent: Delete a space by its path id
    question: How do I delete a documentation space along with all of its content?
  - id: cloneSpace
    intent: Clone a space into a space group
    question: How do I duplicate an existing docs space?
  - id: postSpaceCreate
    intent: Create a space with AI, review or branching
    question: Can I create a space that turns on AI, the review system or branching from the start?
  - id: deleteSpaceDelete
    intent: Delete a space by target space id
    question: How do I delete a space by passing its id in the request body?
  - id: publishSpace
    intent: Publish a space's documents
    question: How do I publish my docs so readers see the latest changes?
  phrasing_ops: 9
  slug: archbee-spaces-api
- baseURL: https://api.archbee.com/api/public-api
  baseurl_source: declared
  description: Reader-submitted suggested changes — merge or discard
  name: Archbee Suggestions API
  phrasing_intents:
  - id: discardSuggestionDocument
    intent: Discard a suggested change
    question: How do I reject a suggested edit without applying it to the doc?
  - id: mergeSuggestionIntoMainDocument
    intent: Merge a suggested change into its document
    question: How do I accept a suggested edit and apply it to the original doc?
  phrasing_ops: 2
  slug: archbee-suggestions-api
artifact_total: 68
asyncapis:
- description: ''
  name: Archbee Webhooks
  slug: archbee-webhooks
collections:
- collection_type: postman
  name: Archbee Public API
  slug: postman-archbee-public-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Archbee Public API
  slug: open-archbee-public-api
common:
- group: company
  title: ''
  type: Website
  url: https://www.archbee.com/
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/archbee/overview
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/archbee/refs/heads/main/agentic-access/archbee-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/archbee-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/archbee/refs/heads/main/security/archbee-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/archbee-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/archbee/refs/heads/main/security/archbee-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/archbee-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/archbee/refs/heads/main/security/archbee-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/archbee-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/archbee/refs/heads/main/authentication/archbee-authentication.yml
  title: ''
  type: Authentication
  url: authentication/archbee-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/archbee
- group: start
  title: ''
  type: Portal
  url: https://www.archbee.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.archbee.com/
- group: company
  title: ''
  type: Blog
  url: https://www.archbee.com/blog
- group: start
  title: ''
  type: Signup
  url: https://app.archbee.com/signup
- group: start
  title: ''
  type: Login
  url: https://app.archbee.com/signin
- group: commercial
  title: ''
  type: Pricing
  url: https://www.archbee.com/pricing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/archbee
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.archbee.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.archbee.com/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.archbee.com/
- group: operate
  title: ''
  type: Support
  url: mailto:support@archbee.com
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/archbee/refs/heads/main/rules/archbee-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/archbee/refs/heads/main/vocabulary/archbee-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: https://raw.githubusercontent.com/api-evangelist/archbee/refs/heads/main/json-ld/archbee-api-context.jsonld
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.archbee.com/llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/archbee/refs/heads/main/llms/archbee-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/archbee-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/archbee/refs/heads/main/mcp/archbee-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/archbee-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/archbee/refs/heads/main/mcp/archbee-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/archbee-tool-crosswalk.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/archbee/refs/heads/main/packages/archbee-packages.yml
  title: ''
  type: Packages
  url: packages/archbee-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/archbee/refs/heads/main/packages/archbee-packages.yml
  title: ''
  type: SDKs
  url: packages/archbee-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/archbee/refs/heads/main/cli/archbee-cli.yml
  title: ''
  type: CLI
  url: cli/archbee-cli.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/archbee/refs/heads/main/components/archbee-components.yml
  title: ''
  type: Components
  url: components/archbee-components.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/archbee/refs/heads/main/well-known/archbee-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/archbee-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/archbee/refs/heads/main/scopes/archbee-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/archbee-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/archbee/refs/heads/main/conventions/archbee-conventions.yml
  title: ''
  type: Conventions
  url: conventions/archbee-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/archbee/refs/heads/main/errors/archbee-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/archbee-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/archbee/refs/heads/main/lifecycle/archbee-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/archbee-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/archbee/refs/heads/main/conformance/archbee-conformance.yml
  title: ''
  type: Conformance
  url: conformance/archbee-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/archbee/refs/heads/main/security/archbee-trust-center.yml
  title: ''
  type: Compliance
  url: security/archbee-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/archbee/refs/heads/main/security/archbee-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/archbee-vulnerability-disclosure.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/archbee/refs/heads/main/data-model/archbee-data-model.yml
  title: ''
  type: DataModel
  url: data-model/archbee-data-model.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/archbee/refs/heads/main/overlays/archbee-public-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/archbee-public-api-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/archbee/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/archbee/refs/heads/main/plans/archbee-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/archbee-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/archbee/refs/heads/main/rate-limits/archbee-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/archbee-rate-limits.yml
- group: docs
  title: ''
  type: APIReference
  url: https://www.archbee.com/docs/get-document
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.archbee.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.archbee.com/docs/how-to-get-started
- group: operate
  title: ''
  type: HelpCenter
  url: https://docs.archbee.com/
created: '2026-03-16'
description: Archbee is a documentation and knowledge-portal platform for software teams. It creates, manages and publishes technical documentation, API references and internal wikis, with collaborative editing, revision history, branching and review, custom-domain publishing, an embeddable in-product docs widget, and AI-assisted search, writing and translation. Archbee imports and syncs OpenAPI and Postman collections to generate rendered API reference documentation. Its own developer surface is a 24-operation REST Public API at https://api.archbee.com/api/public-api, a first-party CLI (@archbee/cli), a React widget package (@archbee/app-widget), and a Model Context Protocol server shipped in two deployments — a hosted OAuth endpoint at https://api.archbee.com/api/public-mcp-ds/sse and a local stdio server on npm as @archbee/mcp — exposing 26 tools over documents, spaces, templates, snippets and variables.
examples:
- key_count: 12
  name: Archbee Document Request Example
  slug: archbee-document-request-example
- key_count: 2
  name: Archbee Document Response Example
  slug: archbee-document-response-example
- key_count: 8
  name: Archbee Document Search Request Example
  slug: archbee-document-search-request-example
- key_count: 2
  name: Archbee Document Search Response Example
  slug: archbee-document-search-response-example
- key_count: 2
  name: Archbee Error Response Example
  slug: archbee-error-response-example
- key_count: 2
  name: Archbee File Upload Response Example
  slug: archbee-file-upload-response-example
- key_count: 5
  name: Archbee Space Create Request Example
  slug: archbee-space-create-request-example
- key_count: 4
  name: Archbee Space Group Create Request Example
  slug: archbee-space-group-create-request-example
- key_count: 3
  name: Archbee Space Update Request Example
  slug: archbee-space-update-request-example
features:
- description: Create and publish beautiful API reference documentation with OpenAPI/Swagger support.
  name: API Documentation
- description: Real-time collaborative editing for documentation teams with version control.
  name: Collaborative Editing
- description: Build customizable developer portals with branded documentation sites.
  name: Developer Portal
- description: Internal and external knowledge base creation with powerful search.
  name: Knowledge Base
- description: Document versioning and change history for tracking documentation evolution.
  name: Version Control
- description: Integrations with GitHub, Slack, Jira, and other developer tools.
  name: Integrations
- description: AI-powered writing assistance for faster technical documentation creation.
  name: AI Writing Assistant
- description: Host documentation on custom domains with SSL included.
  name: Custom Domains
finops:
- name: Archbee Finops
  service_category: API
  slug: archbee-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/archbee.png
json_schemas:
- name: Document Request
  property_count: 12
  slug: archbee-document-request
- name: Document Response
  property_count: 2
  slug: archbee-document-response
- name: Document Search Request
  property_count: 8
  slug: archbee-document-search-request
- name: Document Search Response
  property_count: 2
  slug: archbee-document-search-response
- name: Error Response
  property_count: 2
  slug: archbee-error-response
- name: File Upload Response
  property_count: 2
  slug: archbee-file-upload-response
- name: Space Create Request
  property_count: 5
  slug: archbee-space-create-request
- name: Space Group Create Request
  property_count: 4
  slug: archbee-space-group-create-request
- name: Space Update Request
  property_count: 3
  slug: archbee-space-update-request
json_structures:
- name: Archbee Document Request Structure
  property_count: 12
  slug: archbee-document-request-structure
- name: Archbee Document Response Structure
  property_count: 2
  slug: archbee-document-response-structure
- name: Archbee Document Search Request Structure
  property_count: 8
  slug: archbee-document-search-request-structure
- name: Archbee Document Search Response Structure
  property_count: 2
  slug: archbee-document-search-response-structure
- name: Archbee Error Response Structure
  property_count: 2
  slug: archbee-error-response-structure
- name: Archbee File Upload Response Structure
  property_count: 2
  slug: archbee-file-upload-response-structure
- name: Archbee Space Create Request Structure
  property_count: 5
  slug: archbee-space-create-request-structure
- name: Archbee Space Group Create Request Structure
  property_count: 4
  slug: archbee-space-group-create-request-structure
- name: Archbee Space Update Request Structure
  property_count: 3
  slug: archbee-space-update-request-structure
jsonld:
- class_count: 10
  name: Archbee Api Context
  property_count: 24
  slug: archbee-api-context
layout: provider
mcp_servers:
- description: ''
  name: Archbee MCP Server
  slug: archbee-mcp-server
modified: '2026-09-04'
name: Archbee
nav: Providers
network: true
overview: 'Archbee publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Access Control API, API Reference API, Documents API, and 8 more. Tagged areas include API Documentation, Documentation Platform, Knowledge Base, Technical Writing, and Developer Docs.


  The Archbee catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Archbee''s developer surface includes authentication, developer portal, documentation, engineering blog, signup flow, pricing, support, and 40 more developer resources.'
plans:
- name: Archbee Plans Pricing
  plan_count: 3
  slug: archbee-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 1
  name: Archbee Rate Limits
  slug: archbee-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Archbee API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: archbee-jsonschema-spectral-rules
- effective_rule_count: 66
  extends:
  - spectral:oas
  name: Archbee API Rules
  rule_count: 25
  severity_counts:
    error: 12
    hint: 0
    info: 2
    warn: 11
  slug: archbee-spectral-rules
scopes:
- name: Archbee Scopes
  scope_count: 0
  slug: archbee-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: exemplar
  composite: 70.9
  coverage:
    artifact_dirs: 35
    catalog_earned: 83.0
    catalog_earned_first_party: 20.0
    catalog_gap: 32.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 93.4
    contract_governance: 45.5
    contract_quality: 52.2
    developer_ergonomics: 77.5
    discoverability: 80.0
    operational_transparency: 50.0
  previous_composite: 70.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 6
      marker_coverage: 42.9
      total: 14
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 45.1
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/archbee/refs/heads/main/screenshots/archbee-2026-06-20T172408.png
security:
- kind: authentication
  name: Archbee Authentication
  slug: archbee-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Archbee Domain Security
  slug: archbee-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Archbee Vulnerability Disclosure
  slug: archbee-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Archbee Trust Center
  slug: archbee-trust-center
  summary_line: SOC 2, GDPR
slug: archbee
tags:
- API Documentation
- Documentation Platform
- Knowledge Base
- Technical Writing
- Developer Docs
- Developer Portal
- Docs as Code
- OpenAPI
- MCP
- AI Agents
- Content Management
- Developer Tools
use_cases:
- description: Create comprehensive API reference docs with code samples, SDKs, and interactive API explorers.
  name: API Documentation
- description: Build a unified developer portal for all your APIs, SDKs, and developer resources.
  name: Developer Portal
- description: Create an internal knowledge base for engineering teams with runbooks, architecture docs, and processes.
  name: Internal Wiki
- description: Publish customer-facing help documentation and user guides with powerful search.
  name: Customer Documentation
- description: Create and maintain product documentation for software products with versioning.
  name: Product Documentation
website: https://www.archbee.com/
---
