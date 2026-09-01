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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
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
  score: 28.1
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Weave Agentic Access
  operation_count: 38
  slug: weave-agentic-access
  summary_line: 38 operations · 11 acting
api_count: 1
apis:
- description: Weave's developer platform API for building apps and integrations against Weave communication, scheduling, and payments data. Authorized via OpenID Connect / OAuth 2.0 (authorization_code + client_cre
  name: Weave Platform API
  slug: weave-platform-api
- description: Patient/customer contacts and contact info.
  name: Weave Contacts API
  slug: weave-hq-contacts-api
- description: Platform events and subscription management.
  name: Weave Events API
  slug: weave-hq-events-api
- description: Weave Digital Forms - templates, links, and submissions.
  name: Weave Forms API
  slug: weave-hq-forms-api
- description: Two-way SMS/text messaging with patients.
  name: Weave Messaging API
  slug: weave-hq-messaging-api
- description: Weave Payments methods (text-to-pay, card-on-file).
  name: Weave Payments API
  slug: weave-hq-payments-api
- description: VoIP call records, recordings, voicemails, and call queues.
  name: Weave Phone & Calls API
  slug: weave-hq-phone-calls-api
- description: Review generation, reputation, and business listings.
  name: Weave Reviews API
  slug: weave-hq-reviews-api
- description: Appointments, appointment types, schedules, and calendar events.
  name: Weave Scheduling API
  slug: weave-hq-scheduling-api
artifact_total: 26
collections:
- collection_type: open
  name: Weave Contacts API
  slug: open-weave-contacts-api
- collection_type: open
  name: Weave Contacts Events API
  slug: open-weave-events-api
- collection_type: open
  name: Weave Contacts Forms API
  slug: open-weave-forms-api
- collection_type: open
  name: Weave API
  slug: open-weave-hq
- collection_type: open
  name: Weave Contacts Messaging API
  slug: open-weave-messaging-api
- collection_type: open
  name: Weave Contacts Payments API
  slug: open-weave-payments-api
- collection_type: open
  name: Weave Contacts Phone & Calls API
  slug: open-weave-phone-calls-api
- collection_type: open
  name: Weave Contacts Scheduling API
  slug: open-weave-scheduling-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/weave-capability-edges.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/weave-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/weave-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.getweave.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dp.getweave.com/
- group: docs
  title: ''
  type: Documentation
  url: https://dp.getweave.com/docs
- group: start
  title: ''
  type: SignUp
  url: https://www.getweave.com/demo/
- group: start
  title: ''
  type: Login
  url: https://app.getweave.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.getweave.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.getweave.com/legal/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.getweave.com/legal/privacy/
- group: operate
  title: ''
  type: Support
  url: https://www.weavehelp.com/weavehelp/
- group: company
  title: ''
  type: Blog
  url: https://www.getweave.com/resource-center/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/weave-lab
- group: operate
  title: ''
  type: StatusPage
  url: https://status.getweave.com/
- group: auth
  title: ''
  type: Security
  url: https://www.getweave.com/security/
- group: auth
  title: ''
  type: Compliance
  url: https://www.getweave.com/security/
- group: auth
  title: ''
  type: Authentication
  url: authentication/weave-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/weave-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/weave-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/weave-security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/weave-vulnerability-disclosure.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/weave-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/weave-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/weave-llms.txt
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/weave-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/weave-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/weave-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/weave-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/weave-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/weave-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/getweave
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/weavehq
- group: company
  title: ''
  type: Website
  url: https://www.getweave.com
- group: docs
  title: ''
  type: Documentation
  url: https://dp.getweave.com
- group: commercial
  title: ''
  type: Plans
  url: plans/weave-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/weave-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/weave-finops.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/weave-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/weave-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/weave-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/weave-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/weave-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/weave-scopes.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/weave-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/weave-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/weave-finops.yml
created: '2026-07-17'
description: 'Weave (Weave Communications, Inc., NYSE: WEAV) is an all-in-one customer communication and payments platform built for small and medium healthcare and services businesses — dental, optometry, veterinary, medical, and beyond. Weave brings together a cloud phone system (VoIP), two-way text messaging, appointment scheduling and reminders, online reviews, forms, and integrated payments so practices can automate front-office work, keep schedules full, get paid faster, and collect more reviews. For developers, Weave runs a Developer Platform at dp.getweave.com backed by an OpenID Connect / OAuth 2.0 authorization server (api.weaveconnect.com) that lets partners build apps and integrations against Weave data and events. A Y Combinator company (W14), Weave is HIPAA compliant and maintains ISO 27001 and SOC 2 Type 2 attestations.'
finops:
- name: Weave Finops
  service_category: Business Communication and Payments
  slug: weave-finops
image: https://dp.getweave.com/weave-favicon.svg
layout: provider
modified: '2026-07-21'
name: Weave
nav: Providers
network: true
overview: 'Weave publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Contacts API, Events API, Forms API, and 5 more. Tagged areas include Company, Communications, Messaging, Payments, and Healthcare.


  Weave''s developer surface includes documentation, signup flow, pricing, support, engineering blog, authentication, and 41 more developer resources.'
plans:
- name: Weave Plans Pricing
  plan_count: 4
  slug: weave-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 4
  name: Weave Rate Limits
  slug: weave-rate-limits
scopes:
- name: Weave Scopes
  scope_count: 3
  slug: weave-scopes
  summary_line: 3 scopes
score:
  band: strong
  composite: 65.5
  coverage:
    artifact_dirs: 16
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 100.0
    commercial_clarity: 100.0
    contract_governance: 18.2
    contract_quality: 53.3
    developer_ergonomics: 36.9
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 60.5
  previous_composite: 65.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Health
    regime_id: health
    score: 66.3
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/weave/refs/heads/main/screenshots/weave-2026-08-17T082900.png
security:
- kind: authentication
  name: Weave Authentication
  slug: weave-authentication
  summary_line: oauth2/openIdConnect · 1 scheme
- kind: domain-security
  name: Weave Domain Security
  slug: weave-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Weave Vulnerability Disclosure
  slug: weave-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Weave Trust Center
  slug: weave-trust-center
  summary_line: HIPAA, ISO 27001, SOC 2 Type 2
slug: weave
tags:
- Company
- Communications
- Messaging
- Payments
- Healthcare
- VoIP
- Telephony
- Reviews
- Scheduling
- SMB
- Developer Platform
- Authentication
website: https://www.getweave.com/
---
