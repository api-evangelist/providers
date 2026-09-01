---
access_model:
  confidence: high
  label: Free and keyless for the public OAI-PMH surface · everything else is affiliation-gated
  onboarding: unknown
  pricing: free
  public: true
  source:
  - authentication
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
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: 'OAI-PMH 2.0 harvesting interface for RePub, the Erasmus University Rotterdam institutional publication repository. Keyless and live: Identify, ListMetadataFormats, ListSets and ListIdentifiers all ret'
  name: RePub OAI-PMH Metadata Harvesting Interface
  slug: repub-oai
- description: 'An EUR-operated Kong API gateway. It is unambiguously live and unambiguously closed: the root returns 401 application/json {"message":"Unauthorized"} with WWW-Authenticate: Basic realm="kong", HSTS ma'
  name: EUR API Gateway (api.eur.nl)
  slug: api-gateway
- description: 'The EUR & Erasmus MC research information portal runs on Elsevier Pure (CRIS). Its OAI-PMH endpoint is live (Identify 200, repositoryName "EUR Research Repository", earliestDatestamp 2021-06-14T10:37:'
  name: EUR Research Repository — Pure OAI-PMH (Elsevier tenancy)
  slug: pure-oai
- description: EUR's institutional research DATA repository, distinct from the RePub publication repository. This entry replaces the ten Figshare contracts the June 2026 profile saved here. Two things were wrong wit
  name: EUR Data Repository (DataverseNL tenancy)
  slug: edr-dataverse
- description: 'EUR''s learning management system. Live and credentialed: /api/v1/courses returns 401 {"status":"unauthenticated","errors":[{"message":"user authorisation required"}]}. Two machine-readable surfaces an'
  name: Canvas LMS (Instructure tenancy) — REST + LTI 1.3
  slug: canvas-lms
- description: 'EUR''s course catalogue and student self-service, on Caci''s OSIRIS. The public entry points courses.eur.nl and osiris.eur.nl both land on an Angular SPA shell that returns HTTP 200 with no data, which '
  name: OSIRIS Course Catalogue (Caci tenancy)
  slug: osiris-course-catalog
- description: EUR's identity federation entry — the machine-readable institutional surface universities almost never get catalogued for. EUR is registered as an identity provider in SURFconext, the Dutch national r
  name: SURFconext / eduGAIN Identity Provider
  slug: surfconext-idp
artifact_total: 14
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
common:
- group: company
  title: ''
  type: Website
  url: https://www.eur.nl/en
- group: other
  title: ''
  type: IdentityFederation
  url: https://metadata.surfconext.nl/idps-metadata.xml
- group: other
  title: ''
  type: ResearchRepository
  url: https://repub.eur.nl/
- group: other
  title: ''
  type: ResearchRepository
  url: https://dataverse.nl/dataverse/eur
- group: other
  title: ''
  type: ResearchRepository
  url: https://pure.eur.nl/
- group: learn
  title: ''
  type: CourseCatalog
  url: https://courses.eur.nl/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://www.eur.nl/en/library
- group: other
  title: ''
  type: AIPolicy
  url: https://www.eur.nl/en/about-university/policy-and-regulations/regulations-and-guidelines/ai-usage-guidelines
- group: build
  title: ''
  type: AITooling
  url: https://www.eur.nl/en/about-university/vision-strategy-2030/aieur
- group: design
  title: ''
  type: Conformance
  url: conformance/erasmus-university-rotterdam-education-standards.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/erasmus-university-rotterdam-authentication.yml
- group: design
  title: ''
  type: Errors
  url: errors/erasmus-university-rotterdam-errors.yml
- group: build
  title: ''
  type: Examples
  url: examples/erasmus-university-rotterdam-examples.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/erasmus-university-rotterdam-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/erasmus-university-rotterdam-domain-security.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: https://www.eur.nl/.well-known/security.txt
