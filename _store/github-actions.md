---
name: GitHub Actions
description: APIs for GitHub Actions - automation and CI/CD platform.
image: https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png
url: https://docs.github.com/en/rest/actions
created: '2024'
modified: '2026-04-18'
specificationVersion: '0.18'
apis:
  - name: GitHub Actions API
    description: REST API for managing GitHub Actions workflows, runs, artifacts, and secrets.
    image: https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png
    humanURL: https://docs.github.com/en/actions
    baseURL: https://api.github.com
    tags:
      - Automation
      - CI/CD
      - DevOps
      - Workflows
    properties:
      - type: Documentation
        url: https://docs.github.com/en/rest/actions
      - type: OpenAPI
        url: https://raw.githubusercontent.com/github/rest-api-description/main/descriptions/api.github.com/api.github.com.json
      - type: Authentication
        url: https://docs.github.com/en/rest/overview/authenticating-to-the-rest-api
      - type: GettingStarted
        url: https://docs.github.com/en/actions/get-started/quickstart
      - type: APIReference
        url: https://docs.github.com/en/rest/actions
      - type: ChangeLog
        url: https://github.blog/changelog/label/actions/
      - type: SDK
        url: https://github.com/octokit/octokit.js
        title: JavaScript SDK
      - type: SDK
        url: https://github.com/octokit/octokit.rb
        title: Ruby SDK
      - type: SDK
        url: https://github.com/octokit/octokit.net
        title: .NET SDK
      - type: SDK
        url: https://github.com/google/go-github
        title: Go SDK
      - type: CLI
        url: https://cli.github.com/manual/gh_workflow_run
      - type: RateLimits
        url: https://docs.github.com/en/rest/overview/rate-limits-for-the-rest-api
      - type: OpenAPI
        url: openapi/github-actions-openapi.yml
      - type: JSONSchema
        url: json-schema/github-actions-workflow-schema.json
      - type: JSONSchema
        url: json-schema/github-actions-run-schema.json
      - type: JSONSchema
        url: json-schema/github-actions-job-schema.json
      - type: JSONSchema
        url: json-schema/github-actions-artifact-schema.json
      - type: JSONSchema
        url: json-schema/github-actions-secret-schema.json
      - type: JSONSchema
        url: json-schema/github-actions-runner-schema.json
      - type: JSONSchema
        url: json-schema/github-actions-variable-schema.json
      - type: JSONSchema
        url: json-schema/github-actions-cache-schema.json
      - type: JSONSchema
        url: json-schema/github-actions-simple-user-schema.json
      - type: JSONLD
        url: json-ld/github-actions-context.jsonld
    contact:
      - type: Support
        url: https://support.github.com
      - type: StatusPage
        url: https://www.githubstatus.com
    endpoints:
      - name: Workflows
        description: Manage workflow files and workflow runs
        methods:
          - GET /repos/{owner}/{repo}/actions/workflows
          - GET /repos/{owner}/{repo}/actions/workflows/{workflow_id}
          - GET /repos/{owner}/{repo}/actions/workflows/{workflow_id}/runs
          - POST /repos/{owner}/{repo}/actions/workflows/{workflow_id}/dispatches
          - PUT /repos/{owner}/{repo}/actions/workflows/{workflow_id}/disable
          - PUT /repos/{owner}/{repo}/actions/workflows/{workflow_id}/enable
          - GET /repos/{owner}/{repo}/actions/workflows/{workflow_id}/timing
      - name: Workflow Runs
        description: Manage and monitor workflow run executions
        methods:
          - GET /repos/{owner}/{repo}/actions/runs
          - GET /repos/{owner}/{repo}/actions/runs/{run_id}
          - POST /repos/{owner}/{repo}/actions/runs/{run_id}/rerun
          - POST /repos/{owner}/{repo}/actions/runs/{run_id}/cancel
          - DELETE /repos/{owner}/{repo}/actions/runs/{run_id}
          - GET /repos/{owner}/{repo}/actions/runs/{run_id}/approvals
          - POST /repos/{owner}/{repo}/actions/runs/{run_id}/approve
          - GET /repos/{owner}/{repo}/actions/runs/{run_id}/attempts/{attempt_number}
          - GET /repos/{owner}/{repo}/actions/runs/{run_id}/attempts/{attempt_number}/logs
          - POST /repos/{owner}/{repo}/actions/runs/{run_id}/deployment_protection_rule
          - POST /repos/{owner}/{repo}/actions/runs/{run_id}/force-cancel
          - GET /repos/{owner}/{repo}/actions/runs/{run_id}/logs
          - DELETE /repos/{owner}/{repo}/actions/runs/{run_id}/logs
          - GET /repos/{owner}/{repo}/actions/runs/{run_id}/pending_deployments
          - POST /repos/{owner}/{repo}/actions/runs/{run_id}/pending_deployments
          - POST /repos/{owner}/{repo}/actions/runs/{run_id}/rerun-failed-jobs
          - GET /repos/{owner}/{repo}/actions/runs/{run_id}/timing
      - name: Artifacts
        description: Download and manage workflow run artifacts
        methods:
          - GET /repos/{owner}/{repo}/actions/artifacts
          - GET /repos/{owner}/{repo}/actions/artifacts/{artifact_id}
          - GET /repos/{owner}/{repo}/actions/artifacts/{artifact_id}/{archive_format}
          - DELETE /repos/{owner}/{repo}/actions/artifacts/{artifact_id}
          - GET /repos/{owner}/{repo}/actions/runs/{run_id}/artifacts
      - name: Secrets
        description: Manage encrypted secrets for Actions
        methods:
          - GET /repos/{owner}/{repo}/actions/secrets
          - GET /repos/{owner}/{repo}/actions/secrets/{secret_name}
          - PUT /repos/{owner}/{repo}/actions/secrets/{secret_name}
          - DELETE /repos/{owner}/{repo}/actions/secrets/{secret_name}
          - GET /repos/{owner}/{repo}/actions/secrets/public-key
          - GET /repos/{owner}/{repo}/actions/organization-secrets
          - GET /orgs/{org}/actions/secrets
          - GET /orgs/{org}/actions/secrets/public-key
          - GET /orgs/{org}/actions/secrets/{secret_name}
          - PUT /orgs/{org}/actions/secrets/{secret_name}
          - DELETE /orgs/{org}/actions/secrets/{secret_name}
          - GET /orgs/{org}/actions/secrets/{secret_name}/repositories
          - PUT /orgs/{org}/actions/secrets/{secret_name}/repositories
          - PUT /orgs/{org}/actions/secrets/{secret_name}/repositories/{repository_id}
          - DELETE /orgs/{org}/actions/secrets/{secret_name}/repositories/{repository_id}
          - GET /repos/{owner}/{repo}/environments/{environment_name}/secrets
          - GET /repos/{owner}/{repo}/environments/{environment_name}/secrets/public-key
          - GET /repos/{owner}/{repo}/environments/{environment_name}/secrets/{secret_name}
          - PUT /repos/{owner}/{repo}/environments/{environment_name}/secrets/{secret_name}
          - DELETE /repos/{owner}/{repo}/environments/{environment_name}/secrets/{secret_name}
      - name: Self-hosted Runners
        description: Manage self-hosted runners for workflows
        methods:
          - GET /repos/{owner}/{repo}/actions/runners
          - GET /repos/{owner}/{repo}/actions/runners/{runner_id}
          - DELETE /repos/{owner}/{repo}/actions/runners/{runner_id}
          - GET /repos/{owner}/{repo}/actions/runners/downloads
          - POST /repos/{owner}/{repo}/actions/runners/registration-token
          - POST /repos/{owner}/{repo}/actions/runners/remove-token
          - POST /repos/{owner}/{repo}/actions/runners/generate-jitconfig
          - GET /repos/{owner}/{repo}/actions/runners/{runner_id}/labels
          - POST /repos/{owner}/{repo}/actions/runners/{runner_id}/labels
          - PUT /repos/{owner}/{repo}/actions/runners/{runner_id}/labels
          - DELETE /repos/{owner}/{repo}/actions/runners/{runner_id}/labels
          - DELETE /repos/{owner}/{repo}/actions/runners/{runner_id}/labels/{name}
          - GET /orgs/{org}/actions/runners
          - GET /orgs/{org}/actions/runners/{runner_id}
          - DELETE /orgs/{org}/actions/runners/{runner_id}
          - GET /orgs/{org}/actions/runners/downloads
          - POST /orgs/{org}/actions/runners/registration-token
          - POST /orgs/{org}/actions/runners/remove-token
          - POST /orgs/{org}/actions/runners/generate-jitconfig
          - GET /orgs/{org}/actions/runners/{runner_id}/labels
          - POST /orgs/{org}/actions/runners/{runner_id}/labels
          - PUT /orgs/{org}/actions/runners/{runner_id}/labels
          - DELETE /orgs/{org}/actions/runners/{runner_id}/labels
          - DELETE /orgs/{org}/actions/runners/{runner_id}/labels/{name}
      - name: Jobs
        description: Access information about workflow jobs
        methods:
          - GET /repos/{owner}/{repo}/actions/runs/{run_id}/jobs
          - GET /repos/{owner}/{repo}/actions/jobs/{job_id}
          - GET /repos/{owner}/{repo}/actions/jobs/{job_id}/logs
          - POST /repos/{owner}/{repo}/actions/jobs/{job_id}/rerun
          - GET /repos/{owner}/{repo}/actions/runs/{run_id}/attempts/{attempt_number}/jobs
      - name: Cache
        description: Manage workflow dependency caches
        methods:
          - GET /repos/{owner}/{repo}/actions/caches
          - DELETE /repos/{owner}/{repo}/actions/caches
          - DELETE /repos/{owner}/{repo}/actions/caches/{cache_id}
          - GET /repos/{owner}/{repo}/actions/cache/usage
          - GET /repos/{owner}/{repo}/actions/cache/retention-limit
          - PUT /repos/{owner}/{repo}/actions/cache/retention-limit
          - GET /repos/{owner}/{repo}/actions/cache/storage-limit
          - PUT /repos/{owner}/{repo}/actions/cache/storage-limit
          - GET /orgs/{org}/actions/cache/usage
          - GET /orgs/{org}/actions/cache/usage-by-repository
          - GET /organizations/{org}/actions/cache/retention-limit
          - PUT /organizations/{org}/actions/cache/retention-limit
          - GET /organizations/{org}/actions/cache/storage-limit
          - PUT /organizations/{org}/actions/cache/storage-limit
      - name: Variables
        description: Create and manage workflow variables at organization, repository, and environment scopes
        methods:
          - GET /repos/{owner}/{repo}/actions/variables
          - POST /repos/{owner}/{repo}/actions/variables
          - GET /repos/{owner}/{repo}/actions/variables/{name}
          - PATCH /repos/{owner}/{repo}/actions/variables/{name}
          - DELETE /repos/{owner}/{repo}/actions/variables/{name}
          - GET /repos/{owner}/{repo}/actions/organization-variables
          - GET /orgs/{org}/actions/variables
          - POST /orgs/{org}/actions/variables
          - GET /orgs/{org}/actions/variables/{name}
          - PATCH /orgs/{org}/actions/variables/{name}
          - DELETE /orgs/{org}/actions/variables/{name}
          - GET /orgs/{org}/actions/variables/{name}/repositories
          - PUT /orgs/{org}/actions/variables/{name}/repositories
          - PUT /orgs/{org}/actions/variables/{name}/repositories/{repository_id}
          - DELETE /orgs/{org}/actions/variables/{name}/repositories/{repository_id}
          - GET /repos/{owner}/{repo}/environments/{environment_name}/variables
          - POST /repos/{owner}/{repo}/environments/{environment_name}/variables
          - GET /repos/{owner}/{repo}/environments/{environment_name}/variables/{name}
          - PATCH /repos/{owner}/{repo}/environments/{environment_name}/variables/{name}
          - DELETE /repos/{owner}/{repo}/environments/{environment_name}/variables/{name}
      - name: Permissions
        description: Control GitHub Actions enablement, allowed actions, and workflow permissions at organization and repository levels
        methods:
          - GET /orgs/{org}/actions/permissions
          - PUT /orgs/{org}/actions/permissions
          - GET /orgs/{org}/actions/permissions/repositories
          - PUT /orgs/{org}/actions/permissions/repositories
          - PUT /orgs/{org}/actions/permissions/repositories/{repository_id}
          - DELETE /orgs/{org}/actions/permissions/repositories/{repository_id}
          - GET /orgs/{org}/actions/permissions/selected-actions
          - PUT /orgs/{org}/actions/permissions/selected-actions
          - GET /orgs/{org}/actions/permissions/workflow
          - PUT /orgs/{org}/actions/permissions/workflow
          - GET /repos/{owner}/{repo}/actions/permissions
          - PUT /repos/{owner}/{repo}/actions/permissions
          - GET /repos/{owner}/{repo}/actions/permissions/access
          - PUT /repos/{owner}/{repo}/actions/permissions/access
          - GET /repos/{owner}/{repo}/actions/permissions/selected-actions
          - PUT /repos/{owner}/{repo}/actions/permissions/selected-actions
          - GET /repos/{owner}/{repo}/actions/permissions/workflow
          - PUT /repos/{owner}/{repo}/actions/permissions/workflow
      - name: OIDC
        description: Manage OpenID Connect subject claim customization templates for organizations and repositories
        methods:
          - GET /orgs/{org}/actions/oidc/customization/sub
          - PUT /orgs/{org}/actions/oidc/customization/sub
          - GET /repos/{owner}/{repo}/actions/oidc/customization/sub
          - PUT /repos/{owner}/{repo}/actions/oidc/customization/sub
      - name: Self-hosted Runner Groups
        description: Create and manage runner groups to control repository access and organize self-hosted runners
        methods:
          - GET /orgs/{org}/actions/runner-groups
          - POST /orgs/{org}/actions/runner-groups
          - GET /orgs/{org}/actions/runner-groups/{runner_group_id}
          - PATCH /orgs/{org}/actions/runner-groups/{runner_group_id}
          - DELETE /orgs/{org}/actions/runner-groups/{runner_group_id}
          - GET /orgs/{org}/actions/runner-groups/{runner_group_id}/repositories
          - PUT /orgs/{org}/actions/runner-groups/{runner_group_id}/repositories
          - PUT /orgs/{org}/actions/runner-groups/{runner_group_id}/repositories/{repository_id}
          - DELETE /orgs/{org}/actions/runner-groups/{runner_group_id}/repositories/{repository_id}
          - GET /orgs/{org}/actions/runner-groups/{runner_group_id}/runners
          - PUT /orgs/{org}/actions/runner-groups/{runner_group_id}/runners
          - PUT /orgs/{org}/actions/runner-groups/{runner_group_id}/runners/{runner_id}
          - DELETE /orgs/{org}/actions/runner-groups/{runner_group_id}/runners/{runner_id}
      - name: GitHub-hosted Runners
        description: Provision and manage GitHub-hosted runners, custom images, and machine specifications for organizations
        methods:
          - GET /orgs/{org}/actions/hosted-runners
          - POST /orgs/{org}/actions/hosted-runners
          - GET /orgs/{org}/actions/hosted-runners/{hosted_runner_id}
          - PATCH /orgs/{org}/actions/hosted-runners/{hosted_runner_id}
          - DELETE /orgs/{org}/actions/hosted-runners/{hosted_runner_id}
          - GET /orgs/{org}/actions/hosted-runners/images/github-owned
          - GET /orgs/{org}/actions/hosted-runners/images/partner
          - GET /orgs/{org}/actions/hosted-runners/images/custom
          - GET /orgs/{org}/actions/hosted-runners/images/custom/{image_definition_id}
          - DELETE /orgs/{org}/actions/hosted-runners/images/custom/{image_definition_id}
          - GET /orgs/{org}/actions/hosted-runners/images/custom/{image_definition_id}/versions
          - GET /orgs/{org}/actions/hosted-runners/images/custom/{image_definition_id}/versions/{version}
          - DELETE /orgs/{org}/actions/hosted-runners/images/custom/{image_definition_id}/versions/{version}
          - GET /orgs/{org}/actions/hosted-runners/limits
          - GET /orgs/{org}/actions/hosted-runners/machine-sizes
          - GET /orgs/{org}/actions/hosted-runners/platforms
