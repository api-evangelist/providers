---
access_model:
  confidence: high
  label: Free · No self-service signup
  onboarding: unknown
  pricing: free
  public: true
  source:
  - authentication
  - openapi
  - probed
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 30
  human_in_the_loop: 4
  name: Uc Davis Agentic Access
  operation_count: 81
  slug: uc-davis-agentic-access
  summary_line: 81 operations · 30 acting · 4 human-in-the-loop
api_count: 5
apis:
- description: UC Davis operates its own SAML 2.0 identity provider and publishes signed federation metadata as entityID urn:mace:incommon:ucdavis.edu. This is machine-readable, institution-operated by definition, a
  name: UC Davis Shibboleth Identity Provider (SAML 2.0 / InCommon)
  slug: shibboleth-idp
- description: UC Davis Health runs a live HL7 FHIR R4 endpoint on its own domain at emrrp.ucdmc.ucdavis.edu, registered in Epic's public endpoint directory as 'UC Davis' and 'UC Davis - MMC' (active since 2024-11-0
  name: UC Davis Health FHIR R4 endpoint
  slug: health-fhir-r4
- description: 'Information and Educational Technology (IET) Middleware Web Service APIs provide campus integration and identity-related middleware. Probed 2026-08-19: the endpoint returns HTTP 200 but the body is a '
  name: IET Middleware Web Service APIs
  slug: iet-middleware
- description: UC Davis Health Systems Integration offers Epic (EHR), HL7 FHIR and custom SOAP/REST APIs, authenticated with API keys, OAuth2 or Epic Interconnect and fronted by InterSystems API Manager. There is no
  name: UC Davis Health Systems Integration APIs
  slug: health-integration
- description: 'The CAES Computing Resources Unit documents an ACE API supporting college administrative and content workflows. Probed 2026-08-19: the documentation page returns HTTP 200, but no ACE host resolves (ac'
  name: CAES ACE API
  slug: ace
- baseURL: https://peaks.ucdavis.edu
  baseurl_source: declared
  description: The Access resource of PEAKS (People, Equipment, Access, Keys, Space), the asset- and access-tracking application the UC Davis College of Agricultural and Environmental Sciences Computing Resources Un
  name: PEAKS (CAES) — Access API
  slug: uc-davis-access-api
- baseURL: https://peaks.ucdavis.edu
  baseurl_source: declared
  description: The Documents resource of PEAKS (People, Equipment, Access, Keys, Space), the asset- and access-tracking application the UC Davis College of Agricultural and Environmental Sciences Computing Resources
  name: PEAKS (CAES) — Documents API
  slug: uc-davis-documents-api
- baseURL: https://peaks.ucdavis.edu
  baseurl_source: declared
  description: The Equipment resource of PEAKS (People, Equipment, Access, Keys, Space), the asset- and access-tracking application the UC Davis College of Agricultural and Environmental Sciences Computing Resources
  name: PEAKS (CAES) — Equipment API
  slug: uc-davis-equipment-api
- baseURL: https://peaks.ucdavis.edu
  baseurl_source: declared
  description: The Keys resource of PEAKS (People, Equipment, Access, Keys, Space), the asset- and access-tracking application the UC Davis College of Agricultural and Environmental Sciences Computing Resources Unit
  name: PEAKS (CAES) — Keys API
  slug: uc-davis-keys-api
- baseURL: https://peaks.ucdavis.edu
  baseurl_source: declared
  description: The KeySerials resource of PEAKS (People, Equipment, Access, Keys, Space), the asset- and access-tracking application the UC Davis College of Agricultural and Environmental Sciences Computing Resource
  name: PEAKS (CAES) — KeySerials API
  slug: uc-davis-keyserials-api
- baseURL: https://peaks.ucdavis.edu
  baseurl_source: declared
  description: The People resource of PEAKS (People, Equipment, Access, Keys, Space), the asset- and access-tracking application the UC Davis College of Agricultural and Environmental Sciences Computing Resources Un
  name: PEAKS (CAES) — People API
  slug: uc-davis-people-api
- baseURL: https://peaks.ucdavis.edu
  baseurl_source: declared
  description: The PeopleAdmin resource of PEAKS (People, Equipment, Access, Keys, Space), the asset- and access-tracking application the UC Davis College of Agricultural and Environmental Sciences Computing Resourc
  name: PEAKS (CAES) — PeopleAdmin API
  slug: uc-davis-peopleadmin-api
- baseURL: https://peaks.ucdavis.edu
  baseurl_source: declared
  description: The Spaces resource of PEAKS (People, Equipment, Access, Keys, Space), the asset- and access-tracking application the UC Davis College of Agricultural and Environmental Sciences Computing Resources Un
  name: PEAKS (CAES) — Spaces API
  slug: uc-davis-spaces-api
