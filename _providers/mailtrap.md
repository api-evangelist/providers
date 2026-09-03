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
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 12
  human_in_the_loop: 1
  name: Mailtrap Agentic Access
  operation_count: 23
  slug: mailtrap-agentic-access
  summary_line: 23 operations · 12 acting · 1 human-in-the-loop
api_count: 2
apis:
- baseURL: https://send.api.mailtrap.io
  baseurl_source: declared
  description: Manage sandbox inboxes
  name: Mailtrap Inboxes API
  slug: mailtrap-inboxes-api
- baseURL: https://send.api.mailtrap.io
  baseurl_source: declared
  description: Inspect captured messages
  name: Mailtrap Messages API
  slug: mailtrap-messages-api
- baseURL: https://send.api.mailtrap.io
  baseurl_source: declared
  description: Send transactional and bulk emails
  name: Mailtrap Send API
  slug: mailtrap-send-api
artifact_total: 15
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Mailtrap Email Sending API
  slug: open-mailtrap-email-api
- collection_type: open
  name: Mailtrap Email Sandbox API
  slug: open-mailtrap-email-sandbox
- collection_type: open
  name: Mailtrap Email Sending Inboxes API
  slug: open-mailtrap-inboxes-api
- collection_type: open
  name: Mailtrap Email Sending Inboxes Messages API
  slug: open-mailtrap-messages-api
- collection_type: open
  name: Mailtrap Email Sending Inboxes Send API
  slug: open-mailtrap-send-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/mailtrap-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mailtrap-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mailtrap-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mailtrap
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mailtrap
- group: start
  title: ''
  type: Portal
  url: https://mailtrap.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.mailtrap.io/
- group: start
  title: ''
  type: Signup
  url: https://mailtrap.io/register/signup
- group: start
  title: ''
  type: Login
  url: https://mailtrap.io/users/sign_in
- group: commercial
  title: ''
  type: Pricing
  url: https://mailtrap.io/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.mailtrap.io/
- group: operate
  title: ''
  type: Support
  url: https://help.mailtrap.io/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mailtrap.io/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mailtrap.io/privacy-policy/
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.mailtrap.io/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://mailtrap.io/blog/feed/
created: '2025-02-06'
description: Mailtrap provides a RESTful email infrastructure API with high deliverability rates, an email sandbox for safe testing, and actionable analytics. It offers SDKs for smooth integration and supports both transactional sending and bulk email delivery.
finops:
- name: Mailtrap Finops
  service_category: API
  slug: mailtrap-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mailtrap.png
layout: provider
modified: '2026-05-19'
name: Mailtrap
nav: Providers
network: true
overview: 'Mailtrap publishes 3 APIs on the [APIs.io](https://apis.io/) network: Inboxes API, Messages API, and Send API. Tagged areas include Email, Email Delivery, Email Sandbox, Email Testing, and Transactional Email.


  Mailtrap''s developer surface includes authentication, developer portal, documentation, signup flow, pricing, support, engineering blog, and 9 more developer resources.'
plans:
- name: Mailtrap Plans Pricing
  plan_count: 3
  slug: mailtrap-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 5
  name: Mailtrap Rate Limits
  slug: mailtrap-rate-limits
score:
  band: developing
  composite: 40.4
  coverage:
    artifact_dirs: 11
    catalog_gap: 69.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 32.9
    commercial_clarity: 32.9
    contract_governance: 0.0
    contract_quality: 53.3
    developer_ergonomics: 52.4
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 18.4
  previous_composite: 40.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mailtrap/refs/heads/main/screenshots/mailtrap-2026-06-20T184904.png
security:
- kind: authentication
  name: Mailtrap Authentication
  slug: mailtrap-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Mailtrap Domain Security
  slug: mailtrap-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mailtrap
tags:
- Email
- Email Delivery
- Email Sandbox
- Email Testing
- Transactional Email
website: https://mailtrap.io/
---
