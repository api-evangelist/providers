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
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/taiki/hosts/taiki-hosts.yml
  title: ''
  type: Hosts
  url: hosts/taiki-hosts.yml
- group: other
  href: https://artifacts.apis.io/taiki/vendors/taiki-vendors.yml
  title: ''
  type: Vendors
  url: vendors/taiki-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.taiki.ai/legal/privacy-policy
- group: auth
  href: https://artifacts.apis.io/taiki/security/taiki-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/taiki-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://taiki.ai/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://taiki.ai/
  reason: no-developer-program
  state: none
created: '2026-10-21'
description: 'Taiki is a company surfaced via the API Evangelist harvest backlog (source: g2-catalog) and added to the network as a stub for full-pipeline profiling.'
image: https://framerusercontent.com/assets/d1ErO15r64xACIKv7lFzJWrs8Q.png
layout: provider
modified: '2026-10-21'
name: Taiki
nav: Providers
network: true
overview: Taiki is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Tax Documents, API, Payroll Integration, Financial Data Extraction, and Tax Forms.
random_paper: 2
score:
  band: minimal
  composite: 4.2
  coverage:
    artifact_dirs: 7
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 39.3
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 7.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Taiki Domain Security
  slug: taiki-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: taiki
tags:
- Tax Documents
- API
- Payroll Integration
- Financial Data Extraction
- Tax Forms
- Bank Statements
- Brokerage Statements
website: https://taiki.ai/
---
