---
access_model:
  confidence: high
  label: Free and open source
  onboarding: unknown
  pricing: free
  public: true
  source:
  - license
  - plans
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
  scored_at: '2026-09-23'
api_count: 1
apis:
- description: 'Dredd is a language-agnostic command-line tool for validating an API description document against a backend implementation. It supports API Blueprint, OpenAPI 2.0, and OpenAPI 3.0, and provides hooks '
  name: Dredd
  slug: dredd
artifact_total: 5
common:
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/apiaryio/dredd/blob/master/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/apiaryio/dredd/blob/master/LICENSE
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/dredd/refs/heads/main/security/dredd-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dredd-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dredd.org
- group: docs
  title: ''
  type: Documentation
  url: https://dredd.org/en/latest/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apiaryio
- group: start
  title: ''
  type: GettingStarted
  url: https://dredd.org/en/latest/quickstart/
- group: operate
  title: ''
  type: Support
  url: https://github.com/apiaryio/dredd/issues
- group: other
  title: ''
  type: DockerImage
  url: https://hub.docker.com/r/apiaryio/dredd
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/dredd/refs/heads/main/packages/dredd-packages.yml
  title: ''
  type: Packages
  url: packages/dredd-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/dredd/refs/heads/main/packages/dredd-packages.yml
  title: ''
  type: SDKs
  url: packages/dredd-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/dredd/refs/heads/main/cli/dredd-cli.yml
  title: ''
  type: CLI
  url: cli/dredd-cli.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/dredd/refs/heads/main/changelog/dredd-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/dredd-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/dredd/refs/heads/main/lifecycle/dredd-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/dredd-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/dredd/refs/heads/main/conventions/dredd-conventions.yml
  title: ''
  type: Conventions
  url: conventions/dredd-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/dredd/refs/heads/main/conformance/dredd-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dredd-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/dredd/refs/heads/main/llms/dredd-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dredd-llms.txt
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/dredd/refs/heads/main/plans/dredd-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dredd-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/dredd/refs/heads/main/rate-limits/dredd-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/dredd-rate-limits.yml
created: '2026-03-25'
description: Dredd is a language-agnostic, MIT-licensed open source command-line tool that validates a running HTTP API against its own API description document. It compiles every request/response pair documented in an API Blueprint, OpenAPI 2.0 or (experimentally) OpenAPI 3.0 file into an HTTP transaction, calls the API under test, and reports where the implementation and the documentation disagree. Hooks written in Node.js, Ruby, Python, PHP, Perl, Go or Rust handle per-transaction test setup and teardown, and pluggable reporters (xunit, dot, markdown, html) wire it into CI. Dredd publishes no API of its own — it is a client you install and run. The project has been archived and unmaintained since November 2024; the last release, 14.1.0, shipped in November 2021.
finops:
- name: Dredd Finops
  service_category: API
  slug: dredd-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dredd.png
layout: provider
modified: '2026-09-13'
name: Dredd
nav: Providers
network: true
overview: 'Dredd publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Contract Testing, API Testing, OpenAPI, API Blueprint, and Tooling.


  Dredd''s developer surface includes documentation, getting-started guide, support, CLI, changelog, and 14 more developer resources.'
plans:
- name: Dredd Plans Pricing
  plan_count: 0
  slug: dredd-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Dredd Rate Limits
  slug: dredd-rate-limits
score:
  band: emerging
  composite: 20.2
  coverage:
    artifact_dirs: 14
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 7.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 40.5
    discoverability: 59.3
    operational_transparency: 18.4
  previous_composite: 20.2
  provenance:
    conformance: first-party
  schema_version: 0.22.0
  scored_at: '2026-09-23'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/dredd/refs/heads/main/screenshots/dredd-2026-06-20T180221.png
security:
- kind: domain-security
  name: Dredd Domain Security
  slug: dredd-domain-security
  summary_line: TLSv1.3
slug: dredd
tags:
- Contract Testing
- API Testing
- OpenAPI
- API Blueprint
- Tooling
- Developer Tools
- Command Line
- Continuous Integration
- JSON-Schema
- Open-Source
website: https://dredd.org
---
