---
access_model:
  confidence: high
  label: Free to TU Dresden affiliates · no public signup
  onboarding: unknown
  pricing: free
  public: false
  source:
  - authentication
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
  scored_at: '2026-09-01'
api_count: 7
apis:
- description: An OpenAI-compatible LLM inference API operated by ZIH and ScaDS.AI Dresden/Leipzig for TU Dresden staff, students and ScaDS.AI affiliates, served from a LiteLLM proxy on the university's own network.
  name: TUD:AI LLM API
  slug: tud-ai-llm
- description: The DSpace 7.6.2 REST API of OPARA, the open-access research-data repository ZIH operates for TU Dresden and three further Saxon institutions. The HAL root at /server/api is served anonymously and lin
  name: OPARA Research Data Repository REST API
  slug: opara-rest
- description: The standards-based harvesting interface for OPARA — how TU Dresden's research data reaches OpenAIRE, BASE, re3data and the rest of the aggregator layer. Identify returns protocolVersion 2.0, earliest
  name: OPARA OAI-PMH Harvesting Interface
  slug: opara-oai
- description: 'The university''s own Shibboleth identity provider, operated by ZIH, and the surface class this pipeline exists to surface: institution-operated by definition, fully machine-readable, and almost never '
  name: TU Dresden Identity Provider (Shibboleth SAML 2.0 + OpenID Connect)
  slug: sso-shibboleth
- description: A gated JSON API over the public data of the TU Dresden lecture directory — courses, seminars, instructors, buildings, semesters, institutes and degree programmes. Access requires an API account reque
  name: TU Dresden Lecture Catalog API (Vorlesungsverzeichnis)
  slug: lecture-catalog
- description: TU Dresden's research information system, a current-research-information-system tenancy on Elsevier Pure, published to the world as the TUD Research Portal at fis.tu-dresden.de. The public portal is f
  name: TU Dresden Research Portal (Elsevier Pure) Web Service
  slug: fis-pure
- description: The OAI-PMH 2.0 harvesting interface for the TU Dresden instance of Qucosa, the Saxon document and publication server used for dissertations, theses and open-access publications. Identify returns prot
  name: Qucosa TU Dresden OAI-PMH (Institutional Document Server)
  slug: qucosa-oai
artifact_total: 13
common:
- group: company
  title: ''
  type: Website
  url: https://tu-dresden.de/
- group: company
  title: ''
  type: Blog
  url: https://tu-dresden.de/tu-dresden/newsportal
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tu-dresden
- group: company
  title: ''
  type: LinkedIn
  url: https://de.linkedin.com/school/tu-dresden/
- group: docs
  title: ''
  type: Documentation
  url: https://llm.scads.ai/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://llm.scads.ai/docs/usage/api/
- group: operate
  title: ''
  type: Status
  url: https://llm.scads.ai/status/
- group: operate
  title: ''
  type: Support
  url: https://tu-dresden.de/zih/dienste/service-desk
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tu-dresden.de/impressum
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tu-dresden.de/datenschutz
- group: other
  title: ''
  type: IdentityFederation
  url: https://met.refeds.org/met/entity/https%3A%2F%2Fidp.tu-dresden.de%2Fidp%2Fshibboleth/
- group: other
  title: ''
  type: ResearchRepository
  url: https://opara.zih.tu-dresden.de/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://katalog.slub-dresden.de/
- group: learn
  title: ''
  type: CourseCatalog
  url: https://vvz.phil.tu-dresden.de/
- group: other
  title: ''
  type: ResearchComputing
  url: https://tu-dresden.de/zih/hochleistungsrechnen
- group: other
  title: ''
  type: AIPolicy
  url: https://tu-dresden.de/tu-dresden/digitalisierung/ki-an-der-tu-dresden
- group: build
  title: ''
  type: AITooling
  url: https://llm.scads.ai/docs/
- group: auth
  title: ''
  type: Authentication
  url: authentication/tu-dresden-authentication.yml
- group: design
  title: ''
  type: Errors
  url: errors/tu-dresden-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/tu-dresden-education-standards.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/tu-dresden-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tu-dresden-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/tu-dresden-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tu-dresden-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/tu-dresden-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
