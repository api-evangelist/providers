---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 12.0
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 2
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/21dotco/two1-python/issues
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/21dotco/two1-python/blob/master/CONTRIBUTING.md
- group: company
  title: ''
  type: Website
  url: https://earn.com/
- group: other
  title: ''
  type: Successor
  url: https://www.coinbase.com/earn
- group: auth
  title: ''
  type: DomainSecurity
  url: security/earncom-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/21dotco
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/21dotco/two1-python
- group: build
  title: ''
  type: Packages
  url: packages/earncom-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/earncom-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/earncom-cli.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/earncom-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/earncom-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/earncom-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/earncom-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/earncom-error-codes.yml
created: '2026-07-17'
description: Earn.com was a cryptocurrency startup founded in 2013 as 21e6 and later known as 21 Inc and 21.co, backed by a16z and others, which raised over $116 million. It began as a Bitcoin mining venture selling the 21 Bitcoin Computer, then pivoted to a paid-messaging marketplace where senders paid recipients in cryptocurrency to read and reply to email. Coinbase acquired Earn.com in April 2018 for a reported $120 million, and co-founder Balaji Srinivasan became Coinbase's first Chief Technology Officer. The standalone Earn.com product was retired and the brand was folded into Coinbase Earn, the learn-and-earn program. As of July 2026 the earn.com domain issues a blanket HTTP 301 redirect for every path to https://www.coinbase.com/earn, and no developer, documentation, or API subdomain resolves. Earn.com therefore has no independent API surface; any remaining API capability lives under Coinbase.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/earncom.png
layout: provider
modified: '2026-07-20'
name: Earn.com
nav: Providers
network: true
overview: 'Earn.com is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cryptocurrency, Bitcoin, Payments, and Acquired.


  Earn.com''s developer surface includes CLI, changelog, authentication, and 12 more developer resources.'
random_paper: 145
score:
  band: minimal
  composite: 10.6
  delta: -2.9
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 18.4
  previous_composite: 13.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 18.8
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/earncom/refs/heads/main/screenshots/earncom-2026-07-25T212653.png
security:
- kind: authentication
  name: Earncom Authentication
  slug: earncom-authentication
  summary_line: http/custom-signature · 2 schemes
- kind: domain-security
  name: Earncom Domain Security
  slug: earncom-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: earncom
tags:
- Company
- Cryptocurrency
- Bitcoin
- Payments
- Acquired
- Defunct
- Messaging
website: https://earn.com/
---
