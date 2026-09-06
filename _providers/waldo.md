---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - '{''url'': ''https://www.waldo.com/'', ''status'': 301, ''note'': ''declared website redirects to https://www.tricentis.com/ — a different registrable domain (waldo.com -> tricentis.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
agent_readiness:
  band: human-only
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
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: W3C WebDriver + Appium-compatible endpoint for creating sessions on Waldo cloud devices and driving native, hybrid, and mobile-web apps programmatically.
  name: Waldo Scripting (Core) API
  slug: waldo-scripting-core-api
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://www.waldo.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.waldo.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.waldo.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.waldo.com/reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.waldo.com/docs/waldo-cli
- group: commercial
  title: ''
  type: Pricing
  url: https://www.waldo.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.waldo.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/waldoapp
- group: start
  title: ''
  type: SignUp
  url: https://app.waldo.com/
- group: build
  title: ''
  type: Packages
  url: packages/waldo-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/waldo-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/waldo-cli.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/waldo-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/waldo-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/waldo-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/waldo-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/waldo-llms.txt
created: '2026-07-17'
description: Waldo is a no-code mobile test automation platform for iOS and Android that lets any team member create, run, and maintain reliable end-to-end tests on a cloud of virtual devices (iOS simulators and Android emulators) with zero device setup. Its Scripting (Core) API exposes a W3C WebDriver and Appium-compatible endpoint at core.waldo.com so engineers can programmatically create sessions on cloud devices and drive native, hybrid, and mobile-web apps, capturing video replays, logs, and network calls. Build upload runs through a Go CLI, GitHub Actions, Bitrise, and a fastlane plugin. Waldo was acquired by Tricentis in July 2023 and is part of the Tricentis mobile testing portfolio.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/waldo.png
layout: provider
modified: '2026-07-21'
name: Waldo
nav: Providers
network: true
overview: 'Waldo publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, DevOps, Testing, Mobile, and Test Automation.


  Waldo''s developer surface includes documentation, API reference, getting-started guide, pricing, engineering blog, signup flow, CLI, and 10 more developer resources.'
random_paper: 10
score:
  band: emerging
  composite: 17.9
  coverage:
    artifact_dirs: 9
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 17.9
  provenance:
    conformance: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/waldo/refs/heads/main/screenshots/waldo-2026-09-02T170405.png
security:
- kind: authentication
  name: Waldo Authentication
  slug: waldo-authentication
  summary_line: apiKey · 1 scheme
slug: waldo
tags:
- Company
- DevOps
- Testing
- Mobile
- Test Automation
- Quality Engineering
- WebDriver
- Appium
- CI/CD
website: https://www.waldo.com/
---
