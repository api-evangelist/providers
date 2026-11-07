---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: platform
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: derived
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: full
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 34.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 25
  human_in_the_loop: 0
  name: Readme Agentic Access
  operation_count: 44
  slug: readme-agentic-access
  summary_line: 44 operations · 25 acting
api_count: 2
apis:
- description: ReadMe operates a hosted Model Context Protocol (MCP) server that lets AI tools (Claude, Cursor, IDEs, CI pipelines) search, read, and update ReadMe documentation through natural language. ReadMe also
  name: ReadMe MCP Server
  slug: mcp-server
- description: ReadMe's Personalized Docs Webhook is the outbound, customer-hosted webhook the developer hub calls at user sign-in to look up a reader's account data. ReadMe POSTs a JSON body containing the user's e
  name: ReadMe Personalized Docs Webhook
  slug: personalized-docs-webhook
- baseURL: https://api.readme.com/v2
  baseurl_source: declared
  description: Page view, quality, and search analytics
  name: ReadMe Analytics API
  slug: readme-analytics-api
- baseURL: https://api.readme.com/v2
  baseurl_source: declared
  description: Manage ReadMe API keys
  name: ReadMe API Keys API
  slug: readme-api-keys-api
- baseURL: https://api.readme.com/v2
  baseurl_source: declared
  description: Manage versions and branches
  name: ReadMe Branches API
  slug: readme-branches-api
- baseURL: https://api.readme.com/v2
  baseurl_source: declared
  description: Manage sidebar groupings
  name: ReadMe Categories API
  slug: readme-categories-api
- baseURL: https://api.readme.com/v2
  baseurl_source: declared
  description: Manage changelog posts
  name: ReadMe Changelog API
  slug: readme-changelog-api
- baseURL: https://api.readme.com/v2
  baseurl_source: declared
  description: Manage custom documentation pages
  name: ReadMe Custom Pages API
  slug: readme-custom-pages-api
- baseURL: https://api.readme.com/v2
  baseurl_source: declared
  description: Manage knowledge base guide pages
  name: ReadMe Guides API
  slug: readme-guides-api
- baseURL: https://api.readme.com/v2
  baseurl_source: declared
  description: Upload and manage images
  name: ReadMe Images API
  slug: readme-images-api
- baseURL: https://api.readme.com/v2
  baseurl_source: declared
  description: Send API request metrics from server-side SDKs
  name: ReadMe Metrics API
  slug: readme-metrics-api
- baseURL: https://api.readme.com/v2
  baseurl_source: declared
  description: Manage interactive recipe content
  name: ReadMe Recipes API
  slug: readme-recipes-api
- baseURL: https://api.readme.com/v2
  baseurl_source: declared
  description: Search knowledge base content
  name: ReadMe Search API
  slug: readme-search-api
- baseURL: https://api.readme.com/v2
  baseurl_source: declared
  description: Manage API definitions and reference pages
  name: ReadMe APIs API
  slug: readme-apis-api
arazzos:
- description: Create a branch (version), add a category, and seed it with a first guide.
  name: ReadMe Stand Up A New Version With Starter Docs
  slug: readme-create-branch-with-guide-workflow
- description: Create a sidebar category and immediately add a guide page to it.
  name: ReadMe Create A Category With A Guide
  slug: readme-create-category-with-guide-workflow
- description: Create a changelog post on a branch and read it back by slug.
  name: ReadMe Publish A Changelog Post
  slug: readme-publish-changelog-post-workflow
- description: Create a custom page on a branch and read it back by slug.
  name: ReadMe Publish A Custom Page
  slug: readme-publish-custom-page-workflow
- description: Create an interactive recipe and read it back by slug.
  name: ReadMe Publish A Recipe
  slug: readme-publish-recipe-workflow
- description: Create a branch, upload its API definition, and post a launch changelog.
  name: ReadMe Cut A Version And Announce It
  slug: readme-release-version-workflow
- description: Send API request logs to Metrics, then retrieve page quality scores.
  name: ReadMe Submit Metrics And Audit Quality
  slug: readme-submit-metrics-and-audit-workflow
- description: Upload an OpenAPI definition to a branch and read the created definition back.
  name: ReadMe Upload An API Definition And Verify
  slug: readme-upload-api-definition-workflow
- description: Find a category by slug and update it if it exists, otherwise create it.
  name: ReadMe Upsert A Category
  slug: readme-upsert-category-workflow
- description: Find a changelog post by slug and update it if it exists, otherwise create it.
  name: ReadMe Upsert A Changelog Post
  slug: readme-upsert-changelog-post-workflow
