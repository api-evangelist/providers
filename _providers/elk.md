---
access_model:
  confidence: high
  label: Free / Open Source
  onboarding: unknown
  pricing: free
  public: true
  source:
  - plans
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 15.0
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: 'Elk''s own server surface, served by its Nuxt runtime at https://elk.zone/api. Four endpoints: list the Mastodon-compatible instances offered in the sign-in picker, build the instance authorize URL, co'
  name: Elk Client API
  slug: elk-client-api
artifact_total: 8
common:
- group: operate
  title: ''
  type: Releases
  url: https://github.com/elk-zone/elk/releases
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/elk-zone/elk/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/elk-zone/elk/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/elk-zone/elk/blob/main/LICENSE
- group: auth
  title: ''
  type: DomainSecurity
  url: security/elk-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://elk.zone
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/elk-zone
- group: operate
  title: ''
  type: Support
  url: https://github.com/elk-zone/elk/issues
- group: docs
  title: ''
  type: Documentation
  url: https://docs.elk.zone
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.elk.zone/guide
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://docs.elk.zone/privacy
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/elk-zone/elk/releases
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/elk-changelog.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/elk-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Packages
  url: packages/elk-packages.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/elk-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/elk-plans-pricing.yml
created: '2024-01-01'
description: 'Elk is a nimble, MIT-licensed Mastodon web client maintained by Anthony Fu, Daniel Roe, Kevin Deng and Patak. It runs as a Nuxt 4 progressive web app at elk.zone and connects to any Mastodon-compatible instance the user chooses, speaking the Mastodon Client API through Masto.js with WebSocket streaming and Web Push notifications. Elk sells no API product and issues no credential of its own: its small server surface at elk.zone/api exists to list sign-in instances and broker the OAuth 2.0 handshake with the user''s own server, and every timeline, post and notification call goes to that instance directly.'
finops:
- name: Elk Finops
  service_category: API
  slug: elk-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/elk.png
layout: provider
modified: '2026-08-27'
name: Elk
nav: Providers
network: true
overview: 'Elk publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Fediverse, Mastodon, Open-Source, Social Networking, and Social-Media.


  Elk''s developer surface includes support, documentation, getting-started guide, changelog, and 14 more developer resources.'
plans:
- name: Elk Plans Pricing
  plan_count: 0
  slug: elk-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Elk Rate Limits
  slug: elk-rate-limits
scopes:
- name: Elk Scopes
  scope_count: 0
  slug: elk-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 29.6
  coverage:
    artifact_dirs: 17
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 18.4
    commercial_clarity: 18.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 45.2
    discoverability: 83.3
    governance: 18.2
    operational_transparency: 18.4
  open_source:
    applies: true
    score: 65.0
  previous_composite: 29.6
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/elk/refs/heads/main/screenshots/elk-2026-06-20T180618.png
security:
- kind: authentication
  name: Elk Authentication
  slug: elk-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Elk Domain Security
  slug: elk-domain-security
  summary_line: TLSv1.3
- kind: vulnerability-disclosure
  name: Elk Vulnerability Disclosure
  slug: elk-vulnerability-disclosure
  summary_line: Hackerone
slug: elk
tags:
- Fediverse
- Mastodon
- Open-Source
- Social Networking
- Social-Media
- Web-Client
- Progressive Web App
- Authentication
website: https://elk.zone
---
