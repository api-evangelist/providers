---
access_model:
  confidence: medium
  label: Enterprise (free trial)
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  trial: true
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 6
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ivalua-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ivalua-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ivalua.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.ivalua.com/technology/ivalua-open-ecosystem/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/Ivalua
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ivalua
- group: company
  title: ''
  type: Blog
  url: https://www.ivalua.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.saasworthy.com/product/ivalua-procurement-solution/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://www.ivalua.com/
- group: other
  title: ''
  type: X
  url: https://twitter.com/ivalua
- group: commercial
  title: ''
  type: Plans
  url: plans/ivalua-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ivalua-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/ivalua-finops.yml
created: '2026-06-13'
description: Ivalua is an enterprise AI-powered procurement platform offering a unified source-to-pay solution that enables organizations to manage all categories of spend and suppliers. The platform exposes a REST API built on open standards, supporting JSON and XML data formats via secure web services, enabling programmatic integration for supplier onboarding, contract lifecycle management, sourcing events, purchase orders, invoice automation, and spend analytics. Ivalua's Enterprise Application Interface (EAI) module combines APIs, ETL, and query tools to orchestrate data transfer between Ivalua and external enterprise systems including SAP, Oracle, and Microsoft Dynamics. The Integration Hub supports 60+ ERP and enterprise system connectors, providing developer tooling to build and discover APIs without requiring middleware. Authentication leverages SAML-based SSO and two-factor authentication, with raw interface request/response logging available through the Integration Console for
  audit and debugging purposes.
finops:
- name: Ivalua Finops
  service_category: ''
  slug: ivalua-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ivalua.png
jsonld:
- class_count: 17
  name: Ivalua Context
  property_count: 5
  slug: ivalua-context
layout: provider
modified: '2026-07-25'
name: Ivalua
nav: Providers
network: true
overview: 'Ivalua is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Procurement, Source-to-Pay, Supplier Management, Contract Management, and Sourcing.


  The Ivalua catalog on APIs.io includes 1 JSON-LD context.


  Ivalua''s developer surface includes documentation, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Ivalua Plans Pricing
  plan_count: 1
  slug: ivalua-plans-pricing
random_paper: 46
rate_limits:
- limit_count: 3
  name: Ivalua Rate Limits
  slug: ivalua-rate-limits
score:
  band: emerging
  composite: 24.9
  delta: -0.2
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 11.3
    developer_ergonomics: 11.9
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 25.1
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ivalua/refs/heads/main/screenshots/ivalua-2026-06-20T183638.png
security:
- kind: domain-security
  name: Ivalua Domain Security
  slug: ivalua-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Ivalua Vulnerability Disclosure
  slug: ivalua-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: ivalua
tags:
- Procurement
- Source-to-Pay
- Supplier Management
- Contract Management
- Sourcing
- Purchase Orders
- Invoices
- Spend Analytics
- ERP Integration
- Enterprise
website: https://www.ivalua.com/
---
