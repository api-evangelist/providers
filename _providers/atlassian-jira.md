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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Atlassian Jira Agentic Access
  operation_count: 15
  slug: atlassian-jira-agentic-access
  summary_line: 15 operations · 7 acting
api_count: 8
apis:
- description: Read Jira field metadata.
  name: Atlassian Jira Fields API
  slug: atlassian-jira-fields-api
- description: Manage comments on issues.
  name: Atlassian Jira Issue Comments API
  slug: atlassian-jira-issue-comments-api
- description: Search issues using JQL.
  name: Atlassian Jira Issue Search API
  slug: atlassian-jira-issue-search-api
- description: List and perform workflow transitions.
  name: Atlassian Jira Issue Transitions API
  slug: atlassian-jira-issue-transitions-api
- description: Manage worklogs on issues.
  name: Atlassian Jira Issue Worklogs API
  slug: atlassian-jira-issue-worklogs-api
- description: Create, read, update and delete Jira issues.
  name: Atlassian Jira Issues API
  slug: atlassian-jira-issues-api
- description: Manage Jira projects.
  name: Atlassian Jira Projects API
  slug: atlassian-jira-projects-api
- description: Read user information.
  name: Atlassian Jira Users API
  slug: atlassian-jira-users-api
artifact_total: 38
collections:
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
  url: https://www.linkedin.com/showcase/atlassian-jira
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
modified: '2026-04-19'
name: Atlassian Jira
nav: Providers
network: true
overview: 'Atlassian Jira publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Fields API, Issue Comments API, Issue Search API, and 5 more. Tagged areas include Agile, Atlassian, Bug Tracking, Issue Tracking, and ITSM.


  Atlassian Jira''s developer surface includes authentication, documentation, getting-started guide, pricing, support, engineering blog, and 14 more developer resources.'
plans:
- name: Atlassian Jira Plans Pricing
  plan_count: 3
  slug: atlassian-jira-plans-pricing
random_paper: 50
rate_limits:
- limit_count: 5
  name: Atlassian Jira Rate Limits
  slug: atlassian-jira-rate-limits
scopes:
- name: Atlassian Jira Scopes
  scope_count: 4
  slug: atlassian-jira-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: developing
  composite: 49.7
  delta: -3.1
  facets:
    commercial_clarity: 78.9
    contract_quality: 49.2
    developer_ergonomics: 37.0
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 52.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
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
