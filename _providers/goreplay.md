---
access_model:
  confidence: high
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - pricing
  trial: false
  try_now: false
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-09-21'
api_count: 1
apis:
- description: 'GoReplay captures live HTTP traffic with libpcap and replays it against a test target, letting teams validate deploys, configuration changes and infrastructure changes against real production traffic '
  name: GoReplay
  slug: goreplay-tool
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://goreplay.org
- group: docs
  title: ''
  type: Documentation
  url: https://goreplay.org/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://goreplay.org/docs/installation/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/probelabs/goreplay
- group: operate
  title: ''
  type: Support
  url: https://github.com/probelabs/goreplay/issues
- group: company
  title: ''
  type: Blog
  url: https://goreplay.org/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://goreplay.org/pro/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://github.com/probelabs/goreplay/blob/master/COMM-LICENSE
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/goreplay/refs/heads/main/cli/goreplay-cli.yml
  title: ''
  type: CLI
  url: cli/goreplay-cli.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/goreplay/refs/heads/main/packages/goreplay-packages.yml
  title: ''
  type: Packages
  url: packages/goreplay-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/goreplay/refs/heads/main/llms/goreplay-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/goreplay-llms.txt
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/goreplay/refs/heads/main/changelog/goreplay-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/goreplay-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/goreplay/refs/heads/main/lifecycle/goreplay-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/goreplay-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/goreplay/refs/heads/main/conventions/goreplay-conventions.yml
  title: ''
  type: Conventions
  url: conventions/goreplay-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/goreplay/refs/heads/main/conformance/goreplay-conformance.yml
  title: ''
  type: Conformance
  url: conformance/goreplay-conformance.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/goreplay/refs/heads/main/plans/goreplay-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/goreplay-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/goreplay/refs/heads/main/rate-limits/goreplay-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/goreplay-rate-limits.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/goreplay/refs/heads/main/security/goreplay-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/goreplay-domain-security.yml
created: '2026-03-26'
description: GoReplay is an open source network traffic capture and replay tool, distributed as a single `gor` binary under LGPL-3.0, that records live HTTP traffic on a server and replays it against another environment for shadow testing, load testing with real production traffic, and debugging. It sits off the critical path rather than acting as a proxy, captures via libpcap without application changes, and can filter, rewrite or hand each message to external middleware before replay. A commercial GoReplay PRO edition ($2,950/year) adds Amazon S3 capture storage, binary protocol support, keep-alive TCP session recognition and dedicated support. GoReplay publishes no HTTP API of its own; its machine-readable contract is the CLI flag surface plus a documented middleware STDIN/STDOUT wire protocol.
finops:
- name: Goreplay Finops
  service_category: API
  slug: goreplay-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/goreplay.png
layout: provider
modified: '2026-09-13'
name: GoReplay
nav: Providers
network: true
overview: 'GoReplay publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include API Testing, HTTP Traffic, Load Testing, Network Capture, and Open-Source.


  GoReplay''s developer surface includes documentation, getting-started guide, support, engineering blog, pricing, CLI, changelog, and 11 more developer resources.'
plans:
- name: Goreplay Plans Pricing
  plan_count: 2
  slug: goreplay-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Goreplay Rate Limits
  slug: goreplay-rate-limits
score:
  band: thin
  composite: 28.4
  coverage:
    artifact_dirs: 16
    catalog_earned: 43.0
    catalog_earned_first_party: 8.0
    catalog_gap: 72.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 66.7
    operational_transparency: 18.4
  previous_composite: 28.4
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.22.0
  scored_at: '2026-09-21'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/goreplay/refs/heads/main/screenshots/goreplay-2026-06-20T182250.png
security:
- kind: domain-security
  name: Goreplay Domain Security
  slug: goreplay-domain-security
  summary_line: TLSv1.3 · HSTS
slug: goreplay
tags:
- API Testing
- HTTP Traffic
- Load Testing
- Network Capture
- Open-Source
- Traffic Replay
website: https://goreplay.org
---
