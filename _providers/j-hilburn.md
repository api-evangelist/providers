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
  scored_at: '2026-08-26'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://jhilburn.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://jhilburn.com/termsandconditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://jhilburn.com/privacypolicy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/JHilburn
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/j-hilburn
- group: auth
  title: ''
  type: DomainSecurity
  url: security/j-hilburn-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/j-hilburn-llms.txt
coverage:
  checked: '2026-08-23'
  detail: J.Hilburn sells custom clothing and ships only end-user software (two iOS stylist apps and a web storefront); its own robots.txt discloses private /clientapi/ and *.asmx endpoints behind a live IIS/ASP.NET origin at api.jhilburn.com, but there is no developer portal, no API reference and no machine-readable description anywhere on its public surface.
  evidence:
  - status: 200
    url: https://jhilburn.com/robots.txt
  - status: 403
    url: https://api.jhilburn.com/
  - status: 404
    url: https://api.jhilburn.com/swagger/v1/swagger.json
  - status: 404
    url: https://jhilburn.com/.well-known/api-catalog
  - status: 404
    url: https://jhilburn.com/llms.txt
  reason: no-developer-program
  state: none
created: '2026-08-23'
description: 'J.Hilburn is a Dallas, Texas based direct-to-consumer custom menswear brand founded in 2007. It designs and sells made-to-measure suits, shirts, trousers, polos and outerwear through a network of roughly 1,000 independent personal stylists and a small number of studio spaces rather than traditional retail stores. Its public technology surface is consumer- and stylist-facing rather than developer-facing: a catalog and checkout storefront at jhilburn.com, a stylist recruiting and training site at stylist.jhilburn.com, and two iOS applications, J.Hilburn Stylist and J.Hilburn VMA (Virtual Measuring App). J.Hilburn publishes no developer portal, no API reference and no machine-readable API description; the only API surfaces evident from the public web are private, undocumented internal endpoints that the company''s own robots.txt disallows crawlers from reaching.'
image: https://avatars.githubusercontent.com/u/1018061?v=4
layout: provider
modified: '2026-08-23'
name: J Hilburn
nav: Providers
network: true
overview: J Hilburn is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Retail, Apparel, Fashion, and Ecommerce.
random_paper: 4
score:
  band: minimal
  composite: 9.6
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 9.6
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: domain-security
  name: J Hilburn Domain Security
  slug: j-hilburn-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: j-hilburn
tags:
- Company
- Retail
- Apparel
- Fashion
- Ecommerce
- Direct to Consumer
- Menswear
- Custom Clothing
website: https://jhilburn.com
---
