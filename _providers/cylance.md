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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: documented
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 22.9
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: API documentation referenced from Arctic Wolf developer portal. No machine‑readable contract discovered.
  name: Cylance API
  slug: cylance-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: Compliance
  url: https://trust.arcticwolf.com/
- group: auth
  title: ''
  type: Security
  url: https://arcticwolf.com/vulnerability-disclosure
- group: agent
  href: https://artifacts.apis.io/cylance/llms/cylance-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cylance-llms.txt
- group: auth
  href: https://artifacts.apis.io/cylance/well-known/cylance-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/cylance-status-security.txt
- group: auth
  href: https://artifacts.apis.io/cylance/well-known/cylance-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/cylance-security.txt
- group: agent
  href: https://artifacts.apis.io/cylance/well-known/cylance-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cylance-well-known.yml
- group: other
  href: https://artifacts.apis.io/cylance/hosts/cylance-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cylance-hosts.yml
- group: other
  href: https://artifacts.apis.io/cylance/vendors/cylance-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cylance-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://community.arcticwolf.com/site/terms
- group: operate
  title: ''
  type: StatusPage
  url: https://status.arcticwolf.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://arcticwolf.com/privacy-policy/
- group: company
  title: ''
  type: Blog
  url: https://arcticwolf.com/resources/blog/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.arcticwolf.com/en/onboarding-portal
- group: docs
  title: ''
  type: Documentation
  url: https://developer.arcticwolf.com/
- group: auth
  href: https://artifacts.apis.io/cylance/security/cylance-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/cylance-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/cylance/security/cylance-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/cylance-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/cylance/security/cylance-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cylance-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://arcticwolf.com/cylance
coverage:
  detail: Developer portal pages are rendered via JavaScript, no static OpenAPI spec found.
  evidence:
  - status: 200
    url: https://developer.arcticwolf.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-21'
description: Cylance, now part of Arctic Wolf, provides AI‑driven endpoint protection and threat detection solutions. Leveraging machine‑learning, the platform prevents malware, ransomware and zero‑day attacks before they execute, helping enterprises reduce risk and meet compliance. The company’s technology integrates with broader security operations, offering visibility, automation and advanced analytics for modern cyber defenses.
image: https://arcticwolf.com/wp-content/uploads/2025/01/aw_cylance_splash-og-image.jpg
layout: provider
modified: '2026-10-21'
name: Cylance
nav: Providers
network: true
overview: 'Cylance is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Endpoint Security, Artificial Intelligence, and Cybersecurity.


  Cylance''s developer surface includes engineering blog, getting-started guide, documentation, and 15 more developer resources.'
random_paper: 15
score:
  band: emerging
  composite: 23.2
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 57.1
    operational_transparency: 26.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cylance Domain Security
  slug: cylance-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Cylance Vulnerability Disclosure
  slug: cylance-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Cylance Trust Center
  slug: cylance-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, PCI DSS, HIPAA, FedRAMP, GDPR, CSA STAR
slug: cylance
tags:
- Company
- Security
- Endpoint Security
- Artificial Intelligence
- Cybersecurity
website: https://arcticwolf.com/cylance
---
