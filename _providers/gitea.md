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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 51.4
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 470
  human_in_the_loop: 12
  name: Gitea Agentic Access
  operation_count: 944
  slug: gitea-agentic-access
  summary_line: 944 operations · 470 acting · 12 human-in-the-loop
api_count: 13
apis:
- description: GitHub-Actions-compatible workflow engine embedded in Gitea. The Actions API surface is exposed under the main REST API (/repos/{owner}/{repo}/actions/* and /admin/actions/*) for managing workflows, r
  name: Gitea Actions API
  slug: gitea-actions-api
- description: Multi-format package registry built into Gitea exposing client protocols for 24 ecosystems including Cargo, Composer, Conan, Conda, Container (OCI), CRAN, Debian, Generic, Go, Helm, Maven, npm, NuGet,
  name: Gitea Package Registry
  slug: gitea-package-registry
- description: Outbound HTTP webhook system delivering JSON event payloads for pushes, pull requests, issues, releases, package events, and more. Webhooks are configurable per repository, organization or instance-wi
  name: Gitea Webhooks
  slug: gitea-webhooks
- description: Gitea Cloud management plane for provisioning and operating single-tenant managed Gitea instances. Each provisioned instance exposes the same REST API at /api/v1/. The management plane itself does not
  name: Gitea Cloud Management API
  slug: gitea-cloud-management-api
- description: The admin API from Gitea — 22 operation(s) for admin.
  name: Gitea admin API
  slug: gitea-admin-api
- description: The issue API from Gitea — 34 operation(s) for issue.
  name: Gitea issue API
  slug: gitea-issue-api
- description: The miscellaneous API from Gitea — 12 operation(s) for miscellaneous.
  name: Gitea miscellaneous API
  slug: gitea-miscellaneous-api
- description: The notification API from Gitea — 4 operation(s) for notification.
  name: Gitea notification API
  slug: gitea-notification-api
- description: The organization API from Gitea — 37 operation(s) for organization.
  name: Gitea organization API
  slug: gitea-organization-api
- description: The package API from Gitea — 7 operation(s) for package.
  name: Gitea package API
  slug: gitea-package-api
- description: The repository API from Gitea — 133 operation(s) for repository.
  name: Gitea repository API
  slug: gitea-repository-api
- description: The settings API from Gitea — 4 operation(s) for settings.
  name: Gitea settings API
  slug: gitea-settings-api
- description: The user API from Gitea — 48 operation(s) for user.
  name: Gitea user API
  slug: gitea-user-api
arazzos:
- description: Create a repository, open a tracking issue in it, and add a kickoff comment.
  name: Gitea Bootstrap Repository With Tracking Issue
  slug: gitea-bootstrap-repo-with-tracking-issue-workflow
- description: Create a feature branch, open a pull request, and merge it.
  name: Gitea Feature Branch To Merged Pull Request
  slug: gitea-branch-pull-request-merge-workflow
- description: Post a closing comment on an issue and then close it.
  name: Gitea Comment And Close Issue
  slug: gitea-comment-and-close-issue-workflow
- description: Create a branch, commit a new file to it, and open a pull request.
  name: Gitea Commit File On New Branch And Open Pull Request
  slug: gitea-commit-file-and-open-pr-workflow
- description: Create a branch and poll until it is retrievable from the repository.
  name: Gitea Create Branch And Await Availability
  slug: gitea-create-branch-and-await-workflow
- description: Create a draft release, attach an asset, then publish the release.
  name: Gitea Draft Then Publish Release
  slug: gitea-draft-then-publish-release-workflow
- description: Create a repository label and apply it to an existing issue.
  name: Gitea Create Label And Apply To Issue
  slug: gitea-label-create-and-apply-workflow
- description: Create a milestone and open an issue assigned to that milestone.
  name: Gitea Create Milestone With Tracked Issue
  slug: gitea-milestone-with-issue-workflow
- description: Confirm a repository is a mirror, trigger a sync, and verify a branch.
  name: Gitea Sync Mirror And Confirm Branch
  slug: gitea-mirror-sync-workflow
- description: Open a pull request and then triage it with assignees and labels.
  name: Gitea Open And Triage Pull Request
  slug: gitea-open-and-triage-pull-request-workflow
- description: Create an organization, add a repository, and create an org-wide label.
  name: Gitea Bootstrap Organization With Shared Label
  slug: gitea-org-bootstrap-with-label-workflow
- description: Create an organization, add a repository to it, and register a webhook.
  name: Gitea Provision Organization Repository With Webhook
  slug: gitea-org-repo-with-webhook-workflow
- description: Create an organization and register an organization-level webhook.
  name: Gitea Create Organization With Webhook
  slug: gitea-org-with-webhook-workflow
- description: Create a release and confirm it by looking it up by its tag.
  name: Gitea Create Release And Verify By Tag
  slug: gitea-release-and-verify-by-tag-workflow
- description: Create a release on a tag and upload a binary asset to it.
  name: Gitea Publish Release With Asset
  slug: gitea-release-with-asset-workflow
- description: Create a repository, create a label in it, and open a pre-labeled issue.
  name: Gitea Create Repository With A Labeled Issue
  slug: gitea-repo-with-labeled-issue-workflow
- description: Create a repository for the authenticated user and register a webhook.
  name: Gitea Create Repository With Webhook
  slug: gitea-repo-with-webhook-workflow
- description: Confirm a repository exists, open an issue in it, and comment on it.
  name: Gitea Report Issue To Existing Repository
  slug: gitea-report-issue-to-existing-repo-workflow
- description: Create a milestone and label, open an issue under them, and apply the label.
  name: Gitea Sprint Issue Setup
  slug: gitea-sprint-issue-setup-workflow
artifact_total: 130
collections:
- collection_type: postman
  name: Gitea API
  slug: postman-gitea-rest-api-openapi-original
- collection_type: postman
  name: Gitea API
  slug: postman-gitea-rest-api
- collection_type: open
  name: Gitea API
  slug: open-gitea-rest-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/gitea-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/gitea-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/gitea-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gitea-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/gitea-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/gitea-scopes.yml
- group: build
  title: ''
  type: Packages
  url: packages/gitea-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/gitea-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/gitea-security.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/gitea-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/gitea-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/gitea-rest-api-overlay.yaml
- group: other
  title: ''
  type: Protobuf
  url: grpc/gitea-runner-v1-services.proto
- group: other
  title: ''
  type: Protobuf
  url: grpc/gitea-runner-v1-messages.proto
- group: other
  title: ''
  type: Protobuf
  url: grpc/gitea-ping-v1-services.proto
- group: design
  title: ''
  type: Conformance
  url: conformance/gitea-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/gitea-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/gitea-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/gitea-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/gitea-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/gitea-cli.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/gitea-data-model.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/gitea/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/gitea-bootstrap-repo-with-tracking-issue-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/gitea-branch-pull-request-merge-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/gitea-comment-and-close-issue-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/gitea-commit-file-and-open-pr-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/gitea-create-branch-and-await-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/gitea-draft-then-publish-release-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/gitea-label-create-and-apply-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/gitea-milestone-with-issue-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/gitea-mirror-sync-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/gitea-open-and-triage-pull-request-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/gitea-org-bootstrap-with-label-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/gitea-org-repo-with-webhook-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/gitea-org-with-webhook-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/gitea-release-and-verify-by-tag-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/gitea-release-with-asset-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/gitea-repo-with-labeled-issue-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/gitea-repo-with-webhook-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/gitea-report-issue-to-existing-repo-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/gitea-sprint-issue-setup-workflow.yml
- group: company
  title: ''
  type: Website
  url: https://about.gitea.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.gitea.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.gitea.com/api/
- group: company
  title: ''
  type: Blog
  url: https://blog.gitea.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/go-gitea
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/go-gitea/gitea
- group: start
  title: ''
  type: Signup
  url: https://cloud.gitea.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://about.gitea.com/pricing/
- group: commercial
  title: ''
  type: Plans
  url: plans/gitea-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/gitea-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/gitea-finops.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://about.gitea.com/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://about.gitea.com/legal/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://forum.gitea.com/
- group: operate
  title: ''
  type: FAQ
  url: https://about.gitea.com/about/faq
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://blog.gitea.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/go-gitea/gitea/blob/main/CHANGELOG.md
- group: operate
  title: ''
  type: StatusPage
  url: https://status.gitea.com/
- group: auth
  title: ''
  type: Security
  url: https://docs.gitea.com/administration/security
- group: auth
  title: ''
  type: Compliance
  url: https://about.gitea.com/products/cloud
- group: build
  title: ''
  type: SDKs
  url: https://gitea.com/gitea/go-sdk
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/gitea-js
- group: build
  title: ''
  type: SDKs
  url: https://pypi.org/project/py-gitea/
- group: build
  title: ''
  type: SDKs
  url: https://github.com/hypermodeinc/gitea4j
- group: build
  title: ''
  type: CLI
  url: https://gitea.com/gitea/tea
- group: build
  title: ''
  type: CLI
  url: https://gitea.com/gitea/runner
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/go-gitea/terraform-provider-gitea
- group: build
  title: ''
  type: GitHubRepository
  url: https://gitea.com/gitea/helm-gitea
- group: build
  title: ''
  type: GitHubRepository
  url: https://gitea.com/gitea/helm-actions
- group: other
  title: ''
  type: Resources
  url: https://gitea.com/gitea/awesome-gitea
- group: other
  title: ''
  type: Hub
  url: https://discord.gg/gitea
- group: operate
  title: ''
  type: Forums
  url: https://forum.gitea.com/
- group: design
  title: ''
  type: SpectralRules
  url: rules/gitea-rules.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/gitea-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/gitea-vocabulary.yml
created: '2026-05-06'
description: Gitea is an open-source, self-hosted Git service and all-in-one DevOps platform written in Go and licensed under the MIT License. It provides Git hosting, code review, team collaboration, an integrated package registry across 24+ formats, issue tracking, project boards, and GitHub-Actions-compatible CI/CD via Gitea Actions. Gitea ships with a comprehensive Swagger 2.0 / OpenAPI-described REST API at /api/v1/ exposing roughly 300 operations across repositories, users, organizations, issues, packages, notifications, admin, and miscellaneous tags. The project is governed by CommitGo, Inc., which also offers Gitea Enterprise (self-managed, with SSO, audit logs and Kubernetes auto-scaling runners) and Gitea Cloud (single-tenant fully-managed hosting in multiple regions).
examples:
- key_count: 3
  name: Gitea Rest Api Admin User Create Example
  slug: gitea-rest-api-admin-user-create-example
- key_count: 2
  name: Gitea Rest Api Branches List Example
  slug: gitea-rest-api-branches-list-example
- key_count: 2
  name: Gitea Rest Api Commits List Example
  slug: gitea-rest-api-commits-list-example
- key_count: 6
  name: Gitea Rest Api Hook Example
  slug: gitea-rest-api-hook-example
- key_count: 3
  name: Gitea Rest Api Issue Create Example
  slug: gitea-rest-api-issue-create-example
- key_count: 12
  name: Gitea Rest Api Issue Example
  slug: gitea-rest-api-issue-example
- key_count: 2
  name: Gitea Rest Api Issues List Example
  slug: gitea-rest-api-issues-list-example
- key_count: 2
  name: Gitea Rest Api Notifications List Example
  slug: gitea-rest-api-notifications-list-example
- key_count: 3
  name: Gitea Rest Api Org Create Example
  slug: gitea-rest-api-org-create-example
- key_count: 2
  name: Gitea Rest Api Org Repos List Example
  slug: gitea-rest-api-org-repos-list-example
- key_count: 7
  name: Gitea Rest Api Package Example
  slug: gitea-rest-api-package-example
- key_count: 2
  name: Gitea Rest Api Packages List Owner Example
  slug: gitea-rest-api-packages-list-owner-example
- key_count: 3
  name: Gitea Rest Api Pull Create Example
  slug: gitea-rest-api-pull-create-example
- key_count: 12
  name: Gitea Rest Api Pullrequest Example
  slug: gitea-rest-api-pullrequest-example
- key_count: 2
  name: Gitea Rest Api Pulls List Example
  slug: gitea-rest-api-pulls-list-example
- key_count: 3
  name: Gitea Rest Api Release Create Example
  slug: gitea-rest-api-release-create-example
- key_count: 9
  name: Gitea Rest Api Release Example
  slug: gitea-rest-api-release-example
- key_count: 2
  name: Gitea Rest Api Repo Get Example
  slug: gitea-rest-api-repo-get-example
- key_count: 3
  name: Gitea Rest Api Repo Update Example
  slug: gitea-rest-api-repo-update-example
- key_count: 18
  name: Gitea Rest Api Repository Example
  slug: gitea-rest-api-repository-example
- key_count: 2
  name: Gitea Rest Api User Get Example
  slug: gitea-rest-api-user-get-example
- key_count: 3
  name: Gitea Rest Api User Repo Create Example
  slug: gitea-rest-api-user-repo-create-example
- key_count: 3
  name: Gitea Rest Api Webhook Create Example
  slug: gitea-rest-api-webhook-create-example
features:
- description: Self-hosted Git remote with HTTPS and SSH transport, granular repository visibility (public, private, internal), and full repository CRUD over the REST API.
  name: Git Repository Hosting
- description: Branch-based pull requests with reviewers, required approvals, status checks, draft state, conflict detection, and inline review comments.
  name: Pull Requests And Code Review
- description: Built-in issue tracker with labels, milestones, assignees, dependencies, and Kanban-style project boards at repo and org scope.
  name: Issue Tracking And Projects
- description: Native, GitHub-Actions-compatible workflow engine driven by the act_runner agent. Supports matrix builds, secrets, and autoscaling runners on Kubernetes (Enterprise).
  name: Gitea Actions CI/CD
- description: Multi-format package registry covering 24 ecosystems including Container (OCI), Maven, npm, NuGet, PyPI, Helm, Cargo, Terraform, and Generic uploads.
  name: Package Registry
- description: Outgoing webhooks for repository, issue, pull request, release, and package events with optional secret signing.
  name: Webhooks And Events
- description: Approximately 300 endpoints under /api/v1/ described by a Swagger 2.0 specification with multiple authentication schemes.
  name: Comprehensive REST API
- description: Supports BasicAuth, personal access tokens, OAuth2 with PKCE, OpenID Connect, LDAP, SMTP, PAM, SAML SSO (Enterprise), and two-factor authentication.
  name: Authentication And SSO
- description: Pluggable storage backend supporting SQLite, MySQL, PostgreSQL, TiDB, and MS SQL.
  name: Multi-Database Storage
- description: Pull and push mirrors plus one-shot migration import from GitHub, GitLab, Bitbucket, Gitea, and other sources.
  name: Mirroring And Migration
finops:
- name: Gitea Finops
  service_category: Developer Tools / DevOps
  slug: gitea-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gitea.png
integrations:
- description: GitHub-compatible workflow ecosystem; most public Actions run unmodified on Gitea Actions runners.
  name: Gitea Actions / GitHub Actions Marketplace
- description: First-class integration with Drone for repository-driven continuous delivery pipelines.
  name: Drone CI
- description: Webhooks and credentials make Gitea a drop-in source for Jenkins multibranch pipelines.
  name: Jenkins
- description: Official Terraform provider (terraform-provider-gitea) and a Terraform module package registry endpoint.
  name: Terraform
- description: Helm charts and operator-friendly deployment, plus Gitea Enterprise Kubernetes auto-scaling runners.
  name: Kubernetes
- description: GitOps controllers can use a Gitea repository as the source of truth for cluster state.
  name: Argo CD / Flux
- description: Outbound webhook templates for Discord, Slack, and Microsoft Teams notifications.
  name: Discord And Slack
- description: Official command-line client for browsing and managing repositories, issues, pull requests, and releases.
  name: Tea CLI
json_schemas:
- name: Branch
  property_count: 9
  slug: gitea-rest-api-branch
- name: Comment
  property_count: 11
  slug: gitea-rest-api-comment
- name: Commit contains information generated from a Git commit.
  property_count: 10
  slug: gitea-rest-api-commit
- name: Hook
  property_count: 10
  slug: gitea-rest-api-hook
- name: Issue
  property_count: 27
  slug: gitea-rest-api-issue
- name: Label
  property_count: 7
  slug: gitea-rest-api-label
- name: Milestone
  property_count: 10
  slug: gitea-rest-api-milestone
- name: NotificationThread
  property_count: 7
  slug: gitea-rest-api-notificationthread
- name: Organization
  property_count: 11
  slug: gitea-rest-api-organization
- name: Package
  property_count: 9
  slug: gitea-rest-api-package
- name: PullRequest
  property_count: 38
  slug: gitea-rest-api-pullrequest
- name: Release
  property_count: 16
  slug: gitea-rest-api-release
- name: Repository
  property_count: 67
  slug: gitea-rest-api-repository
- name: Tag
  property_count: 6
  slug: gitea-rest-api-tag
- name: Team
  property_count: 9
  slug: gitea-rest-api-team
- name: User
  property_count: 22
  slug: gitea-rest-api-user
json_structures:
- name: Gitea Rest Api Branch Structure
  property_count: 9
  slug: gitea-rest-api-branch-structure
- name: Gitea Rest Api Comment Structure
  property_count: 11
  slug: gitea-rest-api-comment-structure
- name: Gitea Rest Api Commit Structure
  property_count: 10
  slug: gitea-rest-api-commit-structure
- name: Gitea Rest Api Hook Structure
  property_count: 10
  slug: gitea-rest-api-hook-structure
- name: Gitea Rest Api Issue Structure
  property_count: 27
  slug: gitea-rest-api-issue-structure
- name: Gitea Rest Api Label Structure
  property_count: 7
  slug: gitea-rest-api-label-structure
- name: Gitea Rest Api Milestone Structure
  property_count: 10
  slug: gitea-rest-api-milestone-structure
- name: Gitea Rest Api Notificationthread Structure
  property_count: 7
  slug: gitea-rest-api-notificationthread-structure
- name: Gitea Rest Api Organization Structure
  property_count: 11
  slug: gitea-rest-api-organization-structure
- name: Gitea Rest Api Package Structure
  property_count: 9
  slug: gitea-rest-api-package-structure
- name: Gitea Rest Api Pullrequest Structure
  property_count: 38
  slug: gitea-rest-api-pullrequest-structure
- name: Gitea Rest Api Release Structure
  property_count: 16
  slug: gitea-rest-api-release-structure
- name: Gitea Rest Api Repository Structure
  property_count: 67
  slug: gitea-rest-api-repository-structure
- name: Gitea Rest Api Tag Structure
  property_count: 6
  slug: gitea-rest-api-tag-structure
- name: Gitea Rest Api Team Structure
  property_count: 9
  slug: gitea-rest-api-team-structure
- name: Gitea Rest Api User Structure
  property_count: 22
  slug: gitea-rest-api-user-structure
jsonld:
- class_count: 0
  name: Gitea Context
  property_count: 14
  slug: gitea-context
layout: provider
mcp_servers:
- description: ''
  name: gitea-mcp.yml
  slug: gitea-mcpyml
modified: '2026-06-20'
name: Gitea
nav: Providers
network: true
overview: 'Gitea publishes 9 APIs on the [APIs.io](https://apis.io/) network, including admin API, issue API, miscellaneous API, and 6 more. Tagged areas include Git, Source Control, DevOps, CI/CD, and Code Hosting.


  The Gitea catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Gitea''s developer surface includes authentication, changelog, CLI, documentation, API reference, engineering blog, signup flow, and 70 more developer resources.'
plans:
- name: Gitea Plans Pricing
  plan_count: 3
  slug: gitea-plans-pricing
random_paper: 36
rate_limits:
- limit_count: 5
  name: Gitea Rate Limits
  slug: gitea-rate-limits
rules:
- name: Gitea API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: gitea-jsonschema-spectral-rules
- name: Gitea API Rules
  rule_count: 16
  severity_counts:
    error: 4
    hint: 3
    info: 0
    warn: 9
  slug: gitea-rules
scopes:
- name: Gitea Scopes
  scope_count: 0
  slug: gitea-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: exemplar
  composite: 73.8
  delta: -3.6
  facets:
    commercial_clarity: 86.8
    contract_quality: 61.3
    developer_ergonomics: 67.4
    discoverability: 77.8
    governance: 80.2
    operational_transparency: 78.9
  previous_composite: 77.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gitea/refs/heads/main/screenshots/gitea-2026-06-20T181832.png
security:
- kind: authentication
  name: Gitea Authentication
  slug: gitea-authentication
  summary_line: apiKey/http · 7 schemes
- kind: domain-security
  name: Gitea Domain Security
  slug: gitea-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Gitea Vulnerability Disclosure
  slug: gitea-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Gitea Trust Center
  slug: gitea-trust-center
  summary_line: SOC 2
slug: gitea
solutions:
- description: Free, MIT-licensed self-hosted edition with the complete feature set and unlimited users.
  name: Gitea (Open Source)
- description: Commercial self-hosted edition adding SAML SSO, audit logs, Kubernetes auto-scaling runners, priority SLA support, and installation/upgrade assistance.
  name: Gitea Enterprise
- description: Single-tenant fully-managed Gitea hosted by CommitGo with choice of regions (including a Frankfurt EU region), 24x7 availability, and SOC 2 Type 2 certification.
  name: Gitea Cloud
- description: Stand-alone runner agent for executing Gitea Actions workflows on customer infrastructure.
  name: Gitea Actions Runner (act_runner)
tags:
- Git
- Source Control
- DevOps
- CI/CD
- Code Hosting
- Open Source
- Self Hosted
- Package Registry
- Issue Tracking
- Pull Requests
use_cases:
- description: Run a private Git server inside a corporate or air-gapped network, retaining full data ownership.
  name: Self-Hosted Source Control
- description: Combine Git, Actions, packages, and projects to build an internal developer platform without stitching together multiple SaaS vendors.
  name: Internal Developer Platform
- description: Reuse existing GitHub Actions workflows on a self-hosted or cloud runner without depending on github.com.
  name: GitHub Actions Compatible CI/CD
- description: Use Gitea as a single artifact registry for OCI containers, language packages, and generic binaries.
  name: Multi-Format Artifact Registry
- description: Single-tenant Gitea Cloud regions provide data-residency options for regulated industries and EU customers.
  name: Regulated And Sovereign Hosting
website: https://about.gitea.com/
---
