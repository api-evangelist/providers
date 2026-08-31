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
  scored_at: '2026-08-30'
api_count: 2
apis:
- description: 'Open, REST-style API providing developer access to data about the Princeton University Art Museum and its collections. Four surfaces: objects (with a label-level /tombstone sub-resource and filtering '
  name: Princeton University Art Museum API
  slug: art-museum-api
- description: Princeton's Office of Information Technology enterprise API gateway, running WSO2 API Manager. Fronts institutional APIs — ActiveDirectory user and group lookups, PrincetonInfo departmental data, a Mo
  name: Princeton OIT API Gateway
  slug: oit-api-gateway
- description: Princeton's library catalog at catalog.princeton.edu, a Blacklight application the Library writes and maintains itself as pulibrary/orangelight. Every route answers to a .json suffix, so catalog.princ
  name: Princeton University Library Catalog (Orangelight)
  slug: catalog
- description: Princeton University Library's own bibliographic data service at bibdata.princeton.edu. A Rails application (pulibrary/bibdata) that reads from Alma and re-serves bibliographic records, holdings, deli
  name: PUL Bibliographic Data Web Service (Bibdata)
  slug: bibdata
- description: Figgy is Princeton University Library's Valkyrie-based digital repository backend (pulibrary/figgy). It serves IIIF manifests for digitised material and exposes an OAI-PMH 2.0 metadata-harvesting endp
  name: Figgy Digital Repository — OAI-PMH and IIIF
  slug: figgy-oai
- description: Princeton's research data repository, split into pdc_describe for deposit and description and pdc_discovery for the public portal at datacommons.princeton.edu/discovery. Both are Princeton-written (pu
  name: Princeton Data Commons — Discovery
  slug: data-commons
- description: DataSpace is Princeton's older DSpace-based institutional repository for theses, dissertations and archived research output, with an OAI-PMH metadata-harvesting endpoint and content migrating to Princ
  name: DataSpace Institutional Repository — OAI-PMH
  slug: dataspace-oai
- description: Archival finding aids for Princeton's special collections and the Mudd Manuscript Library, served by an ArcLight application the Library maintains as pulibrary/pulfalight. The Blacklight .json surface
  name: Princeton University Library Finding Aids (PULFAlight)
  slug: finding-aids
- description: GeoBlacklight application at maps.princeton.edu (pulibrary/pulmap) serving Princeton's geospatial data catalog. The .json surface is anonymously readable and the records follow the OpenGeoMetadata con
  name: Princeton University Library Maps and Geospatial Data (PUL Map)
  slug: maps
- description: Princeton's public digital collections site at dpul.princeton.edu (pulibrary/dpul), the presentation layer over Figgy. Blacklight .json endpoints return collection and item records anonymously; the sa
  name: Digital PUL (DPUL)
  slug: digital-pul
- description: Princeton's campus identity provider publishes signed SAML 2.0 metadata at idp.princeton.edu/idp/shibboleth. The EntityDescriptor names Princeton University, carries administrative, support and techni
  name: Princeton Shibboleth Identity Provider — SAML 2.0 Metadata
  slug: shibboleth-idp
- description: 'Princeton''s library management and discovery layer runs on Ex Libris, with institution code 01PRI_INST: Alma at na05.alma.exlibrisgroup.com and a Primo VE instance at princeton.primo.exlibrisgroup.com'
  name: Ex Libris Alma / Primo VE — Princeton tenancy (01PRI_INST)
  slug: exlibris-tenancy
- description: Princeton's learning management system is Instructure Canvas at princeton.instructure.com. The host is live behind a Cloudflare interstitial (403 to non-browser clients). Any Canvas REST API, LTI conf
  name: Canvas LMS — Princeton tenancy
  slug: canvas-tenancy
- description: The Article API from Princeton University — 1 operation(s) for article.
  name: Princeton University Article API
  slug: princeton-article-api
