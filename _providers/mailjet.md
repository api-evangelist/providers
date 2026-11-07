---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
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
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Mailjet Agentic Access
  operation_count: 20
  slug: mailjet-agentic-access
  summary_line: 20 operations · 10 acting
api_count: 1
apis:
- baseURL: https://api.mailjet.com/v3
  baseurl_source: declared
  description: Manage campaigns and drafts
  name: Mailjet Campaigns API
  slug: mailjet-campaigns-api
- baseURL: https://api.mailjet.com/v3
  baseurl_source: declared
  description: Manage contact lists and recipients
  name: Mailjet Contact Lists API
  slug: mailjet-contact-lists-api
- baseURL: https://api.mailjet.com/v3
  baseurl_source: declared
  description: Manage contacts and properties
  name: Mailjet Contacts API
  slug: mailjet-contacts-api
- baseURL: https://api.mailjet.com/v3
  baseurl_source: declared
  description: Retrieve real-time event data
  name: Mailjet Event API
  slug: mailjet-event-api
- baseURL: https://api.mailjet.com/v3
  baseurl_source: declared
  description: Send transactional and marketing emails
  name: Mailjet Send API
  slug: mailjet-send-api
- baseURL: https://api.mailjet.com/v3
  baseurl_source: declared
  description: Manage verified sender addresses
  name: Mailjet Senders API
  slug: mailjet-senders-api
- baseURL: https://api.mailjet.com/v3
  baseurl_source: declared
  description: Retrieve aggregated sending statistics
  name: Mailjet Statistics API
  slug: mailjet-statistics-api
- baseURL: https://api.mailjet.com/v3
  baseurl_source: declared
  description: Manage reusable email templates
  name: Mailjet Templates API
  slug: mailjet-templates-api
artifact_total: 25
collections:
- collection_type: open
  name: Mailjet Email Campaigns API
  slug: open-mailjet-campaigns-api
- collection_type: open
  name: Mailjet Email Campaigns Contact Lists API
  slug: open-mailjet-contact-lists-api
- collection_type: open
  name: Mailjet Email Campaigns Contacts API
  slug: open-mailjet-contacts-api
- collection_type: open
  name: Mailjet Email API
  slug: open-mailjet-email-api
- collection_type: open
  name: Mailjet Email Campaigns Event API
  slug: open-mailjet-event-api
- collection_type: open
  name: Mailjet Email Campaigns Send API
  slug: open-mailjet-send-api
- collection_type: open
  name: Mailjet Email Campaigns Senders API
  slug: open-mailjet-senders-api
- collection_type: open
  name: Mailjet Email Campaigns Statistics API
  slug: open-mailjet-statistics-api
- collection_type: open
  name: Mailjet Email Campaigns Templates API
  slug: open-mailjet-templates-api
common:
- group: commercial
  href: https://artifacts.apis.io/mailjet/plans/mailjet-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/mailjet-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/mailjet/rate-limits/mailjet-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/mailjet-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/mailjet/finops/mailjet-finops.yml
  title: ''
  type: FinOps
  url: finops/mailjet-finops.yml
- group: other
  href: https://artifacts.apis.io/mailjet/capabilities/mailjet-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/mailjet-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://www.mailjet.com/
- group: agent
  href: https://artifacts.apis.io/mailjet/agentic-access/mailjet-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/mailjet-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/mailjet/security/mailjet-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mailjet-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/mailjet/authentication/mailjet-authentication.yml
  title: ''
  type: Authentication
  url: authentication/mailjet-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mailjet
- group: start
  title: ''
  type: Portal
  url: https://dev.mailjet.com/
- group: start
  title: ''
  type: Signup
  url: https://app.mailjet.com/signup
- group: start
  title: ''
  type: Login
  url: https://app.mailjet.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mailjet
- group: operate
  title: ''
  type: Support
  url: https://documentation.mailjet.com/hc/en-us
- group: commercial
  title: ''
  type: Pricing
  url: https://www.mailjet.com/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://mailjetstatus.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.mailjet.com/legal/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.mailjet.com/legal/privacy-policy/
- group: company
  title: ''
  type: Blog
  url: https://www.mailjet.com/blog/feed/
created: '2026-03-16'
description: Mailjet is an email service provider offering a powerful REST API for sending transactional and marketing emails. It provides an easy-to-integrate API with support for PHP, Python, Ruby, Java, Node.js, C#, and Go, along with SMTP relay and real-time email tracking.
finops:
- has_sources: true
  method: derived
  name: Mailjet Finops
  primary_unit: subscription
  service_category: ''
  slug: mailjet-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mailjet.png
layout: provider
modified: '2026-05-19'
name: Mailjet
nav: Providers
network: true
overview: 'Mailjet publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Campaigns API, Contact Lists API, Contacts API, and 5 more. Tagged areas include Email, Email Delivery, Marketing Email, SMTP, and Transactional Email.


  The Mailjet catalog on APIs.io includes 1 Spectral governance ruleset.


  Mailjet''s developer surface includes authentication, developer portal, signup flow, support, pricing, engineering blog, and 13 more developer resources.'
plans:
- name: Mailjet Plans Pricing
  plan_count: 5
  slug: mailjet-plans-pricing
- name: Mailjet Price Estimates
  plan_count: 0
  slug: mailjet-price-estimates
random_paper: 22
rate_limits:
- limit_count: 5
  name: Mailjet Rate Limits
  slug: mailjet-rate-limits
rules:
- authorship: generated
  effective_rule_count: 97
  extends:
  - spectral:oas
  name: Mailjet API Rules
  rule_count: 56
  severity_counts:
    error: 53
    hint: 0
    info: 2
    warn: 1
  slug: mailjet-rules
score:
  band: developing
  composite: 50.1
  coverage:
    artifact_dirs: 17
    catalog_earned: 59.5
    catalog_earned_first_party: 12.0
    catalog_gap: 55.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 2.0
  facets:
    access_clarity: 77.6
    contract_governance: 13.6
    contract_quality: 46.3
    developer_ergonomics: 57.1
    discoverability: 66.1
    operational_transparency: 26.3
  previous_composite: 48.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/mailjet/mailjet-2026-06-20T184859.png
security:
- kind: authentication
  name: Mailjet Authentication
  slug: mailjet-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Mailjet Domain Security
  slug: mailjet-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: mailjet
tags:
- Email
- Email Delivery
- Marketing Email
- SMTP
- Transactional Email
website: https://www.mailjet.com/
---
