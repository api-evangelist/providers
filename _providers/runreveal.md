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
  band: agent-aware
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 24.6
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: 'REST API for RunReveal — manage sources, detections, pipelines, investigations, dashboards, notifications, agents, and agent skills across a workspace. OAuth2 (authorization_code + PKCE) or workspace '
  name: RunReveal API
  slug: runreveal-api
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://runreveal.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.runreveal.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.runreveal.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.runreveal.com/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.runreveal.com/how-to-guides/onboarding
- group: company
  title: ''
  type: Blog
  url: https://blog.runreveal.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/runreveal
- group: commercial
  title: ''
  type: Pricing
  url: https://runreveal.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://runreveal.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://runreveal.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://runreveal.com/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://runrevealstatus.com
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/runreveal-changelog.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/runreveal-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://runreveal.com/security
- group: auth
  title: ''
  type: Authentication
  url: authentication/runreveal-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/runreveal-scopes.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/runreveal-mcp.yml
- group: build
  title: ''
  type: CLI
  url: cli/runreveal-cli.yml
- group: build
  title: ''
  type: Packages
  url: packages/runreveal-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/runreveal-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/runreveal-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/runreveal-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/runreveal-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/runreveal-conventions.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/runreveal-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: RunReveal is a unified security log management and detection platform that replaces traditional SIEM with a scalable security data lake, AI-powered detection engineering, and natural-language investigations. It ingests and normalizes security logs from 100+ sources (object storage, forwarders, and webhook/API polling), runs detections-as-code (native and Sigma), and lets analysts query with SQL or PQL, build dashboards, and route alerts. RunReveal exposes a REST API, a JSON-in/JSON-out CLI, OAuth-based access with granular workspace scopes, and both hosted-remote and local Model Context Protocol (MCP) servers for AI-agent integration. Backed by Costanoa Ventures.
image: https://runreveal.com/unfurl.png
layout: provider
mcp_servers:
- description: ''
  name: RunReveal MCP Server
  slug: runreveal-mcp-server
modified: '2026-07-21'
name: RunReveal
nav: Providers
network: true
overview: 'RunReveal publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, SIEM, Security Log Management, and Detection Engineering.


  RunReveal''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, changelog, and 20 more developer resources.'
random_paper: 14
scopes:
- name: Runreveal Scopes
  scope_count: 37
  slug: runreveal-scopes
  summary_line: 37 scopes · authorizationCode/refreshToken
score:
  band: developing
  composite: 39.9
  coverage:
    artifact_dirs: 15
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 18.2
    contract_quality: 5.3
    developer_ergonomics: 61.3
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 34.2
  previous_composite: 39.9
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/runreveal/refs/heads/main/screenshots/runreveal-2026-09-02T154209.png
security:
- kind: authentication
  name: Runreveal Authentication
  slug: runreveal-authentication
  summary_line: oauth2/apiKey · 2 schemes
- kind: domain-security
  name: Runreveal Domain Security
  slug: runreveal-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Runreveal Trust Center
  slug: runreveal-trust-center
  summary_line: SOC 2, GDPR
slug: runreveal
tags:
- Company
- Security
- SIEM
- Security Log Management
- Detection Engineering
- Threat Detection
- Incident Response
- Observability
- SQL
- MCP
- Artificial Intelligence
website: https://runreveal.com
---
