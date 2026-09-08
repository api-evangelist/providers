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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 47.1
  scored_at: '2026-09-07'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Atlassian Jira Agentic Access
  operation_count: 15
  slug: atlassian-jira-agentic-access
  summary_line: 15 operations · 7 acting
api_count: 4
apis:
- baseURL: https://your-domain.atlassian.net/rest/api/3
  baseurl_source: declared
  description: Read Jira field metadata.
  name: Atlassian Jira Fields API
  slug: atlassian-jira-fields-api
- baseURL: https://your-domain.atlassian.net/rest/api/3
  baseurl_source: declared
  description: Manage comments on issues.
  name: Atlassian Jira Issue Comments API
  slug: atlassian-jira-issue-comments-api
- baseURL: https://your-domain.atlassian.net/rest/api/3
  baseurl_source: declared
  description: Search issues using JQL.
  name: Atlassian Jira Issue Search API
  slug: atlassian-jira-issue-search-api
- baseURL: https://your-domain.atlassian.net/rest/api/3
  baseurl_source: declared
  description: List and perform workflow transitions.
  name: Atlassian Jira Issue Transitions API
  slug: atlassian-jira-issue-transitions-api
- baseURL: https://your-domain.atlassian.net/rest/api/3
  baseurl_source: declared
  description: Manage worklogs on issues.
  name: Atlassian Jira Issue Worklogs API
  slug: atlassian-jira-issue-worklogs-api
- baseURL: https://your-domain.atlassian.net/rest/api/3
  baseurl_source: declared
  description: Create, read, update and delete Jira issues.
  name: Atlassian Jira Issues API
  slug: atlassian-jira-issues-api
- baseURL: https://your-domain.atlassian.net/rest/api/3
  baseurl_source: declared
  description: Manage Jira projects.
  name: Atlassian Jira Projects API
  slug: atlassian-jira-projects-api
- baseURL: https://your-domain.atlassian.net/rest/api/3
  baseurl_source: declared
  description: Read user information.
  name: Atlassian Jira Users API
  slug: atlassian-jira-users-api
- baseURL: https://your-domain.atlassian.net
  baseurl_source: declared
  description: The complete first-party Jira Cloud platform REST API — 617 operations across 421 paths covering issues, projects, users, workflows, fields, screens, permissions, dashboards, filters, webhooks and adm
  name: Atlassian Jira Cloud Platform REST API v3
  slug: atlassian-jira-cloud-platform-api
- baseURL: https://your-domain.atlassian.net
  baseurl_source: declared
  description: The first-party Jira Software (Agile) REST API at /rest/agile/1.0 — 105 operations covering boards, sprints, epics, backlogs, versions, and the development-information surface for builds, deployments,
  name: Jira Software Cloud API
  slug: atlassian-jira-software-cloud-api
- baseURL: https://your-domain.atlassian.net
  baseurl_source: declared
  description: The first-party Jira Service Management REST API at /rest/servicedeskapi — 75 operations covering service desks, customer requests, request types, queues, SLAs, organizations, customers and the knowle
  name: Jira Service Management REST API
  slug: atlassian-jira-service-management-api
- description: Atlassian's official hosted Model Context Protocol server. An OAuth 2.1 protected endpoint that exposes Jira, Jira Service Management, Confluence, Bitbucket, Compass and Loom to MCP-capable AI clients
  name: Atlassian Remote MCP Server
  slug: atlassian-jira-remote-mcp-server
artifact_total: 53
asyncapis:
- description: ''
  name: Atlassian Jira Webhooks
  slug: atlassian-jira-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Atlassian Jira Cloud Platform REST API v3 Fields API
  slug: open-atlassian-jira-fields-api
- collection_type: open
  name: Atlassian Jira Cloud Platform REST API v3 Fields Issue Comments API
  slug: open-atlassian-jira-issue-comments-api
- collection_type: open
  name: Atlassian Jira Cloud Platform REST API v3 Fields Issue Search API
  slug: open-atlassian-jira-issue-search-api
- collection_type: open
  name: Atlassian Jira Cloud Platform REST API v3 Fields Issue Transitions API
  slug: open-atlassian-jira-issue-transitions-api
- collection_type: open
  name: Atlassian Jira Cloud Platform REST API v3 Fields Issue Worklogs API
  slug: open-atlassian-jira-issue-worklogs-api
