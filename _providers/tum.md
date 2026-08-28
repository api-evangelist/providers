---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: true
  source:
  - probed
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Tum Agentic Access
  operation_count: 19
  slug: tum-agentic-access
  summary_line: 19 operations · 4 acting
api_count: 6
apis:
- description: REST and gRPC backend behind the official TUM Campus App. 19 operations across campus news and alerts, student clubs, cinema listings, canteen and dish ratings, device registration and feedback. The c
  name: TUM Campus App Backend API
  slug: campus-backend
- description: Search and navigation API for TUM rooms, buildings and places — a Rust service over MeiliSearch, fully unauthenticated, documented with an OpenAPI 3 contract served live at https://nav.tum.de/api/open
  name: NavigaTUM
  slug: navigatum
- description: 'OAI-PMH 2.0 harvesting interface over TUM''s institutional repository. Verified verbs Identify, ListMetadataFormats and ListSets all answer 200. Metadata prefixes: oai_dc, epicur and xMetaDissPlus (the'
  name: mediaTUM OAI-PMH Repository Interface
  slug: mediatum-oai-pmh
- description: Machine-readable SAML 2.0 identity provider metadata — an EntityDescriptor with an IDPSSODescriptor supporting urn:oasis:names:tc:SAML:2.0:protocol, registered in DFN-AAI since 2009-05-26 and reachabl
  name: TUM Shibboleth Identity Provider (SAML 2.0 Metadata)
  slug: identity-federation
- description: 'TUM''s student information system of record, running CAMPUSonline. Two machine-readable surfaces were verified live and unauthenticated on 2026-08-19: a hypermedia course catalog REST endpoint at /tumo'
  name: TUMonline (CAMPUSonline) — Course Catalog and Identity
  slug: tumonline
- description: 'Static JSON API for Munich student canteen menus, prices, dish labels and opening hours, regenerated on a schedule and served as flat files from GitHub Pages. Two OpenAPI files below are one contract '
  name: eat-api — Munich Student Canteen Menus
  slug: eat-api
artifact_total: 33
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: eat-api calendar API
  slug: open-tum-calendar-api
- collection_type: open
  name: eat-api calendar feedback API
  slug: open-tum-feedback-api
- collection_type: open
  name: eat-api calendar locations API
  slug: open-tum-locations-api
- collection_type: open
  name: eat-api calendar maps API
  slug: open-tum-maps-api
- collection_type: open
  name: eat-api calendar menu API
  slug: open-tum-menu-api
- collection_type: open
  name: eat-api calendar Openapi.json API
  slug: open-tum-openapi-json-api
- collection_type: open
  name: eat-api calendar static API
  slug: open-tum-static-api
- collection_type: open
  name: eat-api calendar Status API
  slug: open-tum-status-api
common:
- group: company
  title: ''
  type: Website
  url: https://www.tum.de/en/
- group: company
  title: ''
  type: Blog
  url: https://www.tum.de/en/news-and-events/all-news
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/TUM-Dev
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/technische-universitat-munchen/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tum.de/ueber-die-tum/kontakt-und-anfahrt/impressum
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tum.de/en/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://www.it.tum.de/en/
- group: learn
  title: ''
  type: CourseCatalog
  url: https://campus.tum.de/tumonline/ee/ui/ca2/app/desktop/
- group: other
  title: ''
  type: ResearchRepository
  url: https://mediatum.ub.tum.de/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://www.ub.tum.de/en
- group: other
  title: ''
  type: IdentityFederation
  url: https://login.tum.de/idp/shibboleth
- group: other
  title: ''
  type: ResearchComputing
  url: https://www.researchdata.tum.de/
- group: other
  title: ''
  type: AIPolicy
  url: https://www.tum.de/en/news-and-events/all-news/press-releases/details/tum-issues-a-comprehensive-ai-strategy
- group: other
  title: ''
  type: Accessibility
  url: https://www.tum.de/en/spezialseiten/accessibility
- group: design
  title: ''
  type: x-conformance
  url: conformance/tum-education-standards-conformance.yml
- group: auth
  title: ''
  type: x-authentication
  url: authentication/tum-authentication.yml
- group: auth
  title: ''
  type: x-scopes
  url: scopes/tum-scopes.yml
- group: design
  title: ''
  type: x-errors
  url: errors/tum-errors.yml
- group: design
  title: ''
  type: x-lifecycle
  url: lifecycle/tum-lifecycle.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tum-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/tum-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tum-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/tum-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tum-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/tum-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
