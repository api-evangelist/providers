---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 17.3
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: API for DaySmart Vet platform as described on the documentation site.
  name: DaySmart Vet API
  slug: daysmart-vet-api
artifact_total: 3
common:
- group: agent
  href: https://artifacts.apis.io/daysmart-vet/llms/daysmart-vet-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/daysmart-vet-llms.txt
- group: auth
  href: https://artifacts.apis.io/daysmart-vet/well-known/daysmart-vet-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/daysmart-vet-status-security.txt
- group: auth
  href: https://artifacts.apis.io/daysmart-vet/well-known/daysmart-vet-security-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/daysmart-vet-security-security.txt
- group: agent
  href: https://artifacts.apis.io/daysmart-vet/well-known/daysmart-vet-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/daysmart-vet-well-known.yml
- group: other
  href: https://artifacts.apis.io/daysmart-vet/hosts/daysmart-vet-hosts.yml
  title: ''
  type: Hosts
  url: hosts/daysmart-vet-hosts.yml
- group: other
  href: https://artifacts.apis.io/daysmart-vet/vendors/daysmart-vet-vendors.yml
  title: ''
  type: Vendors
  url: vendors/daysmart-vet-vendors.yml
- group: build
  href: https://artifacts.apis.io/daysmart-vet/packages/daysmart-vet-packages.yml
  title: ''
  type: SDKs
  url: packages/daysmart-vet-packages.yml
- group: build
  href: https://artifacts.apis.io/daysmart-vet/packages/daysmart-vet-packages.yml
  title: ''
  type: Packages
  url: packages/daysmart-vet-packages.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://security.daysmart.com/trust
- group: operate
  title: ''
  type: StatusPage
  url: https://status.daysmart.com/
- group: start
  title: ''
  type: Login
  url: https://security.daysmart.com/auth/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/DaySmart
- group: auth
  href: https://artifacts.apis.io/daysmart-vet/security/daysmart-vet-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/daysmart-vet-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://daysmart.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.daysmart.com/vet/
- group: docs
  title: ''
  type: APIReference
  url: https://sandbox.vettersoftware.com/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.daysmart.com/vet/demo/
- group: operate
  title: ''
  type: Support
  url: https://www.daysmart.com/vet/contact/
- group: company
  title: ''
  type: Blog
  url: https://www.daysmart.com/vet/resources/category/blogs/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.daysmart.com/vet/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.daysmart.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.daysmart.com/privacy-policy/
coverage:
  checked: '2026-10-28'
  detail: Documentation at https://sandbox.vettersoftware.com/docs/ provides HTML only and no discoverable OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts.
  evidence:
  - status: 200
    url: https://sandbox.vettersoftware.com/docs/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: DaySmart Vet provides cloud-based veterinary practice management software that streamlines scheduling, medical records, billing, client communication, and inventory management. The platform integrates AI tools, supports multi-location clinics, and offers extensive integrations for labs, pharmacies, and payment processors, helping veterinary practices improve efficiency and patient care.
image: https://www.daysmart.com/wp-content/uploads/2026/09/daysmart-homepage-og.png?wsr
layout: provider
modified: '2026-10-28'
name: DaySmart Vet
nav: Providers
network: true
overview: 'DaySmart Vet is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Veterinary, Software, Cloud, and PracticeManagement.


  DaySmart Vet''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, and 16 more developer resources.'
plans:
- name: Daysmart Vet Plans Pricing
  plan_count: 0
  slug: daysmart-vet-plans-pricing
random_paper: 1
score:
  band: thin
  composite: 30.3
  coverage:
    artifact_dirs: 10
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 42.9
    discoverability: 57.1
    operational_transparency: 31.6
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Daysmart Vet Domain Security
  slug: daysmart-vet-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: daysmart-vet
tags:
- Company
- Veterinary
- Software
- Cloud
- PracticeManagement
website: https://daysmart.com/
---
