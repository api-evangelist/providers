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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-10'
api_count: 0
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/acquco-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.acqu.co/
- group: company
  title: ''
  type: About
  url: https://www.acqu.co/about-us
- group: other
  title: ''
  type: Services
  url: https://sellerfusion.io/services
- group: other
  title: ''
  type: CaseStudies
  url: https://sellerfusion.io/case-studies
- group: commercial
  title: ''
  type: Pricing
  url: https://sellerfusion.io/pricing
- group: commercial
  title: ''
  type: Plans
  url: plans/acquco-plans-pricing.yml
- group: start
  title: ''
  type: Login
  url: https://app.sellerfusion.io/auth/sign_in
- group: operate
  title: ''
  type: HelpCenter
  url: https://sellerfusion.io/helpcenter
- group: operate
  title: ''
  type: Support
  url: https://sellerfusion.io/contact
- group: operate
  title: ''
  type: ContactUs
  url: https://www.acqu.co/get-evaluated
- group: company
  title: ''
  type: Partners
  url: https://www.acqu.co/partner-solution
- group: company
  title: ''
  type: Careers
  url: https://www.acqu.co/careers
- group: company
  title: ''
  type: Newsroom
  url: https://www.acqu.co/newsroom
- group: company
  title: ''
  type: Blog
  url: https://www.acqu.co/resources
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.acqu.co/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.acqu.co/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/acquco
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/acquco
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/acquco
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/channel/UCadvoB17oc15G-YTc5sXvEQ
- group: other
  title: ''
  type: x-secondary-market-listing
  url: https://equityzen.com/company/acquco/
- group: auth
  title: ''
  type: Security
  url: security/acquco-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/acquco-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/acquco-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: security/acquco-trust-center.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/acquco-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/acquco-llms.txt
- group: agent
  title: ''
  type: x-well-known-probe
  url: well-known/acquco-well-known.yml
- group: build
  title: ''
  type: x-packages-probe
  url: packages/acquco-packages.yml
- group: other
  title: ''
  type: x-rate-limits-probe
  url: rate-limits/acquco-rate-limits.yml
coverage:
  checked: '2026-09-06'
  detail: 'Acquco buys and operates Amazon FBA brands, and its one software product — Sellerfusion, "powered by Acquco" — is a seller-operations SaaS that CONSUMES Amazon SP-API, Shopify, Walmart, Target Plus and NetSuite while publishing nothing itself: no developer portal, no spec at any discovery path on five probed hosts, and its own api.sellerfusion.io answers every one of them with a JSON 404 from behind a self-signed certificate issued to scraper-proxy.easychamp.com.'
  evidence:
  - status: 404
    url: https://api.sellerfusion.io/openapi.json
  - status: 404
    url: https://sellerfusion.io/openapi.json
  - status: 404
    url: https://www.acqu.co/openapi.json
  - status: 404
    url: https://www.acqu.co/.well-known/agent-card.json
  - status: 404
    url: https://sellerfusion.io/.well-known/agent-card.json
  - status: 404
    url: https://sellerfusion.io/llms.txt
  - status: 404
    url: https://app.sellerfusion.io/auth/sign_up
  reason: no-developer-program
  state: none
created: '2026-09-06'
description: 'Acquco is a New York City based acquirer and operator of Amazon third-party (FBA) e-commerce brands, founded in 2020 by former Amazon operators Raunak Nirmal and Haumin Lum and backed by roughly $160M in Series A equity and debt from CoVenture, Crossbeam and Crosslink Capital. The company buys established Amazon seller businesses — closing in an average of about 23 days — then migrates them onto its own operating stack and scales them across Amazon, Walmart, Target Plus and DTC channels. That stack is productized as Sellerfusion (sellerfusion.io, "powered by Acquco"), a multi-marketplace seller operations platform for analytics, automation, monitoring, PPC and financial reconciliation, which integrates with Amazon Seller Central and the Amazon Selling Partner API (SP-API), Shopify, Walmart Marketplace, Target Plus and NetSuite ERP. Acquco is therefore an API CONSUMER rather than an API producer: it publishes no public API, developer portal, OpenAPI/GraphQL contract, SDK or
  webhook surface of its own, and its Sellerfusion enterprise tier offers "custom API integrations" only as bespoke, sales-gated work. It does publish a substantive Security & Trust page covering its security program, incident response and Amazon DPP / GDPR / CCPA compliance posture.'
image: https://cdn.prod.website-files.com/5e57b021f53be6722a091469/5e5ff35e34ad5de3778fbc80_acquco-fav-lg.png
layout: provider
modified: '2026-09-06'
name: Acquco
nav: Providers
network: true
overview: 'Acquco is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, E-Commerce, Amazon, Marketplaces, and Amazon FBA.


  Acquco''s developer surface includes pricing, support, engineering blog, YouTube channel, and 27 more developer resources.'
plans:
- name: Acquco Plans Pricing
  plan_count: 3
  slug: acquco-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Acquco Rate Limits
  slug: acquco-rate-limits
score:
  band: thin
  composite: 29.5
  coverage:
    artifact_dirs: 7
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 13.2
  previous_composite: 29.5
  provenance:
    conformance: first-party
  schema_version: 0.20.0
  scored_at: '2026-09-10'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Acquco Domain Security
  slug: acquco-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
- kind: vulnerability-disclosure
  name: Acquco Vulnerability Disclosure
  slug: acquco-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Acquco Trust Center
  slug: acquco-trust-center
  summary_line: audited_certifications, note
slug: acquco
tags:
- Company
- E-Commerce
- Amazon
- Marketplaces
- Amazon FBA
- Aggregator
- Mergers And Acquisitions
- Seller Tools
- Analytics
- Retail
- SaaS
- New York
website: https://www.acqu.co/
---
