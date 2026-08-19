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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 53.3
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 39
  human_in_the_loop: 2
  name: Github Actions Agentic Access
  operation_count: 82
  slug: github-actions-agentic-access
  summary_line: 82 operations · 39 acting · 2 human-in-the-loop
api_count: 11
apis:
- description: Download and manage workflow run artifacts
  name: GitHub Actions Artifacts API
  slug: github-actions-artifacts-api
- description: Manage workflow dependency caches
  name: GitHub Actions Cache API
  slug: github-actions-cache-api
- description: Access information about workflow jobs
  name: GitHub Actions Jobs API
  slug: github-actions-jobs-api
- description: Manage OIDC subject claim customization
  name: GitHub Actions OIDC API
  slug: github-actions-oidc-api
- description: Control Actions enablement and permissions
  name: GitHub Actions Permissions API
  slug: github-actions-permissions-api
- description: Manage encrypted secrets for Actions
  name: GitHub Actions Secrets API
  slug: github-actions-secrets-api
- description: Manage runner groups for organizations
  name: GitHub Actions Self-Hosted Runner Groups API
  slug: github-actions-self-hosted-runner-groups-api
- description: Manage self-hosted runners for workflows
  name: GitHub Actions Self-Hosted Runners API
  slug: github-actions-self-hosted-runners-api
- description: Create and manage workflow variables
  name: GitHub Actions Variables API
  slug: github-actions-variables-api
- description: Manage and monitor workflow run executions
  name: GitHub Actions Workflow Runs API
  slug: github-actions-workflow-runs-api
- description: Manage workflow files and workflow runs
  name: GitHub Actions Workflows API
  slug: github-actions-workflows-api
arazzos:
- description: Get a run, find its pending deployment environments, approve them, then poll the run to completion.
  name: GitHub Actions Approve a Pending Deployment
  slug: github-actions-approve-pending-deployment-workflow
- description: Get a run, request cancellation, poll until it is no longer in progress, and force-cancel if it gets stuck.
  name: GitHub Actions Cancel a Workflow Run and Confirm
  slug: github-actions-cancel-run-workflow
- description: Find the latest run for a repository, confirm it, list its artifacts, and resolve a download URL.
  name: GitHub Actions Collect Workflow Run Artifacts
  slug: github-actions-collect-run-artifacts-workflow
- description: Manually dispatch a workflow, find the run it created, poll until it completes, then list its jobs.
  name: GitHub Actions Dispatch and Track a Workflow Run
  slug: github-actions-dispatch-and-track-run-workflow
- description: Find the latest failed run, list its jobs, get the failing job, and resolve its log download URL.
  name: GitHub Actions Inspect Failed Job Logs
  slug: github-actions-inspect-failed-job-logs-workflow
- description: Read cache usage, list the largest caches, and delete the largest one by id to reclaim space.
  name: GitHub Actions Prune Repository Caches
  slug: github-actions-prune-repo-caches-workflow
- description: List the available runner application binaries, mint a registration token, then list the repository's runners.
  name: GitHub Actions Register a Self-hosted Runner
  slug: github-actions-register-runner-workflow
- description: Find the most recent failed run, re-run only its failed jobs, and poll the run until it completes again.
  name: GitHub Actions Re-run Failed Jobs and Track
  slug: github-actions-rerun-failed-run-workflow
- description: Fetch the org public key, create or update a selected-visibility org secret, scope it to repositories, and list them.
  name: GitHub Actions Share an Organization Secret with Selected Repositories
  slug: github-actions-share-org-secret-workflow
- description: Fetch the repository public key, create or update an encrypted secret, then confirm it exists.
  name: GitHub Actions Upsert a Repository Secret
  slug: github-actions-upsert-repo-secret-workflow
- description: Look up a repository variable by name and either create it or update it, then read it back.
  name: GitHub Actions Upsert a Repository Variable
  slug: github-actions-upsert-repo-variable-workflow
artifact_total: 165
collections:
- collection_type: postman
  name: GitHub Actions API
  slug: postman-github-actions
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: GitHub Actions Artifacts API
  slug: open-github-actions-artifacts-api
- collection_type: open
  name: GitHub Actions Artifacts Cache API
  slug: open-github-actions-cache-api
- collection_type: open
  name: GitHub Actions Artifacts Jobs API
  slug: open-github-actions-jobs-api
