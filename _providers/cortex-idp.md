---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 41.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 25
  human_in_the_loop: 0
  name: Cortex Idp Agentic Access
  operation_count: 47
  slug: cortex-idp-agentic-access
  summary_line: 47 operations · 25 acting
api_count: 1
apis:
- baseURL: https://api.getcortexapp.com/api/v1
  baseurl_source: declared
  description: Arbitrary key/value metadata attached to catalog entities.
  name: Cortex Custom Data API
  slug: cortex-idp-custom-data-api
- baseURL: https://api.getcortexapp.com/api/v1
  baseurl_source: declared
  description: Deployment events recorded per catalog entity.
  name: Cortex Deploys API
  slug: cortex-idp-deploys-api
- baseURL: https://api.getcortexapp.com/api/v1
  baseurl_source: declared
  description: Time-boxed improvement campaigns driving entities toward a Scorecard target.
  name: Cortex Initiatives API
  slug: cortex-idp-initiatives-api
- baseURL: https://api.getcortexapp.com/api/v1
  baseurl_source: declared
  description: Standards that measure catalog entities, with scores and exemptions.
  name: Cortex Scorecards API
  slug: cortex-idp-scorecards-api
- description: REST endpoints to list and inspect entity-to-entity dependencies (caller and callee) and the relationships used to build the service graph.
  name: Cortex Dependencies API
  slug: dependencies-api
- description: REST endpoints for managing and querying Workflow runs, used to drive developer self-service actions and scaffolding from the Cortex IDP.
  name: Cortex Workflow Runs API
  slug: workflows-api
- description: Model Context Protocol server exposing Cortex catalog, scorecards, dependencies, and on-call data to AI agents and copilots through MCP tools and resources.
  name: Cortex MCP Server
  slug: mcp
- baseURL: https://api.getcortexapp.com/api/v1
  baseurl_source: declared
  description: The API Keys API from Cortex — 2 operation(s) for api keys.
  name: Cortex API Keys API
  slug: cortex-idp-api-keys-api
- baseURL: https://api.getcortexapp.com/api/v1
  baseurl_source: declared
  description: The Audit Logs API from Cortex — 1 operation(s) for audit logs.
  name: Cortex Audit Logs API
  slug: cortex-idp-audit-logs-api
- baseURL: https://api.getcortexapp.com/api/v1
  baseurl_source: declared
  description: The Catalog Entities API from Cortex — 13 operation(s) for catalog entities.
  name: Cortex Catalog Entities API
  slug: cortex-idp-catalog-entities-api
- baseURL: https://api.getcortexapp.com/api/v1
  baseurl_source: declared
  description: The Catalogs API from Cortex — 2 operation(s) for catalogs.
  name: Cortex Catalogs API
  slug: cortex-idp-catalogs-api
- baseURL: https://api.getcortexapp.com/api/v1
  baseurl_source: declared
  description: The Custom Data [Advanced] API from Cortex — 1 operation(s) for custom data [advanced].
  name: Cortex Custom Data [Advanced] API
  slug: cortex-idp-custom-data-advanced-api
- baseURL: https://api.getcortexapp.com/api/v1
  baseurl_source: declared
  description: The Custom Events API from Cortex — 2 operation(s) for custom events.
  name: Cortex Custom Events API
  slug: cortex-idp-custom-events-api
- baseURL: https://api.getcortexapp.com/api/v1
  baseurl_source: declared
  description: The Custom Metrics API from Cortex — 4 operation(s) for custom metrics.
  name: Cortex Custom Metrics API
  slug: cortex-idp-custom-metrics-api
- baseURL: https://api.getcortexapp.com/api/v1
  baseurl_source: declared
  description: The Dependencies API from Cortex — 3 operation(s) for dependencies.
  name: Cortex Dependencies API
  slug: cortex-idp-dependencies-api
- baseURL: https://api.getcortexapp.com/api/v1
  baseurl_source: declared
  description: The dev-login-controller API from Cortex — 1 operation(s) for dev-login-controller.
  name: Cortex Dev Login Controller API
  slug: cortex-idp-dev-login-controller-api
