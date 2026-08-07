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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 47.7
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Perforce Agentic Access
  operation_count: 27
  slug: perforce-agentic-access
  summary_line: 27 operations · 15 acting
api_count: 14
apis:
- description: Technology Preview REST API introduced with P4 Server 2025.2, providing a new way to automate workflows and integrate P4 with other tools via standard HTTP endpoints for server info, depots, files, an
  name: Perforce P4 REST API
  slug: perforce-p4-rest-api
- description: API for Hansoft agile project management, providing access to project planning, tracking, and reporting capabilities.
  name: Perforce Hansoft API
  slug: perforce-hansoft-api
- description: GraphQL and REST API for P4 Plan (formerly Hansoft) agile project management, supporting queries, mutations, and real-time subscriptions for planning views, sprints, tasks, and user management.
  name: Perforce P4 Plan API
  slug: perforce-p4-plan-api
- description: REST API for Helix ALM application lifecycle management platform, enabling automation of tasks and development of integrations for requirements management, issue tracking, and test case management.
  name: Perforce Helix ALM REST API
  slug: perforce-helix-alm-rest-api
- description: 'REST API for Helix TeamHub source code repository management platform, providing access to repositories, projects, users, and company resources across Git, Mercurial, Subversion, and other repository '
  name: Perforce Helix TeamHub API
  slug: perforce-helix-teamhub-api
- description: REST API for P4 DAM (Digital Asset Management), enabling integration with digital asset workflows for finding, reviewing, sharing, and managing versioned assets stored in Helix Core.
  name: Perforce P4 DAM REST API
  slug: perforce-p4-dam-rest-api
- description: REST API for P4 Search, providing indexing and search capabilities across Helix Core servers to support code review, file content search, and changelist description search.
  name: Perforce P4 Search API
  slug: perforce-p4-search-api
- description: REST API for the Helix Authentication Service, a Node.js based authentication protocol integration service supporting OpenID Connect and SAML 2.0 for authenticating users across Perforce products.
  name: Perforce Helix Authentication Service API
  slug: perforce-helix-authentication-service-api
- description: Endpoints for viewing and creating activity stream entries.
  name: Perforce Activity API
  slug: perforce-activity-api
- description: Endpoints for inspecting changelists and their relationships.
  name: Perforce Changes API
  slug: perforce-changes-api
- description: Endpoints for managing review and changelist comments.
  name: Perforce Comments API
  slug: perforce-comments-api
- description: Endpoints for managing Swarm projects.
  name: Perforce Projects API
  slug: perforce-projects-api
- description: Endpoints for managing code reviews.
  name: Perforce Reviews API
  slug: perforce-reviews-api
- description: Endpoints for retrieving Swarm server version information.
  name: Perforce Version API
  slug: perforce-version-api
artifact_total: 91
collections:
- collection_type: postman
  name: Perforce Helix Swarm Activity API
  slug: postman-perforce-activity-api
- collection_type: postman
  name: Perforce Helix Swarm Activity Changes API
  slug: postman-perforce-changes-api
- collection_type: postman
  name: Perforce Helix Swarm Activity Comments API
  slug: postman-perforce-comments-api
- collection_type: postman
  name: Perforce Helix Swarm Activity Projects API
  slug: postman-perforce-projects-api
- collection_type: postman
  name: Perforce Helix Swarm Activity Reviews API
  slug: postman-perforce-reviews-api
- collection_type: postman
  name: Perforce Helix Swarm Activity Version API
  slug: postman-perforce-version-api
- collection_type: open
  name: Perforce Helix Swarm API
  slug: open-perforce-helix-swarm
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/perforce/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/perforce-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/perforce-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/perforce-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/perforce
- group: start
  title: ''
  type: Portal
  url: https://www.perforce.com/support/developers
- group: start
  title: ''
  type: GettingStarted
  url: https://www.perforce.com/support/self-service-resources
- group: docs
  title: ''
  type: Documentation
  url: https://www.perforce.com/support/self-service-resources/documentation
- group: company
  title: ''
  type: Blog
  url: https://www.perforce.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.perforce.com/support
