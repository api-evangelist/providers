---
aid: github-actions
url: https://raw.githubusercontent.com/api-evangelist/github-actions/refs/heads/main/apis.yml
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
  - type: Getting Started
    url: https://docs.github.com/en/actions/get-started/quickstart
  - type: API Reference
    url: https://docs.github.com/en/rest/actions
  - type: Change Log
    url: https://github.blog/changelog/label/actions/
  - type: SDK - JavaScript
    url: https://github.com/octokit/octokit.js
  - type: SDK - Ruby
    url: https://github.com/octokit/octokit.rb
  - type: SDK - .NET
    url: https://github.com/octokit/octokit.net
  - type: SDK - Go
    url: https://github.com/google/go-github
  - type: SDK - GitHub Actions
    url: https://github.com/octokit/action.js
  - type: CLI
    url: https://cli.github.com/manual/gh_workflow_run
  - type: Libraries
    url: https://docs.github.com/en/rest/using-the-rest-api/libraries-for-the-rest-api
  - type: Rate Limits
    url: https://docs.github.com/en/rest/overview/rate-limits-for-the-rest-api
  - type: REST API Quickstart
    url: https://docs.github.com/en/rest/quickstart
  - type: OpenAPI
    url: openapi/github-actions-openapi.yml
  - type: JSON Schema - Workflow
    url: json-schema/github-actions-workflow-schema.json
  - type: JSON Schema - Workflow Run
    url: json-schema/github-actions-run-schema.json
  - type: JSON Schema - Job
    url: json-schema/github-actions-job-schema.json
  - type: JSON Schema - Artifact
    url: json-schema/github-actions-artifact-schema.json
  - type: JSON Schema - Secret
    url: json-schema/github-actions-secret-schema.json
  - type: JSON Schema - Runner
    url: json-schema/github-actions-runner-schema.json
  - type: JSON Schema - Variable
    url: json-schema/github-actions-variable-schema.json
  - type: JSON Schema - Cache
    url: json-schema/github-actions-cache-schema.json
  - type: JSON Schema - Simple User
    url: json-schema/github-actions-simple-user-schema.json
  - type: JSON-LD Context
    url: json-ld/github-actions-context.jsonld
  contact:
  - type: Support
    url: https://support.github.com
  - type: API Status
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
name: GitHub Actions
tags:
- API
type: Contract
image: https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: APIs for GitHub Actions - automation and CI/CD platform.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

