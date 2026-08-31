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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.5
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 627
  human_in_the_loop: 22
  name: Gitlab Ci Agentic Access
  operation_count: 1125
  slug: gitlab-ci-agentic-access
  summary_line: 1125 operations · 627 acting · 22 human-in-the-loop
api_count: 1
apis:
- description: GitLab's GraphQL API at /api/graphql. Many CI/CD entities (Pipeline, CiJob, CiRunner, MergeRequest pipelines) are exposed via GraphQL queries and mutations.
  name: GitLab GraphQL API
  slug: graphql
- description: Operations related to access requests
  name: GitLab CI/CD access_requests API
  slug: gitlab-ci-access-requests-api
- description: Operations about access_tokens
  name: GitLab CI/CD access_tokens API
  slug: gitlab-ci-access-tokens-api
- description: Operations about agents
  name: GitLab CI/CD agents API
  slug: gitlab-ci-agents-api
- description: Operations about alert_managements
  name: GitLab CI/CD alert_management API
  slug: gitlab-ci-alert-management-api
- description: Operations about applications
  name: GitLab CI/CD applications API
  slug: gitlab-ci-applications-api
- description: Operations about attestations
  name: GitLab CI/CD attestations API
  slug: gitlab-ci-attestations-api
- description: Operations about audit_events
  name: GitLab CI/CD audit_events API
  slug: gitlab-ci-audit-events-api
- description: Operations about avatars
  name: GitLab CI/CD avatars API
  slug: gitlab-ci-avatars-api
- description: Operations about award_emoji
  name: GitLab CI/CD award_emoji API
  slug: gitlab-ci-award-emoji-api
- description: Operations about badges
  name: GitLab CI/CD badges API
  slug: gitlab-ci-badges-api
- description: Operations about batched_background_migrations
  name: GitLab CI/CD batched_background_migrations API
  slug: gitlab-ci-batched-background-migrations-api
- description: Operations about branches
  name: GitLab CI/CD branches API
  slug: gitlab-ci-branches-api
- description: Operations about broadcast_messages
  name: GitLab CI/CD broadcast_messages API
  slug: gitlab-ci-broadcast-messages-api
- description: Operations about chaos
  name: GitLab CI/CD chaos API
  slug: gitlab-ci-chaos-api
- description: Operations about ci_catalogs
  name: GitLab CI/CD ci_catalog API
  slug: gitlab-ci-ci-catalog-api
- description: Operations about ci_jobs
  name: GitLab CI/CD ci_jobs API
  slug: gitlab-ci-ci-jobs-api
- description: Operations related to linting a CI config file
  name: GitLab CI/CD ci_lint API
  slug: gitlab-ci-ci-lint-api
- description: Operations to manage job concurrency with resource groups
  name: GitLab CI/CD ci_resource_groups API
  slug: gitlab-ci-ci-resource-groups-api
- description: Operations about ci_runners
  name: GitLab CI/CD ci_runners API
  slug: gitlab-ci-ci-runners-api
- description: Operations about ci_triggers
  name: GitLab CI/CD ci_triggers API
  slug: gitlab-ci-ci-triggers-api
- description: Operations related to CI/CD variables
  name: GitLab CI/CD ci_variables API
  slug: gitlab-ci-ci-variables-api
- description: Operations related to the GitLab agent for Kubernetes
  name: GitLab CI/CD cluster_agents API
  slug: gitlab-ci-cluster-agents-api
- description: Operations related to clusters
  name: GitLab CI/CD clusters API
  slug: gitlab-ci-clusters-api
- description: Operations about commit_statuses
  name: GitLab CI/CD commit_statuses API
  slug: gitlab-ci-commit-statuses-api
- description: Operations about commits
  name: GitLab CI/CD commits API
  slug: gitlab-ci-commits-api
- description: Operations related to container registry
  name: GitLab CI/CD container_registry API
  slug: gitlab-ci-container-registry-api
- description: Operations about custom_attributes
  name: GitLab CI/CD custom_attributes API
  slug: gitlab-ci-custom-attributes-api
- description: Operations about database_dictionaries
  name: GitLab CI/CD database_dictionary API
  slug: gitlab-ci-database-dictionary-api
- description: Operations to manage dependency proxy for a groups
  name: GitLab CI/CD dependency_proxy API
  slug: gitlab-ci-dependency-proxy-api
- description: Operations about deploy_resources
  name: GitLab CI/CD deploy_resources API
  slug: gitlab-ci-deploy-resources-api
- description: Operations about draft_notes
  name: GitLab CI/CD draft_notes API
  slug: gitlab-ci-draft-notes-api
- description: Operations related to environments
  name: GitLab CI/CD environments API
  slug: gitlab-ci-environments-api