- description: Find a custom page by slug and update it if it exists, otherwise create it.
  name: ReadMe Upsert A Custom Page
  slug: readme-upsert-custom-page-workflow
- description: Find a guide by slug and update it if it exists, otherwise create it.
  name: ReadMe Upsert A Guide Page
  slug: readme-upsert-guide-workflow
artifact_total: 68
asyncapis:
- description: AsyncAPI 2.6 description of ReadMe's Personalized Docs Webhook surface. The Personalized Docs Webhook is the integration that lets ReadMe inject a logged-in end user's account data into a project's ho
  name: ReadMe Personalized Docs Webhook
  slug: readme-personalized-docs-webhook-asyncapi
collections:
- collection_type: open
  name: ReadMe Developer Metrics Analytics API
  slug: open-readme-analytics-api
- collection_type: open
  name: ReadMe Developer Metrics Analytics API Keys API
  slug: open-readme-api-keys-api
- collection_type: open
  name: ReadMe Developer Metrics Analytics APIs API
  slug: open-readme-apis-api
- collection_type: open
  name: ReadMe Developer Metrics Analytics Branches API
  slug: open-readme-branches-api
- collection_type: open
  name: ReadMe Developer Metrics Analytics Categories API
  slug: open-readme-categories-api
- collection_type: open
  name: ReadMe Developer Metrics Analytics Changelog API
  slug: open-readme-changelog-api
- collection_type: open
  name: ReadMe Developer Metrics Analytics Custom Pages API
  slug: open-readme-custom-pages-api
- collection_type: open
  name: ReadMe Developer Metrics API
  slug: open-readme-developer-metrics
- collection_type: open
  name: ReadMe Developer Metrics Analytics Guides API
  slug: open-readme-guides-api
- collection_type: open
  name: ReadMe Developer Metrics Analytics Images API
  slug: open-readme-images-api
- collection_type: open
  name: ReadMe Developer Analytics Metrics API
  slug: open-readme-metrics-api
- collection_type: open
  name: ReadMe Developer Metrics Analytics Recipes API
  slug: open-readme-recipes-api
- collection_type: open
  name: ReadMe Developer Metrics Analytics Search API
  slug: open-readme-search-api
- collection_type: open
  name: ReadMe API
  slug: open-readme
common:
- group: agent
  href: https://artifacts.apis.io/readme/mcp/readme-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/readme-mcp.yml
- group: auth
  href: https://artifacts.apis.io/readme/well-known/readme-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/readme-security.txt
- group: build
  href: https://artifacts.apis.io/readme/integrations/readme-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/readme-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/readme/capabilities/readme-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/readme-capability-edges.yml
- group: design
  href: https://artifacts.apis.io/readme/rules/readme-rules.yml
  title: ''
  type: Spectral
  url: rules/readme-rules.yml
- group: design
  href: https://artifacts.apis.io/readme/rules/readme-jsonschema-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/readme-jsonschema-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/readme/rules/readme-asyncapi-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/readme-asyncapi-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/readme/json-ld/readme-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/readme-context.jsonld
- group: agent
  href: https://artifacts.apis.io/readme/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/readme/asyncapi/readme-personalized-docs-webhook-asyncapi.yml
  title: ''
  type: Webhooks
  url: asyncapi/readme-personalized-docs-webhook-asyncapi.yml
- group: docs
  href: https://artifacts.apis.io/readme/asyncapi/readme-personalized-docs-webhook-asyncapi.yml
  title: ''
  type: AsyncAPI
  url: asyncapi/readme-personalized-docs-webhook-asyncapi.yml
- group: design
  href: https://artifacts.apis.io/readme/data-model/readme-data-model.yml
  title: ''
  type: DataModel
  url: data-model/readme-data-model.yml
- group: build
  href: https://artifacts.apis.io/readme/cli/readme-cli.yml
  title: ''
  type: CLI
  url: cli/readme-cli.yml
- group: design
  href: https://artifacts.apis.io/readme/conventions/readme-conventions.yml
  title: ''
  type: Conventions
  url: conventions/readme-conventions.yml
- group: design
  href: https://artifacts.apis.io/readme/errors/readme-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/readme-problem-types.yml
- group: design
  href: https://artifacts.apis.io/readme/conformance/readme-conformance.yml
  title: ''
  type: Conformance
  url: conformance/readme-conformance.yml
- group: agent
  href: https://artifacts.apis.io/readme/llms/readme-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/readme-llms.txt
- group: agent
  href: https://artifacts.apis.io/readme/well-known/readme-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/readme-well-known.yml
- group: other
  href: https://artifacts.apis.io/readme/hosts/readme-hosts.yml
  title: ''
  type: Hosts
  url: hosts/readme-hosts.yml
