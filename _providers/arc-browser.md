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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-11'
api_count: 5
apis:
- description: Desktop browser for macOS and Windows, organized around Spaces, Profiles, Tabs, Split View, and Themes. Built on Chromium.
  name: Arc Browser (Desktop)
  slug: desktop
- description: Mobile-first AI-augmented search and browsing experience that builds "Browse for Me" summary pages from a query. iOS and Android.
  name: Arc Search
  slug: search
- description: User-authored CSS and JavaScript overlays that customize the look and behavior of any website inside Arc. Authored from inside the browser rather than via a public REST API; can be shared via Boost li
  name: Arc Boosts
  slug: boosts
- description: Arc inherits the Chromium / Chrome Web Store extension model, so any Manifest V3 extension can be installed. There is no Arc-specific extension API beyond Chromium.
  name: Arc Chromium Extensions
  slug: extensions
- description: In-browser Developer Mode for engineers - exposes developer tools, extension management, and Portrait Mode for sharing in-progress work. Not a public API.
  name: Arc Developer Mode
  slug: developer-mode
artifact_total: 11
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/arc-browser-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/arc-browser-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/arc-browser-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://arc.net/
- group: other
  title: ''
  type: Company
  url: https://thebrowser.company/
- group: other
  title: ''
  type: ResourceCenter
  url: https://resources.arc.net/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/the-browser-company
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/browsercompany
- group: company
  title: ''
  type: Blog
  url: https://arc.net/blog
created: '2026-05-23'
description: Arc is a Chromium-based alternative web browser from The Browser Company, organized around Spaces, Profiles, Split View, Boosts (user-authored CSS/JS overlays), Easels, Notes, and Arc Search on mobile. Arc is primarily a consumer product without a broad public developer REST API. Developer surface area is limited to Developer Mode in the desktop browser, the underlying Chromium extension model, and user-created Boosts. The company has signalled that Arc's active product investment is winding down in favor of the successor product, Dia.
finops:
- name: Arc Browser Finops
  service_category: API
  slug: arc-browser-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/arc-browser.png
layout: provider
modified: '2026-05-23'
name: Arc (The Browser Company)
nav: Providers
network: true
overview: 'Arc (The Browser Company) publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Browser, Consumer, Chromium, Boosts, and The Browser Company.


  Arc (The Browser Company)''s developer surface includes engineering blog and 8 more developer resources.'
plans:
- name: Arc Browser Plans Pricing
  plan_count: 1
  slug: arc-browser-plans-pricing
random_paper: 83
rate_limits:
- limit_count: 2
  name: Arc Browser Rate Limits
  slug: arc-browser-rate-limits
score:
  band: emerging
  composite: 18.0
  delta: 0.0
  facets:
    commercial_clarity: 36.8
    contract_quality: 0.0
    developer_ergonomics: 2.2
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 18.0
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/arc-browser/refs/heads/main/screenshots/arc-browser-2026-06-20T172352.png
security:
- kind: domain-security
  name: Arc Browser Domain Security
  slug: arc-browser-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Arc Browser Vulnerability Disclosure
  slug: arc-browser-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Arc Browser Trust Center
  slug: arc-browser-trust-center
  summary_line: SOC 2, ISO 27001
slug: arc-browser
tags:
- Browser
- Consumer
- Chromium
- Boosts
- The Browser Company
website: https://arc.net/
---
