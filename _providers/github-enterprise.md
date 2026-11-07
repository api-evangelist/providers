---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 39.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Github Enterprise Agentic Access
  operation_count: 17
  slug: github-enterprise-agentic-access
  summary_line: 17 operations · 5 acting
api_count: 2
apis:
- description: The GitHub Enterprise Cloud GraphQL API at https://api.github.com/graphql (GitHub Enterprise Server serves it at https://{hostname}/api/graphql). The public schema SDL is published by GitHub at docs.g
  name: GitHub Enterprise Cloud GraphQL API
  slug: github-enterprise-graphql-api
- description: GitHub's official remote MCP server at https://api.githubcopilot.com/mcp/ (OAuth via github.com/login/oauth), also available as the open-source github/github-mcp-server local server.
  name: GitHub MCP Server
  slug: github-mcp-server
- baseURL: https://api.github.com
  baseurl_source: declared
  description: The Actions API from GitHub Enterprise — 2 operation(s) for actions.
  name: GitHub Enterprise Actions API
  slug: github-enterprise-actions-api
- baseURL: https://api.github.com
  baseurl_source: declared
  description: The Code Scanning API from GitHub Enterprise — 1 operation(s) for code scanning.
  name: GitHub Enterprise Code Scanning API
  slug: github-enterprise-code-scanning-api
- baseURL: https://api.github.com
  baseurl_source: declared
  description: The Enterprise Admin API from GitHub Enterprise — 1 operation(s) for enterprise admin.
  name: GitHub Enterprise Admin API
  slug: github-enterprise-enterprise-admin-api
- baseURL: https://api.github.com
  baseurl_source: declared
  description: The Issues API from GitHub Enterprise — 1 operation(s) for issues.
  name: GitHub Enterprise Issues API
  slug: github-enterprise-issues-api
- baseURL: https://api.github.com
  baseurl_source: declared
  description: The SCIM API from GitHub Enterprise — 1 operation(s) for scim.
  name: GitHub Enterprise SCIM API
  slug: github-enterprise-scim-api
- baseURL: https://api.github.com
  baseurl_source: declared
  description: The Users API from GitHub Enterprise — 2 operation(s) for users.
  name: GitHub Enterprise Users API
  slug: github-enterprise-users-api
- baseURL: https://api.github.com
  baseurl_source: declared
  description: Activity APIs provide access to notifications, subscriptions, and timelines.
  name: GitHub Enterprise Activity API
  slug: github-enterprise-activity-api
- baseURL: https://api.github.com
  baseurl_source: declared
  description: Endpoints to manage and interact with agent automations.
  name: GitHub Enterprise Agent Automations API
  slug: github-enterprise-agent-automations-api
- baseURL: https://api.github.com
  baseurl_source: declared
  description: Endpoints to manage Agent Merge enrollment for pull requests.
  name: GitHub Enterprise Agent Merge API
  slug: github-enterprise-agent-merge-api
- baseURL: https://api.github.com
  baseurl_source: declared
  description: Endpoints to manage and interact with agent tasks.
  name: GitHub Enterprise Agent Tasks API
  slug: github-enterprise-agent-tasks-api
- baseURL: https://api.github.com
  baseurl_source: declared
  description: Endpoints for Agents secrets and variables.
  name: GitHub Enterprise Agents API
  slug: github-enterprise-agents-api
- baseURL: https://api.github.com
  baseurl_source: declared
  description: Information for integrations and installations.
  name: GitHub Enterprise Apps API
  slug: github-enterprise-apps-api
- baseURL: https://api.github.com
  baseurl_source: declared
  description: Monitor charges and usage from Actions and Packages.
  name: GitHub Enterprise Billing API
  slug: github-enterprise-billing-api
- baseURL: https://api.github.com
  baseurl_source: declared
  description: Endpoints to manage campaigns via the REST API.
  name: GitHub Enterprise Campaigns API
  slug: github-enterprise-campaigns-api
- baseURL: https://api.github.com
  baseurl_source: declared
  description: Rich interactions with checks run by your integrations.
  name: GitHub Enterprise Checks API
  slug: github-enterprise-checks-api
- baseURL: https://api.github.com
  baseurl_source: declared
  description: Interact with GitHub Classroom.
  name: GitHub Enterprise Classroom API
  slug: github-enterprise-classroom-api
- baseURL: https://api.github.com
  baseurl_source: declared
  description: Insights into reliability, maintainability, and efficiency of your codebase.
  name: GitHub Enterprise Code Quality API
  slug: github-enterprise-code-quality-api
