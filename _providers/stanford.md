---
access_model:
  confidence: high
  label: Mixed — open library data, gated administrative and AI surfaces
  onboarding: unknown
  pricing: free
  public: true
  source:
  - plans
  - authentication/stanford-authentication.yml
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.3
  scored_at: '2026-09-01'
api_count: 5
apis:
- description: Persistent URLs into the Stanford Digital Repository. GET /{druid} returns HTML, /{druid}.xml returns the cocina publicObject document, /{druid}.mods returns MODS 3.7. Open, no credential. Verified li
  name: Stanford Libraries PURL API
  slug: library-purl
- description: IIIF Presentation (v2.1 stable, v3 alpha) and Image v2 APIs over the Stanford Digital Repository. Manifests served from purl.stanford.edu, image tiles from stacks.stanford.edu. Open, no credential. Ma
  name: Stanford Libraries IIIF API
  slug: library-iiif
- description: Operating hours for 24 Stanford library locations, answered as a JSON:API document at library-hours.stanford.edu/libraries.json. Open, no credential. Verified live 2026-08-19.
  name: Stanford Libraries Library Hours API
  slug: library-hours
- description: File and image delivery for Stanford Digital Repository content, served from stacks.stanford.edu. Documentation verified live 2026-08-19; access to individual files follows each object's rights statem
  name: Stanford Libraries Digital Stacks API
  slug: library-digital-stacks
- description: oEmbed-style service returning an embeddable viewer for a Stanford Digital Repository object. Documentation verified live 2026-08-19.
  name: Stanford Libraries Embed API
  slug: library-embed
- description: The Registrar's course catalog, queryable as XML by appending view=xml-20140630 to a search. Open, no credential, and the largest genuinely public dataset Stanford serves — a single department query r
  name: ExploreCourses course-data XML query interface
  slug: explorecourses
- description: Signed Shibboleth SAML 2.0 identity-provider metadata, entityID https://idp.stanford.edu/, valid until 2027-08-16. Declares an IDPSSODescriptor, three SSO bindings (HTTP-POST, HTTP-POST-SimpleSign, HT
  name: Stanford Identity Provider — SAML 2.0 metadata
  slug: idp-saml
- description: Direct API access to the large language models hosted in Stanford's own cloud infrastructure behind the AI Playground, for faculty, staff and students building their own AI applications. Keyed per API
  name: Stanford AI API Gateway
  slug: ai-api-gateway
- description: 'University IT''s Registry web services — Account, Person, Student, CourseClass, Privilege and Workgroup — over Stanford''s consolidated system of record. Documented publicly but gated: access requires a'
  name: MaIS Registry APIs
  slug: mais-registry
- description: API over the Community Academic Profiles directory (18,000+ faculty, students, postdocs and staff). The interactive console at cap.stanford.edu/cap-api/console redirects to authentication; credentials
  name: CAP / Stanford Profiles API
  slug: cap-profiles
- description: The About API from Stanford University — 1 operation(s) for about.
  name: Stanford University About API
  slug: stanford-about-api
- description: Authenticate the user
  name: Stanford University Authentication API
  slug: stanford-authentication-api
- description: Add and update Moabs in the catalog
  name: Stanford University Catalog API
  slug: stanford-catalog-api
- description: Operations about events
  name: Stanford University Events API
  slug: stanford-events-api
- description: upload binary files
  name: Stanford University Files API
  slug: stanford-files-api
- description: Identifier operations
  name: Stanford University Identifiers API
  slug: stanford-identifiers-api
- description: Integrations with other Systems
  name: Stanford University Integrations API
  slug: stanford-integrations-api
- description: Operations involving background jobs
  name: Stanford University Jobs API
  slug: stanford-jobs-api
- description: Legacy endpoints
  name: Stanford University Legacy API
  slug: stanford-legacy-api
- description: Digital Repository Objects
  name: Stanford University Metadata API
  slug: stanford-metadata-api
- description: Digital Repository Objects
  name: Stanford University Objects API
  slug: stanford-objects-api
- description: Operations about release tags
  name: Stanford University Release Tags API
  slug: stanford-release-tags-api
- description: Tags
  name: Stanford University Tags API
  slug: stanford-tags-api
- description: Operations about object versions
  name: Stanford University Versions API
  slug: stanford-versions-api
- description: Operations about workflows
  name: Stanford University Workflows API
  slug: stanford-workflows-api
- description: Operations about workspaces
  name: Stanford University Workspaces API
  slug: stanford-workspaces-api
artifact_total: 43
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/SU-SWS/cap-api/blob/master/LICENSE
- group: company
  title: ''
  type: Website
  url: https://www.stanford.edu/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://uit.stanford.edu/developers
- group: docs
  title: ''
  type: APIReference
  url: https://api.library.stanford.edu/
- group: docs
  title: ''
  type: Documentation
  url: https://uit.stanford.edu/developers/apis
- group: learn
  title: ''
  type: CourseCatalog
  url: https://explorecourses.stanford.edu/about
- group: other
  title: ''
  type: ResearchRepository
  url: https://purl.stanford.edu/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://searchworks.stanford.edu/
- group: other
  title: ''
  type: IdentityFederation
  url: https://idp.stanford.edu/metadata.xml
- group: other
  title: ''
  type: ResearchComputing
  url: https://srcc.stanford.edu/
- group: other
  title: ''
  type: AIPolicy
  url: https://uit.stanford.edu/security/responsibleai
