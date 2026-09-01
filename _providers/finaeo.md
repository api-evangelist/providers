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
  url: security/finaeo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.finaeo.com/
- group: start
  title: ''
  type: Login
  url: https://www.finaeo.com/login/
- group: start
  title: ''
  type: SignUp
  url: https://www.finaeo.com/signup/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.finaeo.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://www.finaeo.com/blog/
- group: auth
  title: ''
  type: Security
  url: https://www.finaeo.com/security/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.finaeo.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.finaeo.com/privacy-policy/
- group: other
  title: ''
  type: Marketplace
  url: https://www.finaeo.com/marketplace/
- group: start
  title: ''
  type: ClientPortal
  url: https://www.finaeo.com/client-portal/
- group: operate
  title: ''
  type: Support
  url: https://www.finaeo.com/contactus/
- group: start
  title: ''
  type: Demo
  url: https://www.finaeo.com/book-a-demo/
- group: operate
  title: ''
  type: ContactSales
  url: https://www.finaeo.com/contact-sales/
- group: learn
  title: ''
  type: Tutorials
  url: https://www.finaeo.com/tutorials/
- group: company
  title: ''
  type: About
  url: https://www.finaeo.com/who-we-are/
- group: company
  title: ''
  type: Newsroom
  url: https://www.finaeo.com/who-we-are/newsroom/
- group: other
  title: ''
  type: WhitePapers
  url: https://www.finaeo.com/white-papers/
- group: learn
  title: ''
  type: Videos
  url: https://www.finaeo.com/videos/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/finaeo-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/finaeo-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/finaeo-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/finaeo-lifecycle.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/FinaeoInc
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/finaeo
- group: company
  title: ''
  type: X (Twitter)
  url: https://twitter.com/finaeohq
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/channel/UCe3BqBc3dM93Nr7irYMkFEw
created: '2026-07-25'
description: Finaeo Inc. is a Toronto-based Canadian insurtech operating a digital marketplace that connects life insurance carriers, independent brokers and their clients. Its platform gives independent life brokers a product marketplace across carriers and hundreds of products, side-by-side product comparison and quoting, a place-a-policy checkout flow with selected carriers, a white-labeled client portal with digital onboarding and custom Financial Needs Assessments, contact and document management, broker landing pages, and team and distributor white-label offerings. Its home market is Canada, with expansion into the United States through IMO and broker-agency partnerships. Line of business is life insurance distribution — Finaeo is a distribution and agency technology vendor, not a risk carrier. Its API posture is honestly one of absence — Finaeo publishes no public developer portal, no API reference, no downloadable OpenAPI or Swagger, and no SDK. No developer, docs or api subdomain
  resolves in DNS, and a sweep of 2,840 archived first-party URLs turns up no developer surface at all. Finaeo's own carrier marketing explicitly positions its integration story against APIs, describing a "no-code toolkit to digitize products, configure applications, and launch custom workflows" that works "without the need for bulky APIs." The only documented carrier integration is a bilateral, partner-negotiated data handoff (Empire Life Fast & Full Life Application, 2021). Everything else sits behind a broker login or a book-a-demo form, making Finaeo a partner-gated, no-public-API provider.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-25'
name: Finaeo
nav: Providers
network: true
overview: 'Finaeo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, Canada, Life Insurance, Insurtech, and Brokers.


  Finaeo''s developer surface includes signup flow, pricing, engineering blog, support, YouTube channel, and 22 more developer resources.'
random_paper: 17
score:
  band: emerging
  composite: 20.2
  coverage:
    artifact_dirs: 7
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 13.2
  previous_composite: 20.2
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 28.8
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Finaeo Domain Security
  slug: finaeo-domain-security
  summary_line: TLSv1.3
slug: finaeo
tags:
- Insurance
- Canada
- Life Insurance
- Insurtech
- Brokers
- Agency Management
- Marketplace
- Distribution
- Quoting
- Policy Administration
website: https://www.finaeo.com/
---
