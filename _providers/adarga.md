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
  scored_at: '2026-09-10'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/adarga-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.adarga.ai/
- group: company
  title: ''
  type: About
  url: https://www.adarga.ai/about
- group: other
  title: ''
  type: CaseStudies
  url: https://www.adarga.ai/case-studies
- group: company
  title: ''
  type: Blog
  url: https://www.adarga.ai/news
- group: company
  title: ''
  type: BlogRSS
  url: https://www.adarga.ai/news?format=rss
- group: operate
  title: ''
  type: Support
  url: https://support.adarga.ai/support/home
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.adarga.ai/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/adarga-ai
- group: company
  title: ''
  type: LinkedIn
  url: https://uk.linkedin.com/company/adargaai
- group: company
  title: ''
  type: Careers
  url: https://adarga.recruitee.com/
- group: build
  title: ''
  type: Packages
  url: packages/adarga-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/adarga-plans-pricing.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/adarga-llms.txt
coverage:
  checked: '2026-09-07'
  detail: Adarga markets Catalyst as "The Developer Platform" where customers build "agents, tools and APIs", but the only documentation surface is a Freshservice customer portal at support.adarga.ai whose category list is public while every article folder returns HTTP 401 Unauthorized to an anonymous reader, and adarga.ai itself is a 14-page Squarespace estate with no developer section.
  evidence:
  - status: 401
    url: https://support.adarga.ai/support/solutions/folders/51000033057
  - status: 403
    url: https://support.adarga.ai/api/_/solutions/categories
  - status: 200
    url: https://www.adarga.ai/sitemap.xml
  - status: 404
    url: https://www.adarga.ai/openapi.json
  - status: 404
    url: https://www.adarga.ai/.well-known/agent-card.json
  reason: customer-only-docs
  state: gated
created: '2026-09-07'
description: Adarga is a British artificial-intelligence software company, founded in London in 2016 by Rob Bassett Cross, that builds information-intelligence and decision-advantage software for Defence, National Security and Resilience customers. Its products include Adarga Vantage, an AI analysis platform that extracts, contextualises and connects information from millions of internal and external sources in more than 75 languages; Adarga Augur, an alerting and intelligence tool; and Catalyst, a multidomain data-fusion and developer platform that the company markets as a Sovereign AI Stack. Adarga sells to the UK Ministry of Defence and Strategic Command and to US federal customers, and partners with Oracle to run Vantage on Oracle Cloud Infrastructure. Adarga publishes no public developer portal, API documentation, or machine-readable API contract; its product documentation sits behind a customer support portal.
image: http://static1.squarespace.com/static/69b8196e37339d1a13c7da39/t/69b81b862863403cb2492195/1773673350751/Adarga_White_16x9.gif?format=1500w
layout: provider
modified: '2026-09-07'
name: Adarga
nav: Providers
network: true
overview: 'Adarga is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Defense, National Security, and Intelligence.


  Adarga''s developer surface includes engineering blog, support, and 12 more developer resources.'
plans:
- name: Adarga Plans Pricing
  plan_count: 0
  slug: adarga-plans-pricing
random_paper: 20
score:
  band: minimal
  composite: 8.9
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-kingdom
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - united-kingdom-ireland
  previous_composite: 8.9
  schema_version: 0.20.0
  scored_at: '2026-09-10'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Adarga Domain Security
  slug: adarga-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: adarga
tags:
- Company
- Artificial Intelligence
- Defense
- National Security
- Intelligence
- Analytics
- Natural Language Processing
- Data Fusion
- Machine Learning
- United Kingdom
website: https://www.adarga.ai/
---
