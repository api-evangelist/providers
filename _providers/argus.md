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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 6.7
  scored_at: '2026-07-23'
api_count: 5
apis:
- description: The ARGUS API is a cloud-based integration gateway that provides programmatic access to data in ARGUS Enterprise and other cloud-enabled ARGUS solutions. It enables users to extract and ingest data, t
  name: ARGUS API
  slug: argus-api
- description: The industry-standard commercial property valuation and cash flow forecasting software providing lease-by-lease modeling, DCF valuations, budgeting, scenario testing, and 40+ portfolio reports.
  name: ARGUS Enterprise
  slug: argus-enterprise
- description: Real estate development feasibility and project management software for property developers, appraisers, and financiers covering pro forma modeling, residual land value, scenario analysis, and cash fl
  name: ARGUS Developer
  slug: argus-developer
- description: Next-generation real estate investment management platform integrating ARGUS Enterprise with portfolio dashboards, benchmarking, asset manager, portfolio manager, and fund manager capabilities for com
  name: ARGUS Intelligence Platform
  slug: argus-intelligence
- description: Real estate fund management software for modeling and managing the performance of real estate funds, supporting complex fund structures, waterfall calculations, and investor reporting.
  name: ARGUS Taliance
  slug: argus-taliance
artifact_total: 26
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/argus-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/argus-software-solutions
- group: company
  title: ''
  type: Website
  url: https://www.altusgroup.com/argus/
- group: company
  title: ''
  type: Blog
  url: https://www.altusgroup.com/insights/
- group: docs
  title: ''
  type: Documentation
  url: https://www.altusgroup.com/argus/downloads/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.altusgroup.com/support/start-using-argus-intelligence/
- group: start
  title: ''
  type: Portal
  url: https://cloud.altusplatform.com/login
- group: operate
  title: ''
  type: Support
  url: https://www.altusgroup.com/support/
- group: learn
  title: ''
  type: Training
  url: https://www.altusgroup.com/argus/training/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.altusgroup.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.altusgroup.com/privacy-policy/
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://www.altusgroup.com/argus/downloads/
- group: auth
  title: ''
  type: Security
  url: https://www.altusgroup.com/security/
created: '2024-01-15'
description: ARGUS is the industry-standard suite of commercial real estate software solutions by Altus Group. The ARGUS platform includes ARGUS Enterprise (property valuation and cash flow forecasting), ARGUS Developer (development feasibility and project management), ARGUS Intelligence Platform (portfolio analytics, asset management, and fund management), ARGUS EstateMaster (property development feasibility), and ARGUS Taliance (real estate fund management). ARGUS is recognized as the industry standard and taught at 200+ universities worldwide. The ARGUS API provides integration capabilities across cloud-enabled ARGUS solutions.
features:
- description: ARGUS is recognized as the industry standard for CRE investment analysis, taught at 200+ universities worldwide.
  name: Industry Standard Platform
- description: Cloud-based API gateway enabling programmatic extraction and ingestion of data across ARGUS solutions.
  name: ARGUS API Integration
- description: Pre-built connectors for integrating ARGUS with Yardi, MRI, and other property management systems.
  name: ARGUS Connector
- description: All ARGUS solutions available as cloud-based platform via ARGUS Cloud on Microsoft Azure.
  name: Cloud Delivery
- description: ISO/IEC 27001:2022 certified and SOC 2 Type II audited for enterprise security standards.
  name: ISO 27001 Certified
- description: Portfolio-level dashboards, performance analytics, and benchmarking across all ARGUS-managed assets.
  name: ARGUS Intelligence Dashboard
finops:
- name: Argus Finops
  service_category: API
  slug: argus-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/argus.png
integrations:
- description: Pre-built ARGUS Connector for ingesting lease and property management data from Yardi.
  name: Yardi
- description: Integration with MRI property management platform for data synchronization.
  name: MRI Software
- description: ARGUS Cloud hosted on Microsoft Azure for cloud delivery and data security.
  name: Microsoft Azure
- description: JLL uses ARGUS across their global real estate asset management operations.
  name: JLL
- description: CBRE relies on ARGUS for valuation and investment analysis services worldwide.
  name: CBRE
- description: Export ARGUS data for visualization in Microsoft Power BI dashboards.
  name: Power BI
layout: provider
modified: '2026-04-19'
name: ARGUS
nav: Providers
network: true
overview: 'ARGUS publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Altus Group, Asset Management, Commercial Real Estate, Fund Management, and Portfolio Management.


  ARGUS''s developer surface includes engineering blog, documentation, getting-started guide, developer portal, support, training material, release notes, and 6 more developer resources.'
plans:
- name: Argus Plans Pricing
  plan_count: 3
  slug: argus-plans-pricing
random_paper: 36
rate_limits:
- limit_count: 5
  name: Argus Rate Limits
  slug: argus-rate-limits
score:
  band: thin
  composite: 35.3
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 0.0
    developer_ergonomics: 34.8
    discoverability: 87.5
    governance: 0.0
    operational_transparency: 57.9
  previous_composite: 35.3
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/argus/refs/heads/main/screenshots/argus-2026-06-20T172427.png
security:
- kind: domain-security
  name: Argus Domain Security
  slug: argus-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: argus
tags:
- Altus Group
- Asset Management
- Commercial Real Estate
- Fund Management
- Portfolio Management
- Real Estate Software
- Valuation
use_cases:
- description: Manage the full commercial real estate investment lifecycle from acquisition underwriting through asset management and disposition.
  name: CRE Investment Lifecycle Management
- description: Monitor portfolio performance across all assets using standardized metrics and industry benchmarking.
  name: Portfolio Analytics and Benchmarking
- description: Integrate ARGUS data with property management, ERP, and analytics platforms via the ARGUS API.
  name: Third-Party System Integration
- description: Model complex real estate fund structures, waterfalls, and investor reporting with ARGUS Taliance.
  name: Fund Management
- description: Assess development project financial viability from initial feasibility through construction completion.
  name: Development Feasibility
website: https://www.altusgroup.com/argus/
---
