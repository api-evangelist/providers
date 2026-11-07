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
  - sandbox
  trial: false
  try_now: false
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
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 48.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 19
  human_in_the_loop: 1
  name: Pluralsight Agentic Access
  operation_count: 36
  slug: pluralsight-agentic-access
  summary_line: 36 operations · 19 acting · 1 human-in-the-loop
api_count: 30
apis:
- baseURL: https://paas-rest-api.pluralsight.com
  baseurl_source: declared
  description: Public course catalog operations
  name: Pluralsight Catalog API
  phrasing_intents:
  - id: getCourseCatalog
    intent: Browse the full public course catalog
    question: What courses are in the Pluralsight public catalog?
  phrasing_ops: 1
  slug: pluralsight-catalog-api
- baseURL: https://flow-api.pluralsight.com
  baseurl_source: declared
  description: Code-level engineering metrics operations
  name: Pluralsight Coding Metrics API
  phrasing_intents:
  - id: getCodingMetrics
    intent: Get code-level developer productivity metrics
    question: How productive were our developers at the code level last quarter?
  phrasing_ops: 1
  slug: pluralsight-coding-metrics-api
- baseURL: https://api.appfireflow.com
  baseurl_source: declared
  description: Pull request and collaboration metrics operations
  name: Pluralsight Collaboration Metrics API
  phrasing_intents:
  - id: getCollaborationMetrics
    intent: Get pull request collaboration metrics for teams
    question: How well are my engineering teams collaborating on code review?
  phrasing_ops: 1
  slug: pluralsight-collaboration-metrics-api
- baseURL: https://{workspace}.appfireflow.com/v3/customer/core
  baseurl_source: declared
  description: Commit data operations
  name: Pluralsight Commits API
  phrasing_intents:
  - id: getCommits
    intent: Get commit data across repositories
    question: How many commits landed across our repositories this sprint?
  phrasing_ops: 1
  slug: pluralsight-commits-api
- baseURL: https://flow-api.pluralsight.com
  baseurl_source: declared
  description: DORA engineering metrics operations
  name: Pluralsight DORA Metrics API
  phrasing_intents:
  - id: getDoraMetrics
    intent: Get DORA delivery performance metrics
    question: What is our deployment frequency and lead time for changes?
  phrasing_ops: 1
  slug: pluralsight-dora-metrics-api
- baseURL: https://{workspace}.appfireflow.com/v3/customer/core
  baseurl_source: declared
  description: Flow integration management operations
  name: Pluralsight Integrations API
  phrasing_intents:
  - id: listIntegrations
    intent: List Flow integrations and connection status
    question: Which external tools are connected to our Flow workspace?
  phrasing_ops: 1
  slug: pluralsight-integrations-api
- baseURL: https://app.pluralsight.com/plans/api/license/v1
  baseurl_source: declared
  description: License management operations (deprecated)
  name: Pluralsight Licensing API
  phrasing_intents:
  - id: listInvitations
    intent: List pending user invitations
    question: Who has been invited to our plan but hasn't accepted yet?
  - id: createInvitation
    intent: Send a user invitation to the plan
    question: How do I invite a new user to our Pluralsight plan?
  - id: listUsers
    intent: List licensed users in the plan
    question: Which users hold a license in our plan?
  - id: listTeams
    intent: List teams in the plan
    question: What teams exist in our learning plan?
  phrasing_ops: 4
  slug: pluralsight-licensing-api
- baseURL: https://{workspace}.appfireflow.com/v3/customer/core
  baseurl_source: declared
  description: Pull request data operations
  name: Pluralsight Pull Requests API
  phrasing_intents:
  - id: getPullRequests
    intent: Get pull requests with comments and events
    question: Which pull requests were opened across our repos last week?
  phrasing_ops: 1
  slug: pluralsight-pull-requests-api
- baseURL: https://app.pluralsight.com/plans/api/reports/v1
  baseurl_source: declared
  description: Report download operations (deprecated)
  name: Pluralsight Reports API
  phrasing_intents:
  - id: downloadUserReport
    intent: Download a user report as CSV
    question: How do I export a CSV of all users on our plan?
  - id: downloadCourseCompletionReport
    intent: Download a course completion report as CSV
    question: Which learners have completed which courses?
  - id: downloadCourseUsageReport
    intent: Download a course usage report as CSV
    question: How much time are people spending watching courses?
  phrasing_ops: 3
  slug: pluralsight-reports-api
- baseURL: https://{workspace}.appfireflow.com/v3/customer/core
  baseurl_source: declared
  description: Repository data operations
  name: Pluralsight Repos API
  phrasing_intents:
  - id: getRepos
    intent: List repositories from connected source control
    question: Which repositories does Flow see from our source control systems?
  phrasing_ops: 1
  slug: pluralsight-repos-api
- baseURL: https://{workspace}.appfireflow.com/v3/customer/core
  baseurl_source: declared
  description: Ticket data operations
  name: Pluralsight Tickets API
  phrasing_intents:
  - id: getTickets
    intent: Get tickets from project management tools
    question: What tickets were worked on in our project tracker this month?
  phrasing_ops: 1
  slug: pluralsight-tickets-api
- baseURL: https://{workspace}.appfireflow.com/v3/customer/core
  baseurl_source: declared
  description: Flow user management operations
  name: Pluralsight Users API
  phrasing_intents:
  - id: listUsers
    intent: List Flow users in the workspace
    question: Who are the users in our Flow workspace?
  - id: updateUsers
    intent: Update, merge or hide Flow users in bulk
    question: How do I merge duplicate Flow user accounts?
  phrasing_ops: 2
  slug: pluralsight-users-api
