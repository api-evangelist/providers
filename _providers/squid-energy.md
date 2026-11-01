---
agent_readiness:
  band: agent-aware
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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 3
common:
- group: auth
  href: https://artifacts.apis.io/squid-energy/well-known/squid-energy-squid-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/squid-energy-squid-security.txt
- group: auth
  title: ''
  type: Compliance
  url: https://www.squid.energy/security
- group: agent
  href: https://artifacts.apis.io/squid-energy/llms/squid-energy-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/squid-energy-llms.txt
- group: auth
  href: https://artifacts.apis.io/squid-energy/well-known/squid-energy-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/squid-energy-www-security.txt
- group: auth
  href: https://artifacts.apis.io/squid-energy/well-known/squid-energy-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/squid-energy-security.txt
- group: agent
  href: https://artifacts.apis.io/squid-energy/well-known/squid-energy-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/squid-energy-well-known.yml
- group: other
  href: https://artifacts.apis.io/squid-energy/hosts/squid-energy-hosts.yml
  title: ''
  type: Hosts
  url: hosts/squid-energy-hosts.yml
- group: other
  href: https://artifacts.apis.io/squid-energy/vendors/squid-energy-vendors.yml
  title: ''
  type: Vendors
  url: vendors/squid-energy-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.squid.energy/terms-and-conditions
- group: auth
  title: ''
  type: Security
  url: https://www.squid.energy/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.squid.energy/privacy-policy
- group: auth
  href: https://artifacts.apis.io/squid-energy/security/squid-energy-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/squid-energy-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/squid-energy/security/squid-energy-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/squid-energy-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/squid-energy/security/squid-energy-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/squid-energy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://squid.energy
coverage:
  checked: '2026-10-29'
  detail: The documentation site https://www.squid.energy returns a JavaScript‑rendered page that cannot be parsed for a machine‑readable contract.
  evidence:
  - status: 200
    url: https://www.squid.energy
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-29'
description: Squid provides a model repository for power‑system planning, enabling engineers and agents to validate, analyse and publish interconnected models, scenarios and decisions. Backed by Y Combinator and partners, Squid connects tools like PowerFactory, PSS®E, IPSI, CYME and ETAP into a governed source, improving grid planning efficiency and transparency.
image: https://squid.energy/og.png
layout: provider
modified: '2026-10-29'
name: Squid
nav: Providers
network: true
overview: Squid is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, PowerSystems, Modeling, and GridPlanning.
random_paper: 21
score:
  band: emerging
  composite: 14.6
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 10.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 20.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Squid Energy Domain Security
  slug: squid-energy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Squid Energy Vulnerability Disclosure
  slug: squid-energy-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Squid Energy Trust Center
  slug: squid-energy-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: squid-energy
tags:
- Company
- Energy
- PowerSystems
- Modeling
- GridPlanning
website: https://squid.energy
---
