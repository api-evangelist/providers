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
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.2
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Parambil's API provides programmatic access to its AI-powered medical record review platform.
  name: Parambil API
  slug: parambil-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: Compliance
  url: https://www.parambil.com/security
- group: agent
  href: https://artifacts.apis.io/parambil-com/well-known/parambil-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/parambil-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/parambil-com/hosts/parambil-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/parambil-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/parambil-com/vendors/parambil-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/parambil-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.parambil.com/legal/terms-of-use
- group: auth
  title: ''
  type: Security
  url: https://www.parambil.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.parambil.com/legal/privacy-policy
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.parambil.com/
- group: auth
  href: https://artifacts.apis.io/parambil-com/security/parambil-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/parambil-com-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/parambil-com/security/parambil-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/parambil-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://parambil.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.parambil.com/resources
coverage:
  checked: '2026-10-29'
  detail: Developer portal at https://dev.parambil.com/ redirects to a login page, preventing access to API reference without a customer account.
  evidence:
  - status: 200
    url: https://dev.parambil.com/
  reason: customer-only-docs
  state: gated
created: '2026-10-29'
description: Parambil provides AI-powered medical record review software that accelerates and improves accuracy in mass tort and complex litigation workflows. The platform generates comprehensive chronologies, case validations, and analytic insights, reviewing over 5 million records with 44% higher data correctness and 95% faster processing than traditional methods. Trusted by plaintiff and defense firms, Parambil’s solution helps legal teams streamline evidence analysis and reduce costs.
image: https://cdn.prod.website-files.com/6866833531fb0fe0a1a34dd7/688556b580fdbf02fafb2143_Parambil%20-%20Opengaph.jpg
layout: provider
modified: '2026-10-29'
name: Parambil
nav: Providers
network: true
overview: 'Parambil is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AI, Healthcare, Litigation, MedicalRecords, and SaaS.


  Parambil''s developer surface includes documentation and 11 more developer resources.'
random_paper: 4
rate_limits:
- limit_count: 0
  name: Parambil Com Rate Limits
  slug: parambil-com-rate-limits
scopes:
- name: Parambil Com Scopes
  scope_count: 0
  slug: parambil-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 21.1
  coverage:
    artifact_dirs: 18
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 57.1
    operational_transparency: 10.5
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 30.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Parambil Com Authentication
  slug: parambil-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Parambil Com Domain Security
  slug: parambil-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Parambil Com Trust Center
  slug: parambil-com-trust-center
  summary_line: SOC 2, HIPAA
slug: parambil-com
tags:
- AI
- Healthcare
- Litigation
- MedicalRecords
- SaaS
website: https://parambil.com/
---