- baseURL: https://peaks.ucdavis.edu
  baseurl_source: declared
  description: The Workstations resource of PEAKS (People, Equipment, Access, Keys, Space), the asset- and access-tracking application the UC Davis College of Agricultural and Environmental Sciences Computing Resour
  name: PEAKS (CAES) — Workstations API
  slug: uc-davis-workstations-api
- description: UC Davis's open-access scholarly output is deposited into eScholarship, the University of California's shared repository, under the campus unit path /uc/ucd. The content, the deposits and the DOIs are
  name: eScholarship — UC Davis unit (tenant)
  slug: escholarship-tenant
- description: 'Library discovery at search.library.ucdavis.edu is an Ex Libris Primo instance. The subdomain is UC Davis''s and the collection is UC Davis''s, but the application is Ex Libris''s: the served document is'
  name: UC Davis Library discovery — Ex Libris Primo (tenant)
  slug: library-primo-tenant
- baseURL: https://experts.ucdavis.edu/api
  baseurl_source: declared
  description: The collection API from University of California, Davis — 2 operation(s) for collection.
  name: University of California, Davis Collection API
  slug: uc-davis-collection-api
- baseURL: https://experts.ucdavis.edu/api
  baseurl_source: declared
  description: Expert Information
  name: University of California, Davis Expert API
  slug: uc-davis-expert-api
- baseURL: https://experts.ucdavis.edu/api
  baseurl_source: declared
  description: The item API from University of California, Davis — 1 operation(s) for item.
  name: University of California, Davis Item API
  slug: uc-davis-item-api
- baseURL: https://experts.ucdavis.edu/api
  baseurl_source: declared
  description: The page search API from University of California, Davis — 1 operation(s) for page search.
  name: University of California, Davis page search API
  slug: uc-davis-page-search-api
artifact_total: 53
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: PEAKS API v1 Access API
  slug: open-uc-davis-access-api
- collection_type: open
  name: PEAKS API v1 Access Documents API
  slug: open-uc-davis-documents-api
- collection_type: open
  name: PEAKS API v1 Access Equipment API
  slug: open-uc-davis-equipment-api
- collection_type: open
  name: PEAKS API v1 Access Keys API
  slug: open-uc-davis-keys-api
- collection_type: open
  name: PEAKS API v1 Access KeySerials API
  slug: open-uc-davis-keyserials-api
- collection_type: open
  name: PEAKS API v1 Access People API
  slug: open-uc-davis-people-api
- collection_type: open
  name: PEAKS API v1 Access PeopleAdmin API
  slug: open-uc-davis-peopleadmin-api
- collection_type: open
  name: PEAKS API v1 Access Spaces API
  slug: open-uc-davis-spaces-api
- collection_type: open
  name: PEAKS API v1 Access Workstations API
  slug: open-uc-davis-workstations-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/uc-davis-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://www.ucdavis.edu/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.ucdavis.edu/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ucdavis
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ucd-library
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/uc-davis/
- group: operate
  title: ''
  type: Status
  url: https://status.ucdavis.edu/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ucdavis.edu/help/privacy-accessibility
- group: operate
  title: ''
  type: Support
  url: https://www.ucdavis.edu/help
- group: other
  title: ''
  type: IdentityFederation
  url: https://shibboleth.ucdavis.edu/idp/shibboleth
- group: other
  title: ''
  type: IdentityFederation
  url: identity/uc-davis-identity-federation.yml
- group: learn
  title: ''
  type: CourseCatalog
  url: https://catalog.ucdavis.edu/
- group: other
  title: ''
  type: ResearchRepository
  url: https://escholarship.org/oai?verb=Identify
- group: build
  title: ''
  type: LibraryCatalog
  url: https://search.library.ucdavis.edu/
- group: other
  title: ''
  type: OpenData
  url: https://aggiedata.ucdavis.edu/
- group: other
  title: ''
  type: ResearchComputing
  url: https://hpc.ucdavis.edu/
- group: docs
  title: ''
  type: Documentation
  url: https://library.ucdavis.edu/online-strategy/
- group: docs
  title: ''
  type: APIReference
  url: https://experts.ucdavis.edu/api/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://experts.ucdavis.edu/termsofuse
- group: design
  title: ''
  type: Conformance
  url: conformance/uc-davis-domain-standards.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/uc-davis-lifecycle.yml
- group: auth
  title: ''
  type: Scopes
  url: scopes/uc-davis-scopes.yml
- group: design
  title: ''
  type: Errors
  url: errors/uc-davis-errors.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/uc-davis-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/uc-davis-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/uc-davis-authentication.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/uc-davis-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/uc-davis-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/uc-davis-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
