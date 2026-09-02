---
access_model:
  confidence: medium
  label: Free · no key required on the probed read endpoints
  onboarding: unknown
  pricing: free
  public: true
  source:
  - probed
  trial: false
  try_now: true
agent_readiness:
  band: human-only
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.0
  scored_at: '2026-09-01'
api_count: 6
apis:
- description: 'e-Repositori (Repositori digital de la UPF) is UPF''s open-access institutional repository, self-hosted on UPF''s own domain. Probed 2026-09-01: GET https://repositori.upf.edu/server/api returns HTTP 20'
  name: UPF Digital Repository REST API (DSpace 7)
  slug: repository-rest
- description: 'OAI-PMH 2.0 metadata harvesting endpoint for e-Repositori, on UPF''s own host. Probed 2026-09-01: verb=Identify returns HTTP 200 text/xml with repositoryName "Repositori digital de la UPF", repositoryI'
  name: UPF Digital Repository OAI-PMH Endpoint
  slug: repository-oai
- description: UPF's institutional single sign-on, registered in eduGAIN through RedIRIS SIR, the Spanish national research and education federation. entityID https://www.rediris.es/sir/upfidp, role IDPSSODescriptor
  name: UPF SAML 2.0 Identity Provider (RedIRIS SIR / eduGAIN)
  slug: identity-federation
- description: 'UPF is a Crossref member and registers DOIs under its own prefix. Probed 2026-09-01: GET https://api.crossref.org/members/14960 returns HTTP 200 with primary-name "Universitat Pompeu Fabra", prefixes '
  name: Crossref Membership (member 14960, prefix 10.31009)
  slug: crossref-member
- description: 'UPF''s entry in the Research Organization Registry. Probed 2026-09-01: GET https://api.ror.org/v2/organizations/04n0g0b29 returns HTTP 200 application/json with ror_display "Universitat Pompeu Fabra". '
  name: ROR Registration (04n0g0b29)
  slug: ror
- description: 'guiesbibtic.upf.edu is UPF Library/CRAI''s guides platform and the host of its generative-AI guidance for students and staff. It is not UPF-operated software: DNS resolves guiesbibtic.upf.edu as a CNAM'
  name: Guies BibTIC (Springshare LibGuides tenant)
  slug: libguides
artifact_total: 11
common:
- group: company
  title: ''
  type: Website
  url: https://www.upf.edu/en/home
- group: docs
  title: ''
  type: APIReference
  url: https://repositori.upf.edu/server/api
- group: docs
  title: ''
  type: Documentation
  url: https://repositori-api.upf.edu/oai/request?verb=Identify
- group: other
  title: ''
  type: ResearchRepository
  url: https://repositori.upf.edu
- group: other
  title: ''
  type: IdentityFederation
  url: https://www.rediris.es/sir/upfidp
- group: build
  title: ''
  type: LibraryCatalog
  url: https://guiesbibtic.upf.edu/
- group: other
  title: ''
  type: AIPolicy
  url: https://guiesbibtic.upf.edu/iag
- group: build
  title: ''
  type: AITooling
  url: https://guiesbibtic.upf.edu/prestatges-virtuals/IA_ensenyament
- group: auth
  title: ''
  type: Authentication
  url: https://repositori.upf.edu/server/api/authn
- group: build
  title: ''
  type: GitHub
  url: https://github.com/MTG
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/universitat-pompeu-fabra/
- group: design
  title: ''
  type: Conformance
  url: conformance/universitat-pompeu-fabra-conformance.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/universitat-pompeu-fabra-context.jsonld
- group: auth
  title: ''
  type: DomainSecurity
  url: security/universitat-pompeu-fabra-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/universitat-pompeu-fabra-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/universitat-pompeu-fabra-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/universitat-pompeu-fabra-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Universitat Pompeu Fabra (UPF) is a public research university in Barcelona, Catalonia, Spain, founded in 1990 and ranked #266 in the QS World University Rankings 2025. UPF operates no developer portal and publishes no OpenAPI, AsyncAPI or SDK of its own; a re-profile on 2026-09-01 probed every candidate host and found none. What it does operate, verified live, is the UPF Digital Repository (e-Repositori) at repositori.upf.edu — self-hosted on UPF''s own domain running DSpace 7.6.8, whose REST/HAL API answers at /server/api with 67 link relations over 78 communities, 1,022 collections and 43,503 discoverable objects, and whose OAI-PMH 2.0 endpoint answers verb=Identify at repositori-api.upf.edu with 13 metadata formats and 100 sets. The repository, the host and the content are UPF''s; the API contract is the DSpace project''s generic open-source one and is deliberately not saved here. The same host runs a real Shibboleth SP — the REST API returns WWW-Authenticate: shibboleth
  with a Shibboleth.sso/Login location — and UPF''s own SAML 2.0 Identity Provider is registered in eduGAIN through RedIRIS SIR, the Spanish national research and education federation, as entityID https://www.rediris.es/sir/upfidp with shibmd:Scope upf.edu, Sirtfi asserted and the REFEDS Research and Scholarship entity category. UPF is a Crossref member (member 14960, DOI prefix 10.31009, 1,593 DOIs) and holds ROR 04n0g0b29; it has no DataCite client of its own. The "UPF en Xifres 2.0" linked open data portal that the June 2026 profile was built around — a CKAN action API and a Virtuoso SPARQL endpoint at data.upf.edu — no longer exists: data.upf.edu returns an authoritative NXDOMAIN from UPF''s own nameservers, and both entries have been removed. Most other UPF software is published by research groups, above all the Music Technology Group on GitHub, rather than as institutional APIs.'
finops:
- name: Universitat Pompeu Fabra Finops
  service_category: Education
  slug: universitat-pompeu-fabra-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/universitat-pompeu-fabra.png
jsonld:
- class_count: 24
  name: Universitat Pompeu Fabra Context
  property_count: 3
  slug: universitat-pompeu-fabra-context
layout: provider
modified: '2026-09-01'
name: Universitat Pompeu Fabra
nav: Providers
network: true
overview: 'Universitat Pompeu Fabra publishes 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include University, Higher Education, Education, Public Research University, and Spain.


  The Universitat Pompeu Fabra catalog on APIs.io includes 1 JSON-LD context.


  Universitat Pompeu Fabra''s developer surface includes API reference, documentation, authentication, GitHub presence, and 14 more developer resources.'
plans:
- name: Universitat Pompeu Fabra Plans Pricing
  plan_count: 2
  slug: universitat-pompeu-fabra-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 1
  name: Universitat Pompeu Fabra Rate Limits
  slug: universitat-pompeu-fabra-rate-limits
score:
  band: thin
  composite: 26.9
  coverage:
    artifact_dirs: 8
    catalog_gap: 48.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 5.1
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 4.5
    contract_quality: 14.3
    developer_ergonomics: 16.7
    discoverability: 74.1
    governance: 4.5
    operational_transparency: 26.3
  previous_composite: 21.8
  provenance:
    conformance: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 46.3
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/universitat-pompeu-fabra/refs/heads/main/screenshots/universitat-pompeu-fabra-2026-06-20T200116.png
security:
- kind: domain-security
  name: Universitat Pompeu Fabra Domain Security
  slug: universitat-pompeu-fabra-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: universitat-pompeu-fabra
tags:
- University
- Higher Education
- Education
- Public Research University
- Spain
- Catalonia
- Barcelona
- Institutional Repository
- Research Data
- Identity Federation
- OAI-PMH
- DSpace
- Shibboleth
- Crossref
website: https://www.upf.edu/en/home
---
