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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 46.6
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 43
  human_in_the_loop: 2
  name: Astronomer Agentic Access
  operation_count: 75
  slug: astronomer-agentic-access
  summary_line: 75 operations · 43 acting · 2 human-in-the-loop
api_count: 15
apis:
- description: The AgentToken API from Astronomer — 2 operation(s) for agenttoken.
  name: Astronomer AgentToken API
  slug: astronomer-agenttoken-api
- description: The AllowedIpAddressRange API from Astronomer — 4 operation(s) for allowedipaddressrange.
  name: Astronomer AllowedIpAddressRange API
  slug: astronomer-allowedipaddressrange-api
- description: The `apitoken` object represents a single API token within your Organization. API tokens are used to authenticate automated tools and processes to your Organization. They have varying levels of access
  name: Astronomer ApiToken API
  slug: astronomer-apitoken-api
- description: The Authorization API from Astronomer — 1 operation(s) for authorization.
  name: Astronomer Authorization API
  slug: astronomer-authorization-api
- description: A `cluster` object represents an Astro cluster, which is a Kubernetes cluster that hosts the infrastructure required to run Deployments. Make requests to `cluster` endpoints to manage your standard an
  name: Astronomer Cluster API
  slug: astronomer-cluster-api
- description: The Deploy API from Astronomer — 4 operation(s) for deploy.
  name: Astronomer Deploy API
  slug: astronomer-deploy-api
- description: The `deployment` object represents an Astro Deployment, which is a hosted Airflow environment that is powered by all core Airflow components, including schedulers and workers. Make requests to the `de
  name: Astronomer Deployment API
  slug: astronomer-deployment-api
- description: The Environment API from Astronomer — 3 operation(s) for environment.
  name: Astronomer Environment API
  slug: astronomer-environment-api
- description: The Invite API from Astronomer — 2 operation(s) for invite.
  name: Astronomer Invite API
  slug: astronomer-invite-api
- description: The Options API from Astronomer — 2 operation(s) for options.
  name: Astronomer Options API
  slug: astronomer-options-api
- description: The `organization` object contains the metadata and configurations of an Astro Organization. It does not include objects within the Organization, such as users and clusters. Make requests to `organiza
  name: Astronomer Organization API
  slug: astronomer-organization-api
- description: The Role API from Astronomer — 4 operation(s) for role.
  name: Astronomer Role API
  slug: astronomer-role-api
- description: 'The `team` object represents an Astro Team, which is a group of users that share the same permissions across your Organization and Workspaces. Make requests to `team` endpoints to create, update, and '
  name: Astronomer Team API
  slug: astronomer-team-api
- description: The `user` object represents a user account in your Astro Organization. Astro creates a new `user` object whenever you invite a user by email or add a user to Astro through an identity provider. The o
  name: Astronomer User API
  slug: astronomer-user-api
- description: The `workspace` object represents an Astro Workspace, which is a collection of Deployments that can be accessed by a specific group of users. It contains metadata about a Workspace, but does not conta
  name: Astronomer Workspace API
  slug: astronomer-workspace-api
artifact_total: 37
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Astro Platform AgentToken API
  slug: open-astronomer-agenttoken-api
- collection_type: open
  name: Astro Platform AgentToken AllowedIpAddressRange API
  slug: open-astronomer-allowedipaddressrange-api
- collection_type: open
  name: Astro Platform AgentToken ApiToken API
  slug: open-astronomer-apitoken-api
- collection_type: open
  name: Astro Platform AgentToken Authorization API
  slug: open-astronomer-authorization-api
- collection_type: open
  name: Astro Platform AgentToken Cluster API
  slug: open-astronomer-cluster-api
- collection_type: open
  name: Astro Platform AgentToken Deploy API
  slug: open-astronomer-deploy-api
- collection_type: open
  name: Astro Platform AgentToken Deployment API
  slug: open-astronomer-deployment-api
- collection_type: open
  name: Astro Platform AgentToken Environment API
  slug: open-astronomer-environment-api
- collection_type: open
  name: Astro Platform AgentToken Invite API
  slug: open-astronomer-invite-api
- collection_type: open
  name: Astro Platform AgentToken Options API
  slug: open-astronomer-options-api
