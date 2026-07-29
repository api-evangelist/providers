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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Dolthub Agentic Access
  operation_count: 18
  slug: dolthub-agentic-access
  summary_line: 18 operations · 8 acting
api_count: 8
apis:
- description: The open-source Dolt database ships a MySQL-compatible SQL server (dolt sql-server) over the MySQL wire protocol, giving the same versioned database hosted on DoltHub a self-hostable, drop-in SQL inte
  name: Dolt SQL Server
  slug: dolt-sql-server
- description: The Branches API from DoltHub — 1 operation(s) for branches.
  name: DoltHub Branches API
  slug: dolthub-branches-api
- description: The Databases API from DoltHub — 3 operation(s) for databases.
  name: DoltHub Databases API
  slug: dolthub-databases-api
- description: The Jobs API from DoltHub — 1 operation(s) for jobs.
  name: DoltHub Jobs API
  slug: dolthub-jobs-api
- description: The Operations API from DoltHub — 1 operation(s) for operations.
  name: DoltHub Operations API
  slug: dolthub-operations-api
- description: The Pull Requests API from DoltHub — 3 operation(s) for pull requests.
  name: DoltHub Pull Requests API
  slug: dolthub-pull-requests-api
- description: The SQL API from DoltHub — 4 operation(s) for sql.
  name: DoltHub SQL API
  slug: dolthub-sql-api
- description: The Tags API from DoltHub — 1 operation(s) for tags.
  name: DoltHub Tags API
  slug: dolthub-tags-api
artifact_total: 15
collections:
- collection_type: open
  name: DoltHub API
  slug: open-dolthub
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/dolthub-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dolthub-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/dolthub-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dolthub
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/dolthub
- group: company
  title: ''
  type: Website
  url: https://www.dolthub.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.dolthub.com
- group: commercial
  title: ''
  type: Plans
  url: plans/dolthub-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dolthub-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/dolthub-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.dolthub.com/blog/rss.xml
created: '2026-06-20'
description: DoltHub is the hosting platform for Dolt, the version-controlled SQL database - "Git for data". DoltHub hosts public and private Dolt databases and exposes an HTTP API (the DoltHub SQL API) for running read and write SQL queries against any branch, plus repository, branch, tag, fork, and asynchronous job/operation management over a Git-style version-controlled MySQL-compatible database.
finops:
- name: Dolthub Finops
  service_category: Databases
  slug: dolthub-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dolthub.png
layout: provider
modified: '2026-06-20'
name: DoltHub
nav: Providers
network: true
overview: 'DoltHub publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Branches API, Databases API, Jobs API, and 4 more. Tagged areas include Database, SQL, Version Control, Git for Data, and MySQL.


  DoltHub''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Dolthub Plans Pricing
  plan_count: 2
  slug: dolthub-plans-pricing
random_paper: 43
rate_limits:
- limit_count: 3
  name: Dolthub Rate Limits
  slug: dolthub-rate-limits
score:
  band: thin
  composite: 35.4
  delta: -2.1
  facets:
    commercial_clarity: 28.9
    contract_quality: 52.4
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 37.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dolthub/refs/heads/main/screenshots/dolthub-2026-06-20T180140.png
security:
- kind: authentication
  name: Dolthub Authentication
  slug: dolthub-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Dolthub Domain Security
  slug: dolthub-domain-security
  summary_line: TLSv1.3 · DMARC
slug: dolthub
tags:
- Database
- SQL
- Version Control
- Git for Data
- MySQL
website: https://www.dolthub.com
---
