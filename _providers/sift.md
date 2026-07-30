---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
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
- acting_count: 13
  human_in_the_loop: 0
  name: Sift Agentic Access
  operation_count: 20
  slug: sift-agentic-access
  summary_line: 20 operations · 13 acting
api_count: 7
apis:
- description: Apply and retrieve decisions against users, orders, sessions, and content.
  name: Sift Decisions API
  slug: sift-decisions-api
- description: Stream user activity to Sift's machine learning models.
  name: Sift Events API
  slug: sift-events-api
- description: Legacy API for labeling users to train models.
  name: Sift Labels API
  slug: sift-labels-api
- description: Manage sub-merchant profiles for payment service providers.
  name: Sift PSP Merchant Management API
  slug: sift-psp-merchant-management-api
- description: Retrieve real-time Sift Scores per abuse type.
  name: Sift Score API
  slug: sift-score-api
- description: One-time passcode (OTP) step-up verification.
  name: Sift Verification API
  slug: sift-verification-api
- description: Retrieve the status and results of Sift Workflow runs.
  name: Sift Workflows API
  slug: sift-workflows-api
artifact_total: 14
collections:
- collection_type: open
  name: Sift API
  slug: open-sift
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sift-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sift-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sift-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SiftScience
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sift-science
- group: company
  title: ''
  type: Website
  url: https://sift.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.sift.com/docs
- group: commercial
  title: ''
  type: Plans
  url: plans/sift-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sift-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/sift-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://sift.com/blog
created: '2026-07-12'
description: Sift is a digital trust and safety platform that uses machine learning to detect and prevent online fraud and abuse - payment fraud, account takeover, account abuse, content abuse, and promotion abuse. Applications stream user events to the Sift Events API, retrieve real-time risk Sift Scores (0-100) per abuse type, and act on them through the Decisions API, automated Workflows, verification (OTP), and PSP merchant risk management. Sift exposes a documented public REST API over HTTPS at https://api.sift.com with API-key authentication.
finops:
- name: Sift Finops
  service_category: Security and Fraud Prevention
  slug: sift-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sift.png
layout: provider
modified: '2026-07-12'
name: Sift
nav: Providers
network: true
overview: 'Sift publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Decisions API, Events API, Labels API, and 4 more. Tagged areas include Fraud Detection, Fraud Prevention, Risk, Trust and Safety, and Machine Learning.


  Sift''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Sift Plans Pricing
  plan_count: 3
  slug: sift-plans-pricing
random_paper: 28
rate_limits:
- limit_count: 3
  name: Sift Rate Limits
  slug: sift-rate-limits
score:
  band: thin
  composite: 39.5
  delta: -2.5
  facets:
    commercial_clarity: 39.5
    contract_quality: 60.2
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 42.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Sift Authentication
  slug: sift-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Sift Domain Security
  slug: sift-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sift
tags:
- Fraud Detection
- Fraud Prevention
- Risk
- Trust and Safety
- Machine Learning
- Payment Fraud
- Account Takeover
- Chargebacks
- Digital Trust
website: https://sift.com
---
