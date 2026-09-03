---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: platform
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 21.6
  scored_at: '2026-09-02'
api_count: 4
apis:
- description: Anonymous agent-commerce surface for the Prime Labs supplement storefront, implementing the Universal Commerce Protocol 2026-04-08 over MCP. Thirteen tools cover catalog search, product lookup, cart l
  name: Prime Labs Storefront Agent API (UCP / MCP)
  slug: prime-labs-storefront-agent-api-ucp-mcp
- description: Anonymous agent-commerce surface for the Vital Vitamins beauty and longevity supplement storefront, implementing the Universal Commerce Protocol 2026-04-08 over MCP with the same thirteen catalog, car
  name: Vital Vitamins Storefront Agent API (UCP / MCP)
  slug: vital-vitamins-storefront-agent-api-ucp-mcp
- description: Anonymous agent-commerce surface for the Happy Healthy Hippie plant-based herbal wellness storefront, implementing the Universal Commerce Protocol 2026-04-08 over MCP with the same thirteen catalog, c
  name: Happy Healthy Hippie Storefront Agent API (UCP / MCP)
  slug: happy-healthy-hippie-storefront-agent-api-ucp-mcp
- description: 'Anonymous agent-commerce surface for the Asterwood peptide-powered skincare storefront, implementing the Universal Commerce Protocol 2026-04-08 over MCP with the same thirteen catalog, cart, checkout '
  name: Asterwood Storefront Agent API (UCP / MCP)
  slug: asterwood-storefront-agent-api-ucp-mcp
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://boostedcommerce.com
- group: company
  title: ''
  type: About
  url: https://boostedcommerce.com/about/
- group: operate
  title: ''
  type: Support
  url: https://boostedcommerce.com/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://boostedcommerce.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://boostedcommerce.com/privacy-policy-2/
- group: other
  title: ''
  type: Accessibility
  url: https://boostedcommerce.com/accessibility/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/boosted-commerce
- group: other
  title: ''
  type: Investment
  url: https://forgeglobal.com/boosted-commerce_stock/
- group: agent
  title: ''
  type: MCPServer
  url: mcp/boosted-commerce-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/boosted-commerce-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/boosted-commerce-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/boosted-commerce-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/boosted-commerce-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/boosted-commerce-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: conventions/boosted-commerce-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/boosted-commerce-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/boosted-commerce-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/boosted-commerce-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/boosted-commerce-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-08'
description: 'Boosted Commerce is a Los Angeles based consumer brand platform that acquires and operates direct-to-consumer and Amazon FBA businesses in health, wellness, beauty and longevity. Founded by Keith Richman and Charlie Chanaratsopon, the company runs a portfolio of supplement and skincare brands — Prime Labs, Vital Vitamins, Happy Healthy Hippie and Asterwood — and is expanding those brands from marketplace and DTC channels into national retail with EDI-ready vendor operations. Boosted Commerce publishes no first-party developer program of its own, but every brand storefront runs on Shopify and serves a live, anonymous agent-commerce surface: a Universal Commerce Protocol (UCP) merchant profile at /.well-known/ucp, agent instructions at /llms.txt and /agents.md, and a Model Context Protocol endpoint at /api/ucp/mcp exposing 13 catalog, cart, checkout and order tools with published JSON Schema inputs.'
image: https://boostedcommerce.com/wp-content/uploads/2026/07/Boosted_Green_Ico_512-300x300.png
layout: provider
mcp_servers:
- description: ''
  name: Boosted Commerce MCP Server
  slug: boosted-commerce-mcp-server
modified: '2026-08-08'
name: Boosted Commerce
nav: Providers
network: true
overview: 'Boosted Commerce publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, E-Commerce, Retail, Consumer Packaged Goods, and Health and Wellness.


  Boosted Commerce''s developer surface includes support, authentication, and 18 more developer resources.'
random_paper: 2
score:
  band: emerging
  composite: 22.4
  coverage:
    artifact_dirs: 11
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 28.0
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 22.4
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 31.3
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/boosted-commerce/refs/heads/main/screenshots/boosted-commerce-2026-09-02T144936.png
security:
- kind: authentication
  name: Boosted Commerce Authentication
  slug: boosted-commerce-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Boosted Commerce Domain Security
  slug: boosted-commerce-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: boosted-commerce
tags:
- Company
- E-Commerce
- Retail
- Consumer Packaged Goods
- Health and Wellness
- Supplements
- Beauty
- Agentic Commerce
- Universal Commerce Protocol
- MCP
- Shopify
- Direct to Consumer
website: https://boostedcommerce.com
---
