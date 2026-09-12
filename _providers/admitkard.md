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
  scored_at: '2026-09-12'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://www.admitkard.com/
- group: company
  title: ''
  type: Blog
  url: https://www.admitkard.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/admitkard
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.admitkard.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.admitkard.com/privacy
- group: auth
  title: ''
  type: DomainSecurity
  url: security/admitkard-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/admitkard-llms.txt
coverage:
  checked: '2026-09-07'
  detail: AdmitKard sells study-abroad counselling to students, not a developer product — there is no developer portal, API reference, SDK or machine-readable contract anywhere on its surface, and its own API host api.admitkard.com answers every path with a Cloudflare 522 origin timeout.
  evidence:
  - status: 522
    url: https://api.admitkard.com/openapi.json
  - status: 404
    url: https://www.admitkard.com/openapi.json
  - status: 404
    url: https://www.admitkard.com/llms.txt
  - status: 404
    url: https://www.admitkard.com/.well-known/api-catalog
  - status: 200
    url: https://github.com/admitkard
  reason: no-developer-program
  state: none
created: '2026-09-07'
description: 'AdmitKard is a Noida, India based study-abroad EdTech company, founded in 2016 by IIT-IIM alumni Piyush Bhartiya and Rachit Agrawal, that guides Indian students through the full overseas-education journey: university and course shortlisting, profile building, test preparation, applications, SOP/LOR support, scholarships, education loans, foreign-exchange remittance, student visas and accommodation. The company is an ICEF-accredited and AIRC-certified agency and raised a Rs 50 crore (about $6M) Series A led by GSV Ventures in 2023. It sells counselling services to students and universities rather than a developer product: as of this profile it publishes no public API, developer portal, SDK or machine-readable contract, and its api.admitkard.com host answers with a Cloudflare 522 origin timeout.'
image: https://www.admitkard.com/admitkard-logo-color.png
layout: provider
modified: '2026-09-07'
name: Admitkard
nav: Providers
network: true
overview: 'Admitkard is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Education, EdTech, Study Abroad, and Higher Education.


  Admitkard''s developer surface includes engineering blog and 6 more developer resources.'
random_paper: 0
score:
  band: minimal
  composite: 10.5
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
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.4
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - india
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - india-south-asia
  previous_composite: 10.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 25.9
  schema_version: 0.21.0
  scored_at: '2026-09-12'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Admitkard Domain Security
  slug: admitkard-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: admitkard
tags:
- Company
- Education
- EdTech
- Study Abroad
- Higher Education
- Student Recruitment
- Admissions
- Counseling
- India
website: https://www.admitkard.com/
---
