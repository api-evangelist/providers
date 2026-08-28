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
  url: security/kinaset-therapeutics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.kinasettherapeutics.com/
- group: company
  title: ''
  type: News
  url: https://www.kinasettherapeutics.com/news
- group: company
  title: ''
  type: About
  url: https://www.kinasettherapeutics.com/about-us
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/kinaset-tx/
- group: other
  title: ''
  type: Profile
  url: https://www.nasdaqprivatemarket.com/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kinaset-therapeutics-llms.txt
coverage:
  checked: '2026-08-23'
  detail: Kinaset Therapeutics is a clinical-stage inhaled-respiratory drug developer whose product is the frevecitinib (KN-002) pipeline, not software; its whole public surface is a 34-URL Squarespace marketing and investor-news site with no developer, API or docs route, no api/developer/docs subdomain (NXDOMAIN on all three), no GitHub organization and no first-party package on any registry, and its robots.txt additionally disallows every Squarespace JSON view and blocks the major AI crawlers by user agent.
  evidence:
  - status: 404
    url: https://www.kinasettherapeutics.com/openapi.json
  - status: 404
    url: https://www.kinasettherapeutics.com/swagger.json
  - status: 404
    url: https://www.kinasettherapeutics.com/api-docs
  - status: 404
    url: https://www.kinasettherapeutics.com/graphql
  - status: 404
    url: https://www.kinasettherapeutics.com/_api/mcp
  - status: 404
    url: https://www.kinasettherapeutics.com/.well-known/agent-card.json
  - status: 404
    url: https://www.kinasettherapeutics.com/.well-known/agent.json
  - status: 404
    url: https://www.kinasettherapeutics.com/.well-known/security.txt
  - status: 404
    url: https://www.kinasettherapeutics.com/llms.txt
  - status: 200
    url: https://www.kinasettherapeutics.com/sitemap.xml
  reason: not-a-software-company
  state: none
created: '2026-08-23'
description: 'Kinaset Therapeutics, Inc. is a clinical-stage biopharmaceutical company based in Medfield, Massachusetts, founded in 2020 by Robert Clarke (CEO), Roger Heerman (COO) and Frazer Morgan (CDO) to develop novel inhaled therapeutics for severe respiratory disease. Its lead candidate, frevecitinib (KN-002), is a dry-powder inhaled pan-JAK inhibitor — potent and balanced across JAK1, JAK2, JAK3 and TYK2 — designed as a non-invasive anti-inflammatory add-on to standard of care for all severe asthma patients regardless of the underlying cause of inflammation, and explored in COPD. The company completed a Phase 1/1b program (NCT05006521), received FDA IND clearance, and in July 2026 dosed the first patient in the Phase 2b PANAIRAMA trial (NCT07532265) after closing a $103M oversubscribed Series B in January 2026 led by RA Capital Management and Forge Life Science Partners, with EQT Life Sciences, Vivo Capital, Schroders Capital, Willett Advisors, Pictet Alternative Advisors, Sixty Degree
  Capital, Atlas Venture, 5AM Ventures and Gimv participating on roughly $143M raised to date. Kinaset is a drug developer, not a software company: its product is a clinical pipeline, and it publishes no developer program, no public API, no SDKs, no webhooks and no machine-readable API contract. Its entire public surface is a 34-page Squarespace marketing and investor-news site whose robots.txt disallows every platform JSON view and blocks the major AI crawlers by user agent.'
image: https://images.squarespace-cdn.com/content/6074890838dd81772d76a539/a1b26a82-6ba5-42b8-a5b7-d9307544c035/Kinaset-share-social.png?content-type=image%2Fpng
layout: provider
modified: '2026-08-23'
name: Kinaset Therapeutics
nav: Providers
network: true
overview: 'Kinaset Therapeutics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Pharmaceuticals, Life Sciences, and Clinical Stage.


  Kinaset Therapeutics'' developer surface includes product news and 6 more developer resources.'
random_paper: 14
score:
  band: minimal
  composite: 3.3
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 3.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: domain-security
  name: Kinaset Therapeutics Domain Security
  slug: kinaset-therapeutics-domain-security
  summary_line: TLSv1.3 · HSTS
slug: kinaset-therapeutics
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Life Sciences
- Clinical Stage
- Drug Discovery
- Respiratory
- Asthma
- COPD
- Inhaled Therapeutics
- Healthcare
website: https://www.kinasettherapeutics.com/
---
