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
  url: security/retro-biosciences-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/retro-biosciences-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.retro.bio/
- group: company
  title: ''
  type: About
  url: https://www.retro.bio/science
- group: other
  title: ''
  type: Product
  url: https://www.retro.bio/pipeline
- group: other
  title: ''
  type: Team
  url: https://www.retro.bio/team
- group: company
  title: ''
  type: Blog
  url: https://www.retro.bio/blog
- group: company
  title: ''
  type: Careers
  url: https://www.retro.bio/careers
- group: operate
  title: ''
  type: Contact
  url: mailto:hi@retro.bio
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/retrobiosciences
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/retro-biosciences
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/RetroBio_
- group: other
  title: ''
  type: SecondaryMarket
  url: https://www.hiive.com/securities/retro-biosciences-stock
coverage:
  checked: '2026-08-05'
  detail: Retro Biosciences is a preclinical therapeutics developer whose products are drugs, not software; its entire published site is the seven URLs in its own sitemap.xml (home, science, pipeline, team, careers, blog, one post), and api., developer. and docs.retro.bio are Vercel wildcard records that answer DEPLOYMENT_NOT_FOUND rather than serving anything.
  evidence:
  - status: 200
    url: https://www.retro.bio/sitemap.xml
  - status: 404
    url: https://www.retro.bio/openapi.json
  - status: 404
    url: https://www.retro.bio/.well-known/agent-card.json
  - status: 404
    url: https://www.retro.bio/.well-known/security.txt
  - status: 404
    url: https://api.retro.bio/openapi.json
  - status: 404
    url: https://developer.retro.bio/
  - status: 404
    url: https://docs.retro.bio/
  - status: 404
    url: https://www.retro.bio/llms.txt
  reason: not-a-software-company
  state: none
created: '2026-08-05'
description: 'Retro Biosciences is a Redwood City, California longevity biotechnology company founded in 2021 whose stated mission is to add ten years to healthy human lifespan. Its published preclinical pipeline spans RTR242, a small-molecule autophagy-flux booster aimed at Alzheimer''s disease; RTR888, iPSC-derived microglial progenitors for CNS conditions; RTR890, iPSC-derived hematopoietic stem cells for blood disorders; AAV-delivered in vivo tissue reprogramming for osteoarthritis and age-related hearing loss; and AI-designed protein therapeutics, the last built on a 2025 collaboration with OpenAI on a protein-engineering model for reprogramming factors. Retro was seeded with $180M from Sam Altman and reported a $1.8B valuation in 2026. It is a therapeutics company rather than a software company: it operates a public GitHub organization of internal lab-automation and bioinformatics tooling, but publishes no API, SDK, developer portal or machine-readable contract of any kind.'
image: https://www.retro.bio/opengraph-image.jpg
layout: provider
modified: '2026-08-05'
name: Retro Biosciences
nav: Providers
network: true
overview: 'Retro Biosciences is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Life Sciences, Longevity, and Aging.


  Retro Biosciences'' developer surface includes engineering blog and 12 more developer resources.'
random_paper: 17
score:
  band: minimal
  composite: 4.9
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
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 4.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/retro-biosciences/refs/heads/main/screenshots/retro-biosciences-2026-09-02T153636.png
security:
- kind: domain-security
  name: Retro Biosciences Domain Security
  slug: retro-biosciences-domain-security
  summary_line: TLSv1.3 · HSTS
slug: retro-biosciences
tags:
- Company
- Biotechnology
- Life Sciences
- Longevity
- Aging
- Therapeutics
- Cell Therapy
- Gene Therapy
- Drug Discovery
- Regenerative Medicine
- Neuroscience
- United States
website: https://www.retro.bio/
---