- baseURL: https://paas-rest-api.pluralsight.com
  baseurl_source: declared
  description: GraphQL query and mutation operations
  name: Pluralsight Graph QL API
  phrasing_intents:
  - id: manageChannels
    intent: Query and manage learning content channels
    question: How do I create a content channel and add members to it?
  phrasing_ops: 1
  slug: pluralsight-graph-ql-api
artifact_total: 268
collections:
- collection_type: postman
  name: Pluralsight Channels Catalog API
  slug: postman-pluralsight-catalog-api
- collection_type: postman
  name: Pluralsight Channels Catalog Coding Metrics API
  slug: postman-pluralsight-coding-metrics-api
- collection_type: postman
  name: Pluralsight Channels Catalog Collaboration Metrics API
  slug: postman-pluralsight-collaboration-metrics-api
- collection_type: postman
  name: Pluralsight Channels Catalog Commits API
  slug: postman-pluralsight-commits-api
- collection_type: postman
  name: Pluralsight Channels Catalog DORA Metrics API
  slug: postman-pluralsight-dora-metrics-api
- collection_type: postman
  name: Pluralsight Channels Catalog GraphQL API
  slug: postman-pluralsight-graphql-api
- collection_type: postman
  name: Pluralsight Channels Catalog Integrations API
  slug: postman-pluralsight-integrations-api
- collection_type: postman
  name: Pluralsight Channels Catalog Licensing API
  slug: postman-pluralsight-licensing-api
- collection_type: postman
  name: Pluralsight Channels Catalog Pull Requests API
  slug: postman-pluralsight-pull-requests-api
- collection_type: postman
  name: Pluralsight Channels Catalog Reports API
  slug: postman-pluralsight-reports-api
- collection_type: postman
  name: Pluralsight Channels Catalog Repos API
  slug: postman-pluralsight-repos-api
- collection_type: postman
  name: Pluralsight Channels Catalog Teams API
  slug: postman-pluralsight-teams-api
- collection_type: postman
  name: Pluralsight Channels Catalog Tickets API
  slug: postman-pluralsight-tickets-api
- collection_type: postman
  name: Pluralsight Channels Catalog Users API
  slug: postman-pluralsight-users-api
- collection_type: open
  name: Pluralsight Channels API
  slug: open-channels
- collection_type: open
  name: Pluralsight Content Catalog API
  slug: open-content-catalog
- collection_type: open
  name: Pluralsight Content Progress API
  slug: open-content-progress
- collection_type: open
  name: Pluralsight Content Slug API
  slug: open-content-slug
- collection_type: open
  name: Pluralsight Course Catalog API
  slug: open-course-catalog
- collection_type: open
  name: Pluralsight Course Daily Usage API
  slug: open-course-daily-usage
- collection_type: open
  name: Pluralsight Course Progress API
  slug: open-course-progress
- collection_type: open
  name: Pluralsight Flow Coding Metrics API
  slug: open-flow-coding-metrics
- collection_type: open
  name: Pluralsight Flow Collaboration Metrics API
  slug: open-flow-collaboration-metrics
- collection_type: open
  name: Pluralsight Flow Commits API
  slug: open-flow-commits
- collection_type: open
  name: Pluralsight Flow DORA Metrics API
  slug: open-flow-dora-metrics
- collection_type: open
  name: Pluralsight Flow Integrations API
  slug: open-flow-integrations
- collection_type: open
  name: Pluralsight Flow Pull Requests API
  slug: open-flow-pull-requests
- collection_type: open
  name: Pluralsight Flow Repos API
  slug: open-flow-repos
- collection_type: open
  name: Pluralsight Flow Teams API
  slug: open-flow-teams
- collection_type: open
  name: Pluralsight Flow Tickets API
  slug: open-flow-tickets
- collection_type: open
  name: Pluralsight Flow Users API
  slug: open-flow-users
- collection_type: open
  name: Pluralsight Labs API
  slug: open-labs
- collection_type: open
  name: Pluralsight Learning Paths API
  slug: open-learning-paths
- collection_type: open
  name: Pluralsight Licensing REST API
  slug: open-licensing-rest
- collection_type: open
  name: Pluralsight Plan Info API
  slug: open-plan-info
- collection_type: open
  name: Pluralsight Channels Catalog API
  slug: open-pluralsight-catalog-api
- collection_type: open
  name: Pluralsight Channels Catalog Coding Metrics API
  slug: open-pluralsight-coding-metrics-api
- collection_type: open
  name: Pluralsight Channels Catalog Collaboration Metrics API
  slug: open-pluralsight-collaboration-metrics-api
- collection_type: open
  name: Pluralsight Channels Catalog Commits API
  slug: open-pluralsight-commits-api
- collection_type: open
  name: Pluralsight Channels Catalog DORA Metrics API
  slug: open-pluralsight-dora-metrics-api
- collection_type: open
  name: Pluralsight Channels Catalog GraphQL API
  slug: open-pluralsight-graphql-api
- collection_type: open
  name: Pluralsight Channels Catalog Integrations API
  slug: open-pluralsight-integrations-api
- collection_type: open
  name: Pluralsight Channels Catalog Licensing API
  slug: open-pluralsight-licensing-api
- collection_type: open
  name: Pluralsight Channels Catalog Pull Requests API
  slug: open-pluralsight-pull-requests-api
- collection_type: open
  name: Pluralsight Channels Catalog Reports API
  slug: open-pluralsight-reports-api
- collection_type: open
  name: Pluralsight Channels Catalog Repos API
  slug: open-pluralsight-repos-api
- collection_type: open
  name: Pluralsight Channels Catalog Teams API
  slug: open-pluralsight-teams-api
