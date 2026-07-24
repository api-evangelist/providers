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
- acting_count: 9
  human_in_the_loop: 0
  name: Signeasy Agentic Access
  operation_count: 12
  slug: signeasy-agentic-access
  summary_line: 12 operations · 9 acting
api_count: 5
apis:
- description: Embedded signing and sending flows for iframes and pop-ups.
  name: Signeasy Embedded API
  slug: signeasy-embedded-api
- description: Signature requests composed of originals and templates.
  name: Signeasy Envelopes API
  slug: signeasy-envelopes-api
- description: Master documents used to build signature requests.
  name: Signeasy Originals API
  slug: signeasy-originals-api
- description: Reusable documents with predefined roles and merge fields.
  name: Signeasy Templates API
  slug: signeasy-templates-api
- description: Authenticated account details and envelope credits.
  name: Signeasy Users API
  slug: signeasy-users-api
artifact_total: 13
collections:
- collection_type: open
  name: Signeasy API v3
  slug: open-signeasy
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/signeasy-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/signeasy-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/signeasy-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/signeasy-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/signeasy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/signeasy
- group: company
  title: ''
  type: Website
  url: https://signeasy.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.signeasy.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/signeasy-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/signeasy-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/signeasy-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://signeasy.com/blog/
created: '2026-07-03'
description: Signeasy is an eSignature and intelligent contract management platform used by tens of thousands of businesses to sign, send, and manage documents. The Signeasy API (v3) is a RESTful eSignature API that lets developers send documents for signature (envelopes), embed signing and sending flows directly inside their own web and mobile apps via iframes, manage reusable templates with merge fields, upload original documents, and receive real-time signature lifecycle notifications through webhooks. All endpoints are served from https://api.signeasy.com/v3 and authenticated with OAuth 2.0 Bearer access tokens (sandbox and live).
finops:
- name: Signeasy Finops
  service_category: Business Applications and eSignature
  slug: signeasy-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/signeasy.png
layout: provider
modified: '2026-07-03'
name: Signeasy
nav: Providers
network: true
overview: 'Signeasy publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Embedded API, Envelopes API, Originals API, and 2 more. Tagged areas include eSignature, Electronic Signature, Documents, Contract Management, and Embedded Signing.


  Signeasy''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Signeasy Plans Pricing
  plan_count: 4
  slug: signeasy-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 5
  name: Signeasy Rate Limits
  slug: signeasy-rate-limits
score:
  band: thin
  composite: 39.1
  delta: 0.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 54.9
    developer_ergonomics: 21.7
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 39.1
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Signeasy Authentication
  slug: signeasy-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Signeasy Domain Security
  slug: signeasy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Signeasy Trust Center
  slug: signeasy-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: signeasy
tags:
- eSignature
- Electronic Signature
- Documents
- Contract Management
- Embedded Signing
- Templates
- Webhooks
website: https://signeasy.com/
---