coverage:
  detail: 'Three genuinely institution-authored contracts were found, fetched and verified callable, so this is not a thin profile. It is a GATED one. Everything UC Davis operates is either open with no registration path at all (Aggie Experts, DAMS — no securitySchemes, no plans, no rate-limit headers) or closed behind institutional affiliation with no public onboarding (PEAKS API keys, IET middleware, UC Davis Health integration). Separately, a cluster of campus surfaces that certainly exist sits behind a Cloudflare bot challenge and returned 403 to every user agent tried, including a current desktop browser string: the AggieData open data portal, the registrar''s course search, research computing, and the campus IT AI pages. Those 403s are a limit on this measurement, not a finding about UC Davis — they are live hosts we could not read. eScholarship and ucdavis.figshare.com answer automated clients with an AWS WAF challenge (HTTP 202, zero bytes); the eScholarship tenant relationship was
    confirmed instead through its OAI-PMH verbs, and no Figshare tenant was claimed because none could be verified. No campus-wide developer portal, changelog, deprecation policy, pricing or rate-limit documentation exists to find.'
  evidence:
  - note: Aggie Experts OpenAPI 3.0.0 v5.0 — institution-authored
    status: 200
    url: https://experts.ucdavis.edu/api/
  - note: callable anonymously, 196 results
    status: 200
    url: https://experts.ucdavis.edu/api/expert/browse?p=A&size=3
  - note: 1,625 hits
    status: 200
    url: https://experts.ucdavis.edu/api/search/?q=genomics&size=1
  - note: DAMS OpenAPI 3.0.0 — institution-authored
    status: 200
    url: https://digital.ucdavis.edu/api/
  - note: 'soft-200: body is an Elasticsearch error with a stack trace'
    status: 200
    url: https://digital.ucdavis.edu/api/collection
  - note: PEAKS API v1, 214KB
    status: 200
    url: https://peaks.ucdavis.edu/swagger/v1/swagger.json
  - note: SAML 2.0 IdP metadata
    status: 200
    url: https://shibboleth.ucdavis.edu/idp/shibboleth
  - note: signed InCommon entity
    status: 200
    url: https://mdq.incommon.org/entities/urn%3Amace%3Aincommon%3Aucdavis.edu
  - note: FHIR R4 CapabilityStatement — Epic-authored, not claimed
    status: 200
    url: https://emrrp.ucdmc.ucdavis.edu/FHIR/api/FHIR/R4/metadata
  - status: 200
    url: https://emrrp.ucdmc.ucdavis.edu/FHIR/api/FHIR/R4/.well-known/smart-configuration
  - note: CDL-operated; tenant relationship only
    status: 200
    url: https://escholarship.org/oai?verb=Identify
  - note: AWS WAF challenge, zero bytes — landing page unreadable
    status: 202
    url: https://escholarship.org/uc/ucd
  - note: Ex Libris Primo — tenant
    status: 200
    url: https://search.library.ucdavis.edu/
  - note: Cloudflare bot challenge — LIVE, unreadable by us
    status: 403
    url: https://aggiedata.ucdavis.edu/
  - note: Cloudflare bot challenge
    status: 403
    url: https://registrar-apps.ucdavis.edu/courses/search/index.cfm
  - note: Cloudflare bot challenge
    status: 403
    url: https://hpc.ucdavis.edu/
  - note: Cloudflare bot challenge — no AIPolicy pointer emitted because none could be verified
    status: 403
    url: https://it.ucdavis.edu/artificial-intelligence/
  - note: General Catalog, HTML only, no machine-readable course feed found
    status: 200
    url: https://catalog.ucdavis.edu/
  - note: 1KB HTML welcome page, no contract
    status: 200
    url: https://iet-ws.ucdavis.edu/api/
  - note: AWS WAF challenge; no Figshare tenant claimed without evidence
    status: 202
    url: https://ucdavis.figshare.com/
  - status: 404
    url: https://www.ucdavis.edu/llms.txt
  - status: 404
    url: https://www.ucdavis.edu/.well-known/security.txt
  - note: the @context the PRODUCTION Aggie Experts API emits does not resolve
    status: 0
    url: https://stage.experts.library.ucdavis.edu/api/schema/context.jsonld
  - note: no institution-operated OAI-PMH
    status: 404
    url: https://digital.ucdavis.edu/oai?verb=Identify
  - note: host resolves (18.144.178.99) but serves nothing
    status: 404
    url: https://api.ucdavis.edu/
  reason: partial_bot_block_and_no_self_service
  state: gated
