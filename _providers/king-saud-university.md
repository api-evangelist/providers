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
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.4
  scored_at: '2026-09-01'
api_count: 2
apis:
- description: The King Saud University Data Management Office (مكتب إدارة البيانات) publishes institutional open data as stable, unauthenticated HTTP resources on the university's own domain. Seven dataset families
  name: KSU Open Data Distribution API
  slug: open-data
- description: 'King Saud University operates its own authorization server and identity provider, and publishes both discovery documents anonymously: OpenID Connect Discovery 1.0 at /.well-known/openid-configuration '
  name: KSU Identity and Access Management (OAuth 2.0 / OpenID Connect / SAML 2.0)
  slug: identity
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
artifact_total: 14
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
  title: ''
  type: DomainSecurity
  url: security/king-saud-university-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/king-saud-university-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/king-saud-university-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/king-saud-university-finops.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/king-saud-university-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/king-saud-university-lifecycle.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'King Saud University (جامعة الملك سعود, KSU) is Saudi Arabia''s oldest public research university, founded in Riyadh in 1957. Contrary to the 2026-06-03 review of this profile, KSU does operate public, machine-readable surfaces on its own domain — they are documented only in Arabic, which is why an English-language review missed them. Its Data Management Office publishes an institutional open-data programme at data.ksu.edu.sa: 852 dataset distribution files across seven dataset families in JSON, XML, RDF/XML, CSV and XLSX, unauthenticated, under a KSU-authored open-data licence, on a declared annual cadence, with an Arabic API guide and a 13-page reference PDF. Separately, the university runs its own identity plane at iam.ksu.edu.sa, which serves a public OpenID Connect discovery document and RFC 8414 authorization-server metadata, and whose SAML 2.0 identity provider is registered in eduGAIN through the Saudi Maeen Identity Federation. What KSU does NOT publish is a developer
  programme: there is no developer portal, no API reference in English, no OpenAPI, no apis.json, no llms.txt, no status page and no self-service client registration — the advertised OAuth registration endpoint answers 404. The filtered open-data query API the university still documents has been withdrawn from its own router. Everything else students and staff touch — Edugate, MyKSU, the Blackboard LMS, the library catalogue — is either a gated end-user application or a vendor platform running under a KSU hostname.'
finops:
- name: King Saud University Finops
  service_category: Education
  slug: king-saud-university-finops
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
overview: 'King Saud University publishes 2 APIs on the [APIs.io](https://apis.io/) network: KSU Open Data Distribution API and KSU Identity and Access Management (OAuth 2.0 / OpenID Connect / SAML 2.0). Tagged areas include Education, Higher Education, University, Public Research University, and Saudi Arabia.


  The King Saud University catalog on APIs.io includes 1 JSON-LD context.


  King Saud University''s developer surface includes API reference, documentation, authentication, engineering blog, support, and 17 more developer resources.'
plans:
- name: King Saud University Plans Pricing
  plan_count: 2
  slug: king-saud-university-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 2
  name: King Saud University Rate Limits
  slug: king-saud-university-rate-limits
scopes:
- name: King Saud University Scopes
  scope_count: 0
  slug: king-saud-university-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 42.5
  coverage:
    artifact_dirs: 14
    catalog_gap: 50.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 20.5
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 26.8
    developer_ergonomics: 35.7
    discoverability: 59.3
    governance: 18.2
    operational_transparency: 21.1
  previous_composite: 22.0
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
    score: 79.6
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/king-saud-university/refs/heads/main/screenshots/king-saud-university-2026-06-20T184048.png
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
- Single Sign-On
- Research
- Linked Data
website: https://ksu.edu.sa/en
---
