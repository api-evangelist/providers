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
  scored_at: '2026-09-12'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/advancell-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.advancell.com.au/
- group: company
  title: ''
  type: About
  url: https://www.advancell.com.au/company/
- group: company
  title: ''
  type: Newsroom
  url: https://www.advancell.com.au/news/
- group: operate
  title: ''
  type: Contact
  url: https://www.advancell.com.au/contact/
- group: company
  title: ''
  type: InvestorRelations
  url: https://www.advancell.com.au/partners-and-investors/
- group: company
  title: ''
  type: Careers
  url: https://jobs.lever.co/advancell
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.advancell.com.au/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.advancell.com.au/privacy/
- group: other
  title: ''
  type: x-cookie-policy
  url: https://www.advancell.com.au/cookies/
- group: other
  title: ''
  type: x-acceptable-use-policy
  url: https://www.advancell.com.au/acceptable-use/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/advancell/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/advancell-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/advancell-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/advancell-rate-limits.yml
coverage:
  checked: '2026-09-09'
  detail: AdvanCell is a private clinical-stage radiopharmaceutical developer whose entire public surface is an eleven-page WordPress marketing site (Home, Company, Partners and Investors, News, Contact, four policy pages, ESMO2025, coming-soon) with no developer, docs or api subdomain and no product to integrate with; every OpenAPI/GraphQL/well-known/agent-card path probed on www.advancell.com.au returned 404, and the only JSON endpoint on the domain is the default WordPress core /wp-json/ route index, which is a CMS default rather than a published API.
  evidence:
  - status: 404
    url: https://www.advancell.com.au/openapi.json
  - status: 404
    url: https://www.advancell.com.au/.well-known/agent-card.json
  - status: 404
    url: https://www.advancell.com.au/graphql
  - status: 404
    url: https://www.advancell.com.au/llms.txt
  - status: 200
    url: https://www.advancell.com.au/wp-json/
  - status: 200
    url: https://www.advancell.com.au/page-sitemap.xml
  reason: not-a-software-company
  state: none
created: '2026-09-09'
description: AdvanCell is a vertically integrated, clinical-stage radiopharmaceutical company developing targeted alpha therapies (TAT) for cancer, built around lead-212 (Pb-212) alpha-emitting isotopes and a proprietary, scalable isotope production and supply chain. Its lead candidate, 212Pb-ADVC001, is in clinical development for metastatic prostate cancer, and the company operates GMP radiochemistry and sterile manufacturing capability across Sydney, Brisbane (Translational Research Institute and Richlands) and Adelaide in Australia, with a global headquarters established in the Greater Boston area. AdvanCell is a private, venture-backed biotechnology company; it publishes no public developer program, API, or machine-readable API contract.
image: https://www.advancell.com.au/wp-content/uploads/2025/04/advancell-og-image.jpg
layout: provider
modified: '2026-09-09'
name: AdvanCell
nav: Providers
network: true
overview: AdvanCell is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Pharmaceuticals, Health, and Oncology.
plans:
- name: Advancell Plans Pricing
  plan_count: 0
  slug: advancell-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Advancell Rate Limits
  slug: advancell-rate-limits
score:
  band: minimal
  composite: 9.8
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - australia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - anz
  previous_composite: 9.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.21.0
  scored_at: '2026-09-12'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Advancell Domain Security
  slug: advancell-domain-security
  summary_line: TLSv1.3 · DMARC
slug: advancell
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Health
- Oncology
- Radiopharmaceuticals
- Life Sciences
- Clinical Trials
- Australia
website: https://www.advancell.com.au/
---
