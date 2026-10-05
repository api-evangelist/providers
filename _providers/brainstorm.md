---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
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
  score: 10.8
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/brainstorm/refs/heads/main/llms/brainstorm-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/brainstorm-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/brainstorm/refs/heads/main/well-known/brainstorm-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/brainstorm-status-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/brainstorm/refs/heads/main/well-known/brainstorm-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/brainstorm-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/brainstorm/refs/heads/main/hosts/brainstorm-hosts.yml
  title: ''
  type: Hosts
  url: hosts/brainstorm-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/brainstorm/refs/heads/main/vendors/brainstorm-vendors.yml
  title: ''
  type: Vendors
  url: vendors/brainstorm-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://support.brainstorminc.com/support/home
- group: operate
  title: ''
  type: StatusPage
  url: https://status.brainstorminc.com/
- group: auth
  title: ''
  type: Security
  url: https://www.brainstorminc.com/hubfs/Assets%20for%20Resource%20Center/Security/Scam%20Wise%C2%A0Remote%20Security%20Dos%20and%20Don%E2%80%99ts.pdf
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.brainstorminc.com/privacypolicy
- group: company
  title: ''
  type: Newsroom
  url: https://www.brainstorminc.com/resources/news
- group: company
  title: ''
  type: Blog
  url: https://www.brainstorminc.com/blog
- group: docs
  title: ''
  type: Documentation
  url: https://help.brainstorminc.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/brainstorm/refs/heads/main/security/brainstorm-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/brainstorm-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.brainstorminc.com/
coverage:
  checked: '2026-10-03'
  detail: The provider's site offers no public machine‑readable API specification despite having a login portal and blog.
  evidence:
  - status: 404
    url: https://api.brainstorminc.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-03'
description: BrainStorm provides an Enterprise AI Adoption Platform designed to drive behavior change across organizations. It offers adaptive workflows, content packs, and AI‑powered tools for software vendors, customers, and partners to accelerate product adoption, user onboarding, and change management. The platform integrates with Microsoft 365 Copilot, ChatGPT, Claude AI, and other AI services to deliver personalized learning, security compliance, and analytics.
image: https://www.brainstorminc.com/hubfs/2024/Website/Videos/Thumbnail2.jpg
layout: provider
modified: '2026-10-03'
name: BrainStorm
nav: Providers
network: true
overview: 'BrainStorm is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Enterprise, Adoption, and Platform.


  BrainStorm''s developer surface includes support, engineering blog, documentation, and 11 more developer resources.'
random_paper: 11
score:
  band: emerging
  composite: 14.4
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
    developer_ergonomics: 16.7
    discoverability: 57.1
    operational_transparency: 26.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Brainstorm Domain Security
  slug: brainstorm-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: brainstorm
tags:
- Company
- Artificial Intelligence
- Enterprise
- Adoption
- Platform
website: https://www.brainstorminc.com/
---
