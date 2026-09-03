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
    agentic_commerce: false
    auth_clarity: bearer
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 18.0
  scored_at: '2026-09-03'
api_count: 6
apis:
- description: REST API for managing procurement operations including requisitions, purchase orders, and supplier information.
  name: Oracle Procurement REST API
  slug: oracle-procurement-rest-api
- description: Create, update, and manage purchase orders.
  name: Purchase Orders API
  slug: purchase-orders-api
- description: Manage purchase requisitions and approval workflows.
  name: Requisitions API
  slug: requisitions-api
- description: Access and manage supplier information, sites, and contacts.
  name: Suppliers API
  slug: suppliers-api
- description: Manage blanket purchase agreements and contract terms.
  name: Purchase Agreements API
  slug: purchase-agreements-api
- description: Record and manage receipt transactions for purchased goods and services.
  name: Receipts API
  slug: receipts-api
artifact_total: 10
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/oracle-procurement-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/oracle
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.oracle.com/en/cloud/saas/procurement/23d/fapra/QuickStart.html
- group: auth
  title: ''
  type: Authentication
  url: https://docs.oracle.com/en/cloud/get-started/subscriptions-cloud/
- group: start
  title: ''
  type: Portal
  url: https://cloud.oracle.com/
- group: operate
  title: ''
  type: Support
  url: https://www.oracle.com/support/
- group: operate
  title: ''
  type: StatusPage
  url: https://ocistatus.oraclecloud.com/
created: '2024-01-01'
description: A collection of APIs for Oracle Procurement Cloud services, enabling procurement processes, supplier management, purchasing, and spend analysis.
finops:
- name: Oracle Procurement Finops
  service_category: API
  slug: oracle-procurement-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/oracle-procurement.png
layout: provider
modified: '2026-04-28'
name: Oracle Procurement
nav: Providers
network: true
overview: 'Oracle Procurement publishes 1 API on the [APIs.io](https://apis.io/) network: REST API. Tagged areas include ERP, Procurement, Purchasing, Spend Management, and Suppliers.


  Oracle Procurement''s developer surface includes getting-started guide, authentication, developer portal, support, and 3 more developer resources.'
plans:
- name: Oracle Procurement Plans Pricing
  plan_count: 3
  slug: oracle-procurement-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 5
  name: Oracle Procurement Rate Limits
  slug: oracle-procurement-rate-limits
score:
  band: thin
  composite: 27.4
  coverage:
    artifact_dirs: 5
    catalog_gap: 81.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 26.7
    developer_ergonomics: 47.6
    discoverability: 46.3
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 27.4
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/oracle-procurement/refs/heads/main/screenshots/oracle-procurement-2026-06-20T191144.png
security:
- kind: domain-security
  name: Oracle Procurement Domain Security
  slug: oracle-procurement-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: oracle-procurement
tags:
- ERP
- Procurement
- Purchasing
- Spend Management
- Suppliers
website: https://cloud.oracle.com/
---
