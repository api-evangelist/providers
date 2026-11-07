---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
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
  score: 30.9
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 10
common:
- group: commercial
  href: https://artifacts.apis.io/codspeed/plans/codspeed-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/codspeed-plans-pricing.yml
- group: company
  title: ''
  type: BlogRSS
  url: https://codspeed.io/blog/feed/rss.xml
- group: company
  title: ''
  type: Website
  url: https://codspeed.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.codspeed.io/
- group: docs
  title: ''
  type: Documentation
  url: https://codspeed.io/docs
- group: docs
  title: ''
  type: APIReference
  url: https://codspeed.io/docs/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://codspeed.io/docs/quickstart
- group: company
  title: ''
  type: Blog
  url: https://codspeed.io/blog
- group: operate
  title: ''
  type: Support
  url: mailto:support@codspeed.io
- group: operate
  title: ''
  type: Community
  url: https://discord.gg/MxpaCfKSqF
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CodSpeedHQ
- group: commercial
  title: ''
  type: Pricing
  url: https://codspeed.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.codspeed.io/login?flow=get-started
- group: start
  title: ''
  type: Login
  url: https://app.codspeed.io/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://codspeed.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://codspeed.io/privacy
- group: operate
  title: ''
  type: ChangeLog
  url: https://codspeed.io/changelog
- group: operate
  href: https://artifacts.apis.io/codspeed/changelog/codspeed-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/codspeed-changelog.yml
- group: agent
  href: https://artifacts.apis.io/codspeed/mcp/codspeed-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/codspeed-mcp.yml
- group: agent
  href: https://artifacts.apis.io/codspeed/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://artifacts.apis.io/codspeed/packages/codspeed-packages.yml
  title: ''
  type: Packages
  url: packages/codspeed-packages.yml
- group: build
  href: https://artifacts.apis.io/codspeed/packages/codspeed-packages.yml
  title: ''
  type: SDKs
  url: packages/codspeed-packages.yml
- group: build
  href: https://artifacts.apis.io/codspeed/cli/codspeed-cli.yml
  title: ''
  type: CLI
  url: cli/codspeed-cli.yml
- group: agent
  href: https://artifacts.apis.io/codspeed/llms/codspeed-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/codspeed-llms.txt
- group: auth
  href: https://artifacts.apis.io/codspeed/authentication/codspeed-authentication.yml
  title: ''
  type: Authentication
  url: authentication/codspeed-authentication.yml
- group: design
  href: https://artifacts.apis.io/codspeed/conformance/codspeed-conformance.yml
  title: ''
  type: Conformance
  url: conformance/codspeed-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.codspeed.io
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.codspeed.io
- group: auth
  title: ''
  type: Security
  url: https://codspeed.io/docs/security
- group: auth
  href: https://artifacts.apis.io/codspeed/security/codspeed-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/codspeed-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/codspeed/security/codspeed-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/codspeed-domain-security.yml
created: '2026-07-17'
description: CodSpeed is a continuous performance testing and optimization platform that automatically detects performance regressions in pull requests and proposes autonomous optimizations. It runs benchmarks with sub-1% variance inside CI (GitHub Actions, GitLab CI, Buildkite), generates differential flamegraphs to pinpoint the exact lines that degraded, and gates PRs that fail performance standards. CodSpeed supports Rust, C++, Go, Java, Python, and Node.js via first-party harnesses (pytest-codspeed, cargo-codspeed / codspeed-rust, google_benchmark, JMH, vitest, tinybench, benchmark.js), CPU-simulation, walltime, and memory instruments, plus MongoDB database instrumentation. It ships an open-source CLI, a GitHub Action, a hosted MCP server, and packaged Agent Skills so AI coding assistants can investigate regressions and optimize code directly. CodSpeed is a Techstars-backed company.
finops:
- has_sources: true
  method: derived
  name: Codspeed Finops
  primary_unit: user
  service_category: ''
  slug: codspeed-finops
  template: false
image: https://codspeed.io/logo.svg
layout: provider
mcp_servers:
- description: Hosted, remote MCP server that gives AI-powered coding tools direct access to CodSpeed performance data (benchmark runs, comparisons, flamegraphs) so agents can investigate regressions and optimize co
  name: CodSpeed MCP Server
  slug: codspeed
modified: '2026-10-06'
name: CodSpeed
nav: Providers
network: true
overview: 'CodSpeed is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Performance, Benchmarking, Continuous Integration, and Developer Tools.


  CodSpeed''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, signup flow, and 24 more developer resources.'
plans:
- name: Codspeed Plans Pricing
  plan_count: 3
  slug: codspeed-plans-pricing
- name: Codspeed Price Estimates
  plan_count: 0
  slug: codspeed-price-estimates
random_paper: 23
score:
  band: developing
  composite: 43.4
  coverage:
    artifact_dirs: 17
    catalog_earned: 42.0
    catalog_earned_first_party: 12.0
    catalog_gap: 73.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 64.3
    discoverability: 58.3
    operational_transparency: 28.9
  previous_composite: 43.4
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/codspeed/codspeed-2026-07-25T205952.png
security:
- kind: authentication
  name: Codspeed Authentication
  slug: codspeed-authentication
  summary_line: oauth2/oidc/token/github-app · 4 schemes
- kind: domain-security
  name: Codspeed Domain Security
  slug: codspeed-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Codspeed Vulnerability Disclosure
  slug: codspeed-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Codspeed Trust Center
  slug: codspeed-trust-center
  summary_line: SOC 2 Type II
skill_count: 2
skills:
- name: codspeed-optimize
  slug: codspeed-optimize
- name: codspeed-setup-harness
  slug: codspeed-setup-harness
slug: codspeed
tags:
- Company
- Performance
- Benchmarking
- Continuous Integration
- Developer Tools
- Observability
- Testing
- DevOps
- Artificial Intelligence
- MCP
website: https://codspeed.io/
---
