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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 2
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/ibm/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/netezza-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.ibm.com/trust/security-psirt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/netezza-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ibm.com/products/netezza
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.ibm.com/components/netezza-performance-server/
- group: docs
  title: ''
  type: Documentation
  url: https://www.ibm.com/docs/en/netezza
- group: start
  title: ''
  type: GettingStarted
  url: https://www.ibm.com/docs/en/netezza?topic=data-getting-started
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/IBM
- group: company
  title: ''
  type: Blog
  url: https://developer.ibm.com/components/netezza-performance-server/articles/
- group: operate
  title: ''
  type: Support
  url: https://community.ibm.com/community/user/groups/community-home?CommunityKey=d9f9d5de-e89f-4a6a-84a0-31df8b81f182
- group: commercial
  title: ''
  type: Pricing
  url: https://www.ibm.com/products/netezza/pricing
- group: build
  title: ''
  type: Packages
  url: packages/netezza-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/netezza-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/netezza-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/netezza-security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/netezza-llms.txt
created: '2026-07-17'
description: IBM Netezza Performance Server is a cloud-native data warehouse and analytics appliance for running large-scale SQL analytics and in-database machine learning on structured data. Originally a standalone data-warehouse appliance vendor acquired by IBM, Netezza is now delivered as Netezza Performance Server on IBM Cloud, AWS, and Microsoft Azure and as part of IBM Cloud Pak for Data. It is consumed primarily through SQL over standard database connectivity — the pure-Python nzpy DB-API 2.0 driver, JDBC (nzjdbc) and ODBC drivers, and the nzpyida in-database analytics library — rather than as a public REST API, with a REST interface for backup/restore administration and a web console for monitoring and administration.
image: https://www.ibm.com/products/netezza
layout: provider
modified: '2026-08-21'
name: Netezza
nav: Providers
network: true
overview: 'Netezza is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data Warehouse, Analytics, Database, and SQL.


  Netezza''s developer surface includes documentation, getting-started guide, engineering blog, support, pricing, and 12 more developer resources.'
random_paper: 13
score:
  band: emerging
  composite: 18.6
  coverage:
    artifact_dirs: 6
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 45.2
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 18.6
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/netezza/refs/heads/main/screenshots/netezza-2026-08-07T184931.png
security:
- kind: domain-security
  name: Netezza Domain Security
  slug: netezza-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Netezza Vulnerability Disclosure
  slug: netezza-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: netezza
tags:
- Company
- Data Warehouse
- Analytics
- Database
- SQL
- Machine-Learning
- Big Data
- Cloud Data Platform
- IBM
website: https://www.ibm.com/products/netezza
---