- collection_type: open
  name: GitHub Actions Artifacts OIDC API
  slug: open-github-actions-oidc-api
- collection_type: open
  name: GitHub Actions Artifacts Permissions API
  slug: open-github-actions-permissions-api
- collection_type: open
  name: GitHub Actions Artifacts Secrets API
  slug: open-github-actions-secrets-api
- collection_type: open
  name: GitHub Actions Artifacts Self-Hosted Runner Groups API
  slug: open-github-actions-self-hosted-runner-groups-api
- collection_type: open
  name: GitHub Actions Artifacts Self-Hosted Runners API
  slug: open-github-actions-self-hosted-runners-api
- collection_type: open
  name: GitHub Actions Artifacts Variables API
  slug: open-github-actions-variables-api
- collection_type: open
  name: GitHub Actions Artifacts Workflow Runs API
  slug: open-github-actions-workflow-runs-api
- collection_type: open
  name: GitHub Actions Artifacts Workflows API
  slug: open-github-actions-workflows-api
- collection_type: open
  name: GitHub Actions API
  slug: open-github-actions
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/github-actions-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/github-actions-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/github-actions/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/github-actions-approve-pending-deployment-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/github-actions-cancel-run-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/github-actions-collect-run-artifacts-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/github-actions-dispatch-and-track-run-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/github-actions-inspect-failed-job-logs-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/github-actions-prune-repo-caches-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/github-actions-register-runner-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/github-actions-rerun-failed-run-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/github-actions-share-org-secret-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/github-actions-upsert-repo-secret-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/github-actions-upsert-repo-variable-workflow.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docs.github.com/en/site-policy/github-terms/github-terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://docs.github.com/en/site-policy/privacy-policies/github-privacy-statement
- group: operate
  title: ''
  type: RateLimits
  url: https://docs.github.com/en/rest/overview/rate-limits-for-the-rest-api
- group: company
  title: ''
  type: Blog
  url: https://github.blog/category/product/actions/
- group: operate
  title: ''
  type: StatusPage
  url: https://www.githubstatus.com
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.blog/changelog/label/actions/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.github.com/en/actions/get-started/quickstart
- group: auth
  title: ''
  type: Authentication
  url: https://docs.github.com/en/rest/overview/authenticating-to-the-rest-api
- group: operate
  title: ''
  type: Support
  url: https://support.github.com
- group: commercial
  title: ''
  type: Pricing
  url: https://github.com/pricing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/github
- group: start
  title: ''
  type: Portal
  url: https://docs.github.com/en/rest
- group: docs
  title: ''
  type: Documentation
  url: https://docs.github.com/en/actions
- group: start
  title: ''
  type: Signup
  url: https://github.com/signup
- group: start
  title: ''
  type: Login
  url: https://github.com/login
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.github.com/
- group: other
  title: ''
  type: Marketplace
  url: https://github.com/marketplace?type=actions
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/github-actions
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/github
- group: build
  title: JavaScript SDK
  type: SDKs
  url: https://github.com/octokit/octokit.js
- group: build
  title: Ruby SDK
  type: SDKs
  url: https://github.com/octokit/octokit.rb
- group: build
  title: .NET SDK
  type: SDKs
  url: https://github.com/octokit/octokit.net
- group: build
  title: Go SDK
  type: SDKs
  url: https://github.com/google/go-github
- group: build
  title: ''
  type: CLI
  url: https://cli.github.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.github.com/en/rest/quickstart
- group: auth
  title: ''
  type: Security
  url: https://docs.github.com/en/actions/security-for-github-actions
- group: design
  title: ''
  type: JSONLD
  url: json-ld/github-actions-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/github-actions-workflow-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/github-actions-run-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/github-actions-job-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/github-actions-artifact-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/github-actions-secret-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/github-actions-runner-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/github-actions-variable-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/github-actions-cache-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/github-actions-simple-user-schema.json
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.github.com/llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/github-actions-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/github-actions-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/github-actions-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/github-actions-security.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/github-actions-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/github-actions-openapi-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/github-actions-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/github-actions-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/github-actions-lifecycle.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/github-actions-scopes.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/github-actions-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/github-actions-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/github-actions-trust-center.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/github-actions-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/github-actions-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/github-actions-cli.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/github-actions-data-model.yml
created: '2024'
description: APIs for GitHub Actions - automation and CI/CD platform.
examples:
- key_count: 7
  name: Github Actions Actions Cache Entry Example
  slug: github-actions-actions-cache-entry-example