- baseURL: https://api.github.com
  baseurl_source: declared
  description: Endpoints to manage Code security using the REST API.
  name: GitHub Enterprise Code Security API
  slug: github-enterprise-code-security-api
- baseURL: https://api.github.com
  baseurl_source: declared
  description: Insight into codes of conduct for your communities.
  name: GitHub Enterprise Codes Of Conduct API
  slug: github-enterprise-codes-of-conduct-api
- baseURL: https://api.github.com
  baseurl_source: declared
  description: Endpoints to manage Codespaces using the REST API.
  name: GitHub Enterprise Codespaces API
  slug: github-enterprise-codespaces-api
- baseURL: https://api.github.com
  baseurl_source: declared
  description: Endpoints to manage Copilot using the REST API.
  name: GitHub Enterprise Copilot API
  slug: github-enterprise-copilot-api
- baseURL: https://api.github.com
  baseurl_source: declared
  description: Endpoints to manage Copilot Spaces using the REST API.
  name: GitHub Enterprise Copilot Spaces API
  slug: github-enterprise-copilot-spaces-api
- baseURL: https://api.github.com
  baseurl_source: declared
  description: Revoke compromised or leaked GitHub credentials.
  name: GitHub Enterprise Credentials API
  slug: github-enterprise-credentials-api
- baseURL: https://api.github.com
  baseurl_source: declared
  description: Endpoints to manage Dependabot.
  name: GitHub Enterprise Dependabot API
  slug: github-enterprise-dependabot-api
- baseURL: https://api.github.com
  baseurl_source: declared
  description: Endpoints to access Dependency Graph features.
  name: GitHub Enterprise Dependency Graph API
  slug: github-enterprise-dependency-graph-api
- baseURL: https://api.github.com
  baseurl_source: declared
  description: List emojis available to use on GitHub.
  name: GitHub Enterprise Emojis API
  slug: github-enterprise-emojis-api
- baseURL: https://api.github.com
  baseurl_source: declared
  description: Endpoints to manage GitHub Enterprise Team memberships.
  name: GitHub Enterprise Enterprise Team Memberships API
  slug: github-enterprise-enterprise-team-memberships-api
- baseURL: https://api.github.com
  baseurl_source: declared
  description: Endpoints to manage GitHub Enterprise Team organization assignments.
  name: GitHub Enterprise Enterprise Team Organizations API
  slug: github-enterprise-enterprise-team-organizations-api
- baseURL: https://api.github.com
  baseurl_source: declared
  description: Endpoints to manage GitHub Enterprise Teams.
  name: GitHub Enterprise Enterprise Teams API
  slug: github-enterprise-enterprise-teams-api
- baseURL: https://api.github.com
  baseurl_source: declared
  description: View, modify your gists.
  name: GitHub Enterprise Gists API
  slug: github-enterprise-gists-api
- baseURL: https://api.github.com
  baseurl_source: declared
  description: Raw Git functionality.
  name: GitHub Enterprise Git API
  slug: github-enterprise-git-api
- baseURL: https://api.github.com
  baseurl_source: declared
  description: View gitignore templates
  name: GitHub Enterprise Gitignore API
  slug: github-enterprise-gitignore-api
- baseURL: https://api.github.com
  baseurl_source: declared
  description: Manage hosted compute networking resources.
  name: GitHub Enterprise Hosted Compute API
  slug: github-enterprise-hosted-compute-api
- baseURL: https://api.github.com
  baseurl_source: declared
  description: Owner or admin management of users interactions.
  name: GitHub Enterprise Interactions API
  slug: github-enterprise-interactions-api
- baseURL: https://api.github.com
  baseurl_source: declared
  description: View various OSS licenses.
  name: GitHub Enterprise Licenses API
  slug: github-enterprise-licenses-api
- baseURL: https://api.github.com
  baseurl_source: declared
  description: Render GitHub flavored Markdown
  name: GitHub Enterprise Markdown API
  slug: github-enterprise-markdown-api
- baseURL: https://api.github.com
  baseurl_source: declared
  description: Interact with GitHub Merge Queues.
  name: GitHub Enterprise Merge Queue API
  slug: github-enterprise-merge-queue-api
- baseURL: https://api.github.com
  baseurl_source: declared
  description: Endpoints that give information about the API.
  name: GitHub Enterprise Meta API
  slug: github-enterprise-meta-api
