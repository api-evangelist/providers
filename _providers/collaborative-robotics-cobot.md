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
artifact_total: 2
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/collaborative-robotics-cobot/refs/heads/main/well-known/collaborative-robotics-cobot-clarity-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/collaborative-robotics-cobot-clarity-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/collaborative-robotics-cobot/refs/heads/main/well-known/collaborative-robotics-cobot-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/collaborative-robotics-cobot-well-known.yml
- group: auth
  title: ''
  type: Security
  url: https://clarity.com/vdp
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/collaborative-robotics-cobot/refs/heads/main/hosts/collaborative-robotics-cobot-hosts.yml
  title: ''
  type: Hosts
  url: hosts/collaborative-robotics-cobot-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/collaborative-robotics-cobot/refs/heads/main/vendors/collaborative-robotics-cobot-vendors.yml
  title: ''
  type: Vendors
  url: vendors/collaborative-robotics-cobot-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.co.bot/
- group: start
  title: ''
  type: SignUp
  url: https://www.co.bot/signup-thank-you
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.co.bot/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://www.co.bot/news
- group: other
  title: ''
  type: Leadership
  url: https://www.co.bot/team
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/collaborative-robotics-cobot/refs/heads/main/security/collaborative-robotics-cobot-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/collaborative-robotics-cobot-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/collaborative-robotics-cobot/refs/heads/main/security/collaborative-robotics-cobot-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/collaborative-robotics-cobot-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.co.bot/
coverage:
  checked: '2026-10-09'
  detail: The site serves only JavaScript‑rendered pages and no machine‑readable OpenAPI spec was found.
  evidence:
  - status: 200
    url: https://www.co.bot/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-09'
description: 'Collaborative Robotics Cobot is a company surfaced via the API Evangelist harvest backlog (source: secondary-market) and added to the network as a stub for full-pipeline profiling.'
image: https://cdn.sanity.io/images/3qpw73bq/yellow/0c6fde851c459ca8c6824bdacad5b3aa5c7e8983-1200x630.png?w=1200&h=630
layout: provider
modified: '2026-10-09'
name: Collaborative Robotics Cobot
nav: Providers
network: true
overview: 'Collaborative Robotics Cobot is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  Collaborative Robotics Cobot''s developer surface includes signup flow and 12 more developer resources.'
random_paper: 17
score:
  band: emerging
  composite: 11.9
  coverage:
    artifact_dirs: 7
    catalog_earned: 17.0
    catalog_earned_first_party: 0.0
    catalog_gap: 98.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 33.9
    operational_transparency: 10.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Collaborative Robotics Cobot Domain Security
  slug: collaborative-robotics-cobot-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Collaborative Robotics Cobot Vulnerability Disclosure
  slug: collaborative-robotics-cobot-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: collaborative-robotics-cobot
tags:
- Company
website: https://www.co.bot/
---
