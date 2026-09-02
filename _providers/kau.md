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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.0
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: King Abdulaziz University's own open data web service. A single GET endpoint, /api/StudentsData, returns aggregate student enrollment and graduation counts broken down by faculty, department, educatio
  name: KAU Open Data API
  slug: open-data
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
  slug: scientific-platform
- description: KAU holds two Crossref memberships in its own name. Member 2709, "King Abdulaziz University Scientific Publishing Centre", operates DOI prefix 10.4197 with 1,920 registered DOIs of which 358 are curre
  name: Crossref membership
  slug: crossref
- description: 'King Abdulaziz University is registered in ROR as https://ror.org/02ma4wv74, with declared domain kau.edu.sa, types education and funder, and cross-references to Crossref Funder ID 501100004054, GRID '
  name: ROR registration
  slug: ror
artifact_total: 16
common:
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
  title: ''
  type: IdentityFederation
  url: identity-federation/kau-identity-federation.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/kau-conformance.yml
- group: auth
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
  title: ''
  type: DomainSecurity
  url: security/kau-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/kau-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/kau-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/kau-finops.yml
- group: other
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
- name: Kau Finops
  service_category: Education
  slug: kau-finops
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
modified: '2026-09-01'
name: King Abdulaziz University
nav: Providers
network: true
overview: 'King Abdulaziz University publishes 1 API on the [APIs.io](https://apis.io/) network: KAU Open Data API. Tagged areas include University, Higher Education, Education, Research, and Open Data.


  The King Abdulaziz University catalog on APIs.io includes 1 JSON-LD context.


  King Abdulaziz University''s developer surface includes authentication and 13 more developer resources.'
plans:
- name: Kau Plans Pricing
  plan_count: 2
  slug: kau-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 1
  name: Kau Rate Limits
  slug: kau-rate-limits
score:
  band: emerging
  composite: 25.3
  coverage:
    artifact_dirs: 14
    catalog_gap: 48.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 4.5
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 3.8
    contract_quality: 26.7
    developer_ergonomics: 15.5
    discoverability: 59.3
    governance: 3.8
    operational_transparency: 21.1
  previous_composite: 20.8
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
    score: 31.5
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kau/refs/heads/main/screenshots/kau-2026-06-20T183925.png
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
- Learning Management
- Saudi Arabia
- Middle East
website: https://www.kau.edu.sa/en
---
