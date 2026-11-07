---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.9
  scored_at: '2026-11-06'
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
  name: Europeana Search and Record API
  slug: open-europeana-record-api
- collection_type: open
  name: Europeana and Record Search API
  slug: open-europeana-search-api
- collection_type: open
  name: Europeana Search and Record API
  slug: open-europeana
common:
- group: commercial
  href: https://artifacts.apis.io/europeana/plans/europeana-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/europeana-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/europeana/rate-limits/europeana-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/europeana-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/europeana/finops/europeana-finops.yml
  title: ''
  type: FinOps
  url: finops/europeana-finops.yml
- group: company
  title: ''
  type: Website
  url: https://europeana.eu
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/europeana/api2/issues
- group: commercial
  title: ''
  type: License
  url: https://github.com/europeana/api2/blob/develop/LICENSE
- group: agent
  href: https://artifacts.apis.io/europeana/agentic-access/europeana-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/europeana-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/europeana/security/europeana-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/europeana-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/europeana/authentication/europeana-authentication.yml
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
- has_sources: false
  method: generated
  name: Europeana Finops
  primary_unit: request
  service_category: API
  slug: europeana-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/europeana.png
layout: provider
modified: '2026-09-16'
name: Europeana
nav: Providers
network: true
overview: 'Europeana publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Record API and Search API. Tagged areas include Archives, Cultural Heritage, Europe, Library, and Museums.


  The Europeana catalog on APIs.io includes 1 Spectral governance ruleset.


  Europeana''s developer surface includes authentication, developer portal, product news, changelog, getting-started guide, signup flow, and 14 more developer resources.'
plans:
- name: Europeana Plans Pricing
  plan_count: 3
  slug: europeana-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 5
  name: Europeana Rate Limits
  slug: europeana-rate-limits
rules:
- authorship: generated
  effective_rule_count: 101
  extends:
  - spectral:oas
  name: Europeana API Rules
  rule_count: 60
  severity_counts:
    error: 58
    hint: 0
    info: 1
    warn: 1
  slug: europeana-rules
score:
  band: developing
  composite: 42.9
  coverage:
    artifact_dirs: 14
    catalog_earned: 47.5
    catalog_earned_first_party: 0.0
    catalog_gap: 67.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 42.1
    contract_governance: 13.6
    contract_quality: 48.4
    developer_ergonomics: 50.0
    discoverability: 67.9
    operational_transparency: 28.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
  previous_composite: 42.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 19.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/europeana/europeana-2026-07-25T213706.png
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
- Library
- Museums
- Search
- OAI-PMH
website: https://europeana.eu
---
