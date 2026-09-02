---
access_model:
  confidence: high
  label: Free, but closed to the public — a UMPASS account is required for a key
  onboarding: unknown
  pricing: free
  public: false
  source:
  - https://data.um.edu.mo/quickstart
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
    error_semantics: documented
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
  score: 25.9
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Sixteen JSON APIs, nineteen operations, all GET, covering About UM (organizational units in Chinese, English and Portuguese; public holidays), Academic (course catalog and per-semester course offering
  name: UM Data and Open Data API Platform
  slug: open-data-api
- description: UMPASS, the university's single sign-on, is served by UM's own AD FS farm. It publishes federation metadata as application/samlmetadata+xml — 71 KB, signed, carrying both an IDPSSODescriptor and an SP
  name: UM Web SSO — institutional SAML 2.0 / OpenID Connect identity provider
  slug: websso-idp
- description: 'The identity broker in front of UM''s own IdP. Sign-in to data.um.edu.mo, UMMoodle and the GenAI chat starts at a Microsoft sign-in page and is redirected to websso.um.edu.mo, so the Entra tenant is a '
  name: Microsoft Entra ID tenant federation for um.edu.mo
  slug: entra-federation
- description: The University of Macau's Moodle learning management system publishes a live LTI 1.3 Advantage platform key set at /mod/lti/certs.php (200, application/json, RSA RS256 signing key), an OAuth 2.0 clien
  name: UMMoodle — LTI 1.3 Advantage platform
  slug: ummoodle-lti
- description: The University of Macau Library's catalog and discovery layer is an Ex Libris Primo VE tenancy. UM's institution code is 853UOM_INST and its view is umlibrary. No UM-operated library API exists; any P
  name: UM Library discovery — Ex Libris Primo VE tenancy
  slug: primo-discovery
- description: '澳門大學學者庫, the University of Macau''s institutional repository and scholar profile system, indexing faculties and institutes, scholars, publications and subjects. It is not harvestable: /oai and /oai/req'
  name: UM Scholars Hub — institutional repository
  slug: scholars-hub
- description: The university's own generative-AI chat service for staff and students, an Open WebUI deployment authenticated by OIDC against UMPASS, with self-signup and the local login form disabled. Its unauthent
  name: UM GENAI Chat — Open WebUI deployment
  slug: genai-chat
- description: The University of Macau is Crossref member 53643, with DOI prefix 10.64219 and 21 DOIs registered as of 2026-09-01. This is a fact about the institution and one of the education regime's named standar
  name: Crossref membership — University of Macau
  slug: crossref-member
- description: Research Organization Registry identifier for the University of Macau, carrying its English, Portuguese and historical names (Universidade de Macau, University of East Asia) and its cross-references t
  name: ROR identifier — University of Macau
  slug: ror
artifact_total: 17
common:
- group: company
  title: ''
  type: Website
  url: https://www.um.edu.mo/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://data.um.edu.mo/
- group: other
  title: ''
  type: OpenData
  url: https://data.um.edu.mo/dataset
- group: docs
  title: ''
  type: Documentation
  url: https://data.um.edu.mo/api-documents/api-operations
- group: docs
  title: ''
  type: APIReference
  url: https://data.um.edu.mo/data-dictionary
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/university-of-macau-open-data-api-openapi.yml
- group: learn
  title: ''
  type: CourseCatalog
  url: https://data.um.edu.mo/data-dictionary
- group: other
  title: ''
  type: IdentityFederation
  url: https://websso.um.edu.mo/FederationMetadata/2007-06/FederationMetadata.xml
- group: other
  title: ''
  type: ResearchRepository
  url: https://repository.um.edu.mo/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://umlibrary.primo.exlibrisgroup.com/discovery/search?vid=853UOM_INST:umlibrary
- group: other
  title: ''
  type: AIPolicy
  url: https://genai.um.edu.mo/
- group: build
  title: ''
  type: AITooling
  url: https://chat.genai.um.edu.mo/
- group: auth
  title: ''
  type: Authentication
  url: authentication/university-of-macau-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/university-of-macau-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/university-of-macau-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/university-of-macau-lifecycle.yml
- group: start
  title: ''
  type: SignUp
  url: https://data.um.edu.mo/quickstart
- group: commercial
  title: ''
  type: TermsOfService
  url: https://data.um.edu.mo/terms-and-conditions-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.um.edu.mo/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://data.um.edu.mo/contact-us
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/universityofmacau/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-macau-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-macau-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-macau-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-macau-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
coverage:
  detail: 'The University of Macau operates a genuine institution-owned API platform and documents it unusually well, but no part of it can be called without a UMPASS account, which is issued only to UM staff and students. Every one of the sixteen APIs on api.data.um.edu.mo answers an unauthenticated request with 401 and an Azure API Management key challenge; the single published product, "UM Members", cannot be subscribed to from outside the institution. The surface itself is fully readable — the developer portal''s own backend at /developer/apis?api-version=2022-04-01-preview is anonymously readable and yielded the complete API list, every operation, and every documented query parameter, which is how the OpenAPI in this repository was reconstructed — so this is coverage limited by credentials, not by obscurity. UM publishes no OpenAPI of its own (the portal''s export returns paths: {}), no llms.txt, no apis.json, no /.well-known/api-catalog and no security.txt. Two further institution-operated
    machine-readable surfaces are fully open and are recorded here: the SAML 2.0 federation metadata and OIDC discovery for UM''s own AD FS identity provider, and the LTI 1.3 key set on UMMoodle. What UM does not have is a research-output surface — no OAI-PMH provider exists on any um.edu.mo host, the institutional repository blocks harvesting by IP, and there is no DataCite account. No official University of Macau GitHub organization exists; github.com/university-of-macau and github.com/umacau are both empty registrations with zero public repositories and no profile, and neither is claimed here.'
  evidence:
  - status: 401
    url: https://api.data.um.edu.mo/service/media/events/all
  - status: 200
    url: https://data.um.edu.mo/developer/apis?api-version=2022-04-01-preview
  - status: 200
    url: https://data.um.edu.mo/
  - status: 200
    url: https://data.um.edu.mo/api-documents/api-operations
  - status: 200
    url: https://data.um.edu.mo/quickstart
  - status: 200
    url: https://data.um.edu.mo/dataset
  - status: 200
    url: https://data.um.edu.mo/data-dictionary
  - status: 200
    url: https://websso.um.edu.mo/FederationMetadata/2007-06/FederationMetadata.xml
  - status: 200
    url: https://websso.um.edu.mo/adfs/.well-known/openid-configuration
  - status: 200
    url: https://login.microsoftonline.com/um.edu.mo/v2.0/.well-known/openid-configuration
  - status: 200
    url: https://ummoodle.um.edu.mo/mod/lti/certs.php
  - status: 404
    url: https://repository.um.edu.mo/oai?verb=Identify
  - note: 200 body reads "Your IP is not allowed to access or harvest this resources!"
    status: 200
    url: https://repository.um.edu.mo/api/core/sites
  - status: 200
    url: https://umlibrary.primo.exlibrisgroup.com/discovery/search?vid=853UOM_INST:umlibrary
  - status: 200
    url: https://chat.genai.um.edu.mo/api/config
  - status: 200
    url: https://genai.um.edu.mo/
  - status: 200
    url: https://api.crossref.org/members/53643
  - status: 200
    url: https://ror.org/01r4q9n85
  - note: empty data array — no DataCite account
    status: 200
    url: https://api.datacite.org/clients?query=Macau
  - status: 404
    url: https://data.um.edu.mo/llms.txt
  - status: 404
    url: https://data.um.edu.mo/.well-known/api-catalog
  - status: 404
    url: https://www.um.edu.mo/.well-known/security.txt
  reason: auth_required
  state: gated
created: '2026-06-03'
description: 'The University of Macau (UM), founded in 1981, is the public comprehensive research university of the Macao Special Administrative Region, teaching mainly in English with a largely international faculty and a residential-college undergraduate model. Its programmable footprint is real but narrow, and it is almost entirely campus operations rather than research output. The Information and Communication Technology Office (ICTO) operates a Data and Open Data API Platform at data.um.edu.mo whose gateway, api.data.um.edu.mo, serves sixteen JSON APIs across nineteen operations: organizational units and public holidays, the course catalog and per-semester course offerings, car park availability, computer room PC status and reservations, shuttle bus arrival times, sports facilities and their bookings, door access control records, outdoor WiFi access logs, university news and events, residential college hostel bed spaces and student job vacancies. The platform documents pagination, filtering,
  sorting and a full response-code table with remediation guidance — better documentation discipline than most universities manage. It publishes no OpenAPI, however, and it is not callable by the public: every API requires a subscription key issued only to holders of a UMPASS account, which means UM staff and students. Two further institution-run surfaces are machine-readable and were missed by earlier profiling: UM''s own AD FS identity provider at websso.um.edu.mo publishes signed SAML 2.0 metadata and an OpenID Connect discovery document, and its Moodle deployment publishes a live LTI 1.3 Advantage platform key set. Everything else that looks like a UM API belongs to somebody else — library discovery is an Ex Libris Primo VE tenancy, the UM Scholars Hub repository runs third-party institutional-repository software behind an IP allowlist with no OAI-PMH, and the university''s GenAI chat is an Open WebUI deployment with API keys switched off. UM registers DOIs as a Crossref member and is
  identified in ROR; it holds no DataCite account.'
finops:
- name: University Of Macau Finops
  service_category: Education
  slug: university-of-macau-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-macau.png
json_schemas:
- name: University of Macau Data and Open Data API — schemas
  property_count: 0
  slug: university-of-macau-open-data-schemas
jsonld:
- class_count: 21
  name: University Of Macau Context
  property_count: 5
  slug: university-of-macau-context
layout: provider
modified: '2026-09-01'
name: University of Macau
nav: Providers
network: true
overview: 'University of Macau publishes 1 API on the [APIs.io](https://apis.io/) network: UM Data and Open Data API Platform. Tagged areas include University, Higher Education, Education, Public Research University, and Macau.


  The University of Macau catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  University of Macau''s developer surface includes documentation, API reference, authentication, signup flow, support, and 21 more developer resources.'
plans:
- name: University Of Macau Plans Pricing
  plan_count: 1
  slug: university-of-macau-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 2
  name: University Of Macau Rate Limits
  slug: university-of-macau-rate-limits
rules:
- effective_rule_count: 15
  extends: []
  name: University of Macau API Rules
  rule_count: 15
  severity_counts:
    error: 6
    hint: 0
    info: 0
    warn: 9
  slug: university-of-macau-openapi-spectral-rules
score:
  band: strong
  composite: 57.9
  coverage:
    artifact_dirs: 16
    catalog_gap: 46.3
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 28.1
  facets:
    access_clarity: 63.2
    commercial_clarity: 63.2
    contract_governance: 29.5
    contract_quality: 68.2
    developer_ergonomics: 54.8
    discoverability: 59.3
    governance: 29.5
    operational_transparency: 21.1
  previous_composite: 29.8
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 1
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 61.1
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-macau/refs/heads/main/screenshots/university-of-macau-2026-06-20T200211.png
security:
- kind: authentication
  name: University Of Macau Authentication
  slug: university-of-macau-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: University Of Macau Domain Security
  slug: university-of-macau-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: university-of-macau
tags:
- University
- Higher Education
- Education
- Public Research University
- Macau
- China
- Open Data
- Course Catalog
- Campus Life
- Identity Federation
- Research Repository
- Library
website: https://www.um.edu.mo/
---
