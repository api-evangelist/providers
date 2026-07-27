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
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Bettercloud Agentic Access
  operation_count: 18
  slug: bettercloud-agentic-access
  summary_line: 18 operations · 9 acting
api_count: 5
apis:
- description: Query audit events and activity logs
  name: BetterCloud Events API
  slug: bettercloud-events-api
- description: Manage groups and group memberships
  name: BetterCloud Groups API
  slug: bettercloud-groups-api
- description: Manage SaaS application integrations and connections
  name: BetterCloud Integrations API
  slug: bettercloud-integrations-api
- description: Manage users across integrated SaaS applications
  name: BetterCloud Users API
  slug: bettercloud-users-api
- description: Manage automation workflows and triggers
  name: BetterCloud Workflows API
  slug: bettercloud-workflows-api
artifact_total: 104
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bettercloud-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bettercloud-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bettercloud-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bettercloud
- group: start
  title: ''
  type: Portal
  url: https://developer.bettercloud.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://support.bettercloud.com/s/article/BCCINT4000--BetterCloud-API-Overview-bc33451
- group: commercial
  title: ''
  type: Pricing
  url: https://www.bettercloud.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://www.bettercloud.com/monitor/
- group: operate
  title: ''
  type: Support
  url: https://support.bettercloud.com/s/
- group: start
  title: ''
  type: Login
  url: https://support.bettercloud.com/s/login/
- group: start
  title: ''
  type: Signup
  url: https://www.bettercloud.com/monitor/sign-up/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/BetterCloud
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/bettercloud/refs/heads/main/rules/bettercloud-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/bettercloud/refs/heads/main/vocabulary/bettercloud-vocabulary.yaml
created: '2026-03-16'
description: BetterCloud is the end-to-end SaaS management platform that enables IT teams to discover, manage, and secure the growing SaaS environment. The platform provides automated workflows, security policies, and management capabilities for SaaS applications in enterprise environments, handling billions of API calls per day across 100+ SaaS application integrations.
examples:
- key_count: 6
  name: Bettercloud Event Example
  slug: bettercloud-event-example
- key_count: 1
  name: Bettercloud Event List Response Example
  slug: bettercloud-event-list-response-example
- key_count: 3
  name: Bettercloud Group Create Request Example
  slug: bettercloud-group-create-request-example
- key_count: 7
  name: Bettercloud Group Example
  slug: bettercloud-group-example
- key_count: 1
  name: Bettercloud Group List Response Example
  slug: bettercloud-group-list-response-example
- key_count: 2
  name: Bettercloud Group Member Add Request Example
  slug: bettercloud-group-member-add-request-example
- key_count: 4
  name: Bettercloud Group Member Example
  slug: bettercloud-group-member-example
- key_count: 1
  name: Bettercloud Group Member List Response Example
  slug: bettercloud-group-member-list-response-example
- key_count: 0
  name: Bettercloud Group Member Response Example
  slug: bettercloud-group-member-response-example
- key_count: 0
  name: Bettercloud Group Response Example
  slug: bettercloud-group-response-example
- key_count: 5
  name: Bettercloud Integration Example
  slug: bettercloud-integration-example
- key_count: 1
  name: Bettercloud Integration List Response Example
  slug: bettercloud-integration-list-response-example
- key_count: 3
  name: Bettercloud Meta Response Example
  slug: bettercloud-meta-response-example
- key_count: 11
  name: Bettercloud User Example
  slug: bettercloud-user-example
- key_count: 1
  name: Bettercloud User List Response Example
  slug: bettercloud-user-list-response-example
- key_count: 0
  name: Bettercloud User Response Example
  slug: bettercloud-user-response-example
- key_count: 5
  name: Bettercloud User Update Request Example
  slug: bettercloud-user-update-request-example
- key_count: 4
  name: Bettercloud Workflow Create Request Example
  slug: bettercloud-workflow-create-request-example
- key_count: 8
  name: Bettercloud Workflow Example
  slug: bettercloud-workflow-example
- key_count: 1
  name: Bettercloud Workflow List Response Example
  slug: bettercloud-workflow-list-response-example
- key_count: 0
  name: Bettercloud Workflow Response Example
  slug: bettercloud-workflow-response-example
- key_count: 1
  name: Bettercloud Workflow Run Request Example
  slug: bettercloud-workflow-run-request-example