- group: operate
  title: ''
  type: Status
  url: https://status.eur.nl/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/eur-nl
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/erasmus-university-rotterdam/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.eur.nl/en/disclaimer
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.eur.nl/en/privacy
- group: docs
  title: ''
  type: Documentation
  url: https://www.eur.nl/en/library/research-support
- group: start
  title: ''
  type: Registry
  url: https://ror.org/057w15z03
- group: commercial
  title: ''
  type: Plans
  url: plans/erasmus-university-rotterdam-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/erasmus-university-rotterdam-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/erasmus-university-rotterdam-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
coverage:
  detail: 'Erasmus University Rotterdam publishes no API of its own — no OpenAPI, no developer portal, no API reference, no open data portal, no llms.txt. It operates exactly one public, callable, keyless API — the RePub OAI-PMH 2.0 harvesting endpoint — and it publishes no machine-readable contract for it. The OpenAPI in this repo is DERIVED by API Evangelist from live probes, not published by EUR. Everything else is either a vendor platform running under an eur.nl hostname or a gateway that exposes nothing to an unauthenticated caller. Nothing blocked us: sixty-plus hosts and paths were probed successfully and the thinness is the institution''s, not a fetch failure. Verified institution-operated and live: https://repub.eur.nl/oai answers Identify (repositoryName "Erasmus University OAIPMH Feed", adminEmail opdecoul@ubib.eur.nl and vanhuisstede@ubib.eur.nl, earliestDatestamp 2023-11-24T00:00:00Z, deletedRecord transient), ListMetadataFormats (oai_dc, mods, nl_didl), ListSets (openaire,
    nwo) and ListIdentifiers, all 200, all keyless; repub.eur.nl is a CNAME to bib-app01.ubib.eur.nl -> 145.5.2.24 with no vendor in the chain. Institution-operated but closed: https://api.eur.nl/ returns 401 with WWW-Authenticate: Basic realm="kong" and {"message":"Unauthorized"}, and every probed path returns Kong''s {"message":"no Route matched with those values"} — a real EUR-run API gateway (api.eur.nl -> api2.eur.nl -> 145.5.1.16) whose entire route table, documentation and contract are private; /openapi.json, /swagger.json, /docs, /v1, /api, /health and /status were all probed. Institution-operated non-API surfaces: a live RFC 9116 https://www.eur.nl/.well-known/security.txt (Contact mailto:cert@eur.nl, Expires 2026-12-07, policy and hall-of-fame URLs, both 200) and a status page at status.eur.nl (200, "Status: Erasmus University Rotterdam", on Netlify, with no JSON feed — /api/v2/status.json and /index.json both 404). Verified live but tenant-operated: pure.eur.nl (CNAME erasmus.elsevierpure.com
    -> eu.prod.elsevierpure.com, OAI-PMH 200 with the OpenAIRE CERIF 1.2 profile, adminEmail purehosted@elsevier.com, /ws/api/524/openapi.json 401), canvas.eur.nl (CNAME EUR-vanity.instructure.com, LTI 1.3 JWKS 200 and .well-known/openid-configuration 200, /api/v1/courses 401), eur.osiris-student.nl (Caci OSIRIS; the SPA shell 200s but POST /student/osiris/student/cursussen/zoeken returns a structured OSIRIS Link JSON error with an exchange-id, proving a live service behind it), and dataverse.nl/dataverse/eur (200; the dataverse.nl API is behind an Anubis proof-of-work bot challenge, so /api/info/version and /api/dataverses/eur return the challenge page rather than JSON — the host is live, we are the ones excluded). Confirmed dead or absent: datarepository.eur.nl returns NXDOMAIN — the Figshare-era repository hostname the June profile''s vocabulary and rulesets still cited; no DNS for developer.eur.nl, developers.eur.nl, opendata.eur.nl, data.open.eur.nl, edr.eur.nl, dataverse.eur.nl, idp.eur.nl,
    adfs.eur.nl, hpc.eur.nl, mcp.eur.nl, library.eur.nl, primo.eur.nl, catalogue.eur.nl, vle.eur.nl or lms.eur.nl; data.eur.nl resolves but serves only a Taggrs server-side tracking endpoint, not open data; www.eur.nl/llms.txt, /.well-known/api-catalog, /.well-known/ai-plugin.json and /openapi.json all return the site''s soft 404 ("Pagina niet gevonden", 146,268 bytes of HTML under an HTTP 404 status).'
  evidence:
  - status: 200
    url: https://repub.eur.nl/oai?verb=Identify
  - status: 200
    url: https://repub.eur.nl/oai?verb=ListMetadataFormats
  - status: 200
    url: https://repub.eur.nl/oai?verb=ListSets
  - status: 200
    url: https://repub.eur.nl/oai?verb=ListIdentifiers&metadataPrefix=oai_dc
  - status: 200
    url: https://repub.eur.nl/oai?verb=BadVerb
  - status: 200
    url: https://repub.eur.nl/
  - status: 404
    url: https://repub.eur.nl/openapi.json
  - status: 401
    url: https://api.eur.nl/
  - status: 404
    url: https://api.eur.nl/openapi.json
  - status: 404
    url: https://api.eur.nl/swagger.json
  - status: 401
    url: https://api.eur.nl/docs
  - status: 404
    url: https://api.eur.nl/v1
  - status: 200
    url: https://pure.eur.nl/ws/oai?verb=Identify
  - status: 200
    url: https://pure.eur.nl/ws/oai?verb=ListMetadataFormats
  - status: 200
    url: https://pure.eur.nl/ws/oai?verb=ListSets
  - status: 200
    url: https://pure.eur.nl/ws/api
  - status: 401
    url: https://pure.eur.nl/ws/api/524/openapi.json
  - status: 200
    url: https://canvas.eur.nl/api/lti/security/jwks
  - status: 200
    url: https://canvas.eur.nl/.well-known/openid-configuration
  - status: 401
    url: https://canvas.eur.nl/api/v1/courses
  - status: 401
    url: https://canvas.eur.nl/login/oauth2/auth
  - status: 500
    url: https://eur.osiris-student.nl/student/osiris/student/cursussen/zoeken
  - status: 200
    url: https://courses.eur.nl/
  - status: 200
    url: https://dataverse.nl/dataverse/eur
  - status: 200
    url: https://dataverse.nl/api/info/version
  - status: 200
    url: https://metadata.surfconext.nl/idps-metadata.xml
  - status: 200
    url: https://api.datacite.org/providers/dhcm
  - status: 200
    url: https://api.datacite.org/repositories?provider-id=dhcm
  - status: 200
    url: https://api.datacite.org/dois?provider-id=dhcm
  - status: 200
    url: https://api.crossref.org/members?query=erasmus+university+rotterdam
  - status: 200
    url: https://api.ror.org/v2/organizations/057w15z03
  - status: 200
    url: https://www.eur.nl/.well-known/security.txt
  - status: 200
    url: https://status.eur.nl/
  - status: 404
    url: https://status.eur.nl/api/v2/status.json
  - status: 404
    url: https://www.eur.nl/llms.txt
  - status: 404
    url: https://www.eur.nl/.well-known/api-catalog
  - status: 404
    url: https://www.eur.nl/openapi.json
  - status: 200
    url: https://github.com/eur-nl
  - status: 0
    url: https://datarepository.eur.nl/
  - status: 202
    url: https://eur.figshare.com/
  reason: no_public_api
  state: gated
