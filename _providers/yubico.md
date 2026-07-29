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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 45.3
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: Yubico OTP validation operations.
  name: Yubico Validation API
  slug: yubico-validation-api
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://yubico.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.yubico.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.yubico.com/OTP/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.yubico.com/Software_Projects/YubiCloud_REST_API.html
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.yubico.com/OTP/OTP_Walk-Through.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Yubico
- group: operate
  title: ''
  type: Support
  url: https://support.yubico.com/
- group: company
  title: ''
  type: Blog
  url: https://www.yubico.com/blog/
- group: start
  title: ''
  type: SignUp
  url: https://upgrade.yubico.com/getapikey/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.yubico.com/store/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.yubico.com/support/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.yubico.com/support/terms-conditions/privacy-notice/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.yubico.com/
- group: operate
  title: ''
  type: Deprecation
  url: https://support.yubico.com/hc/en-us/articles/360016614820
- group: build
  title: ''
  type: Packages
  url: packages/yubico-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/yubico-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/yubico-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/yubico-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/yubico-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/yubico-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/yubico-security.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/yubico-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/yubico-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/yubico-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/yubico-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/yubico-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.yubico.com/solutions/cybersecurity-compliance/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/yubico-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/yubico-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.yubico.com/support/issue-rating-system/
- group: auth
  title: ''
  type: TrustCenter
  url: security/yubico-trust-center.yml
created: '2026-07-17'
description: Yubico is the security company behind the YubiKey hardware authentication device and the inventor of the Yubico One-Time Password (OTP). Its public developer surface centers on YubiCloud, a hosted REST service that verifies Yubico OTPs via a signed HTTPS request to api.yubico.com, alongside a broad set of first-party SDKs and libraries for WebAuthn/FIDO2, PIV smart cards, OATH, OTP, and the YubiHSM 2 across Python, .NET, Java, Android, iOS, and C, plus the ykman command-line tool. Yubico co-authored the FIDO U2F standard, ships FIPS 140-3 validated keys, and holds a SOC 2 Type 2 attestation for its enterprise services.
image: https://www.yubico.com/wp-content/uploads/2021/02/Yubico-Logo.png
layout: provider
mcp_servers:
- description: ''
  name: yubico-mcp.yml
  slug: yubico-mcpyml
modified: '2026-07-21'
name: Yubico
nav: Providers
network: true
overview: 'Yubico publishes 1 API on the [APIs.io](https://apis.io/) network: Validation API. Tagged areas include Company, Enterprise, Authentication, Security, and Identity.


  Yubico''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, pricing, and 25 more developer resources.'
random_paper: 3
score:
  band: strong
  composite: 57.7
  delta: 0.1
  facets:
    commercial_clarity: 60.5
    contract_quality: 61.9
    developer_ergonomics: 69.0
    discoverability: 87.0
    governance: 20.8
    operational_transparency: 39.5
  previous_composite: 57.6
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Yubico Authentication
  slug: yubico-authentication
  summary_line: apiKey/hmac-signature · 2 schemes
- kind: domain-security
  name: Yubico Domain Security
  slug: yubico-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Yubico Vulnerability Disclosure
  slug: yubico-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Yubico Trust Center
  slug: yubico-trust-center
  summary_line: SOC 2 Type 2, FIPS 140-3, FIDO2, FIDO U2F, NIST SP 800-63-3 AAL3
slug: yubico
tags:
- Company
- Enterprise
- Authentication
- Security
- Identity
- Hardware Security
- FIDO2
- WebAuthn
- One-Time Password
website: https://yubico.com
---