- group: build
  title: ''
  type: AITooling
  url: https://uit.stanford.edu/ai
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sul-dlss
- group: build
  title: ''
  type: GitHub
  url: https://github.com/SU-SWS
- group: auth
  title: ''
  type: Authentication
  url: https://login.stanford.edu/
- group: operate
  title: ''
  type: Status
  url: https://library-status.stanford.edu/
- group: operate
  title: ''
  type: Support
  url: https://stanford.service-now.com/it_services?id=get_help
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.stanford.edu/site/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.stanford.edu/site/privacy/
- group: auth
  title: ''
  type: SecurityContact
  url: https://uit.stanford.edu/security/report-incident
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/stanford-university/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/Stanford
- group: auth
  title: ''
  type: TrustCenter
  url: security/stanford-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/stanford-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/stanford-authentication.yml
- group: auth
  title: ''
  type: Scopes
  url: scopes/stanford-scopes.yml
- group: design
  title: ''
  type: Errors
  url: errors/stanford-errors.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/stanford-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/stanford-lifecycle.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/stanford-vocabulary.yml
- group: design
  title: ''
  type: Rules
  url: rules/stanford-rules.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/stanford-context.jsonld
- group: build
  title: ''
  type: Examples
  url: examples/index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/stanford-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/stanford-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/stanford-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Stanford University is a private research university in Stanford, California. Unusually for a higher-education institution, essentially its entire programmable footprint is genuinely institution-operated rather than a vendor tenancy: every surface listed here runs on a stanford.edu host. Stanford Libraries (SUL-DLSS) publishes five first-party OpenAPI contracts for the Stanford Digital Repository — SDR, DOR Services, Technical Metadata, Preservation Catalog and SURI, 76 operations, Apache 2.0, on its own GitHub org — though the services themselves sit on the internal network. Public and open without credentials are PURL (XML/MODS/IIIF Presentation 2.1 off purl.stanford.edu), the Library Hours JSON:API, and the Registrar''s ExploreCourses XML query interface, which reports its own deprecation in every response body. University IT runs the certificate-gated MaIS Registry web services (Account, Person, Student, CourseClass, Privilege, Workgroup) and a metered AI API Gateway keyed
  to a Stanford billing account. Stanford also publishes signed Shibboleth SAML 2.0 identity-provider metadata at idp.stanford.edu — machine-readable identity federation that most universities never get catalogued. What is missing is equally clear: no OAI-PMH provider was found on any Stanford host, no institution-operated open-data portal, no OAuth scopes, no contact or terms in any contract, no examples on any of the 76 operations, and no unified developer portal spanning the Libraries and University IT surfaces.'
examples:
- key_count: 7
  name: Stanford Embed Oembed Example
  slug: stanford-embed-oembed-example
- key_count: 7
  name: Stanford Iiif Manifest Example
  slug: stanford-iiif-manifest-example
- key_count: 7
  name: Stanford Library Hours Example
  slug: stanford-library-hours-example
finops:
- name: Stanford Finops
  service_category: Education
  slug: stanford-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/stanford.png
json_schemas:
- name: DOR Services API — component schemas
  property_count: 0
  slug: stanford-dor-services-api-schemas
- name: Preservation Catalog HTTP API — component schemas
  property_count: 0
  slug: stanford-preservation-catalog-api-schemas
- name: SDR API — component schemas
  property_count: 0
  slug: stanford-sdr-api-schemas
- name: SURI API — component schemas
  property_count: 0
  slug: stanford-suri-api-schemas
- name: Technical Metadata API — component schemas
  property_count: 0
  slug: stanford-technical-metadata-api-schemas
jsonld:
- class_count: 30
  name: Stanford Context
  property_count: 5
  slug: stanford-context
layout: provider
modified: '2026-08-19'
name: Stanford University
nav: Providers
network: true
overview: 'Stanford University publishes 16 APIs on the [APIs.io](https://apis.io/) network, including About API, Authentication API, Catalog API, and 13 more. Tagged areas include University, Higher Education, Education, Research, and United States.


  The Stanford University catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Stanford University''s developer surface includes API reference, documentation, GitHub presence, authentication, status page, support, code examples, and 30 more developer resources.'
plans:
- name: Stanford Plans Pricing
  plan_count: 2
  slug: stanford-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 1
  name: Stanford Rate Limits
  slug: stanford-rate-limits
rules:
- effective_rule_count: 0
  extends: []
  name: Stanford University API Rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: stanford-rules
scopes:
- name: Stanford Scopes
  scope_count: 0
  slug: stanford-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 57.2
  coverage:
    artifact_dirs: 17
    catalog_gap: 44.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.3
  facets:
    access_clarity: 71.1
    commercial_clarity: 71.1
    contract_governance: 3.8
    contract_quality: 67.2
    developer_ergonomics: 48.8
    discoverability: 59.3
    governance: 3.8
    operational_transparency: 23.7
  previous_composite: 56.9
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 16
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 74.1
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/stanford/refs/heads/main/screenshots/stanford-2026-06-20T194502.png
security:
- kind: authentication
  name: Stanford Authentication
  slug: stanford-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Stanford Domain Security
  slug: stanford-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Stanford Trust Center
  slug: stanford-trust-center
  summary_line: HIPAA, GDPR
slug: stanford
tags:
- University
- Higher Education
- Education
- Research
- United States
- California
- Private Research University
- Association of American Universities
- Research Repository
- Course Catalog
- Identity Federation
- Library
- Digital Repository
- Artificial Intelligence
- IIIF
website: https://www.stanford.edu/
---
