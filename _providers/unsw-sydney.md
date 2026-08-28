---
access_model:
  confidence: high
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  - probed
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    error_semantics: verified
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
  score: 28.8
  scored_at: '2026-08-26'
api_count: 9
apis:
- description: UNSWorks is the UNSW open-access institutional repository, running DSpace 7.0 on UNSW infrastructure and administered by the UNSW Library. The HAL/REST server at /server/api is readable without creden
  name: UNSWorks Repository REST API (DSpace 7.0)
  slug: unsworks-rest
- description: OAI-PMH 2.0 metadata harvesting endpoint for UNSWorks. Fully anonymous. All six verbs were exercised live and answer with a well-formed envelope; twelve metadata formats are offered (oai_dc, qdc, uket
  name: UNSWorks Repository OAI-PMH
  slug: unsworks-oai
- description: UNSW's own SAML 2.0 identity provider — a Shibboleth IdP whose entity metadata is published as a machine-readable XML document at the entityID URL and is carried in the AAF federation aggregate, which
  name: UNSW Shibboleth Identity Provider (AAF / eduGAIN)
  slug: shibboleth-idp
- description: 'The front door to UNSW''s Enterprise API Gateway, built on Microsoft Azure API Management. Cataloguing it is a statement about the gate, not about the APIs behind it: /apis returns 404, there is no sel'
  name: UNSW Enterprise Developer Portal
  slug: developer-portal
- description: 'UNSW''s learning management system, operated for UNSW by Open LMS. It is a live, conformant 1EdTech LTI 1.3 platform: the public keyset at /mod/lti/certs.php serves RS256 JWKs, the authorisation endpoi'
  name: Moodle @ UNSW (TELT) — LTI 1.3 platform
  slug: moodle-lti
- description: 'UNSW Library''s discovery layer runs on Ex Libris Primo VE. This entry records the tenancy so the relationship is visible in the catalogue; no Ex Libris specification is saved under this institution''s '
  name: UNSW Library discovery (Ex Libris Primo VE)
  slug: primo-discovery
- description: A live student-society API exposing UNSW campus buildings and teaching rooms with coordinates, capacity, school and usage type — the campus-life surface class, built by students rather than by the ins
  name: Freerooms API (DevSoc, community)
  slug: freerooms
- description: 'A scraper and public API for UNSW''s timetable site, produced by the UNSW Software Development Society. ARCHIVED BY ITS OWNER ON 2026-04-05 and now read-only. The June 2026 profile of this institution '
  name: UNSW Timetable API (DevSoc, community) — ARCHIVED
  slug: timetable-scraper
- description: 'A public API for fetching degree, specialisation and course information from the UNSW Handbook, published by the UNSW Computer Science and Engineering Society. ARCHIVED BY ITS OWNER ON 2026-04-03 and '
  name: UNSW Handbook API (CSESoc, community) — ARCHIVED
  slug: handbook-api
artifact_total: 20
common:
- group: company
  title: ''
  type: Website
  url: https://www.unsw.edu.au/
- group: docs
  title: ''
  type: Documentation
  url: https://apideveloper.unsw.edu.au/getting-started
- group: start
  title: ''
  type: DeveloperPortal
  url: https://apideveloper.unsw.edu.au/
- group: other
  title: ''
  type: ResearchRepository
  url: https://unsworks.unsw.edu.au/
- group: other
  title: ''
  type: IdentityFederation
  url: https://aaf.unsw.edu.au/idp/shibboleth
- group: other
  title: ''
  type: ResearchComputing
  url: https://docs.restech.unsw.edu.au/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://www.library.unsw.edu.au/
- group: learn
  title: ''
  type: CourseCatalog
  url: https://www.handbook.unsw.edu.au/
- group: other
  title: ''
  type: AIPolicy
  url: https://www.teaching.unsw.edu.au/ai/guidelines
- group: build
  title: ''
  type: AITooling
  url: https://www.unsw.edu.au/myit/emerging-technologies/ai
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/unsw-edu-au
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.unsw.edu.au/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.unsw.edu.au/copyright-disclaimer
- group: operate
  title: ''
  type: Support
  url: https://www.unsw.edu.au/myit
- group: company
  title: ''
  type: Blog
  url: https://www.unsw.edu.au/newsroom
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/unsw/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/unsw-sydney-unsworks-dspace-openapi.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/unsw-sydney-unsworks-oai-pmh-openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/unsw-sydney-unsworks-dspace-schema.json
- group: build
  title: ''
  type: Examples
  url: examples/unsw-sydney-unsworks-dspace-example.json
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/unsw-sydney-unsworks-vocabulary.yml
- group: design
  title: ''
  type: Rules
  url: rules/unsw-sydney-rules.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/unsw-sydney-authentication.yml
- group: auth
  title: ''
  type: Scopes
  url: scopes/unsw-sydney-scopes.yml
- group: design
  title: ''
  type: Errors
  url: errors/unsw-sydney-errors.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/unsw-sydney-education-standards-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/unsw-sydney-lifecycle.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/unsw-sydney-context.jsonld
- group: auth
  title: ''
  type: DomainSecurity
  url: security/unsw-sydney-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/unsw-sydney-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/unsw-sydney-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/unsw-sydney-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
coverage:
  detail: 'UNSW''s one substantial institution-operated API platform — the Enterprise API Gateway behind apideveloper.unsw.edu.au — cannot be read without authorisation, and authorisation is granted only through a manual request process that can require a data sharing agreement or a manager''s approval. The catalogue path returns 404 unauthenticated, no gateway base URL is published anywhere on the portal, and the portal itself states that even authorised consumers cannot exercise APIs from within it. So the count, shape, versioning and lifecycle of UNSW''s enterprise APIs are unknowable from outside, and this profile asserts nothing about them. What could be read was read completely: the UNSWorks DSpace REST API, its OAI-PMH endpoint and the UNSW Shibboleth IdP metadata were all probed live and are fully covered. Nothing here was blocked by bot protection, and the thinness of this profile is a fact about UNSW''s publishing posture, not a gap in the sweep. UNSW operates no open data portal
    (data.unsw.edu.au redirects to an information-governance page), publishes no OpenAPI, no status page, no changelog and no security.txt, and its research-data toolkit sits behind a Microsoft tenant login.'
  evidence:
  - status: 200
    url: https://apideveloper.unsw.edu.au/
  - status: 200
    url: https://apideveloper.unsw.edu.au/getting-started
  - status: 404
    url: https://apideveloper.unsw.edu.au/apis
  - status: 200
    url: https://apideveloper.unsw.edu.au/signin
  - status: 200
    url: https://unsworks.unsw.edu.au/server/api
  - status: 200
    url: https://unsworks.unsw.edu.au/server/api/discover/search/objects?size=1
  - status: 401
    url: https://unsworks.unsw.edu.au/server/api/core/items?size=1
  - status: 200
    url: https://unsworks.unsw.edu.au/oai/request?verb=Identify
  - status: 200
    url: https://unsworks.unsw.edu.au/oai/request?verb=ListMetadataFormats
  - status: 200
    url: https://aaf.unsw.edu.au/idp/shibboleth
  - status: 200
    url: https://md.aaf.edu.au/aaf-metadata.xml
  - status: 200
    url: https://moodle.telt.unsw.edu.au/mod/lti/certs.php
  - status: 200
    url: https://freerooms.devsoc.app/api/buildings
  - status: 502
    url: https://api.unsw.edu.au/
  - note: Redirects to https://www.unsw.edu.au/information-governance — not an open data portal.
    status: 200
    url: https://data.unsw.edu.au/
  - status: 404
    url: https://www.unsw.edu.au/llms.txt
  - status: 404
    url: https://www.unsw.edu.au/.well-known/security.txt
  - note: NXDOMAIN — retired 2021.
    status: 0
    url: https://resdata.unsw.edu.au/
  reason: gated_developer_portal
  state: gated
created: '2026-06-03'
description: 'The University of New South Wales (UNSW Sydney) is a public research university in Sydney, Australia, and a member of the Group of Eight. Like almost every institution, UNSW is a federation of buyers rather than an API producer, and its programmable footprint has to be read that way. The one substantial platform UNSW runs itself — the Enterprise API Gateway and Developer Portal on Microsoft Azure API Management at apideveloper.unsw.edu.au — is completely gated: onboarding is request-based, the API catalogue is invisible before sign-in, no base URL is disclosed, and the portal states outright that consumers cannot exercise APIs in the portal. The surfaces a member of the public can actually read are three, and all three are institution- operated: the UNSWorks institutional repository REST API (DSpace 7.0, anonymous discovery search, authenticated item browse), its OAI-PMH 2.0 harvesting endpoint exposing twelve metadata formats back to 2007, and the UNSW Shibboleth identity
  provider whose SAML 2.0 entity metadata is published under the institution''s own domain and registered in the Australian Access Federation. Everything else is a tenancy on someone else''s platform — an Ex Libris Primo library discovery view, a vendor-hosted Moodle that is a conformant LTI 1.3 platform, a Microsoft Power Apps research-data toolkit — or student-society work on non-institution domains. UNSW publishes no OpenAPI, no open data portal, no status page, no changelog and no API governance ruleset.'
examples:
- key_count: 2
  name: Unsw Sydney Moodle Lti Jwks Example
  slug: unsw-sydney-moodle-lti-jwks-example
- key_count: 5
  name: Unsw Sydney Unsworks Dspace Example
  slug: unsw-sydney-unsworks-dspace-example
finops:
- name: Unsw Sydney Finops
  service_category: Education
  slug: unsw-sydney-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/unsw-sydney.png
json_schemas:
- name: UNSWorks Repository DSpace 7.0 REST payloads
  property_count: 0
  slug: unsw-sydney-unsworks-dspace
jsonld:
- class_count: 19
  name: Unsw Sydney Context
  property_count: 5
  slug: unsw-sydney-context
layout: provider
modified: '2026-08-19'
name: University of New South Wales
nav: Providers
network: true
overview: 'University of New South Wales publishes 2 APIs on the [APIs.io](https://apis.io/) network: UNSWorks Repository REST API (DSpace 7.0) and UNSWorks Repository OAI-PMH. Tagged areas include University, Higher Education, Education, Research, and Australia.


  The University of New South Wales catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  University of New South Wales'' developer surface includes documentation, support, engineering blog, code examples, authentication, and 28 more developer resources.'
plans:
- name: Unsw Sydney Plans Pricing
  plan_count: 2
  slug: unsw-sydney-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 1
  name: Unsw Sydney Rate Limits
  slug: unsw-sydney-rate-limits
rules:
- effective_rule_count: 0
  extends: []
  name: University of New South Wales API Rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: unsw-sydney-rules
scopes:
- name: Unsw Sydney Scopes
  scope_count: 0
  slug: unsw-sydney-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 53.4
  delta: 2.7
  facets:
    access_clarity: 63.2
    commercial_clarity: 63.2
    contract_governance: 15.2
    contract_quality: 64.6
    developer_ergonomics: 38.1
    discoverability: 64.8
    governance: 15.2
    operational_transparency: 23.7
  previous_composite: 50.7
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 2
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 64.8
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/unsw-sydney/refs/heads/main/screenshots/unsw-sydney-2026-06-20T200413.png
security:
- kind: authentication
  name: Unsw Sydney Authentication
  slug: unsw-sydney-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Unsw Sydney Domain Security
  slug: unsw-sydney-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: unsw-sydney
tags:
- University
- Higher Education
- Education
- Research
- Australia
- Group of Eight
- Sydney
- Research Repository
- Identity Federation
- Course Catalog
- Library
- Open Repository
website: https://www.unsw.edu.au/
---
