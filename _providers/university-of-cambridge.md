---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.9
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: University Of Cambridge Agentic Access
  operation_count: 39
  slug: university-of-cambridge-agentic-access
  summary_line: 39 operations
api_count: 1
apis:
- description: The University's central web authentication service. Raven OAuth2 conforms to OpenID Connect; applications register client credentials to authenticate Cambridge users. An identity/SSO interface rather
  name: Raven Authentication (OAuth2 / OpenID Connect)
  slug: raven
- description: UIS API Gateway (ALPHA) publishing read-oriented REST APIs — University Card, University Student (CamSIS-sourced), and University Human Resources (CHRIS-sourced). Interactive "try this API" docs on th
  name: Cambridge API Gateway (Card / Student / HR)
  slug: gateway
- description: Cambridge's open-access research repository (Apollo) on the DSpace platform, exposing OAI-PMH metadata harvesting and a DSpace REST API. Managed by Cambridge University Library Open Research Systems.
  name: Apollo Institutional Repository API (DSpace)
  slug: apollo
- description: 'Methods for querying and manipulating groups. #### The fetch parameter for groups All methods that return groups also accept an optional `fetch` parameter that may be used to request additional inform'
  name: University of Cambridge group API
  slug: university-of-cambridge-group-api
- description: Common methods for searching for objects in the Lookup/Ibis database.
  name: University of Cambridge ibis API
  slug: university-of-cambridge-ibis-api
- description: 'Methods for querying and manipulating institutions. #### The fetch parameter for institutions All methods that return institutions also accept an optional `fetch` parameter that may be used to request'
  name: University of Cambridge institution API
  slug: university-of-cambridge-institution-api
- description: 'Methods for querying and manipulating people. #### Notes on the fetch parameter All methods that return people, institutions or groups also accept an optional `fetch` parameter that may be used to req'
  name: University of Cambridge person API
  slug: university-of-cambridge-person-api
- description: The University's Shibboleth identity provider, publishing signed SAML 2.0 IdP metadata at https://shib.raven.cam.ac.uk/shibboleth. The EntityDescriptor carries entityID https://shib.raven.cam.ac.uk/sh
  name: Cambridge Shibboleth Identity Provider (SAML 2.0 metadata)
  slug: shibboleth-idp
- description: OAI-PMH 2.0 harvesting interface for Apollo, the University's institutional repository, served from Cambridge's own host. Identify returns repositoryName "Apollo - University of Cambridge Repository",
  name: Apollo OAI-PMH metadata harvesting endpoint
  slug: apollo-oai-pmh
- description: The Cambridge University Library digital collections platform exposes IIIF Presentation API 2.1 manifests at cudl.lib.cam.ac.uk/iiif/<item-id> and IIIF Image API 2.1 endpoints at images.lib.cam.ac.uk/
  name: Cambridge Digital Library IIIF APIs
  slug: cudl-iiif
- description: Cambridge's library discovery layer runs on Ex Libris Primo VE. idiscover.lib.cam.ac.uk is a CNAME to cam.primo.exlibrisgroup.com -> eu00.primo.exlibrisgroup.com, and the landing URL redirects to /dis
  name: iDiscover library discovery (Ex Libris Primo VE) — TENANT
  slug: idiscover-primo
- description: 'Cambridge''s current research information system (CRIS) is Symplectic Elements, reached at elements.admin.cam.ac.uk. The host sits under cam.ac.uk but resolves via CNAME to cam.elements.symplectic.org '
  name: Symplectic Elements research information system — TENANT
  slug: elements-symplectic
artifact_total: 35
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Lookup/Ibis web service group API
  slug: open-university-of-cambridge-group-api
- collection_type: open
  name: Lookup/ web service group ibis API
  slug: open-university-of-cambridge-ibis-api
- collection_type: open
  name: Lookup/Ibis web service group institution API
  slug: open-university-of-cambridge-institution-api
- collection_type: open
  name: Lookup/Ibis web service group person API
  slug: open-university-of-cambridge-person-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/university-of-cambridge-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-cambridge-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/university-of-cambridge-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.cam.ac.uk/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.api.apps.cam.ac.uk/
- group: build
  title: ''
  type: SourceCode
  url: https://gitlab.developers.cam.ac.uk/
- group: company
  title: ''
  type: Twitter
  url: https://x.com/Cambridge_Uni
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/university-of-cambridge/
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-cambridge-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-cambridge-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-cambridge-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
- group: company
  title: ''
  type: Blog
  url: https://www.cam.ac.uk/rss/
- group: docs
  title: ''
  type: Documentation
  url: https://www.lookup.cam.ac.uk/doc/ws-doc/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.api.apps.cam.ac.uk/apis
- group: other
  title: ''
  type: IdentityFederation
  url: https://shib.raven.cam.ac.uk/shibboleth
- group: other
  title: ''
  type: ResearchRepository
  url: https://www.repository.cam.ac.uk/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://www.lib.cam.ac.uk/idiscover
- group: other
  title: ''
  type: ResearchComputing
  url: https://www.hpc.cam.ac.uk/
- group: other
  title: ''
  type: AIPolicy
  url: https://guidebook.devops.uis.cam.ac.uk/standards/genai-policy/
- group: build
  title: ''
  type: AITooling
  url: https://gitlab.developers.cam.ac.uk/uis/devops/ai/agent-skills
