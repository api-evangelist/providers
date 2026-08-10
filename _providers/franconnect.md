---
access_model:
  confidence: medium
  label: Enterprise · Requires approval
  onboarding: approval
  pricing: enterprise
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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-10'
api_count: 5
apis:
- description: 'Franchise Sales / Development module (path segment "fs"). Import and export franchise development leads, prospects, and the franchise sales pipeline used to recruit and qualify new franchisees. Exact '
  name: FranConnect Franchise Sales API
  slug: franconnect-franchise-sales-api
- description: CRM module (path segment "cm"). Read and write contacts and relationship/communication records that support franchise and consumer engagement. Endpoint paths are modeled from the published module stru
  name: FranConnect CRM API
  slug: franconnect-crm-api
- description: Info Manager module (path segment "fim"). The system of record for franchisee and unit/location profiles, plus document retrieval - recent releases added dedicated REST endpoints for programmatic acce
  name: FranConnect Info Manager API
  slug: franconnect-info-manager-api
- description: Finance module (path segment "manage-finance"). Import and export financial data - unit sales reporting, royalties, fees, and invoicing used to calculate and reconcile franchisee obligations. Endpoint
  name: FranConnect Finance API
  slug: franconnect-finance-api
- description: Admin module (path segment "admin"). Administrative entities such as users, roles, and configuration that govern the FranConnect Sky tenant. Endpoint paths are modeled from the published module struct
  name: FranConnect Admin API
  slug: franconnect-admin-api
artifact_total: 9
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/franconnect-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/franconnect-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/franconnect-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/franconnect
- group: company
  title: ''
  type: Website
  url: https://www.franconnect.com/en/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.franconnect.net/
- group: docs
  title: ''
  type: Documentation
  url: https://marketplace.franconnect.net/api-detail.html
- group: commercial
  title: ''
  type: Plans
  url: plans/franconnect-plans-pricing.yml
created: '2026-07-04'
description: FranConnect is a franchise and multi-location management platform used by 1,500+ brands across roughly one million locations, covering franchise development and sales, franchisee/unit information management, field operations and audits, financials and royalties, and CRM. Its FranConnect Sky product exposes a RESTful API - organized by module (Franchise Sales "fs", CRM "cm", Info Manager "fim", Finance "manage-finance", and Admin "admin") - that lets customers import and export data between FranConnect Sky and third-party applications. All API calls are made over HTTPS and authenticated with an Authorization-Token header. API access is not open/self-serve - it is gated behind a FranConnect Sky customer or partner account, with credentials provisioned by FranConnect, and the reference documentation portal (docs.franconnect.net) requires a signed-in account.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/franconnect.png
layout: provider
modified: '2026-07-04'
name: FranConnect
nav: Providers
network: true
overview: 'FranConnect publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Franchise Management, Franchise Development, Franchise Operations, Field Operations, and Multi-Location.


  FranConnect''s developer surface includes documentation and 7 more developer resources.'
plans:
- name: Franconnect Plans Pricing
  plan_count: 1
  slug: franconnect-plans-pricing
random_paper: 9
score:
  band: emerging
  composite: 14.9
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 14.9
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/franconnect/refs/heads/main/screenshots/franconnect-2026-07-25T215117.png
security:
- kind: domain-security
  name: Franconnect Domain Security
  slug: franconnect-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Franconnect Vulnerability Disclosure
  slug: franconnect-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Franconnect Trust Center
  slug: franconnect-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, PCI DSS, HIPAA, FedRAMP, GDPR, CSA STAR
slug: franconnect
tags:
- Franchise Management
- Franchise Development
- Franchise Operations
- Field Operations
- Multi-Location
- CRM
- Franchise Sales
- SaaS
website: https://www.franconnect.com/en/
---
