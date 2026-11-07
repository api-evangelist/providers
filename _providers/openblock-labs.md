---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - scopes
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
    mcp_server: verified
    mcp_tool_quality: full
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 14.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: The OB-1 coding-agent platform. The only publicly reachable API surface is the OAuth 2.0 / OpenID Connect authorization server; the platform data API and manual sit behind authenticated dashboard acce
  name: OB-1 Platform
  slug: ob-1-platform
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.openblocklabs.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dashboard.openblocklabs.com/
- group: docs
  title: ''
  type: Documentation
  url: https://dashboard.openblocklabs.com/manual
- group: commercial
  title: ''
  type: Pricing
  url: https://openblocklabs.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://auth.openblocklabs.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dashboard.openblocklabs.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dashboard.openblocklabs.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/openblocklabs
- group: operate
  title: ''
  type: Support
  url: https://join.slack.com/t/ob1-co/shared_invite/zt-3rjae490g-uiEO5z_FnWJ5GAc~hkfkyA
- group: auth
  href: https://artifacts.apis.io/openblock-labs/authentication/openblock-labs-authentication.yml
  title: ''
  type: Authentication
  url: authentication/openblock-labs-authentication.yml
- group: auth
  href: https://artifacts.apis.io/openblock-labs/scopes/openblock-labs-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/openblock-labs-scopes.yml
- group: agent
  href: https://artifacts.apis.io/openblock-labs/well-known/openblock-labs-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/openblock-labs-well-known.yml
- group: design
  href: https://artifacts.apis.io/openblock-labs/conformance/openblock-labs-conformance.yml
  title: ''
  type: Conformance
  url: conformance/openblock-labs-conformance.yml
- group: build
  href: https://artifacts.apis.io/openblock-labs/cli/openblock-labs-cli.yml
  title: ''
  type: CLI
  url: cli/openblock-labs-cli.yml
- group: design
  href: https://artifacts.apis.io/openblock-labs/conventions/openblock-labs-conventions.yml
  title: ''
  type: Conventions
  url: conventions/openblock-labs-conventions.yml
- group: agent
  href: https://artifacts.apis.io/openblock-labs/llms/openblock-labs-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/openblock-labs-llms.txt
- group: auth
  href: https://artifacts.apis.io/openblock-labs/security/openblock-labs-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/openblock-labs-domain-security.yml
created: '2026-07-17'
description: OpenBlock Labs builds OB-1, a self-improving autonomous coding agent that automates the software development lifecycle from PM to PR. OB-1 runs as a native terminal CLI and inside VS Code and JetBrains IDEs, consumes MCP (Model Context Protocol) servers for custom tool integration, and provides a built-in browser agent. It routes across 300+ models via OpenRouter with bring-your-own-keys, bills usage-based at 1:1 model-token pass-through, and integrates with GitHub, Linear, Graphite, and Slack. Access is authenticated through a standards-compliant OAuth 2.0 / OpenID Connect authorization server (auth.openblocklabs.com, WorkOS AuthKit), with SSO/SAML, self-hosting, and audit logging available on enterprise plans. Originally surfaced as a portfolio company of Electric Capital and enriched by the API Evangelist pipeline from its public product surface and published auth metadata.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/openblock-labs.png
layout: provider
mcp_servers:
- description: Remote MCP server at docs.openblocklabs.com over HTTP; 3 tools listed.
  name: OpenBlock Labs MCP Server
  slug: openblock-labs
modified: '2026-09-16'
name: OpenBlock Labs
nav: Providers
network: true
overview: 'OpenBlock Labs is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data, Coding Agents, AI Agents, and Developer Tools.


  OpenBlock Labs'' developer surface includes documentation, pricing, signup flow, support, authentication, CLI, and 11 more developer resources.'
random_paper: 4
scopes:
- name: Openblock Labs Scopes
  scope_count: 4
  slug: openblock-labs-scopes
  summary_line: 4 scopes
score:
  band: emerging
  composite: 23.7
  coverage:
    artifact_dirs: 12
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 23.7
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 33.3
    discoverability: 75.0
    operational_transparency: 2.6
  previous_composite: 23.7
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/openblock-labs/openblock-labs-2026-08-07T190536.png
security:
- kind: authentication
  name: Openblock Labs Authentication
  slug: openblock-labs-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Openblock Labs Domain Security
  slug: openblock-labs-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: openblock-labs
tags:
- Company
- Data
- Coding Agents
- AI Agents
- Developer Tools
- Automation
- OAuth
- MCP
- Identity Federation
- Authentication
website: https://www.openblocklabs.com/
---
