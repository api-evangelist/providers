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
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 26.1
  scored_at: '2026-08-06'
api_count: 1
apis:
- description: Hosted, authenticated Model Context Protocol server for managing assessments, reviewing candidates, and analyzing hiring data. Streamable-HTTP transport; Bearer MeritFirst API key (mf_) required.
  name: MeritFirst MCP
  slug: meritfirst-mcp
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/meritfirst-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://meritfirst.us
- group: start
  title: ''
  type: SignUp
  url: https://meritfirst.us/login?signup=true
- group: start
  title: ''
  type: Login
  url: https://meritfirst.us/login
- group: auth
  title: ''
  type: Security
  url: https://www.meritfirst.us/security
- group: agent
  title: ''
  type: MCPServer
  url: mcp/meritfirst-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/meritfirst-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/meritfirst-security.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/meritfirst-authentication.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/meritfirst-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/meritfirst-llms.txt
created: '2026-07-17'
description: MeritFirst is a skills-based hiring platform that replaces resume- and credential-based recruiting with practical, real-world assessments. Candidates prove their craft through work samples (Build, Try, Get Seen) and companies evaluate and match them on demonstrated ability rather than pedigree. MeritFirst exposes a hosted, authenticated Model Context Protocol (MCP) server so agents and tools can manage assessments, review candidates, and analyze hiring data. Backed by 8VC and Slow Ventures.
image: https://www.meritfirst.us/images/logo.svg
layout: provider
mcp_servers:
- description: ''
  name: meritfirst-mcp.yml
  slug: meritfirst-mcpyml
modified: '2026-07-20'
name: Meritfirst
nav: Providers
network: true
overview: 'Meritfirst publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Hiring, Recruiting, Assessments, and Talent.


  Meritfirst''s developer surface includes signup flow, authentication, and 9 more developer resources.'
random_paper: 80
score:
  band: emerging
  composite: 16.6
  delta: 0.0
  facets:
    commercial_clarity: 13.2
    contract_quality: 0.0
    developer_ergonomics: 19.6
    discoverability: 87.0
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 16.6
  provenance:
    mcp: first-party
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Meritfirst Authentication
  slug: meritfirst-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Meritfirst Domain Security
  slug: meritfirst-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Meritfirst Vulnerability Disclosure
  slug: meritfirst-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: meritfirst
tags:
- Company
- Hiring
- Recruiting
- Assessments
- Talent
- Skills-Based Hiring
- MCP
website: https://meritfirst.us
---
