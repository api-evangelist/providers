---
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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 7.4
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Peppyrus Agentic Access
  operation_count: 12
  slug: peppyrus-agentic-access
  summary_line: 12 operations · 3 acting
api_count: 1
apis:
- description: Peppyrus API provides access to Peppol e‑invoicing services via a free and paid plan.
  name: Peppyrus API
  slug: peppyrus-api
artifact_total: 15
common:
- group: design
  href: https://artifacts.apis.io/peppyrus/conformance/peppyrus-conformance.yml
  title: ''
  type: Conformance
  url: conformance/peppyrus-conformance.yml
- group: other
  href: https://artifacts.apis.io/peppyrus/overlays/peppyrus-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/peppyrus-openapi-overlay.yaml
- group: other
  href: https://artifacts.apis.io/peppyrus/hosts/peppyrus-hosts.yml
  title: ''
  type: Hosts
  url: hosts/peppyrus-hosts.yml
- group: start
  title: ''
  type: SignUp
  url: https://customer.peppyrus.be/register?language=en
- group: auth
  href: https://artifacts.apis.io/peppyrus/security/peppyrus-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/peppyrus-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://peppyrus.be/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://peppyrus.be/en
- group: docs
  title: ''
  type: Documentation
  url: https://api.peppyrus.be/v1/openapi.json
- group: docs
  title: ''
  type: APIReference
  url: https://api.peppyrus.be/v1/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://peppyrus.be/en#get-started
- group: operate
  title: ''
  type: Support
  url: https://customer.peppyrus.be/login?language=en
created: '2026-10-27'
description: Peppyrus provides a free Peppol Access Point, enabling businesses to connect to the global e‑invoicing network. It offers both a test environment (https://api.test.peppyrus.be/v1) and a production API (https://api.peppyrus.be/v1) for seamless integration, along with a customer portal for managing invoices and licenses. The service is certified, developer‑friendly, and includes free and paid plans.
json_schemas:
- name: MessageBody
  property_count: 5
  slug: peppyrus-message-body
- name: Message Render
  property_count: 2
  slug: peppyrus-message-render
- name: Message Report
  property_count: 2
  slug: peppyrus-message-report
- name: Message
  property_count: 10
  slug: peppyrus-message
- name: OrganizationInfo
  property_count: 7
  slug: peppyrus-organization-info
- name: Participant
  property_count: 3
  slug: peppyrus-participant
jsonld:
- class_count: 18
  name: Peppyrus Context
  property_count: 54
  slug: peppyrus-context
layout: provider
modified: '2026-10-27'
name: Peppyrus
nav: Providers
network: true
overview: 'Peppyrus publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Peppol, E‑invoicing, API, and Free.


  The Peppyrus catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Peppyrus'' developer surface includes signup flow, documentation, API reference, getting-started guide, support, and 6 more developer resources.'
plans:
- name: Peppyrus Plans Pricing
  plan_count: 0
  slug: peppyrus-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Peppyrus Rate Limits
  slug: peppyrus-rate-limits
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: Peppyrus API Rules
  rule_count: 14
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 1
  slug: peppyrus-rules
scopes:
- name: Peppyrus Scopes
  scope_count: 0
  slug: peppyrus-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 24.2
  coverage:
    artifact_dirs: 25
    catalog_earned: 50.5
    catalog_earned_first_party: 0.0
    catalog_gap: 64.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 13.2
    contract_governance: 18.2
    contract_quality: 14.7
    developer_ergonomics: 42.9
    discoverability: 62.5
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - belgium
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - benelux
    - europe
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: unknown
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Peppyrus Authentication
  slug: peppyrus-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Peppyrus Domain Security
  slug: peppyrus-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: peppyrus
tags:
- Company
- Peppol
- E‑invoicing
- API
- Free
- Developer-friendly
website: https://peppyrus.be/
---
