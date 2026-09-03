---
access_model:
  confidence: high
  label: Free
  onboarding: unknown
  pricing: free
  public: true
  source:
  - probed
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
    error_semantics: documented
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
  score: 25.9
  scored_at: '2026-09-02'
api_count: 3
apis:
- description: The University of Tokyo operates three SAML 2.0 entities registered in GakuNin, Japan's academic access federation — two Shibboleth Identity Providers (the central UTokyo IdP at gidp.adm.u-tokyo.ac.jp
  name: UTokyo Identity Federation (GakuNin SAML 2.0)
  slug: gakunin-identity-federation
- baseURL: https://da.dl.itc.u-tokyo.ac.jp/portal
  baseurl_source: declared
  description: IIIF Presentation and Image API endpoints.
  name: University of Tokyo Iiif API
  slug: university-of-tokyo-iiif-api
- baseURL: https://da.dl.itc.u-tokyo.ac.jp/portal
  baseurl_source: declared
  description: Item representations in JSON-LD, CSV and refer/BibIX.
  name: University of Tokyo Items API
  slug: university-of-tokyo-items-api
- baseURL: https://da.dl.itc.u-tokyo.ac.jp/portal
  baseurl_source: declared
  description: Open Archives Initiative Protocol for Metadata Harvesting, version 2.0.
  name: University of Tokyo Oai Pmh API
  slug: university-of-tokyo-oai-pmh-api
- baseURL: https://da.dl.itc.u-tokyo.ac.jp/portal
  baseurl_source: declared
  description: Deposited items — theses, journal articles, departmental bulletins, research data.
  name: University of Tokyo Records API
  slug: university-of-tokyo-records-api
- baseURL: https://da.dl.itc.u-tokyo.ac.jp/portal
  baseurl_source: declared
  description: OpenSearch-described search over the portal.
  name: University of Tokyo Search API
  slug: university-of-tokyo-search-api
artifact_total: 21
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/utda/mirador/issues
- group: company
  title: ''
  type: Website
  url: https://www.u-tokyo.ac.jp/en/
- group: docs
  title: ''
  type: Documentation
  url: https://da.dl.itc.u-tokyo.ac.jp/portal/en/help/api
- group: docs
  title: ''
  type: APIReference
  url: https://da.dl.itc.u-tokyo.ac.jp/portal/help/api
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.u-tokyo.ac.jp/en/general/site_policy.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.u-tokyo.ac.jp/en/general/privacy_policy.html
- group: operate
  title: ''
  type: Support
  url: https://www.u-tokyo.ac.jp/en/general/contact.html
- group: company
  title: ''
  type: Blog
  url: https://www.u-tokyo.ac.jp/focus/en/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/utda
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/utda/dataset
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/university-of-tokyo/
- group: commercial
  title: ''
  type: License
  url: https://www.lib.u-tokyo.ac.jp/ja/library/general/reuse
- group: other
  title: ''
  type: ResearchRepository
  url: https://repository.dl.itc.u-tokyo.ac.jp/
- group: other
  title: ''
  type: OpenData
  url: https://da.dl.itc.u-tokyo.ac.jp/portal/en/database/list
- group: build
  title: ''
  type: LibraryCatalog
  url: https://opac.dl.itc.u-tokyo.ac.jp/
- group: learn
  title: ''
  type: CourseCatalog
  url: https://catalog.he.u-tokyo.ac.jp/
- group: other
  title: ''
  type: IdentityFederation
  url: https://metadata.gakunin.nii.ac.jp/gakunin-metadata.xml
- group: other
  title: ''
  type: ResearchComputing
  url: https://www.cc.u-tokyo.ac.jp/en/supercomputer/
- group: other
  title: ''
  type: AIPolicy
  url: https://utelecon.adm.u-tokyo.ac.jp/en/docs/ai-tools-in-classes/
- group: build
  title: ''
  type: AITooling
  url: https://utelecon.adm.u-tokyo.ac.jp/notice/2024/0327-ai-service/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/university-of-tokyo-oai-pmh-openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/university-of-tokyo-repository-record.schema.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/university-of-tokyo-context.jsonld
- group: build
  title: ''
  type: Examples
  url: examples/university-of-tokyo-repository-records-list.json
- group: auth
  title: ''
  type: Authentication
  url: authentication/university-of-tokyo-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/university-of-tokyo-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/university-of-tokyo-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/university-of-tokyo-error-handling.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/university-of-tokyo-lifecycle.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/university-of-tokyo-vocabulary.yml
