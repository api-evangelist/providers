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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nabla-bio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.nabla.bio/
- group: other
  title: ''
  type: Platform
  url: https://www.nabla.bio/platform
- group: company
  title: ''
  type: Partner
  url: https://www.nabla.bio/partner
- group: company
  title: ''
  type: News
  url: https://www.nabla.bio/news
- group: other
  title: ''
  type: Team
  url: https://www.nabla.bio/team
- group: company
  title: ''
  type: Careers
  url: https://www.nabla.bio/careers
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.nabla.bio/privacy-policy
- group: commercial
  title: ''
  type: Plans
  url: plans/nabla-bio-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/nabla-bio-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/nabla-bio-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/nabla-bio-llms.txt
coverage:
  checked: '2026-08-26'
  detail: Nabla Bio sells generative protein design through pharmaceutical partnership and molecule licensing only — its five-page Vercel-hosted marketing site has no docs, developer or API route at all, and every spec and .well-known path returns a real 404 on www.nabla.bio.
  evidence:
  - status: 404
    url: https://www.nabla.bio/openapi.json
  - status: 404
    url: https://www.nabla.bio/docs
  - status: 404
    url: https://www.nabla.bio/.well-known/agent-card.json
  - status: 200
    url: https://www.nabla.bio/partner
  reason: no-developer-program
  state: none
created: '2026-08-26'
description: Nabla Bio is a Cambridge, Massachusetts biotechnology company founded in 2021 as a Harvard spinout, building generative protein design systems for de novo biologics discovery. Its platform is JAM (Joint Atomic Modeling), a multimodal generative model trained on large-scale protein sequence and structure data that takes partial molecular context — a disease target or an epitope — and computationally designs the rest, producing de novo antibodies, VHH-Fc and full-length mAb formats, epitope scaffolds, cytokines, receptor traps and multi-domain multispecifics. The company pairs the model with an integrated wet lab that feeds mammalian, cellular and in vivo measurements back into training, and has published work on de novo design of GPCR-targeting antibodies against CXCR4 and CXCR7. Nabla Bio engages exclusively through pharmaceutical partnership and molecule licensing — with AstraZeneca, Bristol Myers Squibb and Takeda — and does not operate a public developer program, API, SDK
  or self-serve platform.
layout: provider
modified: '2026-08-26'
name: Nabla Bio
nav: Providers
network: true
overview: 'Nabla Bio is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Life Sciences, Drug Discovery, and Protein Design.


  Nabla Bio''s developer surface includes product news and 11 more developer resources.'
plans:
- name: Nabla Bio Plans Pricing
  plan_count: 0
  slug: nabla-bio-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Nabla Bio Rate Limits
  slug: nabla-bio-rate-limits
score:
  band: minimal
  composite: 6.5
  coverage:
    artifact_dirs: 6
    catalog_gap: 90.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 53.7
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 12.5
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Nabla Bio Domain Security
  slug: nabla-bio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nabla-bio
tags:
- Company
- Biotechnology
- Life Sciences
- Drug Discovery
- Protein Design
- Artificial Intelligence
- Machine-Learning
- Antibodies
- Generative Models
- Pharmaceuticals
website: https://www.nabla.bio/
---
