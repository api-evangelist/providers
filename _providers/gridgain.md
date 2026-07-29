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
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 59
  human_in_the_loop: 15
  name: Gridgain Agentic Access
  operation_count: 117
  slug: gridgain-agentic-access
  summary_line: 117 operations · 59 acting · 15 human-in-the-loop
api_count: 26
apis:
- description: Legacy GridGain 8 / Apache Ignite REST API for cache operations, SQL and scan queries, cluster activation, and node management over HTTP.
  name: GridGain REST API
  slug: gridgain-rest-api
- description: The authentication API from GridGain — 3 operation(s) for authentication.
  name: GridGain authentication API
  slug: gridgain-authentication-api
- description: The cdcManagement API from GridGain — 9 operation(s) for cdcmanagement.
  name: GridGain cdcManagement API
  slug: gridgain-cdcmanagement-api
- description: The clusterConfiguration API from GridGain — 2 operation(s) for clusterconfiguration.
  name: GridGain clusterConfiguration API
  slug: gridgain-clusterconfiguration-api
- description: The clusterManagement API from GridGain — 3 operation(s) for clustermanagement.
  name: GridGain clusterManagement API
  slug: gridgain-clustermanagement-api
- description: The clusterMetric API from GridGain — 3 operation(s) for clustermetric.
  name: GridGain clusterMetric API
  slug: gridgain-clustermetric-api
- description: The compute API from GridGain — 3 operation(s) for compute.
  name: GridGain compute API
  slug: gridgain-compute-api
- description: The dataNodes API from GridGain — 3 operation(s) for datanodes.
  name: GridGain dataNodes API
  slug: gridgain-datanodes-api
- description: The dcr API from GridGain — 6 operation(s) for dcr.
  name: GridGain dcr API
  slug: gridgain-dcr-api
- description: The deployment API from GridGain — 7 operation(s) for deployment.
  name: GridGain deployment API
  slug: gridgain-deployment-api
- description: The distribution API from GridGain — 1 operation(s) for distribution.
  name: GridGain distribution API
  slug: gridgain-distribution-api
- description: The licenseManagement API from GridGain — 6 operation(s) for licensemanagement.
  name: GridGain licenseManagement API
  slug: gridgain-licensemanagement-api
- description: The nodeConfiguration API from GridGain — 2 operation(s) for nodeconfiguration.
  name: GridGain nodeConfiguration API
  slug: gridgain-nodeconfiguration-api
- description: The nodeManagement API from GridGain — 3 operation(s) for nodemanagement.
  name: GridGain nodeManagement API
  slug: gridgain-nodemanagement-api
- description: The nodeMetric API from GridGain — 4 operation(s) for nodemetric.
  name: GridGain nodeMetric API
  slug: gridgain-nodemetric-api
- description: The privilegesGrants API from GridGain — 3 operation(s) for privilegesgrants.
  name: GridGain privilegesGrants API
  slug: gridgain-privilegesgrants-api
- description: The recovery API from GridGain — 9 operation(s) for recovery.
  name: GridGain recovery API
  slug: gridgain-recovery-api
- description: The roleAssignments API from GridGain — 5 operation(s) for roleassignments.
  name: GridGain roleAssignments API
  slug: gridgain-roleassignments-api
- description: The roleManagement API from GridGain — 2 operation(s) for rolemanagement.
  name: GridGain roleManagement API
  slug: gridgain-rolemanagement-api
- description: The snapshotManagement API from GridGain — 6 operation(s) for snapshotmanagement.
  name: GridGain snapshotManagement API
  slug: gridgain-snapshotmanagement-api
- description: The sql API from GridGain — 3 operation(s) for sql.
  name: GridGain sql API
  slug: gridgain-sql-api
- description: The system API from GridGain — 2 operation(s) for system.
  name: GridGain system API
  slug: gridgain-system-api
- description: The topology API from GridGain — 2 operation(s) for topology.
  name: GridGain topology API
  slug: gridgain-topology-api
- description: The transactions API from GridGain — 2 operation(s) for transactions.
  name: GridGain transactions API
  slug: gridgain-transactions-api
- description: The upgrade API from GridGain — 4 operation(s) for upgrade.
  name: GridGain upgrade API
  slug: gridgain-upgrade-api
- description: The userManagement API from GridGain — 2 operation(s) for usermanagement.
  name: GridGain userManagement API
  slug: gridgain-usermanagement-api
artifact_total: 34
collections:
- collection_type: open
  name: GridGain REST module
  slug: open-gridgain
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/gridgain-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gridgain-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/gridgain-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/gridgain-systems
- group: company
  title: ''
  type: Website
  url: https://www.gridgain.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.gridgain.com/docs/latest/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.gridgain.com/docs/latest/getting-started/quick-start/java
- group: operate
  title: ''
  type: Support
  url: https://www.gridgain.com/support
- group: company
  title: ''
  type: Blog
  url: https://www.gridgain.com/resources/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/gridgain
created: '2025-08-19'
description: GridGain is a unified real-time data platform that provides in-memory computing for transactions, analytics, and AI workloads. Built on top of Apache Ignite, it offers distributed database, caching, and computing capabilities for high-performance data-intensive applications.
finops:
- name: Gridgain Finops
  service_category: API
  slug: gridgain-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gridgain.png
layout: provider
modified: '2026-05-19'
name: GridGain
nav: Providers
network: true
overview: 'GridGain publishes 25 APIs on the [APIs.io](https://apis.io/) network, including authentication API, cdcManagement API, clusterConfiguration API, and 22 more. Tagged areas include Caching, Data Grid, Distributed Database, In-Memory Computing, and Real-Time.


  The GridGain catalog on APIs.io includes 1 Spectral governance ruleset.


  GridGain''s developer surface includes authentication, documentation, getting-started guide, support, engineering blog, and 5 more developer resources.'
plans:
- name: Gridgain Plans Pricing
  plan_count: 3
  slug: gridgain-plans-pricing
random_paper: 67
rate_limits:
- limit_count: 5
  name: Gridgain Rate Limits
  slug: gridgain-rate-limits
rules:
- name: GridGain API Rules
  rule_count: 3
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 1
  slug: gridgain-rules
score:
  band: developing
  composite: 42.5
  delta: -3.6
  facets:
    commercial_clarity: 39.5
    contract_quality: 53.9
    developer_ergonomics: 37.0
    discoverability: 64.8
    governance: 20.8
    operational_transparency: 36.8
  previous_composite: 46.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 25
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gridgain/refs/heads/main/screenshots/gridgain-2026-06-20T182404.png
security:
- kind: authentication
  name: Gridgain Authentication
  slug: gridgain-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Gridgain Domain Security
  slug: gridgain-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: gridgain
tags:
- Caching
- Data Grid
- Distributed Database
- In-Memory Computing
- Real-Time
website: https://www.gridgain.com/
---
