---
access_model:
  confidence: high
  label: Free · open, no registration
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
  scored_at: '2026-09-03'
api_count: 3
apis:
- baseURL: https://centaur.reading.ac.uk/cgi/oai2
  baseurl_source: declared
  description: 'OAI-PMH 2.0 metadata harvesting interface for CentAUR, the Central Archive at the University of Reading — the institutional repository of the university''s research outputs. Operated by the university '
  name: CentAUR OAI-PMH Metadata API
  slug: centaur-oai-pmh
- baseURL: https://researchdata.reading.ac.uk/cgi/oai2
  baseurl_source: declared
  description: OAI-PMH 2.0 metadata harvesting interface for the University of Reading Research Data Archive, the institution's multidisciplinary service for registering, preserving and publishing research datasets.
  name: Research Data Archive OAI-PMH Metadata API
  slug: research-data-archive-oai-pmh
- baseURL: https://centaur.reading.ac.uk/rest/
  baseurl_source: declared
  description: The read-only EPrints REST interface on CentAUR. GET /rest/ returns the dataset index (eprint, user, subject) and GET /rest/eprint/ enumerates every record id — 6.5 MB of ids at probe time — each link
  name: CentAUR Repository REST Listings
  slug: centaur-eprints-rest
- baseURL: https://researchdata.reading.ac.uk/rest/
  baseurl_source: declared
  description: The same read-only EPrints REST interface on the Research Data Archive host. GET /rest/, /rest/eprint/ (47 KB of dataset ids) and /rest/subject/ each returned 200 unauthenticated on 2026-09-01; GET /r
  name: Research Data Archive REST Listings
  slug: research-data-archive-eprints-rest
- description: The University of Reading's own SAML identity provider entity, registered in the UK Access Management Federation and published in eduGAIN. entityID https://reading.ac.uk/oala/metadata, OrganizationNam
  name: UK Access Management Federation Identity Provider Entity
  slug: uk-federation-idp
- description: The university's institutional identity plane. Tenant 4ffa3bc4-ecfc-48c0-9080-f5e43ff90e5f, whose OpenID Connect discovery document is public and complete at login.microsoftonline.com/reading.ac.uk/v2
  name: Microsoft Entra ID Tenant OpenID Connect Discovery
  slug: entra-id-tenant
- description: The University of Reading is a DataCite member — a fact about the institution, not a contract it operates. api.datacite.org/providers/pclw returns provider "University of Reading", symbol PCLW, organi
  name: DataCite Membership and DOI Prefixes
  slug: datacite-membership
- description: The university's entry in the Research Organization Registry, https://ror.org/05v62cm79 — machine-readable identity for the institution itself. The record carries domain reading.ac.uk, established 192
  name: ROR Organization Registration
  slug: ror-registration
- description: The university's public module (course) catalogue, an ASP.NET application the university runs itself at www.reading.ac.uk/modules. Browsable without a login by academic year and school — /modules/scho
  name: Module Catalogue
  slug: module-catalogue
- description: The Department of Meteorology's data server, metdata.reading.ac.uk, which publishes observations from the University of Reading Atmospheric Observatory — one of the longest continuous climatological r
  name: Meteorology Department Climate Data Services
  slug: met-climate-data
- description: 'The University of Reading runs an Elsevier Pure instance at reading.elsevierpure.com, with a staging sibling at reading-staging.elsevierpure.com. Both returned 401 on 2026-09-01 — the tenancy is real '
  name: Elsevier Pure Research Information System (tenant)
  slug: elsevier-pure-cris
- description: 'The university''s online reading list service, a Talis Aspire tenant at reading.rl.talis.com whose canonical institution URI is http://readinglists.reading.ac.uk/. Genuinely machine-readable: /index.js'
  name: Talis Aspire Online Reading Lists (tenant)
  slug: talis-aspire-reading-lists
- description: The library's catalogue, a SirsiDynix Enterprise tenant at rdg.ent.sirsidynix.net.uk/client/en_GB/library (200 on 2026-09-01), linked from the library's own catalogues page. Alongside it the library r
  name: SirsiDynix Enterprise Library Catalogue (tenant)
  slug: library-catalogue
- description: 'Student and staff timetabling at timetable.reading.ac.uk. Operator is the institution — the host is the university''s own registrable domain and the deployment is theirs — while the application itself '
  name: CMISGo Timetabling (gated)
  slug: timetable
artifact_total: 21
common:
- group: company
  title: ''
  type: Website
  url: https://www.reading.ac.uk/
- group: other
  title: ''
  type: ResearchRepository
  url: https://centaur.reading.ac.uk/
- group: other
  title: ''
  type: ResearchData
  url: https://researchdata.reading.ac.uk/
- group: other
  title: ''
  type: OpenData
  url: https://metdata.reading.ac.uk/
