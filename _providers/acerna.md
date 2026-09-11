---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 8.5
  scored_at: '2026-09-10'
api_count: 1
apis:
- description: A live, anonymously reachable Model Context Protocol endpoint served from aceRNA Technologies' own host and advertised in the site's llms.txt. It is provided by the Wix platform, not built by aceRNA —
  name: aceRNA Technologies Site MCP
  slug: site-mcp
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://www.acernatec.com/
- group: agent
  title: ''
  type: MCPServer
  url: mcp/acerna-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/acerna-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/acerna-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/acerna-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/acerna-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://www.acernatec.com/en/news/
- group: operate
  title: ''
  type: Support
  url: https://www.acernatec.com/en/contact/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.acernatec.com/en/privacypolicy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/acerna-technologies
created: '2026-09-06'
description: aceRNA Technologies Co., Ltd. is a Japanese biotechnology venture founded in April 2018 to commercialize the RNA design technology ("RNA Switch") developed in the synthetic RNA biology laboratory of Prof. Hirohide Saito at Kyoto University. An RNA Switch is embedded into a messenger RNA so that expression of the therapeutic transgene is gated by the activity of a specific microRNA inside the cell, letting a treatment act only on the cell type and cell state that is diseased. The company applies the platform across mRNA medicines, cell therapy and gene therapy, co-develops with partners (an agreement with Nitto Denko was announced in December 2021), and closed a JPY 960M Series B in May 2024 led by DCI Partners. It is headquartered at the University of Tokyo Entrepreneur Plaza. aceRNA runs no developer programme and publishes no API reference, OpenAPI or SDK; the only machine-readable surfaces on its domain are the Wix-platform llms.txt and Site MCP endpoint, both captured here.
image: https://static.wixstatic.com/media/0bb01f_e4929cb81df449498969dcb40a661968~mv2.png
layout: provider
mcp_servers:
- description: ''
  name: コーポレートサイト (aceRNA Technologies corporate site)
  slug: コーポレートサイト-acerna-technologies-corporate-site
modified: '2026-09-06'
name: aceRNA Technologies
nav: Providers
network: true
overview: 'aceRNA Technologies publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Therapeutics, Genetic Medicine, and Life Sciences.


  aceRNA Technologies'' developer surface includes authentication, engineering blog, support, and 7 more developer resources.'
plans:
- name: Acerna Plans Pricing
  plan_count: 0
  slug: acerna-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Acerna Rate Limits
  slug: acerna-rate-limits
score:
  band: emerging
  composite: 16.8
  coverage:
    artifact_dirs: 8
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - japan
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - japan-korea
  previous_composite: 16.8
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 26.3
  schema_version: 0.20.0
  scored_at: '2026-09-10'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Acerna Authentication
  slug: acerna-authentication
  summary_line: none/session-token · 2 schemes
- kind: domain-security
  name: Acerna Domain Security
  slug: acerna-domain-security
  summary_line: TLSv1.3 · HSTS
slug: acerna
tags:
- Company
- Biotechnology
- Therapeutics
- Genetic Medicine
- Life Sciences
- Pharmaceuticals
- Japan
- MCP
website: https://www.acernatec.com/
---
