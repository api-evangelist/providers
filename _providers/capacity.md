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
  href: https://raw.githubusercontent.com/api-evangelist/capacity/refs/heads/main/llms/capacity-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/capacity-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/capacity/refs/heads/main/well-known/capacity-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/capacity-status-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/capacity/refs/heads/main/well-known/capacity-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/capacity-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/capacity/refs/heads/main/hosts/capacity-hosts.yml
  title: ''
  type: Hosts
  url: hosts/capacity-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/capacity/refs/heads/main/vendors/capacity-vendors.yml
  title: ''
  type: Vendors
  url: vendors/capacity-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/capacity/refs/heads/main/packages/capacity-packages.yml
  title: ''
  type: SDKs
  url: packages/capacity-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/capacity/refs/heads/main/packages/capacity-packages.yml
  title: ''
  type: Packages
  url: packages/capacity-packages.yml
- group: operate
  title: ''
  type: Support
  url: https://support.capacity.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.capacity.com/
- group: auth
  title: ''
  type: Security
  url: https://capacity.com/security/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://capacity.com/privacy-policy/
- group: commercial
  title: ''
  type: Pricing
  url: https://capacity.com/pricing/
- group: company
  title: ''
  type: Newsroom
  url: https://capacity.com/press/
- group: start
  title: ''
  type: Login
  url: https://capacity.com/login/
- group: company
  title: ''
  type: Blog
  url: https://capacity.com/blog/
- group: start
  title: ''
  type: GettingStarted
  url: https://support.capacity.com/folder/335e2350-2788-491b-9bd6-92fdd048b81d
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/capacity/refs/heads/main/security/capacity-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/capacity-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://capacity.com/
coverage:
  checked: '2026-10-06'
  detail: OpenAPI spec not found at standard endpoints on api.capacity.com (all returned 404)
  evidence:
  - status: 404
    url: https://api.capacity.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-06'
description: Capacity provides a unified CX automation platform that leverages AI agents to automate, assist, analyze, and engage customers across voice, chat, SMS, email, and web channels. Founded in 2017 and part of the Equity.com incubator, it serves over 20,000 organizations, handling billions of automated interactions. The platform offers AI knowledge orchestration, real‑time agent assist, analytics, outbound campaigns, and industry‑specific solutions, aiming to reduce support costs and improve customer experiences.
image: https://capacity.com/wp-content/uploads/2023/01/2021-Homepage-Header-03-with-Security-Badges-1500x1030-1.webp
layout: provider
modified: '2026-10-06'
name: Capacity
nav: Providers
network: true
overview: 'Capacity is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Customer Experience, Automation, and Platform.


  Capacity''s developer surface includes support, pricing, engineering blog, getting-started guide, and 14 more developer resources.'
random_paper: 10
score:
  band: emerging
  composite: 20.3
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 57.1
    operational_transparency: 26.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Capacity Domain Security
  slug: capacity-domain-security
  summary_line: TLSv1.3 · DMARC
slug: capacity
tags:
- Company
- Artificial Intelligence
- Customer Experience
- Automation
- Platform
- Software-as-a-Service
website: https://capacity.com/
---
