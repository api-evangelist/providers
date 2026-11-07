---
access_model:
  confidence: high
  label: Free · open data needs no account; identity plane is not self-service
  onboarding: unknown
  pricing: free
  public: true
  source:
  - probed
  - plans
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
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: documented
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.3
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: King Saud University's SAML 2.0 identity provider is published into the eduGAIN interfederation metadata by the Maeen Identity Federation (https://www.maeen.sa, federation code SA-MIF, an eduGAIN memb
  name: King Saud University identity provider in eduGAIN (via Maeen)
  slug: edugain-idp
- description: King Saud University is Crossref member 19827 and owns DOI prefix 10.33948, under which Crossref reports 1,521 registered DOIs (354 current, 1,167 backfile) as of 2026-09-01. The university's scholarl
  name: Crossref membership and DOI prefix
  slug: crossref
- description: King Saud University is registered in the Research Organization Registry as https://ror.org/02f81g417, the canonical machine-readable identifier for the institution in scholarly infrastructure. Confir
  name: Research Organization Registry identifier
  slug: ror
- description: King Saud University's learning management system is a Blackboard Learn SaaS tenancy fronted by a university hostname. Requesting it returns a SAML AuthnRequest to the university's own identity provid
  name: KSU learning management system (Blackboard Learn SaaS tenancy)
  slug: blackboard-lms
- baseURL: https://data.ksu.edu.sa
  baseurl_source: declared
  description: Stable distributions of King Saud University open datasets.
  name: King Saud University Datasets API
  slug: king-saud-university-datasets-api
- baseURL: https://data.ksu.edu.sa
  baseurl_source: declared
  description: OAuth 2.0 and OpenID Connect endpoints of the King Saud University authorization server.
  name: King Saud University Identity API
  slug: king-saud-university-identity-api
artifact_total: 15
common:
- group: company
  title: ''
  type: Website
  url: https://ksu.edu.sa/en
- group: other
  title: ''
  type: OpenData
  url: https://data.ksu.edu.sa/ar
- group: docs
  title: ''
  type: APIReference
  url: https://data.ksu.edu.sa/ar/api/guide
- group: docs
  title: ''
  type: Documentation
  url: https://data.ksu.edu.sa/ar/node/1163
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ksu.edu.sa/ar/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ksu.edu.sa/ar/privacy
- group: other
  title: ''
  type: IdentityFederation
  url: https://technical.edugain.org/entities?id=671188
- group: auth
  title: ''
  type: Authentication
  url: https://iam.ksu.edu.sa/.well-known/openid-configuration
- group: other
  title: ''
  type: AIPolicy
  url: https://aio.ksu.edu.sa/ar/node/2976
- group: build
  title: ''
  type: AITooling
  url: https://thakaa.ksu.edu.sa/en
- group: build
  title: ''
  type: LibraryCatalog
  url: https://library.ksu.edu.sa/en
- group: company
  title: ''
  type: Blog
  url: https://news.ksu.edu.sa/ar
- group: operate
  title: ''
  type: Support
  url: https://ksu.edu.sa/en/apps
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/king-saud-university/
- group: company
  title: ''
  type: Twitter
  url: https://x.com/_KSU
- group: auth
  href: https://artifacts.apis.io/king-saud-university/security/king-saud-university-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/king-saud-university-domain-security.yml
- group: commercial
  href: https://artifacts.apis.io/king-saud-university/plans/king-saud-university-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/king-saud-university-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/king-saud-university/rate-limits/king-saud-university-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/king-saud-university-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/king-saud-university/finops/king-saud-university-finops.yml
  title: ''
  type: FinOps
  url: finops/king-saud-university-finops.yml
- group: design
  href: https://artifacts.apis.io/king-saud-university/conformance/king-saud-university-conformance.yml
  title: ''
  type: Conformance
  url: conformance/king-saud-university-conformance.yml
- group: design
  href: https://artifacts.apis.io/king-saud-university/lifecycle/king-saud-university-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/king-saud-university-lifecycle.yml
