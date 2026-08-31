---
access_model:
  confidence: high
  label: Free and keyless where public; institutional affiliation where not
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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.7
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: 'Keyless, anonymous OAI-PMH 2.0 metadata harvesting for UCD''s open-access institutional repository. Verified live 2026-08-30: all six verbs return HTTP 200 with a well-formed envelope, ListIdentifiers '
  name: Research Repository UCD — OAI-PMH 2.0
  slug: oai-pmh
- description: UCD's SAML 2.0 Shibboleth Identity Provider, and the institution's only authentication surface it runs itself. It is machine-readable by definition — a federated IdP publishes SAML metadata — and is t
  name: University College Dublin Identity Provider (Shibboleth / Edugate / eduGAIN)
  slug: identity-federation
- description: Static, keyless Dublin Core metadata exports for UCD Library's digital cultural-heritage collections — metadata as CSV and JSON, plus facets, subjects and a TimelineJS export, all linked from a publis
  name: UCD Digital Library collection data exports
  slug: digital-library-data
- description: A live DSpace-CRIS 7.6.1 HAL REST API on UCD's branded repository host, advertising roughly ninety link relations including items, collections, communities, discover, authn, oidc, orcidqueues, orcidhi
  name: Research Repository UCD — DSpace-CRIS REST API (4Science)
  slug: dspace-rest
- description: The National Folklore Collection (Cnuasach Bhéaloideas Éireann) is held at UCD; the Dúchas digitisation platform and its API are built and operated by DCU's Gaois research group. THE API IS WITHDRAWN.
  name: Dúchas API — National Folklore Collection (operated by DCU)
  slug: duchas
- description: UCD Library's discovery layer runs on Serials Solutions (Clarivate/ProQuest) under a customer key, not on a UCD host. It exposes a search interface for people, not a documented public API, and no spec
  name: UCD Library discovery (Serials Solutions / Clarivate)
  slug: library-discovery
artifact_total: 12
common:
- group: company
  title: ''
  type: Website
  url: https://www.ucd.ie/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/University-College-Dublin
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/university-college-dublin/
- group: other
  title: ''
  type: ResearchRepository
  url: https://researchrepository.ucd.ie/
- group: other
  title: ''
  type: IdentityFederation
  url: https://technical.edugain.org/entities
- group: other
  title: ''
  type: OpenData
  url: https://digital.ucd.ie/data.html
- group: learn
  title: ''
  type: CourseCatalog
  url: https://hub.ucd.ie/usis/!W_HU_MENU.P_PUBLISH?p_tag=COURSECATALOGUE
- group: build
  title: ''
  type: LibraryCatalog
  url: https://www.ucd.ie/library/
- group: other
  title: ''
  type: ResearchComputing
  url: https://www.ucd.ie/itservices/ourservices/researchit/researchcomputing/
- group: other
  title: ''
  type: AIPolicy
  url: https://www.ucd.ie/registrar/ucdstrategicpoliciesandinitatives/ai-at-ucd/
- group: build
  title: ''
  type: AITooling
  url: https://www.ucd.ie/itservices/ourservices/communicationcollaboration/officeproductivity/aiservices/
- group: docs
  title: ''
  type: Documentation
  url: https://libguides.ucd.ie/RRU/usage
- group: operate
  title: ''
  type: Support
  url: https://www.ucd.ie/itservices/ourservices/researchit/
- group: company
  title: ''
  type: Blog
  url: https://www.ucd.ie/newsandopinion/
- group: other
  title: ''
  type: Research
  url: https://www.ucd.ie/research/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ucd.ie/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ucd.ie/legal/
- group: other
  title: ''
  type: DataProtection
  url: https://www.ucd.ie/gdpr/
- group: other
  title: ''
  type: FreedomOfInformation
  url: https://www.ucd.ie/foi/
- group: design
  title: ''
  type: Conformance
  url: conformance/ucd-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ucd-authentication.yml
- group: design
  title: ''
  type: Errors
  url: errors/ucd-errors.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/ucd-vocabulary.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ucd-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/ucd-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ucd-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/ucd-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
