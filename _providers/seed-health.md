---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - rate-limits
  - security
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
    consent_identity: true
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
  score: 4.7
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/seed-health-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://seed.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.seed.com/en-US
- group: operate
  title: ''
  type: Support
  url: https://help.seed.com/en-US/contact
- group: company
  title: ''
  type: Blog
  url: https://seed.com/cultured
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/seed-health
- group: commercial
  title: ''
  type: TermsOfService
  url: https://seed.com/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://seed.com/privacy-policy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/seed-health-llms.txt
- group: other
  title: ''
  type: ContentSignal
  url: well-known/seed-health-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/seed-health-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/seed-health-conformance.yml
coverage:
  checked: '2026-08-26'
  detail: 'Seed Health is a direct-to-consumer microbiome supplements brand that ships software only as its own storefront: there is no developer.seed.com (DNS does not resolve), no API reference anywhere on seed.com or help.seed.com, and its one first-party API host, api.seed.com, is the storefront backend that seed.com/robots.txt explicitly closes to crawlers with "Disallow: /api/*"; its only public npm package is a Figma design-token library, and its Practitioner Program integrates through Fullscript and email rather than any programmatic surface.'
  evidence:
  - status: 0
    url: https://developer.seed.com
  - status: 200
    url: https://seed.com/robots.txt
  - status: 404
    url: https://seed.com/.well-known/api-catalog
  - status: 404
    url: https://seed.com/.well-known/agent-card.json
  - status: 200
    url: https://help.seed.com/llms.txt
  reason: no-developer-program
  state: none
created: '2026-08-26'
description: 'Seed Health is a microbiome science company founded in 2017 by Ara Katz and Raja Dhir, headquartered in Los Angeles County, California. It develops and sells clinically studied probiotic, prebiotic and synbiotic consumer products — most notably the DS-01 Daily Synbiotic, the PDS-08 Pediatric Daily Synbiotic and the VS-01 Vaginal Synbiotic — direct to consumers via a subscription commerce site at seed.com, alongside SeedLabs, its environmental and applied-microbiology research arm. Seed publishes a substantial public science, editorial (Cultured) and help-center surface, and maintains a small public GitHub organization, but it operates no public developer program: there is no developer portal, no published API reference, no OpenAPI, GraphQL, AsyncAPI or MCP contract, and its internal storefront API paths are explicitly disallowed in robots.txt. Its practitioner program is fulfilled through Fullscript and email rather than through any integration surface.'
image: https://avatars.githubusercontent.com/u/63071534?v=4
layout: provider
modified: '2026-08-26'
name: Seed Health
nav: Providers
network: true
overview: 'Seed Health is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Consumer Products, Life Sciences, and Microbiome.


  Seed Health''s developer surface includes support, engineering blog, and 10 more developer resources.'
plans:
- name: Seed Health Plans Pricing
  plan_count: 0
  slug: seed-health-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Seed Health Rate Limits
  slug: seed-health-rate-limits
score:
  band: emerging
  composite: 13.7
  coverage:
    artifact_dirs: 9
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 13.7
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 23.8
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/seed-health/refs/heads/main/screenshots/seed-health-2026-09-02T154733.png
security:
- kind: domain-security
  name: Seed Health Domain Security
  slug: seed-health-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: seed-health
tags:
- Company
- Health
- Consumer Products
- Life Sciences
- Microbiome
- Probiotics
- Nutrition
- Subscription Commerce
- Direct to Consumer
- Biotechnology
website: https://seed.com/
---