- description: The Banner API from Princeton University — 1 operation(s) for banner.
  name: Princeton University Banner API
  slug: princeton-banner-api
- description: The Best Bets API from Princeton University — 1 operation(s) for best bets.
  name: Princeton University Best Bets API
  slug: princeton-best-bets-api
- description: The Catalog API from Princeton University — 1 operation(s) for catalog.
  name: Princeton University Catalog API
  slug: princeton-catalog-api
- description: The Dpul API from Princeton University — 1 operation(s) for dpul.
  name: Princeton University Dpul API
  slug: princeton-dpul-api
- description: The Findingaids API from Princeton University — 1 operation(s) for findingaids.
  name: Princeton University Findingaids API
  slug: princeton-findingaids-api
- description: The Journals API from Princeton University — 1 operation(s) for journals.
  name: Princeton University Journals API
  slug: princeton-journals-api
- description: The Libanswers API from Princeton University — 1 operation(s) for libanswers.
  name: Princeton University Libanswers API
  slug: princeton-libanswers-api
- description: The Libguides API from Princeton University — 1 operation(s) for libguides.
  name: Princeton University Libguides API
  slug: princeton-libguides-api
- description: The Library Databases API from Princeton University — 1 operation(s) for library databases.
  name: Princeton University Library Databases API
  slug: princeton-library-databases-api
- description: The Library Staff API from Princeton University — 1 operation(s) for library staff.
  name: Princeton University Library Staff API
  slug: princeton-library-staff-api
- description: The Library Website API from Princeton University — 1 operation(s) for library website.
  name: Princeton University Library Website API
  slug: princeton-library-website-api
- description: Artists, cultural groups and other makers.
  name: Princeton University Makers API
  slug: princeton-makers-api
- description: Art objects in the Museum's collection.
  name: Princeton University Objects API
  slug: princeton-objects-api
- description: Curated groupings of collection material.
  name: Princeton University Packages API
  slug: princeton-packages-api
- description: The Pulmap API from Princeton University — 1 operation(s) for pulmap.
  name: Princeton University Pulmap API
  slug: princeton-pulmap-api
- description: Full-text search across all collection data types.
  name: Princeton University Search API
  slug: princeton-search-api
artifact_total: 46
common:
- group: company
  title: ''
  type: Website
  url: https://www.princeton.edu/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pulibrary
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/PrincetonUniversity
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Princeton-University-Art-Museum
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/princeton-university/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.princeton.edu/privacy-notice
- group: docs
  title: ''
  type: APIReference
  url: https://allsearch-api.princeton.edu/api-docs
- group: build
  title: ''
  type: LibraryCatalog
  url: https://catalog.princeton.edu/
- group: other
  title: ''
  type: ResearchRepository
  url: https://datacommons.princeton.edu/discovery
- group: other
  title: ''
  type: IdentityFederation
  url: https://idp.princeton.edu/idp/shibboleth
- group: other
  title: ''
  type: OpenData
  url: https://maps.princeton.edu/
- group: design
  title: ''
  type: Conformance
  url: conformance/princeton-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/princeton-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/princeton-errors.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/princeton-vocabulary.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/princeton-openapi-spectral-rules.yml
- group: auth
  title: ''
  type: Scopes
  url: scopes/princeton-scopes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/princeton-lifecycle.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/princeton-context.jsonld
