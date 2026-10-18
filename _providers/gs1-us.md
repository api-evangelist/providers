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
artifact_total: 2
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/gs1-us/refs/heads/main/plans/gs1-us-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/gs1-us-plans-pricing.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/gs1-us/refs/heads/main/llms/gs1-us-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/gs1-us-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/gs1-us/refs/heads/main/hosts/gs1-us-hosts.yml
  title: ''
  type: Hosts
  url: hosts/gs1-us-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/gs1-us/refs/heads/main/vendors/gs1-us-vendors.yml
  title: ''
  type: Vendors
  url: vendors/gs1-us-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.gs1us.org/terms-of-use
- group: auth
  title: ''
  type: Security
  url: https://community.gs1us.org/HigherLogic/Security/ResetPassword.aspx
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.gs1us.org/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.connect.gs1us.org/pricing-travel
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.help.gs1us.org/whats-new
- group: start
  title: ''
  type: GettingStarted
  url: https://www.help.gs1us.org/rapid-record-setup
- group: docs
  title: ''
  type: Documentation
  url: https://developer.gs1us.org/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/gs1-us/refs/heads/main/security/gs1-us-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/gs1-us-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.gs1us.org
coverage:
  checked: '2026-10-14'
  detail: The GS1 US developer portal provides documentation but no machine‑readable OpenAPI, AsyncAPI, GraphQL, or other contract is publicly available.
  evidence:
  - status: 200
    url: https://developer.gs1us.org/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-14'
description: GS1 US is the US member organization of GS1, the global standards body for business communication. It provides a range of services including barcode issuance, product identification, data standards, and supply chain solutions to help businesses of all sizes streamline operations, improve traceability, and meet regulatory requirements. Through its web portal, GS1 US offers tools, resources, and support for obtaining UPCs, GTINs, GLNs, and other identifiers, as well as educational content and industry collaborations.
layout: provider
modified: '2026-10-14'
name: GS1 US
nav: Providers
network: true
overview: 'GS1 US is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Standards, Barcodes, Supply Chain, and Data.


  GS1 US''s developer surface includes pricing, changelog, getting-started guide, documentation, and 9 more developer resources.'
plans:
- name: Gs1 Us Plans Pricing
  plan_count: 2
  slug: gs1-us-plans-pricing
random_paper: 16
score:
  band: emerging
  composite: 23.2
  coverage:
    artifact_dirs: 7
    catalog_earned: 33.0
    catalog_earned_first_party: 8.0
    catalog_gap: 82.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 51.8
    operational_transparency: 26.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Gs1 Us Domain Security
  slug: gs1-us-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: gs1-us
tags:
- Company
- Standards
- Barcodes
- Supply Chain
- Data
website: https://www.gs1us.org
---
