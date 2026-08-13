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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.6
  scored_at: '2026-08-12'
api_count: 1
apis:
- description: PlexTrac's JWT-authenticated REST API (v1 and v2) for managing clients, reports, findings, assets, and content-library writeups, along with tenant/RBAC administration and outbound webhooks. The base U
  name: PlexTrac API
  slug: plextrac-api
artifact_total: 7
asyncapis:
- description: ''
  name: Plextrac Llc Webhooks
  slug: plextrac-llc-webhooks
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/plextrac-llc-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://app.drata.com/trust/9cbbf37d-0c38-11ee-865f-029d78a187d9
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/plextrac-llc-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://plextrac.com/vulnerability-disclosure/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/plextrac-llc-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://plextrac.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.plextrac.com/
- group: docs
  title: ''
  type: APIReference
  url: https://api-docs.plextrac.com/
- group: operate
  title: ''
  type: Support
  url: https://helpcenter.plextrac.com/
- group: company
  title: ''
  type: Blog
  url: https://plextrac.com/resources/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://plextrac.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://plextrac.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://plextrac.com/privacy-policy/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/plextrac-llc-llms.txt
created: '2026-07-17'
description: PlexTrac is a penetration test reporting and proactive exposure management platform that unifies offensive security data from pentests, vulnerability scanners, and bug bounty programs into a single system of record. It automates pentest report authoring (including AI-assisted findings), centralizes and prioritizes vulnerability data by business impact, and drives remediation through workflows integrated with tools such as Jira and ServiceNow. PlexTrac exposes a JWT-authenticated REST API (v1 and v2) for managing clients, reports, findings, assets, and content-library writeups, plus RBAC/tenant administration and outbound webhooks, letting security teams and MSSPs integrate reporting and remediation into their own pipelines.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/plextrac-llc.png
layout: provider
mcp_servers:
- description: ''
  name: plextrac-llc-mcp.yml
  slug: plextrac-llc-mcpyml
modified: '2026-07-20'
name: PlexTrac, LLC
nav: Providers
network: true
overview: 'PlexTrac, LLC publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cybersecurity, Penetration Testing, Vulnerability Management, and Security Reporting.


  The PlexTrac, LLC catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  PlexTrac, LLC''s developer surface includes documentation, API reference, support, engineering blog, pricing, and 9 more developer resources.'
random_paper: 27
score:
  band: thin
  composite: 37.2
  delta: 0.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 51.6
    developer_ergonomics: 21.7
    discoverability: 75.9
    governance: 12.5
    operational_transparency: 10.5
  previous_composite: 37.2
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
security:
- kind: authentication
  name: Plextrac Llc Authentication
  slug: plextrac-llc-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Plextrac Llc Domain Security
  slug: plextrac-llc-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Plextrac Llc Vulnerability Disclosure
  slug: plextrac-llc-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Plextrac Llc Trust Center
  slug: plextrac-llc-trust-center
  summary_line: SOC 2, ISO 27001
slug: plextrac-llc
tags:
- Company
- Cybersecurity
- Penetration Testing
- Vulnerability Management
- Security Reporting
- Exposure Management
- Offensive Security
- MSSP
- Remediation
website: https://plextrac.com/
---
