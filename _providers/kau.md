---
access_model:
  confidence: high
  label: Free · no credential required
  onboarding: unknown
  pricing: free
  public: true
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
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
    openapi_examples: verified
    operation_distinctiveness: na
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: King Abdulaziz University's institutional SAML 2.0 identity provider, running Oracle Access Manager Federation at /oamfed/idp/samlv20. The IdP itself is unreachable from outside Saudi Arabia, so it wa
  name: KAU SAML 2.0 Identity Provider
  slug: identity-federation
- description: 'KAU''s Scientific Publishing Centre journals delivered on Elsevier''s Digital Commons (bepress) platform, with a fully working OAI-PMH 2.0 data provider carrying records back to 2000-01-19. This is the '
  name: King Abdulaziz University Journals (Digital Commons tenancy)
  slug: journals-digital-commons
- description: King Abdulaziz University's learning management system, a Blackboard Learn SaaS tenancy. The Blackboard Learn REST API is genuinely provisioned here — /learn/api/public/v1/system/version returns 200 w
  name: KAU Blackboard Learn (LMS tenancy)
  slug: blackboard-learn
- description: KAU's library discovery and scientific content platform, branded "King Abdulaziz scientific platform" and running on Al Manhal. Live at HTTP 200. No public API, OAI-PMH endpoint or machine-readable co
  name: King Abdulaziz Scientific Platform (Al Manhal tenancy)
  provenance: unpublished
  slug: scientific-platform
- description: KAU holds two Crossref memberships in its own name. Member 2709, "King Abdulaziz University Scientific Publishing Centre", operates DOI prefix 10.4197 with 1,920 registered DOIs of which 358 are curre
  name: Crossref membership
  slug: crossref
- description: 'King Abdulaziz University is registered in ROR as https://ror.org/02ma4wv74, with declared domain kau.edu.sa, types education and funder, and cross-references to Crossref Funder ID 501100004054, GRID '
  name: ROR registration
  slug: ror
- baseURL: https://opendata.kau.edu.sa/api/StudentsData
  baseurl_source: declared
  description: Aggregate student enrollment and graduation statistics.
  name: King Abdulaziz University Students Data API
  slug: kau-studentsdata-api
artifact_total: 17
common:
- group: company
  title: ''
  type: Blog
  url: https://www.kau.edu.sa/en/news
- group: company
  title: ''
  type: Website
  url: https://www.kau.edu.sa/en
- group: other
  title: ''
  type: OpenData
  url: https://www.kau.edu.sa/page/open-data
- group: other
  title: ''
  type: ResearchRepository
  url: https://kauj.researchcommons.org/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://libsp.kau.edu.sa/
- group: other
  href: https://artifacts.apis.io/kau/identity-federation/kau-identity-federation.yml
  title: ''
  type: IdentityFederation
  url: identity-federation/kau-identity-federation.yml
- group: design
  href: https://artifacts.apis.io/kau/conformance/kau-conformance.yml
  title: ''
  type: Conformance
  url: conformance/kau-conformance.yml
- group: auth
  href: https://artifacts.apis.io/kau/authentication/kau-authentication.yml
  title: ''
  type: Authentication
  url: authentication/kau-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/king-abdulaziz-university
- group: company
  title: ''
  type: Twitter
  url: https://x.com/kauedu_sa
- group: auth
  href: https://artifacts.apis.io/kau/security/kau-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/kau-domain-security.yml
- group: commercial
  href: https://artifacts.apis.io/kau/plans/kau-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/kau-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/kau/rate-limits/kau-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/kau-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/kau/finops/kau-finops.yml
  title: ''
  type: FinOps
  url: finops/kau-finops.yml
- group: other
  href: https://artifacts.apis.io/kau/review.yml
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: King Abdulaziz University (KAU) is a large public research university in Jeddah, Saudi Arabia, serving over 100,000 students across 30 faculties and institutes including a branch campus at Rabigh. Its programmable footprint is small but, unusually for this cohort, partly its own. KAU operates a genuine institution-run Open Data API at opendata.kau.edu.sa returning aggregate student enrollment and graduation statistics as JSON over eight documented, unauthenticated GET invocations, and it operates its own SAML 2.0 identity provider at iam.kau.edu.sa/oamfed/idp/samlv20 on Oracle Access Manager Federation, self-hosted in KAU's own 192.162.72.0/24 address block with no managed-IdP vendor underneath it. Everything else that looks like a KAU API belongs to somebody else. The best machine-readable surface associated with the university — a complete OAI-PMH 2.0 data provider carrying its journals back to 2000 — is Elsevier's Digital Commons at kauj.researchcommons.org, administered
  from dc-support@elsevier.com. Its learning platform is a Blackboard Learn SaaS tenancy on lms.kau.edu.sa, and its scientific platform at libsp.kau.edu.sa is an Al Manhal tenancy. All three are recorded here as tenant relationships and none of their contracts is claimed as KAU's. KAU is a Crossref member in its own right under DOI prefix 10.4197 and is registered in ROR. It holds no DataCite account, publishes no SAML metadata, and belongs to neither the Maeen national identity federation nor eduGAIN although thirty-eight Saudi entities do. There is no developer portal, no API key or client registration of any kind, no official GitHub organisation, and no OpenAPI — the specification in this repository is derived by API Evangelist from KAU's published endpoints and a real response body, not published by KAU.
examples:
- key_count: 1
  name: Kau Lms System Version Example
  slug: kau-lms-system-version-example
- key_count: 2
  name: Kau Lms Unauthenticated Error Example
  slug: kau-lms-unauthenticated-error-example
finops:
- has_sources: true
  method: generated
  name: Kau Finops
  primary_unit: ''
  service_category: Education
  slug: kau-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kau.png
json_schemas:
- name: King Abdulaziz University Open Data — StudentsData record
  property_count: 0
  slug: kau-students-data
jsonld:
- class_count: 6
  name: Kau Context
  property_count: 2
  slug: kau-context
layout: provider
modified: '2026-10-06'
name: King Abdulaziz University
nav: Providers
network: true
overview: 'King Abdulaziz University publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Students Data API. Tagged areas include University, Higher Education, Education, Research, and Open Data.


  The King Abdulaziz University catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  King Abdulaziz University''s developer surface includes engineering blog, authentication, and 13 more developer resources.'
plans:
- name: Kau Plans Pricing
  plan_count: 2
  slug: kau-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 1
  name: Kau Rate Limits
  slug: kau-rate-limits
rules:
- authorship: generated
  effective_rule_count: 97
  extends:
  - spectral:oas
  name: King Abdulaziz University API Rules
  rule_count: 56
  severity_counts:
    error: 54
    hint: 0
    info: 1
    warn: 1
  slug: kau-rules
score:
  band: emerging
  composite: 20.0
  coverage:
    artifact_dirs: 19
    catalog_earned: 51.3
    catalog_earned_first_party: 0.0
    catalog_gap: 63.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 5.3
    contract_governance: 17.4
    contract_quality: 23.8
    developer_ergonomics: 23.8
    discoverability: 57.1
    operational_transparency: 5.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - saudi-arabia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - mena
    - middle-east
  previous_composite: 20.0
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
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
screenshot: https://apis.io/screenshots/kau/kau-2026-06-20T183925.png
security:
- kind: authentication
  name: Kau Authentication
  slug: kau-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Kau Domain Security
  slug: kau-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: kau
tags:
- University
- Higher Education
- Education
- Research
- Open Data
- Research Repository
- Identity Federation
- LMS
- Saudi Arabia
- Middle East
website: https://www.kau.edu.sa/en
---
