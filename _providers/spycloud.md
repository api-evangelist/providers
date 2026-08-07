---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 48.0
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Spycloud Agentic Access
  operation_count: 69
  slug: spycloud-agentic-access
  summary_line: 69 operations · 2 acting
api_count: 9
apis:
- description: Employee Account Takeover (EAP) Prevention API — a programmatic interface into your watchlist items found in SpyCloud's recaptured breach and malware data. Query breach records by domain, email, IP, p
  name: SpyCloud Enterprise ATO Prevention API
  slug: spycloud-enterprise-ato-prevention-api
- description: Consumer Account Takeover Prevention API — real-time login-risk and account-creation checks against recaptured consumer breach records by email, username, phone number or IP, plus a k-anonymity zero-k
  name: SpyCloud Consumer ATO Prevention API
  slug: spycloud-consumer-ato-prevention-api
- description: Investigations API — the broadest query surface across SpyCloud's recaptured data, letting analysts pivot across emails, usernames, passwords, domains, IPs, phone numbers, social handles, infected mac
  name: SpyCloud Cybercrime Investigations API
  slug: spycloud-cybercrime-investigations-api
- description: Data Partnership API — bulk partner access to recaptured breach records keyed on a wide set of identifiers including domain, email, username, IP, phone, passwords, and hashed identity documents (healt
  name: SpyCloud Data Partnership API
  slug: spycloud-data-partnership-api
- description: IDLink automated identity analytics — given an email, phone number or username, traverses SpyCloud's recaptured identity graph up to four pivot levels deep to return the correlated identity, supportin
  name: SpyCloud IDLink API
  slug: spycloud-idlink-api
- description: Fraud-detection API returning compromised credit, debit, gift and loyalty card records recaptured from breaches and malware logs, queried by six-character BIN.
  name: SpyCloud Compromised Credit Card API
  slug: spycloud-compromised-credit-card-api
- description: Exposure statistics API returning aggregate counts of recaptured breach and malware exposures for a domain or an email address, over a configurable lookback window, without returning the underlying re
  name: SpyCloud Prospecting API
  slug: spycloud-prospecting-api
- description: NIST SP 800-63B aligned compromised-password screening. Submit a five-hex-digit prefix of an NTLM, SHA-1, SHA-256 or SHA-512 password hash and receive matching hashes, so passwords can be validated at
  name: SpyCloud NIST Password API
  slug: spycloud-nist-password-api
- description: Session Identity Protection (SIP) API — returns stolen session cookies recaptured from infostealer malware for a given cookie domain, with cookie-name and expiration filtering, so session-hijacking ex
  name: SpyCloud Session Identity Protection API
  slug: spycloud-session-identity-protection-api
artifact_total: 15
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/spycloud-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/spycloud-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/spycloud-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/spycloud-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://spycloud.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.spycloud.com/public-sc
- group: docs
  title: ''
  type: Documentation
  url: https://docs.spycloud.com/public-sc/docs
- group: docs
  title: ''
  type: APIReference
  url: https://docs.spycloud.com/public-sc/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.spycloud.com/public-sc/docs/api-guidelines
- group: operate
  title: ''
  type: Support
  url: https://spycloud.com/support/
- group: company
  title: ''
  type: Blog
  url: https://spycloud.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://spycloud.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://spycloud.com/request-a-demo/
- group: start
  title: ''
  type: Login
  url: https://portal.spycloud.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://spycloud.com/legal/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://spycloud.com/legal/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.spycloud.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.spycloud.com/public-sc/page/release-notes-1
- group: auth
  title: ''
  type: Compliance
  url: https://spycloud.com/legal/governance-risk-and-compliance/
- group: auth
  title: ''
  type: TrustCenter
  url: https://app.vanta.com/spycloud.com/trust/itvhddyqxnnf6gi6aatcx
- group: auth
  title: ''
  type: Security
  url: https://spycloud.com/.well-known/security.txt
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/spycloud-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/spycloud-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: well-known/spycloud-api-catalog.json
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/spycloud-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/spycloud-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/spycloud-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/spycloud-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/spycloud-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/spycloud-conformance.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/spycloud-rate-limits.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/spycloud-data-model.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/spycloud-trust-center.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-05'
description: 'SpyCloud is an Austin, Texas based identity threat protection company that operates one of the largest repositories of recaptured darknet data — breach records, infostealer malware logs, phishing captures and combolists — and exposes it programmatically through a family of high-volume REST APIs. Security, fraud, identity and investigations teams query recaptured credentials, session cookies, exposed PII and infected-device telemetry to prevent account takeover, ransomware, session hijacking and online fraud. The public API surface spans nine separately-licensed products: Enterprise (Employee) ATO Prevention, Consumer ATO Prevention, Cybercrime Investigations, Data Partnership, IDLink identity correlation, Compromised Credit Card, Prospecting, NIST Password check, and Session Identity Protection. All are REST/JSON, authenticated with an x-api-key header, IP allow-listed, cursor-paginated at 1,000 records per page, and backed by a 99.9% uptime SLA.'
image: https://spycloud.com/wp-content/uploads/2025/04/bg-img-dotted-lines-1920x700-1-1.png
layout: provider
modified: '2026-08-05'
name: SpyCloud
nav: Providers
network: true
overview: 'SpyCloud publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Enterprise ATO Prevention API, Consumer ATO Prevention API, Cybercrime Investigations API, and 6 more. Tagged areas include Cybersecurity, Threat Intelligence, Identity, Fraud Prevention, and Account Takeover.


  SpyCloud''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 27 more developer resources.'
random_paper: 92
rate_limits:
- limit_count: 0
  name: Spycloud Rate Limits
  slug: spycloud-rate-limits
score:
  band: developing
  composite: 53.3
  facets:
    commercial_clarity: 60.5
    contract_quality: 57.3
    developer_ergonomics: 53.8
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 42.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-06'
security:
- kind: authentication
  name: Spycloud Authentication
  slug: spycloud-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Spycloud Domain Security
  slug: spycloud-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Spycloud Vulnerability Disclosure
  slug: spycloud-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Spycloud Trust Center
  slug: spycloud-trust-center
  summary_line: SOC 2, ISO 27001
slug: spycloud
tags:
- Cybersecurity
- Threat Intelligence
- Identity
- Fraud Prevention
- Account Takeover
- Dark Web
- Breach Data
- Malware
- Authentication
- Security
website: https://spycloud.com/
---
