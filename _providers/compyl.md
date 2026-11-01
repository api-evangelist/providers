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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Compyl provides an AI‑powered GRC platform with a developer API documented at https://compyl.com/guides/.
  name: Compyl API
  slug: compyl-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: Compliance
  url: https://trust.compyl.com/
- group: design
  href: https://artifacts.apis.io/compyl/conformance/compyl-conformance.yml
  title: ''
  type: Conformance
  url: conformance/compyl-conformance.yml
- group: agent
  href: https://artifacts.apis.io/compyl/llms/compyl-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/compyl-llms.txt
- group: other
  href: https://artifacts.apis.io/compyl/hosts/compyl-hosts.yml
  title: ''
  type: Hosts
  url: hosts/compyl-hosts.yml
- group: other
  href: https://artifacts.apis.io/compyl/vendors/compyl-vendors.yml
  title: ''
  type: Vendors
  url: vendors/compyl-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://compyl.com/privacy-policy/
- group: commercial
  title: ''
  type: Pricing
  url: https://compyl.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://compyl.com/blog/
- group: docs
  title: ''
  type: Documentation
  url: https://dev.compyl.com/
- group: auth
  href: https://artifacts.apis.io/compyl/security/compyl-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/compyl-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/compyl/security/compyl-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/compyl-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://compyl.com/
coverage:
  checked: '2026-10-10'
  detail: The developer guides page loads content via JavaScript, preventing automated spec discovery.
  evidence:
  - status: 200
    url: https://compyl.com/guides/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-10'
description: Compyl is an AI‑powered Governance, Risk and Compliance (GRC) platform that maps a single control library to over 70 frameworks including SOC 2, ISO 27001, HIPAA, PCI DSS, GDPR and NIST. It provides automated evidence collection, risk management, policy and contract management, and a trust‑center, enabling organizations to stay audit‑ready year‑round with integrated AI assistance.
image: https://mlseyjzh4hqa.i.optimole.com/w:auto/h:auto/q:90/f:best/https://compyl.com/wp-content/uploads/2023/03/CTA-Box.png
layout: provider
modified: '2026-10-10'
name: Compyl
nav: Providers
network: true
overview: 'Compyl is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, GRC, Artificial Intelligence, Compliance, and Risk Management.


  Compyl''s developer surface includes pricing, engineering blog, documentation, and 9 more developer resources.'
random_paper: 12
score:
  band: emerging
  composite: 18.1
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 36.8
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 57.1
    operational_transparency: 0.0
  previous_composite: 18.1
  provenance:
    conformance: first-party
    mcp: unknown
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
    score: 18.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Compyl Domain Security
  slug: compyl-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Compyl Trust Center
  slug: compyl-trust-center
  summary_line: SOC 2
slug: compyl
tags:
- Company
- GRC
- Artificial Intelligence
- Compliance
- Risk Management
website: https://compyl.com/
---
