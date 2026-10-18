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
    well_known_catalog: true
  schema_version: '0.2'
  score: 13.7
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: Stravito provides an AI‑powered customer intelligence platform.
  name: Stravito API
  slug: stravito-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: Security
  url: https://hackerone.com/6c1a1442-7bd8-4bc7-a992-f327c7fcf284/embedded_submissions/new
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/stravito/refs/heads/main/llms/stravito-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/stravito-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/stravito/refs/heads/main/well-known/stravito-stravito-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/stravito-stravito-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/stravito/refs/heads/main/well-known/stravito-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/stravito-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/stravito/refs/heads/main/well-known/stravito-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/stravito-help-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/stravito/refs/heads/main/well-known/stravito-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/stravito-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/stravito/refs/heads/main/hosts/stravito-hosts.yml
  title: ''
  type: Hosts
  url: hosts/stravito-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/stravito/refs/heads/main/vendors/stravito-vendors.yml
  title: ''
  type: Vendors
  url: vendors/stravito-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.stravito.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.stravito.com/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://www.stravito.com/news
- group: other
  title: ''
  type: Leadership
  url: https://www.stravito.com/solution/team/marketing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Stravito
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/stravito/refs/heads/main/security/stravito-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/stravito-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/stravito/refs/heads/main/security/stravito-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/stravito-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.stravito.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.stravito.com/resources
- group: company
  title: ''
  type: Blog
  url: https://www.stravito.com/resources
- group: operate
  title: ''
  type: Support
  url: https://www.stravito.com/contact-us
- group: start
  title: ''
  type: GettingStarted
  url: https://www.stravito.com/request-a-stravito-demo
coverage:
  checked: '2026-10-15'
  detail: Help Center pages render via JavaScript and provide no machine‑readable API spec.
  evidence:
  - status: 200
    url: https://help.stravito.com/en/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-15'
description: Stravito provides an AI‑powered customer intelligence platform that helps enterprise brands simulate consumer reactions, segment audiences, and accelerate innovation. By leveraging proprietary synthetic population modeling and behavioral insights, Stravito enables teams to test concepts, campaigns, and product ideas quickly, reducing time‑to‑insight and improving decision‑making across marketing, research, and product development.
layout: provider
modified: '2026-10-15'
name: Stravito
nav: Providers
network: true
overview: 'Stravito is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Customer Intelligence, Market Research, Enterprise, and Analytics.


  Stravito''s developer surface includes documentation, engineering blog, support, getting-started guide, and 16 more developer resources.'
random_paper: 12
score:
  band: emerging
  composite: 19.3
  coverage:
    artifact_dirs: 6
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 18.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 64.3
    operational_transparency: 15.8
  provenance:
    mcp: unknown
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
  name: Stravito Domain Security
  slug: stravito-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Stravito Vulnerability Disclosure
  slug: stravito-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: stravito
tags:
- Artificial Intelligence
- Customer Intelligence
- Market Research
- Enterprise
- Analytics
website: https://www.stravito.com/
---
