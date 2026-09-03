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
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/unicorn-auctions-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.unicornauctions.com/
- group: operate
  title: ''
  type: Support
  url: https://help.unicornauctions.com/
- group: company
  title: ''
  type: Blog
  url: https://www.unicornauctions.com/unicorn-review
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/unicorn-auctions
- group: start
  title: ''
  type: SignUp
  url: https://www.unicornauctions.com/signup
- group: start
  title: ''
  type: Login
  url: https://www.unicornauctions.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.unicornauctions.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.unicornauctions.com/privacy-policy
- group: company
  title: ''
  type: Careers
  url: https://www.unicornauctions.com/careers
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/unicorn-auctions-llc
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/unicorn-auctions-llms.txt
coverage:
  checked: '2026-09-02'
  detail: 'Unicorn Auctions ships only end-user products - a Next.js bidding site and iOS/Android apps - and publishes nothing for developers: no /developers, /developer or /api-docs page exists, its GitHub organization has zero public repositories, no first-party SDK is on any registry, and the private Rails backend at api.unicornauctions.com answers 404 on every documentation and contract path while robots.txt explicitly disallows /api/.'
  evidence:
  - status: 404
    url: https://www.unicornauctions.com/developers
  - status: 404
    url: https://www.unicornauctions.com/openapi.json
  - status: 404
    url: https://api.unicornauctions.com/openapi.json
  - status: 404
    url: https://api.unicornauctions.com/graphql
  - status: 404
    url: https://www.unicornauctions.com/.well-known/agent-card.json
  - status: 404
    url: https://www.unicornauctions.com/llms.txt
  - status: 200
    url: https://api.github.com/orgs/unicorn-auctions/repos
  - status: 404
    url: https://registry.npmjs.org/unicorn-auctions
  reason: no-developer-program
  state: none
created: '2026-09-02'
description: 'Unicorn Auctions is a Chicago-based online auction marketplace for rare spirits and fine wine, founded in 2019 by A.J. Heindel, Cody Modeer and Phil Mikhaylov out of the city''s restaurant and bar trade. Every lot is sold on consignment: Unicorn authenticates, appraises, photographs and digitizes each bottle before listing it in one to three weekly online auctions that can carry several thousand lots spanning bourbon, scotch, Japanese whisky, tequila, agave spirits and wine. The company also runs a bonded vault storage service for collectors, and publishes The Unicorn Review, an editorial and auction-intelligence blog. Bidding is entirely digital, through the web platform and native iOS and Android apps. Unicorn Auctions publishes no public developer program - no OpenAPI, SDK, webhook catalog or developer portal - and the api.unicornauctions.com backend that serves its own clients is private, undocumented and disallowed in robots.txt.'
image: https://www.unicornauctions.com/images/brand/apple-touch-icon-180x180.png
layout: provider
modified: '2026-09-02'
name: Unicorn Auctions
nav: Providers
network: true
overview: 'Unicorn Auctions is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Auctions, Marketplace, E-Commerce, and Collectibles.


  Unicorn Auctions'' developer surface includes support, engineering blog, signup flow, and 9 more developer resources.'
random_paper: 1
score:
  band: emerging
  composite: 13.9
  coverage:
    artifact_dirs: 3
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 5.3
  schema_version: 0.18.0
  scored_at: '2026-09-02'
security:
- kind: domain-security
  name: Unicorn Auctions Domain Security
  slug: unicorn-auctions-domain-security
  summary_line: TLSv1.3 · DMARC
slug: unicorn-auctions
tags:
- Company
- Auctions
- Marketplace
- E-Commerce
- Collectibles
- Wine
- Spirits
- Retail
- Consumer
website: https://www.unicornauctions.com/
---