- baseURL: https://api.getcortexapp.com/api/v1
  baseurl_source: declared
  description: The Discovery Audit API from Cortex — 1 operation(s) for discovery audit.
  name: Cortex Discovery Audit API
  slug: cortex-idp-discovery-audit-api
- baseURL: https://api.getcortexapp.com/api/v1
  baseurl_source: declared
  description: The Docs API from Cortex — 1 operation(s) for docs.
  name: Cortex Docs API
  slug: cortex-idp-docs-api
- baseURL: https://api.getcortexapp.com/api/v1
  baseurl_source: declared
  description: 'The Eng Intel: 1-Registry API from Cortex — 1 operation(s) for eng intel: 1-registry.'
  name: 'Cortex Eng Intel: 1-Registry API'
  slug: cortex-idp-eng-intel-1-registry-api
- baseURL: https://api.getcortexapp.com/api/v1
  baseurl_source: declared
  description: 'The Eng Intel: 2-Metrics API from Cortex — 1 operation(s) for eng intel: 2-metrics.'
  name: 'Cortex Eng Intel: 2-Metrics API'
  slug: cortex-idp-eng-intel-2-metrics-api
- baseURL: https://api.getcortexapp.com/api/v1
  baseurl_source: declared
  description: 'The Eng Intel: 3-Trace API from Cortex — 1 operation(s) for eng intel: 3-trace.'
  name: 'Cortex Eng Intel: 3-Trace API'
  slug: cortex-idp-eng-intel-3-trace-api
- baseURL: https://api.getcortexapp.com/api/v1
  baseurl_source: declared
  description: 'The Eng Intel: User Labels API from Cortex — 3 operation(s) for eng intel: user labels.'
  name: 'Cortex Eng Intel: User Labels API'
  slug: cortex-idp-eng-intel-user-labels-api
- baseURL: https://api.getcortexapp.com/api/v1
  baseurl_source: declared
  description: The Entity Relationship Types API from Cortex — 2 operation(s) for entity relationship types.
  name: Cortex Entity Relationship Types API
  slug: cortex-idp-entity-relationship-types-api
- baseURL: https://api.getcortexapp.com/api/v1
  baseurl_source: declared
  description: The Entity Relationships API from Cortex — 3 operation(s) for entity relationships.
  name: Cortex Entity Relationships API
  slug: cortex-idp-entity-relationships-api
- baseURL: https://api.getcortexapp.com/api/v1
  baseurl_source: declared
  description: The Entity Types API from Cortex — 2 operation(s) for entity types.
  name: Cortex Entity Types API
  slug: cortex-idp-entity-types-api
- baseURL: https://api.getcortexapp.com/api/v1
  baseurl_source: declared
  description: The GitOps Logs API from Cortex — 1 operation(s) for gitops logs.
  name: Cortex GitOps Logs API
  slug: cortex-idp-gitops-logs-api
- baseURL: https://api.getcortexapp.com/api/v1
  baseurl_source: declared
  description: The Groups API from Cortex — 1 operation(s) for groups.
  name: Cortex Groups API
  slug: cortex-idp-groups-api
- baseURL: https://api.getcortexapp.com/api/v1
  baseurl_source: declared
  description: The Integration Status API from Cortex — 1 operation(s) for integration status.
  name: Cortex Integration Status API
  slug: cortex-idp-integration-status-api
- baseURL: https://api.getcortexapp.com/api/v1
  baseurl_source: declared
  description: The [Integrations] Anthropic API from Cortex — 6 operation(s) for [integrations] anthropic.
  name: Cortex [Integrations] Anthropic API
  slug: cortex-idp-integrations-anthropic-api
- baseURL: https://api.getcortexapp.com/api/v1
  baseurl_source: declared
  description: The [Integrations] Apiiro API from Cortex — 6 operation(s) for [integrations] apiiro.
  name: Cortex [Integrations] Apiiro API
  slug: cortex-idp-integrations-apiiro-api
