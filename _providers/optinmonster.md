---
access_model:
  confidence: high
  gated: none
  gated_conflict: 'x-api-posture: private but 3 published API entries'
  gated_source:
  - onboarding
  label: Freemium (free trial) · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: true
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
    error_semantics: documented
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
  score: 25.2
  scored_at: '2026-11-06'
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
artifact_total: 11
asyncapis:
- description: ''
  name: Optinmonster Webhooks
  slug: optinmonster-webhooks
common:
- group: operate
  href: https://artifacts.apis.io/optinmonster/rate-limits/optinmonster-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/optinmonster-rate-limits.yml
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
  href: https://artifacts.apis.io/optinmonster/packages/optinmonster-packages.yml
  title: ''
  type: Packages
  url: packages/optinmonster-packages.yml
- group: build
  href: https://artifacts.apis.io/optinmonster/packages/optinmonster-packages.yml
  title: ''
  type: SDKs
  url: packages/optinmonster-packages.yml
- group: agent
  href: https://artifacts.apis.io/optinmonster/llms/optinmonster-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/optinmonster-llms.txt
- group: design
  href: https://artifacts.apis.io/optinmonster/asyncapi/optinmonster-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/optinmonster-webhooks.yml
- group: operate
  href: https://artifacts.apis.io/optinmonster/changelog/optinmonster-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/optinmonster-changelog.yml
- group: design
  href: https://artifacts.apis.io/optinmonster/lifecycle/optinmonster-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/optinmonster-lifecycle.yml
- group: commercial
  href: https://artifacts.apis.io/optinmonster/plans/optinmonster-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/optinmonster-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/optinmonster/conformance/optinmonster-conformance.yml
  title: ''
  type: Conformance
  url: conformance/optinmonster-conformance.yml
- group: auth
  href: https://artifacts.apis.io/optinmonster/security/optinmonster-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/optinmonster-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/optinmonster/security/optinmonster-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/optinmonster-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/optinmonster/components/optinmonster-components.yml
  title: ''
  type: Components
  url: components/optinmonster-components.yml
created: '2026-08-12'
description: OptinMonster is a lead-generation and conversion-optimization SaaS from Awesome Motive that serves on-site campaigns — popups, floating bars, slide-ins, fullscreen fills, inline forms and gamified spin-to-win wheels — targeted by display rules such as Exit Intent, page-level targeting, geolocation, referrer and on-site behavior. Campaigns are built in a hosted visual builder at app.optinmonster.com and rendered on customer sites by a JavaScript embed served from the a.omappapi.com CDN. The platform exposes a private-key REST API at api.optinmonster.com (v1 and v2) and a mirror at api.omwpapi.com used by the first-party WordPress plugin, covering campaigns, leads, sites, integrations, revenue attribution and templates; a client-side JavaScript Events API of roughly sixty `om.*` lifecycle events for hooking campaign display, conversion and analytics; and an outbound webhook that POSTs captured lead data to a customer endpoint. Leads are routed to more than sixty marketing platforms
  through built-in integrations.
finops:
- has_sources: true
  method: derived
  name: Optinmonster Finops
  primary_unit: site
  service_category: ''
  slug: optinmonster-finops
  template: false
image: https://cdn.optinmonster.com/wp-content/uploads/2024/05/cropped-archie-1-192x192.png
layout: provider
modified: '2026-08-12'
name: OptinMonster
nav: Providers
network: true
overview: 'OptinMonster is listed with 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Lead Generation, Marketing, Conversion Optimization, and Email Marketing.


  The OptinMonster catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  OptinMonster''s developer surface includes documentation, getting-started guide, support, engineering blog, pricing, signup flow, changelog, and 16 more developer resources.'
plans:
- name: Optinmonster Plans Pricing
  plan_count: 6
  slug: optinmonster-plans-pricing
- name: Optinmonster Price Estimates
  plan_count: 0
  slug: optinmonster-price-estimates
random_paper: 10
rate_limits:
- limit_count: 0
  name: Optinmonster Rate Limits
  slug: optinmonster-rate-limits
score:
  band: developing
  composite: 53.8
  coverage:
    artifact_dirs: 21
    catalog_earned: 55.0
    catalog_earned_first_party: 12.0
    catalog_gap: 60.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 84.2
    contract_governance: 4.5
    contract_quality: 39.0
    developer_ergonomics: 57.1
    discoverability: 78.6
    operational_transparency: 39.5
  previous_composite: 53.8
  provenance:
    conformance: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/optinmonster/optinmonster-2026-08-17T081135.png
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
