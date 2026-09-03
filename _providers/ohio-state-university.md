---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.5
  scored_at: '2026-09-02'
api_count: 1
apis:
- baseURL: https://content.osu.edu/v2
  baseurl_source: declared
  description: 'Public, unauthenticated, read-only JSON API operated by Ohio State''s Office of Technology and Digital Innovation. Serves academic term lists, full-text class search against Student Information System '
  name: Ohio State Mobile Content API v2
  slug: mobile-content-api
- description: CKAN 2.10.10 open data portal operated by Ohio State's Center for Human Resource Research. The full CKAN Action API is public for read (status_show, package_list, package_show, datastore search) and c
  name: CHRR Open Data Portal (CKAN)
  slug: chrr-ckan
- description: Institution-wide web authentication and authorization operated by the Office of Technology and Digital Innovation on Shibboleth, supporting SAML 2.0 with Redirect and POST SSO/SLO bindings and SOAP EC
  name: Web Single Sign-On (Shibboleth Identity Provider)
  slug: websso
- description: Ohio State's SAML 2.0 Identity Provider as published in the InCommon Federation metadata aggregate, retrievable per-entity over the InCommon MDQ service. The signed EntityDescriptor carries Organizati
  name: InCommon Federation IdP Metadata
  slug: incommon-idp-metadata
- description: REST API for the Knowledge Bank, Ohio State University Libraries' DSpace 7.6 institutional repository. Exposes communities, collections, items and bitstreams as HAL JSON. Verified live 2026-09-01 retu
  name: Knowledge Bank DSpace REST API
  slug: kb-rest
- description: 'OAI-PMH 2.0 metadata harvesting endpoint for the Knowledge Bank institutional repository, supporting the standard verbs over Dublin Core and other formats. Verified live 2026-09-01: repositoryName "Th'
  name: Knowledge Bank OAI-PMH Interface
  slug: kb-oai
- description: Library discovery for Ohio State University Libraries, delivered on Ex Libris Primo VE through the OhioLINK consortium (view 01OHIOLINK_OSU). Recorded as a tenancy because the collection and the insti
  name: Library Discovery (Ex Libris Primo VE)
  slug: primo-discovery
- description: Ohio State's Canvas learning management system tenancy, branded Carmen. Canvas exposes an LTI-capable REST API, but that contract is Instructure's and every course-scoped call requires an Ohio State a
  name: Canvas LMS Tenancy
  slug: canvas-lms
- description: 'The Ohio State University is a DataCite direct member, provider symbol GVUZ, active, linked to ROR https://ror.org/00rs6vg23 and created 2025-06-18. It operates one registered repository, gvuz.dcavye '
  name: DataCite Membership (GVUZ)
  slug: datacite-membership
- description: The Ohio State University Libraries is Crossref member 7412 with 4,927 registered DOIs, covering the journals and scholarly series the Libraries publishes. Verified live 2026-09-01 through the Crossre
  name: Crossref Membership (member 7412)
  slug: crossref-membership
- description: The Ohio State University is registered in the Research Organization Registry as https://ror.org/00rs6vg23, the identifier DataCite's provider record for Ohio State points at. Separate ROR records exi
  name: ROR Registration
  slug: ror
artifact_total: 23
common:
- group: company
  title: ''
  type: Website
  url: https://www.osu.edu/
- group: company
  title: ''
  type: Blog
  url: https://news.osu.edu/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/osulibraries
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/the-ohio-state-university/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://it.osu.edu/privacy
- group: learn
  title: ''
  type: CourseCatalog
  url: https://classes.osu.edu/
- group: other
  title: ''
  type: OpenData
  url: https://data.chrr.ohio-state.edu/
- group: other
  title: ''
  type: ResearchRepository
  url: https://kb.osu.edu/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://search.library.osu.edu/
- group: other
  title: ''
  type: IdentityFederation
  url: https://mdq.incommon.org/entities/urn%3Amace%3Aincommon%3Aosu.edu
