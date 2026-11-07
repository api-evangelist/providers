---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - finops
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.6
  scored_at: '2026-11-06'
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
artifact_total: 28
common:
- group: other
  href: https://artifacts.apis.io/argus/hosts/argus-hosts.yml
  title: ''
  type: Hosts
  url: hosts/argus-hosts.yml
- group: other
  href: https://artifacts.apis.io/argus/vendors/argus-vendors.yml
  title: ''
  type: Vendors
  url: vendors/argus-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.altusgroup.com/about-us/newsroom/
- group: start
  title: ''
  type: Login
  url: https://www.altusgroup.com/login/
- group: commercial
  href: https://artifacts.apis.io/argus/finops/argus-finops.yml
  title: ''
  type: FinOps
  url: finops/argus-finops.yml
- group: auth
  href: https://artifacts.apis.io/argus/security/argus-domain-security.yml
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
  type: PrivacyPolicy
  url: https://www.altusgroup.com/legal/privacy-policy/
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://www.altusgroup.com/argus/downloads/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AltusGroup
- group: auth
  title: ''
  type: Compliance
  url: https://www.altusgroup.com/trust-center/
- group: auth
  href: https://artifacts.apis.io/argus/security/argus-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/argus-trust-center.yml
- group: agent
  href: https://artifacts.apis.io/argus/well-known/argus-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/argus-well-known.yml
- group: auth
  href: https://artifacts.apis.io/argus/authentication/argus-authentication.yml
  title: ''
  type: Authentication
  url: authentication/argus-authentication.yml
- group: design
  href: https://artifacts.apis.io/argus/conformance/argus-conformance.yml
  title: ''
  type: Conformance
  url: conformance/argus-conformance.yml
- group: design
  href: https://artifacts.apis.io/argus/lifecycle/argus-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/argus-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/argus/lifecycle/argus-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/argus-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/argus/changelog/argus-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/argus-changelog.yml
- group: commercial
  href: https://artifacts.apis.io/argus/plans/argus-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/argus-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/argus/rate-limits/argus-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/argus-rate-limits.yml
coverage:
  checked: '2026-10-20'
  detail: The ARGUS API is described only in product marketing; its documentation link resolves to the downloads page, and the ARGUS Intelligence Platform host (platform.altusintelligence.com) serves an SPA shell for every path while a POST to /mcp is refused 403 at CloudFront, so no public contract exists.
  evidence:
  - status: 308
    url: https://www.altusgroup.com/argus/argus-api/
  - status: 403
    url: https://platform.altusintelligence.com/mcp
  - status: 404
    url: https://www.altusgroup.com/llms.txt
  reason: customer-only-docs
  state: gated
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
- has_sources: false
  method: generated
  name: Argus Finops
  primary_unit: request
  service_category: API
  slug: argus-finops
  template: true
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
modified: '2026-09-14'
name: ARGUS
nav: Providers
network: true
overview: 'ARGUS is listed with 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Altus Group, Asset Management, Commercial Real Estate, Fund Management, and Portfolio Management.


  ARGUS''s developer surface includes engineering blog, documentation, getting-started guide, developer portal, support, training material, release notes, and 20 more developer resources.'
plans:
- name: Argus Plans Pricing
  plan_count: 0
  slug: argus-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Argus Rate Limits
  slug: argus-rate-limits
score:
  band: thin
  composite: 30.1
  coverage:
    artifact_dirs: 18
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.4
  facets:
    access_clarity: 32.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 50.0
    discoverability: 63.4
    operational_transparency: 26.3
  previous_composite: 31.5
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 25.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/argus/argus-2026-06-20T172427.png
security:
- kind: authentication
  name: Argus Authentication
  slug: argus-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Argus Domain Security
  slug: argus-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Argus Trust Center
  slug: argus-trust-center
  summary_line: ISO/IEC 27001 (Altus Group), SOC 3 Type 2 (ARGUS Cloud (2025)), SOC 3 Type 2 (ARGUS Intelligence Platform (2025)), SOC 3 report (Altus Finance Active / Fairways (2024)), SOC 2 Type II (Altus Group)
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
