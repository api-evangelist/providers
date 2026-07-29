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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: false
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
  score: 21.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 84
  human_in_the_loop: 1
  name: Apache Superset Agentic Access
  operation_count: 146
  slug: apache-superset-agentic-access
  summary_line: 146 operations · 84 acting · 1 human-in-the-loop
api_count: 21
apis:
- description: The Annotation Layer API from Apache Superset — 4 operation(s) for annotation layer.
  name: Apache Superset Annotation Layer API
  slug: apache-superset-annotation-layer-api
- description: The Assets API from Apache Superset — 2 operation(s) for assets.
  name: Apache Superset Assets API
  slug: apache-superset-assets-api
- description: The Async Event API from Apache Superset — 1 operation(s) for async event.
  name: Apache Superset Async Event API
  slug: apache-superset-async-event-api
- description: The Available Domains API from Apache Superset — 1 operation(s) for available domains.
  name: Apache Superset Available Domains API
  slug: apache-superset-available-domains-api
- description: The Cachekey API from Apache Superset — 1 operation(s) for cachekey.
  name: Apache Superset Cachekey API
  slug: apache-superset-cachekey-api
- description: The Chart API from Apache Superset — 10 operation(s) for chart.
  name: Apache Superset Chart API
  slug: apache-superset-chart-api
- description: The Css Template API from Apache Superset — 2 operation(s) for css template.
  name: Apache Superset Css Template API
  slug: apache-superset-css-template-api
- description: The Dashboard API from Apache Superset — 16 operation(s) for dashboard.
  name: Apache Superset Dashboard API
  slug: apache-superset-dashboard-api
- description: The Database API from Apache Superset — 8 operation(s) for database.
  name: Apache Superset Database API
  slug: apache-superset-database-api
- description: The Dataset API from Apache Superset — 8 operation(s) for dataset.
  name: Apache Superset Dataset API
  slug: apache-superset-dataset-api
- description: The Embedded Dashboard API from Apache Superset — 1 operation(s) for embedded dashboard.
  name: Apache Superset Embedded Dashboard API
  slug: apache-superset-embedded-dashboard-api
- description: The Log API from Apache Superset — 2 operation(s) for log.
  name: Apache Superset Log API
  slug: apache-superset-log-api
- description: The Me API from Apache Superset — 2 operation(s) for me.
  name: Apache Superset Me API
  slug: apache-superset-me-api
- description: The Menu API from Apache Superset — 1 operation(s) for menu.
  name: Apache Superset Menu API
  slug: apache-superset-menu-api
- description: The Query API from Apache Superset — 3 operation(s) for query.
  name: Apache Superset Query API
  slug: apache-superset-query-api
- description: The Report API from Apache Superset — 2 operation(s) for report.
  name: Apache Superset Report API
  slug: apache-superset-report-api
- description: The Saved Query API from Apache Superset — 2 operation(s) for saved query.
  name: Apache Superset Saved Query API
  slug: apache-superset-saved-query-api
- description: The Security API from Apache Superset — 11 operation(s) for security.
  name: Apache Superset Security API
  slug: apache-superset-security-api
- description: The Sqllab API from Apache Superset — 6 operation(s) for sqllab.
  name: Apache Superset Sqllab API
  slug: apache-superset-sqllab-api
- description: The Tag API from Apache Superset — 3 operation(s) for tag.
  name: Apache Superset Tag API
  slug: apache-superset-tag-api
- description: The Theme API from Apache Superset — 2 operation(s) for theme.
  name: Apache Superset Theme API
  slug: apache-superset-theme-api
artifact_total: 47
collections:
- collection_type: open
  name: Apache Superset REST API
  slug: open-apache-superset
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/apache-superset-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/apache-superset-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apache-superset-domain-security.yml
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/apache/superset
- group: docs
  title: ''
  type: Documentation
  url: https://superset.apache.org/docs/intro
- group: start
  title: ''
  type: Portal
  url: https://superset.apache.org/
