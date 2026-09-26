---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
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
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: true
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 54.3
  scored_at: '2026-09-25'
agentic_access:
- acting_count: 633
  human_in_the_loop: 25
  name: Gitlab Ci Agentic Access
  operation_count: 1140
  slug: gitlab-ci-agentic-access
  summary_line: 1140 operations · 633 acting · 25 human-in-the-loop
api_count: 1
apis:
- description: GitLab's GraphQL API at /api/graphql. Many CI/CD entities (Pipeline, CiJob, CiRunner, MergeRequest pipelines) are exposed via GraphQL queries and mutations.
  name: GitLab GraphQL API
  slug: graphql
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Operations related to access requests
  name: GitLab CI/CD access_requests API
  slug: gitlab-ci-access-requests-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Operations about access_tokens
  name: GitLab CI/CD access_tokens API
  slug: gitlab-ci-access-tokens-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Operations about agents
  name: GitLab CI/CD Agents API
  slug: gitlab-ci-agents-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Operations about alert_managements
  name: GitLab CI/CD Alert Management API
  slug: gitlab-ci-alert-management-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Operations about applications
  name: GitLab CI/CD Applications API
  slug: gitlab-ci-applications-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Operations about attestations
  name: GitLab CI/CD Attestations API
  slug: gitlab-ci-attestations-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Operations about audit_events
  name: GitLab CI/CD Audit Events API
  slug: gitlab-ci-audit-events-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Operations about avatars
  name: GitLab CI/CD Avatars API
  slug: gitlab-ci-avatars-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Operations about award_emoji
  name: GitLab CI/CD Award Emoji API
  slug: gitlab-ci-award-emoji-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Operations about badges
  name: GitLab CI/CD Badges API
  slug: gitlab-ci-badges-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Operations about batched_background_migrations
  name: GitLab CI/CD Batched Background Migrations API
  slug: gitlab-ci-batched-background-migrations-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Operations about branches
  name: GitLab CI/CD Branches API
  slug: gitlab-ci-branches-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Operations about broadcast_messages
  name: GitLab CI/CD Broadcast Messages API
  slug: gitlab-ci-broadcast-messages-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Operations about chaos
  name: GitLab CI/CD Chaos API
  slug: gitlab-ci-chaos-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Operations about ci_catalogs
  name: GitLab CI/CD Ci Catalog API
  slug: gitlab-ci-ci-catalog-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Operations about ci_jobs
  name: GitLab CI/CD Ci Jobs API
  slug: gitlab-ci-ci-jobs-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Operations related to linting a CI config file
  name: GitLab CI/CD Ci Lint API
  slug: gitlab-ci-ci-lint-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Operations to manage job concurrency with resource groups
  name: GitLab CI/CD Ci Resource Groups API
  slug: gitlab-ci-ci-resource-groups-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Operations about ci_runners
  name: GitLab CI/CD Ci Runners API
  slug: gitlab-ci-ci-runners-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Operations about ci_triggers
  name: GitLab CI/CD Ci Triggers API
  slug: gitlab-ci-ci-triggers-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Operations related to CI/CD variables
  name: GitLab CI/CD Ci Variables API
  slug: gitlab-ci-ci-variables-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Operations related to the GitLab agent for Kubernetes
  name: GitLab CI/CD Cluster Agents API
  slug: gitlab-ci-cluster-agents-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Operations related to clusters
  name: GitLab CI/CD Clusters API
  slug: gitlab-ci-clusters-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Operations about commit_statuses
  name: GitLab CI/CD Commit Statuses API
  slug: gitlab-ci-commit-statuses-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Operations about commits
  name: GitLab CI/CD Commits API
  slug: gitlab-ci-commits-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Operations related to container registry
  name: GitLab CI/CD Container Registry API
  slug: gitlab-ci-container-registry-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Operations about custom_attributes
  name: GitLab CI/CD Custom Attributes API
  slug: gitlab-ci-custom-attributes-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Operations about database_dictionaries
  name: GitLab CI/CD Database Dictionary API
  slug: gitlab-ci-database-dictionary-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Operations to manage dependency proxy for a groups
  name: GitLab CI/CD Dependency Proxy API
  slug: gitlab-ci-dependency-proxy-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Operations about deploy_resources
  name: GitLab CI/CD Deploy Resources API
  slug: gitlab-ci-deploy-resources-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Operations about draft_notes
  name: GitLab CI/CD Draft Notes API
  slug: gitlab-ci-draft-notes-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Operations related to environments
  name: GitLab CI/CD Environments API
  slug: gitlab-ci-environments-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Operations about error_trackings
  name: GitLab CI/CD Error Tracking API
  slug: gitlab-ci-error-tracking-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Operations about events
  name: GitLab CI/CD Events API
  slug: gitlab-ci-events-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Operations related to feature flags
  name: GitLab CI/CD Feature Flags API
  slug: gitlab-ci-feature-flags-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Operations related to managing Flipper-based feature flags
  name: GitLab CI/CD Features API
  slug: gitlab-ci-features-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Operations about files
  name: GitLab CI/CD Files API
  slug: gitlab-ci-files-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Operations related to deploy freeze periods
  name: GitLab CI/CD Freeze Periods API
  slug: gitlab-ci-freeze-periods-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Operations related to Geo
  name: GitLab CI/CD Geo API
  slug: gitlab-ci-geo-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Operations about gitlab_pages
  name: GitLab CI/CD Gitlab Pages API
  slug: gitlab-ci-gitlab-pages-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Operations about glqls
  name: GitLab CI/CD Glql API
  slug: gitlab-ci-glql-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Operations about group_import_and_exports
  name: GitLab CI/CD Group Import And Export API
  slug: gitlab-ci-group-import-and-export-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Operations about groups
  name: GitLab CI/CD Groups API
  slug: gitlab-ci-groups-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Operations about hooks
  name: GitLab CI/CD Hooks API
  slug: gitlab-ci-hooks-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Operations about imports
  name: GitLab CI/CD Imports API
  slug: gitlab-ci-imports-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Operations about instances
  name: GitLab CI/CD Instance API
  slug: gitlab-ci-instance-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Operations related to integrations
  name: GitLab CI/CD Integrations API
  slug: gitlab-ci-integrations-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Operations about internal_operations
  name: GitLab CI/CD Internal Operations API
  slug: gitlab-ci-internal-operations-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Operations about invitations
  name: GitLab CI/CD Invitations API
  slug: gitlab-ci-invitations-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Operations about issues
  name: GitLab CI/CD Issues API
  slug: gitlab-ci-issues-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Operations related to JiraConnect subscriptions
  name: GitLab CI/CD Jira Connect Subscriptions API
  slug: gitlab-ci-jira-connect-subscriptions-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Operations about job_artifacts
  name: GitLab CI/CD Job Artifacts API
  slug: gitlab-ci-job-artifacts-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Operations about jobs
  name: GitLab CI/CD Jobs API
  slug: gitlab-ci-jobs-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Operations about keys
  name: GitLab CI/CD Keys API
  slug: gitlab-ci-keys-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Operations about ldaps
  name: GitLab CI/CD Ldap API
  slug: gitlab-ci-ldap-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Operations about markdowns
  name: GitLab CI/CD Markdown API
  slug: gitlab-ci-markdown-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Operations about members
  name: GitLab CI/CD Members API
  slug: gitlab-ci-members-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Operations about merge_request_approvals
  name: GitLab CI/CD Merge Request Approvals API
  slug: gitlab-ci-merge-request-approvals-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Operations related to merge requests
  name: GitLab CI/CD Merge Requests API
  slug: gitlab-ci-merge-requests-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Operations related to metadata of the GitLab instance
  name: GitLab CI/CD Metadata API
  slug: gitlab-ci-metadata-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Operations about metric_images
  name: GitLab CI/CD Metric Images API
  slug: gitlab-ci-metric-images-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Operations about metrics
  name: GitLab CI/CD Metrics API
  slug: gitlab-ci-metrics-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Operations about migrations
  name: GitLab CI/CD Migrations API
  slug: gitlab-ci-migrations-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Operations related to Model registry
  name: GitLab CI/CD Ml Model Registry API
  slug: gitlab-ci-ml-model-registry-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Operations about namespaces
  name: GitLab CI/CD Namespaces API
  slug: gitlab-ci-namespaces-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Operations about offline_transfers
  name: GitLab CI/CD Offline Transfers API
  slug: gitlab-ci-offline-transfers-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Operations about organizations
  name: GitLab CI/CD Organizations API
  slug: gitlab-ci-organizations-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Operations about packages
  name: GitLab CI/CD Packages API
  slug: gitlab-ci-packages-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Operations about pipeline_schedules
  name: GitLab CI/CD Pipeline Schedules API
  slug: gitlab-ci-pipeline-schedules-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Operations about pipelines
  name: GitLab CI/CD Pipelines API
  slug: gitlab-ci-pipelines-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Operations related to plan limits
  name: GitLab CI/CD Plan Limits API
  slug: gitlab-ci-plan-limits-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Operations related to importing projects
  name: GitLab CI/CD Project Import API
  slug: gitlab-ci-project-import-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Operations about project_snapshots
  name: GitLab CI/CD Project Snapshots API
  slug: gitlab-ci-project-snapshots-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Operations about project_templates
  name: GitLab CI/CD Project Templates API
  slug: gitlab-ci-project-templates-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Operations about project_topics
  name: GitLab CI/CD Project Topics API
  slug: gitlab-ci-project-topics-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Operations related to projects
  name: GitLab CI/CD Projects API
  slug: gitlab-ci-projects-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Operations about projects_job_token_scopes
  name: GitLab CI/CD Projects Job Token Scope API
  slug: gitlab-ci-projects-job-token-scope-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Operations about protected_branches
  name: GitLab CI/CD Protected Branches API
  slug: gitlab-ci-protected-branches-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Operations about protected_tags
  name: GitLab CI/CD Protected Tags API
  slug: gitlab-ci-protected-tags-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Operations related to PyPI packages
  name: GitLab CI/CD Pypi Packages API
  slug: gitlab-ci-pypi-packages-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Operations related to releases
  name: GitLab CI/CD Releases API
  slug: gitlab-ci-releases-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Operations about remote_mirrors
  name: GitLab CI/CD Remote Mirrors API
  slug: gitlab-ci-remote-mirrors-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Operations about repositories
  name: GitLab CI/CD Repositories API
  slug: gitlab-ci-repositories-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Operations about resource_events
  name: GitLab CI/CD Resource Events API
  slug: gitlab-ci-resource-events-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Operations about runners
  name: GitLab CI/CD Runners API
  slug: gitlab-ci-runners-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Operations about searches
  name: GitLab CI/CD Search API
  slug: gitlab-ci-search-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Operations about secure_files
  name: GitLab CI/CD Secure Files API
  slug: gitlab-ci-secure-files-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Operations about snippets
  name: GitLab CI/CD Snippets API
  slug: gitlab-ci-snippets-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Operations about submodules
  name: GitLab CI/CD Submodules API
  slug: gitlab-ci-submodules-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Operations related to suggestions
  name: GitLab CI/CD Suggestions API
  slug: gitlab-ci-suggestions-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Operations about tags
  name: GitLab CI/CD Tags API
  slug: gitlab-ci-tags-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Operations about terraforms
  name: GitLab CI/CD Terraform API
  slug: gitlab-ci-terraform-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Operations about unleashes
  name: GitLab CI/CD Unleash API
  slug: gitlab-ci-unleash-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Operations about usage_data
  name: GitLab CI/CD Usage Data API
  slug: gitlab-ci-usage-data-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Operations about users
  name: GitLab CI/CD Users API
  slug: gitlab-ci-users-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Operations about web_commits
  name: GitLab CI/CD Web Commits API
  slug: gitlab-ci-web-commits-api
