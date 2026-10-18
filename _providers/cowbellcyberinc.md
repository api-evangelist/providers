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
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cowbellcyberinc/refs/heads/main/llms/cowbellcyberinc-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cowbellcyberinc-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cowbellcyberinc/refs/heads/main/hosts/cowbellcyberinc-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cowbellcyberinc-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cowbellcyberinc/refs/heads/main/vendors/cowbellcyberinc-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cowbellcyberinc-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cowbell.insure/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cowbell.insure/privacy/
- group: other
  title: ''
  type: Leadership
  url: https://cowbell.insure/team/
- group: company
  title: ''
  type: Blog
  url: https://cowbell.insure/blog/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cowbellcyberinc/refs/heads/main/security/cowbellcyberinc-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cowbellcyberinc-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cowbell.insure
coverage:
  checked: '2026-10-11'
  detail: Cowbell Cyber does not provide a developer program or public API documentation.
  evidence:
  - status: 200
    url: https://cowbell.insure
  reason: no-developer-program
  state: none
created: '2026-10-11'
description: Cowbell Cyber, Inc. provides AI‑native adaptive cyber and specialty insurance for small and medium‑size enterprises. Leveraging data and artificial intelligence, it offers real‑time risk assessment, automated underwriting, and API‑based quoting to simplify cyber coverage and improve resilience for businesses.
layout: provider
modified: '2026-10-11'
name: Cowbellcyberinc
nav: Providers
network: true
overview: 'Cowbellcyberinc is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Cyber Insurance, Artificial Intelligence, Adaptive, Small Business, and Specialty.


  Cowbellcyberinc''s developer surface includes engineering blog and 8 more developer resources.'
random_paper: 7
score:
  band: minimal
  composite: 9.3
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 53.6
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 11.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cowbellcyberinc Domain Security
  slug: cowbellcyberinc-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cowbellcyberinc
tags:
- Cyber Insurance
- Artificial Intelligence
- Adaptive
- Small Business
- Specialty
website: https://cowbell.insure
---
