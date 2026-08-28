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
  scored_at: '2026-08-26'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/home-trust-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.hometrust.ca/
- group: company
  title: ''
  type: Blog
  url: https://www.hometrust.ca/blog/
- group: company
  title: ''
  type: LinkedIn
  url: https://ca.linkedin.com/company/hometrustco
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hometrust.ca/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.hometrust.ca/disclaimer/
created: '2026-07-23'
description: 'Home Trust Company is a federally regulated Canadian trust company founded in 1977 and headquartered in Toronto, and the principal operating subsidiary of Home Capital Group. Home Capital was taken private by Smith Financial Corporation (Stephen Smith) in 2023, and the group now spans Home Trust, Home Bank (a Schedule I bank), Fairstone Bank, and the Oaken Financial deposit brand, positioning itself as one of Canada''s leading alternative (non-prime) lenders. Its products include residential and commercial mortgages, reverse mortgages, Equityline, Preferred and Secured Visa credit cards, and Oaken GIC and high-interest savings deposits. Home Trust operates no public developer portal or first-party API: developer.hometrust.ca and api.hometrust.ca do not resolve (DNS NXDOMAIN), no downloadable OpenAPI/Swagger is published, and no Interac e-Transfer or Payments Canada Real-Time Rail (RTR) API surface is documented. Canada''s federal Consumer-Driven Banking (open-banking) framework
  is legislated (Budget 2024 / Fall Economic Statement 2024, FCAC as overseer) but not yet operational, and Home Trust publishes no stated CDB or FDX position; any consumer data access today would be via screen-scraping aggregators such as Flinks or Plaid rather than a first-party API. This is an identity-only record: no public API exists as of July 2026.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-23'
name: Home Trust
nav: Providers
network: true
overview: 'Home Trust is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Financial-Services, Banking, Canada, Trust Company, and Alternative Lending.


  Home Trust''s developer surface includes engineering blog and 5 more developer resources.'
random_paper: 19
score:
  band: minimal
  composite: 7.7
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 7.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 17.7
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/home-trust/refs/heads/main/screenshots/home-trust-2026-07-25T221334.png
security:
- kind: domain-security
  name: Home Trust Domain Security
  slug: home-trust-domain-security
  summary_line: TLSv1.3 · DMARC
slug: home-trust
tags:
- Financial-Services
- Banking
- Canada
- Trust Company
- Alternative Lending
- Mortgages
- Credit Cards
- Deposits
website: https://www.hometrust.ca/
---
