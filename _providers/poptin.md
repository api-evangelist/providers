---
access_model:
  confidence: high
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
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'Poptin''s developer-facing surface. The hosted embed script renders popups, bars, sidebars, full-screen and mobile surfaces plus embedded forms into a host page, fires documented DOM CustomEvents with '
  name: Poptin Embed & Events
  slug: poptin-embed-events
artifact_total: 9
asyncapis:
- description: ''
  name: Poptin Webhooks
  slug: poptin-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://poptin.com/
- group: docs
  title: ''
  type: Documentation
  url: https://help.poptin.com/en/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.poptin.com/en/
- group: start
  title: ''
  type: GettingStarted
  url: https://help.poptin.com/en/article/create-your-first-poptin-7vpqx1/
- group: operate
  title: ''
  type: Support
  url: https://www.poptin.com/contact/
- group: company
  title: ''
  type: Blog
  url: https://www.poptin.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.poptin.com/blog/feed/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.poptin.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://app.popt.in/register
- group: start
  title: ''
  type: Login
  url: https://app.popt.in/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.poptin.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.poptin.com/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/poptins
- group: operate
  title: ''
  type: ChangeLog
  url: https://headwayapp.co/poptin-com-updates
- group: operate
  href: https://artifacts.apis.io/poptin/changelog/poptin-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/poptin-changelog.yml
- group: build
  href: https://artifacts.apis.io/poptin/packages/poptin-packages.yml
  title: ''
  type: Packages
  url: packages/poptin-packages.yml
- group: agent
  href: https://artifacts.apis.io/poptin/llms/poptin-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/poptin-llms.txt
- group: design
  href: https://artifacts.apis.io/poptin/components/poptin-components.yml
  title: ''
  type: Components
  url: components/poptin-components.yml
- group: design
  href: https://artifacts.apis.io/poptin/asyncapi/poptin-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/poptin-webhooks.yml
- group: auth
  href: https://artifacts.apis.io/poptin/authentication/poptin-authentication.yml
  title: ''
  type: Authentication
  url: authentication/poptin-authentication.yml
- group: commercial
  href: https://artifacts.apis.io/poptin/plans/poptin-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/poptin-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/poptin/rate-limits/poptin-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/poptin-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/poptin/lifecycle/poptin-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/poptin-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/poptin/conformance/poptin-conformance.yml
  title: ''
  type: Conformance
  url: conformance/poptin-conformance.yml
- group: auth
  href: https://artifacts.apis.io/poptin/security/poptin-trust-center.yml
  title: ''
  type: Compliance
  url: security/poptin-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/poptin/security/poptin-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/poptin-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/poptin/security/poptin-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/poptin-domain-security.yml
created: '2026-08-12'
description: 'Poptin is an Israeli-founded, no-code conversion and lifecycle marketing platform that bundles website popups, bars, embedded forms, coupons, email campaigns, email automation, contact management, audience segmentation and website tracking into a single SaaS product aimed at ecommerce stores, SaaS companies, agencies and small businesses. Delivery is a hosted embed script (cdn.popt.in/pixel.js) installed via first-party plugins for WordPress, Magento 2, Craft CMS, SilverStripe, TYPO3, OctoberCMS, Contao, Shopify, Wix and Google Tag Manager. Its developer surface is client-side and event-shaped rather than REST: documented DOM CustomEvents (poptinView, poptinClose, poptinSubmit, couponCopy) with a published event.detail field set, named global callbacks, and an outbound per-popup Webhooks integration that posts lead data to a subscriber URL. Poptin publishes no public API reference, no OpenAPI, and no developer portal; a Make/Zapier API key is issued from account settings for
  its two automation connectors.'
finops:
- has_sources: true
  method: derived
  name: Poptin Finops
  primary_unit: subscription
  service_category: ''
  slug: poptin-finops
  template: false
image: https://cdn.popt.in/poptin-website/images/common/header/site-logo-dark.svg
layout: provider
modified: '2026-08-12'
name: Poptin
nav: Providers
network: true
overview: 'Poptin is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Marketing, Email Marketing, Marketing Automation, and Lead Generation.


  The Poptin catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Poptin''s developer surface includes documentation, getting-started guide, support, engineering blog, pricing, signup flow, changelog, and 20 more developer resources.'
plans:
- name: Poptin Plans Pricing
  plan_count: 6
  slug: poptin-plans-pricing
- name: Poptin Price Estimates
  plan_count: 0
  slug: poptin-price-estimates
random_paper: 18
rate_limits:
- limit_count: 0
  name: Poptin Rate Limits
  slug: poptin-rate-limits
score:
  band: developing
  composite: 52.9
  coverage:
    artifact_dirs: 18
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 100.0
    contract_governance: 18.2
    contract_quality: 39.0
    developer_ergonomics: 40.5
    discoverability: 73.2
    operational_transparency: 26.3
  previous_composite: 52.9
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/poptin/poptin-2026-08-17T081328.png
security:
- kind: authentication
  name: Poptin Authentication
  slug: poptin-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Poptin Domain Security
  slug: poptin-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Poptin Trust Center
  slug: poptin-trust-center
  summary_line: ISO/IEC 27001:2013, ISO 27001 compliant infrastructure
slug: poptin
tags:
- Company
- Marketing
- Email Marketing
- Marketing Automation
- Lead Generation
- Conversion Optimization
- Forms
- Popups
- Contact Management
- Webhook
- E-Commerce
- Software-as-a-Service
website: https://poptin.com/
---
