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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/csvgateway/refs/heads/main/plans/csvgateway-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/csvgateway-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/csvgateway/refs/heads/main/conformance/csvgateway-conformance.yml
  title: ''
  type: Conformance
  url: conformance/csvgateway-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/csvgateway/refs/heads/main/hosts/csvgateway-hosts.yml
  title: ''
  type: Hosts
  url: hosts/csvgateway-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/csvgateway/refs/heads/main/vendors/csvgateway-vendors.yml
  title: ''
  type: Vendors
  url: vendors/csvgateway-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://csvgateway.app/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://csvgateway.app/privacy
- group: docs
  title: ''
  type: Documentation
  url: https://dev.csvgateway.app/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/csvgateway/refs/heads/main/security/csvgateway-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/csvgateway-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://csvgateway.app/
- group: commercial
  title: ''
  type: Pricing
  url: https://csvgateway.app/pricing
- group: start
  title: ''
  type: SignUp
  url: https://csvgateway.app/register
- group: company
  title: ''
  type: Blog
  url: https://csvgateway.app/blog
- group: operate
  title: ''
  type: Support
  url: https://csvgateway.app/help
coverage:
  checked: '2026-10-16'
  detail: The provider's site returns HTML pages for typical spec URLs (e.g., /openapi.json) without a machine‑readable OpenAPI document.
  evidence:
  - status: 200
    url: https://csvgateway.app/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-16'
description: CSV Gateway provides an instant CSV to REST API generation service. Users upload CSV, Excel, or JSON files and receive production‑ready API endpoints with full CRUD, filtering, authentication, and OpenAPI docs. The platform offers a free forever plan, secure hosting, analytics, and a no‑code interface to modernize data quickly.
image: https://csvgateway.app/csv_gateway_logo_main.png
layout: provider
modified: '2026-10-16'
name: CSV Gateway
nav: Providers
network: true
overview: 'CSV Gateway is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Data Integration, No-Code, API Generation, CSV, and REST.


  CSV Gateway''s developer surface includes documentation, pricing, signup flow, engineering blog, support, and 8 more developer resources.'
plans:
- name: Csvgateway Plans Pricing
  plan_count: 4
  slug: csvgateway-plans-pricing
random_paper: 8
score:
  band: emerging
  composite: 26.1
  coverage:
    artifact_dirs: 7
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Csvgateway Domain Security
  slug: csvgateway-domain-security
  summary_line: TLSv1.3 · DMARC
slug: csvgateway
tags:
- Data Integration
- No-Code
- API Generation
- CSV
- REST
- Software-as-a-Service
website: https://csvgateway.app/
---
