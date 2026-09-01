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
  url: security/helaina-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.myhelaina.com/
- group: company
  title: ''
  type: Blog
  url: https://www.myhelaina.com/blog/list
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.myhelaina.com/terms-conditions
- group: operate
  title: ''
  type: ContactUs
  url: https://www.myhelaina.com/partner-up
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/helaina/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/helaina-llms.txt
coverage:
  checked: '2026-08-22'
  detail: Helaina is a precision-fermentation ingredient manufacturer whose product is a physical protein (effera(R) human lactoferrin) sold B2B to supplement formulators, so there is nothing to expose as an API; its entire web presence is an 18-URL Webflow marketing site with no developer, docs, login, or store subdomain resolving in DNS.
  evidence:
  - status: 404
    url: https://www.myhelaina.com/openapi.json
  - status: 404
    url: https://www.myhelaina.com/api
  - status: 404
    url: https://www.myhelaina.com/.well-known/agent-card.json
  - status: 0
    url: https://developer.myhelaina.com/
  - status: 200
    url: https://www.myhelaina.com/llms.txt
  reason: not-a-software-company
  state: none
created: '2026-08-22'
description: 'Helaina is a New York based biotechnology and nutrition company that uses precision fermentation to produce bio-identical human proteins. Its flagship ingredient, effera(R), is described by the company as the world''s first bio-identical human lactoferrin, designed to match the lactoferrin naturally found in mother''s milk and in the human body rather than being extracted from cow''s milk. Helaina sells effera(R) as a business-to-business ingredient to supplement and nutrition formulators across women''s health, gut health, longevity, hair and skin, active nutrition, and infant and child nutrition, and has announced a partnership with Nestle to advance science-based early-life nutrition. Helaina is an ingredient manufacturer, not a software vendor: it publishes no public API, developer portal, SDK, or machine-readable API specification. The only machine-readable surface it publishes is an llms.txt at its website root, alongside a robots.txt that explicitly allows AI answer
  engines.'
image: https://cdn.prod.website-files.com/68b06b5fe51094ae5260962f/68c880229a68ffee8db183a0_OGD.webp
layout: provider
modified: '2026-08-22'
name: Helaina
nav: Providers
network: true
overview: 'Helaina is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Nutrition, Precision Fermentation, and Food Ingredients.


  Helaina''s developer surface includes engineering blog and 6 more developer resources.'
random_paper: 8
score:
  band: minimal
  composite: 7.4
  coverage:
    artifact_dirs: 4
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 7.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 12.5
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Helaina Domain Security
  slug: helaina-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: helaina
tags:
- Company
- Biotechnology
- Nutrition
- Precision Fermentation
- Food Ingredients
- Life Sciences
- Consumer Health
website: https://www.myhelaina.com/
---