- collection_type: open
  name: Astro Platform AgentToken Organization API
  slug: open-astronomer-organization-api
- collection_type: open
  name: Astro Platform AgentToken Role API
  slug: open-astronomer-role-api
- collection_type: open
  name: Astro Platform AgentToken Team API
  slug: open-astronomer-team-api
- collection_type: open
  name: Astro Platform AgentToken User API
  slug: open-astronomer-user-api
- collection_type: open
  name: Astro Platform AgentToken Workspace API
  slug: open-astronomer-workspace-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/astronomer-astro-overlay.yaml
- group: auth
  title: ''
  type: TrustCenter
  url: security/astronomer-trust-center.yml
- group: company
  title: ''
  type: Website
  url: https://astronomer.io
- group: docs
  title: ''
  type: Documentation
  url: https://www.astronomer.io/docs
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.astronomer.io/docs/astro/api/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://www.astronomer.io/docs/astro/api/v-1/get-started
- group: company
  title: ''
  type: Blog
  url: https://www.astronomer.io/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/astronomer
- group: commercial
  title: ''
  type: Pricing
  url: https://www.astronomer.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.astronomer.io/try-astro/
- group: start
  title: ''
  type: Login
  url: https://cloud.astronomer.io
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.astronomer.io/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.astronomer.io/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.astronomer.io
- group: auth
  title: ''
  type: Compliance
  url: https://trust.astronomer.io
- group: auth
  title: ''
  type: Security
  url: https://www.astronomer.io/vulnerability-disclosure/
- group: agent
  title: ''
  type: MCPServer
  url: mcp/astronomer-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/astronomer-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/astronomer-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/astronomer-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/astronomer-cli.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/astronomer-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://www.astronomer.io/docs/astro/api/v-1/versioning-and-support
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/astronomer-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/astronomer-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/astronomer-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/astronomer-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/astronomer-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/astronomer-well-known.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Astronomer is the company behind Astro, a fully managed data operations platform powered by Apache Airflow. Astro lets data teams author, orchestrate, run, and observe data pipelines (DAGs) at scale across a managed control plane and data plane. The Astro Platform API is a production-ready REST API for programmatic control of Astro resources — Organizations, Workspaces, Deployments, Clusters, Users, Teams, role-based access control, API tokens, deploys, and environment objects — authenticated with bearer API tokens. Astronomer also ships the Astro CLI, an official Terraform provider, the Astro Python SDK, a documentation MCP server, and Astro Runtime, its distribution of Apache Airflow.
image: https://www.astronomer.io/img/logos/astronomer-logo.png
layout: provider
mcp_servers:
- description: ''
  name: astronomer-mcp.yml
  slug: astronomer-mcpyml
modified: '2026-07-18'
name: Astronomer
nav: Providers
network: true
overview: 'Astronomer publishes 15 APIs on the [APIs.io](https://apis.io/) network, including AgentToken API, AllowedIpAddressRange API, ApiToken API, and 12 more. Tagged areas include Company, Data Orchestration, Apache Airflow, Data Pipelines, and Data Engineering.


  Astronomer''s developer surface includes documentation, getting-started guide, engineering blog, pricing, signup flow, CLI, changelog, and 23 more developer resources.'
random_paper: 55
score:
  band: strong
  composite: 56.2
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 57.9
    developer_ergonomics: 64.7
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 55.3
  previous_composite: 56.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
    mcp: first-party
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/astronomer/refs/heads/main/screenshots/astronomer-2026-07-25T201511.png
security:
- kind: authentication
  name: Astronomer Authentication
  slug: astronomer-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Astronomer Domain Security
  slug: astronomer-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Astronomer Vulnerability Disclosure
  slug: astronomer-vulnerability-disclosure
  summary_line: Bugcrowd
- kind: trust-center
  name: Astronomer Trust Center
  slug: astronomer-trust-center
  summary_line: SOC 2, PCI DSS, GDPR
slug: astronomer
tags:
- Company
- Data Orchestration
- Apache Airflow
- Data Pipelines
- Data Engineering
- Workflow Automation
- MLOps
- Managed Platform
website: https://astronomer.io
---
