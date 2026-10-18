---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
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
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.9
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 12
  human_in_the_loop: 1
  name: Mailtrap Agentic Access
  operation_count: 23
  slug: mailtrap-agentic-access
  summary_line: 23 operations · 12 acting · 1 human-in-the-loop
api_count: 3
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
artifact_total: 16
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
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/mailtrap/refs/heads/main/plans/mailtrap-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/mailtrap-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/mailtrap/refs/heads/main/rate-limits/mailtrap-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/mailtrap-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/mailtrap/refs/heads/main/finops/mailtrap-finops.yml
  title: ''
  type: FinOps
  url: finops/mailtrap-finops.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/mailtrap/refs/heads/main/capabilities/mailtrap-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/mailtrap-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://mailtrap.io
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/mailtrap/refs/heads/main/agentic-access/mailtrap-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/mailtrap-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/mailtrap/refs/heads/main/security/mailtrap-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mailtrap-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/mailtrap/refs/heads/main/authentication/mailtrap-authentication.yml
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
- group: design
  title: ''
  type: SpectralRules
  url: https://github.com/mailtrap/mailtrap-openapi/blob/4e2f059c72ebaeb85202188ca7f361e02d0341ad/.spectral.yaml
created: '2025-02-06'
description: Mailtrap provides a RESTful email infrastructure API with high deliverability rates, an email sandbox for safe testing, and actionable analytics. It offers SDKs for smooth integration and supports both transactional sending and bulk email delivery.
finops:
- has_sources: false
  method: generated
  name: Mailtrap Finops
  primary_unit: ''
  service_category: API
  slug: mailtrap-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mailtrap.png
layout: provider
modified: '2026-09-16'
name: Mailtrap
nav: Providers
network: true
overview: 'Mailtrap publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Inboxes API, Messages API, and Send API. Tagged areas include Email, Email Delivery, Email Sandbox, Email Testing, and Transactional Email.


  The Mailtrap catalog on APIs.io includes 1 Spectral governance ruleset.


  Mailtrap''s developer surface includes authentication, developer portal, documentation, signup flow, pricing, support, engineering blog, and 15 more developer resources.'
plans:
- name: Mailtrap Plans Pricing
  plan_count: 3
  slug: mailtrap-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 5
  name: Mailtrap Rate Limits
  slug: mailtrap-rate-limits
rules:
- authorship: provider
  effective_rule_count: 41
  extends:
  - spectral:oas
  name: Mailtrap — mailtrap openapi rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: mailtrap-mailtrap-openapi-spectral-rules
score:
  band: thin
  composite: 38.4
  coverage:
    artifact_dirs: 15
    catalog_earned: 51.0
    catalog_earned_first_party: 5.0
    catalog_gap: 64.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.9
  facets:
    access_clarity: 25.0
    contract_governance: 15.2
    contract_quality: 48.0
    developer_ergonomics: 52.4
    discoverability: 78.6
    operational_transparency: 18.4
  previous_composite: 37.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: true
    score: 0.0
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
website: https://mailtrap.io
---
