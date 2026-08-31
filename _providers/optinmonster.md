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
    error_semantics: documented
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
  score: 25.2
  scored_at: '2026-08-30'
api_count: 3
apis:
- description: The OptinMonster application REST API. Versioned path segments (`/v1`, `/v2`) sit on api.optinmonster.com and cover campaigns, leads, sites, site origins, integrations, account, revenue attribution an
  name: OptinMonster REST API
  slug: optinmonster-rest-api
- description: The API host the first-party OptinMonster WordPress plugin calls (`OPTINMONSTER_API_URL`). Serves the same versioned surface and error envelope as api.optinmonster.com — `v1/optins`, `v1/verify`, `v2/
  name: OptinMonster WordPress Plugin API
  slug: optinmonster-wordpress-plugin-api
- description: A client-side event API exposed by the OptinMonster embed script (served from a.omappapi.com/app/js/api.min.js). Roughly sixty documented `om.*` events fire across campaign initialization, display-rul
  name: OptinMonster JavaScript Events API
  slug: optinmonster-javascript-events-api
artifact_total: 9
asyncapis:
- description: ''
  name: Optinmonster Webhooks
  slug: optinmonster-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://optinmonster.com/
- group: docs
  title: ''
  type: Documentation
  url: https://optinmonster.com/docs/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://optinmonster.com/categories/docs/extending/
- group: start
  title: ''
  type: GettingStarted
  url: https://optinmonster.com/docs/getting-started-optinmonster-wordpress-checklist/
- group: operate
  title: ''
  type: Support
  url: https://optinmonster.com/support/
- group: company
  title: ''
  type: Blog
  url: https://optinmonster.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://optinmonster.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://app.optinmonster.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://optinmonster.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://optinmonster.com/privacy/
- group: auth
  title: ''
  type: Security
  url: https://optinmonster.com/security/
- group: build
  title: ''
  type: Packages
  url: packages/optinmonster-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/optinmonster-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/optinmonster-llms.txt
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/optinmonster-webhooks.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/optinmonster-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/optinmonster-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/optinmonster-plans-pricing.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/optinmonster-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/optinmonster-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/optinmonster-vulnerability-disclosure.yml
- group: design
  title: ''
  type: Components
  url: components/optinmonster-components.yml
created: '2026-08-12'
description: OptinMonster is a lead-generation and conversion-optimization SaaS from Awesome Motive that serves on-site campaigns — popups, floating bars, slide-ins, fullscreen fills, inline forms and gamified spin-to-win wheels — targeted by display rules such as Exit Intent, page-level targeting, geolocation, referrer and on-site behavior. Campaigns are built in a hosted visual builder at app.optinmonster.com and rendered on customer sites by a JavaScript embed served from the a.omappapi.com CDN. The platform exposes a private-key REST API at api.optinmonster.com (v1 and v2) and a mirror at api.omwpapi.com used by the first-party WordPress plugin, covering campaigns, leads, sites, integrations, revenue attribution and templates; a client-side JavaScript Events API of roughly sixty `om.*` lifecycle events for hooking campaign display, conversion and analytics; and an outbound webhook that POSTs captured lead data to a customer endpoint. Leads are routed to more than sixty marketing platforms
  through built-in integrations.
image: https://cdn.optinmonster.com/wp-content/uploads/2024/05/cropped-archie-1-192x192.png
layout: provider
modified: '2026-08-12'
name: OptinMonster
nav: Providers
network: true
overview: 'OptinMonster publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Lead Generation, Marketing, Conversion Optimization, and Email Marketing.


  The OptinMonster catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  OptinMonster''s developer surface includes documentation, getting-started guide, support, engineering blog, pricing, signup flow, changelog, and 15 more developer resources.'
plans:
- name: Optinmonster Plans Pricing
  plan_count: 4
  slug: optinmonster-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Optinmonster Rate Limits
  slug: optinmonster-rate-limits
score:
  band: developing
  composite: 51.2
  coverage:
    artifact_dirs: 17
    catalog_gap: 63.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 4.5
    contract_quality: 42.7
    developer_ergonomics: 57.1
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 39.5
  previous_composite: 51.2
  provenance:
    conformance: derived
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/optinmonster/refs/heads/main/screenshots/optinmonster-2026-08-17T081135.png
security:
- kind: authentication
  name: Optinmonster Authentication
  slug: optinmonster-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Optinmonster Domain Security
  slug: optinmonster-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Optinmonster Vulnerability Disclosure
  slug: optinmonster-vulnerability-disclosure
  summary_line: Hackerone
slug: optinmonster
tags:
- Company
- Lead Generation
- Marketing
- Conversion Optimization
- Email Marketing
- Popups
- WordPress
- Webhook
- Software-as-a-Service
- Marketing Automation
website: https://optinmonster.com/
---