- collection_type: open
  name: Atlassian Jira Cloud Platform REST API v3 Fields Issues API
  slug: open-atlassian-jira-issues-api
- collection_type: open
  name: Atlassian Jira Cloud Platform REST API v3 Fields Projects API
  slug: open-atlassian-jira-projects-api
- collection_type: open
  name: Atlassian Jira Cloud Platform REST API v3 Fields Users API
  slug: open-atlassian-jira-users-api
- collection_type: open
  name: Atlassian Jira Cloud Platform REST API v3
  slug: open-atlassian-jira
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/atlassian-jira-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/atlassian-jira-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/atlassian-jira-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/atlassian-jira-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/atlassian-jira-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/atlassian-jira-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/atlassian
- group: company
  title: ''
  type: Website
  url: https://www.atlassian.com/software/jira
- group: docs
  title: ''
  type: Documentation
  url: https://developer.atlassian.com/cloud/jira/platform/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.atlassian.com/cloud/jira/platform/getting-started/
- group: auth
  title: ''
  type: Authentication
  url: https://developer.atlassian.com/cloud/jira/platform/oauth-2-3lo-apps/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.atlassian.com/software/jira/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.atlassian.com/
- group: operate
  title: ''
  type: Support
  url: https://support.atlassian.com/
- group: operate
  title: ''
  type: Community
  url: https://community.developer.atlassian.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.atlassian.com/legal/cloud-terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.atlassian.com/legal/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/atlassian
- group: company
  title: ''
  type: Blog
  url: https://developer.atlassian.com/blog/
- group: operate
  title: ''
  type: RateLimits
  url: https://developer.atlassian.com/cloud/jira/platform/rate-limiting/
- group: build
  title: ''
  type: Packages
  url: packages/atlassian-jira-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/atlassian-jira-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/atlassian-jira-cli.yml
- group: design
  title: ''
  type: Components
  url: components/atlassian-jira-components.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/atlassian-jira-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/atlassian-jira-security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/atlassian-jira-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/atlassian-jira-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/atlassian-jira-tool-crosswalk.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/atlassian-jira-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.atlassian.com/trust/compliance
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/atlassian-jira-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/atlassian-jira-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://developer.atlassian.com/platform/marketplace/atlassian-rest-api-policy/
- group: design
  title: ''
  type: Conventions
  url: conventions/atlassian-jira-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/atlassian-jira-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/atlassian-jira-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/atlassian-jira-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/atlassian-jira-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/atlassian-jira-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/atlassian-jira-rate-limits.yml
- group: auth
  title: ''
  type: Security
  url: security/atlassian-jira-vulnerability-disclosure.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.atlassian.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issues/
- group: operate
  title: ''
  type: Roadmap
  url: https://www.atlassian.com/roadmap/cloud
- group: start
  title: ''
  type: SignUp
  url: https://www.atlassian.com/try/cloud/signup?bundle=jira-software
- group: operate
  title: ''
  type: HelpCenter
  url: https://community.atlassian.com/
- group: auth
  title: ''
  type: Trust
  url: https://www.atlassian.com/trust
- group: auth
  title: ''
  type: BugBounty
  url: https://bugcrowd.com/atlassian
- group: other
  title: ''
  type: Marketplace
  url: https://marketplace.atlassian.com/
- group: build
  title: ''
  type: PostmanCollection
  url: collections/atlassian-jira.postman_collection.json
- group: build
  title: ''
  type: OpenCollection
  url: collections/atlassian-jira.opencollection.json
- group: commercial
  title: ''
  type: FinOps
  url: finops/atlassian-jira-finops.yml
created: '2024-01-01'
description: Jira is a leading issue tracking and project management platform developed by Atlassian. It provides REST APIs for Jira Cloud Platform, Jira Software, and Jira Service Management enabling programmatic management of issues, projects, workflows, boards, sprints, users, and service desk requests with OAuth 2.0 authentication.
features:
- description: Create, update, transition, and delete Jira issues with full support for custom fields, attachments, comments, and workflow transitions.
  name: Issue Management
- description: Manage Jira projects including project categories, components, versions, and project-level configurations.
  name: Project Management
- description: Create and manage Scrum boards, sprints, and Kanban boards for agile project planning and execution.
  name: Board and Sprint Management
- description: Manage service desk projects, request types, queues, and SLA data for IT service management workflows.
  name: Service Desk
- description: Programmatically configure Jira workflows, statuses, transitions, and screen configurations.
  name: Workflow Configuration