- baseURL: https://api.getcortexapp.com/api/v1
  baseurl_source: declared
  description: The [Integrations] ArgoCD API from Cortex — 6 operation(s) for [integrations] argocd.
  name: Cortex [Integrations] ArgoCD API
  slug: cortex-idp-integrations-argocd-api
- baseURL: https://api.getcortexapp.com/api/v1
  baseurl_source: declared
  description: The [Integrations] AWS API from Cortex — 6 operation(s) for [integrations] aws.
  name: Cortex [Integrations] AWS API
  slug: cortex-idp-integrations-aws-api
- baseURL: https://api.getcortexapp.com/api/v1
  baseurl_source: declared
  description: The [Integrations] Azure Active Directory API from Cortex — 4 operation(s) for [integrations] azure active directory.
  name: Cortex [Integrations] Azure Active Directory API
  slug: cortex-idp-integrations-azure-active-directory-api
- baseURL: https://api.getcortexapp.com/api/v1
  baseurl_source: declared
  description: The [Integrations] Azure Devops API from Cortex — 6 operation(s) for [integrations] azure devops.
  name: Cortex [Integrations] Azure Devops API
  slug: cortex-idp-integrations-azure-devops-api
- baseURL: https://api.getcortexapp.com/api/v1
  baseurl_source: declared
  description: The [Integrations] Azure Resources API from Cortex — 7 operation(s) for [integrations] azure resources.
  name: Cortex [Integrations] Azure Resources API
  slug: cortex-idp-integrations-azure-resources-api
- baseURL: https://api.getcortexapp.com/api/v1
  baseurl_source: declared
  description: The [Integrations] BambooHR API from Cortex — 4 operation(s) for [integrations] bamboohr.
  name: Cortex [Integrations] BambooHR API
  slug: cortex-idp-integrations-bamboohr-api
- baseURL: https://api.getcortexapp.com/api/v1
  baseurl_source: declared
  description: The [Integrations] Bitbucket API from Cortex — 6 operation(s) for [integrations] bitbucket.
  name: Cortex [Integrations] Bitbucket API
  slug: cortex-idp-integrations-bitbucket-api
- baseURL: https://api.getcortexapp.com/api/v1
  baseurl_source: declared
  description: The [Integrations] Bugsnag API from Cortex — 4 operation(s) for [integrations] bugsnag.
  name: Cortex [Integrations] Bugsnag API
  slug: cortex-idp-integrations-bugsnag-api
- baseURL: https://api.getcortexapp.com/api/v1
  baseurl_source: declared
  description: The [Integrations] Buildkite API from Cortex — 4 operation(s) for [integrations] buildkite.
  name: Cortex [Integrations] Buildkite API
  slug: cortex-idp-integrations-buildkite-api
- baseURL: https://api.getcortexapp.com/api/v1
  baseurl_source: declared
  description: The [Integrations] Checkmarx SAST API from Cortex — 4 operation(s) for [integrations] checkmarx sast.
  name: Cortex [Integrations] Checkmarx SAST API
  slug: cortex-idp-integrations-checkmarx-sast-api
- baseURL: https://api.getcortexapp.com/api/v1
  baseurl_source: declared
  description: The [Integrations] CircleCI API from Cortex — 6 operation(s) for [integrations] circleci.
  name: Cortex [Integrations] CircleCI API
  slug: cortex-idp-integrations-circleci-api
- baseURL: https://api.getcortexapp.com/api/v1
  baseurl_source: declared
  description: The [Integrations] ClickUp API from Cortex — 4 operation(s) for [integrations] clickup.
  name: Cortex [Integrations] ClickUp API
  slug: cortex-idp-integrations-clickup-api
- baseURL: https://api.getcortexapp.com/api/v1
  baseurl_source: declared
  description: The [Integrations] Codecov API from Cortex — 4 operation(s) for [integrations] codecov.
  name: Cortex [Integrations] Codecov API
  slug: cortex-idp-integrations-codecov-api
