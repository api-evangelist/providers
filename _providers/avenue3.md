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
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/avenue3-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://avenue3.com/
- group: company
  title: ''
  type: Blog
  url: https://avenue3.com/insights
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Avenue3-dev
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://avenue3.com/privacy-policy
- group: build
  title: ''
  type: Packages
  url: packages/avenue3-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/avenue3-llms.txt
coverage:
  checked: '2026-09-02'
  detail: Avenue3 is a Leeds openEHR consultancy that sells engagements, not software; its Webflow site has no developer section at all and every contract-discovery path on avenue3.com (/openapi.json, /swagger.json, /graphql, /api-docs, /docs, /llms.txt) returns the site 404, with the openEHR REST APIs it implements being published by openEHR International and operated by its clients.
  evidence:
  - status: 404
    url: https://avenue3.com/openapi.json
  - status: 404
    url: https://avenue3.com/graphql
  - status: 404
    url: https://avenue3.com/.well-known/agent-card.json
  - status: 200
    url: https://avenue3.com/sitemap.xml
  - status: 200
    url: https://github.com/Avenue3-dev
  reason: no-developer-program
  state: none
created: '2026-09-02'
description: 'Avenue3 Limited is a UK open data and openEHR technology consultancy headquartered at Platform, New Station Street, Leeds. Founded in November 2020 (Companies House 13040131), the firm positions itself as a trusted public sector partner delivering strategy, discovery, architecture and full-stack engineering services that separate clinical data from the applications that write it. Its practice is built around openEHR — the vendor-neutral health record standard used by NHS organisations across England, Scotland and Wales and by national programmes in Norway, Germany, Slovenia and Australia — and it is a listed openEHR Industry Partner. Avenue3 sells consulting engagements rather than a software product: it publishes no developer portal, no API documentation and no machine-readable contract of its own, and the APIs it builds are operated by its clients. Its only public technical surface is the Avenue3-dev GitHub organisation, which ships a small set of general-purpose open-source
  developer libraries to npm and NuGet. Avenue3 is also listed on the UK Digital Marketplace as a G-Cloud 14 supplier.'
image: https://cdn.prod.website-files.com/67a1e583d74401a6c4059731/67cebf97f47c8a1eee0fbb34_logo-avenue-3-256.png
layout: provider
modified: '2026-09-02'
name: Avenue3
nav: Providers
network: true
overview: 'Avenue3 is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consulting, Healthcare, openEHR, and Open Data.


  Avenue3''s developer surface includes engineering blog and 6 more developer resources.'
random_paper: 2
score:
  band: minimal
  composite: 7.3
  coverage:
    artifact_dirs: 4
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 5.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 12.5
  schema_version: 0.18.0
  scored_at: '2026-09-02'
security:
- kind: domain-security
  name: Avenue3 Domain Security
  slug: avenue3-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: avenue3
tags:
- Company
- Consulting
- Healthcare
- openEHR
- Open Data
- Interoperability
- Health IT
- United Kingdom
- NHS
- Professional Services
website: https://avenue3.com/
---