- key_count: 3
  name: Github Actions Actions Cache Usage Example
  slug: github-actions-actions-cache-usage-example
- key_count: 2
  name: Github Actions Actions Default Workflow Permissions Example
  slug: github-actions-actions-default-workflow-permissions-example
- key_count: 4
  name: Github Actions Actions Organization Permissions Example
  slug: github-actions-actions-organization-permissions-example
- key_count: 2
  name: Github Actions Actions Public Key Example
  slug: github-actions-actions-public-key-example
- key_count: 3
  name: Github Actions Actions Repository Permissions Example
  slug: github-actions-actions-repository-permissions-example
- key_count: 3
  name: Github Actions Actions Secret Example
  slug: github-actions-actions-secret-example
- key_count: 4
  name: Github Actions Actions Variable Example
  slug: github-actions-actions-variable-example
- key_count: 11
  name: Github Actions Artifact Example
  slug: github-actions-artifact-example
- key_count: 2
  name: Github Actions Authentication Token Example
  slug: github-actions-authentication-token-example
- key_count: 8
  name: Github Actions Deployment Example
  slug: github-actions-deployment-example
- key_count: 3
  name: Github Actions Environment Approval Example
  slug: github-actions-environment-approval-example
- key_count: 21
  name: Github Actions Job Example
  slug: github-actions-job-example
- key_count: 6
  name: Github Actions Job Step Example
  slug: github-actions-job-step-example
- key_count: 8
  name: Github Actions Minimal Repository Example
  slug: github-actions-minimal-repository-example
- key_count: 2
  name: Github Actions Oidc Custom Sub Example
  slug: github-actions-oidc-custom-sub-example
- key_count: 1
  name: Github Actions Oidc Custom Sub Org Example
  slug: github-actions-oidc-custom-sub-org-example
- key_count: 5
  name: Github Actions Org Actions Secret Example
  slug: github-actions-org-actions-secret-example
- key_count: 5
  name: Github Actions Pending Deployment Example
  slug: github-actions-pending-deployment-example
- key_count: 6
  name: Github Actions Runner Application Example
  slug: github-actions-runner-application-example
- key_count: 7
  name: Github Actions Runner Group Example
  slug: github-actions-runner-group-example
- key_count: 3
  name: Github Actions Runner Label Example
  slug: github-actions-runner-label-example
- key_count: 6
  name: Github Actions Self Hosted Runner Example
  slug: github-actions-self-hosted-runner-example
- key_count: 6
  name: Github Actions Simple Commit Example
  slug: github-actions-simple-commit-example
- key_count: 7
  name: Github Actions Simple User Example
  slug: github-actions-simple-user-example
- key_count: 10
  name: Github Actions Workflow Example
  slug: github-actions-workflow-example
- key_count: 24
  name: Github Actions Workflow Run Example
  slug: github-actions-workflow-run-example
- key_count: 2
  name: Github Actions Workflow Run Usage Example
  slug: github-actions-workflow-run-usage-example
- key_count: 1
  name: Github Actions Workflow Usage Example
  slug: github-actions-workflow-usage-example
features:
- Automated CI/CD workflows triggered by repository events
- Matrix builds across multiple OS and language versions
- Reusable workflows and composite actions
- Encrypted secrets and variables at repo, org, and environment scopes
- Self-hosted and GitHub-hosted runner management
- Workflow artifact storage and sharing
- Deployment protection rules and environment approvals
- OIDC integration for cloud provider authentication
- Dependency caching for faster builds
- Runner groups for organizational access control
finops:
- name: Github Actions Finops
  service_category: API
  slug: github-actions-finops
image: https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png
integrations:
- AWS (via OIDC)
- Azure (via OIDC)
- Google Cloud (via OIDC)
- Docker Hub
- npm
- PyPI
- Slack
- Jira
json_schemas:
- name: ActionsCacheEntry
  property_count: 7
  slug: github-actions-actions-cache-entry
- name: ActionsCacheUsage
  property_count: 3
  slug: github-actions-actions-cache-usage
- name: ActionsDefaultWorkflowPermissions
  property_count: 2
  slug: github-actions-actions-default-workflow-permissions