- collection_type: open
  name: Pluralsight Channels Catalog Tickets API
  slug: open-pluralsight-tickets-api
- collection_type: open
  name: Pluralsight Channels Catalog Users API
  slug: open-pluralsight-users-api
- collection_type: open
  name: Pluralsight Practice Exams API
  slug: open-practice-exams
- collection_type: open
  name: Pluralsight Programs API
  slug: open-programs
- collection_type: open
  name: Pluralsight Public Course Catalog REST API
  slug: open-public-course-catalog-rest
- collection_type: open
  name: Pluralsight Reports REST API
  slug: open-reports-rest
- collection_type: open
  name: Pluralsight Role IQ API
  slug: open-role-iq
- collection_type: open
  name: Pluralsight Skills Assessment API
  slug: open-skills-assessment
- collection_type: open
  name: Pluralsight Tags API
  slug: open-tags
- collection_type: open
  name: Pluralsight Teams API
  slug: open-teams
- collection_type: open
  name: Pluralsight User Management API
  slug: open-user-management
common:
- group: other
  href: https://artifacts.apis.io/pluralsight/capabilities/pluralsight-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/pluralsight-capability-edges.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/pluralsight/overview
- group: agent
  href: https://artifacts.apis.io/pluralsight/agentic-access/pluralsight-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/pluralsight-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/pluralsight/security/pluralsight-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/pluralsight-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/pluralsight/security/pluralsight-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/pluralsight-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/pluralsight/security/pluralsight-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/pluralsight-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/pluralsight/authentication/pluralsight-authentication.yml
  title: ''
  type: Authentication
  url: authentication/pluralsight-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pluralsight
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/pluralsight
- group: start
  title: ''
  type: Portal
  url: https://developer.pluralsight.com
- group: operate
  title: ''
  type: FAQ
  url: https://developer.pluralsight.com/docs/getting-started/faqs
- group: build
  title: ''
  type: CodeExamples
  url: https://developer.pluralsight.com/docs/getting-started/examples
- group: docs
  title: ''
  type: GraphQL
  url: https://developer.pluralsight.com/docs/getting-started/using-graphql
- group: docs
  title: ''
  type: Documentation
  url: https://developer.pluralsight.com/docs/deprecations/2025-deprecation-guide
- group: docs
  title: ''
  type: Documentation
  url: https://help.pluralsight.com/hc/en-us/articles/24420566008084-Migrating-from-REST-to-GraphQL-APIs
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.pluralsight.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.pluralsight.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://help.pluralsight.com
- group: company
  title: ''
  type: Blog
  url: https://www.pluralsight.com/blog
- group: agent
  href: https://artifacts.apis.io/pluralsight/well-known/pluralsight-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/pluralsight-well-known.yml
- group: auth
  href: https://artifacts.apis.io/pluralsight/well-known/pluralsight-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/pluralsight-security.txt
- group: auth
  title: ''
  type: Security
  url: https://pluralsight.com/.well-known/security.txt
- group: agent
  href: https://artifacts.apis.io/pluralsight/mcp/pluralsight-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/pluralsight-mcp.yml
- group: build
  href: https://artifacts.apis.io/pluralsight/mcp/pluralsight-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/pluralsight-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/pluralsight/llms/pluralsight-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/pluralsight-llms.txt
- group: design
  href: https://artifacts.apis.io/pluralsight/conformance/pluralsight-conformance.yml
  title: ''
  type: Conformance
  url: conformance/pluralsight-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.pluralsight.com/
- group: design
  href: https://artifacts.apis.io/pluralsight/errors/pluralsight-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/pluralsight-problem-types.yml
- group: design
  href: https://artifacts.apis.io/pluralsight/lifecycle/pluralsight-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/pluralsight-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://developer.pluralsight.com/docs/deprecations/deprecation-policy
- group: auth
  href: https://artifacts.apis.io/pluralsight/scopes/pluralsight-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/pluralsight-scopes.yml
- group: design
  href: https://artifacts.apis.io/pluralsight/conventions/pluralsight-conventions.yml
  title: ''
  type: Conventions
  url: conventions/pluralsight-conventions.yml
- group: operate
  href: https://artifacts.apis.io/pluralsight/changelog/pluralsight-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/pluralsight-changelog.yml
- group: start
  href: https://artifacts.apis.io/pluralsight/sandbox/pluralsight-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/pluralsight-sandbox.yml
- group: build
  href: https://artifacts.apis.io/pluralsight/packages/pluralsight-packages.yml
  title: ''
  type: Packages
  url: packages/pluralsight-packages.yml
- group: design
  href: https://artifacts.apis.io/pluralsight/data-model/pluralsight-data-model.yml
  title: ''
  type: DataModel
  url: data-model/pluralsight-data-model.yml
- group: agent
  href: https://artifacts.apis.io/pluralsight/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://artifacts.apis.io/pluralsight/overlays/pluralsight-graphql-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/pluralsight-graphql-overlay.yaml
- group: operate
  href: https://artifacts.apis.io/pluralsight/rate-limits/pluralsight-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/pluralsight-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/pluralsight/plans/pluralsight-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/pluralsight-plans-pricing.yml
- group: commercial
  href: https://artifacts.apis.io/pluralsight/finops/pluralsight-finops.yml
  title: ''
  type: FinOps
  url: finops/pluralsight-finops.yml
- group: design
  href: https://artifacts.apis.io/pluralsight/vocabulary/pluralsight-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/pluralsight-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/pluralsight/rules/pluralsight-spectral-rules.yml
  title: ''
  type: SpectralRules
  url: rules/pluralsight-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/pluralsight/json-ld/pluralsight-context.jsonld
  title: ''
  type: JSONLDContext
  url: json-ld/pluralsight-context.jsonld
