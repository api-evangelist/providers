---
access_model:
  confidence: high
  label: Free · Self-serve API key
  onboarding: self-serve
  pricing: free
  public: true
  source:
  - authentication
  - plans
  - rate-limits
  trial: false
  try_now: true
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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.0
  scored_at: '2026-09-01'
api_count: 3
apis:
- description: The HAL+JSON REST API of ANU's self-hosted DSpace 7.6.7 repository, reachable anonymously at /server/api for the root and discovery resources; /server/api/core/items returns 401, so the surface is gen
  name: ANU Open Research DSpace REST API
  slug: openresearch-rest
- description: 'ANU''s institutional identity provider, publishing machine-readable SAML 2.0 metadata at a stable URL. entityID https://idp2.anu.edu.au/idp/shibboleth, shibmd:Scope anu.edu.au, OrganizationDisplayName '
  name: ANU Shibboleth Identity Provider (SAML 2.0 metadata)
  slug: identity-federation
- description: ANU's research information portal and public researcher/output profiles, running on Elsevier Pure. This is a genuine institutional fact and one of the few programmable research surfaces ANU has, so th
  name: ANU Research Portal Plus (Elsevier Pure) — TENANT
  slug: research-portal-pure
- description: OAI-PMH verbs for metadata harvesting.
  name: Australian National University Harvesting API
  slug: anu-harvesting-api
- description: Retrieval of quantum-generated random values.
  name: Australian National University Random Numbers API
  slug: anu-random-numbers-api
artifact_total: 18
common:
- group: company
  title: ''
  type: Website
  url: https://www.anu.edu.au/
- group: docs
  title: ''
  type: APIReference
  url: https://quantumnumbers.anu.edu.au/documentation
- group: docs
  title: ''
  type: Documentation
  url: https://qrng.anu.edu.au/contact/api-documentation/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/AustralianNationalUniversity
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ANUcybernetics
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/the-australian-national-university/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.anu.edu.au/disclaimer
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.anu.edu.au/privacy
- group: other
  title: ''
  type: Copyright
  url: https://www.anu.edu.au/copyright
- group: operate
  title: ''
  type: Support
  url: https://services.anu.edu.au/information-technology
- group: company
  title: ''
  type: Blog
  url: https://www.anu.edu.au/news
- group: other
  title: ''
  type: ResearchRepository
  url: https://openresearch.anu.edu.au/
- group: other
  title: ''
  type: OpenData
  url: https://datacommons.anu.edu.au/DataCommons/
- group: learn
  title: ''
  type: CourseCatalog
  url: https://programsandcourses.anu.edu.au/
- group: other
  title: ''
  type: IdentityFederation
  url: https://idp2.anu.edu.au/idp/shibboleth
- group: other
  title: ''
  type: AIPolicy
  url: https://www.anu.edu.au/privacy/training-and-resources/generative-ai-and-data-governance
- group: build
  title: ''
  type: AITooling
  url: https://libguides.anu.edu.au/generative-ai
- group: other
  title: ''
  type: Policies
  url: https://policies.anu.edu.au/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/anu-quantum-numbers-openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/anu-quantum-numbers-response-schema.json
- group: build
  title: ''
  type: Examples
  url: examples/anu-qrng-legacy-uint8-example.json
- group: design
  title: ''
  type: Rules
  url: rules/anu-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/anu-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/anu-context.jsonld
- group: auth
  title: ''
  type: Authentication
  url: authentication/anu-authentication.yml
- group: auth
  title: ''
  type: Scopes
  url: scopes/anu-scopes.yml