maintainers:
  - type: GitHub
    name: GitHub, Inc.
    url: https://github.com
    email: support@github.com
  - FN: Kin Lane
    email: kin@apievangelist.com
common:
  - type: TermsOfService
    url: https://docs.github.com/en/site-policy/github-terms/github-terms-of-service
  - type: PrivacyPolicy
    url: https://docs.github.com/en/site-policy/privacy-policies/github-privacy-statement
  - type: RateLimits
    url: https://docs.github.com/en/rest/overview/rate-limits-for-the-rest-api
  - type: Blog
    url: https://github.blog/category/product/actions/
  - type: StatusPage
    url: https://www.githubstatus.com
  - type: ChangeLog
    url: https://github.blog/changelog/label/actions/
  - type: GettingStarted
    url: https://docs.github.com/en/actions/get-started/quickstart
  - type: Authentication
    url: https://docs.github.com/en/rest/overview/authenticating-to-the-rest-api
  - type: Support
    url: https://support.github.com
  - type: Pricing
    url: https://github.com/pricing
  - type: GitHubOrganization
    url: https://github.com/github
  - type: Portal
    url: https://docs.github.com/en/rest
  - type: Documentation
    url: https://docs.github.com/en/actions
  - type: SignUp
    url: https://github.com/signup
  - type: Login
    url: https://github.com/login
  - type: DeveloperPortal
    url: https://developer.github.com/
  - type: Marketplace
    url: https://github.com/marketplace?type=actions
  - type: StackOverflow
    url: https://stackoverflow.com/questions/tagged/github-actions
  - type: YouTube
    url: https://www.youtube.com/github
  - type: SDK
    url: https://github.com/octokit/octokit.js
    title: JavaScript SDK
  - type: SDK
    url: https://github.com/octokit/octokit.rb
    title: Ruby SDK
  - type: SDK
    url: https://github.com/octokit/octokit.net
    title: .NET SDK
  - type: SDK
    url: https://github.com/google/go-github
    title: Go SDK
  - type: CLI
    url: https://cli.github.com/
  - type: Quickstart
    url: https://docs.github.com/en/rest/quickstart
  - type: Security
    url: https://docs.github.com/en/actions/security-for-github-actions
  - type: JSONLD
    url: json-ld/github-actions-context.jsonld
  - type: JSONSchema
    url: json-schema/github-actions-workflow-schema.json
  - type: JSONSchema
    url: json-schema/github-actions-run-schema.json
  - type: JSONSchema
    url: json-schema/github-actions-job-schema.json
  - type: JSONSchema
    url: json-schema/github-actions-artifact-schema.json
  - type: JSONSchema
    url: json-schema/github-actions-secret-schema.json
  - type: JSONSchema
    url: json-schema/github-actions-runner-schema.json
  - type: JSONSchema
    url: json-schema/github-actions-variable-schema.json
  - type: JSONSchema
    url: json-schema/github-actions-cache-schema.json
  - type: JSONSchema
    url: json-schema/github-actions-simple-user-schema.json
  - type: Capabilities
    url: capabilities/ci-cd-automation.yaml
    title: CI/CD Automation Capability
  - type: Capabilities
    url: capabilities/shared/actions.yaml
    title: Actions API Shared Definition
  - type: Features
    data:
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
  - type: UseCases
    data:
      - Continuous integration and testing on every push or pull request
      - Automated deployment to cloud environments
      - Scheduled maintenance and cleanup workflows
      - Building and publishing container images
      - Automated code quality and security scanning
      - Release management and artifact publishing
  - type: Integrations
    data:
      - AWS (via OIDC)
      - Azure (via OIDC)
      - Google Cloud (via OIDC)
      - Docker Hub
      - npm
      - PyPI
      - Slack
      - Jira
---