- group: build
  href: https://artifacts.apis.io/pluralsight/examples/pluralsight-course-catalog-graph-ql-request-example.json
  title: ''
  type: Examples
  url: examples/pluralsight-course-catalog-graph-ql-request-example.json
- group: docs
  href: https://artifacts.apis.io/pluralsight/json-schema/pluralsight-course-catalog-graph-ql-response-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/pluralsight-course-catalog-graph-ql-response-schema.json
- group: design
  href: https://artifacts.apis.io/pluralsight/json-structure/pluralsight-course-catalog-graph-ql-response-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/pluralsight-course-catalog-graph-ql-response-structure.json
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.pluralsight.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.pluralsight.com/docs/getting-started/using-graphql
- group: docs
  title: ''
  type: APIReference
  url: https://developer.pluralsight.com/schema/content/courseCatalog
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.pluralsight.com/docs/getting-started/using-graphql
- group: start
  title: ''
  type: Quickstart
  url: https://developer.pluralsight.com/quick-start
- group: auth
  title: ''
  type: Authentication
  url: https://developer.pluralsight.com/manage-keys
- group: auth
  title: ''
  type: API Keys
  url: https://developer.pluralsight.com/manage-keys
- group: other
  title: ''
  type: Playground
  url: https://developer.pluralsight.com/playground
- group: commercial
  title: ''
  type: Pricing
  url: https://www.pluralsight.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.pluralsight.com/pricing
- group: start
  title: ''
  type: Login
  url: https://app.pluralsight.com
- group: company
  title: ''
  type: Website
  url: https://www.pluralsight.com
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/kinlaneapi/pluralsight/overview
created: '2024'
description: APIs for the Pluralsight technology skills and engineering intelligence platform, providing access to courses, learning paths, assessments, user progress, channels, teams, and engineering metrics via GraphQL and REST APIs.
examples:
- key_count: 3
  name: Pluralsight Channels Graph Ql Error Example
  slug: pluralsight-channels-graph-ql-error-example
- key_count: 3
  name: Pluralsight Channels Graph Ql Request Example
  slug: pluralsight-channels-graph-ql-request-example
- key_count: 2
  name: Pluralsight Channels Graph Ql Response Example
  slug: pluralsight-channels-graph-ql-response-example
- key_count: 3
  name: Pluralsight Content Catalog Graph Ql Error Example
  slug: pluralsight-content-catalog-graph-ql-error-example
- key_count: 3
  name: Pluralsight Content Catalog Graph Ql Request Example
  slug: pluralsight-content-catalog-graph-ql-request-example
- key_count: 2
  name: Pluralsight Content Catalog Graph Ql Response Example
  slug: pluralsight-content-catalog-graph-ql-response-example
- key_count: 3
  name: Pluralsight Content Progress Graph Ql Error Example
  slug: pluralsight-content-progress-graph-ql-error-example
- key_count: 3
  name: Pluralsight Content Progress Graph Ql Request Example
  slug: pluralsight-content-progress-graph-ql-request-example
- key_count: 2
  name: Pluralsight Content Progress Graph Ql Response Example
  slug: pluralsight-content-progress-graph-ql-response-example
- key_count: 3
  name: Pluralsight Content Slug Graph Ql Error Example
  slug: pluralsight-content-slug-graph-ql-error-example
- key_count: 3
  name: Pluralsight Content Slug Graph Ql Request Example
  slug: pluralsight-content-slug-graph-ql-request-example
- key_count: 2
  name: Pluralsight Content Slug Graph Ql Response Example
  slug: pluralsight-content-slug-graph-ql-response-example
- key_count: 3
  name: Pluralsight Course Catalog Graph Ql Error Example
  slug: pluralsight-course-catalog-graph-ql-error-example
- key_count: 3
  name: Pluralsight Course Catalog Graph Ql Request Example
  slug: pluralsight-course-catalog-graph-ql-request-example
- key_count: 2
  name: Pluralsight Course Catalog Graph Ql Response Example
  slug: pluralsight-course-catalog-graph-ql-response-example
- key_count: 3
  name: Pluralsight Course Daily Usage Graph Ql Error Example
  slug: pluralsight-course-daily-usage-graph-ql-error-example
- key_count: 3
  name: Pluralsight Course Daily Usage Graph Ql Request Example
  slug: pluralsight-course-daily-usage-graph-ql-request-example
- key_count: 2
  name: Pluralsight Course Daily Usage Graph Ql Response Example
  slug: pluralsight-course-daily-usage-graph-ql-response-example
- key_count: 3
  name: Pluralsight Course Progress Graph Ql Error Example
  slug: pluralsight-course-progress-graph-ql-error-example
- key_count: 3
  name: Pluralsight Course Progress Graph Ql Request Example
  slug: pluralsight-course-progress-graph-ql-request-example
- key_count: 2
  name: Pluralsight Course Progress Graph Ql Response Example
  slug: pluralsight-course-progress-graph-ql-response-example
- key_count: 3
  name: Pluralsight Labs Graph Ql Error Example
  slug: pluralsight-labs-graph-ql-error-example
- key_count: 3
  name: Pluralsight Labs Graph Ql Request Example
  slug: pluralsight-labs-graph-ql-request-example
- key_count: 2
  name: Pluralsight Labs Graph Ql Response Example
  slug: pluralsight-labs-graph-ql-response-example
- key_count: 3
  name: Pluralsight Learning Paths Graph Ql Error Example
  slug: pluralsight-learning-paths-graph-ql-error-example
- key_count: 3
  name: Pluralsight Learning Paths Graph Ql Request Example
  slug: pluralsight-learning-paths-graph-ql-request-example