- baseURL: https://gitlab.com/api/v4
  baseurl_source: declared
  description: Operations about wikis
  name: GitLab CI/CD Wikis API
  slug: gitlab-ci-wikis-api
artifact_total: 208
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: GitLab access_requests API
  slug: open-gitlab-ci-access-requests-api
- collection_type: open
  name: GitLab access_requests access_tokens API
  slug: open-gitlab-ci-access-tokens-api
- collection_type: open
  name: GitLab access_requests agents API
  slug: open-gitlab-ci-agents-api
- collection_type: open
  name: GitLab access_requests alert_management API
  slug: open-gitlab-ci-alert-management-api
- collection_type: open
  name: GitLab access_requests applications API
  slug: open-gitlab-ci-applications-api
- collection_type: open
  name: GitLab access_requests attestations API
  slug: open-gitlab-ci-attestations-api
- collection_type: open
  name: GitLab access_requests audit_events API
  slug: open-gitlab-ci-audit-events-api
- collection_type: open
  name: GitLab access_requests avatars API
  slug: open-gitlab-ci-avatars-api
- collection_type: open
  name: GitLab access_requests award_emoji API
  slug: open-gitlab-ci-award-emoji-api
- collection_type: open
  name: GitLab access_requests badges API
  slug: open-gitlab-ci-badges-api
