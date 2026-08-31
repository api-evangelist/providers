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
    well_known_catalog: true
  schema_version: 0.2
  score: 2.9
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/allorion-therapeutics-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/allorion-therapeutics-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/allorion-therapeutics-llms.txt
- group: company
  title: ''
  type: Website
  url: https://alloriontx.com/
- group: company
  title: ''
  type: About
  url: https://alloriontx.com/overview/
- group: other
  title: ''
  type: Team
  url: https://alloriontx.com/our-team/
- group: other
  title: ''
  type: Pipeline
  url: https://alloriontx.com/pipeline/
- group: other
  title: ''
  type: Presentations
  url: https://alloriontx.com/presentations/
- group: company
  title: ''
  type: News
  url: https://alloriontx.com/news/
- group: company
  title: ''
  type: Careers
  url: https://alloriontx.com/careers/
- group: operate
  title: ''
  type: Contact
  url: https://alloriontx.com/contact/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/alloriontx/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/AllorionT
- group: other
  title: ''
  type: SecondaryMarket
  url: https://www.nasdaqprivatemarket.com/
coverage:
  checked: '2026-08-06'
  detail: Allorion Therapeutics is a clinical-stage small-molecule drug-discovery company whose only web surface is an eight-page WordPress corporate site (Overview, Team, Pipeline, Presentations, News, Careers, Contact) — no api., developer., docs., dev., portal. or app. host resolves for alloriontx.com, no allorion/alloriontx/allorion-therapeutics GitHub organisation exists, and /openapi.json, /swagger.json, /graphql, /.well-known/agent-card.json, /.well-known/agent.json, /.well-known/security.txt and /.well-known/api-catalog all resolve to the site's WordPress 404 page behind a SiteGround CAPTCHA interstitial that answers every automated request with HTTP 202.
  evidence:
  - status: 404
    url: https://alloriontx.com/openapi.json
  - status: 404
    url: https://alloriontx.com/.well-known/agent-card.json
  - status: 404
    url: https://alloriontx.com/.well-known/agent.json
  - status: 404
    url: https://alloriontx.com/graphql
  - status: 404
    url: https://api.github.com/orgs/alloriontx
  reason: not-a-software-company
  state: none
created: '2026-08-06'
description: Allorion Therapeutics is a clinical-stage biopharmaceutical company founded in 2020 by Qiang Ding and Fang Li, developing novel small-molecule therapies for cancer and autoimmune disease. Operating from Natick, Massachusetts and Guangzhou, China, Allorion applies mutant-selective and isoform-specific medicinal chemistry across a pipeline that includes ARTS-011 (a TYK2 inhibitor), ARTS-021 (a CDK2 inhibitor targeting CCNE1-amplified tumors), and ARTS-023/AVZO-023 partnered with Avenzo Therapeutics, alongside an exclusive option and global license agreement with AstraZeneca for an allosteric EGFR L858R inhibitor. The company is a drug-discovery organization backed by Qiming Venture Partners and INCE Capital; it markets internal data and high-throughput screening platforms but publishes no public developer program, API, SDK, or machine-readable specification.
image: https://alloriontx.com/wp-content/uploads/2024/02/Allorion_Logo_web.png
layout: provider
modified: '2026-08-06'
name: Allorion Therapeutics
nav: Providers
network: true
overview: 'Allorion Therapeutics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Pharmaceuticals, Drug Discovery, and Oncology.


  Allorion Therapeutics'' developer surface includes product news and 13 more developer resources.'
random_paper: 1
score:
  band: minimal
  composite: 4.1
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
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 4.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/allorion-therapeutics/refs/heads/main/screenshots/allorion-therapeutics-2026-08-07T161224.png
security:
- kind: domain-security
  name: Allorion Therapeutics Domain Security
  slug: allorion-therapeutics-domain-security
  summary_line: TLSv1.3 · DMARC
slug: allorion-therapeutics
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Drug Discovery
- Oncology
- Autoimmune
- Life Sciences
- Clinical Stage
website: https://alloriontx.com/
---
