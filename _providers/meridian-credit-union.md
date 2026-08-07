---
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
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-06'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/meridian-credit-union-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.meridiancu.ca/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/meridian-credit-union
- group: operate
  title: ''
  type: Support
  url: https://www.meridiancu.ca/contact-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.meridiancu.ca/about-meridian/privacy-and-security
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.meridiancu.ca/about-meridian/legal/personal-membership-terms-and-conditions
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/meridian-credit-union-llms.txt
created: '2026-07-23'
description: 'Meridian Credit Union is Ontario''s largest credit union and one of the largest in Canada — a member-owned financial cooperative headquartered in St. Catharines and Toronto, serving more than 365,000 members with roughly CAD $31 billion in assets under management, over 2,200 employees, and more than 75 years of history. Formed in 2005 through the merger of Niagara Credit Union and HEPCOE Credit Union, Meridian offers personal, business, and wealth banking and owns Meridian OneCap Credit Corp. (commercial equipment leasing and financing); it previously operated the federally chartered digital bank motusbank, which was wound down in 2023. As a provincially regulated Ontario credit union — overseen by the Financial Services Regulatory Authority of Ontario (FSRA), with member deposits insured under Ontario''s credit-union deposit-insurance scheme — Meridian is a cooperative, not a Schedule I or Schedule II bank. It publishes no first-party public developer API and no downloadable
  OpenAPI specification. Consumer-permissioned account-data access today is aggregator-mediated rather than first-party: Plaid maintains a Meridian institution connector, and the Central 1 / Flinks Outbound seam provides API-based data sharing for member credit unions. Canada''s federal Consumer-Driven Banking framework (legislated in 2024 with the Financial Consumer Agency of Canada / FCAC as overseer) is not yet operational, so Meridian''s open-finance participation remains voluntary and aggregator-based.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-23T18:00:00Z'
name: Meridian Credit Union
nav: Providers
network: true
overview: 'Meridian Credit Union is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Financial Services, Banking, Canada, Credit Union, and Cooperative.


  Meridian Credit Union''s developer surface includes support and 6 more developer resources.'
random_paper: 85
score:
  band: minimal
  composite: 11.9
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 4.3
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 11.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 17.7
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: domain-security
  name: Meridian Credit Union Domain Security
  slug: meridian-credit-union-domain-security
  summary_line: TLSv1.3 · DMARC
slug: meridian-credit-union
tags:
- Financial Services
- Banking
- Canada
- Credit Union
- Cooperative
- Ontario
- Data Aggregation
website: https://www.meridiancu.ca/
---