- collection_type: open
  name: GitLab access_requests batched_background_migrations API
  slug: open-gitlab-ci-batched-background-migrations-api
- collection_type: open
  name: GitLab access_requests branches API
  slug: open-gitlab-ci-branches-api
- collection_type: open
  name: GitLab access_requests broadcast_messages API
  slug: open-gitlab-ci-broadcast-messages-api
- collection_type: open
  name: GitLab access_requests chaos API
  slug: open-gitlab-ci-chaos-api
- collection_type: open
  name: GitLab access_requests ci_catalog API
  slug: open-gitlab-ci-ci-catalog-api
- collection_type: open
  name: GitLab access_requests ci_jobs API
  slug: open-gitlab-ci-ci-jobs-api
- collection_type: open
  name: GitLab access_requests ci_lint API
  slug: open-gitlab-ci-ci-lint-api
- collection_type: open
  name: GitLab access_requests ci_resource_groups API
  slug: open-gitlab-ci-ci-resource-groups-api
- collection_type: open
  name: GitLab access_requests ci_runners API
  slug: open-gitlab-ci-ci-runners-api
- collection_type: open
  name: GitLab access_requests ci_triggers API
  slug: open-gitlab-ci-ci-triggers-api
- collection_type: open
  name: GitLab access_requests ci_variables API
  slug: open-gitlab-ci-ci-variables-api