- baseURL: https://api.github.com
  baseurl_source: declared
  description: Move projects to or from GitHub.
  name: GitHub Enterprise Migrations API
  slug: github-enterprise-migrations-api
- baseURL: https://api.github.com
  baseurl_source: declared
  description: Endpoints to manage GitHub OIDC configuration using the REST API.
  name: GitHub Enterprise Oidc API
  slug: github-enterprise-oidc-api
- baseURL: https://api.github.com
  baseurl_source: declared
  description: Interact with organizations.
  name: GitHub Enterprise Orgs API
  slug: github-enterprise-orgs-api
- baseURL: https://api.github.com
  baseurl_source: declared
  description: Manage packages for authenticated users and organizations.
  name: GitHub Enterprise Packages API
  slug: github-enterprise-packages-api
- baseURL: https://api.github.com
  baseurl_source: declared
  description: Manage private registry configurations.
  name: GitHub Enterprise Private Registries API
  slug: github-enterprise-private-registries-api
- baseURL: https://api.github.com
  baseurl_source: declared
  description: Endpoints to manage Projects using the REST API.
  name: GitHub Enterprise Projects API
  slug: github-enterprise-projects-api
- baseURL: https://api.github.com
  baseurl_source: declared
  description: Interact with GitHub Pull Requests.
  name: GitHub Enterprise Pulls API
  slug: github-enterprise-pulls-api
- baseURL: https://api.github.com
  baseurl_source: declared
  description: Check your current rate limit status.
  name: GitHub Enterprise Rate Limit API
  slug: github-enterprise-rate-limit-api
- baseURL: https://api.github.com
  baseurl_source: declared
  description: Interact with reactions to various GitHub entities.
  name: GitHub Enterprise Reactions API
  slug: github-enterprise-reactions-api
- baseURL: https://api.github.com
  baseurl_source: declared
  description: Interact with GitHub Repos.
  name: GitHub Enterprise Repos API
  slug: github-enterprise-repos-api
- baseURL: https://api.github.com
  baseurl_source: declared
  description: Search for specific items on GitHub.
  name: GitHub Enterprise Search API
  slug: github-enterprise-search-api
- baseURL: https://api.github.com
  baseurl_source: declared
  description: Retrieve secret scanning alerts from a repository.
  name: GitHub Enterprise Secret Scanning API
  slug: github-enterprise-secret-scanning-api
- baseURL: https://api.github.com
  baseurl_source: declared
  description: Manage security advisories.
  name: GitHub Enterprise Security Advisories API
  slug: github-enterprise-security-advisories-api
- baseURL: https://api.github.com
  baseurl_source: declared
  description: Server statistics
  name: GitHub Enterprise Server Statistics API
  slug: github-enterprise-server-statistics-api
- baseURL: https://api.github.com
  baseurl_source: declared
  description: Interact with GitHub Teams.
  name: GitHub Enterprise Teams API
  slug: github-enterprise-teams-api
- baseURL: https://api.github.com
  baseurl_source: declared
  description: The Organizations API from GitHub Enterprise — 1 operation(s) for organizations.
  name: GitHub Enterprise Organizations API
  slug: github-enterprise-organizations-api
- baseURL: https://api.github.com
  baseurl_source: declared
  description: The Pull Requests API from GitHub Enterprise — 1 operation(s) for pull requests.
  name: GitHub Enterprise Pull Requests API
  slug: github-enterprise-pull-requests-api
- baseURL: https://api.github.com
  baseurl_source: declared
  description: The Repositories API from GitHub Enterprise — 2 operation(s) for repositories.
  name: GitHub Enterprise Repositories API
  slug: github-enterprise-repositories-api
artifact_total: 91
asyncapis:
- description: ''
  name: Github Enterprise Webhooks
  slug: github-enterprise-webhooks
collections:
- collection_type: open
  name: GitHub Enterprise Cloud REST Actions API
  slug: open-github-enterprise-actions-api
- collection_type: open
  name: GitHub Enterprise Cloud REST Actions Code Scanning API
  slug: open-github-enterprise-code-scanning-api
- collection_type: open
  name: GitHub Enterprise Cloud REST Actions Enterprise Admin API
  slug: open-github-enterprise-enterprise-admin-api
- collection_type: open
  name: GitHub Enterprise Cloud REST Actions Issues API
  slug: open-github-enterprise-issues-api
- collection_type: open
  name: GitHub Enterprise Cloud REST Actions Organizations API
  slug: open-github-enterprise-organizations-api