coverage:
  checked: '2026-08-30'
  detail: 'University College Dublin operates no public API programme — no developer portal, no API key issuance, no OAuth authorization server, no first-party OpenAPI, no llms.txt and no security.txt on any ucd.ie host — and this profile now says so. Three institution-operated machine-readable surfaces do exist and are catalogued: the OAI-PMH 2.0 harvesting endpoint of Research Repository UCD (17,167 records, fourteen metadata formats, OpenAIRE CRIS profile), the SAML 2.0 Shibboleth IdP registered in Edugate/eduGAIN, and the UCD Digital Library''s static Dublin Core data exports. None is a hosted API product, and the single OpenAPI in this repository is DERIVED by API Evangelist from live probes of the OAI-PMH endpoint, not published by UCD. What was catalogued here on 2026-06-03 was a different institution''s contract: six per-tag OpenAPIs of the Dúchas API, whose info.contact is "Gaois / Dúchas" <eolas@duchas.ie> and whose operator is the Gaois research group at Dublin City University,
    all registered under UCD''s slug with a fabricated baseURL of https://researchrepository.ucd.ie/oai/request — a path that returns 405 and does not serve those endpoints. Six times the apparent footprint, on a host that does not run the software, for an API its own documentation says "is no longer available" and which returns HTTP 500 on every path. Those six specifications, their twelve collections, and every schema, structure, example, ruleset, vocabulary, JSON-LD context and agentic-access file derived from them — 34 files — were removed on 2026-08-30. Two further June entries described the UCD Digital Library''s IIIF Image, IIIF Presentation, Geospatial and unAPI endpoints; those were decommissioned with the old platform and now 404, and were replaced by the static data-export entry. The remaining machinery under UCD''s name belongs to someone else and is labelled as such: the repository platform is DSpace-CRIS 7.6.1 hosted by 4Science (researchrepository.ucd.ie CNAMEs to ucd7.4science.cloud),
    and library discovery is Serials Solutions under a customer key.'
  evidence:
  - status: 200
    url: https://researchrepository.ucd.ie/server/oai/request?verb=Identify
  - status: 405
    url: https://researchrepository.ucd.ie/oai/request?verb=Identify
  - status: 200
    url: https://researchrepository.ucd.ie/server/api
  - status: 200
    url: https://sso.ucd.ie/idp/shibboleth
  - status: 200
    url: https://technical.edugain.org/api.php?action=list_entities&format=json
  - status: 200
    url: https://digital.ucd.ie/data.html
  - status: 404
    url: https://digital.ucd.ie/help/
  - status: 404
    url: https://digital.ucd.ie/api
  - status: 500
    url: https://www.duchas.ie/api/v0.5/api
  - status: 500
    url: https://www.duchas.ie/api/v0.6/api
  - status: 200
    url: https://docs.gaois.ie/en/data/duchas/v0.6/api
  - status: 0
    url: https://api.ucd.ie/
  - status: 0
    url: https://data.ucd.ie/
  - status: 404
    url: https://www.ucd.ie/llms.txt
  - status: 404
    url: https://www.ucd.ie/.well-known/security.txt
  - note: Bot challenge, not a dead host. The DSpace Angular UI answers scripted clients with a "Human Verification" body on every HTML path; the API and OAI-PMH paths on the same host return 200.
    status: 405
    url: https://researchrepository.ucd.ie/
  - note: Directory listing denied; the individual export files return 200.
    status: 403
    url: https://digital.ucd.ie/assets/data/
  - note: LinkedIn's standard scripted-client block. Live in a browser.
    status: 999
    url: https://www.linkedin.com/school/university-college-dublin/
  reason: no_public_api
  state: none
created: '2026-06-03'
description: 'University College Dublin is Ireland''s largest university, a public research institution in Belfield, Dublin. It operates no API programme: there is no developer portal, no API key issuance, no OAuth authorization server and no first-party OpenAPI anywhere on a ucd.ie host. What it does operate, verified live on 2026-08-30, is three real machine-readable surfaces — an OAI-PMH 2.0 harvesting endpoint for Research Repository UCD (17,167 records, fourteen metadata formats, plus an OpenAIRE CRIS base URL), a SAML 2.0 Shibboleth Identity Provider registered in Edugate/eduGAIN as https://sso.ucd.ie/idp/shibboleth with scope ucd.ie, and static Dublin Core collection data exports from the UCD Digital Library. Everything else is somebody else''s engineering under UCD''s name: the repository platform is DSpace-CRIS hosted by 4Science, library discovery is Serials Solutions, and the Dúchas API for the National Folklore Collection — the collection is UCD''s, the platform is DCU''s — was
  withdrawn by its operator and now returns HTTP 500 on every path. This profile was re-run under the university pipeline on 2026-08-30 and the previously catalogued Dúchas contracts were removed.'
examples:
- key_count: 3
  name: Ucd Digital Library Facets Example
  slug: ucd-digital-library-facets-example
finops:
- name: Ucd Finops
  service_category: Education
  slug: ucd-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ucd.png
layout: provider
modified: '2026-08-30'
name: University College Dublin
nav: Providers
network: true
overview: 'University College Dublin publishes 1 API on the [APIs.io](https://apis.io/) network: Research Repository UCD — OAI-PMH 2.0. Tagged areas include University, Higher Education, Education, Ireland, and Europe.


  University College Dublin''s developer surface includes documentation, support, engineering blog, authentication, and 24 more developer resources.'
plans:
- name: Ucd Plans Pricing
  plan_count: 2
  slug: ucd-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 1
  name: Ucd Rate Limits
  slug: ucd-rate-limits
score:
  band: developing
  composite: 42.5
  coverage:
    artifact_dirs: 12
    catalog_gap: 59.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 4.9
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 15.2
    contract_quality: 52.4
    developer_ergonomics: 28.6
    discoverability: 59.3
    governance: 15.2
    operational_transparency: 23.7
  previous_composite: 37.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 46.3
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ucd/refs/heads/main/screenshots/ucd-2026-08-17T130228.png
security:
- kind: authentication
  name: Ucd Authentication
  slug: ucd-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Ucd Domain Security
  slug: ucd-domain-security
  summary_line: TLSv1.3 · DMARC
slug: ucd
tags:
- University
- Higher Education
- Education
- Ireland
- Europe
- Public Research University
- Research Repository
- Open Access
- OAI-PMH
- Identity Federation
- Cultural Heritage
- Open Data
website: https://www.ucd.ie/
---
