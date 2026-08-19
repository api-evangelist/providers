---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 173
  human_in_the_loop: 32
  name: Gremlin Agentic Access
  operation_count: 379
  slug: gremlin-agentic-access
  summary_line: 379 operations · 173 acting · 32 human-in-the-loop
api_count: 55
apis:
- description: List and modify all infrastructure and failure flag agents
  name: Gremlin agents API
  slug: gremlin-agents-api
- description: Create, delete, activate, deactivate and list apikeys
  name: Gremlin apikeys API
  slug: gremlin-apikeys-api
- description: Create, halt, and list attacks
  name: Gremlin attacks API
  slug: gremlin-attacks-api
- description: Get metadata about the AWS IAM role creation for health checks
  name: Gremlin aws.metadata API
  slug: gremlin-aws-metadata-api
- description: List and modify all clients
  name: Gremlin clients API
  slug: gremlin-clients-api
- description: Update company preferences, get all users or clients for a company, and get company details
  name: Gremlin companies API
  slug: gremlin-companies-api
- description: Get all active containers
  name: Gremlin containers API
  slug: gremlin-containers-api
- description: Read Datadog items
  name: Gremlin datadog API
  slug: gremlin-datadog-api
- description: Get and list disaster recovery test reports
  name: Gremlin disaster-recovery-test-reports API
  slug: gremlin-disaster-recovery-test-reports-api
- description: Create, get, list, run, and complete disaster recovery tests
  name: Gremlin disaster-recovery-tests API
  slug: gremlin-disaster-recovery-tests-api
- description: The executions API from Gremlin — 1 operation(s) for executions.
  name: Gremlin executions API
  slug: gremlin-executions-api
- description: Used for managing authentication for Status Checks and Load Generators
  name: Gremlin external-integrations API
  slug: gremlin-external-integrations-api
- description: Get, list, and protect applications
  name: Gremlin failure-flags.apps API
  slug: gremlin-failure-flags-apps-api
- description: Get, list, and protect experiments
  name: Gremlin failure-flags.experiments API
  slug: gremlin-failure-flags-experiments-api
- description: Get, list, and protect failure flags
  name: Gremlin failure-flags.flags API
  slug: gremlin-failure-flags-flags-api
- description: Create, update and run GameDays
  name: Gremlin gamedays API
  slug: gremlin-gamedays-api
- description: Fetch setup instructions for configuring a Google Cloud integration.
  name: Gremlin google-cloud.integration API
  slug: gremlin-google-cloud-integration-api
- description: List resources Gremlin has discovered through a configured integration.
  name: Gremlin google-cloud.integration.resources API
  slug: gremlin-google-cloud-integration-resources-api
- description: Get Grafana alerts
  name: Gremlin grafana API
  slug: gremlin-grafana-api
- description: Halt impacts across the Gremlin platform
  name: Gremlin halts API
  slug: gremlin-halts-api
- description: Create, read, update, delete health checks as well as test health check endpoint and evaluation configuration
  name: Gremlin health checks API
  slug: gremlin-health-checks-api
- description: Manage images for different entities
  name: Gremlin images API
  slug: gremlin-images-api
- description: Handle client integrations
  name: Gremlin integration-clients API
  slug: gremlin-integration-clients-api
- description: Used for interacting with the Private Network Integration
  name: Gremlin integration-invocations API
  slug: gremlin-integration-invocations-api
- description: Create, read Jira tickets
  name: Gremlin jira API
  slug: gremlin-jira-api
- description: Create, halt, and list Kubernetes attacks
  name: Gremlin kubernetes.attacks API
  slug: gremlin-kubernetes-attacks-api
- description: Get information on attackable kubernetes targets
  name: Gremlin kubernetes.targets API
  slug: gremlin-kubernetes-targets-api
- description: Create, read, update, and delete LoadGenerators
  name: Gremlin load-generators API
  slug: gremlin-load-generators-api
- description: Get metadata about the Gremlin commands.
  name: Gremlin metadata API
  slug: gremlin-metadata-api
