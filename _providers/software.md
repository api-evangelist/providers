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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Read-only enterprise engineering-metrics API exposed as a hosted Model Context Protocol (MCP) server over Streamable HTTP. AI assistants and agents query contributor metrics, identity groups, and tren
  name: Antenna Enterprise Metrics API
  slug: antenna-enterprise-metrics-api
artifact_total: 9
common:
- group: commercial
  href: https://artifacts.apis.io/software/plans/software-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/software-plans-pricing.yml
- group: company
  title: ''
  type: Website
  url: https://antenna.dev
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.antenna.dev
- group: docs
  title: ''
  type: Documentation
  url: https://docs.antenna.dev
- group: docs
  title: ''
  type: APIReference
  url: https://docs.antenna.dev/mcp-server
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.antenna.dev/get-started/quickstart
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/swdotcom
- group: operate
  title: ''
  type: StatusPage
  url: https://status.antenna.dev
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.antenna.dev/changelog
- group: operate
  href: https://artifacts.apis.io/software/changelog/software-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/software-changelog.yml
- group: start
  title: ''
  type: SignUp
  url: https://app.antenna.dev/signup
- group: operate
  title: ''
  type: Support
  url: mailto:support@antenna.dev
- group: commercial
  title: ''
  type: Pricing
  url: https://antenna.dev/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://antenna.dev/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://antenna.dev/legal/privacy
- group: auth
  title: ''
  type: Security
  url: https://antenna.dev/legal/security
- group: auth
  title: ''
  type: TrustCenter
  url: https://antenna.dev/security
- group: auth
  title: ''
  type: Compliance
  url: https://antenna.dev/security
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/antennadev
- group: agent
  href: https://artifacts.apis.io/software/mcp/software-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/software-mcp.yml
- group: auth
  href: https://artifacts.apis.io/software/authentication/software-authentication.yml
  title: ''
  type: Authentication
  url: authentication/software-authentication.yml
- group: build
  href: https://artifacts.apis.io/software/packages/software-packages.yml
  title: ''
  type: Packages
  url: packages/software-packages.yml
- group: design
  href: https://artifacts.apis.io/software/lifecycle/software-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/software-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/software/security/software-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/software-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/software/security/software-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/software-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/software/conformance/software-conformance.yml
  title: ''
  type: Conformance
  url: conformance/software-conformance.yml
- group: agent
  href: https://artifacts.apis.io/software/llms/software-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/software-llms.txt
created: '2026-07-17'
description: Software (software.com) is the developer-productivity company behind the Code Time and Music Time editor plugins, now rebranded and operating as Antenna (antenna.dev). Antenna is an AI-native development intelligence platform — a control plane for AI-driven software development that measures AI-tool adoption, engineering productivity shifts, and financial ROI across an engineering organization. It integrates with AI coding assistants (Claude Code, GitHub Copilot, Cursor, Codex, Gemini Code Assist, Windsurf, Amazon Q Developer, Kiro, Augment Code), Git providers (GitHub, GitLab, Bitbucket, Azure DevOps), Jira, Slack and Microsoft Teams, and exposes a hosted Model Context Protocol (MCP) server so AI agents can query engineering metrics in natural language. Backed by 8vc; reports serving 900K+ developers across 10K+ companies.
finops:
- has_sources: true
  method: derived
  name: Software Finops
  primary_unit: user
  service_category: ''
  slug: software-finops
  template: false
image: https://antenna.dev/opengraph-image.png
layout: provider
mcp_servers:
- description: Hosted Model Context Protocol server that lets AI assistants and agents query an enterprise's engineering metrics directly with natural-language prompts (contributor productivity, AI-tool adoption, te
  name: Antenna MCP
  slug: antenna-mcp
modified: '2026-07-21'
name: Software
nav: Providers
network: true
overview: 'Software is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Developer Productivity, Engineering Intelligence, Artificial Intelligence, and Software Development.


  Software''s developer surface includes documentation, API reference, getting-started guide, changelog, signup flow, support, pricing, and 20 more developer resources.'
plans:
- name: Software Plans Pricing
  plan_count: 7
  slug: software-plans-pricing
- name: Software Price Estimates
  plan_count: 0
  slug: software-price-estimates
random_paper: 11
score:
  band: developing
  composite: 48.4
  coverage:
    artifact_dirs: 14
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.5
  facets:
    access_clarity: 100.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 54.8
    discoverability: 65.0
    operational_transparency: 47.4
  previous_composite: 46.9
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 32.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/software/software-2026-09-02T160100.png
security:
- kind: authentication
  name: Software Authentication
  slug: software-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Software Domain Security
  slug: software-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Software Vulnerability Disclosure
  slug: software-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Software Trust Center
  slug: software-trust-center
  summary_line: SOC 2 Type 2
slug: software
tags:
- Company
- Developer Productivity
- Engineering Intelligence
- Artificial Intelligence
- Software Development
- Analytics
- Metrics
- DORA
- MCP
- Developer Experience
website: https://antenna.dev
---
