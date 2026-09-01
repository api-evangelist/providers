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
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-01'
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
overview: 'Framer publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Productivity, Design, No-Code, Web Design, and Software-as-a-Service.


  Framer''s developer surface includes pricing, GitHub presence, and 9 more developer resources.'
plans:
- name: Framer Plans Pricing
  plan_count: 6
  slug: framer-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 4
  name: Framer Rate Limits
  slug: framer-rate-limits
score:
  band: emerging
  composite: 19.6
  coverage:
    artifact_dirs: 6
    catalog_gap: 66.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 19.6
  schema_version: 0.17.2
  scored_at: '2026-09-01'
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
- Software-as-a-Service
website: https://www.framer.com/
---