- group: learn
  title: ''
  type: CourseCatalog
  url: https://www.undergraduate.study.cam.ac.uk/courses
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cam.ac.uk/about-this-site/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cam.ac.uk/about-this-site/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://help.uis.cam.ac.uk/
- group: design
  title: ''
  type: Conformance
  url: conformance/university-of-cambridge-education-standards.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/university-of-cambridge-gateway-lifecycle.yml
- group: design
  title: ''
  type: Errors
  url: errors/university-of-cambridge-errors.yml
created: '2026-06-03'
description: 'The University of Cambridge (founded 1209) is a public collegiate research university and Russell Group member whose programmable footprint is unusually real for a university, and is operated in-house by University Information Services (UIS) rather than bought in. Verified institution-operated surfaces: the Lookup/Ibis directory web service, which publishes a first-party OpenAPI 3.0 document at www.lookup.cam.ac.uk/openapi-3.0.yaml (39 paths, byte-identical to the copy held here); an API Gateway on the University''s own domain (api.apps.cam.ac.uk) whose developer portal lists ten published APIs — Lookup, University Card, University Photo, University Student, University Human Resources, OAuth2, Raven device statistics, Institutional identifier mapping, Undergraduate Admissions and Staff On Costs — fronted by a live OpenID Connect discovery document; a Shibboleth SAML 2.0 identity provider publishing signed IdP metadata; the Apollo institutional repository, self-hosted DSpace
  8.1 on Cambridge IP space with a DSpace REST API and an OAI-PMH endpoint serving eleven metadata formats and minting DataCite DOIs under prefix 10.17863; and the Cambridge Digital Library IIIF Presentation and Image APIs. Honest limits: only the Lookup contract is published as a downloadable machine-readable spec, every gateway API requires registered client credentials before it will answer, and there is no public status page for the API platform. Library discovery (iDiscover, Ex Libris Primo VE) and the research information system (Symplectic Elements) run under Cambridge subdomains but are vendor platforms — they are recorded here as tenant relationships, not as Cambridge contracts.'
examples:
- key_count: 1
  name: University Of Cambridge Group Example
  slug: university-of-cambridge-group-example
- key_count: 1
  name: University Of Cambridge Institution Example
  slug: university-of-cambridge-institution-example
- key_count: 1
  name: University Of Cambridge Person Example
  slug: university-of-cambridge-person-example
finops:
- name: University Of Cambridge Finops
  service_category: Education
  slug: university-of-cambridge-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-cambridge.png
json_schemas:
- name: Group
  property_count: 7
  slug: university-of-cambridge-group
- name: Institution
  property_count: 6
  slug: university-of-cambridge-institution
- name: Person
  property_count: 9
  slug: university-of-cambridge-person
json_structures:
- name: University Of Cambridge Group Structure
  property_count: 6
  slug: university-of-cambridge-group-structure
- name: University Of Cambridge Institution Structure
  property_count: 4
  slug: university-of-cambridge-institution-structure
- name: University Of Cambridge Person Structure
  property_count: 8
  slug: university-of-cambridge-person-structure
jsonld:
- class_count: 22
  name: University Of Cambridge Context
  property_count: 2
  slug: university-of-cambridge-context
layout: provider
modified: '2026-08-19'
name: University of Cambridge
nav: Providers
network: true
overview: 'University of Cambridge publishes 4 APIs on the [APIs.io](https://apis.io/) network, including group API, ibis API, institution API, and 1 more. Tagged areas include Education, Higher Education, University, Research, and United Kingdom.


  The University of Cambridge catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  University of Cambridge''s developer surface includes authentication, engineering blog, documentation, API reference, support, and 23 more developer resources.'
plans:
- name: University Of Cambridge Plans Pricing
  plan_count: 2
  slug: university-of-cambridge-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 1
  name: University Of Cambridge Rate Limits
  slug: university-of-cambridge-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: University of Cambridge API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: university-of-cambridge-jsonschema-spectral-rules
- effective_rule_count: 48
  extends:
  - spectral:oas
  name: University of Cambridge API Rules
  rule_count: 7
  severity_counts:
    error: 3
    hint: 0
    info: 1
    warn: 3
  slug: university-of-cambridge-rules
score:
  band: strong
  composite: 55.2
  coverage:
    artifact_dirs: 19
    catalog_gap: 45.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 63.2
    commercial_clarity: 63.2
    contract_governance: 31.8
    contract_quality: 61.4
    developer_ergonomics: 45.2
    discoverability: 59.3
    governance: 31.8
    operational_transparency: 26.3
  previous_composite: 55.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 61.1
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-cambridge/refs/heads/main/screenshots/university-of-cambridge-2026-06-20T200140.png
security:
- kind: authentication
  name: University Of Cambridge Authentication
  slug: university-of-cambridge-authentication
  summary_line: http/oauth2/openIdConnect/saml · 3 schemes
- kind: domain-security
  name: University Of Cambridge Domain Security
  slug: university-of-cambridge-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: university-of-cambridge
tags:
- Education
- Higher Education
- University
- Research
- United Kingdom
- Russell Group
- Identity
- Identity Federation
- API Gateway
- Developer Portal
- Research Data
- Open Access
- Research Repository
- Library
- Digital Collections
website: https://www.cam.ac.uk/
---
