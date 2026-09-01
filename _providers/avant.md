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
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/avant-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/avant-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/avant-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.avant.com
- group: company
  title: ''
  type: Blog
  url: https://www.avant.com/blog
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.avant.com/
- group: operate
  title: ''
  type: Support
  url: https://support.avant.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.avant.com/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.avant.com/terms-of-use/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/avant-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/avant-security.txt
created: '2026-07-17'
description: Avant is a Chicago-based financial technology company that provides consumer credit products to middle-income U.S. consumers, primarily unsecured personal loans of roughly $2,000-$35,000 (9.95%-35.99% APR, 24-60 month terms) for debt consolidation, emergencies, home improvement, and other needs, alongside the Avant Credit Card issued through WebBank. Founded in 2012 and backed by investors including QED Investors and 500 Global, Avant operates a mobile-first lending and card-servicing platform with a customer help center, personal-finance blog, and SCRA support for military members. Avant is a consumer-facing product company and does not publish a public developer API or portal; this profile captures its public web, security, and support surfaces.
image: https://www.avant.com/favicon.ico
layout: provider
modified: '2026-07-18'
name: Avant
nav: Providers
network: true
overview: 'Avant is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Financial-Services, Fintech, Lending, and Personal Loans.


  Avant''s developer surface includes engineering blog, support, and 9 more developer resources.'
random_paper: 13
score:
  band: emerging
  composite: 11.1
  coverage:
    artifact_dirs: 4
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 11.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 25.3
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/avant/refs/heads/main/screenshots/avant-2026-07-25T201907.png
security:
- kind: domain-security
  name: Avant Domain Security
  slug: avant-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Avant Vulnerability Disclosure
  slug: avant-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: avant
tags:
- Company
- Financial-Services
- Fintech
- Lending
- Personal Loans
- Credit Cards
- Consumer Finance
- Banking
website: https://www.avant.com
---