- group: design
  title: ''
  type: Errors
  url: errors/anu-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/anu-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/anu-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/anu-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/anu-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/anu-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/anu-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The Australian National University (ANU) is a public research university in Canberra and a member of the Group of Eight, ranked #27 in the QS World University Rankings order used by this cohort. Like almost every university, ANU is a federation of buyers rather than an API producer: it operates no central developer portal, no institutional API gateway (api.anu.edu.au and developer.anu.edu.au do not resolve), and publishes no OpenAPI for anything. What it does operate is small, real and genuinely its own — the ANU Quantum Numbers (AQN) service serving live quantum random numbers from the ANU Quantum Optics group, a deprecated predecessor endpoint at qrng.anu.edu.au throttled to one request per minute, a self-hosted DSpace 7.6.7 institutional repository exposing a conformant OAI-PMH 2.0 interface across twelve metadata formats plus a HAL+JSON REST API, and a Shibboleth identity provider registered in the Australian Access Federation and interfederated through eduGAIN. ANU is
  a DataCite member in its own right, holding DOI prefix 10.25911 with 25,559 registered DOIs. Its research information portal, by contrast, is an Elsevier Pure tenancy (researchportalplus.anu.edu.au CNAMEs to elsevierpure.com) — ANU''s data on Elsevier''s contract, recorded here as a tenant relationship and deliberately not credited as ANU engineering. Course, timetable and student systems are gated; the widely used ANU timetable tool is student-built by the Computer Science Students'' Association on a non-ANU domain and is not endorsed on ANU''s own timetabling pages.'
examples:
- key_count: 5
  name: Anu Qrng Legacy Uint8 Example
  slug: anu-qrng-legacy-uint8-example
- key_count: 2
  name: Anu Quantum Numbers Forbidden Example
  slug: anu-quantum-numbers-forbidden-example
- key_count: 6
  name: Anu Quantum Numbers Hex16 Example
  slug: anu-quantum-numbers-hex16-example
finops:
- name: Anu Finops
  service_category: Education
  slug: anu-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/anu.png
json_schemas:
- name: ANU Quantum Numbers request parameters
  property_count: 3
  slug: anu-quantum-numbers-request
- name: ANU Quantum Numbers response
  property_count: 5
  slug: anu-quantum-numbers-response
jsonld:
- class_count: 7
  name: Anu Context
  property_count: 7
  slug: anu-context
layout: provider
modified: '2026-08-19'
name: Australian National University
nav: Providers
network: true
overview: 'Australian National University publishes 2 APIs on the [APIs.io](https://apis.io/) network: Harvesting API and Random Numbers API. Tagged areas include University, Higher Education, Education, Research, and Australia.


  The Australian National University catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Australian National University''s developer surface includes API reference, documentation, GitHub presence, support, engineering blog, code examples, authentication, and 27 more developer resources.'
plans:
- name: Anu Plans Pricing
  plan_count: 3
  slug: anu-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 3
  name: Anu Rate Limits
  slug: anu-rate-limits
rules:
- effective_rule_count: 13
  extends: []
  name: Australian National University API Rules
  rule_count: 13
  severity_counts:
    error: 10
    hint: 0
    info: 0
    warn: 3
  slug: anu-rules
scopes:
- name: Anu Scopes
  scope_count: 0
  slug: anu-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 52.4
  coverage:
    artifact_dirs: 17
    catalog_gap: 30.3
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 73.7
    commercial_clarity: 73.7
    contract_governance: 11.4
    contract_quality: 39.6
    developer_ergonomics: 28.6
    discoverability: 74.1
    governance: 11.4
    operational_transparency: 42.1
  previous_composite: 52.4
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 3
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 79.6
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/anu/refs/heads/main/screenshots/anu-2026-06-20T172029.png
security:
- kind: authentication
  name: Anu Authentication
  slug: anu-authentication
  summary_line: apiKey/none/saml2 · 5 schemes
- kind: domain-security
  name: Anu Domain Security
  slug: anu-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: anu
tags:
- University
- Higher Education
- Education
- Research
- Australia
- Group of Eight
- Research Repository
- Identity Federation
- Open Access
- Quantum
- Random Numbers
- OAI-PMH
website: https://www.anu.edu.au/
---
