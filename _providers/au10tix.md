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
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.4
  scored_at: '2026-08-10'
api_count: 5
apis:
- description: Orchestrates identity verification workflows (the Back Office Server, "BOS"). Creates a verification session/workflow, accepts document and selfie media, and returns a unique session/document identifi
  name: AU10TIX Identity Verification API
  slug: au10tix-identity-verification-api
- description: Authenticates government-issued ID documents (passports, driver's licenses, national ID cards) using document structure checks, data integrity validation, and digital forensic analysis, returning extr
  name: AU10TIX Document Authentication API
  slug: au10tix-document-authentication-api
- description: Compares a captured selfie against the portrait on a verified ID document (1:1 face match) and performs passive/active liveness and deepfake detection to confirm a genuine, present person.
  name: AU10TIX Face Comparison & Liveness API
  slug: au10tix-face-liveness-api
- description: Retrieves the structured result of a verification session by its session/document identifier (polling with retry/backoff), returning the verification status (e.g. VERIFIED, FAILED, REVIEW) and the con
  name: AU10TIX Results API
  slug: au10tix-results-api
- description: Pushes verification decisions to a customer-registered callback URL the moment a workflow reaches a terminal state, removing the need to poll for status. Payload schemas are documented in AU10TIX's au
  name: AU10TIX Webhooks API
  slug: au10tix-webhooks-api
artifact_total: 11
collections:
- collection_type: open
  name: AU10TIX API
  slug: open-au10tix
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/au10tix-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/au10tix-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/au10tix
- group: company
  title: ''
  type: Website
  url: https://www.au10tix.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.au10tix.com/products/platform/
- group: commercial
  title: ''
  type: Plans
  url: plans/au10tix-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/au10tix-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/au10tix-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.au10tix.com/blog/
created: '2026-06-25'
description: AU10TIX is an identity verification and document authentication provider delivering KYC, document analysis, biometric face comparison, liveness, and fraud detection through a single REST API (the Back Office Server, "BOS") and web/mobile SDKs. The platform orchestrates verification workflows/sessions, returns structured results, and notifies clients via webhooks.
finops:
- name: Au10Tix Finops
  service_category: Identity and Fraud
  slug: au10tix-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/au10tix.png
layout: provider
modified: '2026-06-25'
name: AU10TIX
nav: Providers
network: true
overview: 'AU10TIX publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Identity Verification API, Document Authentication API, Face Comparison & Liveness API, and 2 more. Tagged areas include Identity Verification, Document Authentication, KYC, Biometrics, and Fraud Detection.


  AU10TIX''s developer surface includes authentication, documentation, engineering blog, and 6 more developer resources.'
plans:
- name: Au10Tix Plans Pricing
  plan_count: 1
  slug: au10tix-plans-pricing
random_paper: 72
rate_limits:
- limit_count: 3
  name: Au10Tix Rate Limits
  slug: au10tix-rate-limits
score:
  band: thin
  composite: 29.7
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 32.3
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 29.7
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/au10tix/refs/heads/main/screenshots/au10tix-2026-07-25T201647.png
security:
- kind: authentication
  name: Au10Tix Authentication
  slug: au10tix-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Au10Tix Domain Security
  slug: au10tix-domain-security
  summary_line: TLSv1.3 · DMARC
slug: au10tix
tags:
- Identity Verification
- Document Authentication
- KYC
- Biometrics
- Fraud Detection
website: https://www.au10tix.com
---
