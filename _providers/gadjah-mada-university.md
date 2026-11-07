---
access_model:
  confidence: high
  label: Free · Credentials issued internally, read-only surfaces open
  onboarding: unknown
  pricing: free
  public: false
  source:
  - authentication
  - probe
  trial: false
  try_now: true
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
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.3
  scored_at: '2026-11-06'
api_count: 3
apis:
- description: 'UGM''s own Shibboleth Identity Provider, entityID https://sso.ugm.ac.id/idp/shibboleth, publishing an unsigned SAML EntityDescriptor from the university''s own host — retrieved live on 2026-09-01 (200, '
  name: UGM Shibboleth SAML 2.0 Identity Provider
  slug: shibboleth-idp
- description: Central Authentication Service at sso.ugm.ac.id/cas, the login surface UGM systems redirect users to. A bare GET redirects to /cas/login and returns the login form (200, verified 2026-09-01). CAS defi
  name: UGM Single Sign-On (CAS)
  slug: sso-cas
- description: 'UGM''s self-hosted Moodle learning platform, eLOK, at elok.ugm.ac.id, with Moodle Web Services enabled and token-gated. Verified live on 2026-09-01: /webservice/rest/server.php returns the Moodle excep'
  name: eLOK Moodle Web Services (institution deployment)
  slug: elok-moodle-webservices
- description: Universitas Gadjah Mada is a Crossref member in its own name — member id 9411, DOI prefix 10.22146 — verified live on 2026-09-01 against the Crossref REST API. Every DOI minted by UGM's journals begin
  name: Crossref membership (member 9411, prefix 10.22146)
  slug: crossref-membership
- description: 'Universitas Gadjah Mada''s Research Organization Registry identifier, https://ror.org/03ke6d638, verified live on 2026-09-01 against the ROR v2 API. The persistent, machine-readable identifier for the '
  name: ROR organization record (ror.org/03ke6d638)
  slug: ror-record
- baseURL: https://oauth.simaster.ugm.ac.id
  baseurl_source: declared
  description: RFC 8414 & OIDC Discovery
  name: Gadjah Mada University Discovery API
  slug: gadjah-mada-university-discovery-api
- baseURL: https://oauth.simaster.ugm.ac.id
  baseurl_source: declared
  description: Health check & infrastruktur
  name: Gadjah Mada University Infra API
  slug: gadjah-mada-university-infra-api
- baseURL: https://oauth.simaster.ugm.ac.id
  baseurl_source: declared
  description: Open Archives Initiative Protocol for Metadata Harvesting, version 2.0.
  name: Gadjah Mada University OAI PMH API
  slug: gadjah-mada-university-oai-pmh-api
- baseURL: https://oauth.simaster.ugm.ac.id
  baseurl_source: declared
  description: Social provider login (Google, Microsoft, Facebook, LinkedIn)
  name: Gadjah Mada University Social Login API
  slug: gadjah-mada-university-social-login-api
- baseURL: https://sso.ugm.ac.id/idp/profile/Metadata/SAML
  baseurl_source: declared
  description: Endpoint inti OAuth2/OIDC
  name: Gadjah Mada University O Auth2 API
  slug: gadjah-mada-university-oauth2-api
- baseURL: https://sso.ugm.ac.id/idp/profile/Metadata/SAML
  baseurl_source: declared
  description: The Me API from Gadjah Mada University — 1 operation(s) for me.
  name: Gadjah Mada University Me API
  slug: gadjah-mada-university-me-api
- baseURL: https://sso.ugm.ac.id/idp/profile/Metadata/SAML
  baseurl_source: declared
  description: The User API from Gadjah Mada University — 2 operation(s) for user.
  name: Gadjah Mada University User API
  slug: gadjah-mada-university-user-api
artifact_total: 21
common:
- group: other
  href: https://artifacts.apis.io/gadjah-mada-university/capabilities/gadjah-mada-university-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/gadjah-mada-university-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://ugm.ac.id/en/
- group: docs
  title: ''
  type: APIReference
  url: https://oauth.simaster.ugm.ac.id/docs
- group: docs
  title: ''
  type: Documentation
  url: https://oauth.simaster.ugm.ac.id/openapi.json