- key_count: 1
  name: Bettercloud Workflow Run Response Example
  slug: bettercloud-workflow-run-response-example
features:
- description: Automate user onboarding and offboarding workflows across all connected SaaS applications.
  name: User Lifecycle Management
- description: Automatically discover all SaaS applications in use across the organization.
  name: SaaS Discovery
- description: Build no-code automation workflows triggered by events, schedules, or manual action.
  name: Automated Workflows
- description: Create and enforce security policies that monitor and remediate violations across SaaS apps.
  name: Security Policy Enforcement
- description: Manage groups and memberships across Google Workspace, Azure AD, and other directory services.
  name: Group Management
- description: Comprehensive audit trail of all actions taken by users and automated workflows.
  name: Audit Logging
- description: Connect and manage 100+ enterprise SaaS applications including Google Workspace, Slack, Salesforce, and more.
  name: SaaS Integrations
- description: Track and optimize SaaS licenses to reduce spend and identify unused seats.
  name: License Management
finops:
- name: Bettercloud Finops
  service_category: API
  slug: bettercloud-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bettercloud.png
integrations:
- description: Manage Google Workspace users, groups, Drive files, and calendar access.
  name: Google Workspace
- description: Manage Slack workspace users, channels, and app connections.
  name: Slack
- description: Manage Salesforce user provisioning and deprovisioning.
  name: Salesforce
- description: Manage Microsoft 365 users, licenses, and Azure AD groups.
  name: Microsoft 365
- description: Connect BetterCloud workflows with Okta identity management.
  name: Okta
- description: Trigger BetterCloud workflows from ServiceNow ITSM tickets.
  name: ServiceNow
- description: Integrate SaaS management actions with Jira issue workflows.
  name: Jira
json_schemas:
- name: EventListResponse
  property_count: 2
  slug: bettercloud-event-list-response
- name: Event
  property_count: 6
  slug: bettercloud-event
- name: GroupCreateRequest
  property_count: 3
  slug: bettercloud-group-create-request
- name: GroupListResponse
  property_count: 2
  slug: bettercloud-group-list-response
- name: GroupMemberAddRequest
  property_count: 2
  slug: bettercloud-group-member-add-request
- name: GroupMemberListResponse
  property_count: 1
  slug: bettercloud-group-member-list-response
- name: GroupMemberResponse
  property_count: 1
  slug: bettercloud-group-member-response
- name: GroupMember
  property_count: 4
  slug: bettercloud-group-member
- name: GroupResponse
  property_count: 1
  slug: bettercloud-group-response
- name: Group
  property_count: 7
  slug: bettercloud-group
- name: IntegrationListResponse
  property_count: 1
  slug: bettercloud-integration-list-response
- name: Integration
  property_count: 5
  slug: bettercloud-integration
- name: MetaResponse
  property_count: 3
  slug: bettercloud-meta-response
- name: UserListResponse
  property_count: 2
  slug: bettercloud-user-list-response
- name: UserResponse
  property_count: 1
  slug: bettercloud-user-response
- name: User
  property_count: 11
  slug: bettercloud-user
- name: UserUpdateRequest
  property_count: 5
  slug: bettercloud-user-update-request
- name: WorkflowCreateRequest
  property_count: 4
  slug: bettercloud-workflow-create-request
- name: WorkflowListResponse
  property_count: 2
  slug: bettercloud-workflow-list-response
- name: WorkflowResponse
  property_count: 1
  slug: bettercloud-workflow-response
- name: WorkflowRunRequest
  property_count: 1
  slug: bettercloud-workflow-run-request
- name: WorkflowRunResponse
  property_count: 1
  slug: bettercloud-workflow-run-response
- name: Workflow
  property_count: 8
  slug: bettercloud-workflow
json_structures:
- name: Bettercloud Event List Response Structure
  property_count: 2
  slug: bettercloud-event-list-response-structure
- name: Bettercloud Event Structure
  property_count: 6
  slug: bettercloud-event-structure
- name: Bettercloud Group Create Request Structure
  property_count: 3
  slug: bettercloud-group-create-request-structure
- name: Bettercloud Group List Response Structure
  property_count: 2
  slug: bettercloud-group-list-response-structure
- name: Bettercloud Group Member Add Request Structure
  property_count: 2
  slug: bettercloud-group-member-add-request-structure
- name: Bettercloud Group Member List Response Structure
  property_count: 1
  slug: bettercloud-group-member-list-response-structure
