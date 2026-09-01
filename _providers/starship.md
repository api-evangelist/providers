---
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
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/starship-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.starship.xyz/
- group: company
  title: ''
  type: About
  url: https://www.starship.xyz/about/
- group: company
  title: ''
  type: Blog
  url: https://www.starship.xyz/newsroom/
- group: company
  title: ''
  type: Press
  url: https://www.starship.xyz/press/
- group: operate
  title: ''
  type: Support
  url: https://www.starship.xyz/contact/
- group: operate
  title: ''
  type: FAQ
  url: https://www.starship.xyz/faq/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/starship-technologies
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.starship.xyz/legal-terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.starship.xyz/privacy/
- group: company
  title: ''
  type: Careers
  url: https://www.starship.xyz/careers/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://www.hiive.com/securities/starship-stock
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/starship-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/starship-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/starship-rate-limits.yml
coverage:
  checked: '2026-08-29'
  detail: Starship's Delivery Apps page states its APIs create delivery jobs, load robots and return status updates, but the "full developer toolkit, documentation and support" it names is released only after a commercial conversation via business@starship.co — the 43-page site sitemap contains no developer, docs, reference or pricing page at all.
  evidence:
  - status: 200
    url: https://www.starship.xyz/delivery-apps/
  - status: 200
    url: https://www.starship.xyz/page-sitemap.xml
  - status: 404
    url: https://api.starship.xyz/openapi.json
  - status: 404
    url: https://api.starship.xyz/graphql
  - status: 404
    url: https://www.starship.xyz/.well-known/agent-card.json
  reason: sales-gate
  state: gated
created: '2026-08-29'
description: 'Starship Technologies is an autonomous last-mile delivery company that operates a global fleet of self-driving, sidewalk-going delivery robots. Founded in 2014 by Skype co-founders Ahti Heinla and Janus Friis, the company runs commercial robot delivery on university campuses, in residential neighborhoods, on industrial sites and for grocery and restaurant partners across the United States, the United Kingdom, Estonia, Finland, Germany and Denmark, and has completed more than 10 million autonomous deliveries. Its commercial product, Delivery by Starship, is a delivery-as-a-service offering that partners integrate into their own ordering apps: Starship states that its APIs let a partner create delivery jobs, load robots, obtain status updates and handle delivery cancellations, backed by a developer toolkit, documentation, ready-made components and support. That developer surface is not published to the open web — Starship provides it to partners after a commercial conversation
  via business@starship.co, so no public specification, reference or portal exists to profile.'
image: https://www.starship.xyz/wp-content/uploads/2024/11/cropped-Starship_app_icon_ios_1024-1-192x192.png
layout: provider
modified: '2026-08-29'
name: Starship Technologies
nav: Providers
network: true
overview: 'Starship Technologies is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Robotics, Autonomous Vehicles, Last Mile Delivery, and Logistics.


  Starship Technologies'' developer surface includes engineering blog, support, FAQ, and 12 more developer resources.'
plans:
- name: Starship Plans Pricing
  plan_count: 0
  slug: starship-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Starship Rate Limits
  slug: starship-rate-limits
score:
  band: emerging
  composite: 11.0
  coverage:
    artifact_dirs: 6
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 11.0
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Starship Domain Security
  slug: starship-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: starship
tags:
- Company
- Robotics
- Autonomous Vehicles
- Last Mile Delivery
- Logistics
- Food Delivery
- Grocery
- Delivery as a Service
website: https://www.starship.xyz/
---
