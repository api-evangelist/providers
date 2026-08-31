---
access_model:
  confidence: high
  label: Free · Institutional affiliation or federation membership required
  onboarding: unknown
  pricing: free
  public: false
  source:
  - identity-federation
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-08-30'
api_count: 8
apis:
- description: Deakin's Shibboleth identity provider, self-hosted and self-described. The EntityDescriptor at https://signon.deakin.edu.au/idp/shibboleth declares protocol support for SAML 2.0, a signing and an encr
  name: Deakin University SAML 2.0 Identity Provider
  slug: saml-idp
- description: The federation-registered deployment of the same entityID. In the AAF production aggregate, https://signon.deakin.edu.au/idp/shibboleth carries SingleSignOnService locations on aaf.deakin.edu.au, whic
  name: Deakin University federated SSO (AAF Rapid IdP)
  slug: aaf-federated-idp
- description: 'Deakin''s research data portal, used to share datasets and collected materials with the Australian research community. Institution-operated: dataportal.deakin.edu.au CNAMEs to aafapp-p7-web-2020013100-'
  name: Deakin Data Portal
  slug: dataportal
- description: Deakin Research Online is Deakin's institutional research repository, running on figshare. dro.deakin.edu.au is a CNAME to proxy-eu-01.figshare.com and returns HTTP 202 with a zero-byte body to automa
  name: Deakin Research Online (DRO) — figshare tenant
  slug: dro-figshare
- description: Deakin's learning management system. d2l.deakin.edu.au CNAMEs to deakin.brightspace.com on AWS ap-southeast-2. Its keyless D2L Valence version manifest at /d2l/api/versions/ answers HTTP 200 with appl
  name: CloudDeakin — D2L Brightspace tenant
  slug: clouddeakin
- description: Library discovery for Deakin. library.deakin.edu.au resolves to 216.147.221.162, which whois attributes to Ex Libris (USA) Inc. (netname EXLIBRIS-20-1) — a vendor platform under a Deakin hostname. The
  name: Deakin University Library catalogue — Ex Libris tenant
  slug: library-discovery
- description: Deakin's own DataCite repository account, held under the ARDC (Australian Research Data Commons) consortium since 2020-05-14, with DOI prefix 10.26187. 4,597 DOIs are registered against it and 4,596 c
  name: Deakin University DataCite repository (ARDCX.DEAKIN)
  slug: datacite-repository
- description: Deakin is a Crossref member depositing its own DOIs under prefix 10.21153 — 1,303 works, predominantly journal articles from its scholarly publishing. Publicly queryable through the Crossref REST API.
  name: Deakin University Crossref membership (member 8935)
  slug: crossref-member
artifact_total: 12
common:
- group: company
  title: ''
  type: Website
  url: https://www.deakin.edu.au/
- group: other
  title: ''
  type: IdentityFederation
  url: identity-federation/deakin-identity-federation.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/deakin-conformance.yml
- group: other
  title: ''
  type: OpenData
  url: https://dataportal.deakin.edu.au/
- group: other
  title: ''
  type: ResearchRepository
  url: https://dro.deakin.edu.au/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://www.deakin.edu.au/library
- group: learn
  title: ''
  type: CourseCatalog
  url: https://www.deakin.edu.au/study/find-a-course
- group: other
  title: ''
  type: AIPolicy
  url: https://www.deakin.edu.au/about-deakin/why-deakin/generative-artificial-intelligence
- group: build
  title: ''
  type: AITooling
  url: https://www.deakin.edu.au/students/study-support/study-resources/artificial-intelligence
- group: build
  title: ''
  type: GitHub
  url: https://github.com/Deakin
- group: company
  title: ''
  type: LinkedIn
  url: https://au.linkedin.com/school/deakin-university/
- group: company
  title: ''
  type: Blog
  url: https://blogs.deakin.edu.au/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/deakin-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/deakin-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/deakin-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/deakin-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Deakin University is a public research university in Victoria, Australia, with campuses in Geelong, Warrnambool and Melbourne. Its genuinely institution-operated programmable footprint is small, real, and entirely in identity federation. Deakin self-publishes a complete SAML 2.0 EntityDescriptor at signon.deakin.edu.au/idp/shibboleth for a Shibboleth identity provider it runs on its own APNIC address space (128.184.0.0/16, netname DEAKINUNIVERSITY) under a Deakin-procured DigiCert certificate, and it registers that IdP plus three production service providers — the Deakin Data Portal, Envirocare and OT Simulations — in the Australian Access Federation. That metadata document is the only institution-operated machine-readable contract in this profile, and it is what earns Deakin its SAML and Shibboleth conformance. Deakin is also the registrant behind 4,597 DataCite DOIs (prefix 10.26187, repository ARDCX.DEAKIN under ARDC) and 1,303 Crossref deposits (member 8935, prefix 10.21153).
  Everything else that looks like a Deakin API belongs to a platform Deakin buys: Deakin Research Online is figshare (dro.deakin.edu.au CNAMEs to proxy-eu-01.figshare.com), CloudDeakin is D2L Brightspace (d2l.deakin.edu.au CNAMEs to deakin.brightspace.com, and its keyless Valence version manifest is the only JSON API answering on any deakin.edu.au host), library discovery resolves into Ex Libris address space, and the federated SSO endpoints registered with AAF sit on AAF''s managed Rapid IdP on Amazon infrastructure. Those are recorded here as tenant relationships, not as Deakin contracts. There is no central developer portal, no institution-operated OAI-PMH endpoint, and no public course or campus API. The wider deakin.edu.au web estate — www, blogs, the Data Portal, the handbook — sits behind F5/Shape bot protection that answers automated clients with a JavaScript challenge, so it is not machine-readable at all.'
finops:
- name: Deakin Finops
  service_category: Education
  slug: deakin-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/deakin.png
layout: provider
modified: '2026-08-30'
name: Deakin University
nav: Providers
network: true
overview: 'Deakin University publishes 8 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Research, and Australia.


  Deakin University''s developer surface includes GitHub presence, engineering blog, and 15 more developer resources.'
plans:
- name: Deakin Plans Pricing
  plan_count: 2
  slug: deakin-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 1
  name: Deakin Rate Limits
  slug: deakin-rate-limits
score:
  band: emerging
  composite: 21.5
  coverage:
    artifact_dirs: 8
    catalog_gap: 56.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -21.2
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 10.5
    developer_ergonomics: 16.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 42.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 20.4
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/deakin/refs/heads/main/screenshots/deakin-2026-06-20T175744.png
security:
- kind: domain-security
  name: Deakin Domain Security
  slug: deakin-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: deakin
tags:
- Education
- Higher Education
- University
- Research
- Australia
- Victoria
- Identity Federation
- Research Repository
- Research Data
- Learning Management
website: https://www.deakin.edu.au/
---
