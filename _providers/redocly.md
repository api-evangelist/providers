---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: derived
    idempotency: false
    mcp_server: platform
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 36.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Redocly Agentic Access
  operation_count: 15
  slug: redocly-agentic-access
  summary_line: 15 operations · 8 acting
api_count: 4
apis:
- description: Redocly Realm is the comprehensive API lifecycle management platform that unifies Redoc, Revel, and Reef into a single integrated product. Realm includes API documentation, mock servers, linting, cata
  name: Redocly Realm
  slug: redocly-realm
- description: Redocly Reunite is the Git-connected collaboration and deployment surface for Realm. It prepares, deploys, and hosts documentation projects and mock servers and ships a content editor, pull requests a
  name: Redocly Reunite
  slug: redocly-reunite
- description: Redocly Revel is the external developer hub product. It renders Markdown, Markdoc, and React pages with multi-product and localization capabilities, enabling organizations to create polished developer
  name: Redocly Revel
  slug: redocly-revel
- description: 'Redocly Reef is the internal API platform — a service catalog and governance product that organizes, aids discovery, and monitors APIs throughout their lifecycle. Reef includes Catalog for organizing '
  name: Redocly Reef
  slug: redocly-reef
- description: 'Redoc is the open-source engine that renders API reference documentation from OpenAPI definitions with a three-panel layout known for clarity and usability. Supports OpenAPI 3.2, 3.1, 3.0 and OpenAPI '
  name: Redocly Redoc
  slug: redocly-redoc
- description: Redocly CLI is an open-source command-line tool for working with OpenAPI descriptions, developer portals, and other API lifecycle operations. Supports linting, validation, bundling, splitting, and dec
  name: Redocly CLI
  slug: redocly-cli
- description: Respect Monitoring is Redocly's continuous, API-aware monitoring product powered by OpenAPI Arazzo workflows. Rather than uptime checking, it validates that API responses conform to specifications — e
  name: Redocly Respect Monitoring
  slug: redocly-respect
- description: Arazzo is the OpenAPI Initiative's specification for describing multi-step API workflows; Redocly is a primary tooling vendor with first-class Arazzo support across Redocly CLI (lint, validate, genera
  name: Arazzo Specification (Redocly Tooling)
  slug: redocly-arazzo
- baseURL_template: '{host}'
  baseurl_source: spec_template
  description: Operations related to health checks.
  name: Redocly Health API
  phrasing_intents:
  - id: health
    intent: Check the Scout worker's health
    question: Is the Redocly Scout worker up and healthy?
  phrasing_ops: 1
  slug: redocly-health-api
- baseURL_template: https://{host}/api
  baseurl_source: spec_template
  description: Operations related to metadata.
  name: Redocly Metadata API
  phrasing_intents:
  - id: validateMetadata
    intent: Validate API metadata against the project schema
    question: Does my API metadata conform to the metadataSchema in my Redocly project config?
  phrasing_ops: 1
  slug: redocly-metadata-api
- baseURL_template: https://{host}/api
  baseurl_source: spec_template
  description: Operations related to remotes.
  name: Redocly Remotes API
  phrasing_intents:
  - id: upsertRemote
    intent: Create or reuse a remote at a mount path
    question: How do I connect a Git repository or URL as a remote content source in a Redocly project?
  - id: pushToRemote
    intent: Push discovered files into a remote as a commit
    question: Can I upload a set of files to an existing remote with a commit message and author?
  phrasing_ops: 2
  slug: redocly-remotes-api
- baseURL_template: https://{projectUrl}
  baseurl_source: spec_template
  description: Full-text search and facet operations.
  name: Redocly Search API
  phrasing_intents:
  - id: search
    intent: Full-text search a project's docs and API reference
    question: Can I search my Redocly documentation and API reference from a script or MCP server?
  - id: searchFacets
    intent: Get search facets and counts for filter UIs
    question: What facets and value counts can I use to build a filter sidebar for docs search?
  phrasing_ops: 2
  slug: redocly-search-api
- baseURL_template: https://{host}/api
  baseurl_source: spec_template
  description: Operations related to status.
  name: Redocly Status API
  phrasing_intents:
  - id: reportStatus
    intent: Report a Scout instance's status and disk usage
    question: What does a Scout instance send when it reports its status back to Redocly?
  phrasing_ops: 1
  slug: redocly-status-api
- baseURL_template: https://{host}/api
  baseurl_source: spec_template
  description: Operations related to tasks.
  name: Redocly Tasks API
  phrasing_intents:
  - id: startNextJob
    intent: Claim and start the next available Scout job
    question: Can a Scout worker pull the next available job off the queue and start processing it?
  - id: getAllTasks
    intent: List Scout tasks for a project
    question: Which Scout tasks exist for my Redocly project right now?
  - id: getJobById
    intent: Get one Scout task by its job ID
    question: Where can I look up the details of a single Scout task using its job ID?
  - id: updateJob
    intent: Mark a processing Scout job completed or failed
    question: How do I report that a Scout job finished, either completed or failed?
  phrasing_ops: 4
  slug: redocly-tasks-api
