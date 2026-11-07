---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
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
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 6.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for dot•requirements platform providing AI‑native requirements management.
  name: dotrequirements API
  slug: dotrequirements-api
artifact_total: 2
common:
- group: build
  href: https://artifacts.apis.io/dotrequirements-io/cli/dotrequirements-io-cli.yml
  title: ''
  type: CLI
  url: cli/dotrequirements-io-cli.yml
- group: agent
  href: https://artifacts.apis.io/dotrequirements-io/llms/dotrequirements-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dotrequirements-io-llms.txt
- group: agent
  href: https://artifacts.apis.io/dotrequirements-io/well-known/dotrequirements-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dotrequirements-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/dotrequirements-io/hosts/dotrequirements-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dotrequirements-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/dotrequirements-io/vendors/dotrequirements-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dotrequirements-io-vendors.yml
- group: build
  href: https://artifacts.apis.io/dotrequirements-io/packages/dotrequirements-io-packages.yml
  title: ''
  type: SDKs
  url: packages/dotrequirements-io-packages.yml
- group: build
  href: https://artifacts.apis.io/dotrequirements-io/packages/dotrequirements-io-packages.yml
  title: ''
  type: Packages
  url: packages/dotrequirements-io-packages.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://app.dotrequirements.io/privacy
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.dotrequirements.io/getting-started
- group: auth
  href: https://artifacts.apis.io/dotrequirements-io/security/dotrequirements-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dotrequirements-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dotrequirements.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.dotrequirements.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.dotrequirements.io
- group: company
  title: ''
  type: Blog
  url: https://discovery.dotrequirements.io
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://app.dotrequirements.io/mcp
  - status: 200
    url: https://dotrequirements.io/
  reason: partner-login
  state: gated
created: '2026-11-05'
description: dot•requirements (legal name Popover AI Ltd) provides AI‑native, readable, testable requirements that live alongside your code. The platform lets developers write, version, and validate software requirements using natural‑language prompts, integrates with CI/CD pipelines, and offers a sandbox for testing requirement coverage. It aims to improve test coverage, traceability, and collaboration across teams, supporting both open‑source and enterprise workflows.
image: https://dotrequirements.io/DotReq-LinkPreview.png
layout: provider
modified: '2026-11-05'
name: dot•requirements
nav: Providers
network: true
overview: 'dot•requirements is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Requirements, AI-native, Developer Tools, and Software Development.


  dot•requirements'' developer surface includes CLI, getting-started guide, documentation, engineering blog, and 10 more developer resources.'
random_paper: 8
score:
  band: emerging
  composite: 15.6
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 47.6
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dotrequirements Io Domain Security
  slug: dotrequirements-io-domain-security
  summary_line: TLSv1.3 · HSTS
slug: dotrequirements-io
tags:
- Requirements
- AI-native
- Developer Tools
- Software Development
website: https://dotrequirements.io/
---
