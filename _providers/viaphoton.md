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
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 3
common:
- group: build
  title: ''
  type: Packages
  url: packages/viaphoton-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/viaphoton-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/viaphoton-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/viaphoton-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/viaphoton-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://viaphoton.com/
- group: company
  title: ''
  type: Blog
  url: https://viaphoton.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://viaphoton.com/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://viaphoton.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://viaphoton.com/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/viaPhoton
- group: other
  title: ''
  type: Configurator
  url: https://configure.viaphoton.com/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/viaphoton_stock/
coverage:
  checked: '2026-09-02'
  detail: viaPhoton is a fiber optic cable-assembly manufacturer that sells through a configure-price-quote tool, not a developer program; STEP 0b contract discovery did surface one first-party API host (pp-api.viaphoton.com, the Node/Express backend of the public product configurator, keyed from the configurator page) but it serves no spec, reference, or discovery document, and every OpenAPI, Swagger, GraphQL, MCP and agent-card path 404s across all three viaPhoton hosts.
  evidence:
  - status: 404
    url: https://pp-api.viaphoton.com/openapi.json
  - status: 404
    url: https://pp-api.viaphoton.com/graphql
  - status: 404
    url: https://configure.viaphoton.com/.well-known/agent-card.json
  - status: 202
    url: https://viaphoton.com/llms.txt
  reason: no-developer-program
  state: none
created: '2026-09-02'
description: viaPhoton is a Naperville, Illinois fiber optic connectivity manufacturer, founded in 2020, that designs and builds high-density fiber solutions for hyperscale and enterprise data centers, 5G and broadband access networks, and AI network fabrics. Its catalog spans inside-plant products (fiber trunks, fiber arrays, patch cords, MPO/MTP connectivity, structured cabling) and outside-plant products (outdoor fiber jumpers, fiber drop cables, outdoor trunks), produced in a domestic "micro-factory" model intended to shorten lead times against an industry that sources roughly 90% of fiber optic material offshore. viaPhoton sells through a configure-price-quote product configurator rather than a developer program; it publishes no public API, SDK, developer portal, or machine-readable API contract.
image: https://configure.viaphoton.com/img/logo_with_text.svg
layout: provider
modified: '2026-09-02'
name: viaPhoton
nav: Providers
network: true
overview: 'viaPhoton is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fiber Optics, Telecommunications, Networking, and Data Centers.


  viaPhoton''s developer surface includes engineering blog, support, and 11 more developer resources.'
plans:
- name: Viaphoton Plans Pricing
  plan_count: 0
  slug: viaphoton-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Viaphoton Rate Limits
  slug: viaphoton-rate-limits
score:
  band: minimal
  composite: 9.8
  coverage:
    artifact_dirs: 6
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 5.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 19.4
  schema_version: 0.18.0
  scored_at: '2026-09-02'
security:
- kind: domain-security
  name: Viaphoton Domain Security
  slug: viaphoton-domain-security
  summary_line: TLSv1.3 · DMARC
slug: viaphoton
tags:
- Company
- Fiber Optics
- Telecommunications
- Networking
- Data Centers
- Broadband
- Manufacturing
- Hardware
- Connectivity
- 5G
website: https://viaphoton.com/
---
