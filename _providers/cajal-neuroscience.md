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
  url: security/cajal-neuroscience-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cajal-tx.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CajalNeuroscience
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cajal-tx.com/privacy
- group: company
  title: ''
  type: News
  url: https://www.cajal-tx.com/news
- group: operate
  title: ''
  type: Contact
  url: https://www.cajal-tx.com/contact
- group: company
  title: ''
  type: Careers
  url: https://www.cajal-tx.com/careers
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cajal-tx/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cajal-neuroscience-llms.txt
coverage:
  checked: '2026-08-08'
  detail: Cajal is a clinical-stage iron-homeostasis therapeutics company (CTX001 in Phase 1) whose only public engineering output is open-source lab-bench hardware — a drone-motor spin coater and two microfluidic sensors — so there is no product for an API to expose; cajalneuro.com 307-redirects to cajal-tx.com, and api./docs./developer./data.cajal-tx.com have no DNS record at all.
  evidence:
  - status: 404
    url: https://www.cajal-tx.com/openapi.json
  - status: 404
    url: https://www.cajal-tx.com/.well-known/agent-card.json
  - status: 404
    url: https://www.cajal-tx.com/.well-known/api-catalog
  - status: 404
    url: https://www.cajal-tx.com/llms.txt
  - status: 200
    url: https://api.github.com/orgs/CajalNeuroscience
  reason: not-a-software-company
  state: none
created: '2026-08-08'
description: 'Cajal Neuroscience, which now operates publicly as Cajal Therapeutics, is a Seattle, Washington biotechnology company founded in 2020 by Alex Vaughan, Andrew Dervan and Ian Peikon, and launched in November 2022 with a $96 million Series A led by The Column Group and Lux Capital with participation from Two Sigma Ventures and Bristol Myers Squibb. The company develops small-molecule and RNA medicines that restore iron homeostasis, built around "iron mobilizers" — small molecules that transport iron across membranes into the compartments where it is required, bypassing disease-driven bottlenecks such as chronic inflammation, altered iron transporter expression and lysosomal dysfunction. Its pipeline spans systemic disease (CTX001, a clinical-stage iron mobilizer for anemia of chronic kidney disease; CTX201 and CTX211, preclinical siRNA programs for inflammatory anemia and myelofibrosis anemia) and CNS disease (a discovery-stage brain-penetrant iron mobilizer for Parkinson''s disease).
  This is a therapeutics company, not a software or data platform company: it publishes no developer program, no public API, and no machine-readable API contract. Its public GitHub organization contains open-source laboratory hardware and firmware (a drone-motor spin coater, a microfluidic pressure sensor, a flow sensor) plus forks of third-party single-cell and genomics analysis tooling — none of which expose a network API.'
image: https://www.cajal-tx.com/apple-touch-icon.png
layout: provider
modified: '2026-08-08'
name: Cajal Neuroscience
nav: Providers
network: true
overview: 'Cajal Neuroscience is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Pharmaceuticals, Drug Discovery, and Neurodegeneration.


  Cajal Neuroscience''s developer surface includes product news and 8 more developer resources.'
random_paper: 8
score:
  band: minimal
  composite: 6.5
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 6.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 12.5
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: domain-security
  name: Cajal Neuroscience Domain Security
  slug: cajal-neuroscience-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cajal-neuroscience
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Drug Discovery
- Neurodegeneration
- Neuroscience
- Therapeutics
- Life Sciences
- Genomics
- Health
website: https://www.cajal-tx.com/
---
