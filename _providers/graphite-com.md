---
access_model:
  confidence: high
  label: Freemium (free trial) · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.7
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Graphite Com Agentic Access
  operation_count: 7
  slug: graphite-com-agentic-access
  summary_line: 7 operations · 5 acting
api_count: 1
apis:
- baseURL: https://app.graphite.dev
  baseurl_source: declared
  description: Graphite CLI authentication with a Graphite auth token.
  name: Graphite Authentication API
  slug: graphite-com-authentication-api
- baseURL: https://app.graphite.dev
  baseurl_source: declared
  description: GitHub App install and webhook integration entry points.
  name: Graphite GitHub App API
  slug: graphite-com-github-app-api
- baseURL: https://app.graphite.dev
  baseurl_source: declared
  description: Graphite merge queue actions.
  name: Graphite Merge Queue API
  slug: graphite-com-merge-queue-api
- baseURL: https://app.graphite.dev
  baseurl_source: declared
  description: Create, submit, sync, and merge stacked pull requests via the gt CLI.
  name: Graphite Stacks API
  slug: graphite-com-stacks-api
artifact_total: 20
collections:
- collection_type: open
  name: Graphite Platform Authentication API
  slug: open-graphite-com-authentication-api
- collection_type: open
  name: Graphite Platform Authentication GitHub App API
  slug: open-graphite-com-github-app-api
- collection_type: open
  name: Graphite Platform Authentication Merge Queue API
  slug: open-graphite-com-merge-queue-api
- collection_type: open
  name: Graphite Platform Authentication Stacks API
  slug: open-graphite-com-stacks-api
- collection_type: open
  name: Graphite Platform
  slug: open-graphite-com
common:
- group: other
  href: https://artifacts.apis.io/graphite-com/capabilities/graphite-com-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/graphite-com-capability-edges.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/withgraphite/agent-skills/issues
- group: agent
  href: https://artifacts.apis.io/graphite-com/agentic-access/graphite-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/graphite-com-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/graphite-com/security/graphite-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/graphite-com-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/graphite-com/authentication/graphite-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/graphite-com-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/withgraphite
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/graphite-dev
- group: company
  title: ''
  type: Website
  url: https://graphite.dev
- group: docs
  title: ''
  type: Documentation
  url: https://graphite.com/docs
- group: commercial
  href: https://artifacts.apis.io/graphite-com/plans/graphite-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/graphite-com-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/graphite-com/rate-limits/graphite-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/graphite-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/graphite-com/finops/graphite-com-finops.yml
  title: ''
  type: FinOps
  url: finops/graphite-com-finops.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://graphite.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://graphite.com/docs/get-started
- group: docs
  title: ''
  type: Guides
  url: https://graphite.com/guides
- group: build
  href: https://artifacts.apis.io/graphite-com/cli/graphite-com-cli.yml
  title: ''
  type: CLI
  url: cli/graphite-com-cli.yml
- group: docs
  title: ''
  type: CLIDocumentation
  url: https://graphite.com/docs/command-reference
- group: agent
  href: https://artifacts.apis.io/graphite-com/mcp/graphite-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/graphite-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/graphite-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/graphite-com/llms/graphite-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/graphite-com-llms.txt
- group: build
  href: https://artifacts.apis.io/graphite-com/packages/graphite-com-packages.yml
  title: ''
  type: Packages
  url: packages/graphite-com-packages.yml
- group: design
  href: https://artifacts.apis.io/graphite-com/conventions/graphite-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/graphite-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/graphite-com/conventions/graphite-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/graphite-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/graphite-com/lifecycle/graphite-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/graphite-com-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.graphite.com
- group: operate
  href: https://artifacts.apis.io/graphite-com/changelog/graphite-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/graphite-com-changelog.yml
- group: design
  href: https://artifacts.apis.io/graphite-com/conformance/graphite-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/graphite-com-conformance.yml
- group: auth
  href: https://artifacts.apis.io/graphite-com/security/graphite-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/graphite-com-trust-center.yml
- group: auth
  title: ''
  type: Security
  url: https://graphite.com/docs/privacy-and-security
- group: auth
  href: https://artifacts.apis.io/graphite-com/security/graphite-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/graphite-com-vulnerability-disclosure.yml
- group: company
  title: ''
  type: Blog
  url: https://graphite.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://graphite.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.graphite.com/signup
- group: start
  title: ''
  type: Login
  url: https://app.graphite.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://graphite.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://graphite.com/privacy
- group: operate
  title: ''
  type: Support
  url: mailto:support@graphite.com
- group: operate
  title: ''
  type: Community
  url: https://community.graphite.com
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/withgraphite/agent-skills
- group: other
  title: ''
  type: Customers
  url: https://graphite.com/customers
- group: company
  title: ''
  type: Careers
  url: https://graphite.com/careers
- group: company
  title: ''
  type: Twitter
  url: https://x.com/graphite
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@withgraphite
created: '2026-06-20'
description: Graphite is a code review platform built on top of GitHub for stacking pull requests, AI code review, and merging at scale. The gt CLI creates and submits stacked PRs, Graphite Agent (Diamond) provides codebase-aware AI review and chat, and a merge queue batches and tests PRs in parallel. Graphite has no standalone public REST API - it integrates through a GitHub App that consumes GitHub webhooks, the gt CLI (authenticated with a Graphite token), the GT MCP server, and label / GitHub-mediated integrations (Slack, Linear, external merge queue).
finops:
- has_sources: true
  method: derived
  name: Graphite Com Finops
  primary_unit: user/month, billed annually
  service_category: ''
  slug: graphite-com-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/graphite-com.png
layout: provider
mcp_servers:
- description: Local (stdio) MCP server.
  name: GT MCP server
  slug: graphite
modified: '2026-08-04'
name: Graphite
nav: Providers
network: true
overview: 'Graphite publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Authentication API, GitHub App API, Merge Queue API, and 1 more. Tagged areas include Code Review, Stacked PRs, Merge Queue, AI Code Review, and Developer Tools.


  Graphite''s developer surface includes authentication, documentation, getting-started guide, CLI, changelog, engineering blog, pricing, and 36 more developer resources.'
plans:
- name: Graphite Com Plans Pricing
  plan_count: 4
  slug: graphite-com-plans-pricing
- name: Graphite Com Price Estimates
  plan_count: 0
  slug: graphite-com-price-estimates
random_paper: 16
rate_limits:
- limit_count: 4
  name: Graphite Com Rate Limits
  slug: graphite-com-rate-limits
score:
  band: strong
  composite: 63.8
  coverage:
    artifact_dirs: 23
    catalog_earned: 55.0
    catalog_earned_first_party: 12.0
    catalog_gap: 60.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.6
  facets:
    access_clarity: 92.1
    contract_governance: 18.2
    contract_quality: 48.8
    developer_ergonomics: 71.4
    discoverability: 65.0
    operational_transparency: 55.3
  previous_composite: 62.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/graphite-com/graphite-com-2026-06-20T182329.png
security:
- kind: authentication
  name: Graphite Com Authentication
  slug: graphite-com-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Graphite Com Domain Security
  slug: graphite-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Graphite Com Vulnerability Disclosure
  slug: graphite-com-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Graphite Com Trust Center
  slug: graphite-com-trust-center
  summary_line: SOC 2 Type II
skill_count: 1
skills:
- name: graphite
  slug: graphite-com-stacked-pull-requests
slug: graphite-com
tags:
- Code Review
- Stacked PRs
- Merge Queue
- AI Code Review
- Developer Tools
- GitHub
website: https://graphite.dev
---
