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
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.1
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 156
  human_in_the_loop: 4
  name: Bitbucket Agentic Access
  operation_count: 335
  slug: bitbucket-agentic-access
  summary_line: 335 operations · 156 acting · 4 human-in-the-loop
api_count: 23
apis:
- description: The addon resource is intended to use used by Bitbucket Cloud Connect Apps, and only supports JWT authentication.
  name: Bitbucket Addon API
  slug: bitbucket-addon-api
- description: Repository owners and administrators can set branch management rules on a repository that control what can be pushed by whom. Through these rules, you can enforce a project or team workflow. For examp
  name: Bitbucket Branch restrictions API
  slug: bitbucket-branch-restrictions-api
- description: The branching model resource is used to modify the branching model for a repository. You can use the branching model to define a branch based workflow for your repositories. When you map your workflow
  name: Bitbucket Branching model API
  slug: bitbucket-branching-model-api
- description: Commit statuses provide a way to tag commits with meta data, like automated build results.
  name: Bitbucket Commit statuses API
  slug: bitbucket-commit-statuses-api
- description: These are the repository's commits. They are paginated and returned in reverse chronological order, similar to the output of git log.
  name: Bitbucket Commits API
  slug: bitbucket-commits-api
- description: Teams are deploying code faster than ever, thanks to continuous delivery practices and tools like Bitbucket Pipelines. Bitbucket Deployments gives teams visibility into their deployment environments a
  name: Bitbucket Deployments API
  slug: bitbucket-deployments-api
- description: Access the list of download links associated with the repository.
  name: Bitbucket Downloads API
  slug: bitbucket-downloads-api
- description: The GPG resource allows you to manage GPG keys.
  name: Bitbucket GPG API
  slug: bitbucket-gpg-api
- description: The issue resources provide functionality for getting information on issues in an issue tracker, creating new issues, updating them and deleting them. You can access public issues without authenticati
  name: Bitbucket Issue tracker API
  slug: bitbucket-issue-tracker-api
- description: Bitbucket Pipelines brings continuous delivery to Bitbucket Cloud, empowering teams with full branching to deployment visibility and faster feedback loops.
  name: Bitbucket Pipelines API
  slug: bitbucket-pipelines-api
- description: Bitbucket Cloud projects make it easier for teams to focus on a goal, product, or process by organizing their repositories.
  name: Bitbucket Projects API
  slug: bitbucket-projects-api
- description: The properties API from Bitbucket — 4 operation(s) for properties.
  name: Bitbucket properties API
  slug: bitbucket-properties-api
- description: 'Pull requests are a feature that makes it easier for developers to collaborate using Bitbucket. They provide a user-friendly web interface for discussing proposed changes before integrating them into '
  name: Bitbucket Pullrequests API
  slug: bitbucket-pullrequests-api
- description: The refs resource allows you access branches and tags in a repository. By default, results will be in the order the underlying source control system returns them and identical to the ordering one sees
  name: Bitbucket Refs API
  slug: bitbucket-refs-api
- description: Code insights provides reports, annotations, and metrics to help you and your team improve code quality in pull requests throughout the code review process. Some of the available code insights are sta
  name: Bitbucket Reports API
  slug: bitbucket-reports-api
- description: A Git repository is a virtual storage of your project. It allows you to save versions of your code, which you can access when needed. The repo resource allows you to access public repos, or repos that
  name: Bitbucket Repositories API
  slug: bitbucket-repositories-api
- description: The Search API from Bitbucket — 3 operation(s) for search.
  name: Bitbucket Search API
  slug: bitbucket-search-api
- description: Snippets allow you share code segments or files with yourself, members of your workspace, or the world. Like pull requests, repositories and workspaces, the full set of snippets is defined by what the
  name: Bitbucket Snippets API
  slug: bitbucket-snippets-api
- description: Browse the source code in the repository and create new commits by uploading.
  name: Bitbucket Source API
  slug: bitbucket-source-api