- group: design
  title: ''
  type: Rules
  url: rules/university-of-tokyo-harvest-rules.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-tokyo-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-tokyo-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-tokyo-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-tokyo-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The University of Tokyo (東京大学, UTokyo) is Japan''s oldest and largest national research university, founded in 1877, and ranks 28th in the QS World University Rankings. Like almost every institution in this cohort it operates no developer program: there is no API key, no OAuth server, no course or student-information API, no status page, and no OpenAPI, AsyncAPI or GraphQL schema on any host it owns. What it does operate — entirely on its own domain, with no vendor tenancy anywhere in the picture — is library and digital-humanities infrastructure, and that infrastructure is real and standards-conformant rather than nominal. Two OAI-PMH 2.0 endpoints answer live: the UTokyo Repository (self-hosted WEKO3, 69,549 records, seven metadata formats including JPCOAR 2.0 and DDI Codebook) and the Academic Assets Archives Portal (1,957 sets, thirteen years of persistent-deletion metadata). The Archives Portal also serves IIIF Presentation 2.1 manifests, a IIIF Image API 2.0 level2 service
  on iiif.dl.itc.u-tokyo.ac.jp, and DC-NDL item metadata as JSON-LD, CSV and refer/BibIX. The repository additionally exposes an undocumented but fully live JSON records interface. Beyond the library, the university operates three Shibboleth SAML 2.0 entities registered in GakuNin, Japan''s academic access federation — the identity layer is the largest piece of machine-readable engineering the institution actually owns, and it is the piece that never appears in an API catalog. Two honest caveats define this profile: the only API documentation the university publishes exists in Japanese only, so an English-language survey finds nothing here at all; and the documented search API returns HTTP 403 to every external automated client, so it is blocked rather than absent.'
examples:
- key_count: 20
  name: University Of Tokyo Archives Item Jsonld
  slug: university-of-tokyo-archives-item-jsonld
- key_count: 8
  name: University Of Tokyo Iiif Image Info
  slug: university-of-tokyo-iiif-image-info
- key_count: 14
  name: University Of Tokyo Iiif Presentation Manifest
  slug: university-of-tokyo-iiif-presentation-manifest
- key_count: 5
  name: University Of Tokyo Repository Record
  slug: university-of-tokyo-repository-record
- key_count: 3
  name: University Of Tokyo Repository Records List
  slug: university-of-tokyo-repository-records-list
finops:
- name: University Of Tokyo Finops
  service_category: Education
  slug: university-of-tokyo-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-tokyo.png
json_schemas:
- name: UTokyo Repository Record
  property_count: 5
  slug: university-of-tokyo-repository-record.schema
- name: UTokyo Repository Records List
  property_count: 3
  slug: university-of-tokyo-repository-records-list.schema
jsonld:
- class_count: 27
  name: University Of Tokyo Context
  property_count: 1
  slug: university-of-tokyo-context
layout: provider
modified: '2026-08-19'
name: University of Tokyo
nav: Providers
network: true
overview: 'University of Tokyo publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Iiif API, Items API, Oai Pmh API, and 2 more. Tagged areas include University, Higher Education, Education, Japan, and Public Research University.


  The University of Tokyo catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  University of Tokyo''s developer surface includes documentation, API reference, support, engineering blog, code examples, authentication, and 30 more developer resources.'
plans:
- name: University Of Tokyo Plans Pricing
  plan_count: 2
  slug: university-of-tokyo-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 4
  name: University Of Tokyo Rate Limits
  slug: university-of-tokyo-rate-limits
rules:
- effective_rule_count: 0
  extends: []
  name: University of Tokyo API Rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: university-of-tokyo-harvest-rules
scopes:
- name: University Of Tokyo Scopes
  scope_count: 0
  slug: university-of-tokyo-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 45.1
  coverage:
    artifact_dirs: 17
    catalog_gap: 36.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 22.0
    contract_quality: 58.9
    developer_ergonomics: 32.1
    discoverability: 74.1
    governance: 22.0
    operational_transparency: 34.2
  open_source:
    applies: true
    score: 0.0
  previous_composite: 45.1
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 5
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 61.1
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-tokyo/refs/heads/main/screenshots/university-of-tokyo-2026-06-20T200308.png
security:
- kind: authentication
  name: University Of Tokyo Authentication
  slug: university-of-tokyo-authentication
  summary_line: none/saml2 · 2 schemes
- kind: domain-security
  name: University Of Tokyo Domain Security
  slug: university-of-tokyo-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: university-of-tokyo
tags:
- University
- Higher Education
- Education
- Japan
- Public Research University
- Research Data
- Research Repository
- Library
- Digital Archives
- Identity Federation
- IIIF
- OAI-PMH
- Open Access
- Metadata
website: https://www.u-tokyo.ac.jp/en/
---