- baseURL: https://api.getcortexapp.com/api/v1
  baseurl_source: declared
  description: The [Integrations] Coralogix API from Cortex — 6 operation(s) for [integrations] coralogix.
  name: Cortex [Integrations] Coralogix API
  slug: cortex-idp-integrations-coralogix-api
- baseURL: https://api.getcortexapp.com/api/v1
  baseurl_source: declared
  description: The [Integrations] Datadog API from Cortex — 6 operation(s) for [integrations] datadog.
  name: Cortex [Integrations] Datadog API
  slug: cortex-idp-integrations-datadog-api
- baseURL: https://api.getcortexapp.com/api/v1
  baseurl_source: declared
  description: The [Integrations] Dynatrace API from Cortex — 4 operation(s) for [integrations] dynatrace.
  name: Cortex [Integrations] Dynatrace API
  slug: cortex-idp-integrations-dynatrace-api
- baseURL: https://api.getcortexapp.com/api/v1
  baseurl_source: declared
  description: The [Integrations] Firehydrant API from Cortex — 4 operation(s) for [integrations] firehydrant.
  name: Cortex [Integrations] Firehydrant API
  slug: cortex-idp-integrations-firehydrant-api
- baseURL: https://api.getcortexapp.com/api/v1
  baseurl_source: declared
  description: The [Integrations] GitHub API from Cortex — 8 operation(s) for [integrations] github.
  name: Cortex [Integrations] GitHub API
  slug: cortex-idp-integrations-github-api
- baseURL: https://api.getcortexapp.com/api/v1
  baseurl_source: declared
  description: The [Integrations] GitLab API from Cortex — 6 operation(s) for [integrations] gitlab.
  name: Cortex [Integrations] GitLab API
  slug: cortex-idp-integrations-gitlab-api
- baseURL: https://api.getcortexapp.com/api/v1
  baseurl_source: declared
  description: The [Integrations] Harness API from Cortex — 6 operation(s) for [integrations] harness.
  name: Cortex [Integrations] Harness API
  slug: cortex-idp-integrations-harness-api
- baseURL: https://api.getcortexapp.com/api/v1
  baseurl_source: declared
  description: The [Integrations] Incident.io API from Cortex — 6 operation(s) for [integrations] incident.io.
  name: Cortex [Integrations] Incident.io API
  slug: cortex-idp-integrations-incident-io-api
- baseURL: https://api.getcortexapp.com/api/v1
  baseurl_source: declared
  description: The [Integrations] Instana API from Cortex — 4 operation(s) for [integrations] instana.
  name: Cortex [Integrations] Instana API
  slug: cortex-idp-integrations-instana-api
- baseURL: https://api.getcortexapp.com/api/v1
  baseurl_source: declared
  description: The [Integrations] Jenkins API from Cortex — 6 operation(s) for [integrations] jenkins.
  name: Cortex [Integrations] Jenkins API
  slug: cortex-idp-integrations-jenkins-api
- baseURL: https://api.getcortexapp.com/api/v1
  baseurl_source: declared
  description: The [Integrations] Jira API from Cortex — 6 operation(s) for [integrations] jira.
  name: Cortex [Integrations] Jira API
  slug: cortex-idp-integrations-jira-api
- baseURL: https://api.getcortexapp.com/api/v1
  baseurl_source: declared
  description: The [Integrations] Kubernetes API from Cortex — 1 operation(s) for [integrations] kubernetes.
  name: Cortex [Integrations] Kubernetes API
  slug: cortex-idp-integrations-kubernetes-api
- baseURL: https://api.getcortexapp.com/api/v1
  baseurl_source: declared
  description: The [Integrations] LaunchDarkly API from Cortex — 6 operation(s) for [integrations] launchdarkly.
  name: Cortex [Integrations] LaunchDarkly API
  slug: cortex-idp-integrations-launchdarkly-api
