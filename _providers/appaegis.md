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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: derived
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
  score: 3.4
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: REST (v1 + v2) and GraphQL management API for the Mammoth Cyber (Appaegis) zero-trust access platform. Administers users, teams, access roles, policies, applications, networks, registered devices, blo
  name: Mammoth Cyber Management API
  slug: mammoth-cyber-management-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://mammothcyber.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://github.com/appaegis/api-script-samples
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/appaegis/api-script-samples/blob/main/README.md
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/appaegis/api-script-samples#quickstart
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/appaegis/api-script-samples
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/appaegis
- group: company
  title: ''
  type: Blog
  url: https://mammothcyber.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://mammothcyber.com/contact/
- group: start
  title: ''
  type: SignUp
  url: https://mammothcyber.com/schedule-a-demo/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mammothcyber.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mammothcyber.com/policy/
- group: other
  title: ''
  type: Downloads
  url: https://mammothcyber.com/downloads/
- group: auth
  title: ''
  type: Authentication
  url: authentication/appaegis-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/appaegis-conventions.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/appaegis-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/appaegis-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Packages
  url: packages/appaegis-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/appaegis-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/appaegis-domain-security.yml
created: '2026-07-17'
description: 'Appaegis (now Mammoth Cyber) is an enterprise zero-trust access and secure enterprise browser company. Originally launched as Appaegis, the company rebranded to Mammoth Cyber and delivers an Enterprise AI Browser that unifies secure web access, data loss prevention, granular access policy, and zero-trust controls for remote workforces, BYOD, and third-party contractors. The platform is API-first: it exposes a REST management API (v1 and v2) and a GraphQL endpoint on api.mammothcyber.net for administering users, teams, access roles, policies, applications, networks, registered devices, blocked-site lists, and URL categories, with API keys issued from the management portal and a token-exchange authentication flow. This profile was seeded as a 500 Global portfolio lead and enriched from the company''s public developer surface.'
image: https://avatars.githubusercontent.com/u/53629332?v=4
layout: provider
mcp_servers:
- description: ''
  name: Appaegis MCP Server
  slug: appaegis-mcp-server
modified: '2026-07-17'
name: Appaegis
nav: Providers
network: true
overview: 'Appaegis publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Zero Trust, Enterprise Browser, and Access Management.


  Appaegis'' developer surface includes documentation, getting-started guide, engineering blog, support, signup flow, authentication, and 14 more developer resources.'
random_paper: 2
score:
  band: emerging
  composite: 25.1
  coverage:
    artifact_dirs: 10
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 51.8
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 25.1
  provenance:
    mcp: derived
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/appaegis/refs/heads/main/screenshots/appaegis-2026-07-25T200708.png
security:
- kind: authentication
  name: Appaegis Authentication
  slug: appaegis-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Appaegis Domain Security
  slug: appaegis-domain-security
  summary_line: TLSv1.3 · DMARC
slug: appaegis
tags:
- Company
- Security
- Zero Trust
- Enterprise Browser
- Access Management
- Data Loss Prevention
- GenAI Security
- Identity
- SASE
website: https://mammothcyber.com
---
