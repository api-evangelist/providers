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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.3
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 156
  human_in_the_loop: 4
  name: Bitbucket Pipelines Agentic Access
  operation_count: 337
  slug: bitbucket-pipelines-agentic-access
  summary_line: 337 operations · 156 acting · 4 human-in-the-loop
api_count: 23
apis:
- description: The addon resource is intended to use used by Bitbucket Cloud Connect Apps, and only supports JWT authentication.
  name: Bitbucket Pipelines Addon API
  slug: bitbucket-pipelines-addon-api
- description: Repository owners and administrators can set branch management rules on a repository that control what can be pushed by whom. Through these rules, you can enforce a project or team workflow. For examp
  name: Bitbucket Pipelines Branch restrictions API
  slug: bitbucket-pipelines-branch-restrictions-api
- description: The branching model resource is used to modify the branching model for a repository. You can use the branching model to define a branch based workflow for your repositories. When you map your workflow
  name: Bitbucket Pipelines Branching model API
  slug: bitbucket-pipelines-branching-model-api
- description: Commit statuses provide a way to tag commits with meta data, like automated build results.
  name: Bitbucket Pipelines Commit statuses API
  slug: bitbucket-pipelines-commit-statuses-api
- description: These are the repository's commits. They are paginated and returned in reverse chronological order, similar to the output of git log.
  name: Bitbucket Pipelines Commits API
  slug: bitbucket-pipelines-commits-api
- description: Teams are deploying code faster than ever, thanks to continuous delivery practices and tools like Bitbucket Pipelines. Bitbucket Deployments gives teams visibility into their deployment environments a
  name: Bitbucket Pipelines Deployments API
  slug: bitbucket-pipelines-deployments-api
- description: Access the list of download links associated with the repository.
  name: Bitbucket Pipelines Downloads API
  slug: bitbucket-pipelines-downloads-api
- description: The GPG resource allows you to manage GPG keys.
  name: Bitbucket Pipelines GPG API
  slug: bitbucket-pipelines-gpg-api
- description: The issue resources provide functionality for getting information on issues in an issue tracker, creating new issues, updating them and deleting them. You can access public issues without authenticati
  name: Bitbucket Pipelines Issue tracker API
  slug: bitbucket-pipelines-issue-tracker-api
- description: Bitbucket Pipelines brings continuous delivery to Bitbucket Cloud, empowering teams with full branching to deployment visibility and faster feedback loops.
  name: Bitbucket Pipelines Pipelines API
  slug: bitbucket-pipelines-pipelines-api
- description: Bitbucket Cloud projects make it easier for teams to focus on a goal, product, or process by organizing their repositories.
  name: Bitbucket Pipelines Projects API
  slug: bitbucket-pipelines-projects-api
- description: The properties API from Bitbucket Pipelines — 4 operation(s) for properties.
  name: Bitbucket Pipelines properties API
  slug: bitbucket-pipelines-properties-api
- description: 'Pull requests are a feature that makes it easier for developers to collaborate using Bitbucket. They provide a user-friendly web interface for discussing proposed changes before integrating them into '
  name: Bitbucket Pipelines Pullrequests API
  slug: bitbucket-pipelines-pullrequests-api
- description: The refs resource allows you access branches and tags in a repository. By default, results will be in the order the underlying source control system returns them and identical to the ordering one sees
  name: Bitbucket Pipelines Refs API
  slug: bitbucket-pipelines-refs-api
- description: Code insights provides reports, annotations, and metrics to help you and your team improve code quality in pull requests throughout the code review process. Some of the available code insights are sta
  name: Bitbucket Pipelines Reports API
  slug: bitbucket-pipelines-reports-api
- description: A Git repository is a virtual storage of your project. It allows you to save versions of your code, which you can access when needed. The repo resource allows you to access public repos, or repos that
  name: Bitbucket Pipelines Repositories API
  slug: bitbucket-pipelines-repositories-api
- description: The Search API from Bitbucket Pipelines — 3 operation(s) for search.
  name: Bitbucket Pipelines Search API
  slug: bitbucket-pipelines-search-api
- description: Snippets allow you share code segments or files with yourself, members of your workspace, or the world. Like pull requests, repositories and workspaces, the full set of snippets is defined by what the
  name: Bitbucket Pipelines Snippets API
  slug: bitbucket-pipelines-snippets-api
- description: Browse the source code in the repository and create new commits by uploading.
  name: Bitbucket Pipelines Source API
  slug: bitbucket-pipelines-source-api
- description: The SSH resource allows you to manage SSH keys.
  name: Bitbucket Pipelines SSH API
  slug: bitbucket-pipelines-ssh-api
- description: The users resource allows you to access public information associated with a user account. Most resources in the users endpoint have been deprecated in favor of workspaces.
  name: Bitbucket Pipelines Users API
  slug: bitbucket-pipelines-users-api
- description: 'Webhooks provide a way to configure Bitbucket Cloud to make requests to your server (or another external service) whenever certain events occur in Bitbucket Cloud. A webhook consists of: * A subject -'
  name: Bitbucket Pipelines Webhooks API
  slug: bitbucket-pipelines-webhooks-api
- description: A workspace is where you create repositories, collaborate on your code, and organize different streams of work in your Bitbucket Cloud account. Workspaces replace the use of teams and users in API cal
  name: Bitbucket Pipelines Workspaces API
  slug: bitbucket-pipelines-workspaces-api
artifact_total: 56
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Bitbucket Addon API
  slug: open-bitbucket-pipelines-addon-api
- collection_type: open
  name: Bitbucket Addon Branch restrictions API
  slug: open-bitbucket-pipelines-branch-restrictions-api
- collection_type: open
  name: Bitbucket Addon Branching model API
  slug: open-bitbucket-pipelines-branching-model-api
