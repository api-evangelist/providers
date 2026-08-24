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
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 8.5
  scored_at: '2026-08-24'
api_count: 1
apis:
- description: Impart Security's v0 REST management API — programmatically manage specs, API/log bindings, connectors, core rules, rule scripts and recipes, lists, labels, tags, event monitors, and notification temp
  name: Impart Security v0 REST API
  slug: impart-security-v0-rest-api
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.impart.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://console.impartsecurity.net/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.impartsecurity.net/
- group: company
  title: ''
  type: Blog
  url: https://www.impart.ai/resource-center
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/impart-security
- group: start
  title: ''
  type: SignUp
  url: https://www.impart.ai/demo
- group: operate
  title: ''
  type: Support
  url: mailto:support@impart.security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.impart.ai/legal/privacy-policy
- group: auth
  title: ''
  type: Compliance
  url: https://www.impart.ai/
- group: build
  title: ''
  type: Packages
  url: packages/impart-security-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/impart-security-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/impart-security-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/impart-security-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/impart-security-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/impart-security-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/impart-security-llms.txt
created: '2026-07-17'
description: Impart Security is a runtime security platform that unifies WAF, API security, and AI/LLM/agent/MCP protection on one inline enforcement engine. It analyzes the full request/response flow — headers, parameters, query strings, and bodies — models API behavior with machine learning, detects anomalies from a learned baseline, and takes inline mitigation actions (alert, block, behavioral rate limiting, deception, tarpits) before requests reach backend systems. Impart also auto-generates OpenAPI documentation from live traffic, integrates with gateways such as Kong, and ships a programmable rules engine managed as code via first-party Terraform and Pulumi providers against its v0 REST API. Founded by Jonathan DiVincenzo, Marc Harrison, and Brian Joe; backed by Madrona, CRV, 8-bit Capital, and Haystack. SOC 2 Type II certified and GDPR ready.
image: https://cdn.prod.website-files.com/69c2a371d79849d9c09b537d/6a086ac25135439db8499dee_64b88db668b71259bd9720385d8dde1e_Impart%20Open%20Graph.png
layout: provider
modified: '2026-07-19'
name: Impart Security
nav: Providers
network: true
overview: 'Impart Security publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, API Security, Runtime Protection, and WAF.


  Impart Security''s developer surface includes documentation, engineering blog, signup flow, support, authentication, and 11 more developer resources.'
random_paper: 11
score:
  band: emerging
  composite: 23.7
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 31.0
    discoverability: 87.0
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 23.7
  provenance:
    conformance: first-party
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/impart-security/refs/heads/main/screenshots/impart-security-2026-07-25T222144.png
security:
- kind: authentication
  name: Impart Security Authentication
  slug: impart-security-authentication
  summary_line: http-bearer · 1 scheme
- kind: domain-security
  name: Impart Security Domain Security
  slug: impart-security-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: impart-security
tags:
- Company
- Security
- API Security
- Runtime Protection
- WAF
- LLM Security
- AI Security
- MCP
- Agent Security
- Kong
- Governance
website: https://www.impart.ai/
---