- group: start
  title: ''
  type: GettingStarted
  url: https://superset.apache.org/docs/quickstart
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://github.com/apache/superset/releases
- group: operate
  title: ''
  type: Support
  url: https://github.com/apache/superset/discussions
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.apache.org/licenses/
- group: build
  title: Python Package
  type: SDKs
  url: https://pypi.org/project/apache-superset/
created: '2026-03-16'
description: Apache Superset is a modern data exploration and visualization platform designed to be visual, intuitive, and interactive. It provides a rich set of data visualizations, a no-code chart builder, and a SQL editor with support for most SQL-speaking databases. Superset exposes a comprehensive REST API for programmatic access to dashboards, charts, datasets, databases, and user management. It is an Apache Software Foundation top-level project.
features:
- description: Drag-and-drop chart builder with 40+ visualization types requiring no coding.
  name: No-Code Chart Builder
- description: Browser-based SQL editor with query history, saved queries, and result export.
  name: SQL Lab
- description: Interactive dashboard composition with filters, tabs, and layout customization.
  name: Dashboard Builder
- description: Centralized dataset definitions with virtual columns, metrics, and certification.
  name: Semantic Layer
- description: Fine-grained data access control with row-level security rules.
  name: Row-Level Security
- description: Embed Superset dashboards in external applications via iframe or SDK.
  name: Embedded Dashboards
- description: Scheduled PDF/image reports and threshold-based alerts via email or Slack.
  name: Alerts and Reports
- description: 40+ database connectors via SQLAlchemy including BigQuery, Snowflake, and Redshift.
  name: Database Connectivity
finops:
- name: Apache Superset Finops
  service_category: API
  slug: apache-superset-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apache-superset.png
integrations:
- description: Native PostgreSQL support as both metadata database and data source.
  name: PostgreSQL
- description: Druid connector for sub-second OLAP queries on time-series data.
  name: Apache Druid
- description: Google BigQuery connector for cloud data warehouse analytics.
  name: BigQuery
- description: Snowflake connector for cloud analytics platform.
  name: Snowflake
- description: Spark SQL via Hive Thrift Server for distributed data analysis.
  name: Apache Spark SQL
- description: Slack integration for alerts and scheduled report delivery.
  name: Slack
- description: Airflow integration for orchestrating data pipeline and report schedules.
  name: Apache Airflow
layout: provider
modified: '2026-05-19'
name: Apache Superset
nav: Providers
network: true
overview: 'Apache Superset publishes 21 APIs on the [APIs.io](https://apis.io/) network, including Annotation Layer API, Assets API, Async Event API, and 18 more. Tagged areas include Analytics, BI, Dashboard, Data Visualization, and SQL.


  Apache Superset''s developer surface includes documentation, developer portal, getting-started guide, release notes, support, and 6 more developer resources.'
plans:
- name: Apache Superset Plans Pricing
  plan_count: 3
  slug: apache-superset-plans-pricing
random_paper: 45
rate_limits:
- limit_count: 5
  name: Apache Superset Rate Limits
  slug: apache-superset-rate-limits
score:
  band: thin
  composite: 38.9
  delta: -2.7
  facets:
    commercial_clarity: 50.0
    contract_quality: 33.9
    developer_ergonomics: 39.1
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 47.4
  previous_composite: 41.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 21
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apache-superset/refs/heads/main/screenshots/apache-superset-2026-06-20T172150.png
security:
- kind: domain-security
  name: Apache Superset Domain Security
  slug: apache-superset-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Apache Superset Vulnerability Disclosure
  slug: apache-superset-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: apache-superset
tags:
- Analytics
- BI
- Dashboard
- Data Visualization
- SQL
- Open Source
use_cases:
- description: Self-service BI dashboards for business users across operational and analytical data.
  name: Business Intelligence Dashboards
- description: Ad-hoc data exploration and visualization for data analysts.
  name: Data Exploration
- description: White-label analytics embedded in SaaS products and internal applications.
  name: Embedded Analytics
- description: Custom SQL-based reports and scheduled distribution.
  name: SQL-Based Reporting
website: https://superset.apache.org/
---