coverage:
  detail: 'TU Dresden operates five surfaces of its own and four of the five require an institutional credential, which is the normal shape for a German university and is a finding about the institution, not about us. Nothing blocked the probe: more than sixty hosts and paths were fetched successfully with a browser User-Agent, every status code below was observed live, and the thinness that remains is real. Verified institution-operated and live: TUD:AI at https://llm.scads.ai/v1/models answers with a LiteLLM auth_error envelope for a missing key and a DIFFERENT envelope naming a key hash for an invalid one, which proves the token is validated rather than merely required; llm.scads.ai resolves to 141.76.18.84 and 141.76.19.193, inside the RIPE allocation 141.76.0.0/16 netname TUDINF-LAN, org "Technische Universitaet Dresden", and keys are issued from https://selfservice.tu-dresden.de/services/scads-llm-api/ with support at llm.scads.ai@tu-dresden.de. OPARA answers anonymously at https://opara.zih.tu-dresden.de/server/api
    with a DSpace 7.6.2 HAL root document and at /server/oai/request with a valid OAI-PMH 2.0 Identify naming adminEmail servicedesk@tu-dresden.de and twelve metadata prefixes. https://idp.tu-dresden.de/idp/shibboleth serves DFN-AAI-registered SAML metadata and /.well-known/openid-configuration plus /idp/profile/oidc/keyset now serve OIDC — correcting the June profile, which recorded OIDC as "planned but not yet available". https://vvz.phil.tu-dresden.de/api?auth_code=test returns "Der Auth-Code ist leider nicht richtig." under a 200. Verified live but tenant-operated: fis.tu-dresden.de is Elsevier Pure (a PureFacade marker in the portal HTML; /ws/api, /ws/oai and /ws/rest all answer 403 while /portal/ws/api answers 404), and https://tud.qucosa.de/oai/?verb=Identify returns an OAI-PMH envelope whose request element names the backend http://sdvcmr-prod-oai01.slub-dresden.de:8080/oai/ and whose adminEmail is qucosa-it@slub-dresden.de, with the DataCite client for it registered as tbyu.ozzulw
    under SLUB''s provider TBYU. Removed as another institution''s: the five SLUB LOD contracts at data.slub-dresden.de — SLUB is a Saxon state library that serves TU Dresden under agreement, it holds its own Crossref membership (26325) and its own DataCite provider symbol (TBYU), and its API is not TU Dresden''s engineering. Not TU Dresden''s either: OPAL at bildungsportal.sachsen.de, the Saxony-wide LMS run by BPS Bildungsportal Sachsen GmbH, and the Mensa API at studentenwerk-dresden.de, run by the student services organisation. Confirmed absent by DNS: data.tu-dresden.de, api.tu-dresden.de, opendata.tu-dresden.de, developer.tu-dresden.de, gitlab.tu-dresden.de, elearning.tu-dresden.de, status.tu-dresden.de, chat.zih.tu-dresden.de and ki.tu-dresden.de all fail to resolve. Confirmed absent by fetch: https://tu-dresden.de/llms.txt 404, https://llm.scads.ai/v1/openapi.json 404, and github.com/tu-dresden holds a single repository. The one contract that is publicly served — https://llm.scads.ai/openapi.json
    — is LiteLLM''s own generic proxy specification, titled "LiteLLM API", and is deliberately not saved here for the same reason the SLUB contracts were removed.'
  evidence:
  - status: 500
    url: https://llm.scads.ai/v1/models
  - status: 200
    url: https://llm.scads.ai/docs/
  - status: 200
    url: https://llm.scads.ai/docs/usage/api/
  - status: 200
    url: https://llm.scads.ai/docs/models/
  - status: 200
    url: https://llm.scads.ai/status/
  - status: 200
    url: https://llm.scads.ai/openapi.json
  - status: 404
    url: https://llm.scads.ai/v1/openapi.json
  - status: 200
    url: https://chat.llm.scads.ai/
  - status: 200
    url: https://selfservice.tu-dresden.de/services/scads-llm-api/
  - status: 200
    url: https://opara.zih.tu-dresden.de/server/api
  - status: 200
    url: https://opara.zih.tu-dresden.de/server/api/core/collections
  - status: 200
    url: https://opara.zih.tu-dresden.de/server/api/discover/search/objects
  - status: 200
    url: https://opara.zih.tu-dresden.de/server/oai/request?verb=Identify
  - status: 200
    url: https://opara.zih.tu-dresden.de/server/oai/request?verb=ListMetadataFormats
  - status: 200
    url: https://opara.zih.tu-dresden.de/server/oai/request?verb=ListSets
  - status: 200
    url: https://opara.zih.tu-dresden.de/server/oai/request?verb=ListRecords&metadataPrefix=oai_dc
  - status: 200
    url: https://idp.tu-dresden.de/idp/shibboleth
  - status: 200
    url: https://idp.tu-dresden.de/.well-known/openid-configuration
  - status: 200
    url: https://idp.tu-dresden.de/idp/profile/oidc/keyset
  - status: 200
    url: https://met.refeds.org/met/entity/https%3A%2F%2Fidp.tu-dresden.de%2Fidp%2Fshibboleth/
  - status: 200
    url: https://vvz.phil.tu-dresden.de/api
  - status: 200
    url: https://vvz.phil.tu-dresden.de/api?auth_code=test
  - status: 200
    url: https://fis.tu-dresden.de/portal/
  - status: 403
    url: https://fis.tu-dresden.de/ws/api
  - status: 403
    url: https://fis.tu-dresden.de/ws/oai?verb=Identify
  - status: 404
    url: https://fis.tu-dresden.de/portal/ws/api
  - status: 200
    url: https://tud.qucosa.de/oai/?verb=Identify
  - status: 200
    url: https://api.datacite.org/providers/kiyb
  - status: 200
    url: https://api.datacite.org/clients/tib.zih
  - status: 200
    url: https://api.datacite.org/dois/10.25532/OPARA-101
  - status: 200
    url: https://api.crossref.org/members?query=dresden
  - status: 200
    url: https://tu-dresden.de/.well-known/security.txt
  - status: 404
    url: https://tu-dresden.de/llms.txt
  - status: 403
    url: https://bildungsportal.sachsen.de/opal/restapi/repo/entries
  - status: 0
    url: https://data.tu-dresden.de/
  - status: 0
    url: https://api.tu-dresden.de/
  - status: 0
    url: https://opendata.tu-dresden.de/
  - status: 0
    url: https://developer.tu-dresden.de/
  - status: 0
    url: https://gitlab.tu-dresden.de/
  reason: auth_required
  state: gated