- group: design
  title: ''
  type: x-vocabulary
  url: vocabulary/tum-vocabulary.yml
- group: design
  title: ''
  type: x-rules
  url: rules/tum-rules.yml
- group: design
  title: ''
  type: x-json-ld
  url: json-ld/tum-context.jsonld
created: '2026-06-03'
description: 'The Technical University of Munich (TUM) is a public technical research university in Munich, Germany, and one of Germany''s eleven Universities of Excellence. Its programmable footprint is real but small, and almost none of it comes from a central IT developer program: TUM operates no public developer portal, publishes no API terms of service, and lists no API on www.tum.de. What it does operate, verified live on 2026-08-19, is four machine-readable surfaces. Two are OpenAPI contracts built and run by Open Source @ TUM e.V. (TUM-Dev), a TUM-affiliated association: the TUM Campus App backend at api.tum.app (19 operations, Swagger 2.0 generated from tumdev/campus_backend.proto, also served over gRPC at api-grpc.tum.app, listed by TUM IT as an official TUM mobile app), and NavigaTUM at nav.tum.de (room, building and campus navigation, taken into productive operation by TUM as the official room finder). The other two are the surfaces a university operates by definition and rarely
  catalogues: a SAML 2.0 / Shibboleth identity provider publishing DFN-AAI-registered metadata at login.tum.de with SIRTFI2 assurance, and an OAI-PMH 2.0 endpoint on mediaTUM, TUM''s own institutional repository, harvestable back to 1959. Everything else is a tenant relationship on someone else''s platform: the student information system TUMonline runs CAMPUSonline on campus.tum.de (live unauthenticated course REST plus a full OIDC discovery document with 108 scopes), the research information system TUMFIS runs Elsevier Pure, and the canteen menu API eat-api is static JSON on GitHub Pages carrying Studierendenwerk data. No open data portal exists: data.tum.de and opendata.tum.de do not resolve.'
examples:
- key_count: 2
  name: Tum Canteen Menu Example
  slug: tum-canteen-menu-example
- key_count: 2
  name: Tum Canteens Enum Example
  slug: tum-canteens-enum-example
- key_count: 2
  name: Tum Search Example
  slug: tum-search-example
finops:
- name: Tum Finops
  service_category: Education
  slug: tum-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tum.png
json_schemas:
- name: eat-api CanteenMenu
  property_count: 6
  slug: tum-canteen-menu
- name: NavigaTUM SearchResponse
  property_count: 2
  slug: tum-search-response
json_structures:
- name: Tum Canteen Menu Structure
  property_count: 3
  slug: tum-canteen-menu-structure
- name: Tum Search Response Structure
  property_count: 2
  slug: tum-search-response-structure
jsonld:
- class_count: 40
  name: Tum Context
  property_count: 0
  slug: tum-context
layout: provider
modified: '2026-08-19'
name: Technical University of Munich
nav: Providers
network: true
overview: 'Technical University of Munich publishes 3 APIs on the [APIs.io](https://apis.io/) network: TUM Campus App Backend API, NavigaTUM, and eat-api — Munich Student Canteen Menus. Tagged areas include University, Higher Education, Education, Germany, and Technical University.


  The Technical University of Munich catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Technical University of Munich''s developer surface includes engineering blog, support, and 27 more developer resources.'
plans:
- name: Tum Plans Pricing
  plan_count: 2
  slug: tum-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 1
  name: Tum Rate Limits
  slug: tum-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Technical University of Munich API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: tum-jsonschema-spectral-rules
- effective_rule_count: 5
  extends: []
  name: Technical University of Munich API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 4
  slug: tum-rules
scopes:
- name: Tum Scopes
  scope_count: 108
  slug: tum-scopes
  summary_line: 108 scopes
score:
  band: thin
  composite: 36.3
  delta: 3.3
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 9.8
    contract_quality: 17.2
    developer_ergonomics: 23.8
    discoverability: 74.1
    governance: 9.8
    operational_transparency: 23.7
  previous_composite: 33.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 8
      marker_coverage: 100.0
      total: 9
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 64.8
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tum/refs/heads/main/screenshots/tum-2026-06-20T195827.png
security:
- kind: authentication
  name: Tum Authentication
  slug: tum-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Tum Domain Security
  slug: tum-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Tum Vulnerability Disclosure
  slug: tum-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: tum
tags:
- University
- Higher Education
- Education
- Germany
- Technical University
- Universities of Excellence
- Campus
- Course Catalog
- Identity Federation
- Research Repository
- Open-Source
- Student Information System
website: https://www.tum.de/en/
---
