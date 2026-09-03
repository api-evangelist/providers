---
access_model:
  confidence: high
  label: Free · key issued on request by the operating unit
  onboarding: unknown
  pricing: free
  public: false
  source:
  - openapi
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.5
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Pennsylvania State University Agentic Access
  operation_count: 6
  slug: pennsylvania-state-university-agentic-access
  summary_line: 6 operations
api_count: 3
apis:
- baseURL: https://metadata.libraries.psu.edu
  baseurl_source: declared
  description: Penn State University Libraries' faculty and research metadata service, built and run in-house with OSVPR and West Arete. Publishes cleaned researcher metadata — publications, grants, presentations, p
  name: Researcher Metadata Database (RMD) API
  slug: rmd
- baseURL: https://scholarsphere.psu.edu/api/v1
  baseurl_source: declared
  description: Penn State's next-generation institutional repository, written by Penn State University Libraries and released under MIT — not a Figshare, Dataverse or DSpace tenancy. The API is described by the Libr
  name: ScholarSphere API
  slug: scholarsphere
- description: An open OAI-PMH 2.0 harvesting endpoint over Penn State's Electronic Theses and Dissertations Archive, served by the Libraries' own etda_explore application on a psu.edu host. Identify reports reposit
  name: ETDA OAI-PMH Provider
  slug: etda-oai-pmh
- description: Penn State operates its own Shibboleth identity provider and registers it in the InCommon federation under entityID urn:mace:incommon:psu.edu. Penn State SERVES ITS OWN SAML metadata at https://as1.fi
  name: Penn State Identity Federation (InCommon / Shibboleth)
  slug: identity-federation
- baseURL: https://apps.opp.psu.edu/fis-api/v1
  baseurl_source: declared
  description: University buildings and their facility attributes. One tag of the Office of Physical Plant's single LionSpaceFIS service; the buildings, campuses, rooms, events and health entries in this file are fi
  name: Pennsylvania State University Buildings API
  slug: pennsylvania-state-university-buildings-api
- baseURL: https://apps.opp.psu.edu/fis-api/v1
  baseurl_source: declared
  description: Penn State campus reference data, from the Office of Physical Plant LionSpaceFIS service.
  name: Pennsylvania State University Campuses API
  slug: pennsylvania-state-university-campuses-api
- baseURL: https://apps.opp.psu.edu/fis-api/v1
  baseurl_source: declared
  description: Change events for buildings and rooms, from the Office of Physical Plant LionSpaceFIS service.
  name: Pennsylvania State University Events API
  slug: pennsylvania-state-university-events-api
- baseURL: https://apps.opp.psu.edu/fis-api/v1
  baseurl_source: declared
  description: Service health and status for the LionSpaceFIS facilities service; returns appVersion and appStatus with a database connectivity check. Unauthenticated and live (appVersion 1.14.0, probed 2026-08-30).
  name: Pennsylvania State University Health API
  slug: pennsylvania-state-university-health-api
- baseURL: https://apps.opp.psu.edu/fis-api/v1
  baseurl_source: declared
  description: Rooms within buildings, from the Office of Physical Plant LionSpaceFIS service.
  name: Pennsylvania State University Rooms API
  slug: pennsylvania-state-university-rooms-api
artifact_total: 36
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: LionSpaceFIS REST Buildings API
  slug: open-pennsylvania-state-university-buildings-api
- collection_type: open
  name: LionSpaceFIS REST Buildings Campuses API
  slug: open-pennsylvania-state-university-campuses-api
- collection_type: open
  name: LionSpaceFIS REST Buildings Events API
  slug: open-pennsylvania-state-university-events-api
- collection_type: open
  name: LionSpaceFIS REST Buildings Health API
  slug: open-pennsylvania-state-university-health-api
- collection_type: open
  name: LionSpaceFIS REST Buildings Rooms API
  slug: open-pennsylvania-state-university-rooms-api
common:
- group: company
  title: ''
  type: Website
  url: https://www.psu.edu/
- group: docs
  title: ''
  type: APIReference
  url: https://metadata.libraries.psu.edu/api_docs
- group: docs
  title: ''
  type: Documentation
  url: https://docs.scholarsphere.psu.edu/
- group: other
  title: ''
  type: ResearchRepository
  url: https://scholarsphere.psu.edu/
- group: other
  title: ''
  type: ResearchRepository
  url: https://etda.libraries.psu.edu/
- group: other
  title: ''
  type: IdentityFederation
  url: https://as1.fim.psu.edu/idp/shibboleth
- group: build
  title: ''
  type: LibraryCatalog
  url: https://libraries.psu.edu/
- group: learn
  title: ''
  type: CourseCatalog
  url: https://bulletins.psu.edu/
- group: other
  title: ''
  type: OpenData
  url: https://www.datacommons.psu.edu/
- group: other
  title: ''
  type: AIPolicy
  url: https://ai.psu.edu/explore/guidelines
- group: build
  title: ''
  type: AITooling
  url: https://ai.psu.edu/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/PennState
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/psu-libraries
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.psu.edu/web-privacy-statement
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/penn-state-university/
- group: design
  title: ''
  type: Conformance
  url: conformance/pennsylvania-state-university-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/pennsylvania-state-university-authentication.yml