created: '2026-06-03'
description: 'Erasmus University Rotterdam (EUR) is a Dutch public research university founded in 1913, ranked #158 in the QS World University Rankings 2025, with ROR https://ror.org/057w15z03 and the registrable domain eur.nl. Re-profiled on 2026-08-30 under the API Evangelist university pipeline, which settles WHO OPERATES a surface before crediting it to the institution. The June 2026 profile credited EUR with eleven API entries and ten OpenAPI contracts. Every one of them was api.figshare.com/v2 — one Figshare document that the same pass attributed to twenty-five different universities, split by tag into ten apparent surfaces titled "Figshare altmetric Articles API", "Figshare altmetric Authors API" and so on, and it put EUR fifth in the whole 248-institution university cohort. Those contracts, and the twenty Postman and OpenCollection files, four JSON Schemas, three JSON Structures, four payload examples, the JSON-LD context, the vocabulary, the OAuth scopes, the authentication summary,
  the agentic-access classification, the two Spectral rulesets and the capability map derived from them, have all been removed — 51 files. The attribution was wrong twice over: EUR''s Figshare tenancy ENDED on 30 October 2025, when the EUR Data Repository moved to DataverseNL hosted by DANS, and datarepository.eur.nl now has no DNS record at all. What is left is what EUR actually operates. The genuine institution-run surface is the RePub OAI-PMH 2.0 endpoint at repub.eur.nl/oai — keyless, live, correctly configured with an OpenAIRE and an NWO set and three metadata formats, on the university library''s own infrastructure with @ubib.eur.nl administrative contacts and no vendor CNAME in the chain. Beside it sits api.eur.nl, a Kong API gateway EUR runs on its own address space that answers 401 with WWW-Authenticate: Basic realm="kong" and publishes no route, no reference and no contract to the public internet. EUR holds its own DataCite membership (symbol DHCM, 3,722 DOIs minted) and publishes
  a live RFC 9116 security.txt. Everything else programmable is a tenancy that is a real institutional fact but somebody else''s engineering: the EUR Research Repository on Elsevier Pure at pure.eur.nl, the EUR Data Repository on DataverseNL, the course catalogue on Caci''s OSIRIS, the Canvas LMS with a live LTI 1.3 keyset, and the SURFconext/eduGAIN identity provider that is a Microsoft Entra tenant behind SURF''s proxy. EUR publishes no OpenAPI of its own, no developer portal, no open data portal and no llms.txt.'
