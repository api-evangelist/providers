---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 24.1
  scored_at: '2026-08-30'
api_count: 3
apis:
- description: Elysium Health's storefront implements the Universal Commerce Protocol (UCP) for agent-driven commerce, discoverable at https://www.elysiumhealth.com/.well-known/ucp. The merchant profile advertises t
  name: Elysium Health UCP Shopping (Agentic Commerce)
  slug: elysium-ucp-shopping
- description: Shopify Customer Accounts identity surface for elysiumhealth.com. OpenID Connect discovery is published at https://www.elysiumhealth.com/.well-known/openid-configuration (and mirrored at /.well-known/
  name: Elysium Health Customer Account (Shopify OIDC)
  slug: elysium-customer-account
- description: 'Read-only, unauthenticated storefront data endpoints published in Elysium Health''s agent policy: product listings at /products.json, per-product JSON at /products/{handle}.json, collection listings at'
  name: Elysium Health Storefront Product JSON
  slug: elysium-storefront-json
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/elysium-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.elysiumhealth.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.elysiumhealth.com/llms.txt
- group: docs
  title: ''
  type: Documentation
  url: https://www.elysiumhealth.com/agents.md
- group: start
  title: ''
  type: GettingStarted
  url: https://www.elysiumhealth.com/llms.txt
- group: operate
  title: ''
  type: Support
  url: https://www.elysiumhealth.com/pages/support
- group: company
  title: ''
  type: Blog
  url: https://www.elysiumhealth.com/blogs/aging101
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ElysiumHealth
- group: start
  title: ''
  type: SignUp
  url: https://www.elysiumhealth.com/account/login
- group: commercial
  title: ''
  type: Pricing
  url: https://www.elysiumhealth.com/collections/all
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.elysiumhealth.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.elysiumhealth.com/policies/privacy-policy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/elysium-llms.txt
- group: other
  title: ''
  type: AgentsMD
  url: llms/elysium-agents.md
- group: agent
  title: ''
  type: WellKnown
  url: well-known/elysium-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/elysium-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/elysium-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/elysium-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/elysium-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/elysium-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/elysium-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/elysium-data-model.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/elysium-problem-types.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/elysium-browse-catalog.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/elysium-agentic-purchase.md
created: '2026-07-17'
description: Elysium Health is a New York-based consumer longevity and healthspan company founded in 2014 by MIT biologist Leonard Guarente, Eric Marcotulli, and Dan Alminana, and backed by General Catalyst since 2016. It translates academic aging research into direct-to-consumer supplements and diagnostics — Basis (NAD+ / nicotinamide riboside plus pterostilbene), Matter, Signal, Format, Mosaic, Cofactor, Vision, Senolytic Complex, Creatine+, and the Index biological-age epigenetic test — supported by a scientific advisory board that includes multiple Nobel laureates and by academic partnerships and clinical trials published through its Aging Research Center. Elysium publishes no traditional developer API program; its machine-readable surface is an agent-facing commerce stack on Shopify — a Universal Commerce Protocol (UCP) merchant profile at /.well-known/ucp, a UCP MCP endpoint, a published llms.txt / agents.md agent policy, Shopify Customer Account OIDC discovery, and the storefront
  product/collection JSON endpoints.
image: https://www.elysiumhealth.com/cdn/shop/files/share_image_a1a0fd7d-58c0-4fe1-9193-9ca03a2dfcae.png?v=1629386234
layout: provider
mcp_servers:
- description: ''
  name: Elysium Health MCP Server
  slug: elysium-health-mcp-server
modified: '2026-07-20'
name: Elysium Health
nav: Providers
network: true
overview: 'Elysium Health publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Longevity, Supplements, and Consumer Health.


  Elysium Health''s developer surface includes documentation, getting-started guide, support, engineering blog, signup flow, pricing, authentication, and 18 more developer resources.'
random_paper: 20
scopes:
- name: Elysium Scopes
  scope_count: 4
  slug: elysium-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: thin
  composite: 35.0
  coverage:
    artifact_dirs: 14
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 51.8
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 35.0
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 52.5
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/elysium/refs/heads/main/screenshots/elysium-2026-07-25T213214.png
security:
- kind: authentication
  name: Elysium Authentication
  slug: elysium-authentication
  summary_line: openIdConnect/oauth2/none · 4 schemes
- kind: domain-security
  name: Elysium Domain Security
  slug: elysium-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: elysium
tags:
- Company
- Health
- Longevity
- Supplements
- Consumer Health
- Diagnostics
- Agentic Commerce
- Universal Commerce Protocol
- Shopify
- E-Commerce
- MCP
website: https://www.elysiumhealth.com/
---
