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
    agentic_access: false
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
  score: 28.4
  scored_at: '2026-07-28'
api_count: 3
apis:
- description: REST API endpoints for managing and monitoring Oracle Database partitioning operations.
  name: Oracle Database REST API - Partitioning
  slug: oracle-database-rest-api-partitioning
- description: REST services for partition management through SQL Developer.
  name: Oracle SQL Developer REST Services - Partitioning
  slug: oracle-sql-developer-rest-services-partitioning
- description: OCI API for managing partitioned databases in Oracle Cloud.
  name: Oracle Cloud Infrastructure Database API - Partitioning
  slug: oracle-cloud-infrastructure-database-api-partitioning
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/oracle-partitioning-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/oracle
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.oracle.com/en/database/oracle/oracle-database/19/vldbg/partition-intro.html
- group: other
  title: ''
  type: Best Practices
  url: https://docs.oracle.com/en/database/oracle/oracle-database/19/vldbg/partition-strategies.html
- group: other
  title: ''
  type: White Papers
  url: https://www.oracle.com/technetwork/database/options/partitioning/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.oracle.com/database/technologies/partitioning/pricing.html
- group: operate
  title: ''
  type: Support
  url: https://support.oracle.com
- group: auth
  title: ''
  type: Authentication
  url: https://docs.oracle.com/en/database/oracle/oracle-rest-data-services/19.2/orrst/authentication.html
- group: operate
  title: ''
  type: StatusPage
  url: https://status.oracle.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.oracle.com/legal/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.oracle.com/legal/privacy/
created: '2024-01-01'
description: Oracle Partitioning enables tables and indexes to be partitioned into smaller, more manageable pieces, improving performance, availability, and manageability of large database objects.
finops:
- name: Oracle Partitioning Finops
  service_category: API
  slug: oracle-partitioning-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/oracle-partitioning.png
layout: provider
modified: '2026-03-16'
name: Oracle Partitioning
nav: Providers
network: true
overview: 'Oracle Partitioning publishes 2 APIs on the [APIs.io](https://apis.io/) network: Oracle Database REST API - Partitioning and Oracle Cloud Infrastructure Database API - Partitioning. Tagged areas include Composite-Partitioning, Database, Hash-Partitioning, Interval-Partitioning, and List-Partitioning.


  Oracle Partitioning''s developer surface includes getting-started guide, pricing, support, authentication, and 7 more developer resources.'
plans:
- name: Oracle Partitioning Plans Pricing
  plan_count: 3
  slug: oracle-partitioning-plans-pricing
random_paper: 54
rate_limits:
- limit_count: 5
  name: Oracle Partitioning Rate Limits
  slug: oracle-partitioning-rate-limits
score:
  band: thin
  composite: 40.8
  delta: -3.7
  facets:
    commercial_clarity: 71.1
    contract_quality: 32.3
    developer_ergonomics: 26.1
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 44.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/oracle-partitioning/refs/heads/main/screenshots/oracle-partitioning-2026-06-20T191138.png
security:
- kind: domain-security
  name: Oracle Partitioning Domain Security
  slug: oracle-partitioning-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: oracle-partitioning
tags:
- Composite-Partitioning
- Database
- Hash-Partitioning
- Interval-Partitioning
- List-Partitioning
- Oracle
- Partitioning
- Performance
- Range-Partitioning
- Scalability
- VLDB
---
