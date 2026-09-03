---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 40.0
  scored_at: '2026-09-02'
api_count: 3
apis:
- baseURL: https://api.upsun.com
  baseurl_source: declared
  description: The Add-ons API from Platform.sh — 1 operation(s) for add-ons.
  name: Platform.sh Add Ons API
  slug: platform.sh-add-ons-api
- baseURL: https://api.upsun.com
  baseurl_source: declared
  description: The Alerts API from Platform.sh — 1 operation(s) for alerts.
  name: Platform.sh Alerts API
  slug: platform.sh-alerts-api
- baseURL: https://api.upsun.com
  baseurl_source: declared
  description: The API Tokens API from Platform.sh — 2 operation(s) for api tokens.
  name: Platform.sh API Tokens API
  slug: platform.sh-api-tokens-api
- baseURL: https://api.upsun.com
  baseurl_source: declared
  description: Upsun provides native support for autoscaling, allowing your applications to automatically adjust based on resource usage. This ensures that your apps remain responsive under load while helping you op
  name: Platform.sh Autoscaling API
  slug: platform.sh-autoscaling-api
- baseURL: https://api.upsun.com
  baseurl_source: declared
  description: The Blackfire Monitoring API from Platform.sh — 4 operation(s) for blackfire monitoring.
  name: Platform.sh Blackfire Monitoring API
  slug: platform.sh-blackfire-monitoring-api
- baseURL: https://api.upsun.com
  baseurl_source: declared
  description: The Blackfire Profiling API from Platform.sh — 6 operation(s) for blackfire profiling.
  name: Platform.sh Blackfire Profiling API
  slug: platform.sh-blackfire-profiling-api