- group: design
  title: ''
  type: Errors
  url: errors/pennsylvania-state-university-problem-types.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/pennsylvania-state-university-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/pennsylvania-state-university-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/pennsylvania-state-university-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pennsylvania-state-university-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/pennsylvania-state-university-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/pennsylvania-state-university-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/pennsylvania-state-university-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Pennsylvania State University (Penn State) is a public, land-grant research university with its primary campus at University Park, PA, and is ranked #69 in the QS World University Rankings 2025. Its programmable footprint is real but narrow, and it lives almost entirely in University Libraries rather than in central IT. Penn State publishes two genuine first-party OpenAPI descriptions of services it builds and operates itself: the Researcher Metadata Database (RMD), the authority on faculty and research metadata, and ScholarSphere, its self-built institutional repository — both key-gated, both described in OpenAPI 3.0 by the Libraries team that wrote them. Alongside those it runs an open OAI-PMH 2.0 provider over the Electronic Theses and Dissertations Archive, an unauthenticated facilities API from the Office of Physical Plant (LionSpaceFIS), and its own Shibboleth identity provider registered in InCommon. Penn State also authors open-source identity software, including a
  SCIM 2.0 server implementation. What it no longer has is a central developer portal: docs.developer.psu.edu, which catalogued internal REST services such as PSU ID, Academic Course and Cornerstone behind WebAccess single sign-on, now redirects to sites.psu.edu and has been decommissioned. There is no unified API gateway, no shared credential, and no self-service onboarding — each surface issues its own key out of the unit that operates it.'
examples:
- key_count: 2
  name: Pennsylvania State University Gethealth Example
  slug: pennsylvania-state-university-getHealth-example
- key_count: 2
  name: Pennsylvania State University Listbuildings Example
  slug: pennsylvania-state-university-listBuildings-example
- key_count: 6
  name: Pennsylvania State University Listcampuses Example
  slug: pennsylvania-state-university-listCampuses-example
- key_count: 2
  name: Pennsylvania State University Listrooms Example
  slug: pennsylvania-state-university-listRooms-example
- key_count: 6
  name: Pennsylvania State University Rmd Unauthenticated Example
  slug: pennsylvania-state-university-rmd-unauthenticated-example
- key_count: 6
  name: Pennsylvania State University Scholarsphere Unauthenticated Example
  slug: pennsylvania-state-university-scholarsphere-unauthenticated-example
finops:
- name: Pennsylvania State University Finops
  service_category: Education
  slug: pennsylvania-state-university-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pennsylvania-state-university.png
json_schemas:
- name: Building
  property_count: 21
  slug: pennsylvania-state-university-building
- name: Room
  property_count: 22
  slug: pennsylvania-state-university-room
json_structures:
- name: Pennsylvania State University Building Structure
  property_count: 21
  slug: pennsylvania-state-university-building-structure
- name: Pennsylvania State University Room Structure
  property_count: 22
  slug: pennsylvania-state-university-room-structure
jsonld:
- class_count: 24
  name: Pennsylvania State University Context
  property_count: 0
  slug: pennsylvania-state-university-context
layout: provider
modified: '2026-08-30'
name: Pennsylvania State University
nav: Providers
network: true
overview: 'Pennsylvania State University publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Researcher Metadata Database (RMD) API, ScholarSphere API, Buildings API, and 4 more. Tagged areas include Education, Higher Education, University, Public Research University, and Land Grant.


  The Pennsylvania State University catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Pennsylvania State University''s developer surface includes API reference, documentation, authentication, and 23 more developer resources.'
plans:
- name: Pennsylvania State University Plans Pricing
  plan_count: 2
  slug: pennsylvania-state-university-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 1
  name: Pennsylvania State University Rate Limits
  slug: pennsylvania-state-university-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Pennsylvania State University API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: pennsylvania-state-university-jsonschema-spectral-rules
- effective_rule_count: 46
  extends:
  - spectral:oas
  name: Pennsylvania State University API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 3
  slug: pennsylvania-state-university-rules
score:
  band: developing
  composite: 46.3
  coverage:
    artifact_dirs: 17
    catalog_gap: 45.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 55.3
    commercial_clarity: 55.3
    contract_governance: 18.2
    contract_quality: 37.4
    developer_ergonomics: 35.7
    discoverability: 74.1
    governance: 18.2
    operational_transparency: 7.9
  previous_composite: 46.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 5
      marker_coverage: 100.0
      total: 7
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 81.5
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pennsylvania-state-university/refs/heads/main/screenshots/pennsylvania-state-university-2026-06-20T191542.png
security:
- kind: authentication
  name: Pennsylvania State University Authentication
  slug: pennsylvania-state-university-authentication
  summary_line: apiKey/none/saml · 5 schemes
- kind: domain-security
  name: Pennsylvania State University Domain Security
  slug: pennsylvania-state-university-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Pennsylvania State University Vulnerability Disclosure
  slug: pennsylvania-state-university-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Pennsylvania State University Trust Center
  slug: pennsylvania-state-university-trust-center
  summary_line: PCI DSS, HIPAA, GDPR
slug: pennsylvania-state-university
tags:
- Education
- Higher Education
- University
- Public Research University
- Land Grant
- Big Ten
- Research
- Research Data
- Research Repository
- Open Access
- Identity Federation
- Library
- Facilities
- United States
website: https://www.psu.edu/
---
