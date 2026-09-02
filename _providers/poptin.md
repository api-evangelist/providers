---
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.3
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: 'Poptin''s developer-facing surface. The hosted embed script renders popups, bars, sidebars, full-screen and mobile surfaces plus embedded forms into a host page, fires documented DOM CustomEvents with '
  name: Poptin Embed & Events
  slug: poptin-embed-events
artifact_total: 7
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
  title: ''
  type: ChangeLog
  url: changelog/poptin-changelog.yml
- group: build
  title: ''
  type: Packages
  url: packages/poptin-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/poptin-llms.txt
- group: design
  title: ''
  type: Components
  url: components/poptin-components.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/poptin-webhooks.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/poptin-authentication.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/poptin-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/poptin-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/poptin-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/poptin-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/poptin-trust-center.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/poptin-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/poptin-domain-security.yml
created: '2026-08-12'
description: 'Poptin is an Israeli-founded, no-code conversion and lifecycle marketing platform that bundles website popups, bars, embedded forms, coupons, email campaigns, email automation, contact management, audience segmentation and website tracking into a single SaaS product aimed at ecommerce stores, SaaS companies, agencies and small businesses. Delivery is a hosted embed script (cdn.popt.in/pixel.js) installed via first-party plugins for WordPress, Magento 2, Craft CMS, SilverStripe, TYPO3, OctoberCMS, Contao, Shopify, Wix and Google Tag Manager. Its developer surface is client-side and event-shaped rather than REST: documented DOM CustomEvents (poptinView, poptinClose, poptinSubmit, couponCopy) with a published event.detail field set, named global callbacks, and an outbound per-popup Webhooks integration that posts lead data to a subscriber URL. Poptin publishes no public API reference, no OpenAPI, and no developer portal; a Make/Zapier API key is issued from account settings for
  its two automation connectors.'
image: https://cdn.popt.in/poptin-website/images/common/header/site-logo-dark.svg
layout: provider
modified: '2026-08-12'
name: Poptin
nav: Providers
network: true
overview: 'Poptin publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Marketing, Email Marketing, Marketing Automation, and Lead Generation.


  The Poptin catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Poptin''s developer surface includes documentation, getting-started guide, support, engineering blog, pricing, signup flow, changelog, and 20 more developer resources.'
plans:
- name: Poptin Plans Pricing
  plan_count: 0
  slug: poptin-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Poptin Rate Limits
  slug: poptin-rate-limits
score:
  band: developing
  composite: 43.8
  coverage:
    artifact_dirs: 14
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.3
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 40.5
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 26.3
  previous_composite: 44.1
  provenance:
    conformance: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/poptin/refs/heads/main/screenshots/poptin-2026-08-17T081328.png
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