- collection_type: open
  name: GitHub Enterprise Cloud REST Actions Pull Requests API
  slug: open-github-enterprise-pull-requests-api
- collection_type: open
  name: GitHub Enterprise Cloud REST Actions Repositories API
  slug: open-github-enterprise-repositories-api
- collection_type: open
  name: GitHub Enterprise Cloud REST Actions SCIM API
  slug: open-github-enterprise-scim-api
- collection_type: open
  name: GitHub Enterprise Cloud REST Actions Users API
  slug: open-github-enterprise-users-api
- collection_type: open
  name: GitHub Enterprise Cloud REST API
  slug: open-github-enterprise
common:
- group: operate
  href: https://artifacts.apis.io/github-enterprise/rate-limits/github-enterprise-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/github-enterprise-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/github-enterprise/plans/github-enterprise-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/github-enterprise-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/github-enterprise/rules/github-enterprise-rules.yml
  title: ''
  type: Spectral
  url: rules/github-enterprise-rules.yml
- group: design
  href: https://artifacts.apis.io/github-enterprise/json-ld/github-enterprise-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/github-enterprise-context.jsonld
- group: design
  href: https://artifacts.apis.io/github-enterprise/vocabulary/github-enterprise-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/github-enterprise-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/github-enterprise/asyncapi/github-enterprise-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/github-enterprise-webhooks.yml
- group: design
  href: https://artifacts.apis.io/github-enterprise/data-model/github-enterprise-data-model.yml
  title: ''
  type: DataModel
  url: data-model/github-enterprise-data-model.yml
- group: build
  href: https://artifacts.apis.io/github-enterprise/cli/github-enterprise-cli.yml
  title: ''
  type: CLI
  url: cli/github-enterprise-cli.yml
- group: design
  href: https://artifacts.apis.io/github-enterprise/conventions/github-enterprise-conventions.yml
  title: ''
  type: Conventions
  url: conventions/github-enterprise-conventions.yml
- group: design
  href: https://artifacts.apis.io/github-enterprise/lifecycle/github-enterprise-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/github-enterprise-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/github-enterprise/errors/github-enterprise-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/github-enterprise-problem-types.yml
- group: design
  href: https://artifacts.apis.io/github-enterprise/conformance/github-enterprise-conformance.yml
  title: ''
  type: Conformance
  url: conformance/github-enterprise-conformance.yml
- group: auth
  href: https://artifacts.apis.io/github-enterprise/well-known/github-enterprise-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/github-enterprise-www-security.txt
- group: agent
  href: https://artifacts.apis.io/github-enterprise/well-known/github-enterprise-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/github-enterprise-well-known.yml
- group: other
  href: https://artifacts.apis.io/github-enterprise/hosts/github-enterprise-hosts.yml
  title: ''
  type: Hosts
  url: hosts/github-enterprise-hosts.yml
- group: other
  href: https://artifacts.apis.io/github-enterprise/vendors/github-enterprise-vendors.yml
  title: ''
  type: Vendors
  url: vendors/github-enterprise-vendors.yml
- group: build
  href: https://artifacts.apis.io/github-enterprise/packages/github-enterprise-packages.yml
  title: ''
  type: SDKs
  url: packages/github-enterprise-packages.yml
- group: build
  href: https://artifacts.apis.io/github-enterprise/packages/github-enterprise-packages.yml
  title: ''
  type: Packages
  url: packages/github-enterprise-packages.yml
- group: auth
  href: https://artifacts.apis.io/github-enterprise/security/github-enterprise-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/github-enterprise-domain-security.yml
- group: other
  href: https://artifacts.apis.io/github-enterprise/capabilities/github-enterprise-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/github-enterprise-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/github-enterprise/agentic-access/github-enterprise-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/github-enterprise-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/github-enterprise/authentication/github-enterprise-authentication.yml
  title: ''
  type: Authentication
  url: authentication/github-enterprise-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/github-enterprise
- group: company
  title: ''
  type: Website
  url: https://github.com/enterprise
- group: docs
  title: ''
  type: Documentation
  url: https://docs.github.com/en/enterprise-cloud@latest
- group: commercial
  title: ''
  type: Pricing
  url: https://github.com/pricing
- group: start
  title: ''
  type: Signup
  url: https://github.com/enterprise/contact
- group: operate
  title: ''
  type: StatusPage
  url: https://www.githubstatus.com