- group: other
  href: https://artifacts.apis.io/readme/vendors/readme-vendors.yml
  title: ''
  type: Vendors
  url: vendors/readme-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.readme.com/
- group: operate
  title: ''
  type: Support
  url: https://readme.com/help-center
- group: other
  href: https://artifacts.apis.io/readme/vendor-facets/readme-vendor-facets.yml
  title: ''
  type: VendorFacets
  url: vendor-facets/readme-vendor-facets.yml
- group: company
  title: ''
  type: Website
  url: https://www.readme.com/
- group: agent
  href: https://artifacts.apis.io/readme/agentic-access/readme-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/readme-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/readme/security/readme-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/readme-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/readme/authentication/readme-authentication.yml
  title: ''
  type: Authentication
  url: authentication/readme-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/readme/overview
- group: design
  href: https://artifacts.apis.io/readme/arazzo/readme-create-branch-with-guide-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/readme-create-branch-with-guide-workflow.yml
- group: design
  href: https://artifacts.apis.io/readme/arazzo/readme-create-category-with-guide-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/readme-create-category-with-guide-workflow.yml
- group: design
  href: https://artifacts.apis.io/readme/arazzo/readme-publish-changelog-post-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/readme-publish-changelog-post-workflow.yml
- group: design
  href: https://artifacts.apis.io/readme/arazzo/readme-publish-custom-page-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/readme-publish-custom-page-workflow.yml
- group: design
  href: https://artifacts.apis.io/readme/arazzo/readme-publish-recipe-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/readme-publish-recipe-workflow.yml
- group: design
  href: https://artifacts.apis.io/readme/arazzo/readme-release-version-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/readme-release-version-workflow.yml
- group: design
  href: https://artifacts.apis.io/readme/arazzo/readme-submit-metrics-and-audit-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/readme-submit-metrics-and-audit-workflow.yml
- group: design
  href: https://artifacts.apis.io/readme/arazzo/readme-upload-api-definition-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/readme-upload-api-definition-workflow.yml
- group: design
  href: https://artifacts.apis.io/readme/arazzo/readme-upsert-category-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/readme-upsert-category-workflow.yml
- group: design
  href: https://artifacts.apis.io/readme/arazzo/readme-upsert-changelog-post-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/readme-upsert-changelog-post-workflow.yml
- group: design
  href: https://artifacts.apis.io/readme/arazzo/readme-upsert-custom-page-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/readme-upsert-custom-page-workflow.yml
- group: design
  href: https://artifacts.apis.io/readme/arazzo/readme-upsert-guide-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/readme-upsert-guide-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://readme.com
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.readme.com/main/docs/quickstart
- group: docs
  title: ''
  type: Documentation
  url: https://docs.readme.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.readme.com/main/reference/intro-to-the-readme-api
- group: commercial
  title: ''
  type: Pricing
  url: https://readme.com/pricing
- group: start
  title: ''
  type: Signup
  url: https://dash.readme.com/signup
- group: start
  title: ''
  type: Login
  url: https://dash.readme.com/login
- group: company
  title: ''
  type: Blog
  url: https://readme.com/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.readme.com/main/changelog
- group: company
  title: ''
  type: About
  url: https://readme.com/about
- group: operate
  title: ''
  type: StatusPage
  url: https://www.readmestatus.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://readme.com/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://readme.com/privacy
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/readmeio
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/readme
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.readme.com/llms.txt
- group: build
  title: ''
  type: CLI
  url: https://github.com/readmeio/rdme
- group: build
  title: ''
  type: SDKs
  url: https://github.com/readmeio/metrics-sdks
- group: build
  title: ''
  type: Tools
  url: https://github.com/readmeio/oas
- group: build
  title: ''
  type: Tools
  url: https://github.com/readmeio/api
- group: build
  title: ''
  type: Tools
  url: https://github.com/readmeio/markdown
- group: build
  title: ''
  type: GitHubAction
  url: https://github.com/readmeio/rdme
- group: other
  title: ''
  type: Marketplace
  url: https://github.com/readmeio/marketplace
- group: commercial
  href: https://artifacts.apis.io/readme/plans/readme-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/readme-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/readme/rate-limits/readme-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/readme-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/readme/finops/readme-finops.yml
  title: ''
  type: FinOps
  url: finops/readme-finops.yml
- group: design
  href: https://artifacts.apis.io/readme/vocabulary/readme-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/readme-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/readme/json-ld/readme-context.jsonld
  title: ''
  type: JSONLDContext
  url: json-ld/readme-context.jsonld
- group: design
  href: https://artifacts.apis.io/readme/rules/readme-rules.yml
  title: ''
  type: SpectralRules
  url: rules/readme-rules.yml
