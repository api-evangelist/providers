---
access_model:
  confidence: medium
  label: Paid (free trial) · Open access
  onboarding: open
  pricing: paid
  public: true
  source:
  - plans
  trial: true
  try_now: true
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: REST API for managing social media clients, scheduling posts, monitoring mentions, and accessing analytics and reports across multiple social networks. The API is live at https://api.sendible.com/api/
  name: Sendible API
  slug: sendible-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sendible-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.sendible.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/Sendible
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sendible/
- group: company
  title: ''
  type: Blog
  url: https://www.sendible.com/insights
- group: commercial
  title: ''
  type: Pricing
  url: https://www.sendible.com/pricing
- group: other
  title: ''
  type: X
  url: https://x.com/sendible
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/sendible/refs/heads/main/plans/sendible-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/sendible/refs/heads/main/rate-limits/sendible-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/sendible/refs/heads/main/finops/sendible-finops.yml
- group: operate
  title: ''
  type: Support
  url: https://support.sendible.com/hc/en-us
- group: start
  title: ''
  type: SignUp
  url: https://app.sendible.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sendible.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sendible.com/privacy
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.sendible.com/changelog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/sendible-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sendible-lifecycle.yml
- group: auth
  title: ''
  type: Security
  url: https://www.sendible.com/vulnerability-reporting
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/sendible-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sendible-llms.txt
created: '2026-06-13'
description: Sendible is a social media management platform for agencies, franchises, multi-location brands and marketing teams, headquartered in London. It schedules and publishes content across Instagram, Facebook, LinkedIn, X, TikTok, Threads, Bluesky, YouTube, Google Business Profile and WordPress, centralises replies in a Priority Inbox, and produces client-facing analytics reports. Sendible operates a live REST API at api.sendible.com/api/v1 and markets an API-led path for software integrators, but the public developer portal has been retired and no machine-readable contract is published.
finops:
- name: Sendible Finops
  service_category: ''
  slug: sendible-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sendible.png
layout: provider
modified: '2026-08-13'
name: Sendible
nav: Providers
network: true
overview: 'Sendible publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Social-Media, Social Media Management, Agencies, Scheduling, and Analytics.


  Sendible''s developer surface includes engineering blog, pricing, support, signup flow, changelog, and 15 more developer resources.'
plans:
- name: Sendible Plans Pricing
  plan_count: 5
  slug: sendible-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 6
  name: Sendible Rate Limits
  slug: sendible-rate-limits
score:
  band: thin
  composite: 30.7
  coverage:
    artifact_dirs: 14
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 71.1
    commercial_clarity: 71.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 63.2
  previous_composite: 30.7
  provenance:
    mcp: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sendible/refs/heads/main/screenshots/sendible-2026-06-20T193657.png
security:
- kind: authentication
  name: Sendible Authentication
  slug: sendible-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Sendible Domain Security
  slug: sendible-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Sendible Vulnerability Disclosure
  slug: sendible-vulnerability-disclosure
  summary_line: contact published
slug: sendible
tags:
- Social-Media
- Social Media Management
- Agencies
- Scheduling
- Analytics
- Monitoring
website: https://www.sendible.com/
---