- baseURL: https://api.getcortexapp.com/api/v1
  baseurl_source: declared
  description: The [Integrations] Lightstep API from Cortex — 4 operation(s) for [integrations] lightstep.
  name: Cortex [Integrations] Lightstep API
  slug: cortex-idp-integrations-lightstep-api
- baseURL: https://api.getcortexapp.com/api/v1
  baseurl_source: declared
  description: The [Integrations] Mend SAST API from Cortex — 4 operation(s) for [integrations] mend sast.
  name: Cortex [Integrations] Mend SAST API
  slug: cortex-idp-integrations-mend-sast-api
- baseURL: https://api.getcortexapp.com/api/v1
  baseurl_source: declared
  description: The [Integrations] Mend SCA API from Cortex — 4 operation(s) for [integrations] mend sca.
  name: Cortex [Integrations] Mend SCA API
  slug: cortex-idp-integrations-mend-sca-api
- baseURL: https://api.getcortexapp.com/api/v1
  baseurl_source: declared
  description: The [Integrations] New Relic API from Cortex — 6 operation(s) for [integrations] new relic.
  name: Cortex [Integrations] New Relic API
  slug: cortex-idp-integrations-new-relic-api
- baseURL: https://api.getcortexapp.com/api/v1
  baseurl_source: declared
  description: The [Integrations] Okta API from Cortex — 4 operation(s) for [integrations] okta.
  name: Cortex [Integrations] Okta API
  slug: cortex-idp-integrations-okta-api
- baseURL: https://api.getcortexapp.com/api/v1
  baseurl_source: declared
  description: The [Integrations] Opsgenie API from Cortex — 4 operation(s) for [integrations] opsgenie.
  name: Cortex [Integrations] Opsgenie API
  slug: cortex-idp-integrations-opsgenie-api
- baseURL: https://api.getcortexapp.com/api/v1
  baseurl_source: declared
  description: The [Integrations] PagerDuty API from Cortex — 4 operation(s) for [integrations] pagerduty.
  name: Cortex [Integrations] PagerDuty API
  slug: cortex-idp-integrations-pagerduty-api
- baseURL: https://api.getcortexapp.com/api/v1
  baseurl_source: declared
  description: The [Integrations] Prometheus API from Cortex — 6 operation(s) for [integrations] prometheus.
  name: Cortex [Integrations] Prometheus API
  slug: cortex-idp-integrations-prometheus-api
- baseURL: https://api.getcortexapp.com/api/v1
  baseurl_source: declared
  description: The [Integrations] Rollbar API from Cortex — 4 operation(s) for [integrations] rollbar.
  name: Cortex [Integrations] Rollbar API
  slug: cortex-idp-integrations-rollbar-api
- baseURL: https://api.getcortexapp.com/api/v1
  baseurl_source: declared
  description: The [Integrations] Rootly API from Cortex — 4 operation(s) for [integrations] rootly.
  name: Cortex [Integrations] Rootly API
  slug: cortex-idp-integrations-rootly-api
- baseURL: https://api.getcortexapp.com/api/v1
  baseurl_source: declared
  description: The [Integrations] Semgrep API from Cortex — 6 operation(s) for [integrations] semgrep.
  name: Cortex [Integrations] Semgrep API
  slug: cortex-idp-integrations-semgrep-api
- baseURL: https://api.getcortexapp.com/api/v1
  baseurl_source: declared
  description: The [Integrations] Sentry API from Cortex — 4 operation(s) for [integrations] sentry.
  name: Cortex [Integrations] Sentry API
  slug: cortex-idp-integrations-sentry-api
- baseURL: https://api.getcortexapp.com/api/v1
  baseurl_source: declared
  description: The [Integrations] ServiceNow API from Cortex — 4 operation(s) for [integrations] servicenow.
  name: Cortex [Integrations] ServiceNow API
  slug: cortex-idp-integrations-servicenow-api
- baseURL: https://api.getcortexapp.com/api/v1
  baseurl_source: declared
  description: The [Integrations] SignalFx API from Cortex — 4 operation(s) for [integrations] signalfx.
  name: Cortex [Integrations] SignalFx API
  slug: cortex-idp-integrations-signalfx-api
