---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/axial-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.axial.net/
- group: operate
  title: ''
  type: HelpCenter
  url: https://guide.axial.net/
- group: company
  title: ''
  type: Blog
  url: https://www.axial.net/forum/
- group: start
  title: ''
  type: Login
  url: https://network.axial.net/sign-in
- group: operate
  title: ''
  type: StatusPage
  url: https://status.axial.net/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.axial.net/legal/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.axial.net/legal/privacy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/axialmarket
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/axial
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/AxialCo
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/axial-llms.txt
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/axial-lifecycle.yml
coverage:
  checked: '2026-08-06'
  detail: Axial ships its lower-middle-market deal network only as an authenticated end-user application at network.axial.net — api.axial.net resolves in DNS but 404s on every spec path, the app host answers a 15,072-byte SPA shell for any route (so its 200s are a catch-all, not endpoints), and neither the marketing site, the guide.axial.net help center, the published llms.txt nor the Terms of Service mentions an API, SDK or webhook anywhere.
  evidence:
  - status: 404
    url: https://api.axial.net/openapi.json
  - status: 404
    url: https://www.axial.net/developers
  - status: 405
    url: https://network.axial.net/graphql
  - status: 404
    url: https://www.axial.net/.well-known/security.txt
  - status: 200
    url: https://www.axial.net/llms.txt
  reason: no-developer-program
  state: none
created: '2026-08-06'
description: Axial Networks operates Axial (axial.net), a private deal network for mergers, acquisitions and capital raising in the North American lower middle market. Founded in 2010 and based in New York, the platform connects business owners, M&A advisors, private equity buyers, strategic acquirers and lenders around live sell-side and buy-side transactions, and publishes a public member directory, the Middle Market Review editorial forum, industry deal-activity dashboards and business valuation calculators. The member product runs at network.axial.net and product help documentation at guide.axial.net. Axial publishes an llms.txt orientation file for language models and a public status page, but ships no public API, SDK, webhook surface or developer program — the platform is delivered as an authenticated end-user application only.
image: https://www.axial.net/wp-content/uploads/2024/12/cropped-00_Axial-favicon-120x120.png
layout: provider
modified: '2026-08-06'
name: Axial Networks
nav: Providers
network: true
overview: 'Axial Networks is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Mergers and Acquisitions, Private Capital, Deal Sourcing, and Financial-Services.


  Axial Networks'' developer surface includes engineering blog and 12 more developer resources.'
random_paper: 2
score:
  band: emerging
  composite: 12.6
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 18.4
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 12.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 17.7
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/axial/refs/heads/main/screenshots/axial-2026-08-07T162034.png
security:
- kind: domain-security
  name: Axial Domain Security
  slug: axial-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: axial
tags:
- Company
- Mergers and Acquisitions
- Private Capital
- Deal Sourcing
- Financial-Services
- Middle Market
- Investment Banking
- Marketplace
website: https://www.axial.net/
---
