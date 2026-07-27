---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 6.7
  scored_at: '2026-07-27'
api_count: 4
apis:
- description: Build small in-editor apps that interact with the Framer Editor and CMS. Plugins can read and modify the canvas, manage CMS collections and items, register UI panels, and call out to external services
  name: Framer Plugin API
  slug: framer-plugin-api
- description: Author custom React components with visual property controls (PropertyControls) so designers can use them on the canvas. Used to render anything from custom widgets to data-driven UI within Framer sit
  name: Framer Code Components API
  slug: framer-code-components
- description: Higher-order-component-style overrides that modify Layer/Component properties at runtime — used for state, animation, data binding, and behavior.
  name: Framer Code Overrides API
  slug: framer-code-overrides
- description: Lets developers expose external API endpoints inside Framer so designers can bind site content to them without writing code. Used for things like dynamic CMS sources, third-party data, and form submis
  name: Framer Fetch
  slug: framer-fetch
artifact_total: 9
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/framer-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/framer-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/framer
- group: company
  title: ''
  type: Website
  url: https://www.framer.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.framer.com/developers/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.framer.com/pricing/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/framer
- group: commercial
  title: ''
  type: Plans
  url: plans/framer-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/framer-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/framer-finops.yml
- group: other
  title: ''
  type: ProductPage
  url: https://www.framer.com/cms
created: '2026-05-08'
description: 'Framer is a design tool and CMS for shipping production websites without code. The Framer developer surface is centred on in-editor extensibility: the Plugin API for building tools that interact with the Framer Editor and CMS, Code Components for custom React components, Code Overrides for HOC-style mutations, and Fetch for letting designers wire site content to external APIs without code. Framer does not publish a general-purpose REST API for site management at the time of reconciliation.'
finops:
- name: Framer Finops
  service_category: Productivity
  slug: framer-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/framer.png
layout: provider
modified: '2026-07-25'
name: Framer
nav: Providers
network: true
overview: 'Framer publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Productivity, Design, No-Code, Web Design, and SaaS.


  Framer''s developer surface includes pricing, GitHub presence, and 9 more developer resources.'
plans:
- name: Framer Plans Pricing
  plan_count: 6
  slug: framer-plans-pricing
random_paper: 25
rate_limits:
- limit_count: 4
  name: Framer Rate Limits
  slug: framer-rate-limits
score:
  band: emerging
  composite: 26.5
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 26.5
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/framer/refs/heads/main/screenshots/framer-2026-06-20T181511.png
security:
- kind: domain-security
  name: Framer Domain Security
  slug: framer-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Framer Vulnerability Disclosure
  slug: framer-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: framer
tags:
- Productivity
- Design
- No-Code
- Web Design
- SaaS
website: https://www.framer.com/
---
