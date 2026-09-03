---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
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
  url: security/ohalo-genetics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ohalo.com/
- group: company
  title: ''
  type: About
  url: https://www.ohalo.com/about
- group: company
  title: ''
  type: Blog
  url: https://www.ohalo.com/news
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ohalogenetics
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ohalo-genetics
- group: company
  title: ''
  type: Careers
  url: https://job-boards.greenhouse.io/ohalogenetics
coverage:
  checked: '2026-08-26'
  detail: Ohalo Genetics sells plant genetics — Boosted Breeding services, True Seed seedlings and proprietary potato, almond and strawberry varieties — and ohalo.com is a five-page Webflow marketing site with no /docs, /api, /developer, /llms.txt or sitemap, no api/app/docs/developer subdomain in DNS, and a 404 on every /.well-known/ path including a nonsense control path.
  evidence:
  - status: 200
    url: https://www.ohalo.com/
  - status: 404
    url: https://www.ohalo.com/docs
  - status: 404
    url: https://www.ohalo.com/openapi.json
  - status: 404
    url: https://www.ohalo.com/llms.txt
  - status: 404
    url: https://www.ohalo.com/.well-known/api-catalog
  - status: 404
    url: https://www.ohalo.com/.well-known/agent-card.json
  reason: not-a-software-company
  state: none
created: '2026-08-26'
description: Ohalo Genetics is an American agricultural biotechnology company founded in 2019 and led by CEO David Friedberg, developing plant-breeding platforms and proprietary crop varieties. Its flagship Boosted Breeding technology — marketed as "2x + 2x = 4x" — alters the reproductive circuitry of parent plants so each parent passes its entire genome to the next generation rather than a random half, producing polyploid offspring that carry the full genetic contribution of both parents and, in early field trials, substantially higher yields. Ohalo pairs this with an Agile Breeding service and a True Seed program that ships uniform, disease-free seedlings directly to growers, with active programs in potato, almond (the FruitionOne self-fertile Nonpareil variety), strawberry and corn, delivered through partnerships such as the Allied Potato partnership and a strawberry consortium. The company sells plant genetics and breeding services to agricultural partners; it is not a software vendor
  and publishes no public developer program, API, SDK or machine-readable contract.
image: https://cdn.prod.website-files.com/671a849e68709c39225eaca5/67472bba15de91cf033f3a59_Ohalo-Logo.svg
layout: provider
modified: '2026-08-26'
name: Ohalo Genetics
nav: Providers
network: true
overview: 'Ohalo Genetics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Agriculture, AgTech, Biotechnology, and Genetics.


  Ohalo Genetics'' developer surface includes engineering blog and 6 more developer resources.'
random_paper: 19
score:
  band: minimal
  composite: 5.8
  coverage:
    artifact_dirs: 4
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 5.8
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ohalo-genetics/refs/heads/main/screenshots/ohalo-genetics-2026-09-02T150831.png
security:
- kind: domain-security
  name: Ohalo Genetics Domain Security
  slug: ohalo-genetics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ohalo-genetics
tags:
- Company
- Agriculture
- AgTech
- Biotechnology
- Genetics
- Plant Breeding
- Seeds
- Food
website: https://www.ohalo.com/
---
