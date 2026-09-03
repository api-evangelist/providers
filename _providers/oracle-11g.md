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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-02'
api_count: 4
apis:
- description: Java Database Connectivity driver for connecting Java applications to Oracle 11g.
  name: Oracle Database 11g JDBC API
  slug: oracle-database-11g-jdbc-api
- description: Procedural Language extension to SQL for stored procedures and functions.
  name: Oracle Database 11g PL/SQL API
  slug: oracle-database-11g-plsql-api
- description: C/C++ API for building database applications.
  name: Oracle Database 11g OCI (Oracle Call Interface)
  slug: oracle-database-11g-oci
- description: RESTful web services for Oracle Database.
  name: Oracle Database 11g REST Data Services
  slug: oracle-database-11g-rest-data-services
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/oracle-11g-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/oracle
- group: docs
  title: ''
  type: Documentation
  url: https://docs.oracle.com/cd/E11882_01/index.htm
created: '2024-01-01'
description: Collection of APIs and interfaces available for Oracle Database 11g.
finops:
- name: Oracle 11G Finops
  service_category: API
  slug: oracle-11g-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/oracle-11g.png
layout: provider
modified: '2026-04-28'
name: Oracle Database 11g
nav: Providers
network: true
overview: 'Oracle Database 11g publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Database, Enterprise, Oracle, PL/SQL, and RDBMS.


  Oracle Database 11g''s developer surface includes documentation and 2 more developer resources.'
plans:
- name: Oracle 11G Plans Pricing
  plan_count: 3
  slug: oracle-11g-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 5
  name: Oracle 11G Rate Limits
  slug: oracle-11g-rate-limits
score:
  band: emerging
  composite: 12.0
  coverage:
    artifact_dirs: 5
    catalog_gap: 76.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 55.6
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 12.0
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/oracle-11g/refs/heads/main/screenshots/oracle-11g-2026-06-20T191117.png
security:
- kind: domain-security
  name: Oracle 11G Domain Security
  slug: oracle-11g-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: oracle-11g
tags:
- Database
- Enterprise
- Oracle
- PL/SQL
- RDBMS
- SQL
---