- baseURL: https://api.getcortexapp.com/api/v1
  baseurl_source: declared
  description: The [Integrations] Snyk API from Cortex — 4 operation(s) for [integrations] snyk.
  name: Cortex [Integrations] Snyk API
  slug: cortex-idp-integrations-snyk-api
- baseURL: https://api.getcortexapp.com/api/v1
  baseurl_source: declared
  description: The [Integrations] SonarQube API from Cortex — 6 operation(s) for [integrations] sonarqube.
  name: Cortex [Integrations] SonarQube API
  slug: cortex-idp-integrations-sonarqube-api
- baseURL: https://api.getcortexapp.com/api/v1
  baseurl_source: declared
  description: The [Integrations] SumoLogic API from Cortex — 4 operation(s) for [integrations] sumologic.
  name: Cortex [Integrations] SumoLogic API
  slug: cortex-idp-integrations-sumologic-api
- baseURL: https://api.getcortexapp.com/api/v1
  baseurl_source: declared
  description: The [Integrations] Veracode API from Cortex — 4 operation(s) for [integrations] veracode.
  name: Cortex [Integrations] Veracode API
  slug: cortex-idp-integrations-veracode-api
- baseURL: https://api.getcortexapp.com/api/v1
  baseurl_source: declared
  description: The [Integrations] VictorOps API from Cortex — 4 operation(s) for [integrations] victorops.
  name: Cortex [Integrations] VictorOps API
  slug: cortex-idp-integrations-victorops-api
- baseURL: https://api.getcortexapp.com/api/v1
  baseurl_source: declared
  description: The [Integrations] Wiz API from Cortex — 4 operation(s) for [integrations] wiz.
  name: Cortex [Integrations] Wiz API
  slug: cortex-idp-integrations-wiz-api
- baseURL: https://api.getcortexapp.com/api/v1
  baseurl_source: declared
  description: The [Integrations] Workday API from Cortex — 4 operation(s) for [integrations] workday.
  name: Cortex [Integrations] Workday API
  slug: cortex-idp-integrations-workday-api
- baseURL: https://api.getcortexapp.com/api/v1
  baseurl_source: declared
  description: The [Integrations] xMatters API from Cortex — 4 operation(s) for [integrations] xmatters.
  name: Cortex [Integrations] xMatters API
  slug: cortex-idp-integrations-xmatters-api
- baseURL: https://api.getcortexapp.com/api/v1
  baseurl_source: declared
  description: The IP Allowlist API from Cortex — 2 operation(s) for ip allowlist.
  name: Cortex IP Allowlist API
  slug: cortex-idp-ip-allowlist-api
- baseURL: https://api.getcortexapp.com/api/v1
  baseurl_source: declared
  description: The My Workspace API from Cortex — 1 operation(s) for my workspace.
  name: Cortex My Workspace API
  slug: cortex-idp-my-workspace-api
- baseURL: https://api.getcortexapp.com/api/v1
  baseurl_source: declared
  description: The Notification Logs API from Cortex — 2 operation(s) for notification logs.
  name: Cortex Notification Logs API
  slug: cortex-idp-notification-logs-api
- baseURL: https://api.getcortexapp.com/api/v1
  baseurl_source: declared
  description: The On-call API from Cortex — 2 operation(s) for on-call.
  name: Cortex On Call API
  slug: cortex-idp-on-call-api
- baseURL: https://api.getcortexapp.com/api/v1
  baseurl_source: declared
  description: The Packages API from Cortex — 18 operation(s) for packages.
  name: Cortex Packages API
  slug: cortex-idp-packages-api
- baseURL: https://api.getcortexapp.com/api/v1
  baseurl_source: declared
  description: The Plugins API from Cortex — 2 operation(s) for plugins.
  name: Cortex Plugins API
  slug: cortex-idp-plugins-api
