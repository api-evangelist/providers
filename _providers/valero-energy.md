---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
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
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-10'
api_count: 1
apis:
- description: 'Valero Energy Corporation SEC filings and financial data available through the SEC EDGAR system. Includes 10-K, 10-Q, earnings releases, and other regulatory filings. Accessible via the SEC EDGAR API '
  name: Valero Energy SEC EDGAR Data
  slug: sec-edgar
artifact_total: 11
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/valero-energy-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/valero-energy
- group: company
  title: ''
  type: Website
  url: https://www.valero.com/
- group: company
  title: ''
  type: InvestorRelations
  url: https://investorvalero.com/
- group: other
  title: ''
  type: SECEdgar
  url: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001035002
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.valero.com/privacy-policy
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/valero-energy/refs/heads/main/vocabulary/valero-energy-vocabulary.yml
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/valero-energy/refs/heads/main/json-schema/valero-energy-refinery-schema.json
created: '2026-03-21'
description: Valero Energy Corporation is the world's largest independent petroleum refiner and a leading producer of low-carbon transportation fuels. Headquartered in San Antonio, Texas, Valero operates 14 petroleum refineries with 3 million barrels per day capacity, 12 ethanol plants, and renewable diesel production facilities across the US, Canada, and UK. The company trades on NYSE as VLO and is a Fortune 100 company.
examples:
- key_count: 2
  name: Valero Energy Refinery Example
  slug: valero-energy-refinery-example
finops:
- name: Valero Energy Finops
  service_category: Energy
  slug: valero-energy-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/valero-energy.png
json_schemas:
- name: Valero Energy Financial Result
  property_count: 8
  slug: valero-energy-financial
- name: Valero Refinery
  property_count: 7
  slug: valero-energy-refinery
json_structures:
- name: Valero Energy Refinery Structure
  property_count: 0
  slug: valero-energy-refinery-structure
jsonld:
- class_count: 0
  name: Valero Energy Context
  property_count: 3
  slug: valero-energy-context
layout: provider
modified: '2026-07-25'
name: Valero Energy
nav: Providers
network: true
overview: 'Valero Energy publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Energy, Petroleum, Refining, Renewable Fuels, and Fortune 100.


  The Valero Energy catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
plans:
- name: Valero Energy Plans Pricing
  plan_count: 1
  slug: valero-energy-plans-pricing
press:
- date: '2026-05-25'
  title: Valero Energy Corporation - Startups
  url: https://www.startuphub.ai/startups/valero-energy
- date: '2026-05-25'
  title: 'Valero AI Initiatives for 2025: Key Projects, Strategies and ...'
  url: https://enkiai.com/valero-ai-initiatives-for-2025-key-projects-strategies-and-partnerships/
- date: '2026-05-25'
  title: AI at Valero Energy | rudyl.ai
  url: https://www.rudyl.ai/ai-research/companies/valero-energy
- date: '2026-05-25'
  title: Valero Energy Corporation ($VLO)
  url: https://trendspider.com/learning-center/valero-energy-corporation-vlo/
- date: '2026-05-25'
  title: Valero to run refineries up to 95% of capacity in Q2 2026, ...
  url: https://www.reuters.com/business/energy/valero-run-refineries-up-95-capacity-q2-2026-conf-call-2026-04-30/
random_paper: 68
rate_limits:
- limit_count: 1
  name: Valero Energy Rate Limits
  slug: valero-energy-rate-limits
rules:
- name: Valero Energy API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: valero-energy-jsonschema-spectral-rules
score:
  band: emerging
  composite: 25.9
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 8.1
    developer_ergonomics: 0.0
    discoverability: 59.3
    governance: 68.8
    operational_transparency: 21.1
  previous_composite: 25.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 20.3
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/valero-energy/refs/heads/main/screenshots/valero-energy-2026-06-20T200749.png
security:
- kind: domain-security
  name: Valero Energy Domain Security
  slug: valero-energy-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: valero-energy
tags:
- Energy
- Petroleum
- Refining
- Renewable Fuels
- Fortune 100
- Ethanol
- Renewable Diesel
website: https://www.valero.com/
---
