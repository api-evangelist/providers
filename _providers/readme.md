---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.0
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 25
  human_in_the_loop: 0
  name: Readme Agentic Access
  operation_count: 44
  slug: readme-agentic-access
  summary_line: 44 operations · 25 acting
api_count: 14
apis:
- description: ReadMe operates a hosted Model Context Protocol (MCP) server that lets AI tools (Claude, Cursor, IDEs, CI pipelines) search, read, and update ReadMe documentation through natural language. ReadMe also
  name: ReadMe MCP Server
  slug: mcp-server
- description: ReadMe's Personalized Docs Webhook is the outbound, customer-hosted webhook the developer hub calls at user sign-in to look up a reader's account data. ReadMe POSTs a JSON body containing the user's e
  name: ReadMe Personalized Docs Webhook
  slug: personalized-docs-webhook
- description: Page view, quality, and search analytics
  name: ReadMe Analytics API
  slug: readme-analytics-api
- description: Manage ReadMe API keys
  name: ReadMe API Keys API
  slug: readme-api-keys-api
- description: Manage API definitions and reference pages
  name: ReadMe APIs API
  slug: readme-apis-api
- description: Manage versions and branches
  name: ReadMe Branches API
  slug: readme-branches-api
- description: Manage sidebar groupings
  name: ReadMe Categories API
  slug: readme-categories-api
- description: Manage changelog posts
  name: ReadMe Changelog API
  slug: readme-changelog-api
- description: Manage custom documentation pages
  name: ReadMe Custom Pages API
  slug: readme-custom-pages-api
- description: Manage knowledge base guide pages
  name: ReadMe Guides API
  slug: readme-guides-api
- description: Upload and manage images
  name: ReadMe Images API
  slug: readme-images-api
- description: Send API request metrics from server-side SDKs
  name: ReadMe Metrics API
  slug: readme-metrics-api
- description: Manage interactive recipe content
  name: ReadMe Recipes API
  slug: readme-recipes-api
- description: Search knowledge base content
  name: ReadMe Search API
  slug: readme-search-api
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
artifact_total: 51
asyncapis:
- description: AsyncAPI 2.6 description of ReadMe's Personalized Docs Webhook surface. The Personalized Docs Webhook is the integration that lets ReadMe inject a logged-in end user's account data into a project's ho
  name: ReadMe Personalized Docs Webhook
  slug: readme-personalized-docs-webhook-asyncapi
collections:
- collection_type: open
  name: ReadMe Developer Metrics API
  slug: open-readme-developer-metrics
- collection_type: open
  name: ReadMe API
  slug: open-readme
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/readme-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/readme-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/readme-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/readme/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/readme-create-branch-with-guide-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/readme-create-category-with-guide-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/readme-publish-changelog-post-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/readme-publish-custom-page-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/readme-publish-recipe-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/readme-release-version-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/readme-submit-metrics-and-audit-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/readme-upload-api-definition-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/readme-upsert-category-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/readme-upsert-changelog-post-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/readme-upsert-custom-page-workflow.yml
- group: design
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
  title: ''
  type: Plans
  url: plans/readme-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/readme-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/readme-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/readme-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/readme-context.jsonld
- group: design
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
- name: Readme Finops
  service_category: API
  slug: readme-finops
graphqls:
- description: ''
  name: ReadMe GraphQL API
  slug: readme-graphql
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
modified: '2026-05-30'
name: ReadMe
nav: Providers
network: true
overview: 'ReadMe publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Personalized Docs Webhook, Analytics API, API Keys API, and 10 more. Tagged areas include Documentation, Developer Hub, API Reference, Portals, and Analytics.


  The ReadMe catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  ReadMe''s developer surface includes authentication, developer portal, getting-started guide, documentation, API reference, pricing, signup flow, and 38 more developer resources.'
plans:
- name: Readme Plans Pricing
  plan_count: 3
  slug: readme-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 2
  name: Readme Rate Limits
  slug: readme-rate-limits
rules:
- name: ReadMe API Rules
  rule_count: 3
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 1
  slug: readme-asyncapi-spectral-rules
- name: ReadMe API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: readme-jsonschema-spectral-rules
- name: ReadMe API Rules
  rule_count: 9
  severity_counts:
    error: 5
    hint: 0
    info: 0
    warn: 4
  slug: readme-rules
score:
  band: strong
  composite: 58.7
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 65.3
    developer_ergonomics: 65.2
    discoverability: 72.2
    governance: 37.5
    operational_transparency: 42.1
  previous_composite: 58.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/readme/refs/heads/main/screenshots/readme-2026-06-20T192737.png
security:
- kind: authentication
  name: Readme Authentication
  slug: readme-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Readme Domain Security
  slug: readme-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: readme
tags:
- Documentation
- Developer Hub
- API Reference
- Portals
- Analytics
- AI
- MCP
- Bi-Directional Sync
website: https://readme.com
---
