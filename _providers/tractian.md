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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-24'
api_count: 1
apis:
- description: REST API behind the Tractian platform, used for ERP, BI, and business-system integrations alongside native SQL access and prebuilt connectors. The API host is live (public health endpoint reporting v1
  name: Tractian Platform API
  slug: tractian-platform-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tractian-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tractian.com/en
- group: company
  title: ''
  type: Blog
  url: https://tractian.com/en/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://tractian.com/en/blog/categories/releases
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/tractian-changelog.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tractian
- group: operate
  title: ''
  type: Support
  url: https://tractian.com/en/contact
- group: commercial
  title: ''
  type: Pricing
  url: https://tractian.com/en/solutions/cmms/pricing
- group: start
  title: ''
  type: Login
  url: https://app.tractian.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tractian.com/en/master-license
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tractian.com/en/policies/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.tractian.com
- group: commercial
  title: ''
  type: ServiceLevelAgreement
  url: https://tractian.com/en/service-level-agreement
- group: auth
  title: ''
  type: TrustCenter
  url: security/tractian-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.tractian.com/
- group: design
  title: ''
  type: Conformance
  url: conformance/tractian-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tractian-lifecycle.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/tractian-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/tractian-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tractian-llms.txt
created: '2026-07-17'
description: Tractian is a machine intelligence company providing condition monitoring, asset performance management, and predictive maintenance for industrial operations. Smart Trac sensors capture real-time vibration, temperature, and energy data over LTE; patented AI analytics auto-diagnose over 75 failure modes, predict failures, and prescribe actions; and the Tractian CMMS manages work orders, spare parts inventory, maintenance scheduling, and maintenance KPI reporting. The platform integrates with ERPs, BI tools, and fleet systems through native SQL access, prebuilt connectors, and REST APIs, and is FedRAMP High authorized, SOC 2 Type II compliant, and ISO 27001 certified.
image: https://avatars.githubusercontent.com/u/63681035
layout: provider
modified: '2026-07-21'
name: Tractian
nav: Providers
network: true
overview: 'Tractian publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Condition Monitoring, Predictive Maintenance, CMMS, Asset Management, and Industrial IoT.


  Tractian''s developer surface includes engineering blog, changelog, support, pricing, and 16 more developer resources.'
random_paper: 14
score:
  band: thin
  composite: 26.3
  delta: 0.0
  facets:
    access_clarity: 53.9
    commercial_clarity: 53.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 26.3
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 32.4
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
security:
- kind: domain-security
  name: Tractian Domain Security
  slug: tractian-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Tractian Trust Center
  slug: tractian-trust-center
  summary_line: FedRAMP High, SOC 2 Type II, ISO 27001
slug: tractian
tags:
- Condition Monitoring
- Predictive Maintenance
- CMMS
- Asset Management
- Industrial IoT
- Sensors
- Energy Monitoring
- Manufacturing
website: https://tractian.com/en
---
