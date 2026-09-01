---
access_model:
  confidence: high
  label: Free · anonymous read on the research repositories, SSO or bearer token elsewhere
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
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.3
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: 'Public REST API of the TU Wien Research Data repository, running InvenioRDM 14.0. Records, communities, affiliations, funders and vocabularies are readable anonymously; /api/names returns 403 without '
  name: TU Wien Research Data REST API
  slug: researchdata-api
- description: OAI-PMH 2.0 harvesting interface for the TU Wien Research Data repository. Verified live on 2026-08-30 with Identify and ListMetadataFormats; serves oai_dc, datacite and oai_datacite.
  name: TU Wien Research Data OAI-PMH
  slug: researchdata-oai
- description: OAI-PMH 2.0 interface for reposiTUm, the open-access institutional repository of TU Wien, implemented on DSpace-CRIS by TU Wien Campus IT. Serves oai_dc and oai_openaire, with an earliest datestamp of
  name: reposiTUm OAI-PMH
  slug: repositum-oai
- description: 'The DSpace 7 REST layer of reposiTUm is deployed but fronted by a crawler filter: /server/api returned 503 and /server/api/core/items returned 416 with the body "please respect nofollow and noindex he'
  name: reposiTUm DSpace REST API
  slug: repositum-rest
- description: REST API of TISS, TU Wien's Information Systems & Services platform — the course catalogue, curricula, org units, people and room data behind tiss.tuwien.ac.at. The edge is reachable anonymously and r
  name: TISS REST API
  slug: tiss-api
- description: TU Wien's own OpenAPI-described contract, and the only one in this repository. FUNDify publishes Austrian funding programmes and calls and lets institutions annotate them for their own researchers, im
  name: FUNDify — RIS Synergy Funding API
  slug: fundify-funding
- description: Keycloak realm TU Wien operates as the identity broker for the Austrian RIS Synergy network, with SAML brokering endpoints for eleven Austrian universities. Its OpenID Connect discovery document is pu
  name: RIS Synergy Identity Broker (OpenID Connect)
  slug: ris-synergy-oidc
- description: 'TU Wien''s institutional identity provider, registered in the Austrian ACOnet/eduID.at federation and interfederated into eduGAIN. Machine-readable SAML 2.0 metadata, re-signed daily by the federation '
  name: TU Wien SAML 2.0 Identity Provider (eduID.at / eduGAIN)
  slug: saml-idp
- description: TU Wien's library discovery layer. Recorded as a tenant relationship, which is a real institutional fact, so that no Ex Libris contract is ever scored as TU Wien engineering. No spec is saved under th
  name: CatalogPlus library discovery (Ex Libris Primo, OBVSG-hosted)
  slug: catalogplus
artifact_total: 19
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/tuwien-csd/fundify/blob/develop/LICENSE
- group: company
  title: ''
  type: Website
  url: https://www.tuwien.at/en/
- group: docs
  title: ''
  type: Documentation
  url: https://researchdata.tuwien.ac.at/tuw/about/api
- group: docs
  title: ''
  type: APIReference
  url: openapi/tu-wien-fundify-api-openapi.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tuwien-csd
- group: other
  title: ''
  type: ResearchRepository
  url: https://researchdata.tuwien.ac.at/
- group: other
  title: ''
  type: ResearchRepository
  url: https://repositum.tuwien.at/
- group: learn
  title: ''
  type: CourseCatalog
  url: https://tiss.tuwien.ac.at/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://catalogplus.tuwien.at/
- group: other
  title: ''
  type: IdentityFederation
  url: https://eduid.at/md/aconet-registered.xml
- group: other
  title: ''
  type: ResearchComputing
  url: https://www.it.tuwien.ac.at/en/services/research/high-performance-computing/datalab
- group: other
  title: ''
  type: AIPolicy
  url: https://www.tuwien.at/en/studies/teaching-at-tu-wien/digitally-supported-teaching/artificial-intelligence-in-education
- group: build
  title: ''
  type: AITooling
  url: https://github.com/TU-Wien-dataLAB
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tuwien.at/fileadmin/Datenschutz/Data_Protection_Declaration_Websites.pdf
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tuwien.at/en/imprint
- group: company
  title: ''
  type: Blog
  url: https://www.tuwien.at/en/tu-wien/news/news-articles
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/tuwien
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/tu-wien-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tu-wien-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tu-wien-authentication.yml
- group: auth
  title: ''
  type: Scopes
  url: scopes/tu-wien-scopes.yml
