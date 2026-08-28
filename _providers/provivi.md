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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.9
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: The KeystoneJS 5 headless-CMS GraphQL backend that serves the provivi.com marketing site. It exposes 199 types, 83 query fields and 122 mutation fields covering the site's content model — Article, Pre
  name: Provivi Content GraphQL API
  slug: provivi-content-graphql-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/provivi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.provivi.com/en
- group: company
  title: ''
  type: Blog
  url: https://www.provivi.com/en/news-articles
- group: operate
  title: ''
  type: PressReleases
  url: https://www.provivi.com/en/press-release
- group: operate
  title: ''
  type: Support
  url: https://www.provivi.com/en/contact-us
- group: operate
  title: ''
  type: FAQ
  url: https://www.provivi.com/en/frequently-asked-questions
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.provivi.com/en/terms-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.provivi.com/en/privacy-policy
- group: company
  title: ''
  type: Careers
  url: https://www.provivi.com/en/careers
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/provivi-inc-
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/Provivitm
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/channel/UCyb-kB-BI_xMpXO3bzmjrBA
- group: docs
  title: ''
  type: GraphQL
  url: graphql/provivi-content-schema.graphql
- group: auth
  title: ''
  type: Authentication
  url: authentication/provivi-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/provivi-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/provivi-data-model.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/provivi-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/provivi-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/provivi-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/provivi-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/provivi-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/provivi-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/provivi-packages.yml
created: '2026-08-26'
description: 'Provivi, Inc. is an agricultural biotechnology company headquartered at 1701 Colorado Avenue, Santa Monica, California, founded in 2013 by Pedro Coelho, Peter Meinhold and Nobel laureate Frances Arnold. Provivi manufactures insect sex pheromones using a patented catalytic olefin-metathesis process that cuts production cost far enough to make mating-disruption pest control economic on high-acreage row crops — corn, rice and soy — rather than only on high-value specialty crops. Its commercial products target fall armyworm (Spodoptera frugiperda) and are distributed through regional partners including UPL in Mexico, Koppert in Brazil, AgNova in Australia, Andermatt in East Africa and Susbin in Argentina. Provivi is not a software vendor: it runs no developer program, publishes no API documentation, terms of use or pricing for machine access, and ships no SDKs. The only machine-readable surface it operates is the undocumented KeystoneJS GraphQL backend that serves content to provivi.com.'
graphqls:
- description: This is the KeystoneJS 5 headless-CMS backend that serves the `provivi.com` marketing site. It is the
  name: Provivi Content GraphQL API
  slug: provivi-graphql
image: https://www.provivi.com/assets/favicon.png
layout: provider
modified: '2026-08-26'
name: Provivi
nav: Providers
network: true
overview: 'Provivi publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Agriculture, AgTech, Biotechnology, Crop Protection, and Pheromones.


  Provivi''s developer surface includes engineering blog, support, FAQ, YouTube channel, authentication, and 18 more developer resources.'
plans:
- name: Provivi Plans Pricing
  plan_count: 0
  slug: provivi-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Provivi Rate Limits
  slug: provivi-rate-limits
score:
  band: emerging
  composite: 24.7
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 37.2
    developer_ergonomics: 19.0
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 0.0
  provenance:
    conformance: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
security:
- kind: authentication
  name: Provivi Authentication
  slug: provivi-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Provivi Domain Security
  slug: provivi-domain-security
  summary_line: TLSv1.3 · DMARC
slug: provivi
tags:
- Agriculture
- AgTech
- Biotechnology
- Crop Protection
- Pheromones
- Sustainability
- Content Management
- GraphQL
website: https://www.provivi.com/en
---
