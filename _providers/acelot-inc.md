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
  scored_at: '2026-09-06'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://www.acelot.com/
- group: company
  title: ''
  type: Blog
  url: https://www.acelot.com/news
- group: company
  title: ''
  type: BlogRSS
  url: https://www.acelot.com/news?format=rss
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/acelot-inc
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/acelot-inc./
- group: other
  title: ''
  type: x-Publications
  url: https://www.acelot.com/publications
- group: other
  title: ''
  type: x-Team
  url: https://www.acelot.com/our-team
- group: auth
  title: ''
  type: DomainSecurity
  url: security/acelot-inc-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/acelot-inc-llms.txt
coverage:
  checked: '2026-09-06'
  detail: Acelot is a clinical-stage biopharmaceutical company whose product is a small-molecule therapeutic (ACE-2223), and its Resolute AI drug-discovery platform is described by the company as employed in-house only — acelot.com is a five-page Squarespace marketing site with no developer, docs or API section, and every contract-discovery path returned 404 on both acelot.com and www.acelot.com.
  evidence:
  - status: 200
    url: https://www.acelot.com/pipeline-and-platform
  - status: 404
    url: https://www.acelot.com/openapi.json
  - status: 404
    url: https://www.acelot.com/swagger.json
  - status: 404
    url: https://www.acelot.com/api-docs
  - status: 404
    url: https://www.acelot.com/graphql
  - status: 404
    url: https://www.acelot.com/mcp
  - status: 404
    url: https://www.acelot.com/llms.txt
  - status: 404
    url: https://www.acelot.com/.well-known/agent-card.json
  - status: 404
    url: https://www.acelot.com/.well-known/api-catalog
  - status: 200
    url: https://github.com/acelot-inc
  reason: no-developer-program
  state: none
created: '2026-09-06'
description: Acelot, Inc. is a clinical-stage biopharmaceutical company headquartered in South San Francisco, California, developing first-in-class small-molecule therapies for neurodegenerative diseases with high unmet need. Its lead candidate, ACE-2223, is designed to target misfolded and aggregated TDP-43 and restore the protein's healthy form and function, addressing pathology central to amyotrophic lateral sclerosis (ALS) and frontotemporal lobar degeneration (FTLD). Acelot's discovery work is powered by Resolute, an internal integrated drug-discovery platform combining AI-driven computational chemistry with structural and biological insight to drug historically intractable protein targets. Acelot publishes no public API, developer portal, SDK or machine-readable specification; its four public GitHub repositories are forks of third-party cheminformatics tooling.
image: https://static1.squarespace.com/static/6721bd430e24a6572ea4152a/t/6732691e70799e3f6a4e8b71/1731356958733/Acelot-Website-LogoKnockout-111124-v01.png?format=1500w
layout: provider
modified: '2026-09-06'
name: Acelot, Inc.
nav: Providers
network: true
overview: 'Acelot, Inc. is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Pharmaceuticals, Drug Discovery, and Life Sciences.


  Acelot, Inc.''s developer surface includes engineering blog and 8 more developer resources.'
random_paper: 4
score:
  band: minimal
  composite: 4.5
  coverage:
    artifact_dirs: 3
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
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 5.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.19.0
  scored_at: '2026-09-06'
security:
- kind: domain-security
  name: Acelot Inc Domain Security
  slug: acelot-inc-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: acelot-inc
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Drug Discovery
- Life Sciences
- Neurodegenerative Disease
- Artificial Intelligence
- Computational Chemistry
website: https://www.acelot.com/
---
