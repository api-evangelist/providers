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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Microsoft Azure Repo Agentic Access
  operation_count: 24
  slug: microsoft-azure-repo-agentic-access
  summary_line: 24 operations · 10 acting
api_count: 9
apis:
- description: Operations for accessing commit details and commit history within a repository, including diffs and changes.
  name: Azure Repos Commits API
  slug: microsoft-azure-repo-commits-api
- description: Operations for retrieving files, folders, and submodules from a repository. Files are blobs, folders are trees.
  name: Azure Repos Items API
  slug: microsoft-azure-repo-items-api
- description: Operations for managing reviewers on pull requests, including adding, removing, and updating reviewer votes.
  name: Azure Repos Pull Request Reviewers API
  slug: microsoft-azure-repo-pull-request-reviewers-api
- description: Operations for managing comment threads on pull requests, including creating threads and replying to comments.
  name: Azure Repos Pull Request Threads API
  slug: microsoft-azure-repo-pull-request-threads-api
- description: Operations for creating, retrieving, updating, and completing pull requests. Includes managing reviewers, labels, and merge options.
  name: Azure Repos Pull Requests API
  slug: microsoft-azure-repo-pull-requests-api
- description: Operations for listing and creating pushes, which represent one or more commits pushed to a repository branch.
  name: Azure Repos Pushes API
  slug: microsoft-azure-repo-pushes-api
- description: Operations for managing branches and tags (refs) including listing, creating, updating, and deleting refs.
  name: Azure Repos Refs API
  slug: microsoft-azure-repo-refs-api
- description: Operations for managing Git repositories including creating, listing, updating, and deleting repositories within a project.
  name: Azure Repos Repositories API
  slug: microsoft-azure-repo-repositories-api
- description: Operations for retrieving branch statistics such as commit counts ahead and behind relative to the default branch.
  name: Azure Repos Stats API
  slug: microsoft-azure-repo-stats-api
artifact_total: 18
collections:
- collection_type: open
  name: Azure Repos Git API
  slug: open-azure-repo-git-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-azure-repo-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/microsoft-azure-repo-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-azure-repo-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-azure-repo-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-azure-repo-scopes.yml
- group: start
  title: ''
  type: Portal
  url: https://learn.microsoft.com/en-us/azure/devops/repos/?view=azure-devops
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.microsoft.com/en-us/azure/devops/repos/get-started/
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/azure/devops/repos/git/?view=azure-devops
- group: auth
  title: ''
  type: Authentication
  url: https://learn.microsoft.com/en-us/azure/devops/integrate/get-started/authentication/authentication-guidance?view=azure-devops
- group: commercial
  title: ''
  type: Pricing
  url: https://azure.microsoft.com/en-us/pricing/details/devops/azure-devops-services/
- group: operate
  title: ''
  type: RateLimits
  url: https://learn.microsoft.com/en-us/azure/devops/integrate/concepts/rate-limits
- group: operate
  title: ''
  type: StatusPage
  url: https://status.dev.azure.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://azure.microsoft.com/en-us/support/legal/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: operate
  title: ''
  type: ChangeLog
  url: https://learn.microsoft.com/en-us/azure/devops/release-notes/features-timeline-released
- group: company
  title: ''
  type: Blog
  url: https://devblogs.microsoft.com/devops/
- group: operate
  title: ''
  type: Support
  url: https://azure.microsoft.com/en-us/support/devops/
- group: start
  title: ''
  type: Console
  url: https://dev.azure.com
- group: start
  title: ''
  type: Signup
  url: https://learn.microsoft.com/en-us/azure/devops/repos/get-started/sign-up-invite-teammates?view=azure-devops
- group: company
  title: ''
  type: Website
  url: https://azure.microsoft.com/en-us/services/devops/repos/
- group: build
  title: ''
  type: SDKs
  url: https://learn.microsoft.com/en-us/azure/devops/integrate/concepts/dotnet-client-libraries?view=azure-devops
- group: operate
  title: ''
  type: Community
  url: https://developercommunity.visualstudio.com/AzureDevOps
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/azure-devops
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/MicrosoftDocs/vsts-rest-api-specs
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@AzureDevOps
created: '2024-01-01'
description: Azure Repos is a set of version control tools that you can use to manage your code. Whether your software project is large or small, using version control as soon as possible is a good idea.
finops:
- name: Microsoft Azure Repo Finops
  service_category: Developer Tools / Source Control
  slug: microsoft-azure-repo-finops
image: https://docs.microsoft.com/en-us/azure/devops/repos/media/index/repos.svg
layout: provider
modified: '2026-05-19'
name: Azure Repos
nav: Providers
network: true
overview: 'Azure Repos publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Commits API, Items API, Pull Request Reviewers API, and 6 more. Tagged areas include DevOps, Git, Repositories, Source Control, and TFVC.


  Azure Repos'' developer surface includes authentication, developer portal, getting-started guide, documentation, pricing, changelog, engineering blog, and 18 more developer resources.'
plans:
- name: Microsoft Azure Repo Plans Pricing
  plan_count: 5
  slug: microsoft-azure-repo-plans-pricing
random_paper: 66
rate_limits:
- limit_count: 3
  name: Microsoft Azure Repo Rate Limits
  slug: microsoft-azure-repo-rate-limits
scopes:
- name: Microsoft Azure Repo Scopes
  scope_count: 3
  slug: microsoft-azure-repo-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: strong
  composite: 58.3
  delta: 0.0
  facets:
    commercial_clarity: 71.1
    contract_quality: 65.1
    developer_ergonomics: 58.7
    discoverability: 72.2
    governance: 0.0
    operational_transparency: 68.4
  previous_composite: 58.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-repo/refs/heads/main/screenshots/microsoft-azure-repo-2026-06-20T185433.png
security:
- kind: authentication
  name: Microsoft Azure Repo Authentication
  slug: microsoft-azure-repo-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Microsoft Azure Repo Domain Security
  slug: microsoft-azure-repo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Microsoft Azure Repo Vulnerability Disclosure
  slug: microsoft-azure-repo-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: microsoft-azure-repo
tags:
- DevOps
- Git
- Repositories
- Source Control
- TFVC
- Version Control
website: https://azure.microsoft.com/en-us/services/devops/repos/
---
