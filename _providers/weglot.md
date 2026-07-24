---
access_model:
  confidence: high
  label: Freemium (free trial) · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  trial: true
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
- acting_count: 1
  human_in_the_loop: 0
  name: Weglot Agentic Access
  operation_count: 4
  slug: weglot-agentic-access
  summary_line: 4 operations · 1 acting
api_count: 3
apis:
- description: The Languages API from Weglot — 2 operation(s) for languages.
  name: Weglot Languages API
  slug: weglot-languages-api
- description: The Status API from Weglot — 1 operation(s) for status.
  name: Weglot Status API
  slug: weglot-status-api
- description: The Translate API from Weglot — 1 operation(s) for translate.
  name: Weglot Translate API
  slug: weglot-translate-api
artifact_total: 12
collections:
- collection_type: open
  name: Weglot Translation API
  slug: open-weglot
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/weglot-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/weglot-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/weglot-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/weglot-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/weglot-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/weglot
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/weglot
- group: company
  title: ''
  type: Website
  url: https://www.weglot.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.weglot.com
- group: commercial
  title: ''
  type: Plans
  url: plans/weglot-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/weglot-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/weglot-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.weglot.com/blog
created: '2026-06-21'
description: Weglot is a website translation platform that detects, translates, and displays multilingual content with no code changes. Its REST API at https://api.weglot.com powers machine and human translation of arrays of sentences between languages, exposes the catalog of supported languages, and is the same translation service used by the Weglot JavaScript, WordPress, Shopify, and CMS integrations.
finops:
- name: Weglot Finops
  service_category: Web Services
  slug: weglot-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/weglot.png
layout: provider
modified: '2026-06-21'
name: Weglot
nav: Providers
network: true
overview: 'Weglot publishes 3 APIs on the [APIs.io](https://apis.io/) network: Languages API, Status API, and Translate API. Tagged areas include Translation, Localization, Internationalization, Machine Translation, and Multilingual.


  Weglot''s developer surface includes authentication, documentation, engineering blog, and 10 more developer resources.'
plans:
- name: Weglot Plans Pricing
  plan_count: 7
  slug: weglot-plans-pricing
random_paper: 46
rate_limits:
- limit_count: 3
  name: Weglot Rate Limits
  slug: weglot-rate-limits
score:
  band: thin
  composite: 40.0
  delta: 0.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 58.4
    developer_ergonomics: 21.7
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 40.0
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Weglot Authentication
  slug: weglot-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Weglot Domain Security
  slug: weglot-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Weglot Vulnerability Disclosure
  slug: weglot-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Weglot Trust Center
  slug: weglot-trust-center
  summary_line: SOC 2, GDPR
slug: weglot
tags:
- Translation
- Localization
- Internationalization
- Machine Translation
- Multilingual
website: https://www.weglot.com
---
