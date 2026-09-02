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
- description: 'Client-side browser API exposed by the Digioh widget runtime once the Digioh JavaScript tag is installed on a site. Documented calls include DIGIOH_API.LIGHTBOX.loadLightbox(guid) to manually trigger '
  name: Digioh JavaScript API
  slug: digioh-javascript-api
artifact_total: 6
asyncapis:
- description: ''
  name: Digioh Webhooks
  slug: digioh-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/digioh-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.digioh.com/
- group: docs
  title: ''
  type: Documentation
  url: https://help.digioh.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.digioh.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://help.digioh.com/docs/getting-started-guide
- group: docs
  title: ''
  type: APIReference
  url: https://help.digioh.com/docs/digioh-javascript-api
- group: operate
  title: ''
  type: Support
  url: https://www.digioh.com/contact
- group: company
  title: ''
  type: Blog
  url: https://www.digioh.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/digioh
- group: commercial
  title: ''
  type: Pricing
  url: https://www.digioh.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.digioh.com/book-a-demo
- group: start
  title: ''
  type: Login
  url: https://account.digioh.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.digioh.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.digioh.com/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.digioh.com/
- group: auth
  title: ''
  type: Compliance
  url: https://help.digioh.com/knowledgebase/security-and-compliance/
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.digioh.com/blog-categories/product-updates
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/digioh-changelog.yml
- group: build
  title: ''
  type: Packages
  url: packages/digioh-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/digioh-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/digioh-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/digioh-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/digioh-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/digioh-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/digioh-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/digioh-conventions.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/digioh-authentication.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/digioh-webhooks.yml
- group: design
  title: ''
  type: Components
  url: components/digioh-components.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/digioh-sandbox.yml
created: '2026-08-12'
description: Digioh is a US-based onsite personalization and zero-party data platform for ecommerce brands. It ships product recommendation quizzes, pop-ups, banners, sidebars, inline embeds, landing pages, email/SMS preference centers and post-purchase surveys as a JavaScript widget layer installed on a merchant's storefront, plus Digioh Passport for cross-session visitor identification and Digioh Pipelines for routing form submissions into ESP/CRM destinations such as Klaviyo, Iterable, Braze, Attentive, Ometria, HubSpot and Salesforce. Its developer surface is client-side rather than server-side - a documented browser JavaScript API (DIGIOH_API.LIGHTBOX), an outbound "API Form POST" webhook integration that posts submission JSON to a customer-controlled endpoint, iOS and Android embed SDKs, and a WordPress plugin and Shopify app. Digioh publishes no public inbound REST API, no OpenAPI definition and no developer portal.
image: https://cdn.prod.website-files.com/5ff6171603c269c582a4e0ff/670bc8241e4c1b1fd62820d7_Webclip.png
layout: provider
modified: '2026-08-12'
name: Digioh
nav: Providers
network: true
overview: 'Digioh publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Marketing, E-Commerce, Personalization, and Zero-Party Data.


  The Digioh catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Digioh''s developer surface includes documentation, getting-started guide, API reference, support, engineering blog, pricing, signup flow, and 23 more developer resources.'
plans:
- name: Digioh Plans Pricing
  plan_count: 3
  slug: digioh-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: Digioh Rate Limits
  slug: digioh-rate-limits
score:
  band: strong
  composite: 54.9
  coverage:
    artifact_dirs: 16
    catalog_gap: 66.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.2
  facets:
    access_clarity: 84.2
    commercial_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 61.9
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 42.1
  previous_composite: 55.1
  provenance:
    conformance: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/digioh/refs/heads/main/screenshots/digioh-2026-08-17T080859.png
security:
- kind: authentication
  name: Digioh Authentication
  slug: digioh-authentication
  summary_line: tenantIdentifier/http-basic/apiKey · 4 schemes
- kind: domain-security
  name: Digioh Domain Security
  slug: digioh-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: digioh
tags:
- Company
- Marketing
- E-Commerce
- Personalization
- Zero-Party Data
- Forms
- Popups
- Quizzes
- Conversion Rate Optimization
- Identity Resolution
website: https://www.digioh.com/
---
