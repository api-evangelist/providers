---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.3
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Canvas Lms Agentic Access
  operation_count: 25
  slug: canvas-lms-agentic-access
  summary_line: 25 operations · 7 acting
api_count: 16
apis:
- description: 'GraphQL endpoint exposing the Canvas object graph (courses, users, enrollments, assignments, submissions, modules, discussion topics, outcomes, account hierarchies, etc.). Permissions mirror the REST '
  name: Canvas GraphQL API
  slug: canvas-graphql-api
- description: '1EdTech (IMS Global) LTI 1.3 / LTI Advantage implementation. Includes Deep Linking 2.0, Names and Role Provisioning Services (NRPS), Assignment and Grade Services (Line Items, Score, Result), Dynamic '
  name: Canvas LTI Advantage Services
  slug: canvas-lti-advantage
- description: Platform Notification Service (PNS) enables server-to-server communication by allowing Canvas to send Notices (webhook deliveries) to LTI tools outside the scope of an active user session. Tools regis
  name: Canvas Platform Notification Service
  slug: canvas-platform-notification-service
- description: Canvas Live Events stream lifecycle events emitted by Canvas (course, enrollment, assignment, submission, grade change, discussion, module, outcome, file/attachment, SIS batch, conversation, quiz, wik
  name: Canvas Live Events
  slug: canvas-live-events
- description: Data Access Platform (DAP) is the warehouse-scale data export API for Canvas Data 2 — the successor to Canvas Data 1 / Canvas Data CLI. DAP exposes Canvas tables and Caliper-derived event streams as s
  name: Canvas Data Access Platform
  slug: canvas-data-access-platform
- description: The SIS Import API ingests Canvas's canonical SIS CSV format (and ZIP archives of those CSVs) to provision accounts, terms, courses, sections, users, enrollments, groups, group memberships, cross-list
  name: Canvas SIS Import API
  slug: canvas-sis-import-api
- description: Root and sub-accounts that own the Canvas tenancy hierarchy
  name: Canvas LMS Accounts API
  slug: canvas-lms-accounts-api
- description: Assignments, due dates, submission types, and grading
  name: Canvas LMS Assignments API
  slug: canvas-lms-assignments-api
- description: The Canvas Course resource and its lifecycle
  name: Canvas LMS Courses API
  slug: canvas-lms-courses-api
- description: Discussion topics and entries
  name: Canvas LMS Discussions API
  slug: canvas-lms-discussions-api
- description: Student, teacher, TA, observer, and designer enrollments within a course or section
  name: Canvas LMS Enrollments API
  slug: canvas-lms-enrollments-api
- description: Course/user/group files and folders
  name: Canvas LMS Files API
  slug: canvas-lms-files-api
- description: Course modules and module items
  name: Canvas LMS Modules API
  slug: canvas-lms-modules-api
- description: Learning outcomes and outcome results
  name: Canvas LMS Outcomes API
  slug: canvas-lms-outcomes-api
- description: Student submissions, grades, and submission comments
  name: Canvas LMS Submissions API
  slug: canvas-lms-submissions-api
- description: User accounts, profiles, and per-user resources
  name: Canvas LMS Users API
  slug: canvas-lms-users-api
arazzos:
- description: List courses in an account, read one course's detail, then conclude it.
  name: Canvas LMS Audit Account Course and Conclude It
  slug: canvas-lms-account-course-audit-and-conclude-workflow
- description: Locate a discussion topic's graded assignment, then grade a student's discussion submission.
  name: Canvas LMS Grade a Discussion-backed Assignment
  slug: canvas-lms-assign-and-grade-discussion-workflow
- description: List a course's enrollments with grades, then conclude the course.
  name: Canvas LMS Conclude Course After Grade Check
  slug: canvas-lms-conclude-course-with-grade-check-workflow
- description: Read an assignment from a source course and recreate it in a target course.
  name: Canvas LMS Copy Assignment to Another Course
  slug: canvas-lms-copy-assignment-to-course-workflow
- description: Verify a course exists, create an assignment in it, then fetch the assignment back.
  name: Canvas LMS Create Assignment and Confirm
  slug: canvas-lms-create-assignment-and-confirm-workflow
- description: Create an assignment, find a student's submission, and post a grade plus comment.
  name: Canvas LMS Create Assignment and Grade Submission
  slug: canvas-lms-create-assignment-and-grade-submission-workflow
- description: Update a course's settings, then create its first assignment, and read it back.
  name: Canvas LMS Configure Course Then Author Assignment
  slug: canvas-lms-create-course-shell-then-author-assignment-workflow
- description: Enroll a teacher in a course, then create the course's first assignment.
  name: Canvas LMS Enroll Teacher Then Author Assignment
  slug: canvas-lms-enroll-teacher-then-author-assignment-workflow
- description: Enroll a user in a course and confirm the enrollment appears in the course roster.
  name: Canvas LMS Enroll User and Confirm
  slug: canvas-lms-enroll-user-and-confirm-workflow
- description: Read a submission and branch — excuse it when not submitted, otherwise post a grade.
  name: Canvas LMS Excuse or Grade a Submission
  slug: canvas-lms-excuse-or-grade-submission-workflow
- description: Search a course for an assignment by name and create it only when it is missing.
  name: Canvas LMS Find or Create Assignment
  slug: canvas-lms-find-or-create-assignment-workflow
- description: List an assignment's submissions, then post a grade to the first one returned.
  name: Canvas LMS Grade One of Many Submissions
  slug: canvas-lms-grade-all-submissions-workflow
- description: List a course's modules with items, then grade a student on a module assignment.
  name: Canvas LMS Grade an Assignment From a Module
  slug: canvas-lms-list-modules-and-grade-module-assignment-workflow
- description: Validate a user, enroll them as a student, and confirm course membership.
  name: Canvas LMS Onboard Student to Course
  slug: canvas-lms-onboard-student-to-course-workflow
- description: Publish a draft assignment, then list every submission for it.
  name: Canvas LMS Publish Assignment and List Submissions
  slug: canvas-lms-publish-assignment-and-list-submissions-workflow
- description: Find a student via course section enrollments, then grade their assignment.
  name: Canvas LMS Grade a Student by Section Enrollment
  slug: canvas-lms-section-roster-and-grade-workflow
- description: Identify the authenticated teacher, pick their first taught course, and author an assignment.
  name: Canvas LMS Author in the Current User's First Course
  slug: canvas-lms-self-courses-and-create-assignment-workflow
- description: Push an assignment's due date out, then grade a student's late submission.
  name: Canvas LMS Extend Due Date Then Grade Late Submission
  slug: canvas-lms-update-assignment-due-date-and-grade-workflow
artifact_total: 82
collections:
- collection_type: postman
  name: Canvas LMS REST API
  slug: postman-canvas-lms-rest-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Canvas LMS REST Accounts API
  slug: open-canvas-lms-accounts-api
- collection_type: open
  name: Canvas LMS REST Accounts Assignments API
  slug: open-canvas-lms-assignments-api
- collection_type: open
  name: Canvas LMS REST Accounts Courses API
  slug: open-canvas-lms-courses-api
- collection_type: open
  name: Canvas LMS REST Accounts Discussions API
  slug: open-canvas-lms-discussions-api
- collection_type: open
  name: Canvas LMS REST Accounts Enrollments API
  slug: open-canvas-lms-enrollments-api
- collection_type: open
  name: Canvas LMS REST Accounts Files API
  slug: open-canvas-lms-files-api
- collection_type: open
  name: Canvas LMS Live Events
  slug: open-canvas-lms-live-events-asyncapi
- collection_type: open
  name: Canvas LMS REST Accounts Modules API
  slug: open-canvas-lms-modules-api
- collection_type: open
  name: Canvas LMS REST Accounts Outcomes API
  slug: open-canvas-lms-outcomes-api
- collection_type: open
  name: Canvas LMS REST API
  slug: open-canvas-lms-rest-api
- collection_type: open
  name: Canvas LMS REST Accounts Submissions API
  slug: open-canvas-lms-submissions-api
- collection_type: open
  name: Canvas LMS REST Accounts Users API
  slug: open-canvas-lms-users-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/canvas-lms-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/canvas-lms-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/canvas-lms-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/canvas-lms-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/canvas-lms-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/canvas-lms-scopes.yml
- group: build
  title: ''
  type: Packages
  url: packages/canvas-lms-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/canvas-lms-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/canvas-lms-security.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/canvas-lms-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/canvas-lms-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/canvas-lms-rest-api-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/canvas-lms-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/canvas-lms-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/canvas-lms-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/canvas-lms-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/canvas-lms-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/canvas-lms-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/canvas-lms-cli.yml
- group: design
  title: ''
  type: Components
  url: components/canvas-lms-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/canvas-lms-data-model.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/canvas-lms/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/canvas-lms-account-course-audit-and-conclude-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/canvas-lms-assign-and-grade-discussion-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/canvas-lms-conclude-course-with-grade-check-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/canvas-lms-copy-assignment-to-course-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/canvas-lms-create-assignment-and-confirm-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/canvas-lms-create-assignment-and-grade-submission-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/canvas-lms-create-course-shell-then-author-assignment-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/canvas-lms-enroll-teacher-then-author-assignment-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/canvas-lms-enroll-user-and-confirm-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/canvas-lms-excuse-or-grade-submission-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/canvas-lms-find-or-create-assignment-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/canvas-lms-grade-all-submissions-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/canvas-lms-list-modules-and-grade-module-assignment-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/canvas-lms-onboard-student-to-course-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/canvas-lms-publish-assignment-and-list-submissions-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/canvas-lms-section-roster-and-grade-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/canvas-lms-self-courses-and-create-assignment-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/canvas-lms-update-assignment-due-date-and-grade-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://www.instructure.com
- group: start
  title: ''
  type: Portal
  url: https://www.instructure.com/canvas
- group: start
  title: ''
  type: Signup
  url: https://canvas.instructure.com/
- group: docs
  title: ''
  type: Documentation
  url: https://canvas.instructure.com/doc/api/
- group: docs
  title: ''
  type: Documentation
  url: https://canvas.instructure.com/doc/api/all_resources.html
- group: operate
  title: ''
  type: ChangeLog
  url: https://canvas.instructure.com/doc/api/file.changelog.html
- group: docs
  title: ''
  type: Documentation
  url: https://canvas.instructure.com/doc/api/file.graphql.html
- group: auth
  title: ''
  type: Authentication
  url: https://canvas.instructure.com/doc/api/file.oauth.html
- group: operate
  title: ''
  type: RateLimits
  url: https://canvas.instructure.com/doc/api/file.throttling.html
- group: design
  title: ''
  type: Pagination
  url: https://canvas.instructure.com/doc/api/file.pagination.html
- group: docs
  title: ''
  type: Documentation
  url: https://canvas.instructure.com/doc/api/file.tools_intro.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.instructure.com/policies/api-policy
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.instructure.com/policies
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.instructure.com/policies/product-privacy-notice
- group: operate
  title: ''
  type: StatusPage
  url: https://status.instructure.com/
- group: operate
  title: ''
  type: Forums
  url: https://community.canvaslms.com/
- group: operate
  title: ''
  type: Forums
  url: https://community.canvaslms.com/t5/Canvas-Developers-Group/gh-p/canvas-developers
- group: company
  title: ''
  type: Blog
  url: https://www.instructure.com/blog
- group: start
  title: ''
  type: Portal
  url: https://www.instructure.com/canvas/canvas-credentials
- group: start
  title: ''
  type: Portal
  url: https://www.instructure.com/canvas/canvas-studio
- group: start
  title: ''
  type: Portal
  url: https://www.instructure.com/canvas/canvas-catalog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/instructure
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/instructure/canvas-lms
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/instructure/canvas-lms/wiki
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/instructure/canvas-lms/wiki/Quick-Start
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/instructure/canvas-lms/wiki/Production-Start
- group: build
  title: ''
  type: Tools
  url: https://github.com/instructure/canvas-self-hosted
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/instructure/canvas-ios
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/instructure/canvas-android
- group: build
  title: ''
  type: SDKs
  url: https://github.com/instructure/CanvasAPI
- group: build
  title: ''
  type: SDKs
  url: https://github.com/instructure/pandarus
- group: build
  title: ''
  type: SDKs
  url: https://github.com/instructure/canvas_oauth_engine
- group: build
  title: ''
  type: SDKs
  url: https://github.com/instructure/dap-client-py
- group: build
  title: ''
  type: Tools
  url: https://github.com/instructure/canvas-data-loader
- group: build
  title: ''
  type: Tools
  url: https://github.com/instructure/canvas-data-cli
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/instructure/canvas-studio-api-examples
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/instructure/canvas-rce-api
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/instructure/canvas-hosted-data-examples
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/instructure/lti_example
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/instructure/lti1_tool_provider_example
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/instructure/lti_tool_provider_example
- group: build
  title: ''
  type: SDKs
  url: https://github.com/instructure/ims-lti
- group: build
  title: ''
  type: SDKs
  url: https://github.com/instructure/basiclti-util-java
- group: build
  title: ''
  type: Tools
  url: https://github.com/instructure/qti
- group: build
  title: ''
  type: Tools
  url: https://github.com/instructure/QTIMigrationTool
- group: build
  title: ''
  type: Tools
  url: https://github.com/instructure/moodle2cc
- group: build
  title: ''
  type: Tools
  url: https://github.com/instructure/common-cartridge-viewer
- group: build
  title: ''
  type: Tools
  url: https://github.com/instructure/analytics
- group: build
  title: ''
  type: Tools
  url: https://github.com/instructure/instructure-ui
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/instructure/canvas-alexa-lambda
- group: build
  title: ''
  type: Tools
  url: https://github.com/instructure/canvas_connect
- group: other
  title: ''
  type: Marketplace
  url: https://www.instructure.com/canvas/partners
- group: other
  title: ''
  type: Marketplace
  url: https://www.eduappcenter.com/
- group: start
  title: ''
  type: Portal
  url: https://www.instructure.com/canvas/higher-education
- group: start
  title: ''
  type: Portal
  url: https://www.instructure.com/canvas/k-12
- group: start
  title: ''
  type: Portal
  url: https://www.instructure.com/canvas/business
- group: start
  title: ''
  type: Portal
  url: https://www.instructure.com/canvas/government
- group: commercial
  title: ''
  type: Plans
  url: plans/canvas-lms-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/canvas-lms-rate-limits.yml
created: '2026-05-25T00:00:00.000Z'
description: Canvas is the open, AGPLv3-licensed learning management system created and maintained by Instructure, Inc. and used by more than 30 million students, teachers, and administrators across higher education, K-12, business, and government. Canvas exposes a deep REST API (190+ resource groups covering Accounts, Courses, Enrollments, Assignments, Submissions, Grades, Outcomes, Quizzes, Rubrics, Modules, Pages, Discussions, Files, Conversations, Calendar Events, SIS Import, Authentication Providers, Developer Keys, External Tools, AI Conversations, AI Experiences, Analytics, Audit Logs, and more), a GraphQL API at /api/graphql, IMS LTI 1.3 / LTI Advantage services (Names and Role Provisioning, Line Items, Score, Result, Deep Linking), a Platform Notification Service for server-to-server webhook delivery, and the Data Access Platform (DAP / Canvas Data 2) for warehouse-scale event and snapshot data export. Canvas is the same software that powers canvas.instructure.com (Free for Teacher),
  Canvas Cloud for institutions, and self-hosted deployments.
features:
- Open-source AGPLv3 LMS by Instructure with 6,600+ GitHub stars and 30M+ users worldwide
- REST API with 190+ resource groups covering the full LMS surface — courses, users, enrollments, assignments, submissions, grades, outcomes, quizzes, modules, pages, discussions, files, conversations, calendar events, audit logs, AI conversations, AI experiences, and more
- GraphQL API at /api/graphql with hosted GraphiQL explorer at /graphiql
- OAuth2 (RFC 6749) authentication with developer-key-issued client credentials, manual personal access tokens for testing, and the as_user_id masquerading parameter for admin act-as flows
- Full IMS LTI 1.3 / LTI Advantage implementation — Deep Linking 2.0, Names and Role Provisioning, Assignment & Grade Services (Line Items, Score, Result), Dynamic Registration, JWK key exchange
- Platform Notification Service (PNS) for server-to-server webhook delivery to LTI tools
- Plagiarism Detection Platform with webhook subscriptions, originality reports, and plagiarism-platform users/assignments
- SIS Import API with the canonical Canvas SIS CSV format covering accounts, terms, courses, sections, users, enrollments, groups, group memberships, cross-listings, logins, admins
- Data Access Platform (DAP / Canvas Data 2) for warehouse-scale snapshot + incremental table and event exports via the api-gateway.instructure.com/dap endpoint
- Built-in OpenAPI 3.0 generator via the `rake doc:openapi` task using swagger_yard
- Pagination using RFC 5988 Link headers; per_page query parameter; supports `last`, `next`, `prev`, and `first` link rels
- Per-user-per-host throttling with X-Request-Cost and X-Rate-Limit-Remaining response headers
- Compound documents and includes[] query parameter for relationship hydration
- File Upload API with multipart POST-then-PUT flow for direct-to-S3 uploads
- Audit log APIs for Authentications, Course changes, and Grade Changes
- Canvas Studio (video), Canvas Catalog (course discovery + commerce), Canvas Credentials (digital credentials via Parchment), and Canvas Career Experiences
- Cross-platform mobile apps for Students, Teachers, Parents (canvas-ios + canvas-android repos)
- Common Cartridge import/export, QTI 1.x/2.x quiz interchange, Moodle migration
- Self-hosted via Docker (canvas-self-hosted) or hosted as Canvas Cloud (Canvas Free for Teacher, Canvas LMS for institutions)
- Owned by Instructure, Inc. (KKR portfolio company since 2024); Steve Daly, CEO
graphqls:
- description: Canvas exposes a GraphQL endpoint at `/api/graphql` that provides access to the Canvas object graph. The API supports queries and mutations for courses, users, enrollments, assignments, submissions, m
  name: Canvas LMS GraphQL API
  slug: canvas-lms-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/canvas-lms.png
json_schemas:
- name: Canvas LMS Assignment
  property_count: 42
  slug: canvas-lms-assignment
- name: Canvas LMS Course
  property_count: 39
  slug: canvas-lms-course
jsonld:
- class_count: 34
  name: Canvas Lms Context
  property_count: 16
  slug: canvas-lms-context
layout: provider
mcp_servers:
- description: 'Instructure does not publish an official hosted or remote MCP server for Canvas (searched: docs, npm @modelcontextprotocol, MCP registries — July 2026). A healthy community ecosystem of Canvas MCP ser'
  name: Canvas LMS MCP Server
  slug: canvas-lms-mcp-server
modified: '2026-06-20'
name: Canvas LMS
nav: Providers
network: true
overview: 'Canvas LMS publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Canvas Live Events, Accounts API, Assignments API, and 8 more. Tagged areas include Learning Management, Education, EdTech, LMS, and LTI.


  The Canvas LMS catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Canvas LMS''s developer surface includes authentication, sandbox, changelog, CLI, developer portal, signup flow, documentation, and 92 more developer resources.'
plans:
- name: Canvas Lms Plans Pricing
  plan_count: 6
  slug: canvas-lms-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 3
  name: Canvas Lms Rate Limits
  slug: canvas-lms-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Canvas LMS API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: canvas-lms-jsonschema-spectral-rules
scopes:
- name: Canvas Lms Scopes
  scope_count: 3
  slug: canvas-lms-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: exemplar
  composite: 76.2
  delta: 0.0
  facets:
    access_clarity: 73.7
    commercial_clarity: 73.7
    contract_governance: 26.5
    contract_quality: 67.0
    developer_ergonomics: 85.7
    discoverability: 68.5
    governance: 26.5
    operational_transparency: 68.4
  previous_composite: 76.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 85.2
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/canvas-lms/refs/heads/main/screenshots/canvas-lms-2026-06-20T173931.png
security:
- kind: authentication
  name: Canvas Lms Authentication
  slug: canvas-lms-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Canvas Lms Domain Security
  slug: canvas-lms-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Canvas Lms Vulnerability Disclosure
  slug: canvas-lms-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Canvas Lms Trust Center
  slug: canvas-lms-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, PCI DSS, HIPAA, FedRAMP, GDPR, CSA STAR
slug: canvas-lms
tags:
- Learning Management
- Education
- EdTech
- LMS
- LTI
- Higher Education
- K-12
- Open-Source
- AGPL
- Canvas
website: https://www.instructure.com
---
