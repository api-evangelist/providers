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
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: Compliance
  url: https://www.banquethealth.com/security
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/banquet-health/refs/heads/main/conformance/banquet-health-conformance.yml
  title: ''
  type: Conformance
  url: conformance/banquet-health-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/banquet-health/refs/heads/main/hosts/banquet-health-hosts.yml
  title: ''
  type: Hosts
  url: hosts/banquet-health-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/banquet-health/refs/heads/main/vendors/banquet-health-vendors.yml
  title: ''
  type: Vendors
  url: vendors/banquet-health-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://www.banquethealth.com/security
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/banquet-health/refs/heads/main/security/banquet-health-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/banquet-health-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/banquet-health/refs/heads/main/security/banquet-health-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/banquet-health-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.banquethealth.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.banquethealth.com/product
- group: company
  title: ''
  type: Blog
  url: https://www.banquethealth.com/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.banquethealth.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.banquethealth.com/terms-of-service
coverage:
  checked: '2026-09-27'
  detail: No OpenAPI, AsyncAPI, GraphQL or other machine‑readable contract found on the provider’s website.
  evidence:
  - status: 200
    url: https://www.banquethealth.com
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-27'
description: Banquet Health provides a modern software platform that transforms hospital foodservice operations. It automates meal management, reduces errors, ensures compliance, integrates with EMR systems, and improves patient satisfaction by delivering the right meal at the right time. The solution helps healthcare providers cut food waste, boost operational efficiency, and enhance the overall patient experience through personalized menus and real-time ordering.
image: https://cdn.prod.website-files.com/67e6f68dda498227a52ed667/681e26eb685db945bd71eb8b_5de154fe29d586b4e9a017fed43cdaf2_Frame%201410124021.png
layout: provider
modified: '2026-09-27'
name: Banquet Health
nav: Providers
network: true
overview: 'Banquet Health is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Food Service Management, Hospital Software, Meal Management, Healthcare Analytics, and Clinical Nutrition.


  Banquet Health''s developer surface includes documentation, engineering blog, and 10 more developer resources.'
random_paper: 19
score:
  band: emerging
  composite: 19.1
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 36.8
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 48.2
    operational_transparency: 10.5
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Health
    regime_id: health
    score: 18.8
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Banquet Health Domain Security
  slug: banquet-health-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Banquet Health Trust Center
  slug: banquet-health-trust-center
  summary_line: SOC 2, HIPAA
slug: banquet-health
tags:
- Food Service Management
- Hospital Software
- Meal Management
- Healthcare Analytics
- Clinical Nutrition
website: https://www.banquethealth.com
---
