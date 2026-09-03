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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 14.0
  scored_at: '2026-09-02'
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
- description: Connect to MeritFirst to manage assessments, review candidates, and analyze hiring data.
  name: Meritfirst MCP Server
  slug: meritfirst-mcp-server
modified: '2026-07-20'
name: Meritfirst
nav: Providers
network: true
overview: 'Meritfirst publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Hiring, Recruiting, Assessments, and Talent.


  Meritfirst''s developer surface includes signup flow, authentication, and 9 more developer resources.'
random_paper: 5
score:
  band: emerging
  composite: 12.7
  coverage:
    artifact_dirs: 6
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 6.6
    commercial_clarity: 6.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 12.7
  provenance:
    mcp: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/meritfirst/refs/heads/main/screenshots/meritfirst-2026-08-07T172605.png
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
