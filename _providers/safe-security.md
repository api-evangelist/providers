---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 10.0
  scored_at: '2026-09-02'
api_count: 2
apis:
- description: 'The SAFE REST API (v3) gives customers and partners programmatic access to the SAFE One platform: users, assets/technology, findings, risk scenarios, reports, audit-log export, and full lifecycle mana'
  name: SAFE REST API
  slug: safe-rest-api
- description: The Balbix REST API (v1) gives programmatic read access to the asset, vulnerability, misconfiguration, software-inventory and application inventory Balbix discovers - the Continuous Threat Exposure Ma
  name: Balbix REST API
  slug: balbix-rest-api
artifact_total: 16
common:
- group: company
  title: ''
  type: Website
  url: https://safe.security/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.safe.security/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.safe.security/docs/accessing-safe-apis
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/Safe-Security/signal/blob/main/developer-guide.md
- group: operate
  title: ''
  type: Support
  url: https://docs.safe.security/docs/support-and-maintenance
- group: company
  title: ''
  type: Blog
  url: https://safe.security/resources/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://safe.security/feed/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Safe-Security
- group: start
  title: ''
  type: SignUp
  url: https://us.safeone.ai/
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
  type: TrustCenter
  url: security/safe-security-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/safe-security-conformance.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/safe-security-conformance.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/safe-security-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/safe-security-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/safe-security-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/safe-security-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/safe-security-packages.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/safe-security-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: lifecycle/safe-security-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/safe-security-changelog.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/safe-security-plans-pricing.yml
- group: build
  title: ''
  type: Examples
  url: examples/_index.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/safe-security-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/safe-security-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/safe-security-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/safe-security-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/safe-security-authentication.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/safe-security-rate-limits.yml
created: '2026-08-26'
description: 'SAFE Security (SAFE, formerly Lucideus) is a Palo Alto based cyber risk management company whose SAFE One platform quantifies cyber risk in financial terms on the FAIR standard, unifying Cyber Risk Quantification (CRQ), Third-Party Risk Management (TPRM), Continuous Threat Exposure Management (CTEM) and AI Security Posture Management (AI-SPM). The platform is API-first: a versioned REST API at /api/v3 on a per-tenant safeone.ai host lets customers pull users, assets, findings, risk scenarios, reports and audit logs, and drive the 50+ product integrations programmatically, while an open-source Signal specification (MIT, github.com/Safe-Security/signal) defines the JSON contract for pushing CA, VA, EDR and UBA security signals into SAFE from any tool. SAFE acquired RiskLens in 2023 and Balbix in 2025.'
examples:
- key_count: 10
  name: Safe Security Signal High Quality Ca Signal
  slug: safe-security-signal-high-quality-ca-signal
- key_count: 12
  name: Safe Security Signal High Quality Edr Signal
  slug: safe-security-signal-high-quality-edr-signal
- key_count: 11
  name: Safe Security Signal High Quality Uba Signal
  slug: safe-security-signal-high-quality-uba-signal
- key_count: 8
  name: Safe Security Signal Simple Ca Signal
  slug: safe-security-signal-simple-ca-signal
- key_count: 11
  name: Safe Security Signal Simple Edr Signal
  slug: safe-security-signal-simple-edr-signal
- key_count: 8
  name: Safe Security Signal Simple Uba Signal
  slug: safe-security-signal-simple-uba-signal
- key_count: 8
  name: Safe Security Signal Simple Va Signal
  slug: safe-security-signal-simple-va-signal
image: https://safe.security/wp-content/uploads/safe-social.jpg
layout: provider
mcp_servers:
- description: ''
  name: SAFE Security MCP server
  slug: safe-security-mcp-server
modified: '2026-08-26'
name: SAFE Security
nav: Providers
network: true
overview: 'SAFE Security publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Cyber Risk Quantification, Third-Party Risk Management, and Continuous Threat Exposure Management.


  SAFE Security''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, changelog, and 24 more developer resources.'
plans:
- name: Safe Security Plans Pricing
  plan_count: 0
  slug: safe-security-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 1
  name: Safe Security Rate Limits
  slug: safe-security-rate-limits
score:
  band: thin
  composite: 38.3
  coverage:
    artifact_dirs: 17
    catalog_gap: 70.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 18.2
    contract_quality: 6.7
    developer_ergonomics: 54.8
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 65.8
  previous_composite: 38.3
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/safe-security/refs/heads/main/screenshots/safe-security-2026-09-02T154302.png
security:
- kind: authentication
  name: Safe Security Authentication
  slug: safe-security-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Safe Security Domain Security
  slug: safe-security-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Safe Security Vulnerability Disclosure
  slug: safe-security-vulnerability-disclosure
  summary_line: Hackerone · security.txt
- kind: trust-center
  name: Safe Security Trust Center
  slug: safe-security-trust-center
  summary_line: SOC 2 Type 2, SOC 3, ISO 27001:2013, ISO 9001:2015, TX-RAMP
slug: safe-security
tags:
- Company
- Security
- Cyber Risk Quantification
- Third-Party Risk Management
- Continuous Threat Exposure Management
- AI Security Posture Management
- Risk Management
- Governance Risk and Compliance
- FAIR
- Vulnerability Management
website: https://safe.security/
---
