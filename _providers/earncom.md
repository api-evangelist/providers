---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  - '{''url'': ''https://earn.com/'', ''status'': 301, ''note'': ''declared website redirects to https://www.coinbase.com/earn?claim=true — a different registrable domain (earn.com -> coinbase.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 5.4
  scored_at: '2026-09-14'
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
  href: https://raw.githubusercontent.com/api-evangelist/earncom/refs/heads/main/security/earncom-domain-security.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/earncom/refs/heads/main/packages/earncom-packages.yml
  title: ''
  type: Packages
  url: packages/earncom-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/earncom/refs/heads/main/packages/earncom-packages.yml
  title: ''
  type: SDKs
  url: packages/earncom-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/earncom/refs/heads/main/cli/earncom-cli.yml
  title: ''
  type: CLI
  url: cli/earncom-cli.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/earncom/refs/heads/main/changelog/earncom-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/earncom-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/earncom/refs/heads/main/lifecycle/earncom-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/earncom-lifecycle.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/earncom/refs/heads/main/authentication/earncom-authentication.yml
  title: ''
  type: Authentication
  url: authentication/earncom-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/earncom/refs/heads/main/conventions/earncom-conventions.yml
  title: ''
  type: Conventions
  url: conventions/earncom-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/earncom/refs/heads/main/errors/earncom-error-codes.yml
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
random_paper: 6
score:
  band: minimal
  composite: 10.6
  coverage:
    artifact_dirs: 10
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 50.0
    operational_transparency: 18.4
  previous_composite: 10.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 18.8
  schema_version: 0.22.0
  scored_at: '2026-09-14'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
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
