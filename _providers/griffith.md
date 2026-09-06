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
  scored_at: '2026-09-05'
api_count: 8
apis:
- description: Griffith's SAML 2.0 Shibboleth Identity Provider, entityID https://idp1.griffith.edu.au/idp/shibboleth, registered in the Australian Access Federation on 2023-03-06 and exported to eduGAIN as entity 6
  name: Griffith University SAML Identity Provider (AAF / eduGAIN)
  slug: aaf-idp
- description: REST API for Griffith Research Online, the university's institutional repository, running DSpace 7.6. Serves communities, collections, items, bitstreams and metadata for Griffith research outputs; the
  name: Griffith Research Online (GRO) DSpace REST API
  slug: gro-rest
- description: OAI-PMH 2.0 metadata harvesting endpoint for Griffith Research Online. The Identify response returns repositoryName "Griffith Research Online", adminEmail gro@griffith.edu.au, repositoryIdentifier res
  name: Griffith Research Online OAI-PMH
  slug: gro-oai
- description: Griffith Experts is the university's public researcher-profile and research-output discovery portal, running Symplectic Discovery (web-v6.22.0.4). Griffith's own library publishes a tutorial titled "G
  name: Griffith Experts (Symplectic Discovery)
  slug: experts
- description: Griffith operates an Instructure Canvas learning management system at lms.griffith.edu.au. The tenancy exposes two publicly fetchable machine-readable surfaces — an LTI 1.3 platform JWKS at /api/lti/s
  name: Griffith Canvas LMS (Instructure) — LTI 1.3 and REST
  slug: canvas-lms
- description: Griffith University is a DataCite provider, registering DOIs for its research outputs and datasets. Provider id "griffith", symbol "GRIFFITH". Recorded as a membership fact about Griffith; the DataCit
  name: DataCite DOI Registrant — Griffith University
  slug: datacite
- description: Griffith University is Crossref member 5850. Two sub-unit members also resolve under the Griffith name — 50610 Griffith Law School and 22062 School of Human Services and Social Work, Griffith Universi
  name: Crossref Member — Griffith University
  slug: crossref
- description: Griffith University is registered in the Research Organization Registry as https://ror.org/02sc3r913. Recorded as a membership fact; the ROR API contract is ROR's.
  name: ROR Registry Record — Griffith University
  slug: ror
artifact_total: 13
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/griffith-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.griffith.edu.au/
- group: other
  title: ''
  type: ResearchRepository
  url: https://research-repository.griffith.edu.au/
- group: other
  title: ''
  type: IdentityFederation
  url: authentication/griffith-identity-federation.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/griffith-domain-standards.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GriffithUniLibrary
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/gu-eresearch
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/griffith-university/
- group: commercial
  title: ''
  type: Plans
  url: plans/griffith-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/griffith-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/griffith-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
