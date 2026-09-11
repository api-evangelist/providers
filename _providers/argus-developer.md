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
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
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
  score: 17.6
  scored_at: '2026-09-10'
api_count: 1
apis:
- description: 'Altus Group publishes no public API, OpenAPI or developer program for ARGUS Developer. Probed 2026-09-06: no spec on any Altus host, no developer or docs subdomain resolves, and cloud.altusplatform.co'
  name: ARGUS Developer API
  slug: argus-developer-api
artifact_total: 23
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/argus-developer-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.altusgroup.com/solutions/argus-developer/
- group: company
  title: ''
  type: Blog
  url: https://www.altusgroup.com/insights/
- group: docs
  title: ''
  type: Documentation
  url: https://www.altusgroup.com/argus/downloads/argus-developer/
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
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.altusgroup.com/legal/privacy-policy/
- group: learn
  title: ''
  type: Training
  url: https://www.altusgroup.com/argus/training/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AltusGroup
- group: agent
  title: ''
  type: WellKnown
  url: well-known/argus-developer-well-known.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/argus-developer-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: security/argus-developer-trust-center.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/argus-developer-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/argus-developer-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/argus-developer-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/argus-developer-changelog.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/argus-developer-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/argus-developer-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/argus-developer-rate-limits.yml
created: '2024-01-15'
description: ARGUS Developer is a cloud-based real estate development software platform by Altus Group that enables property developers, appraisers, consultants, and financiers to manage complex, multi-stage development projects from initial feasibility through delivery. It provides development pro forma modeling, residual land value analysis, scenario comparison, cash flow forecasting, and professional reporting. Part of the ARGUS Intelligence Platform by Altus Group, the industry-standard suite for commercial real estate.
features:
- description: Configurable financial modeling for multi-stage development projects with support for land acquisition, construction, and sales phases.
  name: Development Pro Forma
- description: Evaluate acquisition and disposal values to determine maximum land bid prices for development sites.
  name: Residual Land Value Analysis
- description: Compare multiple development scenarios side by side to assess risk and optimize project outcomes.
  name: Scenario Analysis
- description: Detailed project cash flow modeling with budget-to-actual tracking for active development projects.
  name: Cash Flow Forecasting
- description: Assess risk by varying costs, revenues, timing, and interest rates to stress-test project assumptions.
  name: Sensitivity Analysis
- description: Model debt, equity, and joint venture funding arrangements with customizable terms.
  name: Flexible Funding Structures
- description: Generate 60+ detailed reports for internal stakeholders and investor communication.
  name: Professional Reporting
- description: Cloud-based platform accessible via ARGUS Cloud, reducing IT overhead.
  name: Cloud Delivery
finops:
- name: Argus Developer Finops
  service_category: API
  slug: argus-developer-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/argus-developer.png
integrations:
- description: Integrate with ARGUS Enterprise for seamless transition from development to stabilized asset management.
  name: ARGUS Enterprise
- description: Connected to the ARGUS Intelligence Platform for portfolio-level analytics and reporting.
  name: ARGUS Intelligence Platform
- description: Integrate lease and property management data from Yardi into development models.
  name: Yardi
- description: Connect MRI property management data with development financial models.
  name: MRI Software
layout: provider
modified: '2026-09-06'
name: ARGUS Developer
nav: Providers
network: true
overview: 'ARGUS Developer publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Altus Group, Commercial Real Estate, Development, Feasibility Analysis, and Real-Estate.


  ARGUS Developer''s developer surface includes engineering blog, documentation, getting-started guide, developer portal, support, training material, changelog, and 13 more developer resources.'
plans:
- name: Argus Developer Plans Pricing
  plan_count: 0
  slug: argus-developer-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Argus Developer Rate Limits
  slug: argus-developer-rate-limits
score:
  band: thin
  composite: 26.7
  coverage:
    artifact_dirs: 11
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 38.1
    discoverability: 66.7
    governance: 18.2
    operational_transparency: 26.3
  previous_composite: 26.7
  provenance:
    conformance: first-party
  schema_version: 0.20.0
  scored_at: '2026-09-10'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/argus-developer/refs/heads/main/screenshots/argus-developer-2026-06-20T172427.png
security:
- kind: domain-security
  name: Argus Developer Domain Security
  slug: argus-developer-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Argus Developer Trust Center
  slug: argus-developer-trust-center
  summary_line: SOC 3 Type 2, SOC 3 Type 2, SOC 3 Type 2, ISO/IEC 27001, SOC 2 Type II
slug: argus-developer
tags:
- Altus Group
- Commercial Real Estate
- Development
- Feasibility Analysis
- Real-Estate
use_cases:
- description: Assess the financial viability of new development projects before committing capital.
  name: Development Feasibility
- description: Calculate residual land values to determine competitive and profitable bid prices.
  name: Land Acquisition Analysis
- description: Model financing structures and present investment cases to lenders and equity partners.
  name: Development Finance
- description: Track and manage multiple active development projects across a real estate portfolio.
  name: Portfolio Development Management
- description: Generate professional reports for investors, lenders, and boards on development project performance.
  name: Investor Reporting
website: https://www.altusgroup.com/solutions/argus-developer/
---