- group: auth
  title: ''
  type: DomainSecurity
  url: security/princeton-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/princeton-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/princeton-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/princeton-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Princeton University is a private Ivy League research university in Princeton, New Jersey. Its programmable footprint is real but almost entirely the work of one unit — Princeton University Library — and it is one of the few institutions in this cohort that operates its own machine-readable contract rather than a vendor''s. The Library publishes an OpenAPI 3.1.1 document for its Allsearch API at allsearch-api.princeton.edu, serves a Swagger UI alongside it, open-sources the application behind it, and runs a family of unauthenticated Blacklight JSON endpoints across the catalog, digital collections, finding aids, maps and the Princeton Data Commons research-data portal. The Art Museum runs a separate open, no-authentication collections API documented in prose on GitHub. Princeton also operates its own Shibboleth identity provider with published SAML 2.0 metadata, an OAI-PMH 2.0 endpoint on Figgy, and DataCite DOI registration under three of its own repository clients. Everything
  outside the Library is gated: the OIT enterprise gateway at api.princeton.edu runs WSO2 API Manager behind NetID or service-account OAuth2, and the developer portal that used to front it, api-store.princeton.edu, no longer resolves at all. Course, registrar, dining and directory data exist as APIs but are not reachable by anyone without a Princeton credential, so no public course-catalog surface is claimed here. Princeton''s teaching and library-discovery layers are vendor tenancies — Canvas and Ex Libris Alma/Primo — and are recorded as relationships, not as Princeton contracts.'
examples:
- key_count: 5
  name: Princeton Allsearch Banner 200
  slug: princeton-allsearch-banner-200
- key_count: 3
  name: Princeton Allsearch Catalog Search 200
  slug: princeton-allsearch-catalog-search-200
- key_count: 1
  name: Princeton Allsearch Empty Query 400
  slug: princeton-allsearch-empty-query-400
- key_count: 19
  name: Princeton Art Museum Maker 200
  slug: princeton-art-museum-maker-200
- key_count: 11
  name: Princeton Art Museum Tombstone 200
  slug: princeton-art-museum-tombstone-200
finops:
- name: Princeton Finops
  service_category: Education
  slug: princeton-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/princeton.png
json_schemas:
- name: Princeton Allsearch error envelope
  property_count: 1
  slug: princeton-allsearch-error
- name: Princeton Allsearch search response
  property_count: 3
  slug: princeton-allsearch-search-response
- name: Princeton University Art Museum art object
  property_count: 28
  slug: princeton-art-museum-object
jsonld:
- class_count: 25
  name: Princeton Context
  property_count: 0
  slug: princeton-context
layout: provider
modified: '2026-08-19'
name: Princeton University
nav: Providers
network: true
overview: 'Princeton University publishes 18 APIs on the [APIs.io](https://apis.io/) network, including Art Museum API, Article API, Banner API, and 15 more. Tagged areas include University, Higher Education, Education, Ivy League, and United States.


  The Princeton University catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Princeton University''s developer surface includes API reference, authentication, and 22 more developer resources.'
plans:
- name: Princeton Plans Pricing
  plan_count: 2
  slug: princeton-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 1
  name: Princeton Rate Limits
  slug: princeton-rate-limits
rules:
- effective_rule_count: 9
  extends: []
  name: Princeton University API Rules
  rule_count: 9
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 7
  slug: princeton-openapi-spectral-rules
scopes:
- name: Princeton Scopes
  scope_count: 0
  slug: princeton-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 41.0
  coverage:
    artifact_dirs: 17
    catalog_gap: 50.3
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 29.5
    contract_quality: 47.5
    developer_ergonomics: 28.6
    discoverability: 44.4
    governance: 29.5
    operational_transparency: 23.7
  previous_composite: 41.6
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 50.0
      total: 2
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 57.4
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/princeton/refs/heads/main/screenshots/princeton-2026-06-20T192107.png
security:
- kind: authentication
  name: Princeton Authentication
  slug: princeton-authentication
  summary_line: none/oauth2/saml · 4 schemes
- kind: domain-security
  name: Princeton Domain Security
  slug: princeton-domain-security
  summary_line: TLSv1.3 · DMARC
slug: princeton
tags:
- University
- Higher Education
- Education
- Ivy League
- United States
- New Jersey
- Research Library
- Research Data
- Open Data
- Digital Collections
- Identity Federation
- Museum
website: https://www.princeton.edu/
---