- group: other
  title: ''
  type: AIPolicy
  url: https://ohiostateresearch.knowledgebase.co/article/artificial-intelligence-40;ai-41;-in-research-guidelines-126.html
- group: build
  title: ''
  type: AITooling
  url: https://ai.osu.edu/resources-buckeyes/approved-ai-tools
- group: auth
  title: ''
  type: Authentication
  url: authentication/ohio-state-university-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ohio-state-university-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ohio-state-university-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/ohio-state-university-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ohio-state-university-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/ohio-state-university-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The Ohio State University is a large public land-grant research university in Columbus, Ohio, United States. It operates no central developer portal and publishes no OpenAPI, no API key programme and no developer documentation for any of its surfaces. What it does operate, verified live on 2026-09-01, is a small set of genuinely institution-run programmable surfaces: an unauthenticated JSON class-search and campus-events API at content.osu.edu/v2 that identifies itself as "OSU Mobile API v2" and backs the public class search at classes.osu.edu; a CKAN 2.10.10 open data portal at data.chrr.ohio-state.edu run by the Center for Human Resource Research, which mints its own DataCite DOIs under prefix 10.82271; and an institution-wide Shibboleth SAML 2.0 Identity Provider published in the InCommon Federation under entityID urn:mace:incommon:osu.edu with REFEDS Research and Scholarship and SIRTFI assurance. Everything else that looks like an Ohio State API is a vendor platform running
  under an Ohio State name: the Knowledge Bank repository is DSpace hosted by Atmire, library discovery is Ex Libris Primo, and the LMS is Instructure Canvas. Those tenancies are recorded here as relationships, not as Ohio State contracts.'
examples:
- key_count: 3
  name: Ohio State University Campus Events Example
  slug: ohio-state-university-campus-events-example
- key_count: 3
  name: Ohio State University Chrr Ckan Package List Example
  slug: ohio-state-university-chrr-ckan-package-list-example
- key_count: 3
  name: Ohio State University Chrr Ckan Status Example
  slug: ohio-state-university-chrr-ckan-status-example
- key_count: 3
  name: Ohio State University Classes Search Example
  slug: ohio-state-university-classes-search-example
- key_count: 3
  name: Ohio State University Classes Searchable Terms Example
  slug: ohio-state-university-classes-searchable-terms-example
- key_count: 3
  name: Ohio State University Datacite Provider Example
  slug: ohio-state-university-datacite-provider-example
finops:
- name: Ohio State University Finops
  service_category: Education
  slug: ohio-state-university-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ohio-state-university.png
jsonld:
- class_count: 16
  name: Ohio State University Context
  property_count: 8
  slug: ohio-state-university-context
layout: provider
modified: '2026-09-01'
name: Ohio State University
nav: Providers
network: true
overview: 'Ohio State University publishes 1 API on the [APIs.io](https://apis.io/) network: Ohio State Mobile Content API v2. Tagged areas include University, Higher Education, Education, United States, and Public Research University.


  The Ohio State University catalog on APIs.io includes 1 JSON-LD context.


  Ohio State University''s developer surface includes engineering blog, authentication, and 17 more developer resources.'
plans:
- name: Ohio State University Plans Pricing
  plan_count: 2
  slug: ohio-state-university-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 1
  name: Ohio State University Rate Limits
  slug: ohio-state-university-rate-limits
score:
  band: thin
  composite: 26.8
  coverage:
    artifact_dirs: 11
    catalog_gap: 56.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 22.1
    developer_ergonomics: 11.9
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 26.8
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
    score: 38.9
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ohio-state-university/refs/heads/main/screenshots/ohio-state-university-2026-06-20T190643.png
security:
- kind: authentication
  name: Ohio State University Authentication
  slug: ohio-state-university-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Ohio State University Domain Security
  slug: ohio-state-university-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ohio-state-university
tags:
- University
- Higher Education
- Education
- United States
- Public Research University
- Course Catalog
- Open Data
- Research Data
- Institutional Repository
- Library
- Identity Federation
- Open Access
website: https://www.osu.edu/
---
