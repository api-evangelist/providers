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
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/credit-key/refs/heads/main/hosts/credit-key-hosts.yml
  title: ''
  type: Hosts
  url: hosts/credit-key-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/credit-key/refs/heads/main/vendors/credit-key-vendors.yml
  title: ''
  type: Vendors
  url: vendors/credit-key-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/credit-key/refs/heads/main/security/credit-key-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/credit-key-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.creditkey.com
coverage:
  checked: '2026-10-11'
  detail: The Credit Key website provides no machine‑readable API specification and only static marketing pages.
  evidence:
  - status: 200
    url: https://www.creditkey.com
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-11'
description: Credit Key provides a B2B payment platform that offers buy‑now‑pay‑later financing, net‑30 terms, and installment options for wholesale distributors, technology vendors, and restaurant equipment suppliers. By underwriting credit at the point of sale, Credit Key enables merchants to increase conversions, average order value, and cash‑flow efficiency while assuming the risk of repayment. The platform includes a merchant portal, a consumer‑facing Credit Key Card, and an API for integrating financing into e‑commerce and in‑store checkout flows.
layout: provider
modified: '2026-10-11'
name: Credit Key
nav: Providers
network: true
overview: Credit Key is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include B2B Payments, Financing, Buy Now Pay Later, Credit, and Wholesale.
random_paper: 19
score:
  band: minimal
  composite: 2.3
  coverage:
    artifact_dirs: 5
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 5.4
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Credit Key Domain Security
  slug: credit-key-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: credit-key
tags:
- B2B Payments
- Financing
- Buy Now Pay Later
- Credit
- Wholesale
website: https://www.creditkey.com
---
