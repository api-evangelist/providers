---
access_model:
  confidence: high
  label: Free, but gated — jAccount required, application approved per scope
  onboarding: unknown
  pricing: free
  public: false
  source:
  - authentication/shanghai-jiao-tong-university-authentication.yml
  - https://developer.sjtu.edu.cn/api/overview.html
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.8
  scored_at: '2026-09-16'
api_count: 3
apis:
- description: SJTU's own identity and single sign-on system, run by the Network and Information Center on the university's own domain. It is a real OAuth 2.0 authorization server — an unparameterised GET of the aut
  name: jAccount Authorization Server (OAuth 2.0 / OpenID Connect)
  slug: jaccount-oauth
- description: SJTU operates a Shibboleth identity provider and publishes its SAML metadata openly at https://jaccount.sjtu.edu.cn/idp/shibboleth — entityID matching the URL, shibmd:Scope sjtu.edu.cn, display name "
  name: SJTU Identity Provider (Shibboleth / SAML 2.0)
  slug: jaccount-shibboleth
- description: SJTU's campus super-app and the low-code process platform behind it, on which the university and approved third parties build workflow applications for staff and students. The developer portal ships a
  name: Jiao Wo Ban (交我办) Process Platform
  slug: jiaowoban
- baseURL: https://api.sjtu.edu.cn
  baseurl_source: declared
  description: '账号类 — account records: jAccount name, staff/student number, display name, unit, ID document, identity type and account status.'
  name: Shanghai Jiao Tong University Account API
  slug: shanghai-jiao-tong-university-account-api
- baseURL: https://api.sjtu.edu.cn
  baseurl_source: declared
  description: 资产类 — institutional asset records, keyed by asset type, company code, applicant, keeper, business year and status.
  name: Shanghai Jiao Tong University Asset API
  slug: shanghai-jiao-tong-university-asset-api
- baseURL: https://api.sjtu.edu.cn
  baseurl_source: declared
  description: Barcode and QR-code image rendering.
  name: Shanghai Jiao Tong University Barcode API
  slug: shanghai-jiao-tong-university-barcode-api
- baseURL: https://api.sjtu.edu.cn
  baseurl_source: declared
  description: Calendar event synchronisation into the campus calendar.
  name: Shanghai Jiao Tong University Calendar API
  slug: shanghai-jiao-tong-university-calendar-api
- baseURL: https://api.sjtu.edu.cn
  baseurl_source: declared
  description: Campus card (一卡通) — account opening, balance, transactions, photo, top-up, freeze and transfer.
  name: Shanghai Jiao Tong University Card API
  slug: shanghai-jiao-tong-university-card-api
- baseURL: https://api.sjtu.edu.cn
  baseurl_source: declared
  description: Teaching records — lessons, student timetables, examinations and GPA.
  name: Shanghai Jiao Tong University Education API
  slug: shanghai-jiao-tong-university-education-api
- baseURL: https://api.sjtu.edu.cn
  baseurl_source: declared
  description: Enterprise directory — posts, identities, rights, organizational units and the academic calendar.
  name: Shanghai Jiao Tong University Enterprise API
  slug: shanghai-jiao-tong-university-enterprise-api
- baseURL: https://api.sjtu.edu.cn
  baseurl_source: declared
  description: '教职工类 — faculty and staff records: basic profile, degrees, and Party/administrative posts.'
  name: Shanghai Jiao Tong University Faculty API
  slug: shanghai-jiao-tong-university-faculty-api
- baseURL: https://api.sjtu.edu.cn
  baseurl_source: declared
  description: Application file storage — upload, download, metadata, thumbnails and WPS preview/edit links.
  name: Shanghai Jiao Tong University File API
  slug: shanghai-jiao-tong-university-file-api
- baseURL: https://api.sjtu.edu.cn
  baseurl_source: declared
  description: Finance appointment workflow — submit, cancel, complete and query financial business items.
  name: Shanghai Jiao Tong University Finance API
  slug: shanghai-jiao-tong-university-finance-api
- baseURL: https://api.sjtu.edu.cn
  baseurl_source: declared
  description: Campus mail — read, send and mark messages on the user's behalf.
  name: Shanghai Jiao Tong University Mail API
  slug: shanghai-jiao-tong-university-mail-api
- baseURL: https://api.sjtu.edu.cn
  baseurl_source: declared
  description: Campus notification delivery and read-state tracking, including Jiao-Wo-Ban (交我办) app pushes.
  name: Shanghai Jiao Tong University Notification API
  slug: shanghai-jiao-tong-university-notification-api
