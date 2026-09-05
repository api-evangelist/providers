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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 27.3
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.realscout.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://learn.realscout.com/pricing/
- group: operate
  title: ''
  type: Support
  url: https://support.realscout.com/
- group: company
  title: ''
  type: Blog
  url: https://blog.realscout.com/
- group: start
  title: ''
  type: Login
  url: https://www.realscout.com/agents/sign_in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.realscout.com/terms-and-policies
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.realscout.com/terms-and-policies
- group: agent
  title: ''
  type: MCPServer
  url: mcp/realscout-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/realscout-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/realscout-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/realscout-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/realscout-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/realscout-llms.txt
created: '2026-07-17'
description: RealScout is a lead-nurture and collaborative home-search platform for real estate professionals — agents, teams, and brokerages — that turns an agent's existing database and local MLS inventory into a recurring source of transactions. It is CRM-agnostic and plugs into existing stacks (Follow Up Boss, Sierra, Salesforce, HubSpot) via native integrations, Zapier/Make, and direct API access on Enterprise plans. Core products include AI Search (natural-language-to-MLS-criteria), Scout Score (0–100 contact engagement scoring), Contact Enrichment, Search Links, and Auto-Nurture alerts. RealScout publishes an OAuth 2.1-protected, standards-compliant MCP server (api://realscout-admin-mcp) for agent/AI access. Backed by DCM Ventures.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/realscout.png
layout: provider
mcp_servers:
- description: ''
  name: RealScout MCP Server
  slug: realscout-mcp-server
modified: '2026-07-20'
name: RealScout
nav: Providers
network: true
overview: 'RealScout is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Enterprise, Real-Estate, PropTech, and Lead Nurture.


  RealScout''s developer surface includes pricing, support, engineering blog, authentication, and 9 more developer resources.'
random_paper: 12
scopes:
- name: Realscout Scopes
  scope_count: 1
  slug: realscout-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: emerging
  composite: 17.2
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 38.2
    commercial_clarity: 38.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 17.2
  provenance:
    mcp: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/realscout/refs/heads/main/screenshots/realscout-2026-09-02T153004.png
security:
- kind: authentication
  name: Realscout Authentication
  slug: realscout-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Realscout Domain Security
  slug: realscout-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: realscout
tags:
- Company
- Enterprise
- Real-Estate
- PropTech
- Lead Nurture
- Home Search
- MLS
- MCP
- Artificial Intelligence
website: https://www.realscout.com/
---
