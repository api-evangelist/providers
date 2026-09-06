---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 6.0
  scored_at: '2026-09-05'
api_count: 2
apis:
- description: The encore.app configuration file is the canonical declaration of an Encore application, including its platform application ID, primary language, global CORS rules, and authenticator settings. The JSO
  name: Encore Application Configuration
  slug: encore-application-config
- description: The Encore CLI provides commands for creating, running, building, testing, deploying, and operating Encore applications. It also generates type-safe API clients in Go, TypeScript, JavaScript, and expe
  name: Encore CLI
  slug: encore-cli
artifact_total: 10
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/encoredev/encore/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/encoredev/encore/releases
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/encoredev/encore/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/encoredev/encore/blob/main/CONTRIBUTING.md
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/encore-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/encore-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/encore
- group: company
  title: ''
  type: Website
  url: https://encore.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://encore.dev/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://encore.dev/docs/ts/quick-start
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/encoredev
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/encoredev/encore
- group: company
  title: ''
  type: Blog
  url: https://encore.dev/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://encore.dev/pricing
- group: operate
  title: ''
  type: Discord
  url: https://encore.dev/discord
- group: commercial
  title: ''
  type: License
  url: https://github.com/encoredev/encore/blob/main/LICENSE
- group: agent
  title: ''
  type: MCPServer
  url: https://encore.dev/blog/mcp-server
- group: agent
  title: ''
  type: LlmsText
  url: https://encore.dev/llms.txt
created: '2026-03-26'
description: Encore is an open source development platform for building type-safe, production-ready backend applications and distributed systems. It supports Go and TypeScript, provides built-in infrastructure automation for databases, caches, pub/sub, and cron jobs, and includes a local development dashboard with automatic API documentation, distributed tracing, and OpenAPI client generation.
finops:
- name: Encore Finops
  service_category: API
  slug: encore-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/encore.png
json_schemas:
- name: Encore App Configuration
  property_count: 6
  slug: encore-app-configuration
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: Encore
nav: Providers
network: true
overview: 'Encore publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Backend, Cloud-Native, Frameworks, Go, and Infrastructure Automation.


  The Encore catalog on APIs.io includes 1 Spectral governance ruleset.


  Encore''s developer surface includes documentation, getting-started guide, engineering blog, pricing, and 14 more developer resources.'
plans:
- name: Encore Plans Pricing
  plan_count: 3
  slug: encore-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 5
  name: Encore Rate Limits
  slug: encore-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Encore API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: encore-jsonschema-spectral-rules
score:
  band: emerging
  composite: 24.2
  coverage:
    artifact_dirs: 9
    catalog_earned: 50.3
    catalog_earned_first_party: 0.0
    catalog_gap: 64.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 9.8
    contract_quality: 8.0
    developer_ergonomics: 28.6
    discoverability: 66.7
    governance: 9.8
    operational_transparency: 26.3
  previous_composite: 24.2
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/encore/refs/heads/main/screenshots/encore-2026-06-20T180722.png
security:
- kind: domain-security
  name: Encore Domain Security
  slug: encore-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Encore Vulnerability Disclosure
  slug: encore-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: encore
tags:
- Backend
- Cloud-Native
- Frameworks
- Go
- Infrastructure Automation
- Microservices
- Open-Source
- TypeScript
website: https://encore.dev/
---
