---
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
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/santander-us-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.santanderbank.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/santander-bank-na
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.santanderbank.com/online-privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.santanderbank.com/terms-and-conditions
- group: operate
  title: ''
  type: Support
  url: https://www.santanderbank.com/personal/security-center
created: '2026-07-23'
description: 'Santander Bank, N.A. (santanderbank.com) is the US retail and commercial banking subsidiary of Spain''s Banco Santander S.A., headquartered in Boston, Massachusetts. It is a nationally chartered bank (National Association, regulated by the OCC) operating a branch network across the Northeast US (Massachusetts, New Hampshire, Rhode Island, Connecticut, New York, New Jersey, Pennsylvania and Delaware), which positions it as a super-regional bank. Unlike UK and Australian institutions bound by mandated open-banking contracts, and unlike US banks such as Capital One or Chase that publish first-party developer portals, Santander Bank N.A. exposes no public, first-party developer API for its US retail franchise: developer.santanderbank.com does not resolve, and the site publishes no developers/API/open-banking pages. Consumer-permissioned data access in the US is available today through aggregators rather than a direct API — Plaid supports "Santander - Personal" (Assets, Auth, Balance
  and Transactions). Santander''s UK developer portal (developer.santander.co.uk) and the group''s Corporate & Investment Banking API marketplace (apimarket.santandercib.com) are operated by separate legal entities and are not the US retail bank''s surface. This record is an honest identity profile of a super-regional bank whose US open-finance posture is aggregator-mediated, with no documented first-party developer program.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-23'
name: Santander US
nav: Providers
network: true
overview: 'Santander US is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Financial-Services, Banking, United States, Super-Regional Bank, and Retail Banking.


  Santander US''s developer surface includes support and 5 more developer resources.'
random_paper: 19
score:
  band: minimal
  composite: 8.2
  coverage:
    artifact_dirs: 2
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 8.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 17.7
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: domain-security
  name: Santander Us Domain Security
  slug: santander-us-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: santander-us
tags:
- Financial-Services
- Banking
- United States
- Super-Regional Bank
- Retail Banking
- Open Finance
- Data Aggregation
website: https://www.santanderbank.com
---