- collection_type: open
  name: GitLab access_requests cluster_agents API
  slug: open-gitlab-ci-cluster-agents-api
- collection_type: open
  name: GitLab access_requests clusters API
  slug: open-gitlab-ci-clusters-api
- collection_type: open
  name: GitLab access_requests commit_statuses API
  slug: open-gitlab-ci-commit-statuses-api
- collection_type: open
  name: GitLab access_requests commits API
  slug: open-gitlab-ci-commits-api
- collection_type: open
  name: GitLab access_requests container_registry API
  slug: open-gitlab-ci-container-registry-api
- collection_type: open
  name: GitLab access_requests custom_attributes API
  slug: open-gitlab-ci-custom-attributes-api
- collection_type: open
  name: GitLab access_requests database_dictionary API
  slug: open-gitlab-ci-database-dictionary-api
- collection_type: open
  name: GitLab access_requests dependency_proxy API
  slug: open-gitlab-ci-dependency-proxy-api
- collection_type: open
  name: GitLab access_requests deploy_resources API
  slug: open-gitlab-ci-deploy-resources-api
- collection_type: open
  name: GitLab access_requests draft_notes API
  slug: open-gitlab-ci-draft-notes-api
- collection_type: open
  name: GitLab access_requests environments API
  slug: open-gitlab-ci-environments-api