- baseURL: https://api.getcortexapp.com/api/v1
  baseurl_source: declared
  description: The public-scim-schema-controller API from Cortex — 2 operation(s) for public-scim-schema-controller.
  name: Cortex Public SCIM Schema Controller API
  slug: cortex-idp-public-scim-schema-controller-api
- baseURL: https://api.getcortexapp.com/api/v1
  baseurl_source: declared
  description: The Queries API from Cortex — 2 operation(s) for queries.
  name: Cortex Queries API
  slug: cortex-idp-queries-api
- baseURL: https://api.getcortexapp.com/api/v1
  baseurl_source: declared
  description: The Scaffolder API from Cortex — 2 operation(s) for scaffolder.
  name: Cortex Scaffolder API
  slug: cortex-idp-scaffolder-api
- baseURL: https://api.getcortexapp.com/api/v1
  baseurl_source: declared
  description: The SCIM API from Cortex — 2 operation(s) for scim.
  name: Cortex SCIM API
  slug: cortex-idp-scim-api
- baseURL: https://api.getcortexapp.com/api/v1
  baseurl_source: declared
  description: The Secrets API from Cortex — 2 operation(s) for secrets.
  name: Cortex Secrets API
  slug: cortex-idp-secrets-api
- baseURL: https://api.getcortexapp.com/api/v1
  baseurl_source: declared
  description: The Team Roles API from Cortex — 1 operation(s) for team roles.
  name: Cortex Team Roles API
  slug: cortex-idp-team-roles-api
- baseURL: https://api.getcortexapp.com/api/v1
  baseurl_source: declared
  description: The Teams [Advanced] API from Cortex — 2 operation(s) for teams [advanced].
  name: Cortex Teams [Advanced] API
  slug: cortex-idp-teams-advanced-api
- baseURL: https://api.getcortexapp.com/api/v1
  baseurl_source: declared
  description: The Teams API from Cortex — 5 operation(s) for teams.
  name: Cortex Teams API
  slug: cortex-idp-teams-api
- baseURL: https://api.getcortexapp.com/api/v1
  baseurl_source: declared
  description: The Teams [Departments] (legacy) API from Cortex — 1 operation(s) for teams [departments] (legacy).
  name: Cortex Teams [Departments] (legacy) API
  slug: cortex-idp-teams-departments-legacy-api
- baseURL: https://api.getcortexapp.com/api/v1
  baseurl_source: declared
  description: The Teams Hierarchies API from Cortex — 1 operation(s) for teams hierarchies.
  name: Cortex Teams Hierarchies API
  slug: cortex-idp-teams-hierarchies-api
- baseURL: https://api.getcortexapp.com/api/v1
  baseurl_source: declared
  description: The Users API from Cortex — 2 operation(s) for users.
  name: Cortex Users API
  slug: cortex-idp-users-api
- baseURL: https://api.getcortexapp.com/api/v1
  baseurl_source: declared
  description: The Verifications API from Cortex — 3 operation(s) for verifications.
  name: Cortex Verifications API
  slug: cortex-idp-verifications-api
- baseURL: https://api.getcortexapp.com/api/v1
  baseurl_source: declared
  description: The Workflows API from Cortex — 7 operation(s) for workflows.
  name: Cortex Workflows API
  slug: cortex-idp-workflows-api
artifact_total: 111
collections:
- collection_type: open
  name: Cortex REST Catalog API
  slug: open-cortex-idp-catalog-api
- collection_type: open
  name: Cortex REST Catalog Custom Data API
  slug: open-cortex-idp-custom-data-api
- collection_type: open
  name: Cortex REST Catalog Deploys API
  slug: open-cortex-idp-deploys-api
- collection_type: open
  name: Cortex REST Catalog Initiatives API
  slug: open-cortex-idp-initiatives-api
- collection_type: open
  name: Cortex REST Catalog Integrations API
  slug: open-cortex-idp-integrations-api
- collection_type: open
  name: Cortex REST Catalog Scorecards API
  slug: open-cortex-idp-scorecards-api
- collection_type: open
  name: Cortex REST API
  slug: open-cortex-idp