- group: operate
  title: ''
  type: Status
  url: https://oauth.simaster.ugm.ac.id/health
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ugm.ac.id/en/privacy-policy/
- group: company
  title: ''
  type: Blog
  url: https://ugm.ac.id/en/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://ugm.ac.id/en/feed/
- group: operate
  title: ''
  type: Support
  url: https://dti.ugm.ac.id/knowledge-base/
- group: other
  title: ''
  type: IdentityFederation
  url: https://sso.ugm.ac.id/idp/profile/Metadata/SAML
- group: other
  title: ''
  type: ResearchRepository
  url: http://repository.ugm.ac.id/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://opac.lib.ugm.ac.id/
- group: other
  title: ''
  type: ScholarlyPublishing
  url: https://journal.ugm.ac.id/
- group: learn
  title: ''
  type: CourseCatalog
  url: https://akademik.ugm.ac.id/
- group: other
  title: ''
  type: AIPolicy
  url: https://web.ugm.ac.id/etika-penggunaan-ai/
- group: build
  title: ''
  type: AITooling
  url: https://lib.ugm.ac.id/file/panduan-penggunaan-genai/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/ugm-ac-id
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/universitas-gadjah-mada/
- group: auth
  href: https://artifacts.apis.io/gadjah-mada-university/authentication/gadjah-mada-university-authentication.yml
  title: ''
  type: Authentication
  url: authentication/gadjah-mada-university-authentication.yml
- group: auth
  href: https://artifacts.apis.io/gadjah-mada-university/scopes/gadjah-mada-university-scopes.yml
  title: ''
  type: Scopes
  url: scopes/gadjah-mada-university-scopes.yml
- group: design
  href: https://artifacts.apis.io/gadjah-mada-university/conformance/gadjah-mada-university-conformance.yml
  title: ''
  type: Conformance
  url: conformance/gadjah-mada-university-conformance.yml
- group: design
  href: https://artifacts.apis.io/gadjah-mada-university/errors/gadjah-mada-university-errors.yml
  title: ''
  type: Errors
  url: errors/gadjah-mada-university-errors.yml
- group: design
  href: https://artifacts.apis.io/gadjah-mada-university/lifecycle/gadjah-mada-university-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/gadjah-mada-university-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/gadjah-mada-university/rules/gadjah-mada-university-rules.yml
  title: ''
  type: Rules
  url: rules/gadjah-mada-university-rules.yml
- group: design
  href: https://artifacts.apis.io/gadjah-mada-university/vocabulary/gadjah-mada-university-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/gadjah-mada-university-vocabulary.yml
- group: build
  href: https://artifacts.apis.io/gadjah-mada-university/examples/gadjah-mada-university-ugm-id-examples.yml
  title: ''
  type: Examples
  url: examples/gadjah-mada-university-ugm-id-examples.yml
- group: docs
  href: https://artifacts.apis.io/gadjah-mada-university/json-schema/gadjah-mada-university-ugm-id-schemas.json
  title: ''
  type: JSONSchema
  url: json-schema/gadjah-mada-university-ugm-id-schemas.json
- group: auth
  href: https://artifacts.apis.io/gadjah-mada-university/security/gadjah-mada-university-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/gadjah-mada-university-domain-security.yml
- group: commercial
  href: https://artifacts.apis.io/gadjah-mada-university/plans/gadjah-mada-university-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/gadjah-mada-university-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/gadjah-mada-university/rate-limits/gadjah-mada-university-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/gadjah-mada-university-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/gadjah-mada-university/finops/gadjah-mada-university-finops.yml
  title: ''
  type: FinOps
  url: finops/gadjah-mada-university-finops.yml
- group: other
  href: https://artifacts.apis.io/gadjah-mada-university/review.yml
  title: ''
  type: Review
  url: review.yml
- group: design
  href: https://artifacts.apis.io/gadjah-mada-university/json-ld/gadjah-mada-university-context.jsonld
  title: ''
  type: x-json-ld
  url: json-ld/gadjah-mada-university-context.jsonld
- group: company
  href: https://artifacts.apis.io/gadjah-mada-university/blogs/blogs.json
  title: ''
  type: x-blogs
  url: blogs/blogs.json