- baseURL: https://api.sjtu.edu.cn
  baseurl_source: declared
  description: 论文类 — academic paper and publication metadata.
  name: Shanghai Jiao Tong University Paper API
  slug: shanghai-jiao-tong-university-paper-api
- baseURL: https://api.sjtu.edu.cn
  baseurl_source: declared
  description: User profile — identity, name, default identity type and organizational unit, with field-level scope control.
  name: Shanghai Jiao Tong University Profile API
  slug: shanghai-jiao-tong-university-profile-api
- baseURL: https://api.sjtu.edu.cn
  baseurl_source: declared
  description: Digital document signing (e-signature).
  name: Shanghai Jiao Tong University Signature API
  slug: shanghai-jiao-tong-university-signature-api
- baseURL: https://api.sjtu.edu.cn
  baseurl_source: declared
  description: InfoPlus task centre — push workflow task updates into the campus task centre.
  name: Shanghai Jiao Tong University Task API
  slug: shanghai-jiao-tong-university-task-api
- baseURL: https://api.sjtu.edu.cn
  baseurl_source: declared
  description: '本科教学类 — undergraduate teaching records: student profile, course catalog, scheduling, and course selection.'
  name: Shanghai Jiao Tong University Undergraduate Teaching API
  slug: shanghai-jiao-tong-university-undergraduate-teaching-api
- baseURL: https://api.sjtu.edu.cn
  baseurl_source: declared
  description: Siyuan code (思源码) — the campus identity and payment QR code, its activation, payment codes and transactions.
  name: Shanghai Jiao Tong University Unicode API
  slug: shanghai-jiao-tong-university-unicode-api
artifact_total: 33
common:
- group: company
  title: ''
  type: Website
  url: https://en.sjtu.edu.cn/
- group: company
  title: ''
  type: About
  url: https://www.sjtu.edu.cn/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.sjtu.edu.cn/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.sjtu.edu.cn/api/overview.html
- group: docs
  title: ''
  type: APIReference
  url: https://developer.sjtu.edu.cn/api/list.html
- group: auth
  title: ''
  type: Authentication
  url: https://developer.sjtu.edu.cn/auth/oauth.html
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/shanghai-jiao-tong-university/refs/heads/main/scopes/shanghai-jiao-tong-university-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/shanghai-jiao-tong-university-scopes.yml
- group: build
  title: ''
  type: SDKs
  url: https://developer.sjtu.edu.cn/api/sdk.html
- group: start
  title: ''
  type: SignUp
  url: https://my.sjtu.edu.cn/
- group: other
  title: ''
  type: IdentityFederation
  url: https://jaccount.sjtu.edu.cn/idp/shibboleth
- group: other
  title: ''
  type: ResearchComputing
  url: https://docs.hpc.sjtu.edu.cn/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://www.lib.sjtu.edu.cn/
- group: other
  title: ''
  type: ResearchRepository
  url: https://scholar.sjtu.edu.cn/
- group: other
  title: ''
  type: AIPolicy
  url: https://www.sjtu.edu.cn/tg/20250304/207682.html
- group: build
  title: ''
  type: AITooling
  url: https://ctld.sjtu.edu.cn/teaching/page/203
- group: company
  title: ''
  type: Blog
  url: https://news.sjtu.edu.cn/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sjtug
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/shanghai-jiao-tong-university/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/shanghai-jiao-tong-university/refs/heads/main/security/shanghai-jiao-tong-university-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/shanghai-jiao-tong-university-domain-security.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/shanghai-jiao-tong-university/refs/heads/main/plans/shanghai-jiao-tong-university-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/shanghai-jiao-tong-university-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/shanghai-jiao-tong-university/refs/heads/main/rate-limits/shanghai-jiao-tong-university-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/shanghai-jiao-tong-university-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/shanghai-jiao-tong-university/refs/heads/main/finops/shanghai-jiao-tong-university-finops.yml
  title: ''
  type: FinOps
  url: finops/shanghai-jiao-tong-university-finops.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/shanghai-jiao-tong-university/refs/heads/main/well-known/shanghai-jiao-tong-university-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/shanghai-jiao-tong-university-well-known.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/shanghai-jiao-tong-university/refs/heads/main/conformance/shanghai-jiao-tong-university-conformance.yml
  title: ''
  type: Conformance
  url: conformance/shanghai-jiao-tong-university-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/shanghai-jiao-tong-university/refs/heads/main/vocabulary/shanghai-jiao-tong-university-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/shanghai-jiao-tong-university-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/shanghai-jiao-tong-university/refs/heads/main/json-ld/shanghai-jiao-tong-university-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/shanghai-jiao-tong-university-context.jsonld
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/shanghai-jiao-tong-university/refs/heads/main/review.yml
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Shanghai Jiao Tong University (上海交通大学, SJTU), founded 1896 in Shanghai, is a C9 League public research university and one of very few institutions anywhere that operates a first-party API platform rather than buying one. Its Network and Information Center runs a documented developer portal covering three institution-operated surfaces, all on sjtu.edu.cn and none a vendor tenancy: the jAccount OAuth 2.0 / OpenID Connect / Shibboleth identity provider; a REST Open API at api.sjtu.edu.cn with 59 documented operations across 13 families (profile, directory, campus card, Siyuan payment code, timetables, exams and GPA, mail, notifications, files, finance, barcode, calendar, e-signature); and a gated Data Resources API. Alongside sit the 交我办 campus super-app and the 交我算 HPC service. What SJTU does not publish is equally real: no OpenAPI, changelog, status page, deprecation policy or self-service signup; docs only in Chinese; and no Crossref, DataCite, ORCID or OAI-PMH anywhere.'
finops:
- name: Shanghai Jiao Tong University Finops
  service_category: Education
  slug: shanghai-jiao-tong-university-finops
