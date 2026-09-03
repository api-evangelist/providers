---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
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
    error_semantics: documented
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
  score: 7.9
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: REST over HTTPS with JSON request/response (CSV supported on specific bulk-load endpoints) for integrating Guidewheel with external ERP, MES and CMMS systems. Covers devices and equipment details, min
  name: Guidewheel REST API v1
  slug: rest-api-v1
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.guidewheel.com/
- group: docs
  title: ''
  type: Documentation
  url: https://support.guidewheel.app/en/
- group: docs
  title: ''
  type: APIReference
  url: https://support.guidewheel.app/en/articles/15696169-guidewheel-api-cmms-erp-integration-guide
- group: start
  title: ''
  type: GettingStarted
  url: https://support.guidewheel.app/en/collections/1677909-getting-started
- group: operate
  title: ''
  type: Support
  url: https://support.guidewheel.app/en/articles/10185853-how-to-reach-guidewheel-support
- group: company
  title: ''
  type: Blog
  url: https://www.guidewheel.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.guidewheel.com/pricing
- group: start
  title: ''
  type: Login
  url: https://app.guidewheel.app/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.guidewheel.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.guidewheel.com/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://guidewheel.statuspage.io/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/guidewheel-changelog.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/guidewheel-authentication.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/guidewheel-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/guidewheel-plans.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/guidewheel-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/guidewheel-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/guidewheel-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/guidewheel-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/guidewheel-sandbox.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/guidewheel-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/guidewheel-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/guidewheel-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/guidewheel-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/guidewheel/
created: '2026-08-01'
description: Guidewheel is a FactoryOps platform for manufacturing. Non-invasive, clip-on current sensors attach to any machine's power leads — regardless of age, make or model — and stream a real-time heartbeat of machine state (running, idle, down) over cellular, with no PLC, SCADA or plant Wi-Fi access required. The platform turns that signal into real-time OEE, downtime categorization and reasoning, Pareto analysis, cycle-time tracking, scrap tracking, shift and plant reporting, and alerting. Guidewheel exposes a REST/JSON API under /api/v1 for CMMS and ERP integration — devices, telemetry, uptime and load states, energy, issues, production entries, SKUs, tags, device lists, plants, shifts and scrap — authenticated with a company-scoped API key in the x-api-key header. It also ships native SAP integration plus Oracle, Epicor, Microsoft Dynamics, Power BI and MaintainX connections via Workato.
image: https://cdn.prod.website-files.com/680ab1b52d269fa62a84d433/68a74e2071f0ccbc78d31733_guidewheel.jpg
layout: provider
modified: '2026-08-01'
name: Guidewheel
nav: Providers
network: true
overview: 'Guidewheel publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Manufacturing, Industrial IoT, Machine Monitoring, and OEE.


  Guidewheel''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, changelog, and 18 more developer resources.'
plans:
- name: Guidewheel Plans
  plan_count: 1
  slug: guidewheel-plans
random_paper: 9
rate_limits:
- limit_count: 2
  name: Guidewheel Rate Limits
  slug: guidewheel-rate-limits
score:
  band: developing
  composite: 39.9
  coverage:
    artifact_dirs: 15
    catalog_gap: 62.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 59.2
    commercial_clarity: 59.2
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 54.8
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 52.6
  previous_composite: 39.9
  provenance:
    conformance: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 33.8
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/guidewheel/refs/heads/main/screenshots/guidewheel-2026-08-07T165856.png
security:
- kind: authentication
  name: Guidewheel Authentication
  slug: guidewheel-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Guidewheel Domain Security
  slug: guidewheel-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: guidewheel
tags:
- Company
- Manufacturing
- Industrial IoT
- Machine Monitoring
- OEE
- FactoryOps
- Predictive Maintenance
- Energy
- Sensors
- Telemetry
website: https://www.guidewheel.com/
---
