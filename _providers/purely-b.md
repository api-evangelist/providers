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
    agent_skills: false
    agentic_access: false
    agentic_commerce: platform
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 15.1
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://purelyb.com
- group: agent
  title: ''
  type: MCPServer
  url: mcp/purely-b-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/purely-b-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/purely-b-conventions.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/purely-b-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/purely-b-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/purely-b-domain-security.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://purelyb.com/policies/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://purelyb.com/policies/terms-of-service
created: '2026-07-17'
description: 'PurelyB is a natural superfood and wellness brand founded by Raja Jesrina Arshad, rooted in ancestral Asian health traditions and selling halal-certified, vegan, gluten-free herbal supplements (Pegaga, Tiger Milk Mushroom, Manjakani, Super Immune-C and a SuperKids line) direct to consumers across Malaysia and Singapore. The storefront runs on Shopify and exposes a standards-based agent-commerce surface: a Universal Commerce Protocol (UCP) merchant profile with a hosted MCP shopping server, Shopify Customer Account OAuth/OIDC, and a published llms.txt for AI shopping agents. Surfaced as a 500 Global portfolio company and enriched from its public developer/agent surface.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/purely-b.png
layout: provider
mcp_servers:
- description: PurelyB is a Shopify storefront that exposes a hosted, remote MCP server via the Universal Commerce Protocol (UCP, ucp.dev) for agent-driven commerce. The server implements the dev.ucp.shopping servic
  name: PurelyB Shopping (UCP)
  slug: purelyb-shopping-ucp
modified: '2026-07-20'
name: Purely B
nav: Providers
network: true
overview: 'Purely B is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Wellness, E-Commerce, Supplements, and Shopify.


  Purely B''s developer surface includes authentication and 8 more developer resources.'
random_paper: 18
score:
  band: emerging
  composite: 12.3
  coverage:
    artifact_dirs: 6
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 12.3
  provenance:
    mcp: first-party
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Purely B Authentication
  slug: purely-b-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Purely B Domain Security
  slug: purely-b-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: purely-b
tags:
- Company
- Wellness
- E-Commerce
- Supplements
- Shopify
- Agentic Commerce
- MCP
website: https://purelyb.com
---