- group: design
  title: ''
  type: Errors
  url: errors/tu-wien-errors.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/tu-wien-education-standards.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tu-wien-lifecycle.yml
- group: build
  title: ''
  type: Examples
  url: examples/tu-wien-examples.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/tu-wien-fundify-funding.json
- group: design
  title: ''
  type: Rules
  url: rules/tu-wien-spectral.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/tu-wien-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/tu-wien-context.jsonld
- group: commercial
  title: ''
  type: Plans
  url: plans/tu-wien-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tu-wien-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/tu-wien-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'TU Wien (Vienna University of Technology) is Austria''s largest science and technology university, founded in 1815, with more than 30,000 students across eight faculties. It operates no central developer portal, publishes no API key issuance page and offers no unified developer credential, and most of what looks like a TU Wien API is a product it bought rather than built. What it does operate is real and unusually varied for the cohort: a self-hosted InvenioRDM research-data repository whose REST API answers anonymously, two live OAI-PMH endpoints, a DSpace-CRIS institutional repository, the TISS student-information REST API (versioned, structured errors, documentation behind TU Wien SSO), a SAML 2.0 identity provider registered in the ACOnet/eduID.at federation and interfederated into eduGAIN, and — the one genuinely engineered contract — the FUNDify funding API, written and maintained by TU Wien Campus Software Development for the Austrian RIS Synergy network the university
  led. Its library discovery layer is a tenant surface on the OBVSG consortium''s Ex Libris Primo platform, not TU Wien engineering. Conformance is concentrated in research infrastructure: OAI-PMH 2.0, DataCite, ORCID and SAML are all verified live; SCIM, LTI, OneRoster, Ed-Fi, Caliper and QTI are absent.'
finops:
- name: Tu Wien Finops
  service_category: Education
  slug: tu-wien-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tu-wien.png
json_schemas:
- name: FUNDify / RIS Synergy funding objects
  property_count: 0
  slug: tu-wien-fundify-funding
jsonld:
- class_count: 13
  name: Tu Wien Context
  property_count: 7
  slug: tu-wien-context
layout: provider
modified: '2026-08-30'
name: TU Wien
nav: Providers
network: true
overview: 'TU Wien publishes 1 API on the [APIs.io](https://apis.io/) network: FUNDify — RIS Synergy Funding API. Tagged areas include University, Higher Education, Education, Technical University, and Austria.


  The TU Wien catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  TU Wien''s developer surface includes documentation, API reference, engineering blog, authentication, code examples, and 28 more developer resources.'
plans:
- name: Tu Wien Plans Pricing
  plan_count: 2
  slug: tu-wien-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 1
  name: Tu Wien Rate Limits
  slug: tu-wien-rate-limits
rules:
- effective_rule_count: 48
  extends:
  - spectral:oas
  name: TU Wien API Rules
  rule_count: 7
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 4
  slug: tu-wien-spectral
scopes:
- name: Tu Wien Scopes
  scope_count: 0
  slug: tu-wien-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 56.8
  coverage:
    artifact_dirs: 17
    catalog_gap: 25.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 60.6
    contract_quality: 64.6
    developer_ergonomics: 31.0
    discoverability: 68.5
    governance: 60.6
    operational_transparency: 23.7
  previous_composite: 56.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 75.9
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tu-wien/refs/heads/main/screenshots/tu-wien-2026-06-20T195820.png
security:
- kind: authentication
  name: Tu Wien Authentication
  slug: tu-wien-authentication
  summary_line: 7 schemes
- kind: domain-security
  name: Tu Wien Domain Security
  slug: tu-wien-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Tu Wien Vulnerability Disclosure
  slug: tu-wien-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: tu-wien
tags:
- University
- Higher Education
- Education
- Technical University
- Austria
- Europe
- Research Data
- Research Repository
- Open Access
- OAI-PMH
- Identity Federation
- Research Computing
- InvenioRDM
- DataCite
- ORCID
- SAML
- RIS Synergy
website: https://www.tuwien.at/en/
---
