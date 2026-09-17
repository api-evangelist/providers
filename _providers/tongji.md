---
access_model:
  confidence: high
  label: Free · thirteen interfaces open, the rest by institutional application
  onboarding: unknown
  pricing: free
  public: true
  source:
  - authentication
  - probed
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.5
  scored_at: '2026-09-16'
api_count: 7
apis:
- description: Tongji University's own SAML 2.0 identity provider, registered into eduGAIN by CARSI, the CERNET Authentication and Resource Sharing Infrastructure — China's national research and education identity f
  name: Tongji University Shibboleth Identity Provider (CARSI / eduGAIN)
  slug: identity-provider
- description: Tongji University is registered in the Research Organization Registry with ROR ID https://ror.org/03rc6as71 (同济大学, Shanghai, China). This is a registry membership, not a contract the university publis
  name: ROR Organization Registration
  slug: ror
- baseURL: https://api.tongji.edu.cn
  baseurl_source: declared
  description: Asynchronous speech-recognition and document-OCR services offered to campus applications by the Tongji University Information Office.
  name: Tongji University AI Services API
  slug: tongji-ai-services-api
- baseURL: https://api.tongji.edu.cn
  baseurl_source: declared
  description: Contract, equipment-asset and purchase-requisition records drawn from the university procurement and asset-management systems.
  name: Tongji University Assets and Procurement API
  slug: tongji-assets-and-procurement-api
- baseURL: https://api.tongji.edu.cn
  baseurl_source: declared
  description: Identity, qualification, degree, enrolment and insurance verification services backed by national and Shanghai municipal education data sources.
  name: Tongji University Education Data Verification API
  slug: tongji-education-data-verification-api
- baseURL: https://api.tongji.edu.cn
  baseurl_source: declared
  description: Library gate-access and loan records from the Tongji University Library systems.
  name: Tongji University Library API
  slug: tongji-library-api
- baseURL: https://api.tongji.edu.cn
  baseurl_source: declared
  description: Openly callable code tables (metadata dictionaries) that define the controlled vocabularies used across every other Open Platform interface.
  name: Tongji University Reference Metadata API
  slug: tongji-reference-metadata-api
- baseURL: https://api.tongji.edu.cn
  baseurl_source: declared
  description: Patent, software-copyright, project, funding, award, publication and monograph records from the university research-management systems.
  name: Tongji University Research API
  slug: tongji-research-api
artifact_total: 32
common:
- group: company
  title: ''
  type: Website
  url: https://www.tongji.edu.cn/
- group: company
  title: ''
  type: Website
  url: https://en.tongji.edu.cn/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.tongji.edu.cn/docs
- group: docs
  title: ''
  type: Documentation
  url: https://api.tongji.edu.cn/docs
- group: docs
  title: ''
  type: APIReference
  url: https://api.tongji.edu.cn/docs/interface
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/tongji/refs/heads/main/authentication/tongji-open-platform-authentication.yml
  title: ''
  type: Authentication
  url: authentication/tongji-open-platform-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/tongji/refs/heads/main/scopes/tongji-open-platform-scopes.yml
  title: ''
  type: Scopes
  url: scopes/tongji-open-platform-scopes.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/tongji/refs/heads/main/identity-federation/tongji-identity-federation.yml
  title: ''
  type: IdentityFederation
  url: identity-federation/tongji-identity-federation.yml
- group: operate
  title: ''
  type: Support
  url: https://api.tongji.edu.cn/docs/intro/apply/contact_us
- group: start
  title: ''
  type: Onboarding
  url: https://api.tongji.edu.cn/docs/intro/apply/teacher_apply
- group: start
  title: ''
  type: Onboarding
  url: https://api.tongji.edu.cn/docs/intro/apply/student_apply
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/tongji/refs/heads/main/security/tongji-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tongji-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/tongji-university/
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/tongji/refs/heads/main/plans/tongji-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/tongji-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/tongji/refs/heads/main/rate-limits/tongji-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/tongji-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/tongji/refs/heads/main/finops/tongji-finops.yml
  title: ''
  type: FinOps
  url: finops/tongji-finops.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/tongji/refs/heads/main/review.yml
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Tongji University (同济大学) is a public research university in Shanghai, China, in the national Double First-Class programme and ranked around #192 in the QS World University Rankings. Unlike most of the university cohort, its programmable footprint is real and it is the university''s own engineering, not a vendor''s: the Tongji University Information Office operates an institutional Open Platform at api.tongji.edu.cn — on China Education and Research Network address space, behind a KrakenD gateway, with its own Keycloak authorization server — publishing roughly 234 documented interfaces across fifteen families covering personnel, student, teaching, research, campus-card, library, asset, procurement, education-data verification, AI and notification services. Its OpenID Connect discovery document is live and lists 491 named OAuth scopes, one per interface for most of the catalog. Thirteen reference-metadata interfaces are documented as requiring no authorization and were confirmed
  anonymously callable, returning live JSON code tables; everything else is gated behind a faculty or student application-and-approval process. The university also runs its own Shibboleth SAML 2.0 identity provider, registered into eduGAIN through CARSI, China''s national research-and-education identity federation. What it does not have is a published contract: no OpenAPI, Swagger, Postman collection, sitemap, robots.txt, llms.txt or changelog is served anywhere on the platform, all documentation is Chinese-only, and there is no institutional repository, OAI-PMH endpoint, open-data portal, DataCite or Crossref membership. Every OpenAPI in this repo is API Evangelist''s derivation from Tongji''s published documentation, not a Tongji artifact.'
