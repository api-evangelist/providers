---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.8
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: The anonymously readable WordPress REST content API behind nurabio.com. It serves the company news archive (9 posts), the six evergreen site pages, the 11-profile leadership, board and founders direct
  name: Nura Bio Content API
  slug: nura-bio-content-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://nurabio.com/
- group: company
  title: ''
  type: About
  url: https://nurabio.com/about-us/
- group: other
  title: ''
  type: Science
  url: https://nurabio.com/our-science/
- group: company
  title: ''
  type: News
  url: https://nurabio.com/news-and-literature/
- group: company
  title: ''
  type: BlogRSS
  url: https://nurabio.com/feed/
- group: company
  title: ''
  type: Careers
  url: https://nurabio.com/join-us/
- group: operate
  title: ''
  type: ContactForm
  url: https://nurabio.com/contact/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/nurabio
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/nura-bio-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/nura-bio-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/nura-bio-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/nura-bio-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/nura-bio-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/nura-bio-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/nura-bio-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/nura-bio-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/nura-bio-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/nura-bio-packages.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nura-bio-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/nura-bio-content-api-overlay.yaml
created: '2026-08-26'
description: Nura Bio, Inc. is a clinical-stage biopharmaceutical company headquartered in South San Francisco, California, developing neuroprotective small-molecule medicines that halt neurodegeneration before it progresses. Conceived in 2018 by The Column Group together with scientific founders Steve McKnight, PhD and Marc Freeman, PhD, the company targets SARM1 — a neuronally enriched NAD hydrolase that acts as an axon-intrinsic metabolic sensor and central driver of axonal degeneration — on the thesis that intervening early in that pathway confers durable structural and functional neuroprotection across peripheral, central and ocular nervous-system disorders. Its pipeline is led by NB-4746, a first-generation oral, brain-penetrant, reversible orthosteric SARM1 inhibitor in a global Phase 1b/2a study in ALS, and NB-9402, a mechanistically differentiated second-generation oral, covalent, irreversible, allosteric inhibitor completing a Phase 1a healthy-volunteer study in 2026. Nura Bio
  launched publicly in January 2020 with a $73 million Series A, extended that round with $68 million to pass $140 million raised, and closed a $73.8 million Series B in June 2026 led by The Column Group with Euclidean Capital, Samsara BioCapital and Sanofi Ventures; Shilpa Sambashivan, PhD, a co-founder and its chief scientist, serves as CEO. Its science is published in NEURON and CELL REPORTS. Nura Bio runs no developer program and publishes no product API, developer portal, API reference, SDK or pricing. The only machine-readable surfaces reachable without credentials are a published llms.txt and the WordPress REST content API behind nurabio.com, which serves the news archive, site pages, people directory and media library as JSON — both catalogued here.
image: https://nurabio.com/wp-content/uploads/2020/07/NuraBio_full_logo_grey_TM-1-1-1030x167.png
layout: provider
modified: '2026-08-26'
name: Nura Bio
nav: Providers
network: true
overview: 'Nura Bio publishes 1 API on the [APIs.io](https://apis.io/) network: Content API. Tagged areas include Company, Biotechnology, Pharmaceuticals, Neuroscience, and Neurodegeneration.


  Nura Bio''s developer surface includes product news, authentication, and 19 more developer resources.'
plans:
- name: Nura Bio Plans Pricing
  plan_count: 0
  slug: nura-bio-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Nura Bio Rate Limits
  slug: nura-bio-rate-limits
score:
  band: thin
  composite: 28.4
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 16.7
    contract_quality: 52.4
    developer_ergonomics: 13.7
    discoverability: 75.9
    governance: 16.7
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 38.8
  schema_version: 0.15.0
  scored_at: '2026-08-26'
security:
- kind: authentication
  name: Nura Bio Authentication
  slug: nura-bio-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Nura Bio Domain Security
  slug: nura-bio-domain-security
  summary_line: TLSv1.3 · DMARC
slug: nura-bio
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Neuroscience
- Neurodegeneration
- Drug Discovery
- Life Sciences
- Clinical Trials
- Rare Disease
- Small Molecule Therapeutics
- Content
website: https://nurabio.com/
---