- baseURL: https://api.upsun.com
  baseurl_source: declared
  description: User-supplied SSL/TLS certificates can be managed using these endpoints. You can now list and modify certificate provisioners using the `/projects/{projectId}/provisioners` and `/projects/{projectId}/
  name: Platform.sh Cert Management API
  slug: platform.sh-cert-management-api
- baseURL: https://api.upsun.com
  baseurl_source: declared
  description: The Connections API from Platform.sh — 2 operation(s) for connections.
  name: Platform.sh Connections API
  slug: platform.sh-connections-api
- baseURL: https://api.upsun.com
  baseurl_source: declared
  description: The Continuous Profiling API from Platform.sh — 4 operation(s) for continuous profiling.
  name: Platform.sh Continuous Profiling API
  slug: platform.sh-continuous-profiling-api
- baseURL: https://api.upsun.com
  baseurl_source: declared
  description: The Deployment API from Platform.sh — 2 operation(s) for deployment.
  name: Platform.sh Deployment API
  slug: platform.sh-deployment-api
- baseURL: https://api.upsun.com
  baseurl_source: declared
  description: 'Upsun is capable of deploying the production environments of projects in multiple topologies: both in clusters of containers, and as dedicated virtual machines. This is an internal API that can only b'
  name: Platform.sh Deployment Target API
  slug: platform.sh-deployment-target-api
- baseURL: https://api.upsun.com
  baseurl_source: declared
  description: The Diff API from Platform.sh — 1 operation(s) for diff.
  name: Platform.sh Diff API
  slug: platform.sh-diff-api
- baseURL: https://api.upsun.com
  baseurl_source: declared
  description: The Discounts API from Platform.sh — 3 operation(s) for discounts.
  name: Platform.sh Discounts API
  slug: platform.sh-discounts-api
- baseURL: https://api.upsun.com
  baseurl_source: declared
  description: These endpoints can be used to add, modify, or remove domain claims from a project. For more information on how domains function on Upsun, see the [Domains](https://docs.upsun.com/anchors/domains/cust
  name: Platform.sh Domain Claim API
  slug: platform.sh-domain-claim-api
- baseURL: https://api.upsun.com
  baseurl_source: declared
  description: These endpoints can be used to add, modify, or remove domains from a project. For more information on how domains function on Upsun, see the [Domains](https://docs.upsun.com/anchors/domains/custom/) s
  name: Platform.sh Domain Management API
  slug: platform.sh-domain-management-api
- baseURL: https://api.upsun.com
  baseurl_source: declared
  description: The Entrypoint API from Platform.sh — 1 operation(s) for entrypoint.
  name: Platform.sh Entrypoint API
  slug: platform.sh-entrypoint-api
- baseURL: https://api.upsun.com
  baseurl_source: declared
  description: The Environment Activity API from Platform.sh — 3 operation(s) for environment activity.
  name: Platform.sh Environment Activity API
  slug: platform.sh-environment-activity-api
- baseURL: https://api.upsun.com
  baseurl_source: declared
  description: On Upsun, an environment encompasses a single instance of your entire application stack, the services used by the application, the application's data storage, and the environment's backups. In general
  name: Platform.sh Environment API
  slug: platform.sh-environment-api
- baseURL: https://api.upsun.com
  baseurl_source: declared
  description: A snapshot is a complete backup of an environment, including all the persistent data from all services running in an environment and all files present in mounted volumes. These endpoints can be used t
  name: Platform.sh Environment Backups API
  slug: platform.sh-environment-backups-api
- baseURL: https://api.upsun.com
  baseurl_source: declared
  description: 'Environment Types is the way Upsun manages access. We currently have 3 environment types: * Development * Staging * Production Each environment type will contain a group of users and their accesses. W'
  name: Platform.sh Environment Type API
  slug: platform.sh-environment-type-api
- baseURL: https://api.upsun.com
  baseurl_source: declared
  description: These endpoints manipulate user-defined variables which are bound to a specific environment, as well as (optionally) the children of an environment. These variables can be made available at both build
  name: Platform.sh Environment Variables API
  slug: platform.sh-environment-variables-api
- baseURL: https://api.upsun.com
  baseurl_source: declared
  description: The Grants API from Platform.sh — 2 operation(s) for grants.
  name: Platform.sh Grants API
  slug: platform.sh-grants-api
- baseURL: https://api.upsun.com
  baseurl_source: declared
  description: The Http Traffic API from Platform.sh — 3 operation(s) for http traffic.
  name: Platform.sh Http Traffic API
  slug: platform.sh-http-traffic-api
- baseURL: https://api.upsun.com
  baseurl_source: declared
  description: These endpoints can be used to retrieve invoices from our billing system. An invoice of type "invoice" is generated automatically every month, if the customer has active projects. Invoices of type "cr
  name: Platform.sh Invoices API
  slug: platform.sh-invoices-api
- baseURL: https://api.upsun.com
  baseurl_source: declared
  description: Multi-Factor Authentication (MFA) requires the user to present two (or more) types of evidence (or factors) to prove their identity. For example, the evidence might be a password and a device-generate
  name: Platform.sh MFA API
  slug: platform.sh-mfa-api
- baseURL: https://api.upsun.com
  baseurl_source: declared
  description: 'These endpoints can be used to retrieve order information from our billing system. Here you can view information about your bill for our services, include the billed amount and a link to a PDF of the '
  name: Platform.sh Orders API
  slug: platform.sh-orders-api
- baseURL: https://api.upsun.com
  baseurl_source: declared
  description: The Organization Invitations API from Platform.sh — 2 operation(s) for organization invitations.
  name: Platform.sh Organization Invitations API
  slug: platform.sh-organization-invitations-api
- baseURL: https://api.upsun.com
  baseurl_source: declared
  description: The Organization Management API from Platform.sh — 4 operation(s) for organization management.
  name: Platform.sh Organization Management API
  slug: platform.sh-organization-management-api
- baseURL: https://api.upsun.com
  baseurl_source: declared
  description: The Organization Members API from Platform.sh — 2 operation(s) for organization members.
  name: Platform.sh Organization Members API
  slug: platform.sh-organization-members-api
- baseURL: https://api.upsun.com
  baseurl_source: declared
  description: The Organization Projects API from Platform.sh — 4 operation(s) for organization projects.
  name: Platform.sh Organization Projects API
  slug: platform.sh-organization-projects-api
- baseURL: https://api.upsun.com
  baseurl_source: declared
  description: The Organizations API from Platform.sh — 4 operation(s) for organizations.
  name: Platform.sh Organizations API
  slug: platform.sh-organizations-api
- baseURL: https://api.upsun.com
  baseurl_source: declared
  description: The PhoneNumber API from Platform.sh — 2 operation(s) for phonenumber.
  name: Platform.sh Phone Number API
  slug: platform.sh-phonenumber-api
- baseURL: https://api.upsun.com
  baseurl_source: declared
  description: The Profiles API from Platform.sh — 2 operation(s) for profiles.
  name: Platform.sh Profiles API
  slug: platform.sh-profiles-api
- baseURL: https://api.upsun.com
  baseurl_source: declared
  description: The Project Activity API from Platform.sh — 3 operation(s) for project activity.
  name: Platform.sh Project Activity API
  slug: platform.sh-project-activity-api
- baseURL: https://api.upsun.com
  baseurl_source: declared
  description: '## Project Overview On Upsun, a Project is backed by a single Git repository and encompasses your entire application stack, the services used by your application, the application''s data storage, the p'
  name: Platform.sh Project API
  slug: platform.sh-project-api
- baseURL: https://api.upsun.com
  baseurl_source: declared
  description: The Project Invitations API from Platform.sh — 2 operation(s) for project invitations.
  name: Platform.sh Project Invitations API
  slug: platform.sh-project-invitations-api
- baseURL: https://api.upsun.com
  baseurl_source: declared
  description: These endpoints can be used to retrieve and manipulate project-level settings. Only the `initialize` property can be set by end users. It is used to initialize a project from an existing Git repositor
  name: Platform.sh Project Settings API
  slug: platform.sh-project-settings-api
- baseURL: https://api.upsun.com
  baseurl_source: declared
  description: These endpoints manipulate user-defined variables which are bound to an entire project. These variables are accessible to all environments within a single project, and they can be made available at bo
  name: Platform.sh Project Variables API
  slug: platform.sh-project-variables-api
- baseURL: https://api.upsun.com
  baseurl_source: declared
  description: The Projects API from Platform.sh — 1 operation(s) for projects.
  name: Platform.sh Projects API
  slug: platform.sh-projects-api
- baseURL: https://api.upsun.com
  baseurl_source: declared
  description: These endpoints retrieve information about which plans were assigned to a particular project at which time.
  name: Platform.sh Records API
  slug: platform.sh-records-api
- baseURL: https://api.upsun.com
  baseurl_source: declared
  description: The References API from Platform.sh — 5 operation(s) for references.
  name: Platform.sh References API
  slug: platform.sh-references-api
- baseURL: https://api.upsun.com
  baseurl_source: declared
  description: The Regions API from Platform.sh — 2 operation(s) for regions.
  name: Platform.sh Regions API
  slug: platform.sh-regions-api
- baseURL: https://api.upsun.com
  baseurl_source: declared
  description: The Git repository backing projects hosted on Upsun can be accessed in a **read-only** manner through the `/projects/{projectId}/git/*` family of endpoints. With these endpoints, you can retrieve obje
  name: Platform.sh Repository API
  slug: platform.sh-repository-api
- baseURL: https://api.upsun.com
  baseurl_source: declared
  description: The Resources API from Platform.sh — 3 operation(s) for resources.
  name: Platform.sh Resources API
  slug: platform.sh-resources-api
- baseURL: https://api.upsun.com
  baseurl_source: declared
  description: These endpoints modify an environment's `routes:` section of the `.upsun/config.yaml` file. For routes to propagate to child environments, the child environments must be synchronized with their parent
  name: Platform.sh Routing API
  slug: platform.sh-routing-api
- baseURL: https://api.upsun.com
  baseurl_source: declared
  description: The Runtime Operations API from Platform.sh — 1 operation(s) for runtime operations.
  name: Platform.sh Runtime Operations API
  slug: platform.sh-runtime-operations-api
- baseURL: https://api.upsun.com
  baseurl_source: declared
  description: These endpoints interact with source code operations as defined in the `source.operations` key in a project's `.upsun/config.yaml` configuration. More information on source code operations is [availab
  name: Platform.sh Source Operations API
  slug: platform.sh-source-operations-api
- baseURL: https://api.upsun.com
  baseurl_source: declared
  description: The SSH Keys API from Platform.sh — 2 operation(s) for ssh keys.
  name: Platform.sh SSH Keys API
  slug: platform.sh-ssh-keys-api
- baseURL: https://api.upsun.com
  baseurl_source: declared
  description: Each project is represented by a subscription that holds the plan information. These endpoints can be used to go to a larger plan, add more storage, or subscribe to optional features.
  name: Platform.sh Subscriptions API
  slug: platform.sh-subscriptions-api
- baseURL: https://api.upsun.com
  baseurl_source: declared
  description: These endpoints can be used to retrieve information about support ticket priority and allow you to submit new ticket to the Upsun Support Team.
  name: Platform.sh Support API
  slug: platform.sh-support-api
- baseURL: https://api.upsun.com
  baseurl_source: declared
  description: These endpoints can be used to retrieve low-level information and interact with the core component of Upsun infrastructure. This is an internal API that can only be used by privileged users.
  name: Platform.sh System Information API
  slug: platform.sh-system-information-api
- baseURL: https://api.upsun.com
  baseurl_source: declared
  description: These endpoints can be used to manage tasks, which are one-off commands that can be run in the context of an environment. Tasks are useful for running database migrations, executing maintenance script
  name: Platform.sh Task API
  slug: platform.sh-task-api
- baseURL: https://api.upsun.com
  baseurl_source: declared
  description: The Team Access API from Platform.sh — 4 operation(s) for team access.
  name: Platform.sh Team Access API
  slug: platform.sh-team-access-api
- baseURL: https://api.upsun.com
  baseurl_source: declared
  description: The Teams API from Platform.sh — 5 operation(s) for teams.
  name: Platform.sh Teams API
  slug: platform.sh-teams-api
- baseURL: https://api.upsun.com
  baseurl_source: declared
  description: Upsun can easily integrate with many third-party services, including Git hosting services (GitHub, GitLab, and Bitbucket), health notification services (email, Slack, PagerDuty), performance analytics
  name: Platform.sh Third-Party Integrations API
  slug: platform.sh-third-party-integrations-api
- baseURL: https://api.upsun.com
  baseurl_source: declared
  description: The Tickets API from Platform.sh — 1 operation(s) for tickets.
  name: Platform.sh Tickets API
  slug: platform.sh-tickets-api
- baseURL: https://api.upsun.com
  baseurl_source: declared
  description: The User Access API from Platform.sh — 4 operation(s) for user access.
  name: Platform.sh User Access API
  slug: platform.sh-user-access-api
- baseURL: https://api.upsun.com
  baseurl_source: declared
  description: The User Profiles API from Platform.sh — 4 operation(s) for user profiles.
  name: Platform.sh User Profiles API
  slug: platform.sh-user-profiles-api
- baseURL: https://api.upsun.com
  baseurl_source: declared
  description: The Users API from Platform.sh — 9 operation(s) for users.
  name: Platform.sh Users API
  slug: platform.sh-users-api
- baseURL: https://api.upsun.com
  baseurl_source: declared
  description: These endpoints can be used to retrieve vouchers associated with a particular user as well as apply a voucher to a particular user.
  name: Platform.sh Vouchers API
  slug: platform.sh-vouchers-api
artifact_total: 68
asyncapis:
- description: ''
  name: Platform.Sh Webhooks
  slug: platform.sh-webhooks
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/platform.sh-capability-edges.yml
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
  url: https://docs.upsun.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.upsun.com/api
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.upsun.com/docs/get-started
- group: operate
  title: ''
  type: Support
  url: https://developer.upsun.com/docs/core-concepts/get-support
- group: company
  title: ''
  type: Blog
  url: https://upsun.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/platformsh
- group: operate
  title: ''
  type: StatusPage
  url: https://status.upsun.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://upsun.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://console.upsun.com/
- group: start
  title: ''
  type: Console
  url: https://console.platform.sh/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://upsun.com/trust-center/legal/tos/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://upsun.com/trust-center/privacy/privacy-notice/
- group: auth
  title: ''
  type: TrustCenter
  url: https://upsun.com/trust-center/
- group: auth
  title: ''
  type: Authentication
  url: authentication/platform.sh-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/platform.sh-scopes.yml
- group: build
  title: ''
  type: Packages
  url: packages/platform.sh-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/platform.sh-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/platform.sh-cli.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/platform.sh-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/platform.sh-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/platform.sh-security.txt
- group: auth
  title: ''
  type: Security
  url: security/platform.sh-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/platform.sh-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/platform.sh-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/platform.sh-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/platform.sh-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/platform.sh-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/platform.sh-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/platform.sh-changelog.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/platform.sh-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/platform.sh-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/platform.sh-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/platform.sh-rest-api-overlay.yaml
- group: commercial
  title: ''
  type: Plans
  url: plans/platform.sh-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/platform.sh-rate-limits.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/platform.sh-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/platform.sh-webhooks.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/platform.sh-tool-crosswalk.yml
created: '2026-08-26'
description: 'Platform.sh is the container-based Platform-as-a-Service (PaaS) founded in 2010 and headquartered in Paris and San Francisco, best known for Git-driven deployments in which a single push plus a few YAML files provisions an entire cluster of applications and managed services (PostgreSQL, MySQL, Redis, RabbitMQ, OpenSearch and more) together with byte-for-byte preview environments cloned from production. The company rebranded to Upsun: platform.sh now redirects to upsun.com, the original Platform.sh product is documented as ''Upsun Fixed'' at docs.upsun.com, and the public REST API - whose own OpenAPI description reads ''Upsun, formerly Platform.sh'' - is still authenticated by the OAuth 2.0 authorization server at auth.api.platform.sh with regional gateways on platform.sh hosts. That API exposes 263 operations across projects, environments, backups, domains, certificates, variables, activities, organizations, teams, subscriptions and billing, returns RFC 9457 application/problem+json
  errors, and is accompanied by a first-party CLI, PHP/JavaScript API clients and language config readers published under the platformsh namespace.'
image: https://upsun.com/default_social.png
layout: provider
mcp_servers:
- description: ''
  name: Upsun MCP Server
  slug: upsun-mcp-server
modified: '2026-08-26'
name: Platform.sh
nav: Providers
network: true
overview: 'Platform.sh publishes 60 APIs on the [APIs.io](https://apis.io/) network, including Add Ons API, Alerts API, API Tokens API, and 57 more. Tagged areas include Platform-as-a-Service, Cloud Hosting, Application Hosting, Deployment, and DevOps.


  The Platform.sh catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Platform.sh''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 35 more developer resources.'
plans:
- name: Platform.Sh Plans Pricing
  plan_count: 0
  slug: platform.sh-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Platform.Sh Rate Limits
  slug: platform.sh-rate-limits
scopes:
- name: Platform.Sh Scopes
  scope_count: 1
  slug: platform.sh-scopes
  summary_line: 1 scope · authorizationCode/clientCredentials
score:
  band: developing
  composite: 52.5
  coverage:
    artifact_dirs: 23
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -1.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 18.2
    contract_quality: 58.6
    developer_ergonomics: 73.2
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 44.7
  previous_composite: 53.5
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 60
    mcp: first-party
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/platform.sh/refs/heads/main/screenshots/platform.sh-2026-09-02T151433.png
security:
- kind: authentication
  name: Platform.Sh Authentication
  slug: platform.sh-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Platform.Sh Domain Security
  slug: platform.sh-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Platform.Sh Vulnerability Disclosure
  slug: platform.sh-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: platform.sh
tags:
- Platform-as-a-Service
- Cloud Hosting
- Application Hosting
- Deployment
- DevOps
- Continuous Deployment
- Containers
- Managed Service
- Developer Tools
- Infrastructure
- Multi-Cloud
- Web Hosting
website: https://upsun.com/
---
