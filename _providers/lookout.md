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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.0
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: RESTful HTTP interface for streaming and querying mobile threat, device, OS, application, and vulnerability data from a Lookout Mobile Endpoint Security tenant. Uses OAuth 2.0 client-credentials authe
  name: Lookout Mobile Risk API v2
  slug: lookout-mobile-risk-api-v2
artifact_total: 6
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/lookout-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.lookout.com/legal/responsible-disclosure
- group: company
  title: ''
  type: Website
  url: https://www.lookout.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://doc.lookout.com/en/mobile-endpoint-security/mes-apis
- group: docs
  title: ''
  type: Documentation
  url: https://doc.lookout.com/en/mobile-endpoint-security/mes-apis
- group: docs
  title: ''
  type: APIReference
  url: https://doc.lookout.com/en/mobile-endpoint-security/mes-apis/mobile-risk-api-v2/swagger-api-documentation
- group: company
  title: ''
  type: Blog
  url: https://www.lookout.com/blog
- group: operate
  title: ''
  type: Support
  url: https://esupport.lookout.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.lookout.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.lookout.com/legal/privacy-notice
- group: auth
  title: ''
  type: Compliance
  url: https://www.lookout.com/legal/compliance-corner
- group: auth
  title: ''
  type: Authentication
  url: authentication/lookout-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/lookout-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/lookout-conformance.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/lookout-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lookout-domain-security.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/lookout-lifecycle.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/lookout-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/lookout-llms.txt
created: '2026-07-17'
description: Lookout is an endpoint-to-cloud cybersecurity company focused on mobile threat defense and data protection. Its Mobile Endpoint Security (MES) platform detects and responds to mobile-specific threats — phishing, smishing, malicious apps, network attacks, and device compromise — across enterprise and government fleets. Lookout exposes RESTful Mobile Intelligence APIs (the Mobile Risk API v2, SSO Config API, Connector API, and PCP Threat Feed) that stream threat events, device state, and vulnerability data into SIEM, SOAR, XDR, and MDM/EMM tooling using OAuth 2.0 client credentials authentication.
image: https://www.lookout.com/images/lookout-logo.svg
layout: provider
modified: '2026-07-20'
name: Lookout
nav: Providers
network: true
overview: 'Lookout publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cybersecurity, Mobile Security, Endpoint Security, and Threat Intelligence.


  Lookout''s developer surface includes documentation, API reference, engineering blog, support, authentication, and 14 more developer resources.'
random_paper: 4
rate_limits:
- limit_count: 1
  name: Lookout Rate Limits
  slug: lookout-rate-limits
score:
  band: thin
  composite: 27.7
  coverage:
    artifact_dirs: 9
    catalog_gap: 70.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 32.1
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 31.6
  previous_composite: 27.7
  provenance:
    conformance: first-party
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lookout/refs/heads/main/screenshots/lookout-2026-07-25T225520.png
security:
- kind: authentication
  name: Lookout Authentication
  slug: lookout-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Lookout Domain Security
  slug: lookout-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Lookout Vulnerability Disclosure
  slug: lookout-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Lookout Trust Center
  slug: lookout-trust-center
  summary_line: SOC 2, FedRAMP, GDPR
slug: lookout
tags:
- Company
- Cybersecurity
- Mobile Security
- Endpoint Security
- Threat Intelligence
- Mobile Threat Defense
- Data Protection
- SIEM
website: https://www.lookout.com
---