- collection_type: open
  name: GitLab access_requests error_tracking API
  slug: open-gitlab-ci-error-tracking-api
- collection_type: open
  name: GitLab access_requests events API
  slug: open-gitlab-ci-events-api
- collection_type: open
  name: GitLab access_requests feature_flags API
  slug: open-gitlab-ci-feature-flags-api
- collection_type: open
  name: GitLab access_requests features API
  slug: open-gitlab-ci-features-api
- collection_type: open
  name: GitLab access_requests files API
  slug: open-gitlab-ci-files-api
- collection_type: open
  name: GitLab access_requests freeze_periods API
  slug: open-gitlab-ci-freeze-periods-api
- collection_type: open
  name: GitLab access_requests geo API
  slug: open-gitlab-ci-geo-api
- collection_type: open
  name: GitLab access_requests gitlab_pages API
  slug: open-gitlab-ci-gitlab-pages-api
- collection_type: open
  name: GitLab access_requests glql API
  slug: open-gitlab-ci-glql-api
- collection_type: open
  name: GitLab access_requests group_import_and_export API
  slug: open-gitlab-ci-group-import-and-export-api
- collection_type: open
  name: GitLab access_requests groups API
  slug: open-gitlab-ci-groups-api
- collection_type: open
  name: GitLab access_requests hooks API
  slug: open-gitlab-ci-hooks-api
- collection_type: open
  name: GitLab access_requests imports API
  slug: open-gitlab-ci-imports-api
- collection_type: open
  name: GitLab access_requests instance API
  slug: open-gitlab-ci-instance-api
- collection_type: open
  name: GitLab access_requests integrations API
  slug: open-gitlab-ci-integrations-api
- collection_type: open
  name: GitLab access_requests internal_operations API
  slug: open-gitlab-ci-internal-operations-api
- collection_type: open
  name: GitLab access_requests invitations API
  slug: open-gitlab-ci-invitations-api
- collection_type: open
  name: GitLab access_requests issues API
  slug: open-gitlab-ci-issues-api
- collection_type: open
  name: GitLab access_requests jira_connect_subscriptions API
  slug: open-gitlab-ci-jira-connect-subscriptions-api
- collection_type: open
  name: GitLab access_requests job_artifacts API
  slug: open-gitlab-ci-job-artifacts-api
- collection_type: open
  name: GitLab access_requests jobs API
  slug: open-gitlab-ci-jobs-api
- collection_type: open
  name: GitLab access_requests keys API
  slug: open-gitlab-ci-keys-api
- collection_type: open
  name: GitLab access_requests ldap API
  slug: open-gitlab-ci-ldap-api
- collection_type: open
  name: GitLab access_requests markdown API
  slug: open-gitlab-ci-markdown-api
- collection_type: open
  name: GitLab access_requests members API
  slug: open-gitlab-ci-members-api
- collection_type: open
  name: GitLab access_requests merge_request_approvals API
  slug: open-gitlab-ci-merge-request-approvals-api
- collection_type: open
  name: GitLab access_requests merge_requests API
  slug: open-gitlab-ci-merge-requests-api
- collection_type: open
  name: GitLab access_requests metadata API
  slug: open-gitlab-ci-metadata-api
- collection_type: open
  name: GitLab access_requests metric_images API
  slug: open-gitlab-ci-metric-images-api
- collection_type: open
  name: GitLab access_requests metrics API
  slug: open-gitlab-ci-metrics-api
- collection_type: open
  name: GitLab access_requests migrations API
  slug: open-gitlab-ci-migrations-api
- collection_type: open
  name: GitLab access_requests ml_model_registry API
  slug: open-gitlab-ci-ml-model-registry-api
- collection_type: open
  name: GitLab access_requests namespaces API
  slug: open-gitlab-ci-namespaces-api
- collection_type: open
  name: GitLab access_requests offline_transfers API
  slug: open-gitlab-ci-offline-transfers-api
- collection_type: open
  name: GitLab access_requests organizations API
  slug: open-gitlab-ci-organizations-api