- baseURL_template: '{host}'
  baseurl_source: spec_template
  description: Operations related to incoming git webhooks.
  name: Redocly Webhooks API
  phrasing_intents:
  - id: processGithubWebhook
    intent: Receive a GitHub repository event for Scout
    question: Which GitHub events does Scout process, just pushes and new pull requests?
  - id: processGitlabWebhook
    intent: Receive a GitLab repository event for Scout
    question: Does Scout handle GitLab merge request and push events?
  phrasing_ops: 2
  slug: redocly-webhooks-api
- baseURL_template: https://{host}/api
  baseurl_source: spec_template
  description: Operations related to todos.
  name: Redocly To Dos API
  phrasing_intents:
  - id: createTodo
    intent: Queue a job todo for Scout on a commit
    question: How do I queue a job for Scout to process a specific repository commit?
  - id: getAllTodos
    intent: List Scout job todos for a project
    question: What job todos are waiting for Scout in my project?
  phrasing_ops: 2
  slug: redocly-to-dos-api
artifact_total: 60
asyncapis:
- description: ''
  name: Redocly Webhooks
  slug: redocly-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/redocly/agentic-access/redocly-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/redocly-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/redocly/rules/redocly-rules.yml
  title: ''
  type: Spectral
  url: rules/redocly-rules.yml
- group: design
  href: https://artifacts.apis.io/redocly/rules/redocly-jsonschema-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/redocly-jsonschema-spectral-rules.yml
- group: operate
  href: https://artifacts.apis.io/redocly/lifecycle/redocly-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/redocly-lifecycle.yml
- group: other
  href: https://artifacts.apis.io/redocly/hosts/redocly-hosts.yml
  title: ''
  type: Hosts
  url: hosts/redocly-hosts.yml
- group: other
  href: https://artifacts.apis.io/redocly/vendors/redocly-vendors.yml
  title: ''
  type: Vendors
  url: vendors/redocly-vendors.yml
- group: build
  title: ''
  type: SDKs
  url: https://redocly.com/blog/category/api-lifecycle/sdks
- group: other
  href: https://artifacts.apis.io/redocly/vendor-facets/redocly-vendor-facets.yml
  title: ''
  type: VendorFacets
  url: vendor-facets/redocly-vendor-facets.yml
- group: company
  title: ''
  type: Website
  url: https://redocly.com
- group: other
  href: https://artifacts.apis.io/redocly/overlays/redocly-search-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/redocly-search-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/redocly/overlays/redocly-docs-mcp-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/redocly-docs-mcp-overlay.yaml
- group: other
  href: https://artifacts.apis.io/redocly/overlays/redocly-scout-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/redocly-scout-overlay.yaml
- group: other
  href: https://artifacts.apis.io/redocly/overlays/redocly-scout-agent-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/redocly-scout-agent-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/redocly/scopes/redocly-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/redocly-scopes.yml
- group: auth
  href: https://artifacts.apis.io/redocly/authentication/redocly-authentication.yml
  title: ''
  type: Authentication
  url: authentication/redocly-authentication.yml
- group: auth
  href: https://artifacts.apis.io/redocly/security/redocly-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/redocly-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://redocly.com/docs
- group: start
  title: ''
  type: Portal
  url: https://redocly.com/docs
- group: other
  title: ''
  type: Customers
  url: https://redocly.com/customers
- group: commercial
  title: ''
  type: Pricing
  url: https://redocly.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://redocly.com/blog
- group: learn
  title: ''
  type: Webinars
  url: https://redocly.com/webinars
- group: auth
  title: ''
  type: Security
  url: https://redocly.com/security
- group: operate
  title: ''
  type: StatusPage
  url: https://status.redocly.com/
- group: commercial
  title: ''
  type: ServiceLevelAgreement
  url: https://redocly.com/sla
- group: build
  title: ''
  type: CLI
  url: https://redocly.com/redocly-cli
- group: company
  title: ''
  type: About
  url: https://redocly.com/about
- group: operate
  title: ''
  type: Support
  url: https://redocly.com/contact-us
- group: other
  title: ''
  type: Products
  url: https://redocly.com/products
- group: start
  title: ''
  type: Login
  url: https://auth.cloud.redocly.com/login
- group: start
  title: ''
  type: Signup
  url: https://redocly.com/billing/signup
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://redocly.com/privacy-notice
- group: commercial
  title: ''
  type: TermsOfService
  url: https://redocly.com/subscription-agreement
