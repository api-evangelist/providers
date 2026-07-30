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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Seon Docs Agentic Access
  operation_count: 6
  slug: seon-docs-agentic-access
  summary_line: 6 operations · 4 acting
api_count: 8
apis:
- description: The SEON Email API is a standalone email enrichment tool that helps identify the approximate minimum age of an email address, its provider, and any connected online profiles.
  name: SEON Email API
  slug: email-api
- description: The SEON Phone API unlocks insights into a user's phone number history and social or digital profiles connected to it, helping detect fraud and verify user identity.
  name: SEON Phone API
  slug: phone-api
- description: The AML API from SEON — 1 operation(s) for aml.
  name: SEON AML API
  slug: seon-docs-aml-api
- description: The BIN API from SEON — 1 operation(s) for bin.
  name: SEON BIN API
  slug: seon-docs-bin-api
- description: The Email API from SEON — 1 operation(s) for email.
  name: SEON Email API
  slug: seon-docs-email-api
- description: The Fraud API from SEON — 1 operation(s) for fraud.
  name: SEON Fraud API
  slug: seon-docs-fraud-api
- description: The IP API from SEON — 1 operation(s) for ip.
  name: SEON IP API
  slug: seon-docs-ip-api
- description: The Phone API from SEON — 1 operation(s) for phone.
  name: SEON Phone API
  slug: seon-docs-phone-api
artifact_total: 16
collections:
- collection_type: open
  name: SEON API
  slug: open-seon-docs
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/seon-docs-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/seon-docs-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/seon-docs-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/seon-docs-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/seontechnologies
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/seon-tech
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
- group: company
  title: ''
  type: Website
  url: https://seon.io/
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.seon.io/llms.txt
created: '2026-03-16'
description: SEON is a fraud prevention and AML compliance platform that provides a modular API architecture for fraud detection, identity verification, email enrichment, phone analysis, IP analysis, device fingerprinting, and AML screening. The platform enables businesses to combine multiple fraud signals to score risk and prevent fraudulent transactions.
finops:
- name: Seon Docs Finops
  service_category: API
  slug: seon-docs-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/seon-docs.png
layout: provider
modified: '2026-05-19'
name: SEON
nav: Providers
network: true
overview: 'SEON publishes 6 APIs on the [APIs.io](https://apis.io/) network, including AML API, BIN API, Email API, and 3 more. Tagged areas include AML Compliance, Fraud Prevention, Identity Verification, and Risk Scoring.


  SEON''s developer surface includes authentication, developer portal, documentation, getting-started guide, and 7 more developer resources.'
plans:
- name: Seon Docs Plans Pricing
  plan_count: 3
  slug: seon-docs-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 5
  name: Seon Docs Rate Limits
  slug: seon-docs-rate-limits
score:
  band: thin
  composite: 41.4
  delta: -1.5
  facets:
    commercial_clarity: 47.4
    contract_quality: 55.1
    developer_ergonomics: 39.1
    discoverability: 55.6
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 42.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/seon-docs/refs/heads/main/screenshots/seon-docs-2026-06-20T193713.png
security:
- kind: authentication
  name: Seon Docs Authentication
  slug: seon-docs-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Seon Docs Domain Security
  slug: seon-docs-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Seon Docs Trust Center
  slug: seon-docs-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: seon-docs
tags:
- AML Compliance
- Fraud Prevention
- Identity Verification
- Risk Scoring
website: https://seon.io/
---
