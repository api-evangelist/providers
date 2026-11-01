---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: flavored
    agent_skills: false
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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.6
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Social Neuron provides AI‑driven content creation and social‑media automation tools. Documentation is hosted at https://docs.socialneuron.com but no machine‑readable contract could be retrieved.
  name: Social Neuron API
  slug: social-neuron-api
artifact_total: 6
common:
- group: commercial
  href: https://artifacts.apis.io/socialneuron/plans/socialneuron-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/socialneuron-plans-pricing.yml
- group: build
  href: https://artifacts.apis.io/socialneuron/cli/socialneuron-cli.yml
  title: ''
  type: CLI
  url: cli/socialneuron-cli.yml
- group: auth
  href: https://artifacts.apis.io/socialneuron/authentication/socialneuron-authentication.yml
  title: ''
  type: Authentication
  url: authentication/socialneuron-authentication.yml
- group: design
  href: https://artifacts.apis.io/socialneuron/conformance/socialneuron-conformance.yml
  title: ''
  type: Conformance
  url: conformance/socialneuron-conformance.yml
- group: agent
  href: https://artifacts.apis.io/socialneuron/llms/socialneuron-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/socialneuron-llms.txt
- group: other
  href: https://artifacts.apis.io/socialneuron/a2a/socialneuron-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/socialneuron-a2a.yml
- group: agent
  href: https://artifacts.apis.io/socialneuron/mcp/socialneuron-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/socialneuron-mcp.yml
- group: auth
  href: https://artifacts.apis.io/socialneuron/well-known/socialneuron-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/socialneuron-security.txt
- group: auth
  href: https://artifacts.apis.io/socialneuron/well-known/socialneuron-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/socialneuron-app-security.txt
- group: agent
  href: https://artifacts.apis.io/socialneuron/well-known/socialneuron-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/socialneuron-well-known.yml
- group: other
  href: https://artifacts.apis.io/socialneuron/hosts/socialneuron-hosts.yml
  title: ''
  type: Hosts
  url: hosts/socialneuron-hosts.yml
- group: other
  href: https://artifacts.apis.io/socialneuron/vendors/socialneuron-vendors.yml
  title: ''
  type: Vendors
  url: vendors/socialneuron-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://socialneuron.com/terms
- group: operate
  title: ''
  type: Support
  url: https://socialneuron.com/help
- group: auth
  title: ''
  type: Security
  url: https://socialneuron.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://socialneuron.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://socialneuron.com/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://socialneuron.com/press
- group: operate
  title: ''
  type: ChangeLog
  url: https://socialneuron.com/changelog
- group: company
  title: ''
  type: Blog
  url: https://socialneuron.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.socialneuron.com/guides/mcp-quickstart
- group: docs
  title: ''
  type: Documentation
  url: https://docs.socialneuron.com/
- group: docs
  title: ''
  type: APIReference
  url: https://socialneuron.com/for-developers
- group: auth
  href: https://artifacts.apis.io/socialneuron/security/socialneuron-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/socialneuron-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/socialneuron/security/socialneuron-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/socialneuron-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://socialneuron.com
coverage:
  checked: '2026-10-27'
  detail: Documentation at https://docs.socialneuron.com provides no OpenAPI, GraphQL, or other machine‑readable contract.
  evidence:
  - status: 404
    url: https://docs.socialneuron.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-27'
description: Social Neuron, built by Cosmocodex Ltd (UK), offers AI‑driven content creation and social‑media automation tools that learn from results. The platform generates videos, posts, and marketing assets for TikTok, Instagram, YouTube, and more, aiming to make AI content smarter and more effective.
image: https://socialneuron.com/logo-full.jpg
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.socialneuron.com requiring OAuth.
  name: Social Neuron MCP Server
  slug: socialneuron-mcp-yml
modified: '2026-10-27'
name: Social Neuron
nav: Providers
network: true
overview: 'Social Neuron is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Content Creation, Social Media, and Automation.


  Social Neuron''s developer surface includes CLI, authentication, support, pricing, changelog, engineering blog, getting-started guide, and 19 more developer resources.'
plans:
- name: Socialneuron Plans Pricing
  plan_count: 5
  slug: socialneuron-plans-pricing
random_paper: 2
score:
  band: thin
  composite: 37.0
  coverage:
    artifact_dirs: 13
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 54.8
    discoverability: 58.3
    operational_transparency: 26.3
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Socialneuron Authentication
  slug: socialneuron-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Socialneuron Domain Security
  slug: socialneuron-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Socialneuron Vulnerability Disclosure
  slug: socialneuron-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: socialneuron
tags:
- Company
- AI
- Content Creation
- Social Media
- Automation
website: https://socialneuron.com
---