- description: The SSH resource allows you to manage SSH keys.
  name: Bitbucket SSH API
  slug: bitbucket-ssh-api
- description: The users resource allows you to access public information associated with a user account. Most resources in the users endpoint have been deprecated in favor of workspaces.
  name: Bitbucket Users API
  slug: bitbucket-users-api
- description: 'Webhooks provide a way to configure Bitbucket Cloud to make requests to your server (or another external service) whenever certain events occur in Bitbucket Cloud. A webhook consists of: * A subject -'
  name: Bitbucket Webhooks API
  slug: bitbucket-webhooks-api
- description: A workspace is where you create repositories, collaborate on your code, and organize different streams of work in your Bitbucket Cloud account. Workspaces replace the use of teams and users in API cal
  name: Bitbucket Workspaces API
  slug: bitbucket-workspaces-api
artifact_total: 103
asyncapis:
- description: Bitbucket Cloud webhooks deliver event payloads to a subscriber URL via HTTP POST whenever a configured event occurs in a repository or workspace. Each event request includes an X-Event-Key header ide
  name: Bitbucket Cloud Webhook Events
  slug: bitbucket-cloud-webhooks-asyncapi
collections:
- collection_type: postman
  name: Bitbucket Addon API
  slug: postman-bitbucket-addon-api
- collection_type: postman
  name: Bitbucket Addon Branch restrictions API
  slug: postman-bitbucket-branch-restrictions-api
- collection_type: postman
  name: Bitbucket Addon Branching model API
  slug: postman-bitbucket-branching-model-api
- collection_type: postman
  name: Bitbucket Addon Commit statuses API
  slug: postman-bitbucket-commit-statuses-api
- collection_type: postman
  name: Bitbucket Addon Commits API
  slug: postman-bitbucket-commits-api
- collection_type: postman
  name: Bitbucket Addon Deployments API
  slug: postman-bitbucket-deployments-api
- collection_type: postman
  name: Bitbucket Addon Downloads API
  slug: postman-bitbucket-downloads-api
- collection_type: postman
  name: Bitbucket Addon GPG API
  slug: postman-bitbucket-gpg-api
- collection_type: postman
  name: Bitbucket Addon Issue tracker API
  slug: postman-bitbucket-issue-tracker-api
- collection_type: postman
  name: Bitbucket Addon Pipelines API
  slug: postman-bitbucket-pipelines-api
- collection_type: postman
  name: Bitbucket Addon Projects API
  slug: postman-bitbucket-projects-api
- collection_type: postman
  name: Bitbucket Addon properties API
  slug: postman-bitbucket-properties-api
- collection_type: postman
  name: Bitbucket Addon Pullrequests API
  slug: postman-bitbucket-pullrequests-api
- collection_type: postman
  name: Bitbucket Addon Refs API
  slug: postman-bitbucket-refs-api
- collection_type: postman
  name: Bitbucket Addon Reports API
  slug: postman-bitbucket-reports-api
- collection_type: postman
  name: Bitbucket Addon Repositories API
  slug: postman-bitbucket-repositories-api
- collection_type: postman
  name: Bitbucket Addon Search API
  slug: postman-bitbucket-search-api
- collection_type: postman
  name: Bitbucket Addon Snippets API
  slug: postman-bitbucket-snippets-api
- collection_type: postman
  name: Bitbucket Addon Source API
  slug: postman-bitbucket-source-api
- collection_type: postman
  name: Bitbucket Addon SSH API
  slug: postman-bitbucket-ssh-api
- collection_type: postman
  name: Bitbucket Addon Users API
  slug: postman-bitbucket-users-api
- collection_type: postman
  name: Bitbucket Addon Webhooks API
  slug: postman-bitbucket-webhooks-api
- collection_type: postman
  name: Bitbucket Addon Workspaces API
  slug: postman-bitbucket-workspaces-api
