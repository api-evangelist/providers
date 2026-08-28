---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
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
    auth_clarity: bearer
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
  score: 5.0
  scored_at: '2026-08-26'
api_count: 0
artifact_total: 19
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/allianz-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/allianz-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/allianz
- group: company
  title: ''
  type: Website
  url: https://www.allianz.com
- group: other
  title: ''
  type: AssetManagement
  url: https://www.allianzgi.com/
- group: other
  title: ''
  type: TravelInsurance
  url: https://www.allianztravelinsurance.com/
- group: company
  title: ''
  type: Partners
  url: https://www.allianz-partners.com/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/allianz
- group: auth
  title: ''
  type: Authentication
  url: ''
- group: auth
  title: ''
  type: Compliance
  url: ''
created: '2026-05-05'
description: A German multinational financial services company and one of the world's largest insurance and asset management firms. Operates in over 70 countries providing insurance, banking, and investment products.
features:
- description: Property & casualty insurance (motor, home, business) underwritten by Allianz operating entities across 70+ countries.
  name: P&C Insurance
- description: Life, health, and pensions underwriting under Allianz Lebensversicherung and equivalent regional entities.
  name: Life & Health Insurance
- description: Asset management through Allianz Global Investors (AllianzGI) and PIMCO, two of the largest active managers globally.
  name: Asset Management
- description: Travel insurance and global emergency assistance delivered by Allianz Partners / Allianz Travel.
  name: Travel Insurance and Assistance
- description: Allianz Commercial / AGCS provides specialty corporate and large-account property, marine, aviation, financial-lines, and energy coverage.
  name: Specialty Lines
finops:
- name: Allianz Finops
  service_category: Insurance / Financial Services
  slug: allianz-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/allianz.png
integrations:
- description: PIMCO is the larger of Allianz's two asset-management subsidiaries, distributing global fixed-income and multi-asset strategies.
  name: PIMCO
- description: AllianzGI is Allianz's active asset-management arm covering equities, fixed income, and multi-asset.
  name: Allianz Global Investors
- description: Allianz Partners delivers travel insurance, assistance, automotive, and health-and-life partner programs to other brands.
  name: Allianz Partners
- description: Specialty / corporate insurer for large accounts within the Allianz Group.
  name: Allianz Commercial / AGCS
- description: Allianz Partners powers white-label embedded insurance with airlines, banks, travel platforms, and consumer brands.
  name: Embedded Insurance Partners
layout: provider
modified: '2026-05-16'
name: Allianz
nav: Providers
network: true
overview: 'Allianz is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, Financial, and Asset Management.


  Allianz''s developer surface includes GitHub presence, authentication, and 6 more developer resources.'
plans:
- name: Allianz Plans Pricing
  plan_count: 1
  slug: allianz-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 1
  name: Allianz Rate Limits
  slug: allianz-rate-limits
score:
  band: emerging
  composite: 18.4
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 40.7
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 18.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 34.8
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/allianz/refs/heads/main/screenshots/allianz-2026-06-20T171535.png
security:
- kind: domain-security
  name: Allianz Domain Security
  slug: allianz-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Allianz Vulnerability Disclosure
  slug: allianz-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: allianz
tags:
- Insurance
- Financial
- Asset Management
use_cases:
- description: Retail P&C, life, and health policies sold through agents, banks, brokers, and direct digital channels in each market.
  name: Retail Insurance Distribution
- description: Large-account property, casualty, marine, aviation, and financial-lines placements via Allianz Commercial.
  name: Corporate Risk Transfer
- description: Global travel-insurance, medical-assistance, and claims handling through Allianz Partners.
  name: Travel Assistance and Claims
- description: Active asset management for institutional and retail investors through AllianzGI and PIMCO.
  name: Asset Management for Institutions and Individuals
website: https://www.allianz.com
---
