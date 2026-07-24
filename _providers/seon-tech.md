---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Seon Tech Agentic Access
  operation_count: 6
  slug: seon-tech-agentic-access
  summary_line: 6 operations · 4 acting
api_count: 10
apis:
- description: SEON Device Intelligence is the device-fingerprinting product surfaced through JavaScript, iOS, Android, Flutter, React Native, Cordova, and Unity SDKs. Captured device signals (True Device ID, hashes
  name: SEON Device Intelligence
  slug: device-intelligence
- description: SEON Identity Verification (IDV) is an AI-powered identity verification product combining document checks, biometric liveness, and enriched fraud signals. Integration is via native iOS and Android SDK
  name: SEON Identity Verification
  slug: idv
- description: SEON Orchestration lets customers compose multi-step fraud, KYC, and risk workflows that combine SEON enrichment with third-party providers. Integration is via the Orchestration SDKs for iOS, Android,
  name: SEON Orchestration
  slug: orchestration
- description: User Session Monitoring streams in-session behavioral, device, and risk signals for continuous account-takeover and session-hijacking detection across web, iOS, and Android. Delivered via dedicated St
  name: SEON User Session Monitoring
  slug: user-session-monitoring
- description: The AML API from SEON — 1 operation(s) for aml.
  name: SEON AML API
  slug: seon-tech-aml-api
- description: The BIN API from SEON — 1 operation(s) for bin.
  name: SEON BIN API
  slug: seon-tech-bin-api
- description: The Email API from SEON — 1 operation(s) for email.
  name: SEON Email API
  slug: seon-tech-email-api
- description: The Fraud API from SEON — 1 operation(s) for fraud.
  name: SEON Fraud API
  slug: seon-tech-fraud-api
- description: The IP API from SEON — 1 operation(s) for ip.
  name: SEON IP API
  slug: seon-tech-ip-api
- description: The Phone API from SEON — 1 operation(s) for phone.
  name: SEON Phone API
  slug: seon-tech-phone-api
artifact_total: 18
collections:
- collection_type: open
  name: SEON API
  slug: open-seon-tech
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/seon-tech-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/seon-tech-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/seon-tech-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/seon-tech-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://seon.io/
- group: start
  title: ''
  type: Portal
  url: https://docs.seon.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.seon.io/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.seon.io/getting-started
- group: auth
  title: ''
  type: Authentication
  url: https://docs.seon.io/api-reference/introduction
- group: start
  title: ''
  type: Signup
  url: https://admin.seon.io/sign-up
- group: start
  title: ''
  type: Login
  url: https://admin.seon.io/
- group: commercial
  title: ''
  type: Pricing
  url: https://seon.io/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.seon.io/
- group: company
  title: ''
  type: Blog
  url: https://seon.io/resources/
- group: company
  title: ''
  type: BlogRSS
  url: https://seon.io/resources/feed/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://seon.io/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://seon.io/privacy-policy/
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://seon.io/security/
- group: auth
  title: ''
  type: ResponsibleDisclosure
  url: https://seon.io/rdp/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/seontechnologies
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/seon-tech
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/seon_tech
- group: company
  title: ''
  type: Crunchbase
  url: https://www.crunchbase.com/organization/seon-technologies
- group: other
  title: ''
  type: Customers
  url: https://seon.io/customers/
- group: other
  title: ''
  type: CaseStudies
  url: https://seon.io/case-studies/
- group: company
  title: ''
  type: Careers
  url: https://seon.io/careers/
- group: operate
  title: ''
  type: ContactUs
  url: https://seon.io/contact-us/
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.seon.io/llms.txt
created: '2026-05-25'
description: SEON is a Budapest-headquartered fraud prevention, AML compliance, and digital footprint analysis platform that exposes a modular REST API for fraud scoring, identity verification, email enrichment, phone enrichment, IP intelligence, BIN lookup, AML screening, device intelligence, and identity verification (IDV). SEON combines real-time enrichment of email, phone, IP, BIN, and device signals with customer-defined rules and machine learning to score risk and prevent fraud, account takeover, multi-accounting, and money laundering across digital channels.
finops:
- name: Seon Tech Finops
  service_category: API
  slug: seon-tech-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/seon-tech.png
layout: provider
modified: '2026-05-25'
name: SEON
nav: Providers
network: true
overview: 'SEON publishes 6 APIs on the [APIs.io](https://apis.io/) network, including AML API, BIN API, Email API, and 3 more. Tagged areas include AML Compliance, Device Intelligence, Digital Footprint, Fraud Prevention, and Identity Verification.


  SEON''s developer surface includes authentication, developer portal, documentation, getting-started guide, signup flow, pricing, engineering blog, and 21 more developer resources.'
plans:
- name: Seon Tech Plans Pricing
  plan_count: 3
  slug: seon-tech-plans-pricing
random_paper: 35
rate_limits:
- limit_count: 5
  name: Seon Tech Rate Limits
  slug: seon-tech-rate-limits
score:
  band: developing
  composite: 54.9
  delta: 0.0
  facets:
    commercial_clarity: 92.1
    contract_quality: 53.1
    developer_ergonomics: 41.3
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 63.2
  previous_composite: 54.9
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/seon-tech/refs/heads/main/screenshots/seon-tech-2026-06-20T193713.png
security:
- kind: authentication
  name: Seon Tech Authentication
  slug: seon-tech-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Seon Tech Domain Security
  slug: seon-tech-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Seon Tech Trust Center
  slug: seon-tech-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: seon-tech
tags:
- AML Compliance
- Device Intelligence
- Digital Footprint
- Fraud Prevention
- Identity Verification
- Risk Scoring
website: https://seon.io/
---