- group: docs
  title: ''
  type: OpenAPI Repository
  url: https://github.com/github/rest-api-description
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.github.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://github.blog/feed/
created: '2026-05-11'
description: 'GitHub Enterprise is GitHub''s offering for organizations that need advanced security, compliance, identity, and scale on top of the GitHub platform. It ships in two flavors: GitHub Enterprise Cloud, a hosted multi-tenant service on api.github.com with enterprise-managed users and SAML SSO; and GitHub Enterprise Server (GHES), a self-hosted appliance with the same REST and GraphQL APIs served from a customer''s domain at /api/v3 and /api/graphql. Both expose the full GitHub REST API for repositories, issues, pull requests, actions, packages, advanced security, audit log, SCIM, and admin operations, authenticated with personal access tokens or GitHub App tokens.'
graphqls:
- description: Hosted GitHub Enterprise Cloud REST API. Provides full access to repositories, issues, pull requests, GitHub Actions, packages, code scanning, secret scanning, Dependabot, audit log, SCIM provisioning
  name: GitHub Enterprise GraphQL API
  slug: github-enterprise-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/github-enterprise.png
json_schemas:
- name: App Permissions
  property_count: 60
  slug: github-enterprise-app-permissions
- name: CodeScanningAlert
  property_count: 4
  slug: github-enterprise-code-scanning-alert
- name: Full Repository
  property_count: 105
  slug: github-enterprise-full-repository
- name: Issue
  property_count: 8
  slug: github-enterprise-issue
- name: Minimal Repository
  property_count: 90
  slug: github-enterprise-minimal-repository
- name: Organization Full
  property_count: 68
  slug: github-enterprise-organization-full
- name: Organization
  property_count: 6
  slug: github-enterprise-organization
- name: PullRequest
  property_count: 8
  slug: github-enterprise-pull-request
- name: Repository
  property_count: 98
  slug: github-enterprise-repository
- name: Team Repository
  property_count: 89
  slug: github-enterprise-team-repository
- name: User
  property_count: 7
  slug: github-enterprise-user
- name: WorkflowRun
  property_count: 8
  slug: github-enterprise-workflow-run
- name: Workflow
  property_count: 4
  slug: github-enterprise-workflow
jsonld:
- class_count: 120
  name: Github Enterprise Context
  property_count: 519
  slug: github-enterprise-context
layout: provider
mcp_servers:
- description: GitHub's official MCP server, hosted remotely at api.githubcopilot.com/mcp/ and also published as an open-source local server (github/github-mcp-server). Tools cover repositories, issues, pull request
  name: GitHub MCP Server
  slug: github-mcp-server
modified: '2026-11-05'
name: GitHub Enterprise
nav: Providers
network: true
overview: 'GitHub Enterprise publishes 58 API contracts indexed on the [APIs.io](https://apis.io/) network, including Actions API, Code Scanning API, Admin API, and 55 more. Tagged areas include Version Control, DevOps, CI/CD, Code Hosting, and Enterprise.


  The GitHub Enterprise catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  GitHub Enterprise''s developer surface includes CLI, authentication, documentation, pricing, signup flow, engineering blog, and 25 more developer resources.'
plans:
- name: Github Enterprise Plans Pricing
  plan_count: 3
  slug: github-enterprise-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 10
  name: Github Enterprise Rate Limits
  slug: github-enterprise-rate-limits
rules:
- authorship: generated
  effective_rule_count: 113
  extends:
  - spectral:oas
  name: GitHub Enterprise API Rules
  rule_count: 72
  severity_counts:
    error: 45
    hint: 0
    info: 7
    warn: 20
  slug: github-enterprise-rules
score:
  band: developing
  composite: 53.3
  coverage:
    artifact_dirs: 31
    catalog_earned: 86.8
    catalog_earned_first_party: 24.0
    catalog_gap: 28.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 25.7
  facets:
    access_clarity: 44.7
    contract_governance: 22.0
    contract_quality: 75.2
    developer_ergonomics: 38.1
    discoverability: 71.7
    operational_transparency: 65.8
  previous_composite: 27.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 56
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/github-enterprise/github-enterprise-2026-06-20T181846.png
security:
- kind: authentication
  name: Github Enterprise Authentication
  slug: github-enterprise-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Github Enterprise Domain Security
  slug: github-enterprise-domain-security
  summary_line: TLSv1.3 · DMARC
slug: github-enterprise
tags:
- Version Control
- DevOps
- CI/CD
- Code Hosting
- Enterprise
- Self-Hosted
- SAML SSO
- SCIM
- Advanced Security
- Developer Tools
---
