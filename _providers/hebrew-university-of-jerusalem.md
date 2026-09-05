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
  score: 20.5
  scored_at: '2026-09-04'
api_count: 1
apis:
- baseURL: https://shnaton.huji.ac.il/api
  baseurl_source: declared
  description: The public JSON API behind shnaton.huji.ac.il, the Hebrew University's official course catalog. Faculties, departments, degree programs, specializations, study roadmaps, courses, course groups, timeta
  name: Shnaton Course Catalog API
  slug: shnaton-course-catalog
- description: The university's own SimpleSAMLphp identity provider, publishing a live SAML 2.0 EntityDescriptor (HTTP 200, application/xml, 4,548 bytes) with IDPSSODescriptor, HTTP-Redirect SSO and SLO bindings, em
  name: Hebrew University of Jerusalem SAML 2.0 Identity Provider
  slug: saml-idp
- description: The university's current research information system and research-output portal at cris.huji.ac.il, running on Elsevier Pure. It publishes a working OAI-PMH 2.0 repository at /ws/oai which answered Id
  name: HUJI Research Portal / CRIS (Elsevier Pure tenant)
  slug: cris-pure
- description: Library discovery for the Hebrew University's library system, running on Ex Libris Primo under institution code 972HUJI_INST with named views 972HUJI_V1 (main), HUJI_THESES (theses collection) and HUJ
  name: HUJI Library Discovery (Ex Libris Primo tenant)
  slug: primo-discovery
- description: 'Two Hebrew University units are registered Crossref members with their own member ids: Hebrew University Magnes Press (member 2773) and the Institute of Archaeology, the Hebrew University of Jerusalem'
  name: Crossref member registration
  slug: crossref-members
- description: The institution's ROR identifier, https://ror.org/03qxff017, resolved from the ROR v2 API on 2026-09-01. The canonical machine-readable identifier for the Hebrew University of Jerusalem and the key us
  name: Research Organization Registry (ROR) record
  slug: ror
artifact_total: 16
common:
- group: company
  title: ''
  type: Website
  url: https://en.huji.ac.il/
- group: docs
  title: ''
  type: APIReference
  url: openapi/hebrew-university-of-jerusalem-shnaton-course-catalog-openapi.yml
- group: learn
  title: ''
  type: CourseCatalog
  url: https://shnaton.huji.ac.il/
- group: other
  title: ''
  type: IdentityFederation
  url: identity-federation/hebrew-university-of-jerusalem-identity-federation.yml
- group: other
  title: ''
  type: ResearchRepository
  url: https://cris.huji.ac.il/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://huji.primo.exlibrisgroup.com/discovery/search?vid=972HUJI_INST:972HUJI_V1
- group: build
  title: ''
  type: Library
  url: https://en.libraries.huji.ac.il/
- group: design
  title: ''
  type: Conformance
  url: conformance/hebrew-university-of-jerusalem-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/hebrew-university-of-jerusalem-authentication.yml
- group: auth
  title: ''
  type: Scopes
  url: scopes/hebrew-university-of-jerusalem-scopes.yml
- group: design
  title: ''
  type: Errors
  url: errors/hebrew-university-of-jerusalem-errors.yml
- group: design
  title: ''
  type: Rules
  url: rules/hebrew-university-of-jerusalem-shnaton-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/hebrew-university-of-jerusalem-vocabulary.yml
- group: build
  title: ''
  type: Examples
  url: examples/hebrew-university-of-jerusalem-shnaton-examples.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/hebrew-university-of-jerusalem-shnaton-schemas.json
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/hebrew-university-of-jerusalem-lifecycle.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/hebrew-university-of-jerusalem-context.jsonld
- group: learn
  title: ''
  type: LearningManagementSystem
  url: https://moodle.huji.ac.il/
- group: other
  title: ''
  type: Regulations
  url: https://en.huji.ac.il/regulations
- group: other
  title: ''
  type: Accessibility
  url: https://en.huji.ac.il/en/accessibility-statement
