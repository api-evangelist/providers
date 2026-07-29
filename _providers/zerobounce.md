---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 18.5
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Zerobounce Agentic Access
  operation_count: 2
  slug: zerobounce-agentic-access
  summary_line: 2 operations · 2 acting
api_count: 3
apis:
- description: Real-time and batch email validation API including credit balance, API usage, file submission and retrieval, email finder, domain search, and AI scoring endpoints. Authenticated via api_key query para
  name: ZeroBounce Email Validation API
  slug: email-validation-api
- description: EU-region endpoint of the ZeroBounce v2 email validation API for customers requiring European data residency.
  name: ZeroBounce Email Validation API (EU)
  slug: email-validation-api-eu
- description: The Validation API from ZeroBounce — 2 operation(s) for validation.
  name: ZeroBounce Validation API
  slug: zerobounce-validation-api
artifact_total: 8
collections:
- collection_type: open
  name: ZeroBounce Validate Email plugin
  slug: open-zerobounce
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/zerobounce-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/zerobounce-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/zerobounce-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zerobounce-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/zerobounce-net
- group: company
  title: ''
  type: Website
  url: https://www.zerobounce.net
- group: docs
  title: ''
  type: Documentation
  url: https://www.zerobounce.net/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://www.zerobounce.net/pricing
- group: start
  title: ''
  type: Signup
  url: https://www.zerobounce.net/members/createaccount
- group: build
  title: ''
  type: GitHub
  url: https://github.com/zerobounce
- group: company
  title: ''
  type: Blog
  url: https://www.zerobounce.net/blog/feed
created: '2026-05-11'
description: ZeroBounce is an email validation and deliverability platform that verifies email addresses, detects spam traps and abuse accounts, scores leads, and helps senders reduce bounce rates and protect sender reputation. The platform provides real-time and batch email validation, credit balance checks, file-based validation jobs, email finder, domain search, and AI scoring through a versioned REST API. The ZeroBounce v2 API uses a per- request api_key parameter and supports both global and EU endpoints.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zerobounce.png
layout: provider
modified: '2026-05-11'
name: ZeroBounce
nav: Providers
network: true
overview: 'ZeroBounce publishes 1 API on the [APIs.io](https://apis.io/) network: Validation API. Tagged areas include Email Validation, Email Deliverability, Email Verification, Marketing, and Lead Scoring.


  ZeroBounce''s developer surface includes documentation, pricing, signup flow, GitHub presence, engineering blog, and 6 more developer resources.'
random_paper: 31
score:
  band: emerging
  composite: 24.6
  delta: -1.9
  facets:
    commercial_clarity: 18.4
    contract_quality: 42.4
    developer_ergonomics: 10.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 26.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/zerobounce/refs/heads/main/screenshots/zerobounce-2026-06-20T201831.png
security:
- kind: domain-security
  name: Zerobounce Domain Security
  slug: zerobounce-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Zerobounce Vulnerability Disclosure
  slug: zerobounce-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Zerobounce Trust Center
  slug: zerobounce-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, HIPAA, GDPR
slug: zerobounce
tags:
- Email Validation
- Email Deliverability
- Email Verification
- Marketing
- Lead Scoring
- Anti-Spam
website: https://www.zerobounce.net
---
