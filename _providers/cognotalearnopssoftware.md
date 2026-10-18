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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 14.4
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: Documentation and support portal for Cognota Learning Operations platform.
  name: Cognota Help Center
  slug: cognota-help-center
artifact_total: 3
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cognotalearnopssoftware/refs/heads/main/well-known/cognotalearnopssoftware-cognota-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/cognotalearnopssoftware-cognota-security.txt
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/cognotalearnopssoftware/refs/heads/main/plans/cognotalearnopssoftware-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cognotalearnopssoftware-plans-pricing.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cognotalearnopssoftware/refs/heads/main/llms/cognotalearnopssoftware-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cognotalearnopssoftware-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cognotalearnopssoftware/refs/heads/main/well-known/cognotalearnopssoftware-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/cognotalearnopssoftware-help-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cognotalearnopssoftware/refs/heads/main/well-known/cognotalearnopssoftware-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cognotalearnopssoftware-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cognotalearnopssoftware/refs/heads/main/hosts/cognotalearnopssoftware-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cognotalearnopssoftware-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cognotalearnopssoftware/refs/heads/main/vendors/cognotalearnopssoftware-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cognotalearnopssoftware-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.cognota.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cognota.com/terms-of-use/
- group: operate
  title: ''
  type: Support
  url: https://help.cognota.com/en/
- group: operate
  title: ''
  type: StatusPage
  url: https://cognota.statuspage.io/
- group: start
  title: ''
  type: SignUp
  url: https://cognota.com/sign-up-cognota-assist-marketplace/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cognota.com/privacy-policy/
- group: commercial
  title: ''
  type: Pricing
  url: https://cognota.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://cognota.com/blog/
- group: start
  title: ''
  type: GettingStarted
  url: https://help.cognota.com/en/articles/12241145-cognota-getting-started-toolkit
- group: docs
  title: ''
  type: Documentation
  url: https://help.cognota.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Cognota
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cognotalearnopssoftware/refs/heads/main/security/cognotalearnopssoftware-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cognotalearnopssoftware-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cognota.com
coverage:
  checked: '2026-10-09'
  detail: Help center pages are rendered via JavaScript and no machine‑readable API spec was found.
  evidence:
  - status: 200
    url: https://help.cognota.com/en/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-09'
description: Cognota is the first Learning Operations platform, helping L&D and talent professionals transform workforce enablement. It offers a unified LearnOps® operating system with features like workflow, marketplace, AI agents, and analytics, serving enterprise customers such as Truist, Sun Life, BMS, GE, and Ace Hardware.
image: https://cognota.com/wp-content/uploads/2026/09/capacity-callouts-signal-legend-transparent-shadow-matched.png
layout: provider
modified: '2026-10-09'
name: Cognotalearnopssoftware
nav: Providers
network: true
overview: 'Cognotalearnopssoftware is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include LearnOps, Learning Operations, Talent Development, HR Software, and Marketplace.


  Cognotalearnopssoftware''s developer surface includes support, signup flow, pricing, engineering blog, getting-started guide, documentation, and 14 more developer resources.'
plans:
- name: Cognotalearnopssoftware Plans Pricing
  plan_count: 1
  slug: cognotalearnopssoftware-plans-pricing
random_paper: 4
score:
  band: thin
  composite: 31.0
  coverage:
    artifact_dirs: 6
    catalog_earned: 40.0
    catalog_earned_first_party: 8.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 73.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 64.3
    operational_transparency: 21.1
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cognotalearnopssoftware Domain Security
  slug: cognotalearnopssoftware-domain-security
  summary_line: TLSv1.3 · DMARC
slug: cognotalearnopssoftware
tags:
- LearnOps
- Learning Operations
- Talent Development
- HR Software
- Marketplace
- AI Governance
website: https://cognota.com
---
