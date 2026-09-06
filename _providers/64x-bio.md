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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://64xbio.com/
- group: company
  title: ''
  type: About
  url: https://64xbio.com/company
- group: company
  title: ''
  type: Blog
  url: https://64xbio.com/news
- group: commercial
  title: ''
  type: TermsOfService
  url: https://64xbio.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://64xbio.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/64xbio
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/64xbio
- group: auth
  title: ''
  type: DomainSecurity
  url: security/64x-bio-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/64x-bio-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/64x-bio-plans-pricing.yml
coverage:
  checked: '2026-09-05'
  detail: '64x Bio sells engineered producer cell lines and wet-lab AAV/LV manufacturing suites under bespoke licensing agreements, and its only computational asset, the CellMap atlas, is internal research infrastructure: the Webflow marketing site is the entire public surface, with no developer subdomain resolving and every spec and .well-known path returning a true 404.'
  evidence:
  - status: 404
    url: https://64xbio.com/openapi.json
  - status: 404
    url: https://64xbio.com/.well-known/agent-card.json
  - status: 404
    url: https://64xbio.com/llms.txt
  - status: 200
    url: https://api.github.com/orgs/64xbio/repos
  - status: 200
    url: https://64xbio.com/
  reason: not-a-software-company
  state: none
created: '2026-09-05'
description: '64x Bio is a bioengineering company in Brisbane, California, founded in 2018 by scientists out of Harvard Medical School and the Wyss Institute to rebuild the manufacturing foundation for cell and gene therapies. Its VectorSelect platform pairs massively parallelized, barcoded genome-scale pooled screens with computational mining of CellMap, a proprietary atlas linking genetic and metabolic pathway data to production phenotypes, to engineer high-yield producer cell lines. Commercial products are the AAV APEX Suite for adeno-associated virus production across serotypes and scales, the LV APEX Suite for lentiviral vectors used in CAR-T programs, and a Biologics Suite for antibodies and protein therapeutics still in development. The business is delivered through licensing and partnership agreements with therapeutics developers and manufacturers rather than as software: CellMap and the screening stack are internal research infrastructure, and 64x Bio publishes no developer program,
  public API, SDK or machine-readable contract of any kind.'
image: https://cdn.prod.website-files.com/6810d12941b95c9ca365bf90/684b1446c4e598a5a00ca94a_OpenGraph.png
layout: provider
modified: '2026-09-05'
name: 64x Bio
nav: Providers
network: true
overview: '64x Bio is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Synthetic Biology, Gene Therapy, and Cell And Gene Therapy.


  64x Bio''s developer surface includes engineering blog and 9 more developer resources.'
plans:
- name: 64X Bio Plans Pricing
  plan_count: 0
  slug: 64x-bio-plans-pricing
random_paper: 18
score:
  band: minimal
  composite: 10.6
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
security:
- kind: domain-security
  name: 64X Bio Domain Security
  slug: 64x-bio-domain-security
  summary_line: TLSv1.3 · HSTS
slug: 64x-bio
tags:
- Company
- Biotechnology
- Synthetic Biology
- Gene Therapy
- Cell And Gene Therapy
- Biomanufacturing
- Cell Line Engineering
- Life Sciences
website: https://64xbio.com/
---