- collection_type: open
  name: GitLab access_requests packages API
  slug: open-gitlab-ci-packages-api
- collection_type: open
  name: GitLab access_requests pipeline_schedules API
  slug: open-gitlab-ci-pipeline-schedules-api
- collection_type: open
  name: GitLab access_requests pipelines API
  slug: open-gitlab-ci-pipelines-api
- collection_type: open
  name: GitLab access_requests plan_limits API
  slug: open-gitlab-ci-plan-limits-api
- collection_type: open
  name: GitLab access_requests project_import API
  slug: open-gitlab-ci-project-import-api
- collection_type: open
  name: GitLab access_requests project_snapshots API
  slug: open-gitlab-ci-project-snapshots-api
- collection_type: open
  name: GitLab access_requests project_templates API
  slug: open-gitlab-ci-project-templates-api
- collection_type: open
  name: GitLab access_requests project_topics API
  slug: open-gitlab-ci-project-topics-api
- collection_type: open
  name: GitLab access_requests projects API
  slug: open-gitlab-ci-projects-api
- collection_type: open
  name: GitLab access_requests projects_job_token_scope API
  slug: open-gitlab-ci-projects-job-token-scope-api
- collection_type: open
  name: GitLab access_requests protected_branches API
  slug: open-gitlab-ci-protected-branches-api
- collection_type: open
  name: GitLab access_requests protected_tags API
  slug: open-gitlab-ci-protected-tags-api
- collection_type: open
  name: GitLab access_requests pypi_packages API
  slug: open-gitlab-ci-pypi-packages-api
- collection_type: open
  name: GitLab access_requests releases API
  slug: open-gitlab-ci-releases-api
- collection_type: open
  name: GitLab access_requests remote_mirrors API
  slug: open-gitlab-ci-remote-mirrors-api
- collection_type: open
  name: GitLab access_requests repositories API
  slug: open-gitlab-ci-repositories-api
- collection_type: open
  name: GitLab access_requests resource_events API
  slug: open-gitlab-ci-resource-events-api
- collection_type: open
  name: GitLab access_requests runners API
  slug: open-gitlab-ci-runners-api
- collection_type: open
  name: GitLab access_requests search API
  slug: open-gitlab-ci-search-api
- collection_type: open
  name: GitLab access_requests secure_files API
  slug: open-gitlab-ci-secure-files-api
- collection_type: open
  name: GitLab access_requests snippets API
  slug: open-gitlab-ci-snippets-api
- collection_type: open
  name: GitLab access_requests submodules API
  slug: open-gitlab-ci-submodules-api
- collection_type: open
  name: GitLab access_requests suggestions API
  slug: open-gitlab-ci-suggestions-api
- collection_type: open
  name: GitLab access_requests tags API
  slug: open-gitlab-ci-tags-api
- collection_type: open
  name: GitLab access_requests terraform API
  slug: open-gitlab-ci-terraform-api
- collection_type: open
  name: GitLab access_requests unleash API
  slug: open-gitlab-ci-unleash-api
- collection_type: open
  name: GitLab access_requests usage_data API
  slug: open-gitlab-ci-usage-data-api
- collection_type: open
  name: GitLab access_requests users API
  slug: open-gitlab-ci-users-api
- collection_type: open
  name: GitLab access_requests web_commits API
  slug: open-gitlab-ci-web-commits-api
- collection_type: open
  name: GitLab access_requests wikis API
  slug: open-gitlab-ci-wikis-api
- collection_type: open
  name: GitLab API
  slug: open-gitlab-ci
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/gitlab-ci/refs/heads/main/capabilities/gitlab-ci-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/gitlab-ci-capability-edges.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/gitlab-ci/refs/heads/main/agentic-access/gitlab-ci-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/gitlab-ci-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/gitlab-ci/refs/heads/main/security/gitlab-ci-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/gitlab-ci-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/gitlab-ci/refs/heads/main/security/gitlab-ci-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/gitlab-ci-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/gitlab-ci/refs/heads/main/security/gitlab-ci-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/gitlab-ci-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/gitlab-ci/refs/heads/main/authentication/gitlab-ci-authentication.yml
  title: ''
  type: Authentication
  url: authentication/gitlab-ci-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://about.gitlab.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.gitlab.com/api/
