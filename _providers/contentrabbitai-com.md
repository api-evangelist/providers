---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 35.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Contentrabbitai Com Agentic Access
  operation_count: 2
  slug: contentrabbitai-com-agentic-access
  summary_line: 2 operations · 2 acting
api_count: 1
apis:
- description: Public REST API for Content Rabbit enabling content creation, scheduling and analytics.
  name: Content Rabbit API
  slug: content-rabbit-api
artifact_total: 8
common:
- group: agent
  href: https://artifacts.apis.io/contentrabbitai-com/agentic-access/contentrabbitai-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/contentrabbitai-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/contentrabbitai-com/rate-limits/contentrabbitai-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/contentrabbitai-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/contentrabbitai-com/plans/contentrabbitai-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/contentrabbitai-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/contentrabbitai-com/rules/contentrabbitai-com-rules.yml
  title: ''
  type: Spectral
  url: rules/contentrabbitai-com-rules.yml
- group: design
  href: https://artifacts.apis.io/contentrabbitai-com/errors/contentrabbitai-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/contentrabbitai-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/contentrabbitai-com/conformance/contentrabbitai-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/contentrabbitai-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/contentrabbitai-com/llms/contentrabbitai-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/contentrabbitai-com-llms.txt
- group: other
  href: https://artifacts.apis.io/contentrabbitai-com/a2a/contentrabbitai-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/contentrabbitai-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/contentrabbitai-com/mcp/contentrabbitai-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/contentrabbitai-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/contentrabbitai-com/well-known/contentrabbitai-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/contentrabbitai-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/contentrabbitai-com/hosts/contentrabbitai-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/contentrabbitai-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/contentrabbitai-com/vendors/contentrabbitai-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/contentrabbitai-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://contentrabbitai.com/terms
- group: operate
  title: ''
  type: Support
  url: https://contentrabbitai.com/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://contentrabbitai.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://contentrabbitai.com/pricing
- group: start
  title: ''
  type: Login
  url: https://contentrabbitai.com/login
- group: start
  title: ''
  type: DeveloperPortal
  url: https://contentrabbitai.com/developers
- group: operate
  title: ''
  type: ChangeLog
  url: https://contentrabbitai.com/changelog
- group: company
  title: ''
  type: Blog
  url: https://blog.contentrabbitai.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://contentrabbitai.com/support/articles/getting-started#main-content
- group: docs
  title: ''
  type: APIReference
  url: https://contentrabbitai.com/llms.txt
- group: auth
  href: https://artifacts.apis.io/contentrabbitai-com/authentication/contentrabbitai-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/contentrabbitai-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/contentrabbitai-com/security/contentrabbitai-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/contentrabbitai-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://contentrabbitai.com/
created: '2026-11-04'
description: Content Rabbit is an AI‑powered social media management platform that helps creators, teams and agencies publish across multiple channels. It offers AI‑generated content suggestions, scheduling, analytics and API access for automating workflows. The service supports platforms such as X (Twitter), Instagram, LinkedIn, TikTok, Threads, Bluesky, Pinterest, Facebook and more, enabling users to manage their social presence from a single dashboard.
image: https://contentrabbitai.com/og-image.png
layout: provider
mcp_servers:
- description: Remote MCP server at contentrabbitai.com requiring an API key.
  name: Content Rabbit MCP Server
  slug: contentrabbitai-com-mcp-yml
modified: '2026-11-04'
name: Content Rabbit
nav: Providers
network: true
overview: 'Content Rabbit is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Software-as-a-Service, Social Media, Artificial Intelligence, Content Management, and Automation.


  The Content Rabbit catalog on APIs.io includes 1 Spectral governance ruleset.


  Content Rabbit''s developer surface includes support, pricing, changelog, engineering blog, getting-started guide, API reference, authentication, and 18 more developer resources.'
plans:
- name: Contentrabbitai Com Plans Pricing
  plan_count: 4
  slug: contentrabbitai-com-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 1
  name: Contentrabbitai Com Rate Limits
  slug: contentrabbitai-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 79
  extends:
  - spectral:oas
  name: Content Rabbit API Rules
  rule_count: 38
  severity_counts:
    error: 36
    hint: 0
    info: 1
    warn: 1
  slug: contentrabbitai-com-rules
score:
  band: developing
  composite: 41.0
  coverage:
    artifact_dirs: 17
    catalog_earned: 61.5
    catalog_earned_first_party: 20.0
    catalog_gap: 53.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 31.8
    contract_quality: 0.0
    developer_ergonomics: 47.6
    discoverability: 65.0
    operational_transparency: 36.8
  provenance:
    agentic_access: derived
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Contentrabbitai Com Authentication
  slug: contentrabbitai-com-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Contentrabbitai Com Domain Security
  slug: contentrabbitai-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: contentrabbitai-com
tags:
- Software-as-a-Service
- Social Media
- Artificial Intelligence
- Content Management
- Automation
website: https://contentrabbitai.com/
---