- key_count: 2
  name: Pluralsight Learning Paths Graph Ql Response Example
  slug: pluralsight-learning-paths-graph-ql-response-example
- key_count: 3
  name: Pluralsight Plan Info Graph Ql Error Example
  slug: pluralsight-plan-info-graph-ql-error-example
- key_count: 3
  name: Pluralsight Plan Info Graph Ql Request Example
  slug: pluralsight-plan-info-graph-ql-request-example
- key_count: 2
  name: Pluralsight Plan Info Graph Ql Response Example
  slug: pluralsight-plan-info-graph-ql-response-example
- key_count: 3
  name: Pluralsight Practice Exams Graph Ql Error Example
  slug: pluralsight-practice-exams-graph-ql-error-example
- key_count: 3
  name: Pluralsight Practice Exams Graph Ql Request Example
  slug: pluralsight-practice-exams-graph-ql-request-example
- key_count: 2
  name: Pluralsight Practice Exams Graph Ql Response Example
  slug: pluralsight-practice-exams-graph-ql-response-example
- key_count: 3
  name: Pluralsight Programs Graph Ql Error Example
  slug: pluralsight-programs-graph-ql-error-example
- key_count: 3
  name: Pluralsight Programs Graph Ql Request Example
  slug: pluralsight-programs-graph-ql-request-example
- key_count: 2
  name: Pluralsight Programs Graph Ql Response Example
  slug: pluralsight-programs-graph-ql-response-example
- key_count: 3
  name: Pluralsight Role Iq Graph Ql Error Example
  slug: pluralsight-role-iq-graph-ql-error-example
- key_count: 3
  name: Pluralsight Role Iq Graph Ql Request Example
  slug: pluralsight-role-iq-graph-ql-request-example
- key_count: 2
  name: Pluralsight Role Iq Graph Ql Response Example
  slug: pluralsight-role-iq-graph-ql-response-example
- key_count: 3
  name: Pluralsight Skills Assessment Graph Ql Error Example
  slug: pluralsight-skills-assessment-graph-ql-error-example
- key_count: 3
  name: Pluralsight Skills Assessment Graph Ql Request Example
  slug: pluralsight-skills-assessment-graph-ql-request-example
- key_count: 2
  name: Pluralsight Skills Assessment Graph Ql Response Example
  slug: pluralsight-skills-assessment-graph-ql-response-example
- key_count: 3
  name: Pluralsight Tags Graph Ql Error Example
  slug: pluralsight-tags-graph-ql-error-example
- key_count: 3
  name: Pluralsight Tags Graph Ql Request Example
  slug: pluralsight-tags-graph-ql-request-example
- key_count: 2
  name: Pluralsight Tags Graph Ql Response Example
  slug: pluralsight-tags-graph-ql-response-example
- key_count: 3
  name: Pluralsight Teams Graph Ql Error Example
  slug: pluralsight-teams-graph-ql-error-example
- key_count: 3
  name: Pluralsight Teams Graph Ql Request Example
  slug: pluralsight-teams-graph-ql-request-example
- key_count: 2
  name: Pluralsight Teams Graph Ql Response Example
  slug: pluralsight-teams-graph-ql-response-example
- key_count: 3
  name: Pluralsight User Management Graph Ql Error Example
  slug: pluralsight-user-management-graph-ql-error-example
- key_count: 3
  name: Pluralsight User Management Graph Ql Request Example
  slug: pluralsight-user-management-graph-ql-request-example
- key_count: 2
  name: Pluralsight User Management Graph Ql Response Example
  slug: pluralsight-user-management-graph-ql-response-example
features:
- description: Access the full Pluralsight course catalog with titles, authors, duration, and release dates via GraphQL.
  name: Course Catalog API
- description: Measure technology skills with Skill IQ assessments and track competency levels.
  name: Skills Assessment
- description: Assess role readiness and track skill gaps for technology roles.
  name: Role IQ
- description: Track course completion, content progress, and daily usage across users and teams.
  name: Learning Progress Tracking
- description: Create and manage curated content channels with sections and member management.
  name: Channels
- description: Manage users, invitations, teams, and permissions via GraphQL mutations.
  name: User and Team Management
- description: Access DevOps Research and Assessment metrics for engineering team performance.
  name: DORA Metrics
- description: Track code-level productivity metrics and developer activity.
  name: Coding Metrics
- description: Monitor pull request and code review collaboration patterns.
  name: Collaboration Metrics
- description: Access hands-on lab catalog and track lab activity for practical learning.
  name: Labs
- description: Retrieve practice exam attempts and scores for certification preparation.
  name: Practice Exams
- description: Access commit, PR, ticket, and repository data for engineering analytics.
  name: Flow Engineering Intelligence
finops:
- has_sources: true
  method: generated
  name: Pluralsight Finops
  primary_unit: ''
  service_category: Learning and Development
  slug: pluralsight-finops
  template: false
graphqls:
- description: GraphQL query for accessing course catalog information including titles, descriptions, authors, duration, release dates, and retirement status. Updated daily.
  name: Pluralsight GraphQL API
  slug: pluralsight-graphql
image: https://www.pluralsight.com/content/dam/pluralsight2/general/headers/logo.png
json_schemas:
- name: GraphQLError
  property_count: 3
  slug: pluralsight-channels-graph-ql-error
- name: GraphQLRequest
  property_count: 3
  slug: pluralsight-channels-graph-ql-request
- name: GraphQLResponse
  property_count: 2
  slug: pluralsight-channels-graph-ql-response
- name: GraphQLError
  property_count: 3
  slug: pluralsight-content-catalog-graph-ql-error
