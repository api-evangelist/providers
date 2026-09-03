---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 18.3
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: The single GraphQL endpoint behind the Masterworks web and mobile apps, covering art offerings, artists, auction and repeat-sale data, contributions, agreements and e-signature, KYC and accreditation,
  name: Masterworks GraphQL API
  slug: masterworks-graphql-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/masterworks-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.masterworks.com/
- group: docs
  title: ''
  type: GraphQL
  url: graphql/masterworks-graphql.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/masterworks-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/masterworks-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/masterworks-error-codes.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/masterworks-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/masterworks-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/masterworks-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/masterworks-llms.txt
- group: operate
  title: ''
  type: Support
  url: https://knowledge.masterworks.com/en/knowledge
- group: company
  title: ''
  type: Blog
  url: https://www.masterworks.com/academy/posts
- group: company
  title: ''
  type: BlogRSS
  url: https://www.masterworks.com/academy/rss.xml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/MasterworksIO
- group: start
  title: ''
  type: SignUp
  url: https://www.masterworks.com/wizard/membership/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.masterworks.com/about/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.masterworks.com/about/privacy
- group: company
  title: ''
  type: About
  url: https://www.masterworks.com/about/about-masterworks
- group: other
  title: ''
  type: HowItWorks
  url: https://www.masterworks.com/about/how-it-works
- group: auth
  title: ''
  type: Disclosure
  url: https://www.masterworks.com/about/disclosure
- group: company
  title: ''
  type: Careers
  url: https://masterworks.breezy.hr/
- group: other
  title: ''
  type: SecondaryMarketListing
  url: https://forgeglobal.com/masterworks_stock/
created: '2026-08-04'
description: 'Masterworks is a New York fintech platform that securitizes blue-chip contemporary art. Founded in 2017 and headquartered at 1 World Trade Center, it acquires paintings by artists such as Picasso, Basquiat, Warhol, Monet and Banksy, places each work in its own LLC, files it with the SEC as a separate Regulation A offering, and sells fractional shares to retail investors — who can also trade those shares with each other on a Masterworks-operated secondary market. The company runs a consumer web app, iOS/Android apps and an "Academy" education site, all backed by a single GraphQL endpoint at api.masterworks.com/graphql. Masterworks publishes no developer program, no OpenAPI, no API documentation and no SDKs: the GraphQL endpoint is the private backend for its own clients. It does, however, answer anonymous schema introspection, so the full machine-readable contract — 516 queries, 621 mutations, 5 subscriptions and 1,584 types — is publicly readable even though every data operation
  returns 401 invalidAuthentication without a user token.'
image: https://www.masterworks.com/mwlogo-400x100.png
layout: provider
modified: '2026-08-04'
name: Masterworks
nav: Providers
network: true
overview: 'Masterworks publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Art, Art Investing, Alternative Investments, Fintech, and Investing.


  Masterworks'' developer surface includes authentication, support, engineering blog, signup flow, and 18 more developer resources.'
random_paper: 0
score:
  band: emerging
  composite: 19.8
  coverage:
    artifact_dirs: 12
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 37.2
    developer_ergonomics: 19.0
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 19.8
  provenance:
    conformance: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 28.3
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/masterworks/refs/heads/main/screenshots/masterworks-2026-08-07T172123.png
security:
- kind: authentication
  name: Masterworks Authentication
  slug: masterworks-authentication
  summary_line: bearer-token · 2 schemes
- kind: domain-security
  name: Masterworks Domain Security
  slug: masterworks-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: masterworks
tags:
- Art
- Art Investing
- Alternative Investments
- Fintech
- Investing
- Securities
- Fractional Ownership
- Secondary Market
- Wealth Management
- Regulation A
- GraphQL
website: https://www.masterworks.com/
---