created: '2026-06-03'
description: 'Technische Universität Dresden (TUD) is a German public technical university in Dresden, Saxony, a member of TU9 and one of the institutions funded under the German Universities Excellence Strategy. Re-profiled on 2026-08-30 under the API Evangelist university pipeline, which settles WHO OPERATES a surface before crediting it to the institution. The June 2026 profile credited TU Dresden with five OpenAPI contracts and five extra apis[] entries; all five were one document — the Linked Open Data API of the Sächsische Landesbibliothek – Staats- und Universitätsbibliothek Dresden (SLUB), a separate Saxon state institution, served from data.slub-dresden.de and split by tag into five apparent surfaces. Worse, every one of those entries carried a baseURL of vvz.phil.tu-dresden.de, a host the specs never mention, which is why a hostname-based audit read them as institution-owned. Those contracts and the twenty-two schema, structure, JSON-LD, vocabulary, ruleset, example, collection
  and agentic-access artifacts derived from them have been removed. What is left is what TU Dresden actually runs, and it is more than the old profile showed. The headline find is TUD:AI at llm.scads.ai/v1 — an OpenAI-compatible LLM inference API operated by ZIH and ScaDS.AI Dresden/Leipzig on TU Dresden''s own network, keyed from the university''s Self-Service Portal, serving nine open-weight chat models plus embedding, audio and image endpoints. Alongside it: OPARA, the DSpace 7.6.2 research-data repository TU Dresden operates for four Saxon institutions, with an open REST API and an OAI-PMH interface; the university''s own Shibboleth identity provider, registered in DFN-AAI and exported to eduGAIN, which now also serves OpenID Connect discovery and a JWKS; and the gated lecture-directory JSON API of the Faculty of Arts. Two surfaces are real institutional facts running on somebody else''s engineering: the Pure-based research information system at fis.tu-dresden.de and the TU Dresden view
  of the SLUB-operated Qucosa document server. TU Dresden publishes no OpenAPI of its own, no developer portal, no open data portal and no llms.txt — but it does publish a security.txt, and it holds its own DataCite membership and DOI prefix.'
finops:
- name: Tu Dresden Finops
  service_category: Education
  slug: tu-dresden-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tu-dresden.png
layout: provider
modified: '2026-08-30'
name: TU Dresden
nav: Providers
network: true
overview: 'TU Dresden publishes 7 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include University, Higher Education, Education, Germany, and Saxony.


  TU Dresden''s developer surface includes engineering blog, documentation, API reference, status page, support, authentication, and 20 more developer resources.'
plans:
- name: Tu Dresden Plans Pricing
  plan_count: 2
  slug: tu-dresden-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 3
  name: Tu Dresden Rate Limits
  slug: tu-dresden-rate-limits
score:
  band: thin
  composite: 37.3
  coverage:
    artifact_dirs: 9
    catalog_gap: 52.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 6.7
    developer_ergonomics: 35.7
    discoverability: 74.1
    governance: 18.2
    operational_transparency: 34.2
  previous_composite: 37.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 57.4
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tu-dresden/refs/heads/main/screenshots/tu-dresden-2026-06-20T195822.png
security:
- kind: authentication
  name: Tu Dresden Authentication
  slug: tu-dresden-authentication
  summary_line: 5 schemes
- kind: domain-security
  name: Tu Dresden Domain Security
  slug: tu-dresden-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Tu Dresden Vulnerability Disclosure
  slug: tu-dresden-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: tu-dresden
tags:
- University
- Higher Education
- Education
- Germany
- Saxony
- TU9
- Research
- Research Data
- Research Computing
- Artificial Intelligence
- Identity Federation
- OAI-PMH
- Institutional Repository
- Open Access
website: https://tu-dresden.de/
---
