---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.1
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 68
  human_in_the_loop: 1
  name: Overops Agentic Access
  operation_count: 137
  slug: overops-agentic-access
  summary_line: 137 operations · 68 acting · 1 human-in-the-loop
api_count: 16
apis:
- description: Fetch and manipulate alerting rules for detecting and disseminating anomalies such as introduction of new events and regressions to different communication channels (e.g. Email, Jira, Slack, Uder defi
  name: Overops Alerts API
  slug: overops-alerts-api
- description: Fetch and manipulate grouping of views into logical categories (e.g "CI/CD", "Favorites")
  name: Overops Categories API
  slug: overops-categories-api
- description: Fetch and manipulate code filters to include / exclude 3rd party and utility classes from OverOps analysis and data capture.
  name: Overops Code Redaction API
  slug: overops-code-redaction-api
- description: Fetch and manipulate data redaction of PII with target environments.
  name: Overops Data Redaction API
  slug: overops-data-redaction-api
- description: The Entry Points API from Overops — 11 operation(s) for entry points.
  name: Overops Entry Points API
  slug: overops-entry-points-api
- description: Fetch monitoring status and control OverOps Agents and Collectors
  name: Overops Environment Management API
  slug: overops-environment-management-api
- description: Fetch and manipulate OverOps Automated Root Cause Events and Snapshots
  name: Overops Events API
  slug: overops-events-api
- description: Fetch general information about provisioned OverOps enviroments
  name: Overops General API
  slug: overops-general-api
- description: Fetch and manipulate events labels
  name: Overops Labels API
  slug: overops-labels-api
- description: Fetch and manipulate dynamic data exported to StatsD, which enables using a variety of third-party tools, providing control over application data from OverOps.
  name: Overops Publish Metrics API
  slug: overops-publish-metrics-api
- description: Fetch system metrics
  name: Overops System Metrics API
  slug: overops-system-metrics-api
- description: APIs related to team management of a service
  name: Overops Team Management API
  slug: overops-team-management-api
- description: Fetch and manipulate OverOps Timers - bottleneck detection and performance diagnosis
  name: Overops Timers API
  slug: overops-timers-api
- description: Fetch and manipulate User Defined Functinos - OverOps extensions using Lambdas.
  name: Overops UDFs API
  slug: overops-udfs-api
- description: Fetch volumetric time series data about observed code events within OverOps monitored applications filtered by server cluster, application and deployments.
  name: Overops View Metrics API
  slug: overops-view-metrics-api
- description: Fetch and manipulate grouping of events (i.e. Views) according to attribute sets (e.g. "uncaught exceptions", "errors from package com.acme")
  name: Overops Views API
  slug: overops-views-api
artifact_total: 20
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/overops-services-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/overops-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/overops-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/overops-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/overops-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/overops-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/overops-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/overops-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/overops-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/overops-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/overops-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/overops-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/overops-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/overops-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/overops-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://doc.overops.com
- group: docs
  title: ''
  type: Documentation
  url: https://doc.overops.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://doc.overops.com/reference
- group: operate
  title: ''
  type: ChangeLog
  url: https://doc.overops.com/docs/whats-new
- group: operate
  title: ''
  type: Support
  url: https://support.overops.com/hc/en-us
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/overops
- group: start
  title: ''
  type: Login
  url: https://app.overops.com
created: '2026-07-17'
description: OverOps (formerly Takipi) is a continuous reliability platform that helps teams who ship software ensure rapid code changes do not degrade the customer experience. It runs in the cloud or on-premises, instruments Java and .NET applications with a micro-agent, and automatically identifies, prevents, and resolves critical software issues across CI/CD, testing, and production. OverOps captures true root-cause code snapshots (stack, source, and variable state) at the moment of failure and exposes everything through a REST API that lets admins and users automate every action available in the OverOps UI. OverOps was acquired by Harness; overops.com now redirects to harness.io, while the developer API, documentation, and application hosts remain live.
image: https://files.readme.io/dd13086-small-Logo_white.png
layout: provider
mcp_servers:
- description: ''
  name: overops-mcp.yml
  slug: overops-mcpyml
modified: '2026-07-20'
name: Overops
nav: Providers
network: true
overview: 'Overops publishes 16 APIs on the [APIs.io](https://apis.io/) network, including Alerts API, Categories API, Code Redaction API, and 13 more. Tagged areas include Company, Observability, Reliability, Error Monitoring, and Application Performance.


  Overops'' developer surface includes authentication, changelog, documentation, API reference, support, and 18 more developer resources.'
random_paper: 62
score:
  band: thin
  composite: 39.5
  delta: 0.0
  facets:
    commercial_clarity: 13.2
    contract_quality: 58.9
    developer_ergonomics: 49.5
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 21.1
  previous_composite: 39.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 16
    mcp: derived
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/overops/refs/heads/main/screenshots/overops-2026-08-07T191135.png
security:
- kind: authentication
  name: Overops Authentication
  slug: overops-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Overops Domain Security
  slug: overops-domain-security
  summary_line: TLSv1.2 · DMARC
slug: overops
tags:
- Company
- Observability
- Reliability
- Error Monitoring
- Application Performance
- Java
- DevOps
- Code Quality
website: https://doc.overops.com
---
