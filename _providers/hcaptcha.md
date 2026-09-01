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
- acting_count: 1
  human_in_the_loop: 0
  name: Hcaptcha Agentic Access
  operation_count: 1
  slug: hcaptcha-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- description: The /siteverify endpoint validates an hCaptcha response token submitted by a browser. The server POSTs the token, secret key, and optional remote IP, and receives a JSON response indicating success, h
  name: hCaptcha Siteverify API
  slug: siteverify
- description: The hCaptcha JS widget renders the visible or invisible challenge on a page and produces a response token on success. Developers include a script tag pointing at js.hcaptcha.com/1/api.js and place a d
  name: hCaptcha JavaScript Widget
  slug: js-widget
- description: Invisible hCaptcha runs the challenge in the background and only surfaces a visible puzzle when risk requires it. It is configured via the same widget script and an additional data-size="invisible" at
  name: hCaptcha Invisible
  slug: invisible
- description: 'hCaptcha publishes native iOS and Android SDKs (with React Native and Flutter wrappers) so mobile apps can present the same risk-based challenges as the web widget and obtain response tokens that the '
  name: hCaptcha Mobile SDKs
  slug: mobile-sdks
- description: hCaptcha Enterprise extends the core challenge with advanced bot detection, account defense (ATO and fake-account protection), MFA and pull-based SMS, fraud signals, and management APIs for provisioni
  name: hCaptcha Enterprise
  slug: enterprise
- description: The Siteverify API from hCaptcha — 1 operation(s) for siteverify.
  name: hCaptcha Siteverify API
  slug: hcaptcha-siteverify-api
artifact_total: 15
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: hCaptcha Siteverify API
  slug: open-hcaptcha-siteverify-api
- collection_type: open
  name: hCaptcha API
  slug: open-hcaptcha
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/hcaptcha-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hcaptcha-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/hcaptcha-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.hcaptcha.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.hcaptcha.com/
- group: other
  title: ''
  type: Enterprise
  url: https://www.hcaptcha.com/enterprise
- group: start
  title: ''
  type: Signup
  url: https://www.hcaptcha.com/signup-interstitial
- group: commercial
  title: ''
  type: Pricing
  url: https://www.hcaptcha.com/#pricing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hCaptcha
- group: company
  title: ''
  type: Blog
  url: https://www.hcaptcha.com/post
- group: commercial
  title: ''
  type: Privacy
  url: https://www.hcaptcha.com/privacy
- group: operate
  title: ''
  type: Status
  url: https://status.hcaptcha.com/
created: '2026-05-23'
description: hCaptcha, operated by Intuition Machines, is a privacy-focused CAPTCHA and bot-defense platform used as a drop-in replacement for Google reCAPTCHA. The free Publisher and Pro tiers offer a JavaScript widget and a server-side /siteverify endpoint that issue and verify single-use tokens. The Enterprise tier (hCaptcha Enterprise) adds advanced bot detection, account defense, MFA, machine-learning fraud signals, and management APIs. hCaptcha is broadly integrated into web frameworks and CMS platforms (React, Vue, Angular, Node/Express, WordPress, Magento) and ships first-party mobile SDKs for iOS and Android.
finops:
- name: Hcaptcha Finops
  service_category: API
  slug: hcaptcha-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hcaptcha.png
layout: provider
modified: '2026-05-23'
name: hCaptcha
nav: Providers
network: true
overview: 'hCaptcha publishes 1 API on the [APIs.io](https://apis.io/) network: Siteverify API. Tagged areas include CAPTCHA, Bot Defense, Privacy, hCaptcha, and Intuition Machines.


  hCaptcha''s developer surface includes authentication, documentation, signup flow, pricing, engineering blog, privacy policy, status page, and 5 more developer resources.'
plans:
- name: Hcaptcha Plans Pricing
  plan_count: 1
  slug: hcaptcha-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 2
  name: Hcaptcha Rate Limits
  slug: hcaptcha-rate-limits
score:
  band: developing
  composite: 39.6
  coverage:
    artifact_dirs: 10
    catalog_gap: 59.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 57.9
    commercial_clarity: 57.9
    contract_governance: 0.0
    contract_quality: 52.4
    developer_ergonomics: 25.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 39.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hcaptcha/refs/heads/main/screenshots/hcaptcha-2026-06-20T182548.png
security:
- kind: authentication
  name: Hcaptcha Authentication
  slug: hcaptcha-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Hcaptcha Domain Security
  slug: hcaptcha-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: hcaptcha
tags:
- CAPTCHA
- Bot Defense
- Privacy
- hCaptcha
- Intuition Machines
- Account Defense
- Enterprise Security
website: https://www.hcaptcha.com/
---
