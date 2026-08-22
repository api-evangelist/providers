---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 22.2
  scored_at: '2026-08-19'
api_count: 2
apis:
- description: Versioned REST API exposed by the Deep Instinct DSX management console (D-Appliance) at https://<your-tenant-fqdn>/api/v1. Covers devices, device groups, policies, events (including the JSON event-sea
  name: Deep Instinct DSX Management REST API
  slug: deep-instinct-dsx-management-rest-api
- description: Model Context Protocol server hosted on Deep Instinct's customer portal at https://portal.deepinstinct.com/mcp, advertised through RFC 9728 protected-resource metadata and an RFC 8414 authorization-se
  name: Deep Instinct Portal MCP Server
  slug: deep-instinct-portal-mcp-server
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://www.deepinstinct.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.deepinstinct.com/
- group: operate
  title: ''
  type: Support
  url: https://www.deepinstinct.com/contact-us
- group: company
  title: ''
  type: Blog
  url: https://www.deepinstinct.com/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://www.deepinstinct.com/blog/feed
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/deepinstinct
- group: start
  title: ''
  type: SignUp
  url: https://www.deepinstinct.com/request-a-demo
- group: start
  title: ''
  type: Login
  url: https://portal.deepinstinct.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.deepinstinct.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.deepinstinct.com/privacy-policy
- group: auth
  title: ''
  type: Compliance
  url: https://www.deepinstinct.com/compliance-certification-evaluation
- group: agent
  title: ''
  type: MCPServer
  url: mcp/deep-instinct-mcp.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/deep-instinct-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/deep-instinct-authentication.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/deep-instinct-well-known.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/deep-instinct-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/deep-instinct-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/deep-instinct-lifecycle.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/deep-instinct-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/deep-instinct-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/deep-instinct-packages.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/deep-instinct-problem-types.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/deep-instinct-llms.txt
created: '2026-08-01'
description: Deep Instinct is a preemptive data security company that applies a purpose-built deep learning framework (the DSX Brain) to prevent and explain unknown malware, ransomware and zero-day threats in real time, without signatures, heuristics, cloud lookups or external threat feeds. Its DSX platform protects data across cloud storage, network-attached storage (Dell CAVA, NetApp Vscan), applications and endpoints, and pairs the prevention engine with DSX Companion (DIANNA), a GenAI analysis assistant that produces human-readable explanations of novel attacks for SOC triage. The DSX management console (D-Appliance) exposes a versioned REST API at /api/v1 for device, group, policy, event, hash allow/block-list, remote remediation and audit-log automation, and Deep Instinct's customer portal now also fronts an OAuth-protected MCP server for agent access to portal content.
image: https://www.deepinstinct.com/image/bltefff210f63a383a8/68937a472607b85c9942030a/Meta_Home_1200_x_627.png
layout: provider
mcp_servers:
- description: ''
  name: deep-instinct-mcp.yml
  slug: deep-instinct-mcpyml
- description: ''
  name: mcp
  slug: mcp
modified: '2026-08-01'
name: Deep Instinct
nav: Providers
network: true
overview: 'Deep Instinct publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include cybersecurity, endpoint-security, malware-prevention, ransomware, and deep-learning.


  Deep Instinct''s developer surface includes support, engineering blog, signup flow, authentication, and 19 more developer resources.'
random_paper: 12
scopes:
- name: Deep Instinct Scopes
  scope_count: 2
  slug: deep-instinct-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: thin
  composite: 26.9
  delta: -0.9
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 87.0
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 27.8
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/deep-instinct/refs/heads/main/screenshots/deep-instinct-2026-08-07T164228.png
security:
- kind: authentication
  name: Deep Instinct Authentication
  slug: deep-instinct-authentication
  summary_line: oauth2/apiKey · 2 schemes
- kind: domain-security
  name: Deep Instinct Domain Security
  slug: deep-instinct-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Deep Instinct Trust Center
  slug: deep-instinct-trust-center
  summary_line: SOC 2 Type II, ISO/IEC 27001, ISO/IEC 27017, ISO/IEC 27018:2019, PCI DSS, GDPR
slug: deep-instinct
tags:
- cybersecurity
- endpoint-security
- malware-prevention
- ransomware
- deep-learning
- threat-prevention
- data-security
- edr
- soc-automation
- mcp
website: https://www.deepinstinct.com/
---
