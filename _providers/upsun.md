---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 59.2
  scored_at: '2026-07-28'
api_count: 50
apis:
- description: The Add-ons API from Upsun — 1 operation(s) for add-ons.
  name: Upsun Add-ons API
  slug: upsun-add-ons-api
- description: The Alerts API from Upsun — 1 operation(s) for alerts.
  name: Upsun Alerts API
  slug: upsun-alerts-api
- description: The API Tokens API from Upsun — 2 operation(s) for api tokens.
  name: Upsun API Tokens API
  slug: upsun-api-tokens-api
- description: Upsun provides native support for autoscaling, allowing your applications to automatically adjust based on resource usage. This ensures that your apps remain responsive under load while helping you op
  name: Upsun Autoscaling API
  slug: upsun-autoscaling-api
- description: User-supplied SSL/TLS certificates can be managed using these endpoints. You can now list and modify certificate provisioners using the `/projects/{projectId}/provisioners` and `/projects/{projectId}/
  name: Upsun Cert Management API
  slug: upsun-cert-management-api
- description: The Connections API from Upsun — 2 operation(s) for connections.
  name: Upsun Connections API
  slug: upsun-connections-api
- description: The Deployment API from Upsun — 2 operation(s) for deployment.
  name: Upsun Deployment API
  slug: upsun-deployment-api
- description: 'Upsun is capable of deploying the production environments of projects in multiple topologies: both in clusters of containers, and as dedicated virtual machines. This is an internal API that can only b'
  name: Upsun Deployment Target API
  slug: upsun-deployment-target-api
- description: The Discounts API from Upsun — 3 operation(s) for discounts.
  name: Upsun Discounts API
  slug: upsun-discounts-api
- description: These endpoints can be used to add, modify, or remove domains from a project. For more information on how domains function on Upsun, see the [Domains](https://docs.upsun.com/anchors/domains/custom/) s
  name: Upsun Domain Management API
  slug: upsun-domain-management-api
- description: The Environment Activity API from Upsun — 3 operation(s) for environment activity.
  name: Upsun Environment Activity API
  slug: upsun-environment-activity-api
- description: On Upsun, an environment encompasses a single instance of your entire application stack, the services used by the application, the application's data storage, and the environment's backups. In general
  name: Upsun Environment API
  slug: upsun-environment-api
- description: A snapshot is a complete backup of an environment, including all the persistent data from all services running in an environment and all files present in mounted volumes. These endpoints can be used t
  name: Upsun Environment Backups API
  slug: upsun-environment-backups-api
- description: 'Environment Types is the way Upsun manages access. We currently have 3 environment types: * Development * Staging * Production Each environment type will contain a group of users and their accesses. W'
  name: Upsun Environment Type API
  slug: upsun-environment-type-api
- description: These endpoints manipulate user-defined variables which are bound to a specific environment, as well as (optionally) the children of an environment. These variables can be made available at both build
  name: Upsun Environment Variables API
  slug: upsun-environment-variables-api
- description: The Grants API from Upsun — 1 operation(s) for grants.
  name: Upsun Grants API
  slug: upsun-grants-api
- description: These endpoints can be used to retrieve invoices from our billing system. An invoice of type "invoice" is generated automatically every month, if the customer has active projects. Invoices of type "cr
  name: Upsun Invoices API
  slug: upsun-invoices-api
- description: Multi-factor authentication (MFA) requires the user to present two (or more) types of evidence (or factors) to prove their identity. For example, the evidence might be a password and a device-generate
  name: Upsun MFA API
  slug: upsun-mfa-api
- description: 'These endpoints can be used to retrieve order information from our billing system. Here you can view information about your bill for our services, include the billed amount and a link to a PDF of the '
  name: Upsun Orders API
  slug: upsun-orders-api
- description: The Organization Invitations API from Upsun — 2 operation(s) for organization invitations.
  name: Upsun Organization Invitations API
  slug: upsun-organization-invitations-api
- description: The Organization Management API from Upsun — 4 operation(s) for organization management.
  name: Upsun Organization Management API
  slug: upsun-organization-management-api
- description: The Organization Members API from Upsun — 2 operation(s) for organization members.
  name: Upsun Organization Members API
  slug: upsun-organization-members-api
- description: The Organization Projects API from Upsun — 3 operation(s) for organization projects.
  name: Upsun Organization Projects API
  slug: upsun-organization-projects-api
- description: The Organizations API from Upsun — 4 operation(s) for organizations.
  name: Upsun Organizations API
  slug: upsun-organizations-api
- description: The PhoneNumber API from Upsun — 2 operation(s) for phonenumber.
  name: Upsun PhoneNumber API
  slug: upsun-phonenumber-api
- description: The Profiles API from Upsun — 2 operation(s) for profiles.
  name: Upsun Profiles API
  slug: upsun-profiles-api
- description: The Project Activity API from Upsun — 3 operation(s) for project activity.
  name: Upsun Project Activity API
  slug: upsun-project-activity-api
- description: '## Project Overview On Upsun, a Project is backed by a single Git repository and encompasses your entire application stack, the services used by your application, the application''s data storage, the p'
  name: Upsun Project API
  slug: upsun-project-api
- description: The Project Invitations API from Upsun — 2 operation(s) for project invitations.
  name: Upsun Project Invitations API
  slug: upsun-project-invitations-api
- description: These endpoints can be used to retrieve and manipulate project-level settings. Only the `initialize` property can be set by end users. It is used to initialize a project from an existing Git repositor
  name: Upsun Project Settings API
  slug: upsun-project-settings-api
- description: These endpoints manipulate user-defined variables which are bound to an entire project. These variables are accessible to all environments within a single project, and they can be made available at bo
  name: Upsun Project Variables API
  slug: upsun-project-variables-api
- description: These endpoints retrieve information about which plans were assigned to a particular project at which time.
  name: Upsun Records API
  slug: upsun-records-api
- description: The References API from Upsun — 5 operation(s) for references.
  name: Upsun References API
  slug: upsun-references-api
- description: The Regions API from Upsun — 2 operation(s) for regions.
  name: Upsun Regions API
  slug: upsun-regions-api
- description: The Git repository backing projects hosted on Upsun can be accessed in a **read-only** manner through the `/projects/{projectId}/git/*` family of endpoints. With these endpoints, you can retrieve obje
  name: Upsun Repository API
  slug: upsun-repository-api
- description: These endpoints modify an environment's `routes:` section of the `.upsun/config.yaml` file. For routes to propagate to child environments, the child environments must be synchronized with their parent
  name: Upsun Routing API
  slug: upsun-routing-api
- description: The Runtime Operations API from Upsun — 1 operation(s) for runtime operations.
  name: Upsun Runtime Operations API
  slug: upsun-runtime-operations-api
- description: These endpoints interact with source code operations as defined in the `source.operations` key in a project's `.upsun/config.yaml` configuration. More information on source code operations is [availab
  name: Upsun Source Operations API
  slug: upsun-source-operations-api
- description: The SSH Keys API from Upsun — 2 operation(s) for ssh keys.
  name: Upsun SSH Keys API
  slug: upsun-ssh-keys-api
- description: Each project is represented by a subscription that holds the plan information. These endpoints can be used to go to a larger plan, add more storage, or subscribe to optional features.
  name: Upsun Subscriptions API
  slug: upsun-subscriptions-api
- description: These endpoints can be used to retrieve information about support ticket priority and allow you to submit new ticket to the Upsun Support Team.
  name: Upsun Support API
  slug: upsun-support-api
- description: These endpoints can be used to retrieve low-level information and interact with the core component of Upsun infrastructure. This is an internal API that can only be used by privileged users.
  name: Upsun System Information API
  slug: upsun-system-information-api
- description: The Team Access API from Upsun — 4 operation(s) for team access.
  name: Upsun Team Access API
  slug: upsun-team-access-api
- description: The Teams API from Upsun — 5 operation(s) for teams.
  name: Upsun Teams API
  slug: upsun-teams-api
- description: Upsun can easily integrate with many third-party services, including Git hosting services (GitHub, GitLab, and Bitbucket), health notification services (email, Slack, PagerDuty), performance analytics
  name: Upsun Third-Party Integrations API
  slug: upsun-third-party-integrations-api
- description: The Tickets API from Upsun — 1 operation(s) for tickets.
  name: Upsun Tickets API
  slug: upsun-tickets-api
- description: The User Access API from Upsun — 4 operation(s) for user access.
  name: Upsun User Access API
  slug: upsun-user-access-api
- description: The User Profiles API from Upsun — 4 operation(s) for user profiles.
  name: Upsun User Profiles API
  slug: upsun-user-profiles-api
- description: The Users API from Upsun — 9 operation(s) for users.
  name: Upsun Users API
  slug: upsun-users-api
- description: These endpoints can be used to retrieve vouchers associated with a particular user as well as apply a voucher to a particular user.
  name: Upsun Vouchers API
  slug: upsun-vouchers-api
artifact_total: 107
asyncapis:
- description: ''
  name: Upsun Activity Webhooks
  slug: upsun-activity-webhooks
collections:
- collection_type: postman
  name: Upsun.com Rest Add-ons API
  slug: postman-upsun-add-ons-api
- collection_type: postman
  name: Upsun.com Rest Add-ons Alerts API
  slug: postman-upsun-alerts-api
- collection_type: postman
  name: Upsun.com Rest Add-ons API Tokens API
  slug: postman-upsun-api-tokens-api
- collection_type: postman
  name: Upsun.com Rest Add-ons Autoscaling API
  slug: postman-upsun-autoscaling-api
- collection_type: postman
  name: Upsun.com Rest Add-ons Cert Management API
  slug: postman-upsun-cert-management-api
- collection_type: postman
  name: Upsun.com Rest Add-ons Connections API
  slug: postman-upsun-connections-api
- collection_type: postman
  name: Upsun.com Rest Add-ons Deployment API
  slug: postman-upsun-deployment-api
- collection_type: postman
  name: Upsun.com Rest Add-ons Deployment Target API
  slug: postman-upsun-deployment-target-api
- collection_type: postman
  name: Upsun.com Rest Add-ons Discounts API
  slug: postman-upsun-discounts-api
- collection_type: postman
  name: Upsun.com Rest Add-ons Domain Management API
  slug: postman-upsun-domain-management-api
- collection_type: postman
  name: Upsun.com Rest Add-ons Environment Activity API
  slug: postman-upsun-environment-activity-api
- collection_type: postman
  name: Upsun.com Rest Add-ons Environment API
  slug: postman-upsun-environment-api
- collection_type: postman
  name: Upsun.com Rest Add-ons Environment Backups API
  slug: postman-upsun-environment-backups-api
- collection_type: postman
  name: Upsun.com Rest Add-ons Environment Type API
  slug: postman-upsun-environment-type-api
- collection_type: postman
  name: Upsun.com Rest Add-ons Environment Variables API
  slug: postman-upsun-environment-variables-api
- collection_type: postman
  name: Upsun.com Rest Add-ons Grants API
  slug: postman-upsun-grants-api
- collection_type: postman
  name: Upsun.com Rest Add-ons Invoices API
  slug: postman-upsun-invoices-api
- collection_type: postman
  name: Upsun.com Rest Add-ons MFA API
  slug: postman-upsun-mfa-api
- collection_type: postman
  name: Upsun.com Rest Add-ons Orders API
  slug: postman-upsun-orders-api
- collection_type: postman
  name: Upsun.com Rest Add-ons Organization Invitations API
  slug: postman-upsun-organization-invitations-api
- collection_type: postman
  name: Upsun.com Rest Add-ons Organization Management API
  slug: postman-upsun-organization-management-api
- collection_type: postman
  name: Upsun.com Rest Add-ons Organization Members API
  slug: postman-upsun-organization-members-api
- collection_type: postman
  name: Upsun.com Rest Add-ons Organization Projects API
  slug: postman-upsun-organization-projects-api
- collection_type: postman
  name: Upsun.com Rest Add-ons Organizations API
  slug: postman-upsun-organizations-api
- collection_type: postman
  name: Upsun.com Rest Add-ons PhoneNumber API
  slug: postman-upsun-phonenumber-api
- collection_type: postman
  name: Upsun.com Rest Add-ons Profiles API
  slug: postman-upsun-profiles-api
- collection_type: postman
  name: Upsun.com Rest Add-ons Project Activity API
  slug: postman-upsun-project-activity-api
- collection_type: postman
  name: Upsun.com Rest Add-ons Project API
  slug: postman-upsun-project-api
- collection_type: postman
  name: Upsun.com Rest Add-ons Project Invitations API
  slug: postman-upsun-project-invitations-api
- collection_type: postman
  name: Upsun.com Rest Add-ons Project Settings API
  slug: postman-upsun-project-settings-api
- collection_type: postman
  name: Upsun.com Rest Add-ons Project Variables API
  slug: postman-upsun-project-variables-api
- collection_type: postman
  name: Upsun.com Rest Add-ons Records API
  slug: postman-upsun-records-api
- collection_type: postman
  name: Upsun.com Rest Add-ons References API
  slug: postman-upsun-references-api
- collection_type: postman
  name: Upsun.com Rest Add-ons Regions API
  slug: postman-upsun-regions-api
- collection_type: postman
  name: Upsun.com Rest Add-ons Repository API
  slug: postman-upsun-repository-api
- collection_type: postman
  name: Upsun.com Rest Add-ons Routing API
  slug: postman-upsun-routing-api
- collection_type: postman
  name: Upsun.com Rest Add-ons Runtime Operations API
  slug: postman-upsun-runtime-operations-api
- collection_type: postman
  name: Upsun.com Rest Add-ons Source Operations API
  slug: postman-upsun-source-operations-api
- collection_type: postman
  name: Upsun.com Rest Add-ons SSH Keys API
  slug: postman-upsun-ssh-keys-api
- collection_type: postman
  name: Upsun.com Rest Add-ons Subscriptions API
  slug: postman-upsun-subscriptions-api
- collection_type: postman
  name: Upsun.com Rest Add-ons Support API
  slug: postman-upsun-support-api
- collection_type: postman
  name: Upsun.com Rest Add-ons System Information API
  slug: postman-upsun-system-information-api
- collection_type: postman
  name: Upsun.com Rest Add-ons Team Access API
  slug: postman-upsun-team-access-api
- collection_type: postman
  name: Upsun.com Rest Add-ons Teams API
  slug: postman-upsun-teams-api
- collection_type: postman
  name: Upsun.com Rest Add-ons Third-Party Integrations API
  slug: postman-upsun-third-party-integrations-api
- collection_type: postman
  name: Upsun.com Rest Add-ons Tickets API
  slug: postman-upsun-tickets-api
- collection_type: postman
  name: Upsun.com Rest Add-ons User Access API
  slug: postman-upsun-user-access-api
- collection_type: postman
  name: Upsun.com Rest Add-ons User Profiles API
  slug: postman-upsun-user-profiles-api
- collection_type: postman
  name: Upsun.com Rest Add-ons Users API
  slug: postman-upsun-users-api
- collection_type: postman
  name: Upsun.com Rest Add-ons Vouchers API
  slug: postman-upsun-vouchers-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/upsun/overview
- group: company
  title: ''
  type: Website
  url: https://upsun.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.upsun.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.upsun.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://developer.upsun.com/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.upsun.com/docs/get-started
- group: auth
  title: ''
  type: Authentication
  url: authentication/upsun-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/upsun-scopes.yml
- group: build
  title: ''
  type: SDKs
  url: packages/upsun-packages.yml
- group: build
  title: ''
  type: Packages
  url: packages/upsun-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/upsun-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/upsun-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/upsun-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/upsun-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/upsun-security.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/upsun-api-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/upsun-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://upsun.com/trust-center/
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/upsun-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/upsun-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.upsun.com/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/upsun-changelog.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/upsun-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/upsun-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/upsun-activity-webhooks.yml
- group: auth
  title: ''
  type: Security
  url: https://upsun.com/trust-center/security/responsible-disclosure/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/upsun-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/upsun-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/upsun-domain-security.yml
- group: start
  title: ''
  type: Console
  url: https://console.upsun.com/
- group: operate
  title: ''
  type: Support
  url: https://community.upsun.com/
- group: company
  title: ''
  type: Blog
  url: https://upsun.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/upsun
- group: commercial
  title: ''
  type: Pricing
  url: https://upsun.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://auth.upsun.com/register
- group: commercial
  title: ''
  type: TermsOfService
  url: https://upsun.com/trust-center/legal/tos/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://upsun.com/trust-center/privacy/privacy-notice/
created: '2026-07-17'
description: Upsun is the cloud application platform from Platform.sh that automatically builds, deploys, and scales applications with git-driven workflows, preview environments per branch, managed services, and usage-based pricing. Its REST API at api.upsun.com covers projects, environments, deployments, backups, domains, certificates, variables, teams, organizations, subscriptions, and observability, secured with OAuth2 API-token exchange, and is complemented by a full-featured CLI, Node.js and PHP SDKs, activity webhooks, and an official hosted MCP server at mcp.upsun.com.
image: https://avatars.githubusercontent.com/u/151578842?v=4
layout: provider
mcp_servers:
- description: ''
  name: upsun-mcp.yml
  slug: upsun-mcpyml
modified: '2026-07-21'
name: Upsun
nav: Providers
network: true
overview: 'Upsun publishes 50 APIs on the [APIs.io](https://apis.io/) network, including Add-ons API, Alerts API, API Tokens API, and 47 more. Tagged areas include Company, Infrastructure Saas, Cloud, PaaS, and Hosting.


  The Upsun catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Upsun''s developer surface includes documentation, API reference, getting-started guide, authentication, CLI, changelog, developer console, and 31 more developer resources.'
random_paper: 32
scopes:
- name: Upsun Scopes
  scope_count: 1
  slug: upsun-scopes
  summary_line: 1 scope · authorizationCode/clientCredentials
score:
  band: strong
  composite: 61.9
  delta: -0.9
  facets:
    commercial_clarity: 60.5
    contract_quality: 61.2
    developer_ergonomics: 86.4
    discoverability: 87.0
    governance: 11.5
    operational_transparency: 55.3
  previous_composite: 62.8
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 50
    mcp: first-party
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Upsun Authentication
  slug: upsun-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Upsun Domain Security
  slug: upsun-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Upsun Vulnerability Disclosure
  slug: upsun-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Upsun Trust Center
  slug: upsun-trust-center
  summary_line: SOC 2 Type 2, ISO 27001, PCI DSS Level 1, HIPAA, IBM Cloud for Financial Services validation, B Corp, EcoVadis, United Nations Global Compact
slug: upsun
tags:
- Company
- Infrastructure Saas
- Cloud
- PaaS
- Hosting
- Deployment
- DevOps
- Containers
- Observability
website: https://upsun.com/
---