- group: learn
  title: ''
  type: CourseCatalog
  url: https://www.reading.ac.uk/modules/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://www.reading.ac.uk/library/using-the-library/catalogues
- group: other
  title: ''
  type: IdentityFederation
  url: http://mdq.ukfederation.org.uk/entities/%7Bsha1%7D57cf958ecb2c90e4fb339c8cf8a95dcee2d68101
- group: other
  title: ''
  type: AIPolicy
  url: https://www.reading.ac.uk/cqsd/artificial-intelligence
- group: build
  title: ''
  type: AITooling
  url: https://www.reading.ac.uk/digital-technology-services/ai-index-hub
- group: docs
  title: ''
  type: Documentation
  url: https://centaur.reading.ac.uk/information.html
- group: company
  title: ''
  type: Blog
  url: https://blogs.reading.ac.uk/
- group: operate
  title: ''
  type: Support
  url: https://www.reading.ac.uk/contact-us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.reading.ac.uk/about/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.reading.ac.uk/about/privacy
- group: company
  title: ''
  type: LinkedIn
  url: https://uk.linkedin.com/school/university-of-reading/
- group: design
  title: ''
  type: x-conformance
  url: conformance/university-of-reading-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/university-of-reading-authentication.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/university-of-reading-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-reading-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-reading-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-reading-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-reading-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The University of Reading is a public research university in Reading, England, founded in 1926 and ranked #172 in the QS World University Rankings 2025. Its programmable footprint is small, real, and almost entirely scholarly: two OAI-PMH 2.0 harvesting endpoints on its own hosts — CentAUR (64,458 research outputs) and the Research Data Archive — plus the read-only EPrints dataset listings beside them. Both were probed live on 2026-09-01 and both are fully open, with no key, no registration and no advertised rate limit. There is no developer portal, no api.reading.ac.uk, no open-data portal and no OpenAPI, AsyncAPI or apis.json document published by the university anywhere. The institution does operate an Azure API Management gateway on its own domain (esb-prod-api.reading.ac.uk) but publishes no route through it. Its strongest institution-operated machine-readable surface after the repositories is identity: a SAML entity in the UK Access Management Federation (entityID https://reading.ac.uk/oala/metadata,
  scoped reading.ac.uk and reading.edu.my) and a Microsoft Entra ID tenant whose OpenID Connect discovery document is public. It is a registered DataCite member (provider PCLW) and holds a ROR identifier. Almost everything else a reader might mistake for a Reading API is a vendor''s contract running under the university''s name — Elsevier Pure, Talis Aspire, SirsiDynix Enterprise, ProQuest Summon, Springshare LibGuides — and those are recorded here as tenant relationships, not as the university''s engineering.'
finops:
- name: University Of Reading Finops
  service_category: Education
  slug: university-of-reading-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-reading.png
jsonld:
- class_count: 15
  name: University Of Reading Context
  property_count: 6
  slug: university-of-reading-context
layout: provider
modified: '2026-09-01'
name: University of Reading
nav: Providers
network: true
overview: 'University of Reading publishes 4 APIs on the [APIs.io](https://apis.io/) network, including CentAUR OAI-PMH Metadata API, Research Data Archive OAI-PMH Metadata API, CentAUR Repository REST Listings, and 1 more. Tagged areas include University, Higher Education, Education, Research, and Research Repository.


  The University of Reading catalog on APIs.io includes 1 JSON-LD context.


  University of Reading''s developer surface includes documentation, engineering blog, support, authentication, and 19 more developer resources.'
plans:
- name: University Of Reading Plans Pricing
  plan_count: 2
  slug: university-of-reading-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 1
  name: University Of Reading Rate Limits
  slug: university-of-reading-rate-limits
score:
  band: thin
  composite: 38.1
  coverage:
    artifact_dirs: 11
    catalog_gap: 48.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 4.5
    contract_quality: 19.8
    developer_ergonomics: 28.6
    discoverability: 74.1
    governance: 4.5
    operational_transparency: 21.1
  previous_composite: 38.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 72.2
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-reading/refs/heads/main/screenshots/university-of-reading-2026-06-20T200222.png
security:
- kind: authentication
  name: University Of Reading Authentication
  slug: university-of-reading-authentication
  summary_line: none/saml2/oidc · 4 schemes
- kind: domain-security
  name: University Of Reading Domain Security
  slug: university-of-reading-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: University Of Reading Vulnerability Disclosure
  slug: university-of-reading-vulnerability-disclosure
  summary_line: disclosure policy published
slug: university-of-reading
tags:
- University
- Higher Education
- Education
- Research
- Research Repository
- Research Data
- Open Access
- OAI-PMH
- Metadata
- Identity Federation
- Course Catalog
- Library
- Climate Data
- United Kingdom
- England
website: https://www.reading.ac.uk/
---