common:
- group: company
  title: ''
  type: Blog
  url: https://www.cortex.io/blog
- group: other
  href: https://artifacts.apis.io/cortex-idp/capabilities/cortex-idp-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/cortex-idp-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/cortex-idp/agentic-access/cortex-idp-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/cortex-idp-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/cortex-idp/authentication/cortex-idp-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cortex-idp-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cortexapp
- group: company
  title: ''
  type: Website
  url: https://www.cortex.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cortex.io
- group: commercial
  href: https://artifacts.apis.io/cortex-idp/plans/cortex-idp-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cortex-idp-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/cortex-idp/rate-limits/cortex-idp-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/cortex-idp-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/cortex-idp/finops/cortex-idp-finops.yml
  title: ''
  type: FinOps
  url: finops/cortex-idp-finops.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://www.cortex.io/pricing
created: '2026-07-11'
description: Cortex (cortex.io) is an internal developer portal (IDP) and software catalog platform. It gives engineering organizations a catalog of services and entities, Scorecards that measure those entities against production-readiness and reliability standards, Initiatives for driving improvement campaigns, and roughly thirty integrations (GitHub, PagerDuty, Datadog, Kubernetes, and more) that hydrate the catalog. Cortex exposes a documented REST API (base https://api.getcortexapp.com/api/v1) with Bearer/API-key authentication covering the Catalog/Entities, Scorecards, Custom Data, Initiatives, Deploys, Teams, and Integrations. NOTE - this is Cortex.io the internal developer portal / service catalog & scorecards company, NOT Cortex XSOAR (Palo Alto Networks), NOT the Cortex crypto token, and NOT Orange Logic's Cortex DAM.
finops:
- has_sources: true
  method: generated
  name: Cortex Idp Finops
  primary_unit: ''
  service_category: Developer Tools and Platform Engineering
  slug: cortex-idp-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cortex-idp.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.cortex.io over HTTP.
  name: Cortex MCP Server
  slug: cortex-idp
modified: '2026-10-06'
name: Cortex
nav: Providers
network: true
overview: 'Cortex publishes 97 API contracts indexed on the [APIs.io](https://apis.io/) network, including Custom Data API, Deploys API, Initiatives API, and 94 more. Tagged areas include Software Catalog, Internal Developer Portal, Service Catalog, Developer Experience, and Scorecards.


  The Cortex catalog on APIs.io includes 1 Spectral governance ruleset.


  Cortex''s developer surface includes engineering blog, authentication, documentation, pricing, and 7 more developer resources.'
plans:
- name: Cortex Idp Plans Pricing
  plan_count: 3
  slug: cortex-idp-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 2
  name: Cortex Idp Rate Limits
  slug: cortex-idp-rate-limits
rules:
- authorship: generated
  effective_rule_count: 96
  extends:
  - spectral:oas
  name: Cortex API Rules
  rule_count: 55
  severity_counts:
    error: 43
    hint: 0
    info: 2
    warn: 10
  slug: cortex-idp-rules
score:
  band: thin
  composite: 34.1
  coverage:
    artifact_dirs: 16
    catalog_earned: 46.5
    catalog_earned_first_party: 0.0
    catalog_gap: 68.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.2
  facets:
    access_clarity: 18.4
    contract_governance: 13.6
    contract_quality: 54.4
    developer_ergonomics: 32.1
    discoverability: 68.3
    operational_transparency: 5.3
  previous_composite: 32.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 93.1
      total: 101
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 33.3
screenshot: https://apis.io/screenshots/cortex-idp/cortex-idp-2026-07-25T210650.png
security:
- kind: authentication
  name: Cortex Idp Authentication
  slug: cortex-idp-authentication
  summary_line: http · 1 scheme
slug: cortex-idp
tags:
- Software Catalog
- Internal Developer Portal
- Service Catalog
- Developer Experience
- Scorecards
- Platform Engineering
- Developer Portal
- Developer Tools
website: https://www.cortex.io
---
