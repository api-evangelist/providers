---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
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
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.0
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Cloudflare Turnstile Agentic Access
  operation_count: 1
  slug: cloudflare-turnstile-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- description: The Turnstile siteverify endpoint accepts a token produced by the browser widget along with the site's secret key and an optional remote IP and idempotency key, and returns a JSON verdict with success
  name: Turnstile Siteverify API
  slug: siteverify
- description: 'The Turnstile client widget renders the challenge in the browser. It is loaded via a script tag at challenges.cloudflare.com/turnstile/v0/api.js and configured with a sitekey, optional theme, action, '
  name: Turnstile Client Widget
  slug: client-widget
- description: Pre-clearance lets a successful Turnstile challenge set a cookie that Cloudflare-proxied properties can honor to skip subsequent bot challenges for the same visitor, which is useful for single-page ap
  name: Turnstile Pre-Clearance
  slug: pre-clearance
- description: Turnstile widgets and analytics are managed through the broader Cloudflare API, which exposes endpoints to list, create, update, and rotate Turnstile sitekeys, retrieve analytics, and integrate with a
  name: Cloudflare Turnstile Management API
  slug: management-api
- baseURL: https://challenges.cloudflare.com/turnstile/v0/siteverify
  baseurl_source: declared
  description: The Verification API from Cloudflare Turnstile — 1 operation(s) for verification.
  name: Cloudflare Turnstile Verification API
  slug: cloudflare-turnstile-verification-api
artifact_total: 14
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Cloudflare Turnstile Siteverify Verification API
  slug: open-cloudflare-turnstile-verification-api
- collection_type: open
  name: Cloudflare Turnstile Siteverify API
  slug: open-cloudflare-turnstile
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cloudflare-turnstile-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/cloudflare-turnstile-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cloudflare-turnstile-domain-security.yml
- group: other
  title: ''
  type: ProductPage
  url: https://www.cloudflare.com/products/turnstile/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.cloudflare.com/turnstile/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.cloudflare.com/turnstile/reference/
- group: other
  title: ''
  type: Dashboard
  url: https://dash.cloudflare.com/?to=/:account/turnstile
- group: company
  title: ''
  type: Blog
  url: https://blog.cloudflare.com/turnstile-private-captcha-alternative/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cloudflare
- group: start
  title: ''
  type: Demos
  url: https://github.com/cloudflare/turnstile-demo-workers
- group: commercial
  title: ''
  type: Pricing
  url: https://developers.cloudflare.com/turnstile/community/limits-and-pricing/
- group: agent
  title: ''
  type: LlmsText
  url: https://developers.cloudflare.com/llms.txt
created: '2026-05-23'
description: Cloudflare Turnstile is Cloudflare's free, smart CAPTCHA alternative that verifies real users without sending traffic through Cloudflare's network. It runs non-interactive client-side challenges (proof-of-work, proof-of-space, web API probing, browser-integrity checks) and returns a short-lived token that the relying server validates against the Turnstile siteverify endpoint. Turnstile offers three widget modes — Managed (risk-adapted), Non-interactive (no user gesture), and Invisible (fully hidden) — and is designed to run on any website regardless of whether the site is proxied through Cloudflare. The product is targeted at developers who want a privacy-respecting reCAPTCHA replacement.
finops:
- name: Cloudflare Turnstile Finops
  service_category: API
  slug: cloudflare-turnstile-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cloudflare-turnstile.png
layout: provider
modified: '2026-05-23'
name: Cloudflare Turnstile
nav: Providers
network: true
overview: 'Cloudflare Turnstile publishes 1 API on the [APIs.io](https://apis.io/) network: Verification API. Tagged areas include CAPTCHA, Bot Defense, Cloudflare, Turnstile, and Privacy.


  Cloudflare Turnstile''s developer surface includes documentation, API reference, engineering blog, pricing, and 8 more developer resources.'
plans:
- name: Cloudflare Turnstile Plans Pricing
  plan_count: 1
  slug: cloudflare-turnstile-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 2
  name: Cloudflare Turnstile Rate Limits
  slug: cloudflare-turnstile-rate-limits
score:
  band: thin
  composite: 32.5
  coverage:
    artifact_dirs: 10
    catalog_earned: 56.0
    catalog_earned_first_party: 0.0
    catalog_gap: 59.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 49.0
    developer_ergonomics: 19.0
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 32.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cloudflare-turnstile/refs/heads/main/screenshots/cloudflare-turnstile-2026-06-20T174557.png
security:
- kind: domain-security
  name: Cloudflare Turnstile Domain Security
  slug: cloudflare-turnstile-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Cloudflare Turnstile Vulnerability Disclosure
  slug: cloudflare-turnstile-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: cloudflare-turnstile
tags:
- CAPTCHA
- Bot Defense
- Cloudflare
- Turnstile
- Privacy
- reCAPTCHA Alternative
- Edge Security
---
