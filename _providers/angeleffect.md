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
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/angeleffect/refs/heads/main/hosts/angeleffect-hosts.yml
  title: ''
  type: Hosts
  url: hosts/angeleffect-hosts.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://angeleffect.co/privacy-and-cookie-policy/
- group: docs
  title: ''
  type: Documentation
  url: https://dev.angeleffect.co/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/angeleffect/refs/heads/main/security/angeleffect-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/angeleffect-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://angeleffect.co
coverage:
  checked: 2026-09-24
  detail: Developer reference pages return HTML shells and no machine‑readable OpenAPI spec was found.
  evidence:
  - status: 200
    url: https://dev.angeleffect.co/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-24'
description: Angeleffect is an angel investing platform that connects entrepreneurs with value‑creating investors, partners, and mentors worldwide. The site describes a global network offering access to high‑impact startup opportunities, with features such as a portfolio of over 2,200 startups across 112 countries, mentorship, and a minimum ticket size of $5,000. It provides information on its AE Network, fund structure, FAQs, and contact options, positioning itself as a bridge between capital and innovative ventures.
image: https://angeleffect.co/wp-content/uploads/2021/04/ae-og-image-e1618481851853.jpg
layout: provider
modified: '2026-09-24'
name: Angeleffect
nav: Providers
network: true
overview: 'Angeleffect is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Angel Investing, Platform, Startup Funding, and Networks.


  Angeleffect''s developer surface includes documentation and 4 more developer resources.'
random_paper: 18
score:
  band: minimal
  composite: 8.0
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Angeleffect Domain Security
  slug: angeleffect-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: angeleffect
tags:
- Company
- Angel Investing
- Platform
- Startup Funding
- Networks
website: https://angeleffect.co
---