- description: Metrics for charting purposes
  name: Gremlin metrics API
  slug: gremlin-metrics-api
- description: Read New Relic items
  name: Gremlin newrelic API
  slug: gremlin-newrelic-api
- description: Manage company level integrations with Slack/Datadog
  name: Gremlin Notification Integrations API
  slug: gremlin-notification-integrations-api
- description: View and modify a team's notification settings
  name: Gremlin notification-settings API
  slug: gremlin-notification-settings-api
- description: OAuth callback endpoints
  name: Gremlin oauth API
  slug: gremlin-oauth-api
- description: Get and update org preferences. Generate new and delete old client certificates
  name: Gremlin orgs API
  slug: gremlin-orgs-api
- description: Get Pagerduty services and incidents
  name: Gremlin pagerduty API
  slug: gremlin-pagerduty-api
- description: Get a list of supported infrastructure providers and supported services by provider
  name: Gremlin providers API
  slug: gremlin-providers-api
- description: API to access resources for reliability management
  name: Gremlin reliability-management API
  slug: gremlin-reliability-management-api
- description: Retrieve reliability report for a given service
  name: Gremlin reliability-report API
  slug: gremlin-reliability-report-api
- description: Get and run reliability tests
  name: Gremlin reliability-tests API
  slug: gremlin-reliability-tests-api
- description: Get users, clients, and attacks summaries
  name: Gremlin reports API
  slug: gremlin-reports-api
- description: Endpoints for receiving access and event logs
  name: Gremlin reports.security API
  slug: gremlin-reports-security-api
- description: List and modify roles
  name: Gremlin roles API
  slug: gremlin-roles-api
- description: Create, update, run, halt, and list scenarios
  name: Gremlin scenarios API
  slug: gremlin-scenarios-api
- description: Get/List recommended scenarios
  name: Gremlin scenarios.recommended API
  slug: gremlin-scenarios-recommended-api
- description: Get, create, and delete schedules
  name: Gremlin schedules API
  slug: gremlin-schedules-api
- description: Overview of a service, including all activity that impacts a service
  name: Gremlin service-overview API
  slug: gremlin-service-overview-api
- description: Get metrics about intelligent health check target for a service
  name: Gremlin services API
  slug: gremlin-services-api
- description: Used for sharing agent assets (eg. K8s Namespaces) between teams
  name: Gremlin sharedAssets API
  slug: gremlin-sharedassets-api
- description: Create, Retrieve, Update, and Delete endpoints for Teams
  name: Gremlin teams API
  slug: gremlin-teams-api
- description: Create custom test suites
  name: Gremlin test-suites API
  slug: gremlin-test-suites-api
- description: Get users (all or active) and activate, deactivate, update, and invite users.
  name: Gremlin users API
  slug: gremlin-users-api
- description: Endpoints for non-MFA user auth
  name: Gremlin users.auth API
  slug: gremlin-users-auth-api
- description: Endpoints for multi-factor user auth (MFA) and for managing MFA providers and secrets
  name: Gremlin users.auth.mfa API
  slug: gremlin-users-auth-mfa-api
- description: Create, read, update, and delete webhooks
  name: Gremlin webhooks API
  slug: gremlin-webhooks-api
artifact_total: 120
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Gremlin agents API
  slug: open-gremlin-agents-api
- collection_type: open
  name: Gremlin agents apikeys API
  slug: open-gremlin-apikeys-api
- collection_type: open
  name: Gremlin agents attacks API
  slug: open-gremlin-attacks-api
- collection_type: open
  name: Gremlin agents aws.metadata API
  slug: open-gremlin-aws-metadata-api
- collection_type: open
  name: Gremlin agents clients API
  slug: open-gremlin-clients-api
- collection_type: open
  name: Gremlin agents companies API
  slug: open-gremlin-companies-api
- collection_type: open
  name: Gremlin agents containers API
  slug: open-gremlin-containers-api
- collection_type: open
  name: Gremlin agents datadog API
  slug: open-gremlin-datadog-api
