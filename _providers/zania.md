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
  score: 6.5
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 3
common:
- group: agent
  href: https://artifacts.apis.io/zania/well-known/zania-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/zania-well-known.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.zania.ai/
- group: design
  href: https://artifacts.apis.io/zania/conformance/zania-conformance.yml
  title: ''
  type: Conformance
  url: conformance/zania-conformance.yml
- group: other
  href: https://artifacts.apis.io/zania/hosts/zania-hosts.yml
  title: ''
  type: Hosts
  url: hosts/zania-hosts.yml
- group: other
  href: https://artifacts.apis.io/zania/vendors/zania-vendors.yml
  title: ''
  type: Vendors
  url: vendors/zania-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://zania.ai/security
- group: company
  title: ''
  type: Newsroom
  url: https://zania.ai/newsroom
- group: auth
  href: https://artifacts.apis.io/zania/security/zania-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/zania-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/zania/security/zania-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/zania-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://zania.ai
- group: company
  title: ''
  type: AboutUs
  url: https://zania.ai/about-us
- group: commercial
  title: ''
  type: Pricing
  url: https://zania.ai/pricing
- group: company
  title: ''
  type: Blog
  url: https://zania.ai/blog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.zania.app
- group: commercial
  title: ''
  type: TermsOfService
  url: https://zania.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://zania.ai/privacy
- group: operate
  title: ''
  type: Contact
  url: https://zania.ai/contact-us
- group: auth
  href: https://artifacts.apis.io/zania/security/zania-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/zania-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/zania/security/zania-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/zania-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://zania.ai
- group: company
  title: ''
  type: AboutUs
  url: https://zania.ai/about-us
- group: commercial
  title: ''
  type: Pricing
  url: https://zania.ai/pricing
- group: company
  title: ''
  type: Blog
  url: https://zania.ai/blog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.zania.app
- group: commercial
  title: ''
  type: TermsOfService
  url: https://zania.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://zania.ai/privacy
- group: operate
  title: ''
  type: Contact
  url: https://zania.ai/contact-us
coverage:
  checked: '2026-10-23'
  detail: The homepage is a Framer‑generated site with no machine‑readable API spec linked.
  evidence:
  - status: 200
    url: https://zania.ai
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-22'
description: Zania provides AI‑driven compliance agents that automate third‑party risk management, security controls testing, and audit workflows. Leveraging large‑language models, Zania’s platform delivers high‑accuracy risk assessments, SOC 2, HIPAA, ISO 27001, GDPR, PCI‑DSS compliance automation, and real‑time security insights for enterprises.
image: https://framerusercontent.com/images/udx7BUTQxXOtum6Qk4yVuhmy9Nc.png
layout: provider
modified: '2026-10-22'
name: Zania
nav: Providers
network: true
overview: 'Zania is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Compliance, Risk Management, and GRC.


  Zania''s developer surface includes pricing, engineering blog, and 25 more developer resources.'
plans:
- name: Zania Plans Pricing
  plan_count: 0
  slug: zania-plans-pricing
random_paper: 3
score:
  band: emerging
  composite: 21.6
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 47.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    operational_transparency: 26.3
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
    score: 21.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Zania Domain Security
  slug: zania-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Zania Trust Center
  slug: zania-trust-center
  summary_line: SOC 2
slug: zania
tags:
- Company
- AI
- Compliance
- Risk Management
- GRC
- Automation
website: https://zania.ai
---
