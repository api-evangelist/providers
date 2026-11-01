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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Public API for ICE server configuration and other integration points.
  name: Pop API
  slug: pop-api
artifact_total: 4
common:
- group: agent
  href: https://artifacts.apis.io/pop/llms/pop-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/pop-llms.txt
- group: auth
  href: https://artifacts.apis.io/pop/well-known/pop-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/pop-status-security.txt
- group: agent
  href: https://artifacts.apis.io/pop/well-known/pop-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/pop-well-known.yml
- group: other
  href: https://artifacts.apis.io/pop/hosts/pop-hosts.yml
  title: ''
  type: Hosts
  url: hosts/pop-hosts.yml
- group: other
  href: https://artifacts.apis.io/pop/vendors/pop-vendors.yml
  title: ''
  type: Vendors
  url: vendors/pop-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.pop.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://support.pop.com/changelog
- group: docs
  title: ''
  type: Documentation
  url: https://dev.pop.com/
- group: auth
  href: https://artifacts.apis.io/pop/security/pop-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/pop-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://pop.com
- group: commercial
  title: ''
  type: Pricing
  url: https://pop.com/pricing
- group: operate
  title: ''
  type: Support
  url: https://support.pop.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://pop.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://pop.com/eula
- group: start
  title: ''
  type: SignUp
  url: https://pop.com/login
coverage:
  checked: '2026-10-29'
  detail: The developer portal at https://dev.pop.com/ is a JavaScript‑rendered SPA, providing no machine‑readable OpenAPI or other contract.
  evidence:
  - status: 200
    url: https://dev.pop.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-29'
description: Pop is a remote collaboration platform that provides multiplayer screen sharing, voice and video, whiteboarding, and integrated Slack calls, enabling teams to work together as if in the same room. It supports macOS, Windows, Linux, and major browsers, offering low‑latency screen sharing and the ability for each participant to control the shared screen with their own mouse and keyboard. Pop also offers a public API endpoint for ICE server configuration and provides pricing plans for individuals and teams. The company, Pop Technologies, Inc., markets its product for pair programming, remote meetings, and collaborative brainstorming.
image: https://pop.com/assets/img/unfurl.png
layout: provider
modified: '2026-10-29'
name: Pop
nav: Providers
network: true
overview: 'Pop is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Collaboration, Screen Sharing, Video Conferencing, and Whiteboarding.


  Pop''s developer surface includes changelog, documentation, pricing, support, signup flow, and 10 more developer resources.'
random_paper: 23
scopes:
- name: Pop Scopes
  scope_count: 0
  slug: pop-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 24.2
  coverage:
    artifact_dirs: 19
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 57.1
    operational_transparency: 42.1
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 23.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Pop Authentication
  slug: pop-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Pop Domain Security
  slug: pop-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: pop
tags:
- Company
- Collaboration
- Screen Sharing
- Video Conferencing
- Whiteboarding
- Remote Work
website: https://pop.com
---
