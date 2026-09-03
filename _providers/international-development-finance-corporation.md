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
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: DFC publishes transaction-level data on its development finance activities including loans, political risk insurance, and equity investments. Data is released as downloadable CSV/Excel datasets rather
  name: DFC Transaction Data
  slug: dfc-transaction-data
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/international-development-finance-corporation-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/dfcgov
- group: company
  title: ''
  type: Website
  url: https://www.dfc.gov
- group: other
  title: ''
  type: Open Data
  url: https://www.dfc.gov/our-impact/dfc-transaction-data
- group: operate
  title: ''
  type: Contact
  url: https://www.dfc.gov/who-we-are/contact-us
created: '2024-12-03'
description: The United States International Development Finance Corporation (DFC) is a development finance institution and agency of the United States federal government. DFC invests in development projects primarily in lower and middle-income countries, providing secure private investment opportunities for emerging markets. DFC does not currently expose a public developer API portal; transaction-level data is published as downloadable datasets.
finops:
- name: International Development Finance Corporation Finops
  service_category: API
  slug: international-development-finance-corporation-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/international-development-finance-corporation.png
layout: provider
modified: '2026-04-28'
name: International Development Finance Corporation
nav: Providers
network: true
overview: International Development Finance Corporation publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Development Finance, Emerging Markets, Federal-Government, Investment, and Open Data.
plans:
- name: International Development Finance Corporation Plans Pricing
  plan_count: 3
  slug: international-development-finance-corporation-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 5
  name: International Development Finance Corporation Rate Limits
  slug: international-development-finance-corporation-rate-limits
score:
  band: minimal
  composite: 10.4
  coverage:
    artifact_dirs: 6
    catalog_gap: 74.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 10.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/international-development-finance-corporation/refs/heads/main/screenshots/international-development-finance-corporation-2026-06-20T183455.png
security:
- kind: domain-security
  name: International Development Finance Corporation Domain Security
  slug: international-development-finance-corporation-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: international-development-finance-corporation
tags:
- Development Finance
- Emerging Markets
- Federal-Government
- Investment
- Open Data
website: https://www.dfc.gov
---
