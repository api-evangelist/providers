---
access_model:
  confidence: high
  label: No Public API
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://www.northwesternmutual.com/
  - https://github.com/northwesternmutual
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
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/northwestern-mutual-vulnerability-disclosure.yml
- group: company
  title: ''
  type: Website
  url: https://www.northwesternmutual.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/northwesternmutual
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/northwestern-mutual
- group: company
  title: ''
  type: Blog
  url: https://news.northwesternmutual.com/
- group: operate
  title: ''
  type: Support
  url: https://www.northwesternmutual.com/contact-us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.northwesternmutual.com/legal-information/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.northwesternmutual.com/privacy-notices/
- group: start
  title: ''
  type: Login
  url: https://login.northwesternmutual.com/login
- group: auth
  title: ''
  type: DomainSecurity
  url: security/northwestern-mutual-domain-security.yml
- group: auth
  title: ''
  type: Security
  url: security/northwestern-mutual-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/northwestern-mutual-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/northwestern-mutual-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/northwestern-mutual-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/northwestern-mutual-llms.txt
coverage:
  checked: '2026-08-28'
  detail: 'Northwestern Mutual runs a large internal API estate — domain and experience APIs behind a governed gateway, harmonized with GraphQL, described only in third-party vendor case studies — but exposes none of it publicly: there is no developer.* or api.* DNS record at all, and every spec path on the corporate host (/openapi.json, /swagger.json, /api-docs, /graphql, /llms.txt) returns the site''s 404 page.'
  evidence:
  - status: 404
    url: https://www.northwesternmutual.com/openapi.json
  - status: 404
    url: https://www.northwesternmutual.com/api-docs
  - status: 404
    url: https://www.northwesternmutual.com/graphql
  - status: 404
    url: https://www.northwesternmutual.com/llms.txt
  - status: 0
    url: https://developer.northwesternmutual.com
  - status: 0
    url: https://api.northwesternmutual.com
  reason: no-developer-program
  state: none
created: '2026-03-21'
description: Northwestern Mutual is a Milwaukee-based Fortune 500 mutual insurance and financial services company founded in 1857, providing life insurance, disability income insurance, long-term care insurance, annuities, investment products, brokerage and wealth management services to individuals, families and businesses through a nationwide network of financial advisors. The company operates a large internal API estate — domain and experience APIs behind an API gateway, with GraphQL used to harmonize them — but publishes no public developer program, API documentation or machine-readable contract; its public engineering presence is an open source GitHub organization and a Bugcrowd-managed responsible disclosure program.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/northwestern-mutual.png
layout: provider
modified: '2026-08-28'
name: Northwestern Mutual
nav: Providers
network: true
overview: 'Northwestern Mutual is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, Life Insurance, Financial-Services, Wealth Management, and Annuities.


  Northwestern Mutual''s developer surface includes engineering blog, support, and 13 more developer resources.'
press:
- date: '2026-05-25'
  title: Stocks Rise as AI Overshadows Inflation, Softening ...
  url: https://www.northwesternmutual.com/life-and-money/stocks-rise-as-ai-overshadows-inflation-softening-employment/
- date: '2026-05-25'
  title: Northwestern Mutual's CIO Jeff Sippel on productivity gains ...
  url: https://www.cio.com/video/2138806/northwestern-mutuals-cio-jeff-sippel-on-productivity-gains-with-ai.html
- date: '2026-05-25'
  title: Artificial Intelligence at Northwestern Mutual
  url: https://emerj.com/artificial-intelligence-at-northwestern-mutual/
- date: '2026-05-25'
  title: Northwestern Mutual News and Press Releases
  url: https://www.prnewswire.com/news/northwestern-mutual/
- date: '2026-05-25'
  title: Americans Trust Advisors More Than AI for Financial ...
  url: https://news.northwesternmutual.com/2025-08-05-Human-Connection-Over-Machines-Americans-Trust-Advisors-More-Than-AI-for-Financial-Advice,-Finds-Northwestern-Mutuals-2025-Planning-Progress-Study
random_paper: 3
score:
  band: emerging
  composite: 14.9
  coverage:
    artifact_dirs: 9
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 14.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 30.3
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: domain-security
  name: Northwestern Mutual Domain Security
  slug: northwestern-mutual-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Northwestern Mutual Vulnerability Disclosure
  slug: northwestern-mutual-vulnerability-disclosure
  summary_line: Bugcrowd · security.txt · contact published
slug: northwestern-mutual
tags:
- Insurance
- Life Insurance
- Financial-Services
- Wealth Management
- Annuities
- Investment Management
- Fortune 500
website: https://www.northwesternmutual.com
---