- description: Operations about error_trackings
  name: GitLab CI/CD error_tracking API
  slug: gitlab-ci-error-tracking-api
- description: Operations about events
  name: GitLab CI/CD events API
  slug: gitlab-ci-events-api
- description: Operations related to feature flags
  name: GitLab CI/CD feature_flags API
  slug: gitlab-ci-feature-flags-api
- description: Operations related to managing Flipper-based feature flags
  name: GitLab CI/CD features API
  slug: gitlab-ci-features-api
- description: Operations about files
  name: GitLab CI/CD files API
  slug: gitlab-ci-files-api
- description: Operations related to deploy freeze periods
  name: GitLab CI/CD freeze_periods API
  slug: gitlab-ci-freeze-periods-api
- description: Operations related to Geo
  name: GitLab CI/CD geo API
  slug: gitlab-ci-geo-api
- description: Operations about gitlab_pages
  name: GitLab CI/CD gitlab_pages API
  slug: gitlab-ci-gitlab-pages-api
- description: Operations about glqls
  name: GitLab CI/CD glql API
  slug: gitlab-ci-glql-api
- description: Operations about group_import_and_exports
  name: GitLab CI/CD group_import_and_export API
  slug: gitlab-ci-group-import-and-export-api
- description: Operations about groups
  name: GitLab CI/CD groups API
  slug: gitlab-ci-groups-api
- description: Operations about hooks
  name: GitLab CI/CD hooks API
  slug: gitlab-ci-hooks-api
- description: Operations about imports
  name: GitLab CI/CD imports API
  slug: gitlab-ci-imports-api
- description: Operations about instances
  name: GitLab CI/CD instance API
  slug: gitlab-ci-instance-api
- description: Operations related to integrations
  name: GitLab CI/CD integrations API
  slug: gitlab-ci-integrations-api
- description: Operations about internal_operations
  name: GitLab CI/CD internal_operations API
  slug: gitlab-ci-internal-operations-api
- description: Operations about invitations
  name: GitLab CI/CD invitations API
  slug: gitlab-ci-invitations-api
- description: Operations about issues
  name: GitLab CI/CD issues API
  slug: gitlab-ci-issues-api
- description: Operations related to JiraConnect subscriptions
  name: GitLab CI/CD jira_connect_subscriptions API
  slug: gitlab-ci-jira-connect-subscriptions-api
- description: Operations about job_artifacts
  name: GitLab CI/CD job_artifacts API
  slug: gitlab-ci-job-artifacts-api
- description: Operations about jobs
  name: GitLab CI/CD jobs API
  slug: gitlab-ci-jobs-api
- description: Operations about keys
  name: GitLab CI/CD keys API
  slug: gitlab-ci-keys-api
- description: Operations about ldaps
  name: GitLab CI/CD ldap API
  slug: gitlab-ci-ldap-api
- description: Operations about markdowns
  name: GitLab CI/CD markdown API
  slug: gitlab-ci-markdown-api
- description: Operations about members
  name: GitLab CI/CD members API
  slug: gitlab-ci-members-api
- description: Operations about merge_request_approvals
  name: GitLab CI/CD merge_request_approvals API
  slug: gitlab-ci-merge-request-approvals-api
- description: Operations related to merge requests
  name: GitLab CI/CD merge_requests API
  slug: gitlab-ci-merge-requests-api
- description: Operations related to metadata of the GitLab instance
  name: GitLab CI/CD metadata API
  slug: gitlab-ci-metadata-api
- description: Operations about metric_images
  name: GitLab CI/CD metric_images API
  slug: gitlab-ci-metric-images-api
- description: Operations about metrics
  name: GitLab CI/CD metrics API
  slug: gitlab-ci-metrics-api
- description: Operations about migrations
  name: GitLab CI/CD migrations API
  slug: gitlab-ci-migrations-api
- description: Operations related to Model registry
  name: GitLab CI/CD ml_model_registry API
  slug: gitlab-ci-ml-model-registry-api
- description: Operations about namespaces
  name: GitLab CI/CD namespaces API
  slug: gitlab-ci-namespaces-api
- description: Operations about offline_transfers
  name: GitLab CI/CD offline_transfers API
  slug: gitlab-ci-offline-transfers-api
- description: Operations about organizations
  name: GitLab CI/CD organizations API
  slug: gitlab-ci-organizations-api
- description: Operations about packages
  name: GitLab CI/CD packages API
  slug: gitlab-ci-packages-api
- description: Operations about pipeline_schedules
  name: GitLab CI/CD pipeline_schedules API
  slug: gitlab-ci-pipeline-schedules-api
- description: Operations about pipelines
  name: GitLab CI/CD pipelines API
  slug: gitlab-ci-pipelines-api
