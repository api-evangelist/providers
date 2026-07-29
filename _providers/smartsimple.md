---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 7
apis:
- description: 'Get, list, and update (create) records stored in SmartSimple''s Universal Tracking Application (UTA) at Level 1, Level 2, and Level 3 - the grant applications, reviews, and sub-records at the heart of '
  name: SmartSimple SmartConnect Records API
  slug: smartsimple-smartconnect-records-api
- description: Get, list, and update the people (applicants, reviewers, contacts, and internal staff) in a SmartSimple instance via the /API/1/user/ endpoint, including their standard and custom profile fields and m
  name: SmartSimple SmartConnect Users API
  slug: smartsimple-smartconnect-users-api
- description: Get, list, and update the organizations (companies, grantee institutions, and accounts) in a SmartSimple instance via the /API/1/company/ endpoint, with their standard and custom fields and multiple-a
  name: SmartSimple SmartConnect Organizations API
  slug: smartsimple-smartconnect-organizations-api
- description: Get, list, and update UTA transaction records (payments, disbursements, budget lines, and other transactional line items attached to grants) via the /API/1/transactions/ endpoint, with criteria filter
  name: SmartSimple SmartConnect Transactions API
  slug: smartsimple-smartconnect-transactions-api
- description: Download a single file, list the files on a record or field, and keyword-search across files using the SmartConnect Download File, List Files, and Search Files actions. Files are the supporting docume
  name: SmartSimple SmartConnect Files API
  slug: smartsimple-smartconnect-files-api
- description: Consume SmartSimple report data through OData V2, V3, and V4 services, with public (pub) endpoints for openly exposed data and private (pri) endpoints requiring basic authentication - for example /ODa
  name: SmartSimple OData Reporting API
  slug: smartsimple-odata-reporting-api
- description: 'The legacy SOAP Web Services API, exposed per instance via a WSDL at /WS/services/UtaUpdate?wsdl (for example https://smart.smartsimple.biz/WS/services/UtaUpdate?wsdl). It predates SmartConnect - new '
  name: SmartSimple Web Services (SOAP) API
  slug: smartsimple-web-services-soap-api
artifact_total: 12
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/smartsimple-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/smartsimple-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.smartsimple.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/smartsimple-software-inc
- group: docs
  title: ''
  type: Documentation
  url: https://wiki.smartsimple.com/wiki/APIs
- group: start
  title: ''
  type: InteractiveDemo
  url: https://api.smartsimple.com/devtools/api.html
- group: commercial
  title: ''
  type: Pricing
  url: https://www.smartsimple.com/pricing
- group: commercial
  title: ''
  type: Plans
  url: plans/smartsimple-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/smartsimple-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/smartsimple-finops.yml
created: '2026-07-05'
description: SmartSimple Software builds SmartSimple Cloud, a configurable cloud platform for grants management, research and government funding administration, corporate social responsibility (CSR), scholarships, and case management. The platform exposes three documented programmatic interfaces on each client instance - SmartConnect (a JSON-based RESTful API), an OData reporting API, and a legacy SOAP Web Services API - covering records (UTA Level 1/2/3), users, organizations, transactions, custom fields, and files. Access is instance-scoped - every customer runs on their own alias.smartsimple.com tenant and provisions an API user account or access token, so the documented endpoints are modeled against a customer instance rather than a single public gateway.
finops:
- name: Smartsimple Finops
  service_category: Grants and Funding Management
  slug: smartsimple-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/smartsimple.png
layout: provider
modified: '2026-07-05'
name: SmartSimple
nav: Providers
network: true
overview: 'SmartSimple publishes 7 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Grants Management, Research Administration, CSR, Funding, and Case Management.


  SmartSimple''s developer surface includes documentation, pricing, and 8 more developer resources.'
plans:
- name: Smartsimple Plans Pricing
  plan_count: 3
  slug: smartsimple-plans-pricing
random_paper: 46
rate_limits:
- limit_count: 4
  name: Smartsimple Rate Limits
  slug: smartsimple-rate-limits
score:
  band: emerging
  composite: 24.8
  delta: -2.6
  facets:
    commercial_clarity: 57.9
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 27.4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: domain-security
  name: Smartsimple Domain Security
  slug: smartsimple-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Smartsimple Trust Center
  slug: smartsimple-trust-center
  summary_line: ISO 27001, HIPAA
slug: smartsimple
tags:
- Grants Management
- Research Administration
- CSR
- Funding
- Case Management
- SaaS
- REST
- OData
- SOAP
website: https://www.smartsimple.com
---
