---
access_model:
  confidence: high
  label: Free · no registration, no credential issued
  onboarding: unknown
  pricing: free
  public: true
  source:
  - probe
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 18.0
  scored_at: '2026-09-01'
api_count: 3
apis:
- description: 'A public, keyless JSON endpoint served by the university''s own website CMS at www.wgtn.ac.nz/api/globalobject. It returns the global site object every page is built from: canonical base URLs including'
  name: Website Global Object
  slug: website-global-object
- description: The university's own SAML 2.0 Identity Provider. entityID https://idp.vuw.ac.nz/idp/shibboleth, shibmd:Scope vuw.ac.nz, metadata served unauthenticated over HTTPS GET and republished in the signed Tua
  name: Shibboleth Identity Provider (Tuakiri / eduGAIN)
  slug: identity-federation
- description: 'The university''s institutional repository, ir.wgtn.ac.nz, running DSpace 7.6.7 on the institution''s OWN infrastructure: the host sits under its own registrable domain, carries no CNAME to any vendor, '
  name: Institutional Repository (self-hosted DSpace)
  slug: institutional-repository
- description: The university's Open Access institutional repository is a Figshare portal running on the institution's own vanity domain openaccess.wgtn.ac.nz, which CNAMEs to figshare.com, with wellington.figshare.
  name: Open Access Repository (Figshare tenancy)
  slug: open-access-repository-figshare
- description: 'Te Waharoa is the library''s discovery service, running on Ex Libris Primo backed by Alma on the institution''s own subdomain tewaharoa.victoria.ac.nz, which CNAMEs to victoria.primo.exlibrisgroup.com. '
  name: Te Waharoa Library Discovery (Ex Libris Primo / Alma tenancy)
  slug: te-waharoa-discovery
- description: Nuku is the university's brand for its learning-management system, an Instructure Canvas tenant at nuku.wgtn.ac.nz, which CNAMEs to wgtn-vanity.instructure.com. The Canvas REST API is present and live
  name: Nuku Learning Management (Instructure Canvas tenancy)
  slug: nuku-canvas-lms
- description: The university's research information system is Symplectic Elements at elements.wgtn.ac.nz, which CNAMEs to vuw.elements.symplectic.org. HTTP 401 to an anonymous request on 2026-08-30 — live, and gate
  name: Research Information System (Symplectic Elements tenancy)
  slug: symplectic-elements
- description: The university self-hosts a WSO2 Identity Server at auth-eis.vuw.ac.nz — no CNAME, resolving directly to 130.195.13.55 inside the institution's own address space — and it is the SAML issuer that front
  name: Enterprise Single Sign-On (WSO2 Identity Server)
  slug: enterprise-sso-wso2
- description: The registrar and student-records system at studentrecords.vuw.ac.nz. The sign-on RelayState /c/auth/SSB identifies it as Ellucian Banner Self-Service, and the host resolves directly to 130.195.15.120
  name: Student Records (Ellucian Banner Self-Service tenancy)
  slug: student-records-banner
- description: 'Production browser single sign-on for the university''s student-facing services federates to a Microsoft Entra ID tenant, cfe63e23-6951-427e-8683-bb84dcf1d20c, observed on the Nuku learning-management '
  name: Microsoft Entra ID Tenant (production browser sign-on)
  slug: entra-id-federation
artifact_total: 21
common:
- group: company
  title: ''
  type: Website
  url: https://www.wgtn.ac.nz/
- group: company
  title: ''
  type: Blog
  url: https://www.wgtn.ac.nz/news/rss
- group: operate
  title: ''
  type: Support
  url: https://www.wgtn.ac.nz/about/contacts
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.wgtn.ac.nz/site-info/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.wgtn.ac.nz/site-info
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/victoria-university-of-wellington/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/victoriauniversity
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/VUW-Library
- group: other
  title: ''
  type: ResearchComputing
  url: https://vuw-research-computing.github.io/raapoi-docs/
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/vuw-research-computing
- group: learn
  title: ''
  type: CourseCatalog
  url: https://www.wgtn.ac.nz/courses
- group: learn
  title: ''
  type: x-course-sitemap
  url: https://www.wgtn.ac.nz/sitemap-courses.xml
- group: other
  title: ''
  type: ResearchRepository
  url: https://openaccess.wgtn.ac.nz/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://tewaharoa.victoria.ac.nz/discovery/search?vid=64VUW_INST:VUWNUI
- group: other
  title: ''
  type: IdentityFederation
  url: https://idp.vuw.ac.nz/idp/shibboleth
- group: auth
  title: ''
  type: x-authentication
  url: authentication/victoria-university-of-wellington-authentication.yml
- group: auth
  title: ''
  type: x-scopes
  url: scopes/victoria-university-of-wellington-scopes.yml
- group: design
  title: ''
  type: x-errors
  url: errors/victoria-university-of-wellington-errors.yml
- group: design
  title: ''
  type: x-lifecycle
  url: lifecycle/victoria-university-of-wellington-lifecycle.yml
- group: design
  title: ''
  type: x-conformance
  url: conformance/victoria-university-of-wellington-conformance.yml
- group: other
  title: ''
  type: ResearchRepository
  url: https://ir.wgtn.ac.nz/
- group: other
  title: ''
  type: x-oai-pmh
  url: https://ir.wgtn.ac.nz/oai/request?verb=Identify
- group: other
  title: ''
  type: x-opensearch
  url: https://ir.wgtn.ac.nz/server/opensearch/service
- group: docs
  title: ''
  type: APIReference
  url: https://ir.wgtn.ac.nz/server/api
