---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: ActivityHero's provider integration surface — outbound, HMAC-SHA256-signed JSON webhooks that sync registrations and activity schedules between ActivityHero and a provider's own systems (configured un
  name: ActivityHero Registration & Schedule Webhooks
  slug: activityhero-registration-schedule-webhooks
artifact_total: 4
asyncapis:
- description: ''
  name: Activityhero Webhooks
  slug: activityhero-webhooks
common:
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/activityhero-webhooks.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/activityhero-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/activityhero-conventions.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/activityhero-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/activityhero-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/activityhero-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://help.activityhero.com/api
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.activityhero.com
- group: company
  title: ''
  type: Blog
  url: https://www.activityhero.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://business.activityhero.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://activityhero.com/pages/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://activityhero.com/pages/privacy
- group: company
  title: ''
  type: Website
  url: https://activityhero.com
created: '2026-07-17'
description: ActivityHero is an online marketplace connecting families with kids' camps, classes, and enrichment activities — a one-stop shop to find top-rated summer camps, holiday camps, and after-school classes near you across categories like art, science, sports, dance, and online programs. For activity providers it offers marketing and registration software (MarketingHero and custom registration software) plus programs for school districts. ActivityHero's developer surface is a provider integration built on outbound, HMAC-SHA256 signed JSON webhooks (a Registration API and a Schedule API) rather than a public REST API; it was surfaced as a portfolio company of 500 Global and enriched into the API Evangelist network from its published help-center docs.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/activityhero.png
layout: provider
modified: '2026-07-17'
name: ActivityHero
nav: Providers
network: true
overview: 'ActivityHero publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Kids Activities, Camps, Classes, and Marketplace.


  The ActivityHero catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  ActivityHero''s developer surface includes authentication, documentation, engineering blog, pricing, and 9 more developer resources.'
random_paper: 5
score:
  band: thin
  composite: 32.5
  coverage:
    artifact_dirs: 8
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.2
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 41.6
    developer_ergonomics: 28.6
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 32.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 37.0
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/activityhero/refs/heads/main/screenshots/activityhero-2026-07-25T181531.png
security:
- kind: authentication
  name: Activityhero Authentication
  slug: activityhero-authentication
  summary_line: signature · 1 scheme
- kind: domain-security
  name: Activityhero Domain Security
  slug: activityhero-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: activityhero
tags:
- Company
- Kids Activities
- Camps
- Classes
- Marketplace
- Registration
- Webhook
- Education
website: https://activityhero.com
---
