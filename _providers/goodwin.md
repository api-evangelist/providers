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
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/goodwin-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.teamgoodwin.com
- group: start
  title: ''
  type: SignUp
  url: https://app.hellogoodwin.com/brokers
- group: start
  title: ''
  type: Login
  url: https://app.hellogoodwin.com/brokers
- group: company
  title: ''
  type: Blog
  url: https://www.teamgoodwin.com/insights
- group: company
  title: ''
  type: News
  url: https://www.teamgoodwin.com/news
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.teamgoodwin.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.teamgoodwin.com/terms-of-service
created: '2026-07-17'
description: Goodwin (Goodwin Company, teamgoodwin.com) is a B2B charter aviation technology company founded in 2023 and headquartered in Columbus, Ohio, backed by Canaan Partners at Series A. Its API-first platform serves the private-jet charter broker-operator ecosystem with aircraft sourcing across an 11,000+ aircraft database, automated proposal generation, modern payment processing beyond wire transfers, real-time market-adaptive pricing, and post-sale trip management. The white-labeled software integrates with operators' existing scheduling systems and is offered to emerging, growing, and enterprise brokers as well as charter operators. Goodwin operates purely B2B and does not currently publish a public developer API, OpenAPI specification, or developer portal; this profile captures its identity and public web properties.
image: https://goodwin-public-images-prod.s3.us-east-2.amazonaws.com/company-profile-images/cmpdf25f07d05e_17436103217340.png
layout: provider
modified: '2026-07-19'
name: Goodwin
nav: Providers
network: true
overview: 'Goodwin is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Aviation, Charter Aviation, Private Aviation, and Travel.


  Goodwin''s developer surface includes signup flow, engineering blog, product news, and 5 more developer resources.'
random_paper: 3
score:
  band: minimal
  composite: 10.7
  coverage:
    artifact_dirs: 3
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 10.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 21.9
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/goodwin/refs/heads/main/screenshots/goodwin-2026-07-25T220101.png
security:
- kind: domain-security
  name: Goodwin Domain Security
  slug: goodwin-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: goodwin
tags:
- Company
- Aviation
- Charter Aviation
- Private Aviation
- Travel
- Payments
- Software-as-a-Service
- B2B
website: https://www.teamgoodwin.com
---
