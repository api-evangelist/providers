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
api_count: 2
apis:
- description: BNP Paribas Corporate and Institutional Banking (CIB) API platform provides programmatic access to capital markets, payment services, securities services, advisory, finance, and treasury solutions for
  name: BNP Paribas CIB API
  slug: bnp-paribas-cib-api
- description: 'BNP Paribas Open Banking APIs provide PSD2-compliant payment services and account information access including check availability of funds for card-based payment instrument issuers, SEPA direct debit '
  name: BNP Paribas Open Banking API
  slug: bnp-paribas-open-banking-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bnp-paribas-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bnpparibas
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bnp-paribas
- group: company
  title: ''
  type: Website
  url: https://www.bnpparibas.com
- group: start
  title: ''
  type: Portal
  url: https://developers.cib.bnpparibas.com/api-catalog
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.cib.bnpparibas.com/how-to
- group: start
  title: ''
  type: OpenBankingPortal
  url: https://apistore.bnpparibas
- group: operate
  title: ''
  type: FAQ
  url: https://developers.cib.bnpparibas.com/faq
- group: company
  title: ''
  type: Blog
  url: https://developers.cib.bnpparibas.com/rss.xml
created: '2025-02-08'
description: BNP Paribas is a leading international banking group providing a wide range of financial services to individuals, businesses, and institutions worldwide. The company offers APIs through its CIB Developer Portal covering capital markets, payment services, securities services, and open banking integrations for corporate and institutional clients.
finops:
- name: Bnp Paribas Finops
  service_category: API
  slug: bnp-paribas-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bnp-paribas.png
layout: provider
modified: '2026-04-21'
name: BNP Paribas
nav: Providers
network: true
overview: 'BNP Paribas publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Banking, Finance, Payments, Capital Markets, and Open Banking.


  BNP Paribas'' developer surface includes developer portal, getting-started guide, FAQ, engineering blog, and 5 more developer resources.'
plans:
- name: Bnp Paribas Plans Pricing
  plan_count: 3
  slug: bnp-paribas-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 5
  name: Bnp Paribas Rate Limits
  slug: bnp-paribas-rate-limits
score:
  band: emerging
  composite: 11.2
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
    developer_ergonomics: 21.4
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 11.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 7.6
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bnp-paribas/refs/heads/main/screenshots/bnp-paribas-2026-06-20T173543.png
security:
- kind: domain-security
  name: Bnp Paribas Domain Security
  slug: bnp-paribas-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: bnp-paribas
tags:
- Banking
- Finance
- Payments
- Capital Markets
- Open Banking
website: https://www.bnpparibas.com
---