- group: commercial
  title: ''
  type: Pricing
  url: https://about.gitlab.com/pricing/
- group: build
  title: ''
  type: GitHub
  url: https://gitlab.com/gitlab-org/gitlab
- group: operate
  title: ''
  type: StatusPage
  url: https://status.gitlab.com/
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/gitlab-ci/refs/heads/main/plans/gitlab-ci-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/gitlab-ci-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/gitlab-ci/refs/heads/main/rate-limits/gitlab-ci-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/gitlab-ci-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/gitlab-ci/refs/heads/main/finops/gitlab-ci-finops.yml
  title: ''
  type: FinOps
  url: finops/gitlab-ci-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.gitlab.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://about.gitlab.com/atom.xml
created: '2026-05-08'
description: GitLab CI/CD is the built-in continuous integration, delivery and deployment platform for GitLab. The CI/CD surface area within GitLab's REST API v4 covers pipelines, jobs, pipeline schedules, pipeline triggers, runners, agents, releases, environments, deployments, package and container registries, and the security/dependency scanners. GitLab also exposes a GraphQL API.
finops:
- name: Gitlab Ci Finops
  service_category: DevOps / CI/CD
  slug: gitlab-ci-finops
graphqls:
- description: GitLab's GraphQL API at /api/graphql. Many CI/CD entities (Pipeline, CiJob, CiRunner, MergeRequest pipelines) are exposed via GraphQL queries and mutations.
  name: GitLab CI/CD GraphQL API
  slug: gitlab-ci-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gitlab-ci.png
json_structures:
- name: Gitlab Ci Structure
  property_count: 0
  slug: gitlab-ci-structure
layout: provider
modified: '2026-05-19'
name: GitLab CI/CD
nav: Providers
network: true
overview: 'GitLab CI/CD publishes 98 APIs on the [APIs.io](https://apis.io/) network, including access_requests API, access_tokens API, Agents API, and 95 more. Tagged areas include DevOps, CI/CD, Pipelines, GitLab, and DevSecOps.


  GitLab CI/CD''s developer surface includes authentication, documentation, pricing, GitHub presence, engineering blog, and 11 more developer resources.'
plans:
- name: Gitlab Ci Plans Pricing
  plan_count: 9
  slug: gitlab-ci-plans-pricing
- name: Gitlab Ci Price Estimates
  plan_count: 0
  slug: gitlab-ci-price-estimates
random_paper: 18
rate_limits:
- limit_count: 2
  name: Gitlab Ci Rate Limits
  slug: gitlab-ci-rate-limits
score:
  band: developing
  composite: 45.1
  coverage:
    artifact_dirs: 18
    catalog_earned: 57.0
    catalog_earned_first_party: 20.0
    catalog_gap: 58.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.2
  facets:
    access_clarity: 57.9
    contract_governance: 0.0
    contract_quality: 44.6
    developer_ergonomics: 31.0
    discoverability: 70.0
    operational_transparency: 42.1
  previous_composite: 45.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 97
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.5
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: true
    score: 33.3
screenshot: https://raw.githubusercontent.com/api-evangelist/gitlab-ci/refs/heads/main/screenshots/gitlab-ci-2026-06-20T181847.png
security:
- kind: authentication
  name: Gitlab Ci Authentication
  slug: gitlab-ci-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Gitlab Ci Domain Security
  slug: gitlab-ci-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Gitlab Ci Vulnerability Disclosure
  slug: gitlab-ci-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Gitlab Ci Trust Center
  slug: gitlab-ci-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, PCI DSS, GDPR, CSA STAR
slug: gitlab-ci
tags:
- DevOps
- CI/CD
- Pipelines
- GitLab
- DevSecOps
- Runners
- Container Registry
- Developer Tools
website: https://about.gitlab.com/
---