- name: GraphQLRequest
  property_count: 3
  slug: pluralsight-content-catalog-graph-ql-request
- name: GraphQLResponse
  property_count: 2
  slug: pluralsight-content-catalog-graph-ql-response
- name: GraphQLError
  property_count: 3
  slug: pluralsight-content-progress-graph-ql-error
- name: GraphQLRequest
  property_count: 3
  slug: pluralsight-content-progress-graph-ql-request
- name: GraphQLResponse
  property_count: 2
  slug: pluralsight-content-progress-graph-ql-response
- name: GraphQLError
  property_count: 3
  slug: pluralsight-content-slug-graph-ql-error
- name: GraphQLRequest
  property_count: 3
  slug: pluralsight-content-slug-graph-ql-request
- name: GraphQLResponse
  property_count: 2
  slug: pluralsight-content-slug-graph-ql-response
- name: GraphQLError
  property_count: 3
  slug: pluralsight-course-catalog-graph-ql-error
- name: GraphQLRequest
  property_count: 3
  slug: pluralsight-course-catalog-graph-ql-request
- name: GraphQLResponse
  property_count: 2
  slug: pluralsight-course-catalog-graph-ql-response
- name: GraphQLError
  property_count: 3
  slug: pluralsight-course-daily-usage-graph-ql-error
- name: GraphQLRequest
  property_count: 3
  slug: pluralsight-course-daily-usage-graph-ql-request
- name: GraphQLResponse
  property_count: 2
  slug: pluralsight-course-daily-usage-graph-ql-response
- name: GraphQLError
  property_count: 3
  slug: pluralsight-course-progress-graph-ql-error
- name: GraphQLRequest
  property_count: 3
  slug: pluralsight-course-progress-graph-ql-request
- name: GraphQLResponse
  property_count: 2
  slug: pluralsight-course-progress-graph-ql-response
- name: GraphQLError
  property_count: 3
  slug: pluralsight-graphqlerror
- name: GraphQLRequest
  property_count: 3
  slug: pluralsight-graphqlrequest
- name: GraphQLResponse
  property_count: 2
  slug: pluralsight-graphqlresponse
- name: GraphQLError
  property_count: 3
  slug: pluralsight-labs-graph-ql-error
- name: GraphQLRequest
  property_count: 3
  slug: pluralsight-labs-graph-ql-request
- name: GraphQLResponse
  property_count: 2
  slug: pluralsight-labs-graph-ql-response
- name: GraphQLError
  property_count: 3
  slug: pluralsight-learning-paths-graph-ql-error
- name: GraphQLRequest
  property_count: 3
  slug: pluralsight-learning-paths-graph-ql-request
- name: GraphQLResponse
  property_count: 2
  slug: pluralsight-learning-paths-graph-ql-response
- name: GraphQLError
  property_count: 3
  slug: pluralsight-plan-info-graph-ql-error
- name: GraphQLRequest
  property_count: 3
  slug: pluralsight-plan-info-graph-ql-request
- name: GraphQLResponse
  property_count: 2
  slug: pluralsight-plan-info-graph-ql-response
- name: GraphQLError
  property_count: 3
  slug: pluralsight-practice-exams-graph-ql-error
- name: GraphQLRequest
  property_count: 3
  slug: pluralsight-practice-exams-graph-ql-request
- name: GraphQLResponse
  property_count: 2
  slug: pluralsight-practice-exams-graph-ql-response
- name: GraphQLError
  property_count: 3
  slug: pluralsight-programs-graph-ql-error
- name: GraphQLRequest
  property_count: 3
  slug: pluralsight-programs-graph-ql-request
- name: GraphQLResponse
  property_count: 2
  slug: pluralsight-programs-graph-ql-response
- name: GraphQLError
  property_count: 3
  slug: pluralsight-role-iq-graph-ql-error
- name: GraphQLRequest
  property_count: 3
  slug: pluralsight-role-iq-graph-ql-request
- name: GraphQLResponse
  property_count: 2
  slug: pluralsight-role-iq-graph-ql-response
- name: GraphQLError
  property_count: 3
  slug: pluralsight-skills-assessment-graph-ql-error
- name: GraphQLRequest
  property_count: 3
  slug: pluralsight-skills-assessment-graph-ql-request
- name: GraphQLResponse
  property_count: 2
  slug: pluralsight-skills-assessment-graph-ql-response
- name: GraphQLError
  property_count: 3
  slug: pluralsight-tags-graph-ql-error
- name: GraphQLRequest
  property_count: 3
  slug: pluralsight-tags-graph-ql-request
- name: GraphQLResponse
  property_count: 2
  slug: pluralsight-tags-graph-ql-response
- name: GraphQLError
  property_count: 3
  slug: pluralsight-teams-graph-ql-error
- name: GraphQLRequest
  property_count: 3
  slug: pluralsight-teams-graph-ql-request
- name: GraphQLResponse
  property_count: 2
  slug: pluralsight-teams-graph-ql-response
- name: GraphQLError
  property_count: 3
  slug: pluralsight-user-management-graph-ql-error
- name: GraphQLRequest
  property_count: 3
  slug: pluralsight-user-management-graph-ql-request
- name: GraphQLResponse
  property_count: 2
  slug: pluralsight-user-management-graph-ql-response
json_structures:
- name: Pluralsight Channels Graph Ql Error Structure
  property_count: 3
  slug: pluralsight-channels-graph-ql-error-structure
- name: Pluralsight Channels Graph Ql Request Structure
  property_count: 3
  slug: pluralsight-channels-graph-ql-request-structure
- name: Pluralsight Channels Graph Ql Response Structure
  property_count: 2
  slug: pluralsight-channels-graph-ql-response-structure
