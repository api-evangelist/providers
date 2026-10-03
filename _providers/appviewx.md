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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.6
  scored_at: '2026-10-03'
api_count: 1
apis:
- description: API documentation is not publicly machine-readable; attempts to fetch OpenAPI specs returned 404 on both api and docs hosts.
  name: Appviewx API
  slug: appviewx-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: Compliance
  url: https://trust.appviewx.com/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/appviewx/refs/heads/main/well-known/appviewx-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/appviewx-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/appviewx/refs/heads/main/hosts/appviewx-hosts.yml
  title: ''
  type: Hosts
  url: hosts/appviewx-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/appviewx/refs/heads/main/vendors/appviewx-vendors.yml
  title: ''
  type: Vendors
  url: vendors/appviewx-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.appviewx.com/terms-of-service/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.appviewx.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.appviewx.com/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/appviewx
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.appviewx.com/2026.2.0/appviewx_setup.html
- group: docs
  title: ''
  type: Documentation
  url: https://docs.appviewx.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/appviewx/refs/heads/main/security/appviewx-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/appviewx-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/appviewx/refs/heads/main/security/appviewx-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/appviewx-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.appviewx.com
created: '2026-09-25'
description: AppViewX provides machine and AI agent identity security solutions, offering certificate lifecycle management, PKI modernization, post‑quantum cryptography readiness, and comprehensive compliance tools for enterprises. Their platform automates identity governance, secure code signing, and IoT device security, helping organizations manage digital certificates and keys at scale.
layout: provider
modified: '2026-09-25'
name: Appviewx
nav: Providers
network: true
overview: 'Appviewx publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Security, Identity, PKI, Certificate Management, and Artificial Intelligence.


  Appviewx''s developer surface includes getting-started guide, documentation, and 11 more developer resources.'
random_paper: 4
score:
  band: emerging
  composite: 20.0
  coverage:
    artifact_dirs: 5
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 53.6
    operational_transparency: 21.1
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 17.3
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Appviewx Domain Security
  slug: appviewx-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Appviewx Trust Center
  slug: appviewx-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS
slug: appviewx
tags:
- Security
- Identity
- PKI
- Certificate Management
- Artificial Intelligence
website: https://www.appviewx.com
---