examples:
- key_count: 7
  name: Tongji V1 Metadata Asset Campus Gate Example
  slug: tongji-v1-metadata-asset-campus-gate-example
- key_count: 7
  name: Tongji V1 Metadata Meeting Meeting Room Example
  slug: tongji-v1-metadata-meeting-meeting-room-example
- key_count: 7
  name: Tongji V1 Metadata Teacher Send User Types Example
  slug: tongji-v1-metadata-teacher-send-user-types-example
- key_count: 7
  name: Tongji V1 Metadata Teacher Status Example
  slug: tongji-v1-metadata-teacher-status-example
- key_count: 7
  name: Tongji V1 Metadata Teacher Tech Job Code Example
  slug: tongji-v1-metadata-teacher-tech-job-code-example
- key_count: 7
  name: Tongji V1 Metadata Teacher Tech Job Level Code Example
  slug: tongji-v1-metadata-teacher-tech-job-level-code-example
- key_count: 7
  name: Tongji V1 Metadata Teacher Tech Level Of Workers Code Example
  slug: tongji-v1-metadata-teacher-tech-level-of-workers-code-example
- key_count: 7
  name: Tongji V1 Metadata Teacher Title Code Example
  slug: tongji-v1-metadata-teacher-title-code-example
- key_count: 7
  name: Tongji V1 Metadata Teacher Types Example
  slug: tongji-v1-metadata-teacher-types-example
- key_count: 7
  name: Tongji V1 Metadata User Person Idcard Type Example
  slug: tongji-v1-metadata-user-person-idcard-type-example
- key_count: 7
  name: Tongji V1 Metadata User Sex Code Example
  slug: tongji-v1-metadata-user-sex-code-example
- key_count: 7
  name: Tongji V2 Metadata Student Accom Building Code Example
  slug: tongji-v2-metadata-student-accom-building-code-example
- key_count: 7
  name: Tongji V2 Metadata Student Accom Region Code Example
  slug: tongji-v2-metadata-student-accom-region-code-example
finops:
- name: Tongji Finops
  service_category: Education
  slug: tongji-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tongji.png
json_schemas:
- name: Tongji University Open Platform Response Envelope
  property_count: 3
  slug: tongji-open-platform-envelope
- name: Tongji University Open Platform Record Schemas
  property_count: 0
  slug: tongji-open-platform-records
- name: Tongji University Open Platform Reference Metadata Code Table
  property_count: 3
  slug: tongji-reference-metadata-code-table
jsonld:
- class_count: 8
  name: Tongji Context
  property_count: 5
  slug: tongji-context
layout: provider
modified: '2026-09-01'
name: Tongji University
nav: Providers
network: true
overview: 'Tongji University publishes 6 APIs on the [APIs.io](https://apis.io/) network, including AI Services API, Assets and Procurement API, Education Data Verification API, and 3 more. Tagged areas include University, Higher Education, Education, China, and Shanghai.


  The Tongji University catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Tongji University''s developer surface includes documentation, API reference, authentication, support, and 13 more developer resources.'
plans:
- name: Tongji Plans Pricing
  plan_count: 2
  slug: tongji-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 3
  name: Tongji Rate Limits
  slug: tongji-rate-limits
rules:
- effective_rule_count: 0
  extends: []
  name: Tongji University API Rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: tongji-open-platform-rules
scopes:
- name: Tongji Open Platform Scopes
  scope_count: 0
  slug: tongji-open-platform-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 38.5
  coverage:
    artifact_dirs: 18
    catalog_earned: 86.0
    catalog_earned_first_party: 25.0
    catalog_gap: 29.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.4
  facets:
    access_clarity: 28.9
    contract_governance: 15.2
    contract_quality: 32.6
    developer_ergonomics: 42.9
    discoverability: 74.1
    operational_transparency: 31.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - china
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - greater-china
  previous_composite: 38.1
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 6
      marker_coverage: 100.0
      total: 6
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 50.0
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/tongji/refs/heads/main/screenshots/tongji-2026-06-20T195456.png
security:
- kind: authentication
  name: Tongji Open Platform Authentication
  slug: tongji-open-platform-authentication
  summary_line: none/oauth2/openid-connect/bearer · 4 schemes
- kind: domain-security
  name: Tongji Domain Security
  slug: tongji-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tongji
tags:
- University
- Higher Education
- Education
- China
- Shanghai
- Double First-Class
- Open Platform
- Campus Data
- Identity Federation
- Research Data
- Library
- Course Catalog
- Reference Data
website: https://www.tongji.edu.cn/
---