- name: Bettercloud Group Member Response Structure
  property_count: 1
  slug: bettercloud-group-member-response-structure
- name: Bettercloud Group Member Structure
  property_count: 4
  slug: bettercloud-group-member-structure
- name: Bettercloud Group Response Structure
  property_count: 1
  slug: bettercloud-group-response-structure
- name: Bettercloud Group Structure
  property_count: 7
  slug: bettercloud-group-structure
- name: Bettercloud Integration List Response Structure
  property_count: 1
  slug: bettercloud-integration-list-response-structure
- name: Bettercloud Integration Structure
  property_count: 5
  slug: bettercloud-integration-structure
- name: Bettercloud Meta Response Structure
  property_count: 3
  slug: bettercloud-meta-response-structure
- name: Bettercloud User List Response Structure
  property_count: 2
  slug: bettercloud-user-list-response-structure
- name: Bettercloud User Response Structure
  property_count: 1
  slug: bettercloud-user-response-structure
- name: Bettercloud User Structure
  property_count: 11
  slug: bettercloud-user-structure
- name: Bettercloud User Update Request Structure
  property_count: 5
  slug: bettercloud-user-update-request-structure
- name: Bettercloud Workflow Create Request Structure
  property_count: 4
  slug: bettercloud-workflow-create-request-structure
- name: Bettercloud Workflow List Response Structure
  property_count: 2
  slug: bettercloud-workflow-list-response-structure
- name: Bettercloud Workflow Response Structure
  property_count: 1
  slug: bettercloud-workflow-response-structure
- name: Bettercloud Workflow Run Request Structure
  property_count: 1
  slug: bettercloud-workflow-run-request-structure
- name: Bettercloud Workflow Run Response Structure
  property_count: 1
  slug: bettercloud-workflow-run-response-structure
- name: Bettercloud Workflow Structure
  property_count: 8
  slug: bettercloud-workflow-structure
jsonld:
- class_count: 28
  name: Bettercloud Context
  property_count: 24
  slug: bettercloud-context
layout: provider
modified: '2026-05-19'
name: BetterCloud
nav: Providers
network: true
overview: 'BetterCloud publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Events API, Groups API, Integrations API, and 2 more. Tagged areas include Automation, Compliance, Enterprise, IT Operations, and SaaS Management.


  The BetterCloud catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  BetterCloud''s developer surface includes authentication, developer portal, getting-started guide, pricing, engineering blog, support, signup flow, and 7 more developer resources.'
plans:
- name: Bettercloud Plans Pricing
  plan_count: 3
  slug: bettercloud-plans-pricing
random_paper: 25
rate_limits:
- limit_count: 5
  name: Bettercloud Rate Limits
  slug: bettercloud-rate-limits
rules:
- name: BetterCloud API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: bettercloud-jsonschema-spectral-rules
- name: BetterCloud API Rules
  rule_count: 34
  severity_counts:
    error: 13
    hint: 0
    info: 2
    warn: 19
  slug: bettercloud-spectral-rules
score:
  band: strong
  composite: 62.3
  delta: 0.0
  facets:
    commercial_clarity: 63.2
    contract_quality: 68.1
    developer_ergonomics: 37.0
    discoverability: 100.0
    governance: 86.8
    operational_transparency: 36.8
  previous_composite: 62.3
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bettercloud/refs/heads/main/screenshots/bettercloud-2026-06-20T173204.png
security:
- kind: authentication
  name: Bettercloud Authentication
  slug: bettercloud-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Bettercloud Domain Security
  slug: bettercloud-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: bettercloud
tags:
- Automation
- Compliance
- Enterprise
- IT Operations
- SaaS Management
- Security
- Workflows
- User Lifecycle
use_cases:
- description: Automatically revoke access and deprovision users across all SaaS applications when an employee leaves.
  name: Employee Offboarding
- description: Automatically provision new employees with appropriate SaaS access based on role and department.
  name: Employee Onboarding
- description: Identify underutilized licenses and redundant applications to reduce SaaS spend.
  name: SaaS Spend Optimization
- description: Immediately suspend and deprovision compromised accounts across all SaaS platforms.
  name: Security Incident Response
- description: Generate audit reports showing who has access to what across all connected SaaS applications.
  name: Compliance Auditing
- description: Periodically review and certify user access to ensure least-privilege principles.
  name: Access Reviews
website: https://developer.bettercloud.com/
---
