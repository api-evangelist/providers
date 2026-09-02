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
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: The BP API Marketplace is a developer portal providing access to BP's digital APIs and services. Features include API discovery and browsing, a testing playground, documentation and tutorials, API spe
  name: BP API Marketplace
  slug: bp-api-marketplace
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bp-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bp
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bp
- group: company
  title: ''
  type: Website
  url: https://www.bp.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.bp.com/hub
- group: company
  title: ''
  type: InvestorRelations
  url: https://www.bp.com/en/global/corporate/investors.html
- group: other
  title: ''
  type: Sustainability
  url: https://www.bp.com/en/global/corporate/sustainability.html
created: '2025-03-01'
description: BP (British Petroleum) is one of the world's largest integrated energy companies, operating in over 70 countries across oil and gas exploration, production, refining, distribution, marketing, petrochemicals, power generation, and renewable energy. BP operates an API Marketplace developer portal (developer.bp.com) enabling seamless integration with BP's digital services, providing API discovery, testing playgrounds, documentation, and billing management for energy sector integrations.
finops:
- name: Bp Finops
  service_category: API
  slug: bp-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bp.png
layout: provider
modified: '2026-04-21'
name: BP
nav: Providers
network: true
overview: BP publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Energy, Oil, Gas, Renewables, and Developer Platform.
plans:
- name: Bp Plans Pricing
  plan_count: 3
  slug: bp-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 5
  name: Bp Rate Limits
  slug: bp-rate-limits
score:
  band: minimal
  composite: 8.8
  coverage:
    artifact_dirs: 5
    catalog_gap: 74.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 8.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 8.1
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bp/refs/heads/main/screenshots/bp-2026-07-25T203719.png
security:
- kind: domain-security
  name: Bp Domain Security
  slug: bp-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bp
tags:
- Energy
- Oil
- Gas
- Renewables
- Developer Platform
website: https://www.bp.com
---
