---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.9
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Europeana Agentic Access
  operation_count: 2
  slug: europeana-agentic-access
  summary_line: 2 operations
api_count: 1
apis:
- baseURL: https://api.europeana.eu/record/v2
  baseurl_source: declared
  description: Retrieve full metadata for a single record
  name: Europeana Record API
  slug: europeana-record-api
- baseURL: https://api.europeana.eu/record/v2
  baseurl_source: declared
  description: Discover records via keyword, faceted, and filtered search
  name: Europeana Search API
  slug: europeana-search-api
artifact_total: 12
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Europeana Search and Record API
  slug: open-europeana-record-api
- collection_type: open
  name: Europeana and Record Search API
  slug: open-europeana-search-api
- collection_type: open
  name: Europeana Search and Record API
  slug: open-europeana
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/europeana/api2/issues
- group: commercial
  title: ''
  type: License
  url: https://github.com/europeana/api2/blob/develop/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/europeana-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/europeana-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/europeana-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/europeana
- group: start
  title: ''
  type: Portal
  url: https://pro.europeana.eu/
- group: company
  title: ''
  type: News
  url: https://pro.europeana.eu/page/news
- group: other
  title: ''
  type: Events
  url: https://pro.europeana.eu/page/events
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.europeana.eu/en/rights
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.europeana.eu/en/rights/privacy-policy
- group: operate
  title: ''
  type: Contact
  url: https://pro.europeana.eu/about-us/office-employees
- group: build
  title: ''
  type: Libraries
  url: https://pro.europeana.eu/page/api-libraries-and-plugins
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/europeana/api2/releases/
- group: start
  title: ''
  type: GettingStarted
  url: https://pro.europeana.eu/page/record#get-started
- group: start
  title: ''
  type: Signup
  url: https://pro.europeana.eu/pages/get-api
created: '2023-11-23'
description: Europeana empowers the cultural heritage sector in its digital transformation. It develops expertise, tools, and policies to embrace digital change and encourage partnerships that foster innovation, making it easier for people to use cultural heritage for education, research, creation, and recreation. The Europeana platform aggregates metadata for over 50 million digitized items from more than 3,500 cultural institutions across Europe and exposes them through public APIs.
finops:
- name: Europeana Finops
  service_category: API
  slug: europeana-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/europeana.png
layout: provider
modified: '2026-05-19'
name: Europeana
nav: Providers
network: true
overview: 'Europeana publishes 2 APIs on the [APIs.io](https://apis.io/) network: Record API and Search API. Tagged areas include Archives, Cultural Heritage, Europe, Libraries, and Museums.


  Europeana''s developer surface includes authentication, developer portal, product news, changelog, getting-started guide, signup flow, and 10 more developer resources.'
plans:
- name: Europeana Plans Pricing
  plan_count: 3
  slug: europeana-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 5
  name: Europeana Rate Limits
  slug: europeana-rate-limits
score:
  band: developing
  composite: 44.0
  coverage:
    artifact_dirs: 9
    catalog_earned: 46.0
    catalog_earned_first_party: 0.0
    catalog_gap: 69.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 53.7
    developer_ergonomics: 50.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 28.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
  previous_composite: 44.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/europeana/refs/heads/main/screenshots/europeana-2026-07-25T213706.png
security:
- kind: authentication
  name: Europeana Authentication
  slug: europeana-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Europeana Domain Security
  slug: europeana-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: europeana
tags:
- Archives
- Cultural Heritage
- Europe
- Libraries
- Museums
- Search
website: https://pro.europeana.eu/
---