finops:
- name: Erasmus University Rotterdam Finops
  service_category: Education
  slug: erasmus-university-rotterdam-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/erasmus-university-rotterdam.png
layout: provider
modified: '2026-08-30'
name: Erasmus University Rotterdam
nav: Providers
network: true
overview: 'Erasmus University Rotterdam publishes 1 API on the [APIs.io](https://apis.io/) network: RePub OAI-PMH Metadata Harvesting Interface. Tagged areas include University, Higher Education, Education, Netherlands, and Rotterdam.


  Erasmus University Rotterdam''s developer surface includes authentication, code examples, status page, GitHub presence, documentation, and 22 more developer resources.'
plans:
- name: Erasmus University Rotterdam Plans Pricing
  plan_count: 2
  slug: erasmus-university-rotterdam-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 1
  name: Erasmus University Rotterdam Rate Limits
  slug: erasmus-university-rotterdam-rate-limits
score:
  band: developing
  composite: 47.3
  coverage:
    artifact_dirs: 11
    catalog_gap: 59.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 59.8
    developer_ergonomics: 21.4
    discoverability: 79.6
    governance: 18.2
    operational_transparency: 26.3
  previous_composite: 47.3
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
    score: 57.4
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/erasmus-university-rotterdam/refs/heads/main/screenshots/erasmus-university-rotterdam-2026-06-20T180813.png
security:
- kind: authentication
  name: Erasmus University Rotterdam Authentication
  slug: erasmus-university-rotterdam-authentication
  summary_line: none/http_basic/oauth2/saml2 · 5 schemes
- kind: domain-security
  name: Erasmus University Rotterdam Domain Security
  slug: erasmus-university-rotterdam-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Erasmus University Rotterdam Vulnerability Disclosure
  slug: erasmus-university-rotterdam-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: erasmus-university-rotterdam
tags:
- University
- Higher Education
- Education
- Netherlands
- Rotterdam
- Research
- Research Data
- Open Access
- Repository
- OAI-PMH
- Identity Federation
- Course Catalog
- Learning Management
website: https://www.eur.nl/en
---