- collection_type: open
  name: Bitbucket API
  slug: open-bitbucket-cloud-rest-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/bitbucket/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bitbucket-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/bitbucket-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/bitbucket-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bitbucket-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bitbucket-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/bitbucket-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/atlassian
- group: start
  title: ''
  type: Portal
  url: https://developer.atlassian.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.atlassian.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.atlassian.com/legal/cloud-terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.atlassian.com/legal/privacy-policy
- group: start
  title: ''
  type: Signup
  url: https://bitbucket.org/account/signup/
- group: company
  title: ''
  type: Blog
  url: https://bitbucket.org/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/atlassian
- group: operate
  title: ''
  type: Support
  url: https://support.atlassian.com/bitbucket-cloud/
- group: design
  title: ''
  type: JSONLD
  url: json-ld/bitbucket-cloud-rest-api-context.jsonld
- group: design
  title: ''
  type: SpectralRules
  url: rules/bitbucket-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/bitbucket-vocabulary.yaml
created: '2024-01-01'
description: Bitbucket is a Git-based source code repository hosting service owned by Atlassian offering both commercial plans and free accounts with unlimited private repositories, along with CI/CD pipelines, code reviews via pull requests, and code collaboration tools for development teams.
examples:
- key_count: 7
  name: Bitbucket Cloud Rest Api Commit Example
  slug: bitbucket-cloud-rest-api-commit-example
- key_count: 10
  name: Bitbucket Cloud Rest Api Pipeline Example
  slug: bitbucket-cloud-rest-api-pipeline-example
- key_count: 15
  name: Bitbucket Cloud Rest Api Pullrequest Example
  slug: bitbucket-cloud-rest-api-pullrequest-example
- key_count: 18
  name: Bitbucket Cloud Rest Api Repository Example
  slug: bitbucket-cloud-rest-api-repository-example
features:
- 'Free: 5 users, 1 GB, 50 build minutes/mo'
- 'Standard at $3.65/user/mo: unlimited users/storage, 2,500 build minutes'
- 'Premium at $7.25/user/mo: 3,500 minutes, AI PR, IP allowlisting, 99.9% SLA'
- REST API v2 at api.bitbucket.org/2.0
- 1,000 req/hr per user, 60K req/hr per IP
- Pipelines for CI/CD
- 'Pipeline concurrency: 1 Free, 10 Standard, 20 Premium'
- OAuth 2.0 + repository/workspace access tokens
- Webhooks for repository, PR, pipeline events
- Code insights for static analysis integration
- Self-hosted runners (1 slot Standard, 2 Premium)
- Deployment environments tracking
- Native Jira integration
- Atlassian Marketplace apps
- Git LFS support (5 GB Standard, 10 GB Premium)
- Forge / Connect framework for apps
finops:
- name: Bitbucket Finops
  service_category: Source Control + CI/CD
  slug: bitbucket-finops
image: /assets/icons/bitbucket.png
integrations:
- description: Deep integration with Jira for issue tracking and project management.
  name: Jira Software
- description: Connect Bitbucket with Trello for visual project management.
  name: Trello
- description: Receive Bitbucket notifications in Slack channels.
  name: Slack
- description: Link documentation in Confluence with code in Bitbucket.
  name: Confluence
- description: Deploy to AWS services using Bitbucket Pipelines.
  name: AWS
- description: Deploy to Azure services using Bitbucket Pipelines.
  name: Azure
- description: Deploy to Google Cloud using Bitbucket Pipelines.
  name: Google Cloud
- description: Build and push Docker images using Bitbucket Pipelines.
  name: Docker
json_schemas:
- name: Commit
  property_count: 7
  slug: bitbucket-cloud-rest-api-commit
- name: Pipeline
  property_count: 10
  slug: bitbucket-cloud-rest-api-pipeline
