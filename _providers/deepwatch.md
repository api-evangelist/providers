---
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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 15.1
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: The authenticated GraphQL API behind the Deepwatch Security Center console (devportal.deepwatch.com). The endpoint is an AWS AppSync GraphQL service at devportalapi.deepwatch.com/graphql/ with a realt
  name: Deepwatch Security Center API
  slug: deepwatch-security-center-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/deepwatch-trust-center.yml
- group: company
  title: ''
  type: Website
  url: https://www.deepwatch.com/
- group: company
  title: ''
  type: Blog
  url: https://www.deepwatch.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.deepwatch.com/feed/
- group: operate
  title: ''
  type: Support
  url: https://www.deepwatch.com/support/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/deepwatch
- group: start
  title: ''
  type: Login
  url: https://login.deepwatch.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://legal.deepwatch.com/tscs-2025-2
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.deepwatch.com/privacy-policy/
- group: auth
  title: ''
  type: Compliance
  url: https://www.deepwatch.com/trust/
- group: auth
  title: ''
  type: Security
  url: https://www.deepwatch.com/trust/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.deepwatch.com/
- group: operate
  title: ''
  type: SLA
  url: https://legal.deepwatch.com/sla-102025
- group: company
  title: ''
  type: Partners
  url: https://www.deepwatch.com/technology-partners/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/deepwatch-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/deepwatch-well-known.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/deepwatch-openid-configuration.json
- group: auth
  title: ''
  type: Authentication
  url: authentication/deepwatch-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/deepwatch-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/deepwatch-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/deepwatch-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/deepwatch-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/deepwatch-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/deepwatch-vulnerability-disclosure.yml
created: '2026-08-01'
description: 'Deepwatch is a US managed security services provider delivering AI-native managed detection and response (MDR) governed by human security experts. Its Guardian platform and Security Center console aggregate and correlate telemetry from a customer''s existing SIEM, EDR, cloud, identity, network and vulnerability tooling — Splunk, CrowdStrike Falcon Next-Gen SIEM, Microsoft Sentinel, Google SecOps, SentinelOne, Microsoft Defender, Carbon Black, Okta, Entra ID, Tenable, Qualys, Wiz, Palo Alto and Fortinet among them — rather than requiring a rip-and-replace. Services span MDR, managed endpoint detection and response, continuous threat exposure management, vulnerability management, managed firewall, dark web monitoring and active response, with the NEXA agentic-AI ecosystem layered across detection, investigation and response. Deepwatch publishes contractual service-level commitments (99.9% platform uptime, 10-minute critical MTTD), a SafeBase trust center and an llms.txt, but
  exposes no public API documentation: the customer-facing surface is an authenticated GraphQL API behind the Security Center console.'
image: https://www.deepwatch.com/wp-content/uploads/cropped-DeepWatch-Guardian-Orange-192x192.png
layout: provider
modified: '2026-08-01'
name: Deepwatch
nav: Providers
network: true
overview: 'Deepwatch publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cybersecurity, Managed Detection and Response, Security Operations, and Threat Intelligence.


  Deepwatch''s developer surface includes engineering blog, support, authentication, and 21 more developer resources.'
random_paper: 4
scopes:
- name: Deepwatch Scopes
  scope_count: 7
  slug: deepwatch-scopes
  summary_line: 7 scopes · authorizationCode/implicit/deviceCode
score:
  band: emerging
  composite: 26.0
  coverage:
    artifact_dirs: 10
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 28.9
  previous_composite: 26.0
  provenance:
    conformance: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/deepwatch/refs/heads/main/screenshots/deepwatch-2026-08-07T164239.png
security:
- kind: authentication
  name: Deepwatch Authentication
  slug: deepwatch-authentication
  summary_line: openIdConnect/oauth2 · 2 schemes
- kind: domain-security
  name: Deepwatch Domain Security
  slug: deepwatch-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Deepwatch Vulnerability Disclosure
  slug: deepwatch-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Deepwatch Trust Center
  slug: deepwatch-trust-center
  summary_line: SOC 2 Type II, ISO/IEC 27001:2022, ISO/IEC 42001:2023, PCI DSS
slug: deepwatch
tags:
- Company
- Cybersecurity
- Managed Detection and Response
- Security Operations
- Threat Intelligence
- Vulnerability Management
- Managed Security Services
- Agentic AI
website: https://www.deepwatch.com/
---
