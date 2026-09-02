---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Tyntec Agentic Access
  operation_count: 10
  slug: tyntec-agentic-access
  summary_line: 10 operations · 3 acting
api_count: 1
apis:
- description: Programmatic two-factor authentication and one-time passwords. Send an OTP to a recipient number (POST /otp), validate the code the user enters (POST /otp/{otp-id}/validate returning VERIFIED, EXPIRED
  name: tyntec 2FA Authentication API
  slug: tyntec-2fa-authentication-api
- description: Send and receive text messages over tyntec's global A2P SMS network. Send via POST /messaging/v1/sms, retrieve delivery status via GET /messaging/v1/messages/{requestId}, receive inbound SMS by webhoo
  name: tyntec SMS API
  slug: tyntec-sms-api
- description: One API for WhatsApp Business, Viber, and SMS. Send single (POST /messages) or bulk (POST /bulks) messages, track delivery status and events, upload and manage media, configure WhatsApp accounts / tem
  name: tyntec Conversations API
  slug: tyntec-conversations-api
- description: HLR reachability/roaming and global number portability lookups (NIS).
  name: tyntec Number Information API
  slug: tyntec-number-information-api
- description: Validate a phone number against reusable criteria templates (Verify API).
  name: tyntec Number Verification API
  slug: tyntec-number-verification-api
- description: Health and version metadata.
  name: tyntec Service API
  slug: tyntec-service-api
- description: Create and manage the criteria templates numbers are checked against.
  name: tyntec Verify Templates API
  slug: tyntec-verify-templates-api
artifact_total: 19
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: tyntec Phone Number Intelligence Number Information API
  slug: open-tyntec-number-information-api
- collection_type: open
  name: tyntec Phone Number Intelligence Number Information Number Verification API
  slug: open-tyntec-number-verification-api
- collection_type: open
  name: tyntec Phone Number Intelligence API
  slug: open-tyntec-number-verification
- collection_type: open
  name: tyntec Phone Number Intelligence Number Information Service API
  slug: open-tyntec-service-api
- collection_type: open
  name: tyntec Phone Number Intelligence Number Information Verify Templates API
  slug: open-tyntec-verify-templates-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/tyntec/api-collection/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/tyntec/api-collection/releases
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tyntec-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tyntec-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tyntec-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tyntec
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tyntec
- group: company
  title: ''
  type: Website
  url: https://www.tyntec.com
- group: docs
  title: ''
  type: Documentation
  url: https://api.tyntec.com/reference/
- group: commercial
  title: ''
  type: Plans
  url: plans/tyntec-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tyntec-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/tyntec-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.tyntec.com/blog
created: '2026-07-11'
description: tyntec is a CPaaS (Communications Platform as a Service) provider whose api.tyntec.com REST APIs let businesses verify, authenticate, and engage mobile consumers worldwide. The platform covers phone number verification and number information (Verify API plus HLR lookup and global number portability), SMS messaging, WhatsApp Business and other chat-app channels via the Conversations API, and two-factor authentication / one-time passwords via the 2FA API. tyntec is an authorized WhatsApp Business Solution Provider. All APIs authenticate with an account API key sent in the apikey request header; tyntec publishes OpenAPI definitions for them in the public tyntec/api-collection GitHub repository.
finops:
- name: Tyntec Finops
  service_category: Communications and Messaging
  slug: tyntec-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tyntec.png
layout: provider
modified: '2026-07-11'
name: tyntec
nav: Providers
network: true
overview: 'tyntec publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Number Information API, Number Verification API, Service API, and 1 more. Tagged areas include Number Verification, CPaaS, SMS, WhatsApp, and Phone Number Intelligence.


  tyntec''s developer surface includes authentication, documentation, engineering blog, and 10 more developer resources.'
plans:
- name: Tyntec Plans Pricing
  plan_count: 2
  slug: tyntec-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 4
  name: Tyntec Rate Limits
  slug: tyntec-rate-limits
score:
  band: thin
  composite: 28.1
  coverage:
    artifact_dirs: 9
    catalog_gap: 55.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 17.2
    developer_ergonomics: 35.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 50.0
  open_source:
    applies: true
    score: 25.0
  previous_composite: 28.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 4
      marker_coverage: 100.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 16.7
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Tyntec Authentication
  slug: tyntec-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Tyntec Domain Security
  slug: tyntec-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tyntec
tags:
- Number Verification
- CPaaS
- SMS
- WhatsApp
- Phone Number Intelligence
- HLR Lookup
- Two-Factor Authentication
- OTP
- Messaging
- Number Portability
website: https://www.tyntec.com
---
