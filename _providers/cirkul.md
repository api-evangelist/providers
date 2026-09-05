---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
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
    agent_skills: derived
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
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 27.7
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: The agent-facing commerce surface Cirkul serves from its own drinkcirkul.com host. It comprises an anonymous Model Context Protocol (MCP) server at /api/mcp exposing five tools with real JSON Schema i
  name: Cirkul Storefront Agent API
  slug: storefront-agent-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://drinkcirkul.com/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/cirkul_stock/
- group: company
  title: ''
  type: About
  url: https://drinkcirkul.com/pages/about
- group: docs
  title: ''
  type: Documentation
  url: https://drinkcirkul.com/agents.md
- group: start
  title: ''
  type: GettingStarted
  url: https://drinkcirkul.com/pages/getting-started
- group: operate
  title: ''
  type: Support
  url: https://drinkcirkul.com/pages/contact-us
- group: operate
  title: ''
  type: HelpCenter
  url: https://drinkcirkul.com/pages/faq
- group: company
  title: ''
  type: Blog
  url: https://drinkcirkul.com/blogs/cirkular
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/drinkcirkul
- group: commercial
  title: ''
  type: Pricing
  url: https://drinkcirkul.com/pages/plans
- group: start
  title: ''
  type: SignUp
  url: https://drinkcirkul.com/account/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://drinkcirkul.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://drinkcirkul.com/policies/privacy-policy
- group: company
  title: ''
  type: Careers
  url: https://drinkcirkul.com/pages/careers
- group: other
  title: ''
  type: StoreLocator
  url: https://drinkcirkul.com/pages/store-locator
- group: other
  title: ''
  type: Sustainability
  url: https://drinkcirkul.com/pages/recycling
- group: agent
  title: ''
  type: MCPServer
  url: mcp/cirkul-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/cirkul-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cirkul-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/cirkul-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cirkul-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/cirkul-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cirkul-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cirkul-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cirkul-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cirkul-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cirkul-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-02'
description: 'Cirkul, Inc. is a Tampa, Florida direct-to-consumer beverage company founded in 2016 by Garrett Waggoner and Andy Gay. Cirkul sells a reusable bottle system paired with patented flavor cartridges — called Sips — that sit in the bottle lid behind a dial, letting a drinker adjust flavor intensity without pre-mixing. The cartridge lines include LifeSip, FitSip and GoSip, covering more than 100 zero-sugar, zero-calorie flavors spanning fruit blends, iced teas, iced coffees and caffeinated and electrolyte formulations. Cirkul does not publish a general-purpose developer API or an OpenAPI definition; its machine-readable surface is an agent-commerce one, served from its own drinkcirkul.com Shopify storefront: an anonymous Model Context Protocol server at /api/mcp, a Universal Commerce Protocol (UCP) merchant profile at /.well-known/ucp, a UCP shopping MCP endpoint at /api/ucp/mcp, published agent instructions at /agents.md and /llms.txt, and OAuth 2.0 / OpenID Connect discovery for
  the Shopify Customer Account API.'
image: https://drinkcirkul.com/cdn/shop/files/MRKTG_0108_25_Meta_Data_Image_Update-You-got-CirkulArtboard_1.jpg
layout: provider
mcp_servers:
- description: ''
  name: Cirkul MCP Server
  slug: cirkul-mcp-server
modified: '2026-08-02'
name: Cirkul
nav: Providers
network: true
overview: 'Cirkul publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Beverages, Consumer Packaged Goods, Direct to Consumer, and E-Commerce.


  Cirkul''s developer surface includes documentation, getting-started guide, support, engineering blog, pricing, signup flow, authentication, and 21 more developer resources.'
random_paper: 20
scopes:
- name: Cirkul Scopes
  scope_count: 4
  slug: cirkul-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: thin
  composite: 27.5
  coverage:
    artifact_dirs: 13
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 42.3
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 27.5
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cirkul/refs/heads/main/screenshots/cirkul-2026-08-07T163427.png
security:
- kind: authentication
  name: Cirkul Authentication
  slug: cirkul-authentication
  summary_line: none/oauth2/openIdConnect/ucp-agent-profile · 4 schemes
- kind: domain-security
  name: Cirkul Domain Security
  slug: cirkul-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cirkul
tags:
- Company
- Beverages
- Consumer Packaged Goods
- Direct to Consumer
- E-Commerce
- Retail
- Subscription Commerce
- Agentic Commerce
- MCP
- Universal Commerce Protocol
- Shopify
- Hydration
website: https://drinkcirkul.com/
---
