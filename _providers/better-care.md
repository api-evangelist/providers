---
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 7.9
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: 'Better Platform''s clinical data repository exposes the openEHR ITS-REST API (EHR, COMPOSITION, DIRECTORY, CONTRIBUTION, TEMPLATE/definition and QUERY/AQL resources) plus Better''s own web-template and '
  name: Better Platform openEHR REST API
  slug: better-platform-openehr-rest-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/better-care-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.better.care/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.better.care/studio/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.better.care/studio/start-here/studio-setup
- group: operate
  title: ''
  type: Support
  url: https://docs.better.care/studio/welcome/resources-and-community
- group: company
  title: ''
  type: Blog
  url: https://www.better.care/category/blog-en/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/better-care
- group: start
  title: ''
  type: SignUp
  url: https://studio.better.care/registration
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.better.care/privacy-cookies/
- group: auth
  title: ''
  type: Compliance
  url: https://www.better.care/certifications/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.better.care/studio/release-notes/release-3-17
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/better-care-changelog.yml
- group: build
  title: ''
  type: Packages
  url: packages/better-care-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/better-care-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/better-care-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/better-care-marketplace-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/better-care-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/better-care-authentication.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/better-care-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.better.care/studio/release-notes/release-3-17
- group: design
  title: ''
  type: Components
  url: components/better-care-components.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/better-care-conventions.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/better-care-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/better-care-rate-limits.yml
created: '2026-09-02'
description: Better (formerly Marand, Ljubljana, Slovenia) is a digital-health vendor whose products are built on openEHR, the open standard for vendor-neutral, computable clinical data. Better Platform is an openEHR-compliant clinical data repository (CDR) and operational data repository that exposes the openEHR ITS-REST API together with AQL (Archetype Query Language) for querying stored compositions. Better Studio is the low-code environment used to build clinical forms, AQL queries, JavaScript views, ETL pipelines and data connectors against that platform; Better Meds is an ePMA for medication management; Better Design System and the Better Marketplace supply reusable widgets, forms and bundles. Better publishes its core openEHR reference libraries — web-template, ehr-common and the openEHR REST conformance test suite — as Apache-2.0 open source on GitHub and Maven Central, but the Better Platform API reference itself is served behind Microsoft Entra single sign-on.
image: https://www.better.care/wp-content/uploads/2024/01/Better-Logo-Blue-Icon.svg
layout: provider
modified: '2026-09-02'
name: Better
nav: Providers
network: true
overview: 'Better publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Healthcare, openEHR, and Electronic Health Records.


  Better''s developer surface includes documentation, getting-started guide, support, engineering blog, signup flow, changelog, authentication, and 17 more developer resources.'
plans:
- name: Better Care Plans Pricing
  plan_count: 0
  slug: better-care-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Better Care Rate Limits
  slug: better-care-rate-limits
score:
  band: emerging
  composite: 21.7
  coverage:
    artifact_dirs: 13
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.1
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 45.2
    discoverability: 66.7
    governance: 18.2
    operational_transparency: 26.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - cee
    - europe
  previous_composite: 29.8
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 21.3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: falling
security:
- kind: authentication
  name: Better Care Authentication
  slug: better-care-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Better Care Domain Security
  slug: better-care-domain-security
  summary_line: TLSv1.3 · DMARC
slug: better-care
tags:
- Company
- Health
- Healthcare
- openEHR
- Electronic Health Records
- Clinical Data
- Interoperability
- HL7 FHIR
- Medication Management
- Digital Health
- Low Code
- AQL
- Slovenia
website: https://www.better.care/
---