- group: company
  title: ''
  type: Careers
  url: https://redocly.com/careers
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/Redocly
- group: other
  title: ''
  type: X
  url: https://twitter.com/Redocly
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/redocly
- group: other
  title: ''
  type: Governance
  url: https://redocly.com/api-governance
- group: operate
  title: ''
  type: ChangeLog
  url: https://redocly.com/docs/realm/changelog
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: https://redocly.com/vulnerability-disclosure-policy
- group: other
  title: ''
  type: DataProcessingAddendum
  url: https://redocly.com/dpa
- group: docs
  title: ''
  type: Reference
  url: https://redocly.com/reference
- group: commercial
  href: https://artifacts.apis.io/redocly/plans/redocly-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/redocly-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/redocly/rate-limits/redocly-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/redocly-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/redocly/finops/redocly-finops.yml
  title: ''
  type: FinOps
  url: finops/redocly-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://redocly.com/llms.txt
- group: build
  href: https://artifacts.apis.io/redocly/packages/redocly-packages.yml
  title: ''
  type: Packages
  url: packages/redocly-packages.yml
- group: agent
  href: https://artifacts.apis.io/redocly/well-known/redocly-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/redocly-well-known.yml
- group: agent
  href: https://artifacts.apis.io/redocly/mcp/redocly-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/redocly-mcp.yml
- group: build
  href: https://artifacts.apis.io/redocly/mcp/redocly-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/redocly-tool-crosswalk.yml
- group: other
  href: https://artifacts.apis.io/redocly/a2a/redocly-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/redocly-a2a.yml
- group: agent
  href: https://artifacts.apis.io/redocly/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/redocly/llms/redocly-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/redocly-llms.txt
- group: design
  href: https://artifacts.apis.io/redocly/conformance/redocly-conformance.yml
  title: ''
  type: Conformance
  url: conformance/redocly-conformance.yml
- group: auth
  href: https://artifacts.apis.io/redocly/security/redocly-trust-center.yml
  title: ''
  type: Compliance
  url: security/redocly-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/redocly/security/redocly-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/redocly-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/redocly/security/redocly-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/redocly-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/redocly/errors/redocly-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/redocly-problem-types.yml
- group: design
  href: https://artifacts.apis.io/redocly/lifecycle/redocly-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/redocly-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/redocly/conventions/redocly-conventions.yml
  title: ''
  type: Conventions
  url: conventions/redocly-conventions.yml
- group: operate
  href: https://artifacts.apis.io/redocly/changelog/redocly-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/redocly-changelog.yml
- group: build
  href: https://artifacts.apis.io/redocly/cli/redocly-cli.yml
  title: ''
  type: CLI
  url: cli/redocly-cli.yml
- group: design
  href: https://artifacts.apis.io/redocly/components/redocly-components.yml
  title: ''
  type: Components
  url: components/redocly-components.yml
- group: design
  href: https://artifacts.apis.io/redocly/data-model/redocly-data-model.yml
  title: ''
  type: DataModel
  url: data-model/redocly-data-model.yml
- group: design
  href: https://artifacts.apis.io/redocly/asyncapi/redocly-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/redocly-webhooks.yml
- group: operate
  title: ''
  type: Roadmap
  url: https://redocly.com/roadmap
- group: start
  title: ''
  type: GettingStarted
  url: https://redocly.com/docs/realm/get-started
- group: start
  title: ''
  type: Quickstart
  url: https://redocly.com/docs/cli/quickstart
- group: learn
  title: ''
  type: Learn
  url: https://redocly.com/learn
- group: other
  title: ''
  type: SubProcessors
  url: https://redocly.com/sub-processors
- group: operate
  title: ''
  type: Contact
  url: mailto:team@redocly.com
created: '2026-01-05'
description: Redocly is a company that specializes in API documentation and governance tooling. Their platform helps organizations create, manage, and publish API documentation through Realm (the integrated lifecycle platform that unifies Redoc, Revel, and Reef), Reunite (Git-connected collaboration and deployment for docs/APIs), Revel (developer portal), Reef (internal API catalog and scorecard), and Redoc (open-source OpenAPI renderer). The Redocly CLI provides linting, bundling, splitting, decoration, and documentation generation for OpenAPI, AsyncAPI, and Arazzo specifications. Respect Monitoring adds continuous, Arazzo-powered API monitoring, and the Enterprise tier exposes MCP Servers and AI search for Realm portals — positioning Redocly's catalog as an AI substrate for agentic software.
examples:
- key_count: 2
  name: Redocly Cli Commands Example
  slug: redocly-cli-commands-example
- key_count: 3
  name: Redocly Config Example
  slug: redocly-config-example
- key_count: 3
  name: Redocly Lint Result Example
  slug: redocly-lint-result-example
finops:
- has_sources: true
  method: derived
  name: Redocly Finops
  primary_unit: subscription
  service_category: ''
  slug: redocly-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/redocly.png