created: '2026-06-03'
description: 'The University of California, Davis is a public land-grant research university in Davis, California and a member of the ten-campus University of California system. Its programmable footprint is real but decentralized: there is no campus-wide developer portal, no API gateway, no published deprecation policy and no self-service signup for anything. What UC Davis genuinely operates and authored itself is three things — the Aggie Experts API (UC Davis Library, OpenAPI 3.0.0 v5.0, twelve operations over experts, works and grants, callable anonymously and returning JSON-LD with ORCID iDs and UC Davis ARK identifiers), the DAMS API behind digital.ucdavis.edu (built on the Library''s own open-source ''fin'' framework, though several documented operations return soft-200 errors), and the PEAKS asset- and access-tracking API run by the College of Agricultural and Environmental Sciences (MIT-licensed, source at github.com/ucdavis/Peaks, API-key gated). Alongside those it runs a SAML 2.0
  Shibboleth identity provider published to InCommon as urn:mace:incommon:ucdavis.edu, and UC Davis Health operates a live FHIR R4 endpoint on its own domain — although that endpoint''s CapabilityStatement is Epic''s work, not UC Davis''s, and is deliberately not claimed here. Two further surfaces are TENANT relationships and are labelled as such rather than credited as UC Davis engineering: scholarly output in eScholarship (operated by the California Digital Library for all of UC) and library discovery on Ex Libris Primo. Several campus surfaces that plainly exist — the open data portal aggiedata.ucdavis.edu, the registrar''s course search, research computing at hpc.ucdavis.edu — sit behind a Cloudflare bot challenge and could not be read; that is a limit on this profile, not evidence of absence.'
examples:
- key_count: 7
  name: Uc Davis Aggie Experts Browse Example
  slug: uc-davis-aggie-experts-browse-example
- key_count: 7
  name: Uc Davis Aggie Experts Work Browse Example
  slug: uc-davis-aggie-experts-work-browse-example
- key_count: 5
  name: Uc Davis Equipment Create Example
  slug: uc-davis-equipment-create-example
- key_count: 5
  name: Uc Davis Keys List Example
  slug: uc-davis-keys-list-example
finops:
- name: Uc Davis Finops
  service_category: Education
  slug: uc-davis-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/uc-davis.png
json_schemas:
- name: UC Davis Aggie Experts — Expert
  property_count: 10
  slug: uc-davis-aggie-experts-expert
- name: UC Davis Aggie Experts — Grant
  property_count: 2
  slug: uc-davis-aggie-experts-grant
- name: UC Davis Aggie Experts — Work
  property_count: 2
  slug: uc-davis-aggie-experts-work
- name: PEAKS Equipment
  property_count: 15
  slug: uc-davis-equipment
- name: PEAKS Key
  property_count: 8
  slug: uc-davis-key
- name: PEAKS Person
  property_count: 14
  slug: uc-davis-person
- name: PEAKS Space
  property_count: 18
  slug: uc-davis-space
json_structures:
- name: Uc Davis Equipment Structure
  property_count: 15
  slug: uc-davis-equipment-structure
- name: Uc Davis Key Structure
  property_count: 8
  slug: uc-davis-key-structure
jsonld:
- class_count: 33
  name: Uc Davis Context
  property_count: 1
  slug: uc-davis-context
layout: provider
modified: '2026-08-19'
name: University of California, Davis
nav: Providers
network: true
overview: 'University of California, Davis publishes 13 APIs on the [APIs.io](https://apis.io/) network, including PEAKS (CAES) — Access API, PEAKS (CAES) — Documents API, PEAKS (CAES) — Equipment API, and 10 more. Tagged areas include University, Higher Education, Education, United States, and California.


  The University of California, Davis catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  University of California, Davis'' developer surface includes status page, support, documentation, API reference, authentication, and 25 more developer resources.'
plans:
- name: Uc Davis Plans Pricing
  plan_count: 2
  slug: uc-davis-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 1
  name: Uc Davis Rate Limits
  slug: uc-davis-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: University of California, Davis API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: uc-davis-jsonschema-spectral-rules
- effective_rule_count: 6
  extends: []
  name: University of California, Davis API Rules
  rule_count: 6
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 4
  slug: uc-davis-rules
scopes:
- name: Uc Davis Scopes
  scope_count: 0
  slug: uc-davis-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 48.0
  coverage:
    artifact_dirs: 21
    catalog_gap: 57.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 63.2
    commercial_clarity: 63.2
    contract_governance: 9.8
    contract_quality: 49.7
    developer_ergonomics: 40.5
    discoverability: 50.0
    governance: 9.8
    operational_transparency: 23.7
  previous_composite: 48.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 13
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 64.8
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/uc-davis/refs/heads/main/screenshots/uc-davis-2026-06-20T195938.png
security:
- kind: authentication
  name: Uc Davis Authentication
  slug: uc-davis-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Uc Davis Domain Security
  slug: uc-davis-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: uc-davis
tags:
- University
- Higher Education
- Education
- United States
- California
- UC System
- Public Research University
- Research
- Research Data
- Identity Federation
- Digital Collections
- Library
- Health
- Open-Source
website: https://www.ucdavis.edu/
---
