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
  scored_at: '2026-08-12'
api_count: 1
apis:
- description: Public-facing presence of the U.S. Election Assistance Commission. The EAC publishes Election Administration and Voting Survey (EAVS) datasets, codebooks, voluntary voting system guidelines, voter lis
  name: Election Assistance Commission
  slug: eac
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/election-assistance-commission-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/u-s-election-assistance-commission
- group: company
  title: ''
  type: Website
  url: https://www.eac.gov
- group: other
  title: ''
  type: ResearchAndData
  url: https://www.eac.gov/research-and-data
- group: other
  title: ''
  type: Datasets
  url: https://www.eac.gov/research-and-data/studies-and-reports
- group: other
  title: ''
  type: Standards
  url: https://www.eac.gov/voting-equipment/voluntary-voting-system-guidelines
- group: other
  title: ''
  type: RSS
  url: https://www.eac.gov/rss.xml
- group: operate
  title: ''
  type: Contact
  url: https://www.eac.gov/contact_us
created: '2024-12-03'
description: The U.S. Election Assistance Commission (EAC) was established by the Help America Vote Act of 2002 (HAVA). The EAC is an independent, bipartisan commission charged with developing guidance to meet HAVA requirements, adopting voluntary voting system guidelines, and serving as a national clearinghouse of information on election administration. The EAC also accredits testing laboratories, certifies voting systems, and audits the use of HAVA funds. The EAC publishes the Election Administration and Voting Survey (EAVS) datasets and operates an RSS news feed; it does not publish a formal developer API.
finops:
- name: Election Assistance Commission Finops
  service_category: API
  slug: election-assistance-commission-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/election-assistance-commission.png
layout: provider
modified: '2026-04-28'
name: Election Assistance Commission
nav: Providers
network: true
overview: Election Assistance Commission publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Federal Government, Elections, Voting, and Open Data.
plans:
- name: Election Assistance Commission Plans Pricing
  plan_count: 3
  slug: election-assistance-commission-plans-pricing
random_paper: 100
rate_limits:
- limit_count: 5
  name: Election Assistance Commission Rate Limits
  slug: election-assistance-commission-rate-limits
score:
  band: minimal
  composite: 9.5
  delta: 0.0
  facets:
    commercial_clarity: 15.8
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 9.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/election-assistance-commission/refs/heads/main/screenshots/election-assistance-commission-2026-06-20T180552.png
security:
- kind: domain-security
  name: Election Assistance Commission Domain Security
  slug: election-assistance-commission-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: election-assistance-commission
tags:
- Federal Government
- Elections
- Voting
- Open Data
website: https://www.eac.gov
---
