---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
  scored_at: '2026-09-12'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/equal-employment-opportunity-commission-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/EEOC
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/eeoc
- group: company
  title: ''
  type: Website
  url: https://www.eeoc.gov
- group: start
  title: ''
  type: X-DataPortal
  url: https://www.eeoc.gov/data
- group: other
  title: ''
  type: X-EEOCExplore
  url: https://www.eeoc.gov/data/eeo-1-employer-information-report-statistics
- group: build
  title: ''
  type: X-EEO1DataCollection
  url: https://www.eeoc.gov/data/eeo-data-collections
- group: operate
  title: ''
  type: Contact
  url: https://www.eeoc.gov/contact-eeoc
- group: company
  title: ''
  type: Blog
  url: https://www.eeoc.gov/rss.xml
- group: other
  title: ''
  type: X-DCAT
  url: data-catalog/equal-employment-opportunity-commission-data-json.json
- group: other
  title: ''
  type: X-DataCatalog
  url: data-catalog/equal-employment-opportunity-commission-data-catalog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/equal-employment-opportunity-commission-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/equal-employment-opportunity-commission-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/equal-employment-opportunity-commission-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/equal-employment-opportunity-commission-rate-limits.yml
- group: build
  title: ''
  type: X-DataToolsAndProducts
  url: https://www.eeoc.gov/data/data-tools-and-products
- group: other
  title: ''
  type: X-DataGovernance
  url: https://www.eeoc.gov/data/data-governance
- group: other
  title: ''
  type: X-DataAndStatistics
  url: https://www.eeoc.gov/data/data-and-statistics
- group: company
  title: ''
  type: Newsroom
  url: https://www.eeoc.gov/newsroom
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.eeoc.gov/privacy-policy-us-equal-employment-opportunity-commission-web-site-and-mobile-app
- group: other
  title: ''
  type: X-Disclaimer
  url: https://www.eeoc.gov/disclaimer
- group: start
  title: ''
  type: X-PublicPortal
  url: https://publicportal.eeoc.gov/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/TheEEOC
- group: other
  title: ''
  type: X
  url: https://x.com/useeoc
created: '2024-12-03'
description: The U.S. Equal Employment Opportunity Commission (EEOC) is responsible for enforcing federal laws that make it illegal to discriminate against a job applicant or an employee because of the person's race, color, religion, sex (including pregnancy, childbirth, or related conditions, gender identity, and sexual orientation), national origin, age (40 or older), disability or genetic information. EEOC publishes EEO-1, EEO-3, EEO-4, and EEO-5 workforce demographic data through the EEOC Explore Tableau dashboards and downloadable bulk data files, and serves the federally required Project Open Data / DCAT-US public data listing at https://www.eeoc.gov/data.json — a 140-record dcat:Catalog in which every distribution is a file download rather than an API endpoint. It publishes no OpenAPI, GraphQL, MCP or event surface of any kind.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/equal-employment-opportunity-commission.png
layout: provider
modified: '2026-09-06'
name: Equal Employment Opportunity Commission
nav: Providers
network: true
overview: 'Equal Employment Opportunity Commission is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Federal-Government, Labor, Employment, Civil Rights, and Open Data.


  Equal Employment Opportunity Commission''s developer surface includes engineering blog, YouTube channel, and 22 more developer resources.'
plans:
- name: Equal Employment Opportunity Commission Plans Pricing
  plan_count: 0
  slug: equal-employment-opportunity-commission-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Equal Employment Opportunity Commission Rate Limits
  slug: equal-employment-opportunity-commission-rate-limits
score:
  band: emerging
  composite: 11.8
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.4
    operational_transparency: 2.6
  previous_composite: 11.8
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 27.8
  schema_version: 0.21.0
  scored_at: '2026-09-12'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/equal-employment-opportunity-commission/refs/heads/main/screenshots/equal-employment-opportunity-commission-2026-06-20T180800.png
security:
- kind: domain-security
  name: Equal Employment Opportunity Commission Domain Security
  slug: equal-employment-opportunity-commission-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
slug: equal-employment-opportunity-commission
tags:
- Federal-Government
- Labor
- Employment
- Civil Rights
- Open Data
website: https://www.eeoc.gov
---
