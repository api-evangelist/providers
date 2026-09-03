---
access_model:
  confidence: medium
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
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
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: The OB-1 coding-agent platform. The only publicly reachable API surface is the OAuth 2.0 / OpenID Connect authorization server; the platform data API and manual sit behind authenticated dashboard acce
  name: OB-1 Platform
  slug: ob-1-platform
artifact_total: 4
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
  title: ''
  type: Authentication
  url: authentication/openblock-labs-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/openblock-labs-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/openblock-labs-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/openblock-labs-conformance.yml
- group: build
  title: ''
  type: CLI
  url: cli/openblock-labs-cli.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/openblock-labs-conventions.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/openblock-labs-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/openblock-labs-domain-security.yml
created: '2026-07-17'
description: OpenBlock Labs builds OB-1, a self-improving autonomous coding agent that automates the software development lifecycle from PM to PR. OB-1 runs as a native terminal CLI and inside VS Code and JetBrains IDEs, consumes MCP (Model Context Protocol) servers for custom tool integration, and provides a built-in browser agent. It routes across 300+ models via OpenRouter with bring-your-own-keys, bills usage-based at 1:1 model-token pass-through, and integrates with GitHub, Linear, Graphite, and Slack. Access is authenticated through a standards-compliant OAuth 2.0 / OpenID Connect authorization server (auth.openblocklabs.com, WorkOS AuthKit), with SSO/SAML, self-hosting, and audit logging available on enterprise plans. Originally surfaced as a portfolio company of Electric Capital and enriched by the API Evangelist pipeline from its public product surface and published auth metadata.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/openblock-labs.png
layout: provider
modified: '2026-07-20'
name: OpenBlock Labs
nav: Providers
network: true
overview: 'OpenBlock Labs publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data, Coding Agents, AI Agents, and Developer Tools.


  OpenBlock Labs'' developer surface includes documentation, pricing, signup flow, support, authentication, CLI, and 11 more developer resources.'
random_paper: 13
scopes:
- name: Openblock Labs Scopes
  scope_count: 0
  slug: openblock-labs-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 21.5
  coverage:
    artifact_dirs: 9
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 33.3
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 21.5
  provenance:
    conformance: first-party
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/openblock-labs/refs/heads/main/screenshots/openblock-labs-2026-08-07T190536.png
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
- Authentication
- MCP
website: https://www.openblocklabs.com/
---