- name: Pluralsight Content Catalog Graph Ql Error Structure
  property_count: 3
  slug: pluralsight-content-catalog-graph-ql-error-structure
- name: Pluralsight Content Catalog Graph Ql Request Structure
  property_count: 3
  slug: pluralsight-content-catalog-graph-ql-request-structure
- name: Pluralsight Content Catalog Graph Ql Response Structure
  property_count: 2
  slug: pluralsight-content-catalog-graph-ql-response-structure
- name: Pluralsight Content Progress Graph Ql Error Structure
  property_count: 3
  slug: pluralsight-content-progress-graph-ql-error-structure
- name: Pluralsight Content Progress Graph Ql Request Structure
  property_count: 3
  slug: pluralsight-content-progress-graph-ql-request-structure
- name: Pluralsight Content Progress Graph Ql Response Structure
  property_count: 2
  slug: pluralsight-content-progress-graph-ql-response-structure
- name: Pluralsight Content Slug Graph Ql Error Structure
  property_count: 3
  slug: pluralsight-content-slug-graph-ql-error-structure
- name: Pluralsight Content Slug Graph Ql Request Structure
  property_count: 3
  slug: pluralsight-content-slug-graph-ql-request-structure
- name: Pluralsight Content Slug Graph Ql Response Structure
  property_count: 2
  slug: pluralsight-content-slug-graph-ql-response-structure
- name: Pluralsight Course Catalog Graph Ql Error Structure
  property_count: 3
  slug: pluralsight-course-catalog-graph-ql-error-structure
- name: Pluralsight Course Catalog Graph Ql Request Structure
  property_count: 3
  slug: pluralsight-course-catalog-graph-ql-request-structure
- name: Pluralsight Course Catalog Graph Ql Response Structure
  property_count: 2
  slug: pluralsight-course-catalog-graph-ql-response-structure
- name: Pluralsight Course Daily Usage Graph Ql Error Structure
  property_count: 3
  slug: pluralsight-course-daily-usage-graph-ql-error-structure
- name: Pluralsight Course Daily Usage Graph Ql Request Structure
  property_count: 3
  slug: pluralsight-course-daily-usage-graph-ql-request-structure
- name: Pluralsight Course Daily Usage Graph Ql Response Structure
  property_count: 2
  slug: pluralsight-course-daily-usage-graph-ql-response-structure
- name: Pluralsight Course Progress Graph Ql Error Structure
  property_count: 3
  slug: pluralsight-course-progress-graph-ql-error-structure
- name: Pluralsight Course Progress Graph Ql Request Structure
  property_count: 3
  slug: pluralsight-course-progress-graph-ql-request-structure
- name: Pluralsight Course Progress Graph Ql Response Structure
  property_count: 2
  slug: pluralsight-course-progress-graph-ql-response-structure
- name: Pluralsight Labs Graph Ql Error Structure
  property_count: 3
  slug: pluralsight-labs-graph-ql-error-structure
- name: Pluralsight Labs Graph Ql Request Structure
  property_count: 3
  slug: pluralsight-labs-graph-ql-request-structure
- name: Pluralsight Labs Graph Ql Response Structure
  property_count: 2
  slug: pluralsight-labs-graph-ql-response-structure
- name: Pluralsight Learning Paths Graph Ql Error Structure
  property_count: 3
  slug: pluralsight-learning-paths-graph-ql-error-structure
- name: Pluralsight Learning Paths Graph Ql Request Structure
  property_count: 3
  slug: pluralsight-learning-paths-graph-ql-request-structure
- name: Pluralsight Learning Paths Graph Ql Response Structure
  property_count: 2
  slug: pluralsight-learning-paths-graph-ql-response-structure
- name: Pluralsight Plan Info Graph Ql Error Structure
  property_count: 3
  slug: pluralsight-plan-info-graph-ql-error-structure
- name: Pluralsight Plan Info Graph Ql Request Structure
  property_count: 3
  slug: pluralsight-plan-info-graph-ql-request-structure
- name: Pluralsight Plan Info Graph Ql Response Structure
  property_count: 2
  slug: pluralsight-plan-info-graph-ql-response-structure
- name: Pluralsight Practice Exams Graph Ql Error Structure
  property_count: 3
  slug: pluralsight-practice-exams-graph-ql-error-structure
- name: Pluralsight Practice Exams Graph Ql Request Structure
  property_count: 3
  slug: pluralsight-practice-exams-graph-ql-request-structure
- name: Pluralsight Practice Exams Graph Ql Response Structure
  property_count: 2
  slug: pluralsight-practice-exams-graph-ql-response-structure
- name: Pluralsight Programs Graph Ql Error Structure
  property_count: 3
  slug: pluralsight-programs-graph-ql-error-structure
- name: Pluralsight Programs Graph Ql Request Structure
  property_count: 3
  slug: pluralsight-programs-graph-ql-request-structure
- name: Pluralsight Programs Graph Ql Response Structure
  property_count: 2
  slug: pluralsight-programs-graph-ql-response-structure
- name: Pluralsight Role Iq Graph Ql Error Structure
  property_count: 3
  slug: pluralsight-role-iq-graph-ql-error-structure
- name: Pluralsight Role Iq Graph Ql Request Structure
  property_count: 3
  slug: pluralsight-role-iq-graph-ql-request-structure
- name: Pluralsight Role Iq Graph Ql Response Structure
  property_count: 2
  slug: pluralsight-role-iq-graph-ql-response-structure
- name: Pluralsight Skills Assessment Graph Ql Error Structure
  property_count: 3
  slug: pluralsight-skills-assessment-graph-ql-error-structure