- group: other
  href: https://artifacts.apis.io/king-saud-university/review.yml
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'King Saud University (جامعة الملك سعود, KSU) is Saudi Arabia''s oldest public research university, founded in Riyadh in 1957. Contrary to the 2026-06-03 review of this profile, KSU does operate public, machine-readable surfaces on its own domain — they are documented only in Arabic, which is why an English-language review missed them. Its Data Management Office publishes an institutional open-data programme at data.ksu.edu.sa: 852 dataset distribution files across seven dataset families in JSON, XML, RDF/XML, CSV and XLSX, unauthenticated, under a KSU-authored open-data licence, on a declared annual cadence, with an Arabic API guide and a 13-page reference PDF. Separately, the university runs its own identity plane at iam.ksu.edu.sa, which serves a public OpenID Connect discovery document and RFC 8414 authorization-server metadata, and whose SAML 2.0 identity provider is registered in eduGAIN through the Saudi Maeen Identity Federation. What KSU does NOT publish is a developer
  programme: there is no developer portal, no API reference in English, no OpenAPI, no apis.json, no llms.txt, no status page and no self-service client registration — the advertised OAuth registration endpoint answers 404. The filtered open-data query API the university still documents has been withdrawn from its own router. Everything else students and staff touch — Edugate, MyKSU, the Blackboard LMS, the library catalogue — is either a gated end-user application or a vendor platform running under a KSU hostname.'
finops:
- has_sources: true
  method: generated
  name: King Saud University Finops
  primary_unit: ''
  service_category: Education
  slug: king-saud-university-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/king-saud-university.png
json_schemas:
- name: King Saud University Open Data — dataset record shapes
  property_count: 0
  slug: king-saud-university-open-data-datasets
jsonld:
- class_count: 11
  name: King Saud University Context
  property_count: 2
  slug: king-saud-university-context
layout: provider
modified: '2026-09-01'
name: King Saud University
nav: Providers
network: true
overview: 'King Saud University publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Datasets API, Identity API, and 4 more. Tagged areas include Education, Higher Education, University, Public Research University, and Saudi Arabia.


  The King Saud University catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  King Saud University''s developer surface includes API reference, documentation, authentication, engineering blog, support, and 17 more developer resources.'
plans:
- name: King Saud University Plans Pricing
  plan_count: 2
  slug: king-saud-university-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 2
  name: King Saud University Rate Limits
  slug: king-saud-university-rate-limits
rules:
- authorship: generated
  effective_rule_count: 103
  extends:
  - spectral:oas
  name: King Saud University API Rules
  rule_count: 62
  severity_counts:
    error: 56
    hint: 0
    info: 3
    warn: 3
  slug: king-saud-university-rules
scopes:
- name: King Saud University Scopes
  scope_count: 6
  slug: king-saud-university-scopes
  summary_line: 6 scopes
score:
  band: thin
  composite: 36.6
  coverage:
    artifact_dirs: 20
    catalog_earned: 62.0
    catalog_earned_first_party: 16.0
    catalog_gap: 53.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 42.1
    contract_governance: 31.8
    contract_quality: 23.8
    developer_ergonomics: 35.7
    discoverability: 57.1
    operational_transparency: 21.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - saudi-arabia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - mena
    - middle-east
  previous_composite: 36.6
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 2
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 42.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/king-saud-university/king-saud-university-2026-06-20T184048.png
security:
- kind: authentication
  name: King Saud University Authentication
  slug: king-saud-university-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: King Saud University Domain Security
  slug: king-saud-university-domain-security
  summary_line: TLSv1.2 · DMARC
slug: king-saud-university
tags:
- Education
- Higher Education
- University
- Public Research University
- Saudi Arabia
- Middle East
- Riyadh
- Open Data
- Research Data
- Identity Federation
- SSO
- Research
- Linked Data
website: https://ksu.edu.sa/en
---
