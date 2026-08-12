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
  scored_at: '2026-08-11'
api_count: 3
apis:
- description: 'The BEP U.S. Currency Reader Program provides free currency readers to blind and visually impaired individuals in the United States, enabling them to identify Federal Reserve Note denominations using '
  name: BEP U.S. Currency Reader Program
  slug: bep-currency-reader-program
- description: The BEP redeems severely damaged or mutilated Federal Reserve Notes as a free public service. Citizens can submit damaged currency for examination and potential redemption.
  name: BEP Mutilated Currency Redemption
  slug: bep-mutilated-currency-redemption
- description: BEP publishes currency production figures, annual reports, and historical data about Federal Reserve Note printing. Data is available via data.gov for programmatic access.
  name: BEP Data and Publications
  slug: bep-data-catalog
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bureau-of-engraving-and-printing-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bureau-of-engraving-and-printing
- group: company
  title: ''
  type: Website
  url: https://www.bep.gov/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bep.gov/privacy-policy
- group: start
  title: ''
  type: Data Portal
  url: https://catalog.data.gov/dataset?organization=bep-gov
- group: other
  title: ''
  type: Currency Features
  url: https://www.bep.gov/currency/current-currency-features
- group: company
  title: ''
  type: About
  url: https://www.bep.gov/about
created: '2024-11-25'
description: The Bureau of Engraving and Printing (BEP) is an agency of the U.S. Department of the Treasury that designs and produces U.S. currency (Federal Reserve Notes), postage stamps, and other official U.S. government security documents. BEP offers a U.S. Currency Reader Program for the visually impaired and provides a mutilated currency redemption service.
finops:
- name: Bureau Of Engraving And Printing Finops
  service_category: API
  slug: bureau-of-engraving-and-printing-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bureau-of-engraving-and-printing.png
layout: provider
modified: '2026-04-21'
name: Bureau of Engraving and Printing
nav: Providers
network: true
overview: Bureau of Engraving and Printing publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Currency, Engraving, Federal Government, Money, and Printing.
plans:
- name: Bureau Of Engraving And Printing Plans Pricing
  plan_count: 3
  slug: bureau-of-engraving-and-printing-plans-pricing
random_paper: 48
rate_limits:
- limit_count: 5
  name: Bureau Of Engraving And Printing Rate Limits
  slug: bureau-of-engraving-and-printing-rate-limits
score:
  band: emerging
  composite: 13.6
  delta: -7.0
  facets:
    commercial_clarity: 26.3
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 20.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 18.5
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/bureau-of-engraving-and-printing/refs/heads/main/screenshots/bureau-of-engraving-and-printing-2026-06-20T173806.png
security:
- kind: domain-security
  name: Bureau Of Engraving And Printing Domain Security
  slug: bureau-of-engraving-and-printing-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: bureau-of-engraving-and-printing
tags:
- Currency
- Engraving
- Federal Government
- Money
- Printing
- Security Printing
website: https://www.bep.gov/
---
