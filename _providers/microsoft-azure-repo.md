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
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.5
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Microsoft Azure Repo Agentic Access
  operation_count: 24
  slug: microsoft-azure-repo-agentic-access
  summary_line: 24 operations · 10 acting
api_count: 1
apis:
- baseURL: https://dev.azure.com/{organization}/{project}/_apis/git
  baseurl_source: declared
  description: Operations for accessing commit details and commit history within a repository, including diffs and changes.
  name: Azure Repos Commits API
  slug: microsoft-azure-repo-commits-api
- baseURL: https://dev.azure.com/{organization}/{project}/_apis/git
  baseurl_source: declared
  description: Operations for retrieving files, folders, and submodules from a repository. Files are blobs, folders are trees.
  name: Azure Repos Items API
  slug: microsoft-azure-repo-items-api
- baseURL: https://dev.azure.com/{organization}/{project}/_apis/git
  baseurl_source: declared
  description: Operations for managing reviewers on pull requests, including adding, removing, and updating reviewer votes.
  name: Azure Repos Pull Request Reviewers API
  slug: microsoft-azure-repo-pull-request-reviewers-api
- baseURL: https://dev.azure.com/{organization}/{project}/_apis/git
  baseurl_source: declared
  description: Operations for managing comment threads on pull requests, including creating threads and replying to comments.
  name: Azure Repos Pull Request Threads API
  slug: microsoft-azure-repo-pull-request-threads-api
- baseURL: https://dev.azure.com/{organization}/{project}/_apis/git
  baseurl_source: declared
  description: Operations for creating, retrieving, updating, and completing pull requests. Includes managing reviewers, labels, and merge options.
  name: Azure Repos Pull Requests API
  slug: microsoft-azure-repo-pull-requests-api
- baseURL: https://dev.azure.com/{organization}/{project}/_apis/git
  baseurl_source: declared
  description: Operations for listing and creating pushes, which represent one or more commits pushed to a repository branch.
  name: Azure Repos Pushes API
  slug: microsoft-azure-repo-pushes-api
- baseURL: https://dev.azure.com/{organization}/{project}/_apis/git
  baseurl_source: declared
  description: Operations for managing branches and tags (refs) including listing, creating, updating, and deleting refs.
  name: Azure Repos Refs API
  slug: microsoft-azure-repo-refs-api
- baseURL: https://dev.azure.com/{organization}/{project}/_apis/git
  baseurl_source: declared
  description: Operations for managing Git repositories including creating, listing, updating, and deleting repositories within a project.
  name: Azure Repos Repositories API
  slug: microsoft-azure-repo-repositories-api
- baseURL: https://dev.azure.com/{organization}/{project}/_apis/git
  baseurl_source: declared
  description: Operations for retrieving branch statistics such as commit counts ahead and behind relative to the default branch.
  name: Azure Repos Stats API
  slug: microsoft-azure-repo-stats-api
artifact_total: 27
collections:
- collection_type: open
  name: Azure Repos Git API
  slug: open-azure-repo-git-api
- collection_type: open
  name: Azure Repos Git Commits API
  slug: open-microsoft-azure-repo-commits-api
- collection_type: open
  name: Azure Repos Git Commits Items API
  slug: open-microsoft-azure-repo-items-api
- collection_type: open
  name: Azure Repos Git Commits Pull Request Threads API
  slug: open-microsoft-azure-repo-pull-request-threads-api
- collection_type: open
  name: Azure Repos Git Commits Pull Requests API
  slug: open-microsoft-azure-repo-pull-requests-api
- collection_type: open
  name: Azure Repos Git Commits Pushes API
  slug: open-microsoft-azure-repo-pushes-api
- collection_type: open
  name: Azure Repos Git Commits Refs API
  slug: open-microsoft-azure-repo-refs-api
- collection_type: open
  name: Azure Repos Git Commits Repositories API
  slug: open-microsoft-azure-repo-repositories-api
- collection_type: open
  name: Azure Repos Git Commits Stats API
  slug: open-microsoft-azure-repo-stats-api
common:
- group: commercial
  href: https://artifacts.apis.io/microsoft-azure-repo/plans/microsoft-azure-repo-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/microsoft-azure-repo-plans-pricing.yml
- group: commercial
  href: https://artifacts.apis.io/microsoft-azure-repo/finops/microsoft-azure-repo-finops.yml
  title: ''
  type: FinOps
  url: finops/microsoft-azure-repo-finops.yml
- group: other
  href: https://artifacts.apis.io/microsoft-azure-repo/capabilities/microsoft-azure-repo-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/microsoft-azure-repo-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/microsoft-azure-repo/agentic-access/microsoft-azure-repo-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-azure-repo-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-repo/security/microsoft-azure-repo-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/microsoft-azure-repo-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-repo/security/microsoft-azure-repo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/microsoft-azure-repo-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-repo/authentication/microsoft-azure-repo-authentication.yml
  title: ''
  type: Authentication
  url: authentication/microsoft-azure-repo-authentication.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-repo/scopes/microsoft-azure-repo-scopes.yml
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
- has_sources: true
  method: derived
  name: Microsoft Azure Repo Finops
  primary_unit: user
  service_category: ''
  slug: microsoft-azure-repo-finops
  template: false
image: https://docs.microsoft.com/en-us/azure/devops/repos/media/index/repos.svg
layout: provider
modified: '2026-05-19'
name: Azure Repos
nav: Providers
network: true
overview: 'Azure Repos publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Commits API, Items API, Pull Request Reviewers API, and 6 more. Tagged areas include Developer Tools, DevOps, Version Control, Repositories, and TFVC.


  Azure Repos'' developer surface includes authentication, developer portal, getting-started guide, documentation, pricing, changelog, engineering blog, and 21 more developer resources.'
plans:
- name: Microsoft Azure Repo Plans Pricing
  plan_count: 8
  slug: microsoft-azure-repo-plans-pricing
- name: Microsoft Azure Repo Price Estimates
  plan_count: 0
  slug: microsoft-azure-repo-price-estimates
random_paper: 21
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
  composite: 60.9
  coverage:
    artifact_dirs: 13
    catalog_earned: 50.0
    catalog_earned_first_party: 12.0
    catalog_gap: 65.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.6
  facets:
    access_clarity: 84.2
    contract_governance: 0.0
    contract_quality: 52.4
    developer_ergonomics: 71.4
    discoverability: 64.3
    operational_transparency: 55.3
  previous_composite: 59.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/microsoft-azure-repo/microsoft-azure-repo-2026-06-20T185433.png
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
- Developer Tools
- DevOps
- Version Control
- Repositories
- TFVC
website: https://azure.microsoft.com/en-us/services/devops/repos/
---
