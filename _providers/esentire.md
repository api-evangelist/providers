---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 7.1
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: An authorization-gated Model Context Protocol server operated by eSentire on its own API host. Every path under https://api.esentire.com/mcp/ answers 401 UNAUTHORIZED with an RFC 9728 challenge (`WWW-
  name: eSentire MCP Server
  slug: esentire-mcp
artifact_total: 9
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/esentire-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.esentire.com/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://www.hiive.com/securities/esentire-stock
- group: company
  title: ''
  type: Blog
  url: https://www.esentire.com/resources/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/eSentire
- group: start
  title: ''
  type: SignUp
  url: https://www.esentire.com/get-started
- group: start
  title: ''
  type: Login
  url: https://atlas.esentire.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.esentire.com/legal/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.esentire.com/legal/privacy-policy
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.esentire.com/
- group: auth
  title: ''
  type: Compliance
  url: security/esentire-trust-center.yml
- group: auth
  title: ''
  type: Security
  url: security/esentire-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/esentire-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/esentire-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/esentire-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/esentire-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/esentire-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/esentire-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/esentire-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/esentire-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/esentire-rate-limits.yml
created: '2026-08-12'
description: 'eSentire, Inc. is a Waterloo, Ontario-headquartered cybersecurity company and, in its own words, "the Authority in Managed Detection and Response (MDR)". Founded in 2001, it protects 2,000+ organizations across 80+ countries and 35 industries with 24/7/365 Managed Detection and Response, Digital Forensics and Incident Response (DFIR), and Continuous Threat Exposure Management (CTEM), delivered from its own Atlas Security Operations Platform and staffed Security Operations Centers. Its public machine-readable surface is narrow but real: an llms.txt at the marketing host, an OAuth 2.0 authorization-server and protected-resource metadata pair at api.esentire.com, and an authorization-gated MCP server behind that same host. There is no public OpenAPI, GraphQL schema, or developer portal — the API and the Atlas/Insight portal are reachable only by contracted customers and partners.'
image: https://storage.googleapis.com/vendor-risk-production-default-bucket/eSentire-Navy-1000x1000.png_b7cac947-6768-4bd5-9fa7-98997a9e13f7
layout: provider
mcp_servers:
- description: ''
  name: esentire-mcp.yml
  slug: esentire-mcpyml
modified: '2026-08-12'
name: eSentire
nav: Providers
network: true
overview: 'eSentire publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Cybersecurity, Managed Detection and Response, and Threat Intelligence.


  eSentire''s developer surface includes engineering blog, signup flow, and 19 more developer resources.'
plans:
- name: Esentire Plans Pricing
  plan_count: 0
  slug: esentire-plans-pricing
random_paper: 118
rate_limits:
- limit_count: 0
  name: Esentire Rate Limits
  slug: esentire-rate-limits
scopes:
- name: Esentire Scopes
  scope_count: 0
  slug: esentire-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 20.4
  delta: -1.2
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 13.2
  previous_composite: 21.6
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: authentication
  name: Esentire Authentication
  slug: esentire-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Esentire Domain Security
  slug: esentire-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Esentire Vulnerability Disclosure
  slug: esentire-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Esentire Trust Center
  slug: esentire-trust-center
  summary_line: SOC 2 Type II, ISO/IEC 27001:2022, ISO/IEC 27001:2013, PCI DSS 4.0.1, HIPAA, GDPR, CCPA, PIPEDA, DORA (EU Digital Operational Resilience Act), CIS Controls v8.1, Shared Assessments SIG
slug: esentire
tags:
- Company
- Security
- Cybersecurity
- Managed Detection and Response
- Threat Intelligence
- Incident Response
- Model Context Protocol
- Agents
- OAuth
- SaaS
website: https://www.esentire.com/
---