- name: ActionsOrganizationPermissions
  property_count: 4
  slug: github-actions-actions-organization-permissions
- name: ActionsPublicKey
  property_count: 2
  slug: github-actions-actions-public-key
- name: ActionsRepositoryPermissions
  property_count: 3
  slug: github-actions-actions-repository-permissions
- name: ActionsSecret
  property_count: 3
  slug: github-actions-actions-secret
- name: ActionsVariable
  property_count: 4
  slug: github-actions-actions-variable
- name: Artifact
  property_count: 11
  slug: github-actions-artifact
- name: AuthenticationToken
  property_count: 2
  slug: github-actions-authentication-token
- name: GitHub Actions Cache Entry
  property_count: 7
  slug: github-actions-cache
- name: Deployment
  property_count: 8
  slug: github-actions-deployment
- name: EnvironmentApproval
  property_count: 3
  slug: github-actions-environment-approval
- name: Job
  property_count: 21
  slug: github-actions-job
- name: JobStep
  property_count: 6
  slug: github-actions-job-step
- name: MinimalRepository
  property_count: 8
  slug: github-actions-minimal-repository
- name: OidcCustomSubOrg
  property_count: 1
  slug: github-actions-oidc-custom-sub-org
- name: OidcCustomSub
  property_count: 2
  slug: github-actions-oidc-custom-sub
- name: OrgActionsSecret
  property_count: 5
  slug: github-actions-org-actions-secret
- name: PendingDeployment
  property_count: 5
  slug: github-actions-pending-deployment
- name: GitHub Actions Workflow Run
  property_count: 27
  slug: github-actions-run
- name: RunnerApplication
  property_count: 6
  slug: github-actions-runner-application
- name: RunnerGroup
  property_count: 7
  slug: github-actions-runner-group
- name: RunnerLabel
  property_count: 3
  slug: github-actions-runner-label
- name: GitHub Actions Self-Hosted Runner
  property_count: 6
  slug: github-actions-runner
- name: GitHub Actions Secret
  property_count: 5
  slug: github-actions-secret
- name: SelfHostedRunner
  property_count: 6
  slug: github-actions-self-hosted-runner
- name: SimpleCommit
  property_count: 6
  slug: github-actions-simple-commit
- name: SimpleUser
  property_count: 7
  slug: github-actions-simple-user
- name: GitHub Actions Variable
  property_count: 4
  slug: github-actions-variable
- name: WorkflowRun
  property_count: 24
  slug: github-actions-workflow-run
- name: WorkflowRunUsage
  property_count: 2
  slug: github-actions-workflow-run-usage
- name: Workflow
  property_count: 10
  slug: github-actions-workflow
- name: WorkflowUsage
  property_count: 1
  slug: github-actions-workflow-usage
json_structures:
- name: Github Actions Actions Cache Entry Structure
  property_count: 7
  slug: github-actions-actions-cache-entry-structure
- name: Github Actions Actions Cache Usage Structure
  property_count: 3
  slug: github-actions-actions-cache-usage-structure
- name: Github Actions Actions Default Workflow Permissions Structure
  property_count: 2
  slug: github-actions-actions-default-workflow-permissions-structure
- name: Github Actions Actions Organization Permissions Structure
  property_count: 4
  slug: github-actions-actions-organization-permissions-structure
- name: Github Actions Actions Public Key Structure
  property_count: 2
  slug: github-actions-actions-public-key-structure
- name: Github Actions Actions Repository Permissions Structure
  property_count: 3
  slug: github-actions-actions-repository-permissions-structure
- name: Github Actions Actions Secret Structure
  property_count: 3
  slug: github-actions-actions-secret-structure
- name: Github Actions Actions Variable Structure
  property_count: 4
  slug: github-actions-actions-variable-structure
- name: Github Actions Artifact Structure
  property_count: 11
  slug: github-actions-artifact-structure
- name: Github Actions Authentication Token Structure
  property_count: 2
  slug: github-actions-authentication-token-structure
- name: Github Actions Deployment Structure
  property_count: 8
  slug: github-actions-deployment-structure
- name: Github Actions Environment Approval Structure
  property_count: 3
  slug: github-actions-environment-approval-structure
- name: Github Actions Job Step Structure
  property_count: 6
  slug: github-actions-job-step-structure
