---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-07-28'
api_count: 2
apis:
- description: REST API for IBM Db2 SaaS on IBM Cloud used to access data, view and create database objects, administer users and roles, and monitor cloud-hosted Db2 service instances. Authenticated via IBM Cloud IA
  name: IBM Db2 as a Service REST API
  slug: saas-api
- description: Native Db2 REST services that allow applications to create, discover, execute, and manage user-defined services directly against a Db2 database via HTTPS, integrated with the Db2 distributed data faci
  name: IBM Db2 REST Services
  slug: rest-services
artifact_total: 4
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ibm-db2-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ibm-db2-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ibm.com/products/db2
- group: docs
  title: ''
  type: Documentation
  url: https://www.ibm.com/docs/en/db2
- group: commercial
  title: ''
  type: Pricing
  url: https://www.ibm.com/products/db2/pricing
- group: start
  title: ''
  type: Signup
  url: https://cloud.ibm.com/registration
- group: other
  title: ''
  type: Developer Center
  url: https://www.ibm.com/products/db2/developers
- group: operate
  title: ''
  type: Community
  url: https://community.ibm.com/community/user/datamanagement/communities/community-home?CommunityKey=db8b3b69-c8a7-44f4-b29f-1fa1bba6e3e5
- group: operate
  title: ''
  type: Support
  url: https://www.ibm.com/mysupport
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/ibm-analytics
created: '2026-05-11'
description: IBM Db2 is a family of data management products from IBM that includes relational and hybrid database servers running on cloud, distributed, and z/OS platforms, supporting transactional, analytical, and AI workloads. Db2 exposes RESTful services that let applications create, discover, execute, and manage user-defined services natively against the database, and IBM Db2 as a Service on IBM Cloud provides a managed REST API for administering and querying cloud-hosted Db2 databases. Authentication is performed via HTTP basic auth, client certificates, or IBM Cloud IAM Bearer tokens depending on the deployment.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ibm-db2.png
layout: provider
modified: '2026-05-11'
name: IBM Db2
nav: Providers
network: true
overview: 'IBM Db2 publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Database, Relational Database, Cloud Database, SQL, and Data Management.


  IBM Db2''s developer surface includes documentation, pricing, signup flow, support, and 6 more developer resources.'
random_paper: 38
score:
  band: minimal
  composite: 11.6
  delta: -2.4
  facets:
    commercial_clarity: 10.5
    contract_quality: 0.0
    developer_ergonomics: 13.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 14.0
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ibm-db2/refs/heads/main/screenshots/ibm-db2-2026-06-20T183127.png
security:
- kind: domain-security
  name: Ibm Db2 Domain Security
  slug: ibm-db2-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Ibm Db2 Vulnerability Disclosure
  slug: ibm-db2-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: ibm-db2
tags:
- Database
- Relational Database
- Cloud Database
- SQL
- Data Management
- IBM Cloud
website: https://www.ibm.com/products/db2
---
