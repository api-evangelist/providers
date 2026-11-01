---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Integrate Andros' Credentialing API for seamless data exchange. Enhance your healthcare network's efficiency and accuracy.
  name: Credentialing API
  slug: credentialing-api
artifact_total: 4
common:
- group: other
  href: https://artifacts.apis.io/andros/hosts/andros-hosts.yml
  title: ''
  type: Hosts
  url: hosts/andros-hosts.yml
- group: other
  href: https://artifacts.apis.io/andros/vendors/andros-vendors.yml
  title: ''
  type: Vendors
  url: vendors/andros-vendors.yml
- group: auth
  href: https://artifacts.apis.io/andros/security/andros-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/andros-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://andros.co/
- group: company
  title: ''
  type: Blog
  url: https://andros.co/insights/
- group: operate
  title: ''
  type: Support
  url: https://andros.co/contact-us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://andros.co/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://andros.co/privacy-policy/
- group: start
  title: ''
  type: SignUp
  url: https://andros.co/login/
coverage:
  checked: '2026-10-29'
  detail: The provider's documentation page https://andros.co/credentialing-api/ describes the API but no machine‑readable OpenAPI/GraphQL/AsyncAPI spec is published.
  evidence:
  - status: 404
    url: https://andros.co/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Andros provides data-driven, integrated provider network management solutions for healthcare organizations, offering credentialing, recruitment, contracting, and comprehensive data services. With over 200 networks built nationwide, its Andros Arc™ platform enables health plans to optimize network performance, improve care quality, and reduce administrative overhead through precise analytics and automation.
image: https://andros.co/wp-content/uploads/final01_wordpressPreviewImage_1200x675_3-28-2025.png
layout: provider
modified: '2026-10-29'
name: Andros
nav: Providers
network: true
overview: 'Andros is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, ProviderNetwork, Credentialing, and DataManagement.


  Andros'' developer surface includes engineering blog, support, signup flow, and 6 more developer resources.'
random_paper: 23
scopes:
- name: Andros Scopes
  scope_count: 0
  slug: andros-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 15.8
  coverage:
    artifact_dirs: 18
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 24.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Andros Authentication
  slug: andros-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Andros Domain Security
  slug: andros-domain-security
  summary_line: TLSv1.3 · DMARC
slug: andros
tags:
- Company
- Healthcare
- ProviderNetwork
- Credentialing
- DataManagement
website: https://andros.co/
---