- description: Operations related to plan limits
  name: GitLab CI/CD plan_limits API
  slug: gitlab-ci-plan-limits-api
- description: Operations related to importing projects
  name: GitLab CI/CD project_import API
  slug: gitlab-ci-project-import-api
- description: Operations about project_snapshots
  name: GitLab CI/CD project_snapshots API
  slug: gitlab-ci-project-snapshots-api
- description: Operations about project_templates
  name: GitLab CI/CD project_templates API
  slug: gitlab-ci-project-templates-api
- description: Operations about project_topics
  name: GitLab CI/CD project_topics API
  slug: gitlab-ci-project-topics-api
- description: Operations related to projects
  name: GitLab CI/CD projects API
  slug: gitlab-ci-projects-api
- description: Operations about projects_job_token_scopes
  name: GitLab CI/CD projects_job_token_scope API
  slug: gitlab-ci-projects-job-token-scope-api
- description: Operations about protected_branches
  name: GitLab CI/CD protected_branches API
  slug: gitlab-ci-protected-branches-api
- description: Operations about protected_tags
  name: GitLab CI/CD protected_tags API
  slug: gitlab-ci-protected-tags-api
- description: Operations related to PyPI packages
  name: GitLab CI/CD pypi_packages API
  slug: gitlab-ci-pypi-packages-api
- description: Operations related to releases
  name: GitLab CI/CD releases API
  slug: gitlab-ci-releases-api
- description: Operations about remote_mirrors
  name: GitLab CI/CD remote_mirrors API
  slug: gitlab-ci-remote-mirrors-api
- description: Operations about repositories
  name: GitLab CI/CD repositories API
  slug: gitlab-ci-repositories-api
- description: Operations about resource_events
  name: GitLab CI/CD resource_events API
  slug: gitlab-ci-resource-events-api
- description: Operations about runners
  name: GitLab CI/CD runners API
  slug: gitlab-ci-runners-api
- description: Operations about searches
  name: GitLab CI/CD search API
  slug: gitlab-ci-search-api
- description: Operations about secure_files
  name: GitLab CI/CD secure_files API
  slug: gitlab-ci-secure-files-api
- description: Operations about snippets
  name: GitLab CI/CD snippets API
  slug: gitlab-ci-snippets-api
- description: Operations about submodules
  name: GitLab CI/CD submodules API
  slug: gitlab-ci-submodules-api
- description: Operations related to suggestions
  name: GitLab CI/CD suggestions API
  slug: gitlab-ci-suggestions-api
- description: Operations about tags
  name: GitLab CI/CD tags API
  slug: gitlab-ci-tags-api
- description: Operations about terraforms
  name: GitLab CI/CD terraform API
  slug: gitlab-ci-terraform-api
- description: Operations about unleashes
  name: GitLab CI/CD unleash API
  slug: gitlab-ci-unleash-api
- description: Operations about usage_data
  name: GitLab CI/CD usage_data API
  slug: gitlab-ci-usage-data-api
- description: Operations about users
  name: GitLab CI/CD users API
  slug: gitlab-ci-users-api
- description: Operations about web_commits
  name: GitLab CI/CD web_commits API
  slug: gitlab-ci-web-commits-api
- description: Operations about wikis
  name: GitLab CI/CD wikis API
  slug: gitlab-ci-wikis-api
artifact_total: 207
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
  title: ''
  type: CapabilityMap
  url: capabilities/gitlab-ci-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/gitlab-ci-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/gitlab-ci-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/gitlab-ci-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gitlab-ci-domain-security.yml
- group: auth
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
  title: ''
  type: Plans
  url: plans/gitlab-ci-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/gitlab-ci-rate-limits.yml
- group: commercial
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
overview: 'GitLab CI/CD publishes 97 APIs on the [APIs.io](https://apis.io/) network, including access_requests API, access_tokens API, agents API, and 94 more. Tagged areas include DevOps, CI/CD, Pipelines, GitLab, and DevSecOps.


  GitLab CI/CD''s developer surface includes authentication, documentation, pricing, GitHub presence, engineering blog, and 11 more developer resources.'
plans:
- name: Gitlab Ci Plans Pricing
  plan_count: 5
  slug: gitlab-ci-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 10
  name: Gitlab Ci Rate Limits
  slug: gitlab-ci-rate-limits
score:
  band: thin
  composite: 36.4
  coverage:
    artifact_dirs: 17
    catalog_gap: 72.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 50.4
    developer_ergonomics: 31.0
    discoverability: 70.4
    governance: 0.0
    operational_transparency: 28.9
  previous_composite: 37.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 97
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
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
website: https://about.gitlab.com/
---
