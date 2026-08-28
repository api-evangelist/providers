---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
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
    error_semantics: false
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
  score: 18.0
  scored_at: '2026-08-26'
api_count: 3
apis:
- description: First-party GraphQL router backing the Brigad talent (freelancer) app — talents, propositions/missions, onboarding, experiences, availabilities and billing. Endpoint is hardcoded in Brigad's own web S
  name: Brigad GraphQL (Talent app)
  slug: brigad-graphql-talent-app
- description: First-party GraphQL router backing the Brigad business/agent app — businesses, sites, missions, mission templates, network/contacts, invoices and payments. Endpoint is hardcoded in Brigad's own web SP
  name: Brigad GraphQL (Business app)
  slug: brigad-graphql-business-app
- description: First-party GraphQL router exposing Brigad's legacy monolith schema (382 queries, 501 mutations spanning both talent and business domains). Anonymous introspection is open. Undocumented internal app b
  name: Brigad GraphQL (Legacy monolith)
  slug: brigad-graphql-legacy-monolith
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://www.brigad.co/
- group: operate
  title: ''
  type: Support
  url: https://help.brigad.co/en/
- group: company
  title: ''
  type: Blog
  url: https://www.brigad.co/en-gb/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.brigad.co/en-gb/business-service-fees
- group: start
  title: ''
  type: SignUp
  url: https://app.hsp.brigad.co/register
- group: start
  title: ''
  type: Login
  url: https://app.hsp.brigad.co/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.brigad.co/en-gb/legal/general-conditions-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.brigad.co/en-gb/legal/privacy-policy
- group: auth
  title: ''
  type: DomainSecurity
  url: security/brigad-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Brigad
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/brigad-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/brigad-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/brigad-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/brigad-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/brigad-mcp.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/brigad-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/brigad-plans-pricing.yml
created: '2026-07-17'
description: Brigad is a French-founded staffing marketplace that connects verified, self-employed hospitality and healthcare professionals with businesses that need short-term cover. Founded in Paris in 2016 by Florent Malbranche, Jean Lebrument and Alexandre Rovetto, the platform pairs a talent app (for freelance chefs, waiters, bartenders, carers and nurses) with a business app (for restaurants, caterers, hotels, clinics, retirement homes and hospitals) and uses a matching algorithm to fill missions, often within hours. Brigad operates in France and the United Kingdom, has supported over 12,000 businesses and 23,000 independent professionals, and completed more than 300,000 missions. It is backed by Balderton Capital, Wendel, Serena and Square, having raised roughly €50 million to date. Brigad publishes no documented public developer API or developer program, but its web app is powered by first-party GraphQL routers on brigad.cloud (talent, business/agent and legacy schemas) whose anonymous
  introspection is open; those live SDLs are captured here as an undocumented internal contract, alongside the company identity and public web properties tracked for the API Evangelist network.
image: https://cdn.prod.website-files.com/650bff9b13318f3181a5cfbc/658043e5f20fc2fc6360d636_opengraph%20-%20EN.webp
layout: provider
mcp_servers:
- description: ''
  name: Brigad MCP Server
  slug: brigad-mcp-server
modified: '2026-08-17'
name: Brigad
nav: Providers
network: true
overview: 'Brigad publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Staffing, Marketplace, Hospitality, and Healthcare.


  Brigad''s developer surface includes support, engineering blog, pricing, signup flow, authentication, and 12 more developer resources.'
plans:
- name: Brigad Plans Pricing
  plan_count: 0
  slug: brigad-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Brigad Rate Limits
  slug: brigad-rate-limits
score:
  band: thin
  composite: 31.3
  delta: 0.0
  facets:
    access_clarity: 38.2
    commercial_clarity: 38.2
    contract_governance: 0.0
    contract_quality: 37.2
    developer_ergonomics: 19.0
    discoverability: 92.6
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 31.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 25.0
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/brigad/refs/heads/main/screenshots/brigad-2026-07-25T203819.png
security:
- kind: authentication
  name: Brigad Authentication
  slug: brigad-authentication
  summary_line: bearer-session · 1 scheme
- kind: domain-security
  name: Brigad Domain Security
  slug: brigad-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: brigad
tags:
- Company
- Staffing
- Marketplace
- Hospitality
- Healthcare
- Gig Economy
- Freelance
- Workforce
website: https://www.brigad.co/
---
