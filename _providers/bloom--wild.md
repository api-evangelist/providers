---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 6.3
  scored_at: '2026-08-10'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/bloom--wild-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/bloom--wild-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bloom--wild-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bloomandwild.com/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://www.hiive.com/securities/bloom--wild-stock
- group: operate
  title: ''
  type: Support
  url: https://www.bloomandwild.com/help
- group: company
  title: ''
  type: Blog
  url: https://www.bloomandwild.com/the-blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/BloomAndWild
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bloomandwild.com/terms-and-privacy
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bloomandwild.com/privacy-statement
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bloom--wild-llms.txt
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/bloom--wild-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/bloom--wild-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/bloom--wild-conformance.yml
coverage:
  checked: '2026-08-07'
  detail: Bloom & Wild runs its own commerce platform but ships no developer product at all — no portal, no docs, no spec, and corporate/bulk gifting is quoted through a contact form and an account manager rather than an API; the live application backend at api.bloomandwild.com answers a JSON error envelope on every discovery path, including /openapi.json.
  evidence:
  - status: 404
    url: https://api.bloomandwild.com/openapi.json
  - status: 404
    url: https://api.bloomandwild.com/graphql
  - status: 404
    url: https://www.bloomandwild.com/.well-known/agent-card.json
  - status: 404
    url: https://www.bloomandwild.com/.well-known/api-catalog
  - status: 200
    url: https://www.bloomandwild.com/llms.txt
  - status: 200
    url: https://www.bloomandwild.com/.well-known/security.txt
  reason: no-developer-program
  state: none
created: '2026-08-07'
description: 'Bloom & Wild is a British direct-to-consumer online florist and gifting brand founded in 2013 by Aron Gelbard and Ben Stanway, best known for pioneering letterbox flowers — bouquets packed flat so they fit through a UK letterbox — alongside hand-tied bouquets, plants, gift sets, gift cards and recurring flower subscriptions. Bloom & Wild Group trades as Bloom & Wild in the United Kingdom, Ireland, Germany and Austria, and operates the sister brands bloomon (Netherlands, Belgium, Denmark) and Bergamotte (France) on separate storefronts. The group is a certified B Corp and runs its own commerce platform — a Ruby on Rails backend fronted by Kong, an Angular multi-brand web app and native iOS and Android clients, on AWS and GCP. Bloom & Wild publishes NO public developer portal, no API documentation, no OpenAPI or other machine-readable API description, and no partner or corporate-gifting API: business and bulk gifting is transacted through a contact form, an account manager and
  invoicing, not through a programmatic surface. The application backends at api.bloomandwild.com and capi.bloomandwild.com are live but private to the brand''s own clients and undocumented. What the group does publish for machines is narrow but real: an llms.txt on the UK and German storefronts that routes assistants to the correct market by delivery destination and even ships an optional agent widget specification, and an RFC 9116 security.txt served across every group storefront.'
image: https://www.bloomandwild.com/assets/branded-icons/favicons/favicon-192x192.png
layout: provider
modified: '2026-08-07'
name: Bloom & Wild
nav: Providers
network: true
overview: 'Bloom & Wild is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, E-commerce, Retail, Flowers, and Gifting.


  Bloom & Wild''s developer surface includes support, engineering blog, and 12 more developer resources.'
random_paper: 15
score:
  band: emerging
  composite: 15.9
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 6.5
    discoverability: 68.5
    governance: 12.5
    operational_transparency: 15.8
  previous_composite: 15.9
  provenance:
    conformance: first-party
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bloom--wild/refs/heads/main/screenshots/bloom--wild-2026-08-07T162636.png
security:
- kind: domain-security
  name: Bloom  Wild Domain Security
  slug: bloom--wild-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Bloom  Wild Vulnerability Disclosure
  slug: bloom--wild-vulnerability-disclosure
  summary_line: Hackerone · contact published
slug: bloom--wild
tags:
- Company
- E-commerce
- Retail
- Flowers
- Gifting
- Direct to Consumer
- Subscriptions
- Consumer Goods
- Logistics
- United Kingdom
- B Corp
website: https://www.bloomandwild.com/
---
