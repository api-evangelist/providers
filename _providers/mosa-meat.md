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
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mosa-meat-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mosameat.com/
- group: company
  title: ''
  type: Blog
  url: https://mosameat.com/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://mosameat.com/blog?format=rss
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mosameat.com/privacy-policy
- group: operate
  title: ''
  type: Contact
  url: https://mosameat.com/contact
- group: operate
  title: ''
  type: FAQ
  url: https://mosameat.com/faq
- group: company
  title: ''
  type: Careers
  url: https://mosameat.com/careers
- group: company
  title: ''
  type: PressKit
  url: https://mosameat.com/press-kit
coverage:
  checked: '2026-08-26'
  detail: Mosa Meat is a cultivated-beef manufacturer whose entire web presence is a 101-page Squarespace marketing site (blog, careers, FAQ, press kit, investor page) with no developer section, no api/developer/docs subdomain resolving in DNS, and no GitHub organization under any spelling of the name.
  evidence:
  - status: 404
    url: https://mosameat.com/openapi.json
  - status: 404
    url: https://mosameat.com/.well-known/agent-card.json
  - status: 404
    url: https://mosameat.com/llms.txt
  - status: 404
    url: https://api.github.com/orgs/mosameat
  - status: 200
    url: https://mosameat.com/
  reason: not-a-software-company
  state: none
created: '2026-08-26'
description: 'Mosa Meat is a European food technology company headquartered in Maastricht, the Netherlands, founded in 2016 as a spin-off of Maastricht University by Mark Post and Peter Verstrate. The company develops cultivated (cell-cultured) beef using cellular agriculture: a small cell sample taken from a cow is nurtured through natural processes into muscle and fat tissue, which the company states can yield up to 80,000 burgers from a single sample. Mosa Meat produced the world''s first cultured beef hamburger in 2013 and now operates the Mosa C.A.M.P.U.S. (Center for Advanced Meat Production, Upscaling, and Sustainability) in Maastricht, reported as the largest cultivated meat campus in the world. It is a B Corp certified organization pursuing regulatory approval and market entry for cultivated beef burgers. Mosa Meat is a laboratory and food production business; it publishes no developer program, public API, or machine-readable API contract.'
image: http://static1.squarespace.com/static/5f58b0094108a94a07e7dbd2/t/650d53aebdd64a47a823c81c/1695372211924/LinkedIn+Banner+2023.png?format=1500w
layout: provider
modified: '2026-08-26'
name: Mosa Meat
nav: Providers
network: true
overview: 'Mosa Meat is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Food Technology, Cultivated Meat, Cellular Agriculture, and Biotechnology.


  Mosa Meat''s developer surface includes engineering blog, FAQ, and 7 more developer resources.'
random_paper: 18
score:
  band: minimal
  composite: 7.6
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  schema_version: 0.15.0
  scored_at: '2026-08-26'
security:
- kind: domain-security
  name: Mosa Meat Domain Security
  slug: mosa-meat-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mosa-meat
tags:
- Company
- Food Technology
- Cultivated Meat
- Cellular Agriculture
- Biotechnology
- Agriculture
- Sustainability
- Netherlands
website: https://mosameat.com/
---
