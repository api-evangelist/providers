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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.4
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: Private REST API backing the EarthOptics customer application (360 PRO dashboard) at app.earthoptics.com. Served from api.earthoptics.com on gunicorn behind Django REST Framework, with a drf-spectacul
  name: EarthOptics Platform API
  slug: earth-optics-platform-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/earth-optics-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/earth-optics-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/earth-optics-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/earth-optics-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/earth-optics-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/earth-optics-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/earth-optics-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/earth-optics-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/earth-optics-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/earth-optics-security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/earth-optics-llms.txt
- group: company
  title: ''
  type: Website
  url: https://earthoptics.com/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/earth-optics_stock/
- group: company
  title: ''
  type: Blog
  url: https://earthoptics.com/news-insights
- group: operate
  title: ''
  type: Support
  url: https://earthoptics.com/contact-us
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/EarthOptics
- group: start
  title: ''
  type: Login
  url: https://earthoptics.com/customer-login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://earthoptics.com/eula
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://earthoptics.com/privacy-policy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/earthoptics/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/EarthOptics
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/EarthOptics
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/earthoptics/
- group: company
  title: ''
  type: Careers
  url: https://earthoptics.bamboohr.com/jobs/?source=bamboohr
created: '2026-08-01'
description: EarthOptics is a soil data measurement and mapping company headquartered in Minneapolis, Minnesota. It combines proprietary in-field proximal sensing hardware, robotics, genomics and laboratory testing with machine learning models to produce high-resolution sub-field maps of soil compaction, fertility and nutrients, soil biology, moisture and soil organic carbon from far fewer physical samples than conventional soil testing. The company sells measurement and analytics, agronomic planning (crop planning, nutrient management, sub-field scripting) and carbon planning (carbon credit planning, sustainability-as-a-service, 45Z clean-fuel documentation) to farmers, agronomists and consultants, ranchers and landowners, seed suppliers, ag retail, carbon project developers and corporate sustainability teams. Results are delivered through the 360 PRO customer dashboard at app.earthoptics.com and through a dealer network. EarthOptics merged with soil-biology company Pattern Ag and reports
  having mapped more than five million acres. It operates a customer-facing web application backed by a private REST API, but publishes no public developer program, API documentation or SDKs.
image: https://s3.us-east-1.amazonaws.com/assets.earthoptics.com/user-photos/_1200x630_crop_center-center_82_none/seo-global.jpg
layout: provider
modified: '2026-08-01'
name: EarthOptics
nav: Providers
network: true
overview: 'EarthOptics publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Agriculture, AgTech, Soil, and Soil Data.


  EarthOptics'' developer surface includes authentication, engineering blog, support, and 21 more developer resources.'
random_paper: 17
score:
  band: emerging
  composite: 22.8
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 79.6
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 22.8
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 38.8
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/earth-optics/refs/heads/main/screenshots/earth-optics-2026-08-07T164636.png
security:
- kind: authentication
  name: Earth Optics Authentication
  slug: earth-optics-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Earth Optics Domain Security
  slug: earth-optics-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Earth Optics Vulnerability Disclosure
  slug: earth-optics-vulnerability-disclosure
  summary_line: Hackerone · security.txt
slug: earth-optics
tags:
- Company
- Agriculture
- AgTech
- Soil
- Soil Data
- Precision Agriculture
- Soil Carbon
- Carbon
- Sustainability
- Agronomy
- Geospatial
- Remote Sensing
- Soil Health
- Carbon Credits
website: https://earthoptics.com/
---
