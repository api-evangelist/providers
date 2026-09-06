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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/3plw-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.triplew.co/
- group: operate
  title: ''
  type: Support
  url: https://www.triplew.co/contact
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/triplew-ltd/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://equityzen.com/company/3plw
coverage:
  checked: '2026-09-05'
  detail: TripleW is an industrial biotechnology and specialty-chemicals manufacturer that sells Circulac-brand lactic acid and PLA feedstock made from food waste, and its entire public surface is a nine-page Webflow marketing site (about, products, valorize-your-waste, closed-loop-plastics, port-of-antwerp-flagship, press, contact) whose only calls to action are info@triplew.co and sales@triplew.co — there is no developer, docs, portal or integration link anywhere in the nav or footer, every REST/GraphQL/MCP/agent-card and llms.txt path probed on both www.triplew.co and triplew.co returns a hard Webflow 404 (confirmed against a random control path returning the same 906-byte 404 body), and api./docs./developer.triplew.co do not resolve in DNS at all.
  evidence:
  - status: 200
    url: https://www.triplew.co/
  - status: 404
    url: https://www.triplew.co/openapi.json
  - status: 404
    url: https://www.triplew.co/swagger.json
  - status: 404
    url: https://www.triplew.co/api-docs
  - status: 404
    url: https://www.triplew.co/llms.txt
  - status: 404
    url: https://www.triplew.co/developers
  - status: 404
    url: https://www.triplew.co/.well-known/agent-card.json
  - status: 404
    url: https://www.triplew.co/.well-known/agent.json
  - status: 404
    url: https://www.triplew.co/.well-known/api-catalog
  - status: 404
    url: https://triplew.co/.well-known/security.txt
  - status: 404
    url: https://www.triplew.co/zz-api-evangelist-control-9f3a
  reason: not-a-software-company
  state: none
created: '2026-09-05'
description: 'TripleW Ltd. (Belgian operating entity TripleW NV) is an industrial biotechnology and specialty-chemicals company founded in 2016, headquartered at Innovatiestraat 1, 2030 Antwerpen, Belgium, with a US office in Shorewood, Wisconsin and R&D split between Israel and Belgium. Its patented process treats food waste as a third-generation renewable feedstock: hydrolysis, fermentation and purification yield pure lactic acid, sold under the Circulac brand in grades for personal care, home care, food and beverage and industrial use, and as the building block of polylactic acid (PLA) bioplastic. The same process chemically recycles discarded PLA back into feedstock, and can be installed inside existing waste-management infrastructure. Its flagship commercial Circulac facility is at the Port of Antwerp. TripleW sells industrial chemical product and engineering services, not software: no developer program, no public API, and no machine-readable API contract of any kind.'
image: https://cdn.prod.website-files.com/6509994d0ba4c9cac56b32c0/65b77561caea175779edc0ac_Webclip.jpg
layout: provider
modified: '2026-09-05'
name: TripleW Ltd.
nav: Providers
network: true
overview: 'TripleW Ltd. is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Chemicals, Industrial Biotechnology, Bioplastics, and Lactic Acid.


  TripleW Ltd.''s developer surface includes support and 4 more developer resources.'
random_paper: 12
score:
  band: minimal
  composite: 6.0
  coverage:
    artifact_dirs: 2
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
security:
- kind: domain-security
  name: 3Plw Domain Security
  slug: 3plw-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: 3plw
tags:
- Company
- Chemicals
- Industrial Biotechnology
- Bioplastics
- Lactic Acid
- Food Waste
- Circular Economy
- Cleantech
- Manufacturing
website: https://www.triplew.co/
---
