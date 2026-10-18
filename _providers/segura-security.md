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
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 12.9
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: API documentation is referenced in the company's documentation site but no machine‑readable contract was found.
  name: Segura API
  slug: segura-api
artifact_total: 2
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/segura-security/refs/heads/main/conformance/segura-security-conformance.yml
  title: ''
  type: Conformance
  url: conformance/segura-security-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/segura-security/refs/heads/main/llms/segura-security-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/segura-security-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/segura-security/refs/heads/main/well-known/segura-security-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/segura-security-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/segura-security/refs/heads/main/hosts/segura-security-hosts.yml
  title: ''
  type: Hosts
  url: hosts/segura-security-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/segura-security/refs/heads/main/vendors/segura-security-vendors.yml
  title: ''
  type: Vendors
  url: vendors/segura-security-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://segura.security/company/trust-center
- group: commercial
  title: ''
  type: TermsOfService
  url: https://segura.security/policies-and-terms/terms-of-service
- group: operate
  title: ''
  type: Support
  url: https://support.segura.security/solution_center
- group: auth
  title: ''
  type: Security
  url: https://segura.security/services/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://segura.security/privacy-and-cookie-statement
- group: company
  title: ''
  type: Newsroom
  url: https://segura.security/company/press
- group: company
  title: ''
  type: Blog
  url: https://segura.security/blog
- group: docs
  title: ''
  type: Documentation
  url: https://docs.segura.security/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.senhasegura.io/llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/segura-security/refs/heads/main/security/segura-security-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/segura-security-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.segura.security
coverage:
  checked: '2026-10-05'
  detail: OpenAPI endpoints return empty files with no operations, and no other machine‑readable contract was found.
  evidence:
  - status: 200
    url: https://www.segura.security/openapi.json
  - status: 200
    url: https://segura.security/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-03'
description: Segura provides a comprehensive Identity Security Platform that secures privileged access, endpoint privilege management, multi‑cloud identity security, DevOps secrets management, certificate lifecycle, and remote access. It serves enterprises across industries, offering audit, compliance, and threat detection capabilities, with a focus on reducing risk and simplifying access governance.
image: https://segura.security/openGraphs/og_6.png
layout: provider
modified: '2026-10-03'
name: Segura
nav: Providers
network: true
overview: 'Segura is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Identity, Privileged Access Management, and Cloud.


  Segura''s developer surface includes support, engineering blog, documentation, and 13 more developer resources.'
random_paper: 18
score:
  band: emerging
  composite: 24.0
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 22.1
  facets:
    access_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 73.2
    operational_transparency: 10.5
  previous_composite: 1.9
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Segura Security Domain Security
  slug: segura-security-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: segura-security
tags:
- Company
- Security
- Identity
- Privileged Access Management
- Cloud
website: https://www.segura.security
---
