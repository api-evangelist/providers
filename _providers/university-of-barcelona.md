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
  scored_at: '2026-09-03'
api_count: 10
apis:
- description: The University of Barcelona's own SAML 2.0 identity provider, published as a signed EntityDescriptor through RedIRIS SIR — the Spanish academic identity federation — and carried into eduGAIN. entityID
  name: UB SAML 2.0 Identity Provider (RedIRIS SIR / eduGAIN)
  slug: ub-idp-edugain
- description: 'UB''s self-hosted Moodle learning platform on the university''s own host. It acts as an LTI 1.3 tool platform: the JWKS at /mod/lti/certs.php serves a live RS256 public key set and the LTI Advantage tok'
  name: Campus Virtual UB (Moodle) — LTI 1.3 Advantage platform and Web Services
  slug: campusvirtual-moodle
- description: Open Journal Systems platform self-hosted by UB at revistes.ub.edu, publishing the university's scholarly journals. Its OAI-PMH 2.0 data provider answers Identify, ListSets and ListMetadataFormats, ad
  name: Revistes Científiques de la UB (OJS) — OAI-PMH 2.0
  slug: revistes-ojs
- description: Universitat de Barcelona centralized single sign-on providing federated authentication for university web applications, on UB's own host. The SAML2 SSOService endpoint is confirmed live (HTTP 200, 202
  name: UB Centralized SSO (Identificació UB, SAML 2.0 / CAS)
  slug: sso-saml
- description: DSpace 7.6.6 REST API for the Dipòsit Digital de la Universitat de Barcelona, UB's institutional repository of teaching, research and institutional output, on UB's own host. The API root advertised HA
  name: Dipòsit Digital REST API (DSpace 7)
  slug: diposit-rest
- description: OAI-PMH metadata-harvesting endpoint for the Dipòsit Digital de la Universitat de Barcelona, used for harvesting into national aggregators and the CRAI discovery layer. The Identify verb returned repo
  name: Dipòsit Digital OAI-PMH
  slug: diposit-oai
- description: UB's named research-data collection on CORA RDR, the Dataverse 6.10.1 instance operated by CSUC (Consorci de Serveis Universitaris de Catalunya) for the Catalan university system. The collection is re
  name: CORA Repositori de Dades de Recerca — Universitat de Barcelona collection
  slug: cora-rdr-ub
- description: The CRAI library discovery layer for UB, delivered on Ex Libris Primo VE under the CSUC shared Alma tenancy. The UB view is 34CSUC_UB:VU1 and it resolves on a ub.edu hostname, but the platform, the co
  name: Cercabib — CRAI library discovery (Ex Libris Primo VE, view 34CSUC_UB)
  slug: cercabib-primo
- description: 'The University of Barcelona press is a Crossref member in its own right: member id 17854, DOI prefixes 10.1344 and 10.32869, 10,561 registered DOIs at probe time. Crossref DOI registration is one of t'
  name: Crossref membership — Edicions de la Universitat de Barcelona (member 17854)
  slug: crossref-member
- description: The University of Barcelona's entry in the Research Organization Registry. ROR id https://ror.org/021018s57, display name "Universitat de Barcelona", country ES, linking to https://web.ub.edu. Resolve
  name: ROR registration — Universitat de Barcelona (021018s57)
  slug: ror-registration
artifact_total: 15
common:
- group: company
  title: ''
  type: Website
  url: https://www.ub.edu/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/university-of-barcelona/
- group: other
  title: ''
  type: IdentityFederation
  url: https://www.rediris.es/sir/ubidp
- group: other
  title: ''
  type: ResearchRepository
  url: https://dataverse.csuc.cat/dataverse/UB
- group: build
  title: ''
  type: LibraryCatalog
  url: https://cercabib.ub.edu/discovery/search?vid=34CSUC_UB:VU1
- group: auth
  title: ''
  type: Authentication
  url: https://sso.ub.edu/SAML2/SSOService.php
- group: design
  title: ''
  type: Conformance
  url: conformance/university-of-barcelona-education-standards.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-barcelona-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-barcelona-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-barcelona-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-barcelona-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/university-of-barcelona-context.jsonld
created: '2026-06-03'
description: 'The University of Barcelona (Universitat de Barcelona, UB) is a public research university founded in 1450 in Barcelona, Catalonia, Spain, ranked #165 in the QS World University Rankings 2025. UB operates no central developer portal, no public API program and no confirmed organization-wide GitHub account, and its main web estate at www.ub.edu sits behind a Cloudflare bot challenge that returns HTTP 403 to any automated client. What it does operate is a genuine, machine-readable institutional footprint that is easy to miss because none of it is marketed as an API: a SAML 2.0 identity provider published through RedIRIS SIR into eduGAIN with the ub.edu attribute scope; an LTI 1.3 Advantage tool platform on its self-hosted Moodle at campusvirtual.ub.edu, with a live JWKS and token endpoint; an OAI-PMH 2.0 data provider over 100 journal sets at revistes.ub.edu; a DSpace 7.6.6 repository at diposit.ub.edu that was live in June 2026 and returned 503 across every probe on 2026-09-01;
  and a Crossref membership for the university press. Its research-data repository and library discovery layer are tenancies on consortium and vendor platforms operated by CSUC and Ex Libris, not UB engineering, and are recorded here as relationships rather than as UB contracts.'
finops:
- name: University Of Barcelona Finops
  service_category: Education
  slug: university-of-barcelona-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-barcelona.png
jsonld:
- class_count: 37
  name: University Of Barcelona Context
  property_count: 12
  slug: university-of-barcelona-context
layout: provider
modified: '2026-09-01'
name: University of Barcelona
nav: Providers
network: true
overview: 'University of Barcelona publishes 10 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include University, Higher Education, Education, Spain, and Catalonia.


  The University of Barcelona catalog on APIs.io includes 1 JSON-LD context.


  University of Barcelona''s developer surface includes authentication and 12 more developer resources.'
plans:
- name: University Of Barcelona Plans Pricing
  plan_count: 2
  slug: university-of-barcelona-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 1
  name: University Of Barcelona Rate Limits
  slug: university-of-barcelona-rate-limits
score:
  band: emerging
  composite: 24.4
  coverage:
    artifact_dirs: 8
    catalog_gap: 50.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 18.0
    developer_ergonomics: 21.4
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 24.4
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 31.5
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
security:
- kind: domain-security
  name: University Of Barcelona Domain Security
  slug: university-of-barcelona-domain-security
  summary_line: TLSv1.2 · DMARC
slug: university-of-barcelona
tags:
- University
- Higher Education
- Education
- Spain
- Catalonia
- Identity Federation
- SAML
- Shibboleth
- eduGAIN
- LTI
- Learning Management
- OAI-PMH
- Repository
- DSpace
- Research Data
- Library
- Scholarly
- Crossref
- Open Access
website: https://www.ub.edu/
---