coverage:
  detail: 'Griffith University publishes no institution-authored API contract and operates no developer portal. A DNS-based operator audit on 2026-09-01 resolved every machine-readable surface on a griffith.edu.au hostname onto a vendor platform — research-repository -> atmire.com, lms -> instructure.com, experts -> symplectic.org — so all three are recorded as tenancies rather than as Griffith contracts. The institution''s own engineering identity is its SAML 2.0 Shibboleth IdP in the Australian Access Federation, exported to eduGAIN, which is recorded as `federation` and is genuinely Griffith''s. Three registry memberships (DataCite provider `griffith`, Crossref member 5850, ROR 02sc3r913) are recorded as facts about Griffith, never as Griffith contracts. Administrative, course-catalog, timetable and registrar interfaces were hunted and none resolve publicly — api., data., courses., programs-courses., timetable., library., sso. and idp. under griffith.edu.au all return NXDOMAIN. The Canvas
    REST API is live but authenticated (401). The main www host sits behind a Cloudflare managed challenge (403, cf-mitigated: challenge) for every non-browser client, including with full browser headers over HTTP/2, so llms.txt, robots.txt and .well-known probes could not be completed there; that is a finding about the edge, not a gap in Griffith''s publishing. No OpenAPI, AsyncAPI or apis.json artifact is saved for Griffith because none belonging to Griffith exists.'
  evidence:
  - status: 200
    url: https://idp1.griffith.edu.au/idp/shibboleth
  - status: 200
    url: https://md.aaf.edu.au/aaf-metadata.xml
  - status: 200
    url: https://research-repository.griffith.edu.au/server/oai/request?verb=Identify
  - status: 200
    url: https://research-repository.griffith.edu.au/server/api
  - status: 200
    url: https://lms.griffith.edu.au/api/lti/security/jwks
  - status: 200
    url: https://lms.griffith.edu.au/.well-known/openid-configuration
  - status: 401
    url: https://lms.griffith.edu.au/api/v1/accounts
  - status: 200
    url: https://experts.griffith.edu.au/
  - status: 403
    url: https://www.griffith.edu.au/
  - status: 403
    url: https://www.griffith.edu.au/llms.txt
  - status: 403
    url: https://www.griffith.edu.au/.well-known/apis.json
  - status: 200
    url: https://api.datacite.org/providers?query=Griffith
  - status: 200
    url: https://api.crossref.org/members?query=Griffith
  - status: 200
    url: https://api.ror.org/v2/organizations?query=Griffith+University
  - status: 0
    url: https://api.griffith.edu.au/
  - status: 0
    url: https://data.griffith.edu.au/
  - status: 0
    url: https://programs-courses.griffith.edu.au/
  reason: tenant_only
  state: gated
created: '2026-06-03'
description: 'Griffith University is a public research university in South East Queensland, Australia, a member of the Innovative Research Universities (IRU) network and ranked #255 in the QS World University Rankings 2025. Griffith operates no public developer portal and publishes no institution-authored API contract; a 2026-09-01 operator audit found that every machine-readable surface running under a griffith.edu.au hostname is a vendor platform under a Griffith tenancy, confirmed by DNS. Griffith Research Online (research-repository.griffith.edu.au) is a DSpace 7.6 repository hosted by Atmire, serving a live REST API and a fully conformant OAI-PMH 2.0 endpoint over Griffith''s own research outputs. lms.griffith.edu.au is an Instructure Canvas tenancy exposing an LTI 1.3 keyset and an OpenID Connect discovery document, with the REST API itself behind authentication. Griffith Experts (experts.griffith.edu.au) is a Symplectic Discovery deployment. The one surface that is unambiguously Griffith''s
  own engineering identity is its SAML 2.0 Shibboleth Identity Provider, registered in the Australian Access Federation and exported to eduGAIN with REFEDS Research & Scholarship, Code of Conduct v2 and SIRTFI assertions. Griffith is additionally a registrant in DataCite, Crossref and ROR. The main website sits behind a Cloudflare managed challenge and is unreadable to non-browser clients.'
finops:
- name: Griffith Finops
  service_category: Education
  slug: griffith-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/griffith.png
jsonld:
- class_count: 19
  name: Griffith Context
  property_count: 12
  slug: griffith-context
layout: provider
modified: '2026-09-01'
name: Griffith University
nav: Providers
network: true
overview: 'Griffith University publishes 8 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Australia, and Queensland.


  The Griffith University catalog on APIs.io includes 1 JSON-LD context.'
plans:
- name: Griffith Plans Pricing
  plan_count: 2
  slug: griffith-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 1
  name: Griffith Rate Limits
  slug: griffith-rate-limits
score:
  band: emerging
  composite: 26.1
  coverage:
    artifact_dirs: 9
    catalog_earned: 65.0
    catalog_earned_first_party: 0.0
    catalog_gap: 50.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.4
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 18.0
    developer_ergonomics: 28.6
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 23.7
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - australia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - anz
  previous_composite: 26.5
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 31.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/griffith/refs/heads/main/screenshots/griffith-2026-06-20T182409.png
security:
- kind: domain-security
  name: Griffith Domain Security
  slug: griffith-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: griffith
tags:
- Education
- Higher Education
- University
- Australia
- Queensland
- Innovative Research Universities
- Research
- Research Repository
- Identity Federation
- Learning Management
- OAI-PMH
- Open Data
- Repository
website: https://www.griffith.edu.au/
---