- collection_type: open
  name: Bitbucket Addon Commit statuses API
  slug: open-bitbucket-pipelines-commit-statuses-api
- collection_type: open
  name: Bitbucket Addon Commits API
  slug: open-bitbucket-pipelines-commits-api
- collection_type: open
  name: Bitbucket Addon Deployments API
  slug: open-bitbucket-pipelines-deployments-api
- collection_type: open
  name: Bitbucket Addon Downloads API
  slug: open-bitbucket-pipelines-downloads-api
- collection_type: open
  name: Bitbucket Addon GPG API
  slug: open-bitbucket-pipelines-gpg-api
- collection_type: open
  name: Bitbucket Addon Issue tracker API
  slug: open-bitbucket-pipelines-issue-tracker-api
- collection_type: open
  name: Bitbucket Addon Pipelines API
  slug: open-bitbucket-pipelines-pipelines-api
- collection_type: open
  name: Bitbucket Addon Projects API
  slug: open-bitbucket-pipelines-projects-api
- collection_type: open
  name: Bitbucket Addon properties API
  slug: open-bitbucket-pipelines-properties-api
- collection_type: open
  name: Bitbucket Addon Pullrequests API
  slug: open-bitbucket-pipelines-pullrequests-api
- collection_type: open
  name: Bitbucket Addon Refs API
  slug: open-bitbucket-pipelines-refs-api
- collection_type: open
  name: Bitbucket Addon Reports API
  slug: open-bitbucket-pipelines-reports-api
- collection_type: open
  name: Bitbucket Addon Repositories API
  slug: open-bitbucket-pipelines-repositories-api
- collection_type: open
  name: Bitbucket Addon Search API
  slug: open-bitbucket-pipelines-search-api
- collection_type: open
  name: Bitbucket Addon Snippets API
  slug: open-bitbucket-pipelines-snippets-api
- collection_type: open
  name: Bitbucket Addon Source API
  slug: open-bitbucket-pipelines-source-api
- collection_type: open
  name: Bitbucket Addon SSH API
  slug: open-bitbucket-pipelines-ssh-api
- collection_type: open
  name: Bitbucket Addon Users API
  slug: open-bitbucket-pipelines-users-api
- collection_type: open
  name: Bitbucket Addon Webhooks API
  slug: open-bitbucket-pipelines-webhooks-api
- collection_type: open
  name: Bitbucket Addon Workspaces API
  slug: open-bitbucket-pipelines-workspaces-api
- collection_type: open
  name: Bitbucket API
  slug: open-bitbucket-pipelines
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bitbucket-pipelines-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/bitbucket-pipelines-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bitbucket-pipelines-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bitbucket-pipelines-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/bitbucket-pipelines-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://bitbucket.org/product/features/pipelines
- group: docs
  title: ''
  type: Documentation
  url: https://support.atlassian.com/bitbucket-cloud/docs/get-started-with-bitbucket-pipelines/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.atlassian.com/software/bitbucket/pricing
- group: build
  title: ''
  type: GitHub
  url: https://bitbucket.org/atlassian/atlassian-pipelines-pipes
- group: operate
  title: ''
  type: StatusPage
  url: https://bitbucket.status.atlassian.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/bitbucket-pipelines-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/bitbucket-pipelines-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/bitbucket-pipelines-finops.yml
created: '2026-05-08'
description: Bitbucket Pipelines is Atlassian's built-in CI/CD service for Bitbucket Cloud, with cloud-hosted and self-hosted runners and YAML-defined pipelines. Pipelines is consumed via the Bitbucket Cloud REST API v2.0 under the /pipelines/ resource family. Atlassian publishes a Swagger 2.0 specification for the full Bitbucket Cloud API.
finops:
- name: Bitbucket Pipelines Finops
  service_category: DevOps / CI/CD
  slug: bitbucket-pipelines-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bitbucket-pipelines.png
layout: provider
modified: '2026-05-19'
name: Bitbucket Pipelines
nav: Providers
network: true
overview: 'Bitbucket Pipelines publishes 23 APIs on the [APIs.io](https://apis.io/) network, including Addon API, Branch restrictions API, Branching model API, and 20 more. Tagged areas include DevOps, CI/CD, Pipelines, Atlassian, and Bitbucket.


  Bitbucket Pipelines'' developer surface includes authentication, documentation, pricing, GitHub presence, and 9 more developer resources.'
plans:
- name: Bitbucket Pipelines Plans Pricing
  plan_count: 4
  slug: bitbucket-pipelines-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 4
  name: Bitbucket Pipelines Rate Limits
  slug: bitbucket-pipelines-rate-limits
scopes:
- name: Bitbucket Pipelines Scopes
  scope_count: 26
  slug: bitbucket-pipelines-scopes
  summary_line: 26 scopes · authorizationCode
score:
  band: thin
  composite: 36.2
  delta: 1.4
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 56.3
    developer_ergonomics: 28.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 28.9
  previous_composite: 34.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 23
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bitbucket-pipelines/refs/heads/main/screenshots/bitbucket-pipelines-2026-06-20T173303.png
security:
- kind: authentication
  name: Bitbucket Pipelines Authentication
  slug: bitbucket-pipelines-authentication
  summary_line: apiKey/http/oauth2 · 3 schemes
- kind: domain-security
  name: Bitbucket Pipelines Domain Security
  slug: bitbucket-pipelines-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Bitbucket Pipelines Vulnerability Disclosure
  slug: bitbucket-pipelines-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: bitbucket-pipelines
tags:
- DevOps
- CI/CD
- Pipelines
- Atlassian
- Bitbucket
- Hosted
- Self-Hosted Runners
website: https://bitbucket.org/product/features/pipelines
---
