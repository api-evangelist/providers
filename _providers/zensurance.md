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
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://www.zensurance.com/
- group: company
  title: ''
  type: Blog
  url: https://www.zensurance.com/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://www.zensurance.com/feed
- group: company
  title: ''
  type: Partners
  url: https://www.zensurance.com/zensurance-partnerships
- group: start
  title: ''
  type: CustomerPortal
  url: https://app.zensurance.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/zensurance
- group: company
  title: ''
  type: Careers
  url: https://www.zensurance.com/careers
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.zensurance.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.zensurance.com/terms-of-use
- group: operate
  title: ''
  type: Support
  url: https://www.zensurance.com/contact
- group: start
  title: ''
  type: SignUp
  url: https://www.zensurance.com/quote
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/zensurance-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zensurance-domain-security.yml
created: '2026-07-25'
description: Zensurance is a Toronto-based digital commercial insurance brokerage founded in 2016 that sells small-business and freelancer coverage online across every Canadian province, placing risk with Canadian carriers rather than underwriting it. Its book is commercial property and casualty — general and commercial general liability, professional liability and errors and omissions, cyber liability, directors and officers, commercial property, commercial auto, builder's risk, and a long tail of trade- and profession-specific packages — sold through a quote-to-bind web flow marketed as an instant online price with licensed broker support and claims advocacy behind it. It sits in the thin digital-broker layer beneath Canada's Big-Few carrier oligopoly, in a market with no open-insurance mandate — OSFI supervises federally-regulated insurers prudentially while FSRA, the AMF, and the other provincial regulators own market conduct, and Consumer-Driven Banking excludes insurance outright.
  Its API posture reflects that. Zensurance publishes no public, self-serve developer portal, no reference documentation, and no downloadable OpenAPI, Swagger, GraphQL, or AsyncAPI definition. The company's partnership page advertises "seamless API integrations and co-branded white-label tools" for distribution partners, but the only route to that surface is a partnership application form — the integration is partner-gated and privately negotiated. A first-party host at api.zensurance.com answers on the public internet (HTTP 200, returning a bare version string, with a /health endpoint) but it is the undocumented backend for Zensurance's own quoting and policy application, not a published product API. No ACORD, AL3, ACORD XML, NGDS, or agency-management-system integration claim appears anywhere on the company's public web properties. The one machine-addressable surface the company does publish for automated consumers is an llms.txt at www.zensurance.com/llms.txt — a 178KB marketing index
  of its pages, blog posts, and FAQs (which inadvertently lists its zenstage.wpengine.com staging host rather than the production domain). It describes insurance products for AI assistants; it documents no API.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-25'
name: Zensurance
nav: Providers
network: true
overview: 'Zensurance is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, Canada, Insurtech, Broker, and Property and Casualty.


  Zensurance''s developer surface includes engineering blog, support, signup flow, and 10 more developer resources.'
random_paper: 15
score:
  band: emerging
  composite: 13.4
  delta: -2.2
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 15.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 21.2
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: domain-security
  name: Zensurance Domain Security
  slug: zensurance-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: zensurance
tags:
- Insurance
- Canada
- Insurtech
- Broker
- Property and Casualty
- Commercial Insurance
- Small Business Insurance
- Cyber Insurance
- Digital Brokerage
- Partner Gated
website: https://www.zensurance.com/
---
