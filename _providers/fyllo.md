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
  scored_at: '2026-08-26'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fyllo-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/fyllo-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/fyllo-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/fyllo-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/fyllo-rate-limits.yml
- group: company
  title: ''
  type: Website
  url: https://www.semasio.com/
- group: company
  title: ''
  type: Blog
  url: https://www.semasio.com/resources/blog
- group: operate
  title: ''
  type: Support
  url: https://www.semasio.com/contact/general
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.semasio.com/legal/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.semasio.com/legal/semasio-privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.semasio.com/company/newsroom
- group: company
  title: ''
  type: About
  url: https://www.semasio.com/company/about
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/semasio/
- group: other
  title: ''
  type: SecondaryMarketListing
  url: https://forgeglobal.com/fyllo_stock/
coverage:
  checked: '2026-08-16'
  detail: Semasio's entire 324-page sitemap is marketing, legal, case-study and podcast content with no developer, API or documentation path, and the only non-marketing hosts it operates — the uip.semasio.net platform UI, which serves a disallow-all robots.txt, and an authentik single sign-on at auth.semasio.net — return 404 for every OpenAPI, GraphQL, MCP and agent-card path probed.
  evidence:
  - status: 200
    url: https://www.semasio.com/sitemap.xml
  - status: 404
    url: https://uip.semasio.net/openapi.json
  - status: 404
    url: https://uip.semasio.net/graphql
  - status: 404
    url: https://www.semasio.com/.well-known/agent-card.json
  - status: 404
    url: https://www.semasio.com/llms.txt
  reason: no-developer-program
  state: none
created: '2026-08-16'
description: Semasio is a Hamburg, Germany advertising-technology company whose semantic targeting platform builds audience, contextual and brand-fit segments for brands, agencies and DSPs across roughly 30 languages and 50 countries. Founded in 2010, it was acquired in 2022 by Casters Holdings, Inc. operating under the Fyllo brand; the combined business traded as Fyllo|Semasio, rebranded to Semasio in April 2024, and was acquired by Samba TV on 31 October 2024. Products include Audience Targeting, Audience Extension, Contextual Targeting, ContextualPLUS, Brand Fit, Interactive Screens, HypertailPMP and the Semasio Factory data onboarding and modeling service. Semasio operates a login-only platform (uip.semasio.net) behind an authentik single sign-on host and publishes no public developer program, API reference, SDK or machine-readable specification.
image: https://cdn.prod.website-files.com/65f445b220ec08022f24d171/661d908d87157eb6fe65f1bd_opengraph-global.png
layout: provider
modified: '2026-08-16'
name: Semasio
nav: Providers
network: true
overview: 'Semasio is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Advertising, Marketing, AdTech, and Audience Targeting.


  Semasio''s developer surface includes engineering blog, support, and 12 more developer resources.'
plans:
- name: Fyllo Plans Pricing
  plan_count: 0
  slug: fyllo-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Fyllo Rate Limits
  slug: fyllo-rate-limits
score:
  band: emerging
  composite: 11.8
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 61.1
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 11.8
  provenance:
    conformance: first-party
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: domain-security
  name: Fyllo Domain Security
  slug: fyllo-domain-security
  summary_line: TLSv1.3 · DMARC
slug: fyllo
tags:
- Company
- Advertising
- Marketing
- AdTech
- Audience Targeting
- Contextual Advertising
- Data
- Segments
- Programmatic
website: https://www.semasio.com/
---
