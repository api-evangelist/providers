---
agent_readiness:
  band: agent-aware
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
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 12.9
  scored_at: '2026-10-17'
api_count: 7
apis:
- baseURL: https://clawhub.ai
  baseurl_source: declared
  description: The Clawdbot API API from Clawdbot — 1 operation(s) for clawdbot api.
  name: Clawdbot Clawdbot API
  slug: clawdbot-clawdbot-api-api
- baseURL: https://clawhub.ai
  baseurl_source: declared
  description: The Npm API from Clawdbot — 2 operation(s) for npm.
  name: Clawdbot Npm API
  slug: clawdbot-npm-api
- baseURL: https://clawhub.ai
  baseurl_source: declared
  description: The Packages API from Clawdbot — 4 operation(s) for packages.
  name: Clawdbot Packages API
  slug: clawdbot-packages-api
- baseURL: https://clawhub.ai
  baseurl_source: declared
  description: The Plugins API from Clawdbot — 1 operation(s) for plugins.
  name: Clawdbot Plugins API
  slug: clawdbot-plugins-api
- baseURL: https://clawhub.ai
  baseurl_source: declared
  description: The Skills API from Clawdbot — 5 operation(s) for skills.
  name: Clawdbot Skills API
  slug: clawdbot-skills-api
- baseURL: https://clawhub.ai
  baseurl_source: declared
  description: The Transfers API from Clawdbot — 1 operation(s) for transfers.
  name: Clawdbot Transfers API
  slug: clawdbot-transfers-api
- baseURL: https://clawhub.ai
  baseurl_source: declared
  description: The Users API from Clawdbot — 1 operation(s) for users.
  name: Clawdbot Users API
  slug: clawdbot-users-api
artifact_total: 10
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/clawdbot/refs/heads/main/rules/clawdbot-rules.yml
  title: ''
  type: Spectral
  url: rules/clawdbot-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/clawdbot/refs/heads/main/conformance/clawdbot-conformance.yml
  title: ''
  type: Conformance
  url: conformance/clawdbot-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/clawdbot/refs/heads/main/llms/clawdbot-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/clawdbot-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/clawdbot/refs/heads/main/well-known/clawdbot-clawhub-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/clawdbot-clawhub-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/clawdbot/refs/heads/main/well-known/clawdbot-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/clawdbot-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/clawdbot/refs/heads/main/hosts/clawdbot-hosts.yml
  title: ''
  type: Hosts
  url: hosts/clawdbot-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/clawdbot/refs/heads/main/vendors/clawdbot-vendors.yml
  title: ''
  type: Vendors
  url: vendors/clawdbot-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://openclaw.ai/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://openclaw.ai/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://openclaw.ai/press
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/openclaw/openclaw/releases/download/v2026.9.9/OpenClaw-2026.9.9.zip
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.openclaw.ai/start/getting-started
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/clawdbot/refs/heads/main/security/clawdbot-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/clawdbot-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/clawdbot/refs/heads/main/security/clawdbot-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/clawdbot-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://openclaw.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.openclaw.ai
- group: docs
  title: ''
  type: APIReference
  url: https://docs.openclaw.ai
- group: company
  title: ''
  type: Blog
  url: https://openclaw.ai/blog
- group: build
  title: ''
  type: Integration
  url: https://openclaw.ai/integrations
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: null
    url: https://docs.openclaw.ai/mcp
  - status: 200
    url: https://openclaw.ai
  - status: 403
    url: https://equityzen.com/company/clawdbot
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-08'
description: Clawdbot is an open‑source personal AI assistant that runs locally on your devices. It integrates with WhatsApp, Telegram, Slack, Discord, Google Chat, Signal, iMessage, Microsoft Teams and WebChat to automate email, calendar, flight check‑ins and more, all while keeping your data private.
image: https://openclaw.ai/og-image.png
layout: provider
modified: '2026-10-08'
name: Clawdbot
nav: Providers
network: true
overview: 'Clawdbot is listed with 7 APIs on the [APIs.io](https://apis.io/) network, including Clawdbot API, Npm API, Packages API, and 4 more. Tagged areas include Company, Artificial Intelligence, Open Source, PersonalAssistant, and Automation.


  The Clawdbot catalog on APIs.io includes 1 Spectral governance ruleset.


  Clawdbot''s developer surface includes changelog, getting-started guide, documentation, API reference, engineering blog, and 14 more developer resources.'
random_paper: 12
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Clawdbot API Rules
  rule_count: 10
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 0
  slug: clawdbot-rules
score:
  band: emerging
  composite: 25.1
  coverage:
    artifact_dirs: 9
    catalog_earned: 43.8
    catalog_earned_first_party: 0.0
    catalog_gap: 71.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 15.9
    contract_quality: 14.1
    developer_ergonomics: 31.0
    discoverability: 80.4
    operational_transparency: 26.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 8
      marker_coverage: 100.0
      total: 8
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: domain-security
  name: Clawdbot Domain Security
  slug: clawdbot-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Clawdbot Vulnerability Disclosure
  slug: clawdbot-vulnerability-disclosure
  summary_line: no policy recorded
slug: clawdbot
tags:
- Company
- Artificial Intelligence
- Open Source
- PersonalAssistant
- Automation
website: https://openclaw.ai
---
