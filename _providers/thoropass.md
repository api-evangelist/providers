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
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: OAuth 2.0-secured Partner API for programmatic access to Thoropass audits, evidence requests, controls, monitoring alerts, devices, change requests, training records and vulnerability data, plus a hos
  name: Thoropass Partner API
  slug: thoropass-partner-api
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://thoropass.com/
- group: docs
  title: ''
  type: Documentation
  url: https://help.thoropass.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.thoropass.com/mcp
- group: operate
  title: ''
  type: Support
  url: https://help.thoropass.com/
- group: company
  title: ''
  type: Blog
  url: https://www.thoropass.com/learn/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.thoropass.com/pricing
- group: start
  title: ''
  type: Login
  url: https://app.thoropass.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://thoropass.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.thoropass.com/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.thoropass.com
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.thoropass.com/
- group: auth
  title: ''
  type: Authentication
  url: authentication/thoropass-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/thoropass-scopes.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/thoropass-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/thoropass-well-known.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/thoropass-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/thoropass-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/thoropass-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/thoropass-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/thoropass-llms.txt
created: '2026-07-17'
description: Thoropass is an auditor-led, AI-powered compliance and audit automation platform that combines software with expert auditor services. Its products span continuous compliance monitoring and alerting, automated evidence collection, a global control library, vulnerability scanning, and CREST-accredited penetration testing, helping companies achieve and maintain SOC 2, ISO 27001, HIPAA, PCI DSS and HITRUST. For developers and integration partners, Thoropass exposes a Partner API secured with OAuth 2.0 (Authorization Code + PKCE, refresh tokens, and RFC 7591 dynamic client registration) and a hosted, OAuth-protected Model Context Protocol (MCP) server for AI-agent access to audits, evidence requests, controls, alerts, devices and vulnerability data. Thoropass (formerly Laika) is backed by Bain Capital Ventures.
image: https://cdn.prod.website-files.com/6891db6efb3a962d3fcde7ae/689b377ec946ba9bb8d243f7_Thoropass_Website_OrO-Way-Hero-1.webp
layout: provider
mcp_servers:
- description: ''
  name: Thoropass MCP Server
  slug: thoropass-mcp-server
modified: '2026-07-21'
name: Thoropass
nav: Providers
network: true
overview: 'Thoropass publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Compliance, Compliance Automation, and Audit.


  Thoropass'' developer surface includes documentation, API reference, support, engineering blog, pricing, authentication, and 14 more developer resources.'
random_paper: 8
scopes:
- name: Thoropass Scopes
  scope_count: 24
  slug: thoropass-scopes
  summary_line: 24 scopes · authorizationCode
score:
  band: emerging
  composite: 22.0
  coverage:
    artifact_dirs: 11
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.0
  facets:
    access_clarity: 38.2
    commercial_clarity: 38.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 17.9
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 7.9
  previous_composite: 21.0
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/thoropass/refs/heads/main/screenshots/thoropass-2026-09-02T163551.png
security:
- kind: authentication
  name: Thoropass Authentication
  slug: thoropass-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Thoropass Domain Security
  slug: thoropass-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Thoropass Trust Center
  slug: thoropass-trust-center
  summary_line: trust center published
slug: thoropass
tags:
- Company
- Fintech
- Compliance
- Compliance Automation
- Audit
- Security
- Cybersecurity
- GRC
- SOC 2
- MCP
website: https://thoropass.com/
---
