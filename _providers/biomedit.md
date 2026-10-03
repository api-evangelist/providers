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
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/biomedit/refs/heads/main/hosts/biomedit-hosts.yml
  title: ''
  type: Hosts
  url: hosts/biomedit-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/biomedit/refs/heads/main/vendors/biomedit-vendors.yml
  title: ''
  type: Vendors
  url: vendors/biomedit-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://biomedit.com/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://biomedit.com/privacy-policy
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/biomedit/refs/heads/main/security/biomedit-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/biomedit-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://biomedit.com
coverage:
  checked: '2026-09-28'
  detail: OpenAPI spec not found at standard endpoints on api.biomedit.com
  evidence:
  - status: timeout
    url: https://api.biomedit.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-28'
description: BiomEdit is an innovation company that discovers, designs, and develops novel microbiome‑derived products to address unmet needs in animal health. Leveraging the animal’s own microbial ecosystem, BiomEdit creates solutions where none exist, focusing on improving animal health through microbiome science and advanced product development pipelines.
image: https://biomedit.com/wp-content/uploads/2024/01/thumbnail_image003.png
layout: provider
modified: '2026-09-28'
name: BiomEdit
nav: Providers
network: true
overview: BiomEdit is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Animal Health, Microbiome, Biotechnology, and Innovation.
random_paper: 9
score:
  band: minimal
  composite: 8.8
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 10.9
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Biomedit Domain Security
  slug: biomedit-domain-security
  summary_line: TLSv1.3
slug: biomedit
tags:
- Company
- Animal Health
- Microbiome
- Biotechnology
- Innovation
website: https://biomedit.com
---
