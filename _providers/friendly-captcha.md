---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
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
  score: 30.6
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Friendly Captcha Agentic Access
  operation_count: 1
  slug: friendly-captcha-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 5
apis:
- description: The siteverify endpoint validates a Friendly Captcha solution token. The server POSTs the token and API key (with optional sitekey) and receives a JSON response indicating success, risk score, IP inte
  name: Friendly Captcha Siteverify API
  slug: siteverify
- description: The Friendly Captcha widget is the JavaScript component that runs the proof-of-work puzzle in the browser and produces a solution token. It is configured via a script tag and a div with the sitekey an
  name: Friendly Captcha Widget
  slug: widget
- description: Friendly Captcha publishes open-source wrappers for React, Vue, and Angular that expose the widget as an idiomatic component in each framework, handling lifecycle, callbacks, and token flow.
  name: Friendly Captcha Framework SDKs
  slug: framework-sdks
- description: Pre-built plugins integrate Friendly Captcha into WordPress, Magento, and other CMS platforms, letting non-developers add privacy-preserving bot defense to common forms without writing code.
  name: Friendly Captcha CMS Plugins
  slug: plugins
- description: The Siteverify API from Friendly Captcha — 1 operation(s) for siteverify.
  name: Friendly Captcha Siteverify API
  slug: friendly-captcha-siteverify-api
artifact_total: 12
collections:
- collection_type: open
  name: Friendly Captcha Siteverify API
  slug: open-friendly-captcha
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/FriendlyCaptcha/friendly-challenge/issues
- group: commercial
  title: ''
  type: License
  url: https://github.com/FriendlyCaptcha/friendly-challenge/blob/master/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/friendly-captcha-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/friendly-captcha-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/friendly-captcha-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://friendlycaptcha.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.friendlycaptcha.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.friendlycaptcha.com/docs/v2/api-reference
- group: commercial
  title: ''
  type: Pricing
  url: https://friendlycaptcha.com/pricing/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/FriendlyCaptcha
- group: company
  title: ''
  type: Blog
  url: https://friendlycaptcha.com/insights/
- group: commercial
  title: ''
  type: Privacy
  url: https://friendlycaptcha.com/legal/privacy-end-users/
- group: operate
  title: ''
  type: Contact
  url: https://friendlycaptcha.com/contact/
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.friendlycaptcha.com/llms.txt
created: '2026-05-23'
description: Friendly Captcha is a privacy-first, GDPR-compliant bot protection service from Germany that uses proof-of-work cryptographic puzzles instead of image-labeling challenges. The widget solves a puzzle in the background while a user fills out a form, then submits a token the server validates against the Friendly Captcha siteverify endpoint. The result includes a risk verdict and additional signal intelligence (IP, bot detection, browser identification, anonymization detection). Friendly Captcha publishes open-source widgets and framework integrations for React, Vue, and Angular, plus pre-built plugins for WordPress, Magento, and other CMS platforms.
finops:
- name: Friendly Captcha Finops
  service_category: API
  slug: friendly-captcha-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/friendly-captcha.png
layout: provider
modified: '2026-05-23'
name: Friendly Captcha
nav: Providers
network: true
overview: 'Friendly Captcha publishes 1 API on the [APIs.io](https://apis.io/) network: Siteverify API. Tagged areas include CAPTCHA, Bot Defense, Privacy, Proof of Work, and GDPR.


  Friendly Captcha''s developer surface includes authentication, documentation, API reference, pricing, engineering blog, privacy policy, and 8 more developer resources.'
plans:
- name: Friendly Captcha Plans Pricing
  plan_count: 1
  slug: friendly-captcha-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 2
  name: Friendly Captcha Rate Limits
  slug: friendly-captcha-rate-limits
score:
  band: thin
  composite: 41.8
  delta: 0.2
  facets:
    commercial_clarity: 50.0
    contract_quality: 58.2
    developer_ergonomics: 28.3
    discoverability: 81.5
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 41.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/friendly-captcha/refs/heads/main/screenshots/friendly-captcha-2026-06-20T181553.png
security:
- kind: authentication
  name: Friendly Captcha Authentication
  slug: friendly-captcha-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Friendly Captcha Domain Security
  slug: friendly-captcha-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: friendly-captcha
tags:
- CAPTCHA
- Bot Defense
- Privacy
- Proof of Work
- GDPR
- European Hosting
- Accessibility
website: https://friendlycaptcha.com/
---
