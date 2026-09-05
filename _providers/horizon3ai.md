---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 43.2
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: 'The NodeZero API is a publicly accessible GraphQL API that exposes a subset of the Horizon3.ai Portal: schedule and control autonomous pentest operations, and read pentests, ops, weaknesses, attack pa'
  name: NodeZero GraphQL API
  slug: nodezero-graphql-api
artifact_total: 8
asyncapis:
- description: ''
  name: Horizon3Ai Webhooks
  slug: horizon3ai-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://horizon3.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.horizon3ai.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.horizon3.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.horizon3.ai/api/graphql/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.horizon3.ai/api/getting_started/
- group: docs
  title: ''
  type: GraphQL
  url: https://api.gateway.horizon3ai.com/v1/graphql
- group: company
  title: ''
  type: Blog
  url: https://horizon3.ai/intelligence/blogs/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/horizon3ai
- group: operate
  title: ''
  type: Roadmap
  url: https://horizon3.ai/roadmap/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.horizon3.ai
- group: commercial
  title: ''
  type: Pricing
  url: https://horizon3.ai/use-case/packaging/
- group: start
  title: ''
  type: SignUp
  url: https://portal.horizon3ai.com
- group: start
  title: ''
  type: Login
  url: https://portal.horizon3ai.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://horizon3.ai/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://horizon3.ai/privacy-policy/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.horizon3.ai/
- group: auth
  title: ''
  type: Compliance
  url: https://horizon3.ai/compliance/
- group: auth
  title: ''
  type: Security
  url: https://horizon3.ai/vulnerability-disclosure-policy/
- group: agent
  title: ''
  type: MCPServer
  url: mcp/horizon3ai-mcp.yml
- group: build
  title: ''
  type: CLI
  url: cli/horizon3ai-cli.yml
- group: build
  title: ''
  type: Packages
  url: packages/horizon3ai-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/horizon3ai-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/horizon3ai-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/horizon3ai-well-known.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/horizon3ai-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/horizon3ai-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/horizon3ai-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/horizon3ai-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/horizon3ai-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/horizon3ai-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/horizon3ai-webhooks.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/horizon3ai-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/horizon3ai-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/horizon3ai-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Horizon3.ai is a cybersecurity company whose NodeZero platform delivers autonomous penetration testing and continuous security posture management. NodeZero safely attacks your internal, external, cloud, and hybrid environments the way a real adversary would, proving exploitable attack paths, prioritizing the fixes that matter, and verifying that remediations actually work. Horizon3.ai exposes a publicly documented GraphQL API (the NodeZero API) plus an h3-cli command-line tool and a hosted Model Context Protocol (MCP) server, letting teams schedule pentests, retrieve findings, weaknesses, attack paths, credentials, and host inventory, and wire results into CI/CD, ticketing (Jira, ServiceNow), and agentic workflows. NodeZero Federal is FedRAMP High authorized for public-sector use.
image: https://www.horizon3.ai/wp-content/uploads/2023/08/1200x627-NodeZero-UI_Sankey.jpg
layout: provider
mcp_servers:
- description: Horizon3.ai-hosted Model Context Protocol server exposing NodeZero data and actions to MCP-compliant agents. Backs onto the same NodeZero platform as the GraphQL API. Secured with OAuth 2.1 (PKCE) via
  name: Horizon3.ai MCP Server
  slug: horizon3ai-mcp-server
modified: '2026-07-19'
name: Horizon3.ai
nav: Providers
network: true
overview: 'Horizon3.ai publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Cybersecurity, Penetration Testing, and Autonomous Pentesting.


  The Horizon3.ai catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Horizon3.ai''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, CLI, and 28 more developer resources.'
random_paper: 1
scopes:
- name: Horizon3Ai Scopes
  scope_count: 2
  slug: horizon3ai-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: developing
  composite: 45.0
  coverage:
    artifact_dirs: 18
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 49.4
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 42.1
  previous_composite: 45.0
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/horizon3ai/refs/heads/main/screenshots/horizon3ai-2026-07-25T221429.png
security:
- kind: authentication
  name: Horizon3Ai Authentication
  slug: horizon3ai-authentication
  summary_line: apiKey/http-bearer/oauth2 · 3 schemes
- kind: domain-security
  name: Horizon3Ai Domain Security
  slug: horizon3ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Horizon3Ai Vulnerability Disclosure
  slug: horizon3ai-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Horizon3Ai Trust Center
  slug: horizon3ai-trust-center
  summary_line: FedRAMP High, SOC 2, CMMC 2.0, NIST SP 800-53 Rev. 5
slug: horizon3ai
tags:
- Company
- Security
- Cybersecurity
- Penetration Testing
- Autonomous Pentesting
- Attack Surface Management
- Exposure Management
- Vulnerability Management
- GraphQL
- Offensive Security
website: https://horizon3.ai
---
