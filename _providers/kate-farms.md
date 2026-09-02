---
agent_readiness:
  band: agent-native
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
    idempotency: documented
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 46.4
  scored_at: '2026-09-01'
api_count: 2
apis:
- description: The Shopify Storefront GraphQL API as deployed on Kate Farms' own host. Anonymous introspection succeeded on 2026-08-04, returning 424 types, 35 root query fields and 41 mutations covering products, c
  name: Kate Farms Storefront GraphQL API
  slug: kate-farms-storefront-graphql-api
- description: Kate Farms' storefront advertises the Universal Commerce Protocol (UCP) at /.well-known/ucp and exposes an MCP endpoint for agent-driven commerce — catalog search and lookup, cart, discount, fulfillme
  name: Kate Farms UCP Agentic Commerce (MCP)
  slug: kate-farms-ucp-agentic-commerce-mcp
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://katefarms.com/
- group: docs
  title: ''
  type: Documentation
  url: https://shop.katefarms.com/agents.md
- group: start
  title: ''
  type: GettingStarted
  url: https://shop.katefarms.com/agents.md
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kate-farms-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/kate-farms-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/kate-farms-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/kate-farms-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/kate-farms-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/kate-farms-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/kate-farms-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/kate-farms-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/kate-farms-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/kate-farms-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kate-farms-domain-security.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/kate-farms-rate-limits.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  title: ''
  type: Support
  url: https://katefarms.com/contact-us
- group: operate
  title: ''
  type: HelpCenter
  url: https://katefarms.com/help
- group: start
  title: ''
  type: SignUp
  url: https://shop.katefarms.com/account/register
- group: start
  title: ''
  type: Login
  url: https://shop.katefarms.com/account/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://shop.katefarms.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://katefarms.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfUse
  url: https://katefarms.com/terms-of-use/
- group: other
  title: ''
  type: Accessibility
  url: https://katefarms.com/accessibility/
- group: company
  title: ''
  type: Careers
  url: https://katefarms.com/careers/
- group: company
  title: ''
  type: About
  url: https://katefarms.com/about/
- group: other
  title: ''
  type: HealthcareProfessionals
  url: https://katefarmsmedical.com/
created: '2026-08-04'
description: 'Kate Farms is a Santa Barbara, California nutrition company that makes USDA-certified-organic, plant-based (organic yellow pea protein) medical nutrition formulas and shakes for tube feeding and oral supplemental nutrition, used in more than 1,400 hospitals and prescribed across pediatric and adult care. The company sells direct to consumers through a Shopify storefront at shop.katefarms.com and publishes clinical and reimbursement material for healthcare professionals at katefarmsmedical.com. Its public machine-readable surface is commerce-side rather than a developer product: the storefront exposes an anonymous-introspectable Shopify Storefront GraphQL API, an agent-facing llms.txt / agents.md, and a live Universal Commerce Protocol (UCP) merchant profile with an MCP endpoint for agent-driven catalog search, cart and checkout.'
image: https://cdn.shopify.com/s/files/1/0205/6802/files/KF_Logo_Navy_TM.png
layout: provider
mcp_servers:
- description: ''
  name: Kate Farms MCP Server
  slug: kate-farms-mcp-server
modified: '2026-08-04'
name: Kate Farms
nav: Providers
network: true
overview: 'Kate Farms publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Nutrition, Medical Nutrition, Health, and Food and Beverage.


  Kate Farms'' developer surface includes documentation, getting-started guide, authentication, support, signup flow, and 22 more developer resources.'
random_paper: 16
rate_limits:
- limit_count: 0
  name: Kate Farms Rate Limits
  slug: kate-farms-rate-limits
scopes:
- name: Kate Farms Scopes
  scope_count: 4
  slug: kate-farms-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: developing
  composite: 40.4
  coverage:
    artifact_dirs: 15
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 37.2
    developer_ergonomics: 47.0
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 40.4
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
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kate-farms/refs/heads/main/screenshots/kate-farms-2026-08-07T171111.png
security:
- kind: authentication
  name: Kate Farms Authentication
  slug: kate-farms-authentication
  summary_line: openIdConnect/oauth2/apiKey/none · 5 schemes
- kind: domain-security
  name: Kate Farms Domain Security
  slug: kate-farms-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: kate-farms
tags:
- Company
- Nutrition
- Medical Nutrition
- Health
- Food and Beverage
- Consumer Packaged Goods
- E-Commerce
- Agentic Commerce
- Retail
- Shopify
- GraphQL
website: https://katefarms.com/
---
