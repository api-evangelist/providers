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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fincompare-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://fincompare.de/
- group: start
  title: ''
  type: SignUp
  url: https://anfrage.fincompare.de
- group: start
  title: ''
  type: Login
  url: https://app.fincompare.de/account/login
- group: operate
  title: ''
  type: Support
  url: https://fincompare.de/faqs
- group: commercial
  title: ''
  type: TermsOfService
  url: https://fincompare.de/agb
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://fincompare.de/datenschutz
created: '2026-07-17'
description: Fincompare (now operating under the Fynbiz brand alongside Compeon) is a Berlin-based digital financing marketplace for small and medium-sized enterprises. Founded in 2017, the platform lets businesses request, compare, and close financing offers from 100+ banks and alternative lenders in one place, covering business loans, leasing, factoring, goods and warehouse financing, real-estate financing, and revenue-based financing. Fincompare connects lenders such as ING, VR Smart Finanz, and iwoca directly through bank API integrations to automate credit decisions. The company was acquired by a consortium of DZ Bank, several Volksbanken, and Atruvia in 2021. Fincompare operates a customer-facing SME financing product; it does not publish a public developer API or documentation surface.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fincompare.png
layout: provider
modified: '2026-07-19'
name: Fincompare
nav: Providers
network: true
overview: 'Fincompare is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Financing, SME Lending, Fintech, and Loans.


  Fincompare''s developer surface includes signup flow, support, and 5 more developer resources.'
random_paper: 10
score:
  band: minimal
  composite: 10.8
  coverage:
    artifact_dirs: 2
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 10.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 17.7
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fincompare/refs/heads/main/screenshots/fincompare-2026-07-25T214508.png
security:
- kind: domain-security
  name: Fincompare Domain Security
  slug: fincompare-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: fincompare
tags:
- Company
- Financing
- SME Lending
- Fintech
- Loans
- Comparison Marketplace
- Banking
- Factoring
- Leasing
- Germany
website: https://fincompare.de/
---
