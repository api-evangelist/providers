---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
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
- acting_count: 5
  human_in_the_loop: 0
  name: Veriff Com Agentic Access
  operation_count: 12
  slug: veriff-com-agentic-access
  summary_line: 12 operations · 5 acting
api_count: 6
apis:
- description: List verification attempts within a session.
  name: Veriff Attempts API
  slug: veriff-com-attempts-api
- description: Retrieve verification decisions and registry results.
  name: Veriff Decisions API
  slug: veriff-com-decisions-api
- description: Upload and retrieve document, face, and NFC media.
  name: Veriff Media API
  slug: veriff-com-media-api
- description: Retrieve verified person data.
  name: Veriff Person API
  slug: veriff-com-person-api
- description: Create, update, and delete verification sessions.
  name: Veriff Sessions API
  slug: veriff-com-sessions-api
- description: Retrieve AML PEP, sanctions, and adverse-media screening results.
  name: Veriff Watchlist Screening API
  slug: veriff-com-watchlist-screening-api
artifact_total: 14
collections:
- collection_type: open
  name: Veriff Public API
  slug: open-veriff-com
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/veriff-com-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/veriff-com-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/veriff-com-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/veriff-com-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/veriff
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/veriff
- group: company
  title: ''
  type: Website
  url: https://www.veriff.com
- group: docs
  title: ''
  type: Documentation
  url: https://devdocs.veriff.com
- group: commercial
  title: ''
  type: Plans
  url: plans/veriff-com-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/veriff-com-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/veriff-com-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.veriff.com/feed
created: '2026-07-01'
description: Veriff is a global identity verification platform that combines AI and human review to verify people online. Its API-first IDV stack covers document and biometric (face-match, liveness) verification, KYC/AML onboarding, proof of address, and database/watchlist (PEP and sanctions) screening, orchestrated around verification sessions with HMAC-secured REST endpoints and decision/event webhooks.
finops:
- name: Veriff Com Finops
  service_category: Identity and Fraud
  slug: veriff-com-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/veriff-com.png
layout: provider
modified: '2026-07-01'
name: Veriff
nav: Providers
network: true
overview: 'Veriff publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Attempts API, Decisions API, Media API, and 3 more. Tagged areas include Identity Verification, KYC, AML, Biometrics, and Document Verification.


  Veriff''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Veriff Com Plans Pricing
  plan_count: 3
  slug: veriff-com-plans-pricing
random_paper: 34
rate_limits:
- limit_count: 2
  name: Veriff Com Rate Limits
  slug: veriff-com-rate-limits
score:
  band: thin
  composite: 38.1
  delta: -3.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 60.2
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 41.1
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
security:
- kind: authentication
  name: Veriff Com Authentication
  slug: veriff-com-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Veriff Com Domain Security
  slug: veriff-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Veriff Com Vulnerability Disclosure
  slug: veriff-com-vulnerability-disclosure
  summary_line: disclosure policy published
slug: veriff-com
tags:
- Identity Verification
- KYC
- AML
- Biometrics
- Document Verification
- Fraud Prevention
website: https://www.veriff.com
---
