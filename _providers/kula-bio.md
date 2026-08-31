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
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kula-bio-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kula-bio-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.kulabio.com/
- group: company
  title: ''
  type: About
  url: https://www.kulabio.com/about
- group: company
  title: ''
  type: Blog
  url: https://www.kulabio.com/news
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.kulabio.com/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.kulabio.com/privacy
- group: operate
  title: ''
  type: Contact
  url: https://www.kulabio.com/contact
- group: other
  title: ''
  type: Product
  url: https://www.kulabio.com/product
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/kulabio
coverage:
  checked: '2026-08-23'
  detail: Kula Bio manufactures Kula-N, a physical nitrogen-fixing microbial biofertilizer sold to growers through agronomic distribution; its entire web presence is an eight-page Webflow marketing site with no developer, docs, or api subdomain in DNS, and every contract-discovery path probed on www.kulabio.com (/openapi.json, /graphql, /llms.txt, /.well-known/agent-card.json) returned a clean 404.
  evidence:
  - status: 200
    url: https://www.kulabio.com/
  - status: 404
    url: https://www.kulabio.com/openapi.json
  - status: 404
    url: https://www.kulabio.com/graphql
  - status: 404
    url: https://www.kulabio.com/llms.txt
  - status: 404
    url: https://www.kulabio.com/.well-known/agent-card.json
  - status: 404
    url: https://api.github.com/orgs/kulabio
  reason: not-a-software-company
  state: none
created: '2026-08-23'
description: Kula Bio is an agricultural biotechnology company headquartered in Natick, Massachusetts that manufactures Kula-N, a nitrogen-fixing microbial biofertilizer built on the bacterium Xanthobacter autotrophicus. The company's process, originating in Dr. Dan Nocera's research, "supercharges" the microbe with renewable energy so it fixes atmospheric nitrogen at the root zone, letting growers replace a portion of synthetic nitrogen while cutting the greenhouse-gas footprint of the applied product. Kula Bio sells a liquid formulation and, since February 2026, a Soluble Powder (SP) line, serving produce and row-crop growers through agronomic distribution rather than through software. It raised a $50M Series A led by Lowercarbon Capital and was named to TIME's list of America's Top GreenTech Companies of 2026. Kula Bio publishes no developer program, API, SDK, or machine-readable contract of any kind; this profile records that measured absence alongside its verified public corporate surface.
image: https://cdn.prod.website-files.com/669e8de72476f4b31efa3737/669e8de72476f4b31efa375a_kb-logo.svg
layout: provider
modified: '2026-08-23'
name: Kula Bio
nav: Providers
network: true
overview: 'Kula Bio is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Agriculture, AgTech, Biotechnology, and Fertilizer.


  Kula Bio''s developer surface includes engineering blog and 9 more developer resources.'
random_paper: 11
score:
  band: minimal
  composite: 9.7
  coverage:
    artifact_dirs: 4
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 9.7
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: domain-security
  name: Kula Bio Domain Security
  slug: kula-bio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: kula-bio
tags:
- Company
- Agriculture
- AgTech
- Biotechnology
- Fertilizer
- Sustainability
- Climate
- Manufacturing
website: https://www.kulabio.com/
---