- name: Pluralsight Skills Assessment Graph Ql Request Structure
  property_count: 3
  slug: pluralsight-skills-assessment-graph-ql-request-structure
- name: Pluralsight Skills Assessment Graph Ql Response Structure
  property_count: 2
  slug: pluralsight-skills-assessment-graph-ql-response-structure
- name: Pluralsight Structure
  property_count: 0
  slug: pluralsight-structure
- name: Pluralsight Tags Graph Ql Error Structure
  property_count: 3
  slug: pluralsight-tags-graph-ql-error-structure
- name: Pluralsight Tags Graph Ql Request Structure
  property_count: 3
  slug: pluralsight-tags-graph-ql-request-structure
- name: Pluralsight Tags Graph Ql Response Structure
  property_count: 2
  slug: pluralsight-tags-graph-ql-response-structure
- name: Pluralsight Teams Graph Ql Error Structure
  property_count: 3
  slug: pluralsight-teams-graph-ql-error-structure
- name: Pluralsight Teams Graph Ql Request Structure
  property_count: 3
  slug: pluralsight-teams-graph-ql-request-structure
- name: Pluralsight Teams Graph Ql Response Structure
  property_count: 2
  slug: pluralsight-teams-graph-ql-response-structure
- name: Pluralsight User Management Graph Ql Error Structure
  property_count: 3
  slug: pluralsight-user-management-graph-ql-error-structure
- name: Pluralsight User Management Graph Ql Request Structure
  property_count: 3
  slug: pluralsight-user-management-graph-ql-request-structure
- name: Pluralsight User Management Graph Ql Response Structure
  property_count: 2
  slug: pluralsight-user-management-graph-ql-response-structure
jsonld:
- class_count: 3
  name: Pluralsight Context
  property_count: 8
  slug: pluralsight-context
layout: provider
mcp_servers:
- description: 'Pluralsight runs a live, remote Model Context Protocol server at https://mcp.pluralsight.com/mcp. It is a real MCP endpoint, not a marketing page: an unauthenticated JSON-RPC tools/list call returns a'
  name: Pluralsight MCP Gateway
  slug: pluralsight-mcp-gateway
modified: '2026-08-29'
name: Pluralsight
nav: Providers
network: true
overview: 'Pluralsight publishes 13 API contracts indexed on the [APIs.io](https://apis.io/) network, including Catalog API, Coding Metrics API, Collaboration Metrics API, and 10 more. Tagged areas include Courses, Education, Engineering Metrics, Learning, and Skills Assessment.


  The Pluralsight catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Pluralsight''s developer surface includes authentication, developer portal, FAQ, code examples, documentation, support, engineering blog, and 53 more developer resources.'
plans:
- name: Pluralsight Plans Pricing
  plan_count: 8
  slug: pluralsight-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 3
  name: Pluralsight Rate Limits
  slug: pluralsight-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Pluralsight — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: pluralsight-jsonschema-spectral-rules
- authorship: generated
  effective_rule_count: 65
  extends:
  - spectral:oas
  name: Pluralsight API Rules
  rule_count: 24
  severity_counts:
    error: 13
    hint: 0
    info: 2
    warn: 9
  slug: pluralsight-spectral-rules
scopes:
- name: Pluralsight Scopes
  scope_count: 0
  slug: pluralsight-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 65.8
  coverage:
    artifact_dirs: 37
    catalog_earned: 69.0
    catalog_earned_first_party: 12.0
    catalog_gap: 46.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 68.4
    contract_governance: 45.5
    contract_quality: 57.9
    developer_ergonomics: 63.1
    discoverability: 80.0
    operational_transparency: 63.2
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 65.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 84.6
      derived: 0
      marker_coverage: 0.0
      total: 13
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 45.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/pluralsight/pluralsight-2026-08-17T124736.png
security:
- kind: authentication
  name: Pluralsight Authentication
  slug: pluralsight-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Pluralsight Domain Security
  slug: pluralsight-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Pluralsight Vulnerability Disclosure
  slug: pluralsight-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Pluralsight Trust Center
  slug: pluralsight-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, GDPR
skill_count: 4
skills:
- name: pluralsight-catalog-and-progress-report
  slug: pluralsight-catalog-and-progress-report
- name: pluralsight-curate-channel
  slug: pluralsight-curate-channel
- name: pluralsight-onboard-learner-to-team
  slug: pluralsight-onboard-learner-to-team
- name: pluralsight-skills-gap-analysis
  slug: pluralsight-skills-gap-analysis
slug: pluralsight
solutions:
- description: Technology skills platform with courses, assessments, and learning paths for upskilling teams.
  name: Pluralsight Skills
- description: Engineering intelligence platform with DORA metrics, coding analytics, and collaboration insights.
  name: Pluralsight Flow
tags:
- Courses
- Education
- Engineering Metrics
- Learning
- Skills Assessment
- Technology
- Video Training
use_cases:
- description: Sync Pluralsight course catalog and completion data with enterprise learning management systems.
  name: LMS Integration
- description: Assess team skill levels and identify training needs using Skill IQ and Role IQ data.
  name: Skills Gap Analysis
- description: Track DORA metrics, coding activity, and collaboration patterns for engineering teams.
  name: Engineering Performance
- description: Generate training completion reports for regulatory and compliance requirements.
  name: Compliance Reporting
- description: Automate new hire provisioning, team assignment, and learning path enrollment.
  name: Onboarding Automation
- description: Build custom learning channels with curated content for specific teams and roles.
  name: Content Curation
- description: Analyze commit, PR, and ticket data to measure and improve developer productivity.
  name: Developer Productivity
- description: Track practice exam scores and assessment results for certification readiness.
  name: Certification Tracking
website: https://www.pluralsight.com
---
