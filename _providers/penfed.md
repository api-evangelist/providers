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
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/penfed-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.penfed.org/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.penfed.org/
- group: start
  title: ''
  type: Login
  url: https://www.penfed.org/login
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.penfed.org/privacy-policy
created: '2026-07-23'
description: 'PenFed Credit Union (Pentagon Federal Credit Union), founded in 1935 and headquartered in McLean, Virginia, is a federally chartered credit union regulated by the National Credit Union Administration (NCUA) and one of the largest credit unions in the United States, with roughly 2.9 million members and tens of billions of dollars in assets. It is a not-for-profit, member-owned financial cooperative that originally served the U.S. military and defense community and now offers open membership, providing mortgages, auto loans, credit cards, personal loans, and deposit accounts. On the open-finance front, PenFed runs an internal API-management practice — MuleSoft/Anypoint is the backbone of its digital-banking platform and an Apigee-backed developer portal host exists at developer.penfed.org (with an api.penfed.org gateway) — but neither surface is publicly documented or openly reachable: there is no public developer program, no published OpenAPI, and consumer account data is made
  available to members through permissioned third-party aggregators such as Plaid rather than a directly documented FDX or CFPB Section 1033 data-access API.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-23'
name: PenFed Credit Union
nav: Providers
network: true
overview: PenFed Credit Union is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Financial-Services, Banking, Credit Union, United States, and Open Finance.
random_paper: 17
score:
  band: minimal
  composite: 5.2
  coverage:
    artifact_dirs: 1
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 11.8
    commercial_clarity: 11.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 10.1
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Penfed Domain Security
  slug: penfed-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: penfed
tags:
- Financial-Services
- Banking
- Credit Union
- United States
- Open Finance
- Data Aggregation
website: https://www.penfed.org/
---
