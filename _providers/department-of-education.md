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
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Department Of Education Agentic Access
  operation_count: 1
  slug: department-of-education-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- description: The College Scorecard API provides programmatic access to postsecondary institution and field-of-study data published by the U.S. Department of Education. The API exposes more than 6,000 schools and o
  name: College Scorecard API
  slug: college-scorecard-api
- description: The Department of Education Open Data Platform (ODP) at data.ed.gov is built on CKAN and exposes a CKAN-compatible REST API for searching, retrieving, and downloading the Department's public datasets.
  name: Department of Education Open Data Platform API
  slug: open-data-platform-api
- description: The Integrated Postsecondary Education Data System (IPEDS) gathers data annually from every college, university, and technical and vocational institution that participates in the federal student finan
  name: IPEDS Data
  slug: ipeds-data
- baseURL: https://api.data.gov/ed/collegescorecard/v1
  baseurl_source: declared
  description: The Schools API from Department of Education — 1 operation(s) for schools.
  name: Department of Education Schools API
  slug: department-of-education-schools-api
artifact_total: 14
collections:
- collection_type: open
  name: U.S. Department of Education — College Scorecard Schools API
  slug: open-department-of-education-schools-api
- collection_type: open
  name: U.S. Department of Education — College Scorecard API
  slug: open-department-of-education
common:
- group: commercial
  href: https://artifacts.apis.io/department-of-education/plans/department-of-education-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/department-of-education-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/department-of-education/rate-limits/department-of-education-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/department-of-education-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/department-of-education/finops/department-of-education-finops.yml
  title: ''
  type: FinOps
  url: finops/department-of-education-finops.yml
- group: agent
  href: https://artifacts.apis.io/department-of-education/agentic-access/department-of-education-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/department-of-education-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/department-of-education/security/department-of-education-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/department-of-education-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/department-of-education/authentication/department-of-education-authentication.yml
  title: ''
  type: Authentication
  url: authentication/department-of-education-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/usedgov
- group: company
  title: ''
  type: Website
  url: https://www.ed.gov
- group: other
  title: ''
  type: Open Data Platform
  url: https://data.ed.gov/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.data.gov/
- group: other
  title: ''
  type: NCES
  url: https://nces.ed.gov/
- group: other
  title: ''
  type: College Scorecard
  url: https://collegescorecard.ed.gov/
- group: other
  title: ''
  type: Federal Student Aid
  url: https://studentaid.gov
- group: other
  title: ''
  type: Data.gov ED Catalog
  url: https://catalog.data.gov/dataset?organization=ed-gov
- group: company
  title: ''
  type: News
  url: https://www.ed.gov/news
- group: operate
  title: ''
  type: Contact
  url: https://www.ed.gov/about/contact-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ed.gov/notices/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/usedgov
- group: design
  href: https://artifacts.apis.io/department-of-education/json-ld/department-of-education-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/department-of-education-context.jsonld
- group: design
  href: https://artifacts.apis.io/department-of-education/vocabulary/department-of-education-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/department-of-education-vocabulary.yml
- group: company
  title: ''
  type: Blog
  url: https://www.ed.gov/rss.xml
- group: company
  title: ''
  type: About
  url: https://www2.ed.gov/about/inits/ed/edfacts/index.html
created: '2024-12-03'
description: The U.S. Department of Education (ED) is a federal agency that manages and coordinates federal assistance to education and establishes policy for it. ED's mission is to promote student achievement and preparation for global competitiveness, and to ensure equal access to education. The Department exposes a portfolio of public APIs through api.data.gov, NCES, and the Open Data Platform (ODP) at data.ed.gov for postsecondary outcomes, institutional characteristics, and federal education programs.
finops:
- has_sources: false
  method: generated
  name: Department Of Education Finops
  primary_unit: request
  service_category: API
  slug: department-of-education-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/department-of-education.png
jsonld:
- class_count: 0
  name: Department Of Education Context
  property_count: 5
  slug: department-of-education-context
layout: provider
modified: '2026-07-25'
name: Department of Education
nav: Providers
network: true
overview: 'Department of Education publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Schools API, and 3 more. Tagged areas include College Scorecard, Education, Federal Government, Higher Education, and IPEDS.


  The Department of Education catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Department of Education''s developer surface includes authentication, product news, engineering blog, and 19 more developer resources.'
plans:
- name: Department Of Education Plans Pricing
  plan_count: 3
  slug: department-of-education-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 5
  name: Department Of Education Rate Limits
  slug: department-of-education-rate-limits
rules:
- authorship: generated
  effective_rule_count: 94
  extends:
  - spectral:oas
  name: Department of Education API Rules
  rule_count: 53
  severity_counts:
    error: 51
    hint: 0
    info: 1
    warn: 1
  slug: department-of-education-rules
score:
  band: thin
  composite: 35.2
  coverage:
    artifact_dirs: 18
    catalog_earned: 57.0
    catalog_earned_first_party: 0.0
    catalog_gap: 58.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 27.3
    contract_quality: 53.0
    developer_ergonomics: 33.3
    discoverability: 67.0
    operational_transparency: 10.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 35.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/department-of-education/department-of-education-2026-06-20T175915.png
security:
- kind: authentication
  name: Department Of Education Authentication
  slug: department-of-education-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Department Of Education Domain Security
  slug: department-of-education-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: department-of-education
tags:
- College Scorecard
- Education
- Federal Government
- Higher Education
- IPEDS
- K-12
- NCES
- Open Data
- Postsecondary
website: https://www.ed.gov
---
