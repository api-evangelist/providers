---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - rate-limits
  - security
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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 17.6
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: 'Read-only REST API (v1) for programmatic access to Balbix Assets and their associated Vulnerabilities, Misconfigurations, Software Inventory, Applications and application Artifacts. Authentication is '
  name: Balbix REST API
  slug: balbix-rest-api
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://safe.security/
- group: company
  title: ''
  type: LegacyWebsite
  url: https://www.balbix.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.safe.security/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.safe.security/balbixhelp/docs/dashboard-overview
- group: docs
  title: ''
  type: APIReference
  url: https://docs.safe.security/balbixhelp/docs/balbix-rest-api-guide-v20
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.safe.security/balbixhelp/docs/implementing-the-ctem-cycle-with-balbix
- group: operate
  title: ''
  type: Support
  url: https://docs.safe.security/balbixhelp/docs/support.md
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.balbix.com/hc/en-us
- group: start
  title: ''
  type: Login
  url: https://app.balbix.net/
- group: company
  title: ''
  type: Blog
  url: https://safe.security/resources/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://safe.security/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://safe.security/privacy-policy/
- group: auth
  title: ''
  type: Security
  url: https://safe.security/security/
- group: auth
  title: ''
  type: Compliance
  url: https://safe.security/security/
- group: auth
  title: ''
  type: TrustCenter
  url: security/balbix-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/balbix-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/balbix-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/balbix-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/balbix-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/balbix-well-known.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/balbix-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/balbix-rate-limits.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/balbix-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/balbix-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/balbix-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/balbix-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/balbix-llms.txt
created: '2026-08-02'
description: Balbix is a cyber risk and exposure management platform founded in 2015 in San Jose, California. The Balbix Security Cloud (Balbix D3) ingests telemetry from 70+ security and IT systems through pre-built connectors and sensors, unifies it into a single asset, application, vulnerability and software inventory model, and quantifies breach risk in dollar terms so security teams can prioritize remediation. The platform covers cyber asset attack surface management (CAASM), continuous threat exposure management (CTEM), AppSec risk, and cyber risk quantification (CRQ), and ships BIX, a natural-language AI assistant for security posture questions. Balbix exposes a read-only REST API (v1) for programmatic access to assets, vulnerabilities, misconfigurations, software inventory, applications and application artifacts. Balbix was acquired by SAFE Security in November 2025; balbix.com now redirects to safe.security and the Balbix product documentation is published as the "Balbix Help" section
  of docs.safe.security.
layout: provider
modified: '2026-08-02'
name: Balbix
nav: Providers
network: true
overview: 'Balbix publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cybersecurity, Security, Risk Management, and Vulnerability Management.


  Balbix''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, changelog, and 20 more developer resources.'
random_paper: 17
rate_limits:
- limit_count: 1
  name: Balbix Rate Limits
  slug: balbix-rate-limits
scopes:
- name: Balbix Scopes
  scope_count: 7
  slug: balbix-scopes
  summary_line: 7 scopes · authorizationCode
score:
  band: thin
  composite: 35.7
  coverage:
    artifact_dirs: 14
    catalog_gap: 72.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 57.1
    discoverability: 72.2
    governance: 18.2
    operational_transparency: 47.4
  previous_composite: 35.7
  provenance:
    conformance: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/balbix/refs/heads/main/screenshots/balbix-2026-08-07T162112.png
security:
- kind: authentication
  name: Balbix Authentication
  slug: balbix-authentication
  summary_line: http/apiKey/openIdConnect · 5 schemes
- kind: domain-security
  name: Balbix Domain Security
  slug: balbix-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Balbix Vulnerability Disclosure
  slug: balbix-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Balbix Trust Center
  slug: balbix-trust-center
  summary_line: SOC 2 Type 2, SOC 3, ISO 27001:2013, ISO 9001:2015, TX-RAMP
slug: balbix
tags:
- Company
- Cybersecurity
- Security
- Risk Management
- Vulnerability Management
- Exposure Management
- Asset Management
- Cyber Asset Attack Surface Management
- Continuous Threat Exposure Management
- Cyber Risk Quantification
- Application Security
website: https://safe.security/
---