- name: Pullrequest
  property_count: 16
  slug: bitbucket-cloud-rest-api-pullrequest
- name: Repository
  property_count: 18
  slug: bitbucket-cloud-rest-api-repository
json_structures:
- name: Bitbucket Cloud Rest Api Commit Structure
  property_count: 4
  slug: bitbucket-cloud-rest-api-commit-structure
- name: Bitbucket Cloud Rest Api Pipeline Structure
  property_count: 6
  slug: bitbucket-cloud-rest-api-pipeline-structure
- name: Bitbucket Cloud Rest Api Pullrequest Structure
  property_count: 10
  slug: bitbucket-cloud-rest-api-pullrequest-structure
- name: Bitbucket Cloud Rest Api Repository Structure
  property_count: 15
  slug: bitbucket-cloud-rest-api-repository-structure
- name: Bitbucket Structure
  property_count: 0
  slug: bitbucket-structure
jsonld:
- class_count: 4
  name: Bitbucket Cloud Rest Api Context
  property_count: 23
  slug: bitbucket-cloud-rest-api-context
layout: provider
modified: '2026-05-29'
name: Bitbucket
nav: Providers
network: true
overview: 'Bitbucket publishes 23 APIs on the [APIs.io](https://apis.io/) network, including Addon API, Branch restrictions API, Branching model API, and 20 more. Tagged areas include Atlassian, CI/CD, Code Collaboration, Code Review, and DevOps.


  The Bitbucket catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Bitbucket''s developer surface includes authentication, developer portal, signup flow, engineering blog, support, and 14 more developer resources.'
plans:
- name: Bitbucket Plans Pricing
  plan_count: 3
  slug: bitbucket-plans-pricing
random_paper: 117
rate_limits:
- limit_count: 5
  name: Bitbucket Rate Limits
  slug: bitbucket-rate-limits
rules:
- name: Bitbucket API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 6
  slug: bitbucket-asyncapi-spectral-rules
- name: Bitbucket API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: bitbucket-jsonschema-spectral-rules
- name: Bitbucket API Rules
  rule_count: 22
  severity_counts:
    error: 8
    hint: 0
    info: 2
    warn: 12
  slug: bitbucket-spectral-rules
scopes:
- name: Bitbucket Scopes
  scope_count: 26
  slug: bitbucket-scopes
  summary_line: 26 scopes · authorizationCode
score:
  band: developing
  composite: 54.2
  delta: 0.0
  facets:
    commercial_clarity: 57.9
    contract_quality: 78.6
    developer_ergonomics: 30.4
    discoverability: 68.5
    governance: 52.1
    operational_transparency: 28.9
  previous_composite: 54.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 23
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bitbucket/refs/heads/main/screenshots/bitbucket-2026-06-20T173301.png
security:
- kind: authentication
  name: Bitbucket Authentication
  slug: bitbucket-authentication
  summary_line: apiKey/http/oauth2 · 3 schemes
- kind: domain-security
  name: Bitbucket Domain Security
  slug: bitbucket-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Bitbucket Vulnerability Disclosure
  slug: bitbucket-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Bitbucket Trust Center
  slug: bitbucket-trust-center
  summary_line: FedRAMP
slug: bitbucket
tags:
- Atlassian
- CI/CD
- Code Collaboration
- Code Review
- DevOps
- Git
- Pull Requests
- Repository Hosting
- Version Control
use_cases:
- description: Enforce code quality through structured pull request reviews with required approvals.
  name: Code Review Workflows
- description: Automate build, test, and deployment pipelines triggered by code changes.
  name: CI/CD Automation
- description: Enable distributed development teams to collaborate on code with workspaces and projects.
  name: Team Collaboration
- description: Manage releases with deployment tracking and environment promotion.
  name: Release Management
- description: Integrate security scanning into CI/CD pipelines for vulnerability detection.
  name: Security Scanning
website: https://developer.atlassian.com/
---