- group: auth
  title: ''
  type: DomainSecurity
  url: security/victoria-university-of-wellington-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/victoria-university-of-wellington-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/victoria-university-of-wellington-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/victoria-university-of-wellington-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Te Herenga Waka—Victoria University of Wellington is a public research university in Wellington, Aotearoa New Zealand, and it operates almost no programmable surface of its own. It publishes no developer portal, no API documentation, no API keys, no status page and no changelog. What it has instead is what most universities have: a federation of vendor platforms bought under its own name, and four surfaces it genuinely runs itself. The four are a self-hosted DSpace 7.6.7 institutional repository at ir.wgtn.ac.nz — no CNAME, its own address space, 23,150 records harvestable over its own keyless OAI-PMH 2.0 base URL in twelve metadata formats, with an anonymously readable DSpace REST root, an OpenSearch 1.1 description and FAIR Signposting link sets alongside it; an undocumented but public, keyless JSON configuration endpoint on its own website (www.wgtn.ac.nz/api/globalobject, HTTP 200, CORS open to all origins); a self-hosted WSO2 Identity Server at auth-eis.vuw.ac.nz that
  issues SAML for the student-records system and whose every discovery endpoint answers HTTP 403 behind a web application firewall — live and protected, not missing; and a SAML 2.0 Shibboleth Identity Provider at idp.vuw.ac.nz, entityID https://idp.vuw.ac.nz/idp/shibboleth, scope vuw.ac.nz, registered in the Tuakiri New Zealand Access Federation since 2012 with the REFEDS Research & Scholarship entity category and a REFEDS Sirtfi assurance certification. The repository and the identity federation entry are the institution''s most durable and most genuinely machine-readable assets, and both are classes of interface a university operates by definition rather than by purchase. Everything else programmable that carries the university''s name is a tenancy: the Open Access research repository is a SECOND, Figshare-hosted repository on the institution''s own openaccess.wgtn.ac.nz vanity domain (OAI-PMH set portal_771, DataCite repository FIGSHARE.VUW, 4,301 DOIs) — the university runs two repositories,
  one its own and one bought; Te Waharoa library discovery is an Ex Libris Primo/Alma deployment on tewaharoa.victoria.ac.nz whose SRU 1.2 endpoint is anonymously callable and returns MARCXML; Nuku is an Instructure Canvas tenant; the research information system is Symplectic Elements; and browser sign-on for student services federates to a Microsoft Entra ID tenant. The data in those systems is the university''s. The contracts are not, and none of them are saved here. A previous profile of this institution attributed Figshare''s generic v2 REST API to it as though the university had written it; that contract and the sixteen artifacts derived from it have been removed. The institution also runs three public GitHub organisations, of which only VUW Research Computing — documenting the Rāpoi HPC cluster — is currently active, and it publishes a 12,160-URL machine-readable course sitemap covering every course-year page. The registrar surface, where student-built course APIs appear at peer institutions,
  is a self-hosted Ellucian Banner Self-Service behind SAML with no public interface at all.'
examples:
- key_count: 8
  name: Victoria University Of Wellington Globalobject Example
  slug: victoria-university-of-wellington-globalobject-example
- key_count: 6
  name: Victoria University Of Wellington Ir Dspace Root
  slug: victoria-university-of-wellington-ir-dspace-root
finops:
- name: Victoria University Of Wellington Finops
  service_category: Education
  slug: victoria-university-of-wellington-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/victoria-university-of-wellington.png
json_schemas:
- name: Te Herenga Waka Website Global Object
  property_count: 0
  slug: victoria-university-of-wellington-globalobject
jsonld:
- class_count: 16
  name: Victoria University Of Wellington Context
  property_count: 27
  slug: victoria-university-of-wellington-context
layout: provider
modified: '2026-08-30'
name: Victoria University of Wellington
nav: Providers
network: true
overview: 'Victoria University of Wellington publishes 3 APIs on the [APIs.io](https://apis.io/) network: Website Global Object, Shibboleth Identity Provider (Tuakiri / eduGAIN), and Institutional Repository (self-hosted DSpace). Tagged areas include University, Higher Education, Education, New Zealand, and Public Research University.


  The Victoria University of Wellington catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Victoria University of Wellington''s developer surface includes engineering blog, support, API reference, and 26 more developer resources.'
plans:
- name: Victoria University Of Wellington Plans Pricing
  plan_count: 2
  slug: victoria-university-of-wellington-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 1
  name: Victoria University Of Wellington Rate Limits
  slug: victoria-university-of-wellington-rate-limits
rules:
- effective_rule_count: 52
  extends:
  - spectral:oas
  name: Victoria University of Wellington API Rules
  rule_count: 11
  severity_counts:
    error: 7
    hint: 0
    info: 0
    warn: 4
  slug: victoria-university-of-wellington-rules
scopes:
- name: Victoria University Of Wellington Scopes
  scope_count: 0
  slug: victoria-university-of-wellington-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 36.1
  coverage:
    artifact_dirs: 17
    catalog_gap: 36.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -11.2
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 45.5
    contract_quality: 26.8
    developer_ergonomics: 23.8
    discoverability: 74.1
    governance: 45.5
    operational_transparency: 7.9
  previous_composite: 47.3
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
    score: 53.7
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/victoria-university-of-wellington/refs/heads/main/screenshots/victoria-university-of-wellington-2026-06-20T201017.png
security:
- kind: authentication
  name: Victoria University Of Wellington Authentication
  slug: victoria-university-of-wellington-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Victoria University Of Wellington Domain Security
  slug: victoria-university-of-wellington-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: victoria-university-of-wellington
tags:
- University
- Higher Education
- Education
- New Zealand
- Public Research University
- Research
- Open Access
- Research Repository
- Institutional Repository
- OAI-PMH
- DSpace
- Library
- Course Catalog
- Identity Federation
- Research Computing
website: https://www.wgtn.ac.nz/
---
