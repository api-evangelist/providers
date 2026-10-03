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
  href: https://raw.githubusercontent.com/api-evangelist/audion/refs/heads/main/hosts/audion-hosts.yml
  title: ''
  type: Hosts
  url: hosts/audion-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/audion/refs/heads/main/vendors/audion-vendors.yml
  title: ''
  type: Vendors
  url: vendors/audion-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.audion.com/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.audion.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.audion.com/news
- group: start
  title: ''
  type: Login
  url: https://www.audion.com/login
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/audion/refs/heads/main/security/audion-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/audion-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.audion.com
coverage:
  checked: 2026-09-26
  detail: No OpenAPI or other machine-readable contract found at api.audion.com or portal.audion.com.
  evidence:
  - status: 0
    url: https://api.audion.com/openapi.json
  - status: 302
    url: https://portal.audion.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-26'
description: Audion Packaging Machines, founded in 1947, designs and manufactures innovative packaging solutions for healthcare, food, industry and e‑commerce sectors. Their product range includes automatic baggers, industrial bag sealers and sustainable packaging technologies, emphasizing automation, digital integration and net‑zero operations. Audion serves a global customer base with a focus on quality, reliability and environmental responsibility.
image: https://www.audion.com/images/favicon.svg
layout: provider
modified: '2026-09-26'
name: Audion
nav: Providers
network: true
overview: Audion is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Packaging, Manufacturing, Automation, and Sustainability.
random_paper: 2
score:
  band: emerging
  composite: 11.6
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Audion Domain Security
  slug: audion-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: audion
tags:
- Company
- Packaging
- Manufacturing
- Automation
- Sustainability
website: https://www.audion.com
---
