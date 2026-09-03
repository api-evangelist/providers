---
access_model:
  confidence: high
  label: Free · anonymous read on the repository and metadata surfaces
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
    agent_skills: derived
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
  score: 5.9
  scored_at: '2026-09-02'
api_count: 7
apis:
- description: Public DSpace REST API for "edoc", the open-access institutional repository of the University of Basel, running DSpace-CRIS 7.6.2 (cris-2023.02.06) on the university's own host. The API root reports d
  name: edoc DSpace REST API
  slug: edoc-rest
- description: 'OAI-PMH 2.0 metadata harvesting interface for edoc. Identify reports repositoryName "edoc: Open Access Repository University of Basel", repositoryIdentifier edoc.unibas.ch and adminEmail openaccess@un'
  name: edoc OAI-PMH
  slug: edoc-oai
- description: Basel's SAML 2.0 identity provider, entityID https://aai-logon.unibas.ch/idp/shibboleth, registered in the SWITCHaai federation and exported to eduGAIN. Its metadata declares shibmd:Scope unibas.ch, s
  name: University of Basel SWITCHaai / eduGAIN Identity Provider
  slug: switchaai-idp
- description: OpenID Connect issuer operated by sciCORE, the University of Basel's centre for scientific computing, at https://iam.scicore.unibas.ch/realms/switch-eduid — a Keycloak realm that brokers SWITCH edu-ID
  name: sciCORE OpenID Connect Issuer
  slug: scicore-oidc
- description: LTI launch endpoint on ADAM, the University of Basel's ILIAS learning management system, at https://adam.unibas.ch/lti.php. It answers an unauthenticated GET with the ILIAS LTI error string rather tha
  name: ADAM (ILIAS) LTI launch endpoint
  slug: adam-lti
- description: The REST backend of UNIverse (universe.unibas.ch), the University of Basel's research information system, at https://universe-intern.unibas.ch/api. It is the only OpenAPI contract the university itsel
  name: UNIverse Research Information System API
  slug: universe-research-information
- description: SRU (Search/Retrieve via URL) interface to swisscovery, the Swiss national library discovery platform, scoped to the University of Basel institution zone 41SLSP_UBS. The catalogue records and the inst
  name: swisscovery (SLSP / Ex Libris Alma) SRU — Basel institution zone
  slug: swisscovery-sru
artifact_total: 13
common:
- group: company
  title: ''
  type: Website
  url: https://www.unibas.ch/en
- group: company
  title: ''
  type: Blog
  url: https://www.unibas.ch/en/News-Events/News.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.unibas.ch/en/Legal-notice.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.unibas.ch/en/Legal-notice/Data-Protection.html
- group: operate
  title: ''
  type: Support
  url: https://its.unibas.ch/en/contact/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ITS-Unibas
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/RISE-UNIBAS
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/university-of-basel/
- group: other
  title: ''
  type: ResearchRepository
  url: https://edoc.unibas.ch/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://swisscovery.slsp.ch/discovery/search?vid=41SLSP_UBS:UBS
- group: learn
  title: ''
  type: CourseCatalog
  url: https://vorlesungsverzeichnis.unibas.ch/en/course-directory
- group: other
  title: ''
  type: IdentityFederation
  url: https://metadata.aai.switch.ch/metadata.switchaai.xml
- group: other
  title: ''
  type: ResearchComputing
  url: https://scicore.unibas.ch/
- group: other
  title: ''
  type: AIPolicy
  url: https://www.unibas.ch/en/Studies/Learning-and-Teaching/AI-in-learning-and-teaching.html
- group: auth
  title: ''
  type: Authentication
  url: authentication/university-of-basel-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/university-of-basel-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-basel-domain-security.yml
- group: auth
  title: ''
  type: Security
  url: security/university-of-basel-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/university-of-basel-vulnerability-disclosure.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-basel-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-basel-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-basel-finops.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/university-of-basel-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The University of Basel (Universität Basel) is the oldest university in Switzerland, founded in 1460, and a canton-funded public research university. It operates no developer portal, no self-serve API program and no public product API; every machine-readable surface it runs is scholarly infrastructure, federated identity, or the back end of one of its own administrative systems. Exactly one OpenAPI contract is served under unibas.ch — the REST back end of UNIverse, the research information system, which publishes an OpenAPI 3.1.0 description and a Swagger UI anonymously while enforcing a bearer token on every data path. Beyond it, verified live on the university''s own hosts: "edoc", the open-access institutional repository running DSpace-CRIS 7.6.2, which answers on both a DSpace REST API and an OAI-PMH 2.0 interface carrying eleven metadata formats and an OpenAIRE-CRIS profile; a SWITCHaai / eduGAIN SAML 2.0 identity provider scoped to unibas.ch, alongside thirty-two registered
  service providers under the same domain; an OpenID Connect issuer at the sciCORE scientific computing centre; and an LTI launch endpoint on ADAM, the university''s ILIAS learning platform. Library discovery is a tenancy, not a Basel system — swisscovery is operated by SLSP on Ex Libris Alma, with Basel holding the 41SLSP_UBS institution zone. The DaSCH Service Platform API (api.dasch.swiss), previously catalogued here as Basel''s, is not: DaSCH is a legally independent association hosted at the university, and that contract and its derived artifacts were removed in the 2026-08-30 pass.'
finops:
- name: University Of Basel Finops
  service_category: Education
  slug: university-of-basel-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-basel.png
layout: provider
modified: '2026-08-30'
name: University of Basel
nav: Providers
network: true
overview: 'University of Basel publishes 7 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include University, Higher Education, Education, Switzerland, and Basel.


  University of Basel''s developer surface includes engineering blog, support, authentication, and 22 more developer resources.'
plans:
- name: University Of Basel Plans Pricing
  plan_count: 1
  slug: university-of-basel-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: University Of Basel Rate Limits
  slug: university-of-basel-rate-limits
score:
  band: thin
  composite: 34.4
  coverage:
    artifact_dirs: 11
    catalog_gap: 64.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.7
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 4.4
    developer_ergonomics: 37.5
    discoverability: 74.1
    governance: 18.2
    operational_transparency: 13.2
  previous_composite: 35.1
  provenance:
    conformance: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 57.4
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-basel/refs/heads/main/screenshots/university-of-basel-2026-06-20T200131.png
security:
- kind: authentication
  name: University Of Basel Authentication
  slug: university-of-basel-authentication
  summary_line: none/http_bearer/openid_connect/saml · 6 schemes
- kind: domain-security
  name: University Of Basel Domain Security
  slug: university-of-basel-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: University Of Basel Vulnerability Disclosure
  slug: university-of-basel-vulnerability-disclosure
  summary_line: Intigriti
slug: university-of-basel
tags:
- University
- Higher Education
- Education
- Switzerland
- Basel
- Research Data
- Research Information
- Institutional Repository
- Open Access
- OAI-PMH
- Identity Federation
- Library
- Research Computing
website: https://www.unibas.ch/en
---
