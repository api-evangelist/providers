---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - rate-limits
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.silvr.co/
- group: company
  title: ''
  type: Blog
  url: https://www.silvr.co/blog
- group: operate
  title: ''
  type: HelpCenter
  url: https://silvrspace.notion.site/Client-Help-Center-42f217ee279c4c32acbeac5506bdd54e
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.silvr.co/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.silvr.co/legal
- group: operate
  title: ''
  type: FAQ
  url: https://www.silvr.co/faq
- group: company
  title: ''
  type: About
  url: https://www.silvr.co/about
- group: company
  title: ''
  type: Press
  url: https://www.silvr.co/press
- group: other
  title: ''
  type: CaseStudies
  url: https://www.silvr.co/case-studies
- group: company
  title: ''
  type: Partners
  url: https://www.silvr.co/partners
- group: auth
  title: ''
  type: DomainSecurity
  url: security/silvr-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/silvr-llms.txt
coverage:
  checked: '2026-08-17'
  detail: Silvr Groupe SAS declared cessation of payments in June 2025 and on 2 December 2025 the Nanterre court awarded Karmen the takeover of all its assets bar the non-performing loan portfolio, so silvr.co is now a Webflow marketing archive whose apply and login buttons redirect to app.karmen.io; the embedded-finance partner API it once marketed never had a public reference and every spec, /.well-known and developer-host probe returns 404 or NXDOMAIN.
  evidence:
  - status: 404
    url: https://www.silvr.co/openapi.json
  - status: 404
    url: https://www.silvr.co/.well-known/agent-card.json
  - status: 0
    url: https://docs.silvr.co/
  - status: 200
    url: https://www.silvr.co/partners
  - status: 200
    url: https://app.karmen.io/sign-up?utm_source=silvr
  reason: defunct
  state: none
created: '2026-08-17'
description: Silvr (Silvr Groupe SAS, Neuilly-sur-Seine, France) was a French fintech that brought Revenue Based Financing to Europe, underwriting non-dilutive growth capital for e-commerce, SaaS and digital SMEs from its own Silvr Analytics scoring model and later broadening into flexible business loans of EUR 5k-10M covering receivables advances, inventory and equipment financing and working capital. Founded in 2020 by Nima Karimi and Gregory Tappero, it raised a EUR 130M Series A plus EUR 200M in debt from Citi and Channel, with ISAI, Serena, XAnge, Otium, Eurazeo and Bpifrance on the cap table. Silvr declared cessation of payments in June 2025; on 2 December 2025 the Nanterre court awarded Karmen the takeover of all Silvr assets except the non-performing loan portfolio, and silvr.co now redirects applicants and logins to app.karmen.io. Silvr marketed an embedded-finance partner API for real-time eligibility, but never published a developer portal, API reference or machine-readable contract,
  and that partner funnel now points at Karmen.
image: https://cdn.prod.website-files.com/6462b9f508a3cf04f201948d/6463bbf2935ab4f2d9b9c42c_Silvr_logo_black.svg
layout: provider
modified: '2026-08-17'
name: Silvr
nav: Providers
network: true
overview: 'Silvr is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech Insurtech, Lending, Revenue-Based Financing, and Embedded Finance.


  Silvr''s developer surface includes engineering blog, FAQ, and 10 more developer resources.'
plans:
- name: Silvr Plans Pricing
  plan_count: 0
  slug: silvr-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Silvr Rate Limits
  slug: silvr-rate-limits
score:
  band: minimal
  composite: 9.5
  coverage:
    artifact_dirs: 7
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
    developer_ergonomics: 2.4
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - france
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - france-iberia
  previous_composite: 9.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 21.2
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/silvr/refs/heads/main/screenshots/silvr-2026-09-02T155519.png
security:
- kind: domain-security
  name: Silvr Domain Security
  slug: silvr-domain-security
  summary_line: TLSv1.3 · HSTS
slug: silvr
tags:
- Company
- Fintech Insurtech
- Lending
- Revenue-Based Financing
- Embedded Finance
- Working Capital
- Invoice Financing
- SME Finance
- France
- Acquired
website: https://www.silvr.co/
---
