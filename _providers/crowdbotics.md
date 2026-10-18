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
  href: https://raw.githubusercontent.com/api-evangelist/crowdbotics/refs/heads/main/llms/crowdbotics-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/crowdbotics-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/crowdbotics/refs/heads/main/well-known/crowdbotics-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/crowdbotics-status-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/crowdbotics/refs/heads/main/well-known/crowdbotics-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/crowdbotics-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/crowdbotics/refs/heads/main/hosts/crowdbotics-hosts.yml
  title: ''
  type: Hosts
  url: hosts/crowdbotics-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/crowdbotics/refs/heads/main/vendors/crowdbotics-vendors.yml
  title: ''
  type: Vendors
  url: vendors/crowdbotics-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/crowdbotics/refs/heads/main/packages/crowdbotics-packages.yml
  title: ''
  type: SDKs
  url: packages/crowdbotics-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/crowdbotics/refs/heads/main/packages/crowdbotics-packages.yml
  title: ''
  type: Packages
  url: packages/crowdbotics-packages.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.crowdbotics.com/
- group: company
  title: ''
  type: Newsroom
  url: https://crowdbotics.com/newsroom/
- group: other
  title: ''
  type: Leadership
  url: https://crowdbotics.com/leadership/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/crowdbotics/refs/heads/main/security/crowdbotics-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/crowdbotics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://crowdbotics.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.crowdbotics.com/
- group: company
  title: ''
  type: Blog
  url: https://crowdbotics.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://crowdbotics.com/support/
- group: commercial
  title: ''
  type: Pricing
  url: https://crowdbotics.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://crowdbotics.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://crowdbotics.com/privacy-policy/
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 403
    url: https://docs.crowdbotics.com/mcp
  - status: 403
    url: https://status.crowdbotics.com/mcp
  - status: 200
    url: https://crowdbotics.com
  - status: 403
    url: https://equityzen.com/company/crowdbotics
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-11'
description: Crowdbotics, now operating as CoreStory, provides an AI‑powered platform that modernizes and maintains software applications. It offers tools for code analysis, automated refactoring, and full‑stack development, helping enterprises accelerate digital transformation while reducing technical debt.
image: https://crowdbotics.com/wp-content/uploads/2024/12/Screenshot-2024-12-04-at-12.27.01 PM.png
layout: provider
modified: '2026-10-11'
name: Crowdbotics
nav: Providers
network: true
overview: 'Crowdbotics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Platform, Software Modernization, and Low-code.


  Crowdbotics'' developer surface includes documentation, engineering blog, support, pricing, and 14 more developer resources.'
random_paper: 21
score:
  band: emerging
  composite: 18.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 58.9
    operational_transparency: 15.8
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Crowdbotics Domain Security
  slug: crowdbotics-domain-security
  summary_line: TLSv1.3 · DMARC
slug: crowdbotics
tags:
- Company
- Artificial Intelligence
- Platform
- Software Modernization
- Low-code
website: https://crowdbotics.com
---