- name: Github Actions Job Structure
  property_count: 21
  slug: github-actions-job-structure
- name: Github Actions Minimal Repository Structure
  property_count: 8
  slug: github-actions-minimal-repository-structure
- name: Github Actions Oidc Custom Sub Org Structure
  property_count: 1
  slug: github-actions-oidc-custom-sub-org-structure
- name: Github Actions Oidc Custom Sub Structure
  property_count: 2
  slug: github-actions-oidc-custom-sub-structure
- name: Github Actions Org Actions Secret Structure
  property_count: 5
  slug: github-actions-org-actions-secret-structure
- name: Github Actions Pending Deployment Structure
  property_count: 5
  slug: github-actions-pending-deployment-structure
- name: Github Actions Runner Application Structure
  property_count: 6
  slug: github-actions-runner-application-structure
- name: Github Actions Runner Group Structure
  property_count: 7
  slug: github-actions-runner-group-structure
- name: Github Actions Runner Label Structure
  property_count: 3
  slug: github-actions-runner-label-structure
- name: Github Actions Self Hosted Runner Structure
  property_count: 6
  slug: github-actions-self-hosted-runner-structure
- name: Github Actions Simple Commit Structure
  property_count: 6
  slug: github-actions-simple-commit-structure
- name: Github Actions Simple User Structure
  property_count: 7
  slug: github-actions-simple-user-structure
- name: Github Actions Workflow Run Structure
  property_count: 24
  slug: github-actions-workflow-run-structure
- name: Github Actions Workflow Run Usage Structure
  property_count: 2
  slug: github-actions-workflow-run-usage-structure
- name: Github Actions Workflow Structure
  property_count: 10
  slug: github-actions-workflow-structure
- name: Github Actions Workflow Usage Structure
  property_count: 1
  slug: github-actions-workflow-usage-structure
jsonld:
- class_count: 0
  name: Github Actions Context
  property_count: 0
  slug: github-actions-context
layout: provider
mcp_servers:
- description: ''
  name: github-actions-mcp.yml
  slug: github-actions-mcpyml
modified: '2026-06-20'
name: GitHub Actions
nav: Providers
network: true
overview: 'GitHub Actions publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Artifacts API, Cache API, Jobs API, and 8 more.


  The GitHub Actions catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  GitHub Actions'' developer surface includes authentication, engineering blog, changelog, getting-started guide, support, pricing, developer portal, and 61 more developer resources.'
plans:
- name: Github Actions Plans Pricing
  plan_count: 3
  slug: github-actions-plans-pricing
random_paper: 100
rate_limits:
- limit_count: 5
  name: Github Actions Rate Limits
  slug: github-actions-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: GitHub Actions API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: github-actions-jsonschema-spectral-rules
- effective_rule_count: 56
  extends:
  - spectral:oas
  name: GitHub Actions API Rules
  rule_count: 15
  severity_counts:
    error: 8
    hint: 0
    info: 0
    warn: 7
  slug: github-actions-spectral-rules
scopes:
- name: Github Actions Scopes
  scope_count: 0
  slug: github-actions-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 62.2
  delta: -8.6
  facets:
    access_clarity: 61.8
    commercial_clarity: 61.8
    contract_governance: 26.5
    contract_quality: 68.5
    developer_ergonomics: 76.2
    discoverability: 74.1
    governance: 26.5
    operational_transparency: 52.6
  previous_composite: 70.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: first-party
  regulatory:
    applies: false
    note: provider carries no tags; regime could not be determined
    undetermined: true
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/github-actions/refs/heads/main/screenshots/github-actions-2026-06-20T181837.png
security:
- kind: authentication
  name: Github Actions Authentication
  slug: github-actions-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Github Actions Domain Security
  slug: github-actions-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Github Actions Vulnerability Disclosure
  slug: github-actions-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Github Actions Trust Center
  slug: github-actions-trust-center
  summary_line: SOC 1 Type 2, SOC 2 Type 2, SOC 3, ISO/IEC 27001:2013, ISO/IEC 42001:2023, CSA STAR Level 2, FedRAMP LI-SaaS (ATO)
slug: github-actions
use_cases:
- Continuous integration and testing on every push or pull request
- Automated deployment to cloud environments
- Scheduled maintenance and cleanup workflows
- Building and publishing container images
- Automated code quality and security scanning
- Release management and artifact publishing
---