created: '2026-06-03'
description: 'Gadjah Mada University (Universitas Gadjah Mada, UGM) is a public research university in Yogyakarta, Indonesia, founded in 1949 and the country''s oldest and largest state university. Unusually for this cohort, UGM''s programmable footprint is real and it is its own: the university operates and publishes a first-party OpenAPI 3.1.0 contract for UGM ID, its OAuth 2.0 / OpenID Connect authorization server at oauth.simaster.ugm.ac.id, complete with an OIDC Discovery document, an RFC 8414 authorization-server metadata document, PKCE, RFC 7662 introspection, RFC 7009 revocation, RFC 8693 token exchange, a Swagger UI and a public health endpoint. Alongside it UGM runs its own Shibboleth SAML 2.0 Identity Provider, a CAS server, and two independent, fully functional OAI-PMH 2.0 endpoints — the EPrints institutional repository at repository.ugm.ac.id and the university-wide Open Journal Systems platform at journal.ugm.ac.id, whose articles carry DOIs under UGM''s own Crossref prefix
  10.22146 (member 9411). None of that is a vendor''s contract running under UGM''s name; every host is under ugm.ac.id and every specification describes itself as UGM''s. What UGM does not have is a developer programme. There is no developer portal, no self-service client registration, no dynamic client registration, no documented route to a client_id, no changelog, no status page, no terms of service and no licence on any surface. There is no open data portal — data.ugm.ac.id returns a maintenance page — no public course, timetable or registrar API, and no research-computing service catalog. The main site''s WordPress REST API is deliberately closed to anonymous callers, and the whole /.well-known/ path is blocked at the edge. The honest summary is a genuine engineering surface with no consumer-facing programme around it, plus three real registry and federation relationships recorded as facts about the institution rather than as contracts it wrote.'
finops:
- has_sources: true
  method: generated
  name: Gadjah Mada University Finops
  primary_unit: ''
  service_category: Education
  slug: gadjah-mada-university-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gadjah-mada-university.png
json_schemas:
- name: UGM ID — JSON Schemas
  property_count: 0
  slug: gadjah-mada-university-ugm-id-schemas
jsonld:
- class_count: 18
  name: Gadjah Mada University Context
  property_count: 4
  slug: gadjah-mada-university-context
layout: provider
modified: '2026-09-01'
name: Gadjah Mada University
nav: Providers
network: true
overview: 'Gadjah Mada University publishes 12 API contracts indexed on the [APIs.io](https://apis.io/) network, including Discovery API, Infra API, OAI PMH API, and 9 more. Tagged areas include University, Higher Education, Education, Indonesia, and Research.


  The Gadjah Mada University catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Gadjah Mada University''s developer surface includes API reference, documentation, status page, engineering blog, support, GitHub presence, authentication, and 27 more developer resources.'
plans:
- name: Gadjah Mada University Plans Pricing
  plan_count: 2
  slug: gadjah-mada-university-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 1
  name: Gadjah Mada University Rate Limits
  slug: gadjah-mada-university-rate-limits
rules:
- authorship: derived
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Gadjah Mada University API Rules
  rule_count: 11
  severity_counts:
    error: 6
    hint: 0
    info: 0
    warn: 5
  slug: gadjah-mada-university-rules
scopes:
- name: Gadjah Mada University Scopes
  scope_count: 5
  slug: gadjah-mada-university-scopes
  summary_line: 5 scopes
score:
  band: thin
  composite: 37.5
  coverage:
    artifact_dirs: 21
    catalog_earned: 62.4
    catalog_earned_first_party: 0.0
    catalog_gap: 52.6
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.1
  facets:
    access_clarity: 15.8
    contract_governance: 15.2
    contract_quality: 63.0
    developer_ergonomics: 35.7
    discoverability: 71.4
    operational_transparency: 10.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - indonesia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - southeast-asia
  previous_composite: 36.4
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 85.7
      total: 7
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/gadjah-mada-university/gadjah-mada-university-2026-06-20T181636.png
security:
- kind: authentication
  name: Gadjah Mada University Authentication
  slug: gadjah-mada-university-authentication
  summary_line: oauth2/oidc/saml2/cas · 3 schemes
- kind: domain-security
  name: Gadjah Mada University Domain Security
  slug: gadjah-mada-university-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: gadjah-mada-university
tags:
- University
- Higher Education
- Education
- Indonesia
- Research
- Identity Federation
- Authentication
- OAuth
- Research Repository
- Scholarly Publishing
- OAI-PMH
- Library
website: https://ugm.ac.id/en/
---