- group: operate
  title: ''
  type: StatusPage
  url: https://status.perforce.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/perforce
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.perforce.com/terms-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.perforce.com/privacy-policy
- group: operate
  title: ''
  type: Contact
  url: https://www.perforce.com/contact-us
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/perforce/p4mcp-server
created: '2024-01-01'
description: Perforce Software provides enterprise-scale development tools, including version control, application lifecycle management, agile planning, and static analysis solutions for development teams.
examples:
- key_count: 6
  name: Perforce Addchangetoreview Example
  slug: perforce-addchangetoreview-example
- key_count: 6
  name: Perforce Archiveinactivereviews Example
  slug: perforce-archiveinactivereviews-example
- key_count: 6
  name: Perforce Checkchange Example
  slug: perforce-checkchange-example
- key_count: 6
  name: Perforce Cleanupreview Example
  slug: perforce-cleanupreview-example
- key_count: 6
  name: Perforce Createactivity Example
  slug: perforce-createactivity-example
- key_count: 6
  name: Perforce Createcomment Example
  slug: perforce-createcomment-example
- key_count: 6
  name: Perforce Createproject Example
  slug: perforce-createproject-example
- key_count: 6
  name: Perforce Createreview Example
  slug: perforce-createreview-example
- key_count: 6
  name: Perforce Deleteproject Example
  slug: perforce-deleteproject-example
- key_count: 6
  name: Perforce Editcomment Example
  slug: perforce-editcomment-example
- key_count: 6
  name: Perforce Getactiondashboard Example
  slug: perforce-getactiondashboard-example
- key_count: 6
  name: Perforce Getchangeaffectsprojects Example
  slug: perforce-getchangeaffectsprojects-example
- key_count: 6
  name: Perforce Getchangedefaultreviewers Example
  slug: perforce-getchangedefaultreviewers-example
- key_count: 6
  name: Perforce Getproject Example
  slug: perforce-getproject-example
- key_count: 6
  name: Perforce Getreview Example
  slug: perforce-getreview-example
- key_count: 6
  name: Perforce Getreviewtransitions Example
  slug: perforce-getreviewtransitions-example
- key_count: 6
  name: Perforce Getversion Example
  slug: perforce-getversion-example
- key_count: 11
  name: Perforce Helix Swarm Activity Example
  slug: perforce-helix-swarm-activity-example
- key_count: 12
  name: Perforce Helix Swarm Comment Example
  slug: perforce-helix-swarm-comment-example
- key_count: 18
  name: Perforce Helix Swarm Project Example
  slug: perforce-helix-swarm-project-example
- key_count: 22
  name: Perforce Helix Swarm Review Example
  slug: perforce-helix-swarm-review-example
- key_count: 6
  name: Perforce Listactivity Example
  slug: perforce-listactivity-example
- key_count: 6
  name: Perforce Listcomments Example
  slug: perforce-listcomments-example
- key_count: 6
  name: Perforce Listprojects Example
  slug: perforce-listprojects-example
- key_count: 6
  name: Perforce Listreviews Example
  slug: perforce-listreviews-example
- key_count: 6
  name: Perforce Obliteratereview Example
  slug: perforce-obliteratereview-example
- key_count: 6
  name: Perforce Sendcommentnotification Example
  slug: perforce-sendcommentnotification-example
- key_count: 6
  name: Perforce Setreviewvote Example
  slug: perforce-setreviewvote-example
- key_count: 6
  name: Perforce Transitionreviewstate Example
  slug: perforce-transitionreviewstate-example
- key_count: 6
  name: Perforce Updateproject Example
  slug: perforce-updateproject-example
- key_count: 6
  name: Perforce Updatereview Example
  slug: perforce-updatereview-example
features:
- description: Collaborative code review workflows with Helix Swarm supporting inline comments, voting, tasks, and approval gates.
  name: Code Review
- description: Enterprise-scale version control with Helix Core supporting large binary files, distributed development, and atomic changelists.
  name: Version Control
- description: Versioned digital asset workflows with P4 DAM for reviewing, sharing, and managing creative assets stored in Helix Core.
  name: Digital Asset Management
- description: End-to-end ALM with Helix ALM for requirements traceability, issue tracking, and test case management.
  name: Application Lifecycle Management
- description: Agile project management with P4 Plan supporting sprints, backlogs, Gantt charts, and resource planning.
  name: Agile Planning