- description: Build Jira apps using the Atlassian Forge platform with serverless functions and UI modules.
  name: Forge App Development
finops:
- name: Atlassian Jira Finops
  service_category: API
  slug: atlassian-jira-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/atlassian-jira.png
integrations:
- description: Link Jira projects and issues to Confluence spaces and pages for integrated project documentation.
  name: Confluence
- description: Connect Bitbucket repositories to Jira for branch, commit, and pull request linking.
  name: Bitbucket
- description: Integrate GitHub with Jira via the GitHub for Jira app for development activity tracking.
  name: GitHub
- description: Receive Jira issue notifications and create issues directly from Slack using the Jira for Slack app.
  name: Slack
- description: Connect Jenkins build and deployment events to Jira issues via the Atlassian Jenkins plugin.
  name: Jenkins
- description: Create Jira issues automatically from PagerDuty incidents for integrated incident management.
  name: PagerDuty
layout: provider
mcp_servers:
- description: ''
  name: Atlassian Remote MCP Server (Rovo MCP Server)
  slug: atlassian-remote-mcp-server-rovo-mcp-server
modified: '2026-09-06'
name: Atlassian Jira
nav: Providers
network: true
overview: 'Atlassian Jira publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Fields API, Issue Comments API, Issue Search API, and 8 more. Tagged areas include Agile, Atlassian, Bug Tracking, Issue Tracking, and ITSM.


  The Atlassian Jira catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Atlassian Jira''s developer surface includes authentication, documentation, getting-started guide, pricing, support, engineering blog, CLI, and 47 more developer resources.'
plans:
- name: Atlassian Jira Plans Pricing
  plan_count: 4
  slug: atlassian-jira-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 9
  name: Atlassian Jira Rate Limits
  slug: atlassian-jira-rate-limits
scopes:
- name: Atlassian Jira Scopes
  scope_count: 281
  slug: atlassian-jira-scopes
  summary_line: 281 scopes · authorizationCode
score:
  band: strong
  composite: 66.4
  coverage:
    artifact_dirs: 27
    catalog_earned: 67.0
    catalog_earned_first_party: 24.0
    catalog_gap: 48.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 5.4
  facets:
    access_clarity: 94.7
    commercial_clarity: 94.7
    contract_governance: 18.2
    contract_quality: 10.9
    developer_ergonomics: 81.5
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 97.4
  previous_composite: 61.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: first-party
    skills: derived
  schema_version: 0.20.0
  scored_at: '2026-09-07'
  trend: rising
  upsert:
    applies: true
    score: 61.1
screenshot: https://raw.githubusercontent.com/api-evangelist/atlassian-jira/refs/heads/main/screenshots/atlassian-jira-2026-06-20T172533.png
security:
- kind: authentication
  name: Atlassian Jira Authentication
  slug: atlassian-jira-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Atlassian Jira Domain Security
  slug: atlassian-jira-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Atlassian Jira Vulnerability Disclosure
  slug: atlassian-jira-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Atlassian Jira Trust Center
  slug: atlassian-jira-trust-center
  summary_line: FedRAMP
slug: atlassian-jira
solutions:
- description: Manage software development with Scrum and Kanban boards, sprint planning, and backlog management.
  name: Agile Project Management
- description: Provide enterprise ITSM with service catalogs, SLAs, queues, and approval workflows via Jira Service Management.
  name: IT Service Management
- description: Track any business process or workflow using customizable Jira projects and issue types for non-software teams.
  name: Business Process Tracking
tags:
- Agile
- Atlassian
- Bug Tracking
- Issue Tracking
- ITSM
- Kanban
- Project Management
- Scrum
- Service Desk
use_cases:
- description: Automate issue creation, assignment, and transitions from CI/CD pipelines, monitoring alerts, and external systems.
  name: Issue Automation
- description: Extract issue data, sprint velocity, and project metrics for custom reporting and analytics dashboards.
  name: Project Reporting
- description: Integrate Jira Service Management with external monitoring, CMDB, and ITSM tools for incident and change management.
  name: ITSM Integration
- description: Link Jira issues to commits, branches, builds, and deployments from GitHub, Bitbucket, and Jenkins.
  name: DevOps Pipeline Integration
- description: Synchronize custom field data between Jira and external systems for portfolio tracking and compliance reporting.
  name: Custom Field Automation
website: https://www.atlassian.com/software/jira
---
