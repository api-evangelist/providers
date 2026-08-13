---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
  scored_at: '2026-08-12'
api_count: 1
apis:
- description: The Google Sites API allows developers to programmatically access and manage Google Sites content, including pages, lists, and attachments.
  name: Google Sites API
  slug: google-sites-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-sites-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-sites-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://developers.google.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.google.com/sites/api/reference/rest
- group: auth
  title: ''
  type: Authentication
  url: https://developers.google.com/sites/api/guides/authentication
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developers.google.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://policies.google.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cloud.google.com/
- group: operate
  title: ''
  type: Support
  url: https://developers.google.com/sites/api/support
- group: company
  title: ''
  type: Blog
  url: https://developers.googleblog.com
created: '2024-01-01'
description: API for creating and managing Google Sites.
finops:
- name: Google Sites Finops
  service_category: API
  slug: google-sites-finops
image: https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png
layout: provider
modified: '2026-04-28'
name: Google Sites
nav: Providers
network: true
overview: 'Google Sites publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Collaboration, Content Management, Google Workspace, and Websites.


  Google Sites'' developer surface includes developer portal, documentation, authentication, support, engineering blog, and 5 more developer resources.'
plans:
- name: Google Sites Plans Pricing
  plan_count: 3
  slug: google-sites-plans-pricing
random_paper: 34
rate_limits:
- limit_count: 5
  name: Google Sites Rate Limits
  slug: google-sites-rate-limits
score:
  band: thin
  composite: 31.2
  delta: 0.0
  facets:
    commercial_clarity: 36.8
    contract_quality: 32.3
    developer_ergonomics: 34.8
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 31.2
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-sites/refs/heads/main/screenshots/google-sites-2026-06-20T182235.png
security:
- kind: domain-security
  name: Google Sites Domain Security
  slug: google-sites-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Sites Vulnerability Disclosure
  slug: google-sites-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-sites
tags:
- Collaboration
- Content Management
- Google Workspace
- Websites
website: https://developers.google.com
---