graphqls:
- description: '<!-- authorship: rewritten 2026-08-30 by the API Evangelist university pipeline.'
  name: Shanghai Jiao Tong University — Data Resources GraphQL API (SUPERSEDED)
  slug: shanghai-jiao-tong-university-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/shanghai-jiao-tong-university.png
json_schemas:
- name: SJTU Data Resources Account Record
  property_count: 15
  slug: shanghai-jiao-tong-university-account-info
- name: SJTU API Response Envelope
  property_count: 5
  slug: shanghai-jiao-tong-university-envelope
- name: SJTU jAccount Profile
  property_count: 12
  slug: shanghai-jiao-tong-university-profile
jsonld:
- class_count: 9
  name: Shanghai Jiao Tong University Context
  property_count: 5
  slug: shanghai-jiao-tong-university-context
layout: provider
modified: '2026-08-30'
name: Shanghai Jiao Tong University
nav: Providers
network: true
overview: 'Shanghai Jiao Tong University publishes 18 APIs on the [APIs.io](https://apis.io/) network, including Account API, Asset API, Barcode API, and 15 more. Tagged areas include University, Higher Education, Education, Research, and China.


  The Shanghai Jiao Tong University catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Shanghai Jiao Tong University''s developer surface includes documentation, API reference, authentication, signup flow, engineering blog, and 22 more developer resources.'
plans:
- name: Shanghai Jiao Tong University Plans Pricing
  plan_count: 2
  slug: shanghai-jiao-tong-university-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 1
  name: Shanghai Jiao Tong University Rate Limits
  slug: shanghai-jiao-tong-university-rate-limits
rules:
- effective_rule_count: 0
  extends: []
  name: Shanghai Jiao Tong University API Rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: shanghai-jiao-tong-university-design-rules
scopes:
- name: Shanghai Jiao Tong University Scopes
  scope_count: 40
  slug: shanghai-jiao-tong-university-scopes
  summary_line: 40 scopes · authorizationCode/clientCredentials/password
score:
  band: developing
  composite: 43.7
  coverage:
    artifact_dirs: 19
    catalog_earned: 79.0
    catalog_earned_first_party: 5.0
    catalog_gap: 36.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.1
  facets:
    access_clarity: 42.1
    contract_governance: 19.7
    contract_quality: 30.1
    developer_ergonomics: 47.6
    discoverability: 79.6
    operational_transparency: 23.7
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - china
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - greater-china
  previous_composite: 43.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 18
      marker_coverage: 100.0
      total: 18
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 64.8
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/shanghai-jiao-tong-university/refs/heads/main/screenshots/shanghai-jiao-tong-university-2026-06-20T193853.png
security:
- kind: authentication
  name: Shanghai Jiao Tong University Authentication
  slug: shanghai-jiao-tong-university-authentication
  summary_line: oauth2/openIdConnect/saml2/totp · 4 schemes
- kind: domain-security
  name: Shanghai Jiao Tong University Domain Security
  slug: shanghai-jiao-tong-university-domain-security
  summary_line: TLSv1.2 · DNSSEC · DMARC
slug: shanghai-jiao-tong-university
tags:
- University
- Higher Education
- Education
- Research
- China
- C9 League
- Identity Federation
- Course Catalog
- Research Computing
- Campus Life
- Authentication
- OpenID Connect
- SAML
- Shibboleth
- Payments
website: https://en.sjtu.edu.cn/
---