json_schemas:
- name: Redocly Configuration
  property_count: 7
  slug: redocly-config
- name: CreateRemote
  property_count: 15
  slug: redocly-create-remote
- name: Health
  property_count: 1
  slug: redocly-health
- name: JobList
  property_count: 3
  slug: redocly-job-list
- name: Job
  property_count: 20
  slug: redocly-job
- name: Redocly Lint Result
  property_count: 3
  slug: redocly-lint-result
- name: Merge request reopen event
  property_count: 7
  slug: redocly-merge-request-reopen
- name: Merge request update event
  property_count: 7
  slug: redocly-merge-request-update
- name: Metadata
  property_count: 0
  slug: redocly-metadata
- name: MetadataValidationResult
  property_count: 2
  slug: redocly-metadata-validation-result
- name: PatchJob
  property_count: 2
  slug: redocly-patch-job
- name: pull_request opened event
  property_count: 7
  slug: redocly-pull-request-opened
- name: pull_request reopened event
  property_count: 7
  slug: redocly-pull-request-reopened
- name: PullRequest
  property_count: 18
  slug: redocly-pull-request
- name: Push event
  property_count: 15
  slug: redocly-push-2
- name: push event
  property_count: 15
  slug: redocly-push
- name: RemotePush
  property_count: 4
  slug: redocly-remote-push
- name: Remote
  property_count: 16
  slug: redocly-remote
- name: SearchFacetsRequest
  property_count: 5
  slug: redocly-search-facets-request
- name: SearchFacetsResponse
  property_count: 0
  slug: redocly-search-facets-response
- name: SearchRequest
  property_count: 4
  slug: redocly-search-request
- name: SearchResponse
  property_count: 2
  slug: redocly-search-response
- name: Status
  property_count: 5
  slug: redocly-status
json_structures:
- name: Redocly Config Structure
  property_count: 0
  slug: redocly-config-structure
- name: Redocly Lint Result Structure
  property_count: 0
  slug: redocly-lint-result-structure
jsonld:
- class_count: 0
  name: Redocly Context
  property_count: 4
  slug: redocly-context
layout: provider
mcp_servers:
- description: 'Redocly ships a Docs MCP server as a Realm feature and runs it on its own documentation site. The endpoint answers anonymously: tools/list returns two real tools and resources/list returns the publish'
  name: Redocly Docs MCP server
  slug: redocly-docs-mcp-server
modified: '2026-09-16'
name: Redocly
nav: Providers
network: true
overview: 'Redocly publishes 16 API contracts indexed on the [APIs.io](https://apis.io/) network, including Health API, Metadata API, Remotes API, and 13 more. Tagged areas include Artificial Intelligence, API Catalog, API Documentation, Arazzo, and Developer Portal.


  The Redocly catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Redocly''s developer surface includes authentication, documentation, developer portal, pricing, engineering blog, CLI, support, and 64 more developer resources.'
plans:
- name: Redocly Plans Pricing
  plan_count: 3
  slug: redocly-plans-pricing
- name: Redocly Price Estimates
  plan_count: 0
  slug: redocly-price-estimates
random_paper: 10
rate_limits:
- limit_count: 9
  name: Redocly Rate Limits
  slug: redocly-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Redocly — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: redocly-jsonschema-spectral-rules
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: Redocly API Rules
  rule_count: 16
  severity_counts:
    error: 11
    hint: 0
    info: 3
    warn: 2
  slug: redocly-rules
scopes:
- name: Redocly Scopes
  scope_count: 0
  slug: redocly-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: exemplar
  composite: 82.7
  coverage:
    artifact_dirs: 39
    catalog_earned: 85.0
    catalog_earned_first_party: 24.0
    catalog_gap: 30.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 100.0
    contract_governance: 45.5
    contract_quality: 63.3
    developer_ergonomics: 78.6
    discoverability: 71.7
    operational_transparency: 100.0
  previous_composite: 82.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 41.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 22.2
screenshot: https://apis.io/screenshots/redocly/redocly-2026-06-20T192731.png
security:
- kind: authentication
  name: Redocly Authentication
  slug: redocly-authentication
  summary_line: apiKey/http/oauth2 · 5 schemes
- kind: domain-security
  name: Redocly Domain Security
  slug: redocly-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Redocly Vulnerability Disclosure
  slug: redocly-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Redocly Trust Center
  slug: redocly-trust-center
  summary_line: SOC 2 Type II, CSA STAR / CAIQ v4, PCI DSS, GDPR / CCPA
skill_count: 1
skills:
- name: redocly-cli
  slug: redocly-cli
slug: redocly
tags:
- Artificial Intelligence
- API Catalog
- API Documentation
- Arazzo
- Developer Portal
- Governance
- Linting
- MCP
- Monitoring
- OpenAPI
- A2A
website: https://redocly.com
---
