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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://www.incredo.com/
- group: company
  title: ''
  type: About
  url: https://www.incredo.com/about
- group: operate
  title: ''
  type: Contact
  url: https://www.incredo.com/contact
- group: operate
  title: ''
  type: Support
  url: https://www.incredo.com/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.incredo.com/legal/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.incredo.com/legal/terms-of-use
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/douxmatok/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/douxmatok-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/douxmatok-llms.txt
coverage:
  checked: '2026-08-12'
  detail: Incredo (formerly DouxMatok) sells a physical sugar-reduction ingredient to food manufacturers; its entire web presence is a twelve-page Webflow marketing site whose sitemap contains no developer, docs or API page, and api/developer/docs/app/portal subdomains on both incredo.com and douxmatok.com do not resolve.
  evidence:
  - status: 200
    url: https://www.incredo.com/sitemap.xml
  - status: 404
    url: https://www.incredo.com/openapi.json
  - status: 404
    url: https://www.incredo.com/llms.txt
  - status: 404
    url: https://www.incredo.com/.well-known/agent-card.json
  - status: 404
    url: https://www.incredo.com/docs
  reason: not-a-software-company
  state: none
created: '2026-08-12'
description: 'DouxMatok is an Israeli food-technology company, rebranded as Incredo Ltd in May 2023, that develops Incredo Sugar — a sugar-based sugar-reduction ingredient built on a patented silica-carrier delivery technology that improves how efficiently real cane or beet sugar reaches sweet taste receptors, enabling manufacturers to cut sugar in bakery, confectionery, chocolate, spreads and nut butters by 30-50% (the company markets up to 70%) without artificial sweeteners, sugar alcohols or the aftertaste and cooling effects of alternative sweeteners. The technology is protected by more than 20 patents, was named a TIME Best Invention of 2020, and was featured in Netflix''s "Explained". The company sells as a B2B ingredient to food manufacturers through distributors and partner enquiries, and is backed by Sienna Venture Capital, Pitango, DSM-Firmenich Venturing and BlueRed Partners. It is an ingredient manufacturer, not a software vendor: as of this profile it operates a twelve-page
  marketing website and publishes no API, SDK, developer portal or machine-readable specification of any kind.'
image: https://cdn.prod.website-files.com/5fe3ba6011d5957fbf4db778/600070a873051c826ba7d885_og.png
layout: provider
modified: '2026-08-12'
name: DouxMatok
nav: Providers
network: true
overview: 'DouxMatok is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Food Technology, Ingredients, Sugar Reduction, and Manufacturing.


  DouxMatok''s developer surface includes support and 8 more developer resources.'
random_paper: 1
score:
  band: minimal
  composite: 10.9
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - middle-east
  previous_composite: 10.9
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/douxmatok/refs/heads/main/screenshots/douxmatok-2026-09-02T145308.png
security:
- kind: domain-security
  name: Douxmatok Domain Security
  slug: douxmatok-domain-security
  summary_line: TLSv1.3 · HSTS
slug: douxmatok
tags:
- Company
- Food Technology
- Ingredients
- Sugar Reduction
- Manufacturing
- Consumer Packaged Goods
- Israel
website: https://www.incredo.com/
---
