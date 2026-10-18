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
  href: https://raw.githubusercontent.com/api-evangelist/codagenixinc/refs/heads/main/hosts/codagenixinc-hosts.yml
  title: ''
  type: Hosts
  url: hosts/codagenixinc-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/codagenixinc/refs/heads/main/vendors/codagenixinc-vendors.yml
  title: ''
  type: Vendors
  url: vendors/codagenixinc-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://codagenix.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://codagenix.com/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://codagenix.com/news/
- group: other
  title: ''
  type: Leadership
  url: https://codagenix.com/team/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/codagenixinc/refs/heads/main/security/codagenixinc-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/codagenixinc-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://codagenix.com
coverage:
  checked: '2026-10-09'
  detail: Codagenixinc provides no public developer program or API documentation.
  evidence:
  - status: 200
    url: https://codagenix.com
  reason: no-developer-program
  state: none
created: '2026-10-09'
description: Codagenix is a biotechnology company focused on engineering live‑attenuated viruses using codon deoptimization to create safe, effective vaccines. The firm combines synthetic biology with advanced virology to develop next‑generation vaccines for infectious diseases, aiming to improve global health outcomes through rapid, scalable, and stable vaccine platforms.
image: https://codagenix.com/wp-content/uploads/2022/03/codagenix-social-share-image.png
layout: provider
modified: '2026-10-09'
name: Codagenixinc
nav: Providers
network: true
overview: Codagenixinc is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.
random_paper: 6
score:
  band: minimal
  composite: 8.3
  coverage:
    artifact_dirs: 4
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 42.9
    operational_transparency: 0.0
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
  name: Codagenixinc Domain Security
  slug: codagenixinc-domain-security
  summary_line: TLSv1.3 · DMARC
slug: codagenixinc
tags:
- Company
website: https://codagenix.com
---
