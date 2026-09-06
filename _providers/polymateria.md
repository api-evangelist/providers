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
- group: auth
  title: ''
  type: DomainSecurity
  url: security/polymateria-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.polymateria.com/
- group: company
  title: ''
  type: About
  url: https://www.polymateria.com/about-us/what-is-biotransformation/
- group: company
  title: ''
  type: Blog
  url: https://www.polymateria.com/media-centre/newsroom/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.polymateria.com/feed/
- group: operate
  title: ''
  type: Support
  url: https://www.polymateria.com/contacts/get-in-touch/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.polymateria.com/terms-and-conditions-of-supply-and-purchase/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.polymateria.com/privacy-and-cookies/
- group: start
  title: ''
  type: CustomerPortal
  url: https://www.polymateria.com/customer-portal/
- group: company
  title: ''
  type: Careers
  url: https://www.polymateria.com/careers/current-opportunities/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/polymateria
- group: other
  title: ''
  type: Sitemap
  url: https://www.polymateria.com/sitemap_index.xml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/polymateria-llms.txt
coverage:
  checked: '2026-08-26'
  detail: Polymateria sells a chemical masterbatch additive that makes polyolefins biodegrade, not software — the whole of www.polymateria.com is a WordPress marketing site whose only machine-readable surface is the stock /wp-json/ CMS API, and api/docs/developer/app/portal subdomains do not resolve at all.
  evidence:
  - status: 404
    url: https://www.polymateria.com/openapi.json
  - status: 404
    url: https://www.polymateria.com/.well-known/agent-card.json
  - status: 200
    url: https://www.polymateria.com/wp-json/
  - status: 200
    url: https://www.polymateria.com/customer-portal/
  reason: not-a-software-company
  state: none
created: '2026-08-26'
description: 'Polymateria Ltd is a British materials-science company, based at the Imperial College I-HUB on the White City Campus in London, that develops Biotransformation — a masterbatch additive blended into polyethylene and polypropylene at roughly 2% by weight so that plastic which escapes a waste stream weathers into a bioavailable wax and fully biodegrades in the open environment without leaving microplastics behind. The company co-authored BSI PAS 9017, the first standard for measuring the biodegradability of polyolefins, is a World Economic Forum Technology Pioneer and a Terra Carta signatory, and sells to converters, brand owners and packaging manufacturers rather than to developers. Its product is a chemical additive, not software: the public website is a WordPress marketing and media site, and the only credentialed surface it operates is a customer portal that serves third-party test datasets as documents. No developer program, public API, SDK or machine-readable API contract
  of any kind was found in this pass.'
image: https://wp-polymateria-2020.s3.eu-west-2.amazonaws.com/media/2019/02/polymateria-logo.svg
layout: provider
modified: '2026-08-26'
name: Polymateria
nav: Providers
network: true
overview: 'Polymateria is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Materials Science, Plastics, Biodegradable Plastics, and Sustainability.


  Polymateria''s developer surface includes engineering blog, support, and 11 more developer resources.'
random_paper: 15
score:
  band: emerging
  composite: 11.4
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
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 11.4
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/polymateria/refs/heads/main/screenshots/polymateria-2026-09-02T151706.png
security:
- kind: domain-security
  name: Polymateria Domain Security
  slug: polymateria-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: polymateria
tags:
- Company
- Materials Science
- Plastics
- Biodegradable Plastics
- Sustainability
- Chemicals
- Packaging
- Circular Economy
- Manufacturing
website: https://www.polymateria.com/
---