- group: build
  title: ''
  type: GitHub
  url: https://github.com/huji-nlp
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/HUJI-Deep
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/hebrew-university-of-jerusalem/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hebrew-university-of-jerusalem-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/hebrew-university-of-jerusalem-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/hebrew-university-of-jerusalem-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/hebrew-university-of-jerusalem-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The Hebrew University of Jerusalem (HUJI, האוניברסיטה העברית בירושלים) is Israel''s leading research university, founded in 1918 and operating campuses in Jerusalem, Rehovot and Eilat across the humanities, sciences, medicine, agriculture and law. It publishes no developer portal, no API documentation, no API keys and no terms of use for machine access — api.huji.ac.il, developer.huji.ac.il and data.huji.ac.il do not resolve at all. What it does operate, on its own infrastructure and without anyone advertising it, are two genuinely institution-run programmable surfaces. The first is the JSON API behind Shnaton, the official course catalog at shnaton.huji.ac.il: fully public, entirely unauthenticated, bilingual Hebrew/English, covering faculties, degree programs, specializations, courses, timetabled study sessions and syllabi for academic years 2020 through 2027, with a single unauthenticated search call returning the whole 6,355-course catalog in one 14 MB response. The second
  is the university''s own SAML 2.0 identity provider at idp.cc.huji.ac.il, which publishes live machine-readable metadata signed with a certificate the institution issued to itself. Both were confirmed institution-operated by IP ownership rather than hostname — they resolve inside the 128.139.0.0/16 ILAN allocation registered to IUCC and announced by AS378, behind the university''s own load balancers. Beyond those two, the footprint is tenancy: the research portal at cris.huji.ac.il is Elsevier Pure (a CNAME to huji.elsevierpure.com) and its working OAI-PMH endpoint is Pure''s engineering, and library discovery runs on Ex Libris Primo under institution code 972HUJI_INST. Those relationships are recorded here; their vendors'' contracts deliberately are not.'
finops:
- name: Hebrew University Of Jerusalem Finops
  service_category: Education
  slug: hebrew-university-of-jerusalem-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hebrew-university-of-jerusalem.png
json_schemas:
- name: Hebrew University of Jerusalem Shnaton Course Catalog — Schemas
  property_count: 0
  slug: hebrew-university-of-jerusalem-shnaton-schemas
jsonld:
- class_count: 8
  name: Hebrew University Of Jerusalem Context
  property_count: 6
  slug: hebrew-university-of-jerusalem-context
- class_count: 0
  name: Hebrew University Of Jerusalem Shnaton Course Catalog Context
  property_count: 0
  slug: hebrew-university-of-jerusalem-shnaton-course-catalog
layout: provider
modified: '2026-09-01'
name: Hebrew University of Jerusalem
nav: Providers
network: true
overview: 'Hebrew University of Jerusalem publishes 1 API on the [APIs.io](https://apis.io/) network: Shnaton Course Catalog API. Tagged areas include University, Higher Education, Education, Research, and Israel.


  The Hebrew University of Jerusalem catalog on APIs.io includes 2 JSON-LD contexts and 1 Spectral governance ruleset.


  Hebrew University of Jerusalem''s developer surface includes API reference, authentication, code examples, GitHub presence, and 24 more developer resources.'
plans:
- name: Hebrew University Of Jerusalem Plans Pricing
  plan_count: 2
  slug: hebrew-university-of-jerusalem-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 1
  name: Hebrew University Of Jerusalem Rate Limits
  slug: hebrew-university-of-jerusalem-rate-limits
rules:
- effective_rule_count: 49
  extends:
  - spectral:oas
  name: Hebrew University of Jerusalem API Rules
  rule_count: 8
  severity_counts:
    error: 5
    hint: 0
    info: 0
    warn: 3
  slug: hebrew-university-of-jerusalem-shnaton-rules
scopes:
- name: Hebrew University Of Jerusalem Scopes
  scope_count: 0
  slug: hebrew-university-of-jerusalem-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 35.8
  coverage:
    artifact_dirs: 18
    catalog_earned: 86.3
    catalog_earned_first_party: 0.0
    catalog_gap: 28.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 49.2
    contract_quality: 26.7
    developer_ergonomics: 19.0
    discoverability: 68.5
    governance: 49.2
    operational_transparency: 26.3
  previous_composite: 35.8
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 50.0
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hebrew-university-of-jerusalem/refs/heads/main/screenshots/hebrew-university-of-jerusalem-2026-06-20T182715.png
security:
- kind: authentication
  name: Hebrew University Of Jerusalem Authentication
  slug: hebrew-university-of-jerusalem-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Hebrew University Of Jerusalem Domain Security
  slug: hebrew-university-of-jerusalem-domain-security
  summary_line: TLSv1.3 · DMARC
slug: hebrew-university-of-jerusalem
tags:
- University
- Higher Education
- Education
- Research
- Israel
- Jerusalem
- Course Catalog
- Identity Federation
- Research Repository
- Library
- SAML
- OAI-PMH
- Open Access
- Public Research University
website: https://en.huji.ac.il/
---
