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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 24.0
  scored_at: '2026-07-23'
api_count: 3
apis:
- description: The AudaConnect API enables third-party software developers to access, query, and update the Audatex platform including assessments, vehicle reference data, repair orders, and photo management using R
  name: Audatex AudaConnect API
  slug: audatex-audaconnect-api
- description: The Audatex GIC (Global Integration Component) API provides integration capabilities for claims processing and vehicle damage assessment workflows in the insurance and collision repair industries.
  name: Audatex GIC API
  slug: audatex-gic-api
- description: The Solera API Gateway provides access to Audatex and Solera claims processing services including ClaimImage document return and other automotive claims data APIs for North American insurance markets.
  name: Solera API Gateway
  slug: solera-api-gateway
artifact_total: 23
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/audatex-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/audatex-a-solera-company
- group: company
  title: ''
  type: Website
  url: https://www.audatex.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.audatex.com/solutions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.audatex.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.audatex.com/terms-and-conditions/
- group: operate
  title: ''
  type: Contact
  url: https://www.audatex.com/contact/
created: '2025-01-01'
description: Audatex (part of Solera Holdings) provides automotive claims and repair solutions with data and technology services for the automotive insurance, collision repair, and fleet management industries. It offers the AudaConnect API platform for third-party integration with claims processing, damage assessment, repair cost estimation, and vehicle data workflows. APIs are RESTful with JSON/XML support and OAuth 2.0 authentication.
features:
- description: Search, download, upload, and amend vehicle damage assessments programmatically via the AudaConnect API.
  name: Claims Assessment API
- description: Access Audatex repair cost estimation data and labor rates for collision repair workflow automation.
  name: Repair Cost Estimation
- description: Upload, retrieve, and manage vehicle damage photos attached to claims via the assessment API.
  name: Photo Management
- description: Create, update, and query repair orders from bodyshop management systems via BMS API integration.
  name: Repair Order Integration
- description: Query vehicle reference data including make, model, trim, and VIN decoding for assessment setup.
  name: Vehicle Reference Data
- description: All AudaConnect APIs are secured with OAuth 2.0 authorization for enterprise-grade access control.
  name: OAuth 2.0 Security
finops:
- name: Audatex Finops
  service_category: API
  slug: audatex-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/audatex.png
integrations:
- description: Native integration with major BMS platforms for automated repair order and parts pricing workflows.
  name: Bodyshop Management Systems
- description: Integration with insurance policy and claims management systems for end-to-end claims processing.
  name: Insurance Core Systems
- description: Integration with vehicle history and VIN data providers for complete vehicle information at claims initiation.
  name: Vehicle History Providers
- description: Connection to OEM and aftermarket parts supplier catalogs for parts pricing and availability in repair estimates.
  name: Parts Suppliers
layout: provider
modified: '2026-04-19'
name: Audatex
nav: Providers
network: true
overview: 'Audatex publishes 1 API on the [APIs.io](https://apis.io/) network: AudaConnect API. Tagged areas include Automotive, Claims Processing, Insurance, Repair Management, and Vehicle Data.


  Audatex''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Audatex Plans Pricing
  plan_count: 3
  slug: audatex-plans-pricing
random_paper: 34
rate_limits:
- limit_count: 5
  name: Audatex Rate Limits
  slug: audatex-rate-limits
score:
  band: thin
  composite: 36.3
  delta: -1.1
  facets:
    commercial_clarity: 60.5
    contract_quality: 37.7
    developer_ergonomics: 8.7
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 37.4
  regulatory:
    applies: true
    regime: Insurance
    regime_id: insurance
    score: 30.4
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/audatex/refs/heads/main/screenshots/audatex-2026-06-20T172546.png
security:
- kind: domain-security
  name: Audatex Domain Security
  slug: audatex-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: audatex
solutions:
- description: End-to-end automation of auto insurance claims from FNOL through repair authorization and settlement.
  name: Claims Process Automation
- description: Digital workflow management for collision repair shops integrating estimates, parts, labor, and customer communication.
  name: Repair Shop Workflow
tags:
- Automotive
- Claims Processing
- Insurance
- Repair Management
- Vehicle Data
use_cases:
- description: Automate first notice of loss, damage assessment, and claims settlement workflows for auto insurers.
  name: Insurance Claims Automation
- description: Integrate bodyshop management systems with Audatex for repair order creation, parts pricing, and labor time.
  name: Bodyshop Management System Integration
- description: Access vehicle valuation and total loss thresholds to automate total loss claims decisions.
  name: Total Loss Determination
- description: Enable digital submission of vehicle damage photos and assessment data from mobile apps to the Audatex platform.
  name: Digital Claims Submission
website: https://www.audatex.com/
---
