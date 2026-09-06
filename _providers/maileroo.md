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
    error_semantics: verified
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
  score: 25.5
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Maileroo Agentic Access
  operation_count: 5
  slug: maileroo-agentic-access
  summary_line: 5 operations · 4 acting
api_count: 1
apis:
- baseURL: https://smtp.maileroo.com
  baseurl_source: declared
  description: Send transactional and bulk emails
  name: Maileroo Emails API
  slug: maileroo-emails-api
- baseURL: https://smtp.maileroo.com
  baseurl_source: declared
  description: Manage scheduled email deliveries
  name: Maileroo Scheduled API
  slug: maileroo-scheduled-api
artifact_total: 12
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Maileroo Email API
  slug: open-maileroo-email-api
- collection_type: open
  name: Maileroo Email Emails API
  slug: open-maileroo-emails-api
- collection_type: open
  name: Maileroo Email Emails Scheduled API
  slug: open-maileroo-scheduled-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/maileroo-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/maileroo-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/maileroo-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/maileroo
- group: start
  title: ''
  type: Portal
  url: https://maileroo.com/email-for-developers
- group: docs
  title: ''
  type: Documentation
  url: https://maileroo.com/docs/
- group: start
  title: ''
  type: Signup
  url: https://app.maileroo.com/register
- group: start
  title: ''
  type: Login
  url: https://app.maileroo.com/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/maileroo
- group: commercial
  title: ''
  type: Pricing
  url: https://maileroo.com/pricing
- group: agent
  title: ''
  type: LlmsText
  url: https://maileroo.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://maileroo.com/blog/feed
created: '2025-02-06'
description: Maileroo provides transactional and marketing email delivery via a developer-friendly REST API with high deliverability, SMTP relay support, email tracking, and SDKs for popular programming languages. Trusted by businesses of all sizes to handle millions of emails every month.
finops:
- name: Maileroo Finops
  service_category: API
  slug: maileroo-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/maileroo.png
layout: provider
modified: '2026-05-19'
name: Maileroo
nav: Providers
network: true
overview: 'Maileroo publishes 2 APIs on the [APIs.io](https://apis.io/) network: Emails API and Scheduled API. Tagged areas include Email, Email Delivery, Marketing Email, SMTP, and Transactional Email.


  Maileroo''s developer surface includes authentication, developer portal, documentation, signup flow, pricing, engineering blog, and 6 more developer resources.'
plans:
- name: Maileroo Plans Pricing
  plan_count: 3
  slug: maileroo-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 5
  name: Maileroo Rate Limits
  slug: maileroo-rate-limits
score:
  band: developing
  composite: 39.6
  coverage:
    artifact_dirs: 11
    catalog_earned: 46.0
    catalog_earned_first_party: 0.0
    catalog_gap: 69.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 32.9
    commercial_clarity: 32.9
    contract_governance: 0.0
    contract_quality: 58.2
    developer_ergonomics: 47.6
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 39.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/maileroo/refs/heads/main/screenshots/maileroo-2026-06-20T184856.png
security:
- kind: authentication
  name: Maileroo Authentication
  slug: maileroo-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Maileroo Domain Security
  slug: maileroo-domain-security
  summary_line: TLSv1.3 · DMARC
slug: maileroo
tags:
- Email
- Email Delivery
- Marketing Email
- SMTP
- Transactional Email
website: https://maileroo.com/email-for-developers
---