- description: Single sign-on across Perforce products with Helix Authentication Service supporting OpenID Connect and SAML 2.0.
  name: Authentication Services
finops:
- name: Perforce Finops
  service_category: Developer Tools
  slug: perforce-finops
graphqls:
- description: GraphQL and REST API for P4 Plan (formerly Hansoft) agile project management, supporting queries, mutations, and real-time subscriptions for planning views, sprints, tasks, and user management.
  name: Perforce GraphQL API
  slug: perforce-graphql
image: https://www.perforce.com/sites/default/files/perforce-logo.png
integrations:
- description: Trigger builds and report results through Helix Core and Swarm integration plugins for Jenkins CI/CD.
  name: Jenkins
- description: Native Visual Studio integration with P4VS plugin for source control operations from within the IDE.
  name: Visual Studio
- description: Helix Core plugin for Unity game engine enabling version control of game projects directly within the editor.
  name: Unity
- description: Native Helix Core integration with Unreal Engine for versioning game assets and source code.
  name: Unreal Engine
json_schemas:
- name: Activity
  property_count: 11
  slug: perforce-activity
- name: Comment
  property_count: 12
  slug: perforce-comment
- name: Activity
  property_count: 11
  slug: perforce-helix-swarm-activity
- name: Comment
  property_count: 12
  slug: perforce-helix-swarm-comment
- name: Project
  property_count: 18
  slug: perforce-helix-swarm-project
- name: Review
  property_count: 22
  slug: perforce-helix-swarm-review
- name: Project
  property_count: 18
  slug: perforce-project
- name: Perforce Helix Swarm Review
  property_count: 22
  slug: perforce-review
json_structures:
- name: Perforce Helix Swarm Activity Structure
  property_count: 11
  slug: perforce-helix-swarm-activity-structure
- name: Perforce Helix Swarm Comment Structure
  property_count: 12
  slug: perforce-helix-swarm-comment-structure
- name: Perforce Helix Swarm Project Structure
  property_count: 18
  slug: perforce-helix-swarm-project-structure
- name: Perforce Helix Swarm Review Structure
  property_count: 22
  slug: perforce-helix-swarm-review-structure
- name: Perforce Structure
  property_count: 0
  slug: perforce-structure
jsonld:
- class_count: 0
  name: Perforce Context
  property_count: 9
  slug: perforce-context
- class_count: 0
  name: Perforce Helix Swarm Context
  property_count: 0
  slug: perforce-helix-swarm-context
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: Perforce
nav: Providers
network: true
overview: 'Perforce publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Activity API, Changes API, Comments API, and 3 more.


  The Perforce catalog on APIs.io includes 2 JSON-LD contexts and 2 Spectral governance rulesets.


  Perforce''s developer surface includes authentication, developer portal, getting-started guide, documentation, engineering blog, support, and 10 more developer resources.'
plans:
- name: Perforce Plans Pricing
  plan_count: 5
  slug: perforce-plans-pricing
random_paper: 63
rate_limits:
- limit_count: 2
  name: Perforce Rate Limits
  slug: perforce-rate-limits
rules:
- name: Perforce API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: perforce-jsonschema-spectral-rules
- name: Perforce API Rules
  rule_count: 14
  severity_counts:
    error: 7
    hint: 0
    info: 2
    warn: 5
  slug: perforce-spectral-rules
score:
  band: strong
  composite: 60.7
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 72.4
    developer_ergonomics: 58.7
    discoverability: 63.0
    governance: 58.3
    operational_transparency: 42.1
  previous_composite: 60.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/perforce/refs/heads/main/screenshots/perforce-2026-06-20T191608.png
security:
- kind: authentication
  name: Perforce Authentication
  slug: perforce-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Perforce Domain Security
  slug: perforce-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: perforce
use_cases:
- description: Manage large game assets and source code with Helix Core providing fast file transfers and atomic changelists for game studios.
  name: Game Development
- description: Version control for chip design files with support for large binary IP blocks and strict access controls.
  name: Semiconductor Design
- description: Manage safety-critical automotive software with full traceability from requirements through testing using Helix ALM.
  name: Automotive Software
- description: Automate CI/CD pipelines with Helix Core triggers, Swarm review gates, and REST API integrations.
  name: DevOps Automation
website: https://www.perforce.com/support/developers
---
