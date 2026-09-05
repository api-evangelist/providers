---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: platform
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 25.2
  scored_at: '2026-09-04'
api_count: 2
apis:
- description: The agent-facing commerce surface of the SAMBAZON online store. The merchant profile at /.well-known/ucp advertises the Universal Commerce Protocol (versions 2026-04-08 and 2026-01-23) over an MCP/JSO
  name: SAMBAZON Storefront Agentic Commerce (UCP/MCP)
  slug: sambazon-storefront-agentic-commerce-ucpmcp
- description: 'Read-only, unauthenticated Shopify storefront JSON endpoints published on the SAMBAZON store host and named in its own agents.md/llms.txt: /products.json, /products/{handle}.json, /collections/{handle'
  name: SAMBAZON Storefront Product JSON
  slug: sambazon-storefront-product-json
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sambazon-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.sambazon.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.sambazon.com/agents.md
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sambazon-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/sambazon-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/sambazon-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sambazon-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/sambazon-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/sambazon-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/sambazon-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/sambazon-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sambazon-lifecycle.yml
- group: company
  title: ''
  type: Blog
  url: https://www.sambazon.com/pages/blog
- group: operate
  title: ''
  type: Support
  url: https://help.sambazon.com/hc/en-us/requests/new
- group: start
  title: ''
  type: SignUp
  url: https://www.sambazon.com/account/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sambazon.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sambazon.com/policies/privacy-policy
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/sambazon_stock/
created: '2026-08-05'
description: 'SAMBAZON (Sustainable Management of the Brazilian Amazon) is a San Clemente, California organic açaí food and beverage company founded in 2000, selling frozen açaí bowls, smoothie packs, bowl blends and juices through grocery, food service and its own direct-to-consumer store in 45+ countries. It is not a software vendor and publishes no developer program, but its Shopify-hosted storefront at www.sambazon.com exposes a real, public, machine-readable agentic-commerce surface: an llms.txt and agents.md agent instruction set, a Universal Commerce Protocol (UCP) merchant profile at /.well-known/ucp, a UCP/MCP JSON-RPC endpoint at /api/ucp/mcp, Shopify customer-account OpenID Connect metadata, and read-only storefront product/collection JSON endpoints.'
image: https://www.sambazon.com/cdn/shop/files/EnjoyTheDelicousPowersOfAcai_DefaultMetaImageV2.jpg?v=1738620841&width=1000
layout: provider
mcp_servers:
- description: ''
  name: SAMBAZON Storefront UCP/MCP Server
  slug: sambazon-storefront-ucpmcp-server
modified: '2026-08-05'
name: Sambazon
nav: Providers
network: true
overview: 'Sambazon publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Food and Beverage, Consumer Packaged Goods, E-Commerce, and Agentic Commerce.


  Sambazon''s developer surface includes documentation, authentication, engineering blog, support, signup flow, and 14 more developer resources.'
random_paper: 19
scopes:
- name: Sambazon Scopes
  scope_count: 0
  slug: sambazon-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 23.8
  coverage:
    artifact_dirs: 12
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 23.8
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sambazon/refs/heads/main/screenshots/sambazon-2026-09-02T154343.png
security:
- kind: authentication
  name: Sambazon Authentication
  slug: sambazon-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Sambazon Domain Security
  slug: sambazon-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sambazon
tags:
- Company
- Food and Beverage
- Consumer Packaged Goods
- E-Commerce
- Agentic Commerce
- Universal Commerce Protocol
- MCP
- Shopify
- Retail
- Sustainability
website: https://www.sambazon.com/
---