created: '2025-01-08'
description: ReadMe is a developer hub platform that helps companies design, document, and operate their APIs. The platform combines hosted API reference (OpenAPI-driven), guides and changelog, bi-directional Git sync (GitHub and GitLab), interactive API explorer, Try-It console, Developer Dashboard with real-time API logs, and a deep layer of AI tooling — including the ReadMe Agent for multi-page editing, Inline AI rewrites, the AI Linter for style-guide enforcement, Docs Audit, GitHub AI Writer for PR-triggered doc updates, Ask AI for end users, and Model Context Protocol (MCP) servers for both ReadMe itself and each customer project so AI tools can search, read, update docs, and call APIs.
examples:
- key_count: 2
  name: Readme Create Changelog Example
  slug: readme-create-changelog-example
- key_count: 2
  name: Readme Create Guide Example
  slug: readme-create-guide-example
- key_count: 2
  name: Readme List Apis Example
  slug: readme-list-apis-example
- key_count: 2
  name: Readme Metrics Request Example
  slug: readme-metrics-request-example
- key_count: 2
  name: Readme Search Example
  slug: readme-search-example
finops:
- has_sources: true
  method: derived
  name: Readme Finops
  primary_unit: add-on
  service_category: ''
  slug: readme-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/readme.png
json_schemas:
- name: ReadMe API Definition
  property_count: 9
  slug: readme-api-definition
- name: ReadMe Branch
  property_count: 8
  slug: readme-branch
- name: ReadMe Changelog Post
  property_count: 8
  slug: readme-changelog
- name: ReadMe Guide
  property_count: 11
  slug: readme-guide
- name: ReadMe Metrics Request Log
  property_count: 6
  slug: readme-metrics-request
json_structures:
- name: Readme Developer Hub Structure
  property_count: 0
  slug: readme-developer-hub-structure
jsonld:
- class_count: 35
  name: Readme Context
  property_count: 0
  slug: readme-context
layout: provider
mcp_servers:
- description: Remote MCP server at docs.readme.com over HTTP; 11 tools listed.
  name: ReadMe MCP Server
  slug: readme
modified: '2026-05-30'
name: ReadMe
nav: Providers
network: true
overview: 'ReadMe publishes 14 API contracts indexed on the [APIs.io](https://apis.io/) network, including Personalized Docs Webhook, Analytics API, API Keys API, and 11 more. Tagged areas include Documentation, Developer Hub, API Reference, Portal, and Analytics.


  The ReadMe catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  ReadMe''s developer surface includes CLI, support, authentication, developer portal, getting-started guide, documentation, API reference, and 62 more developer resources.'
plans:
- name: Readme Plans Pricing
  plan_count: 5
  slug: readme-plans-pricing
- name: Readme Price Estimates
  plan_count: 0
  slug: readme-price-estimates
random_paper: 22
rate_limits:
- limit_count: 2
  name: Readme Rate Limits
  slug: readme-rate-limits
rules:
- authorship: generated
  effective_rule_count: 30
  extends:
  - spectral:asyncapi
  name: ReadMe — asyncapi rules
  rule_count: 3
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 1
  slug: readme-asyncapi-spectral-rules
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: ReadMe — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: readme-jsonschema-spectral-rules
- authorship: unmarked
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: ReadMe API Rules
  rule_count: 9
  severity_counts:
    error: 5
    hint: 0
    info: 0
    warn: 4
  slug: readme-rules
score:
  band: strong
  composite: 65.7
  coverage:
    artifact_dirs: 38
    catalog_earned: 71.4
    catalog_earned_first_party: 12.0
    catalog_gap: 43.6
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 2.5
  facets:
    access_clarity: 81.6
    contract_governance: 31.8
    contract_quality: 63.5
    developer_ergonomics: 72.0
    discoverability: 66.7
    operational_transparency: 60.5
  previous_composite: 63.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 25.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/readme/readme-2026-06-20T192737.png
security:
- kind: authentication
  name: Readme Authentication
  slug: readme-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Readme Domain Security
  slug: readme-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 4
skills:
- name: readme-branch-create-and-retrieve
  slug: readme-branch-create-and-retrieve
- name: readme-custom-pages-crud
  slug: readme-custom-pages-crud
- name: readme-guide-crud
  slug: readme-guide-crud
- name: readme-manage-recipe
  slug: readme-manage-recipe
slug: readme
tags:
- Documentation
- Developer Hub
- API Reference
- Portal
- Analytics
- Artificial Intelligence
- MCP
- Bi-Directional Sync
- API Documentation
- Developer Portal
- OpenAPI
website: https://www.readme.com/
---