- collection_type: open
  name: Gremlin agents disaster-recovery-test-reports API
  slug: open-gremlin-disaster-recovery-test-reports-api
- collection_type: open
  name: Gremlin agents disaster-recovery-tests API
  slug: open-gremlin-disaster-recovery-tests-api
- collection_type: open
  name: Gremlin agents executions API
  slug: open-gremlin-executions-api
- collection_type: open
  name: Gremlin agents external-integrations API
  slug: open-gremlin-external-integrations-api
- collection_type: open
  name: Gremlin agents failure-flags.apps API
  slug: open-gremlin-failure-flags-apps-api
- collection_type: open
  name: Gremlin agents failure-flags.experiments API
  slug: open-gremlin-failure-flags-experiments-api
- collection_type: open
  name: Gremlin agents failure-flags.flags API
  slug: open-gremlin-failure-flags-flags-api
- collection_type: open
  name: Gremlin agents gamedays API
  slug: open-gremlin-gamedays-api
- collection_type: open
  name: Gremlin agents google-cloud.integration API
  slug: open-gremlin-google-cloud-integration-api
- collection_type: open
  name: Gremlin agents google-cloud.integration.resources API
  slug: open-gremlin-google-cloud-integration-resources-api
- collection_type: open
  name: Gremlin agents grafana API
  slug: open-gremlin-grafana-api
- collection_type: open
  name: Gremlin agents halts API
  slug: open-gremlin-halts-api
- collection_type: open
  name: Gremlin agents health checks API
  slug: open-gremlin-health-checks-api
- collection_type: open
  name: Gremlin agents images API
  slug: open-gremlin-images-api
- collection_type: open
  name: Gremlin agents integration-clients API
  slug: open-gremlin-integration-clients-api
- collection_type: open
  name: Gremlin agents integration-invocations API
  slug: open-gremlin-integration-invocations-api
- collection_type: open
  name: Gremlin agents jira API
  slug: open-gremlin-jira-api
- collection_type: open
  name: Gremlin agents kubernetes.attacks API
  slug: open-gremlin-kubernetes-attacks-api
- collection_type: open
  name: Gremlin agents kubernetes.targets API
  slug: open-gremlin-kubernetes-targets-api
- collection_type: open
  name: Gremlin agents load-generators API
  slug: open-gremlin-load-generators-api
- collection_type: open
  name: Gremlin agents metadata API
  slug: open-gremlin-metadata-api
- collection_type: open
  name: Gremlin agents metrics API
  slug: open-gremlin-metrics-api
- collection_type: open
  name: Gremlin agents newrelic API
  slug: open-gremlin-newrelic-api
- collection_type: open
  name: Gremlin agents Notification Integrations API
  slug: open-gremlin-notification-integrations-api
- collection_type: open
  name: Gremlin agents notification-settings API
  slug: open-gremlin-notification-settings-api
- collection_type: open
  name: Gremlin agents oauth API
  slug: open-gremlin-oauth-api
- collection_type: open
  name: Gremlin agents orgs API
  slug: open-gremlin-orgs-api
- collection_type: open
  name: Gremlin agents pagerduty API
  slug: open-gremlin-pagerduty-api
- collection_type: open
  name: Gremlin agents providers API
  slug: open-gremlin-providers-api
- collection_type: open
  name: Gremlin agents reliability-management API
  slug: open-gremlin-reliability-management-api
- collection_type: open
  name: Gremlin agents reliability-report API
  slug: open-gremlin-reliability-report-api
- collection_type: open
  name: Gremlin agents reliability-tests API
  slug: open-gremlin-reliability-tests-api
- collection_type: open
  name: Gremlin agents reports API
  slug: open-gremlin-reports-api
- collection_type: open
  name: Gremlin agents reports.security API
  slug: open-gremlin-reports-security-api
- collection_type: open
  name: Gremlin agents roles API
  slug: open-gremlin-roles-api
- collection_type: open
  name: Gremlin agents scenarios API
  slug: open-gremlin-scenarios-api
- collection_type: open
  name: Gremlin agents scenarios.recommended API
  slug: open-gremlin-scenarios-recommended-api
- collection_type: open
  name: Gremlin agents schedules API
  slug: open-gremlin-schedules-api
- collection_type: open
  name: Gremlin agents service-overview API
  slug: open-gremlin-service-overview-api
- collection_type: open
  name: Gremlin agents services API
  slug: open-gremlin-services-api
- collection_type: open
  name: Gremlin agents sharedAssets API
  slug: open-gremlin-sharedassets-api
- collection_type: open
  name: Gremlin agents teams API
  slug: open-gremlin-teams-api
- collection_type: open
  name: Gremlin agents test-suites API
  slug: open-gremlin-test-suites-api
- collection_type: open
  name: Gremlin agents users API
  slug: open-gremlin-users-api
- collection_type: open
  name: Gremlin agents users.auth API
  slug: open-gremlin-users-auth-api
- collection_type: open
  name: Gremlin agents users.auth.mfa API
  slug: open-gremlin-users-auth-mfa-api
- collection_type: open
  name: Gremlin agents webhooks API
  slug: open-gremlin-webhooks-api
- collection_type: open
  name: Gremlin API
  slug: open-gremlin
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/gremlin-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/gremlin-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/gremlin-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gremlin-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/gremlin
- group: start
  title: ''
  type: Portal
  url: https://www.gremlin.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.gremlin.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://www.gremlin.com/docs/getting-started
- group: auth
  title: ''
  type: Authentication
  url: https://www.gremlin.com/docs/api-reference
- group: commercial
  title: ''
  type: Pricing
  url: https://www.gremlin.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.gremlin.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.gremlin.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://www.gremlin.com/support
- group: agent
  title: ''
  type: LlmsText
  url: https://www.gremlin.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.gremlin.com/blog
created: '2025-01-01'
description: Gremlin is a chaos engineering platform that helps teams build more resilient systems by running controlled failure experiments. It provides tools to simulate infrastructure failures, network issues, and resource exhaustion to identify and fix weaknesses before they cause real outages.
finops:
- name: Gremlin Finops
  service_category: API
  slug: gremlin-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gremlin.png
layout: provider
modified: '2026-05-19'
name: Gremlin
nav: Providers
network: true
overview: 'Gremlin publishes 55 APIs on the [APIs.io](https://apis.io/) network, including agents API, apikeys API, attacks API, and 52 more. Tagged areas include Chaos Engineering, Fault Injection, Infrastructure Testing, Reliability, and Site Reliability Engineering.


  The Gremlin catalog on APIs.io includes 1 Spectral governance ruleset.


  Gremlin''s developer surface includes developer portal, documentation, getting-started guide, authentication, pricing, support, engineering blog, and 8 more developer resources.'
plans:
- name: Gremlin Plans Pricing
  plan_count: 3
  slug: gremlin-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 5
  name: Gremlin Rate Limits
  slug: gremlin-rate-limits
rules:
- effective_rule_count: 4
  extends: []
  name: Gremlin API Rules
  rule_count: 4
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 3
  slug: gremlin-rules
score:
  band: developing
  composite: 46.4
  delta: -1.7
  facets:
    access_clarity: 55.3
    commercial_clarity: 55.3
    contract_governance: 30.3
    contract_quality: 59.1
    developer_ergonomics: 33.3
    discoverability: 88.9
    governance: 30.3
    operational_transparency: 10.5
  previous_composite: 48.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 55
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gremlin/refs/heads/main/screenshots/gremlin-2026-06-20T182400.png
security:
- kind: domain-security
  name: Gremlin Domain Security
  slug: gremlin-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Gremlin Vulnerability Disclosure
  slug: gremlin-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Gremlin Trust Center
  slug: gremlin-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, GDPR
slug: gremlin
tags:
- Chaos Engineering
- Fault Injection
- Infrastructure Testing
- Reliability
- Site Reliability Engineering
website: https://www.gremlin.com
---
