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
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: 'Agent-facing commerce surface for the True & Co Shopify storefront: a hosted Universal Commerce Protocol (UCP) MCP endpoint for catalog search, cart, and checkout, backed by Shopify Customer Account O'
  name: True & Co UCP Agent Commerce
  slug: true-co-ucp-agent-commerce
artifact_total: 4
common:
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/true-and-co-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/true-and-co-well-known.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/true-and-co-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/true-and-co-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/true-and-co-domain-security.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/true-and-co-conventions.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/true-and-co-llms.txt
- group: commercial
  title: ''
  type: TermsOfService
  url: https://trueandco.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://trueandco.com/policies/privacy-policy
created: '2026-07-17'
description: 'True & Co is a direct-to-consumer women''s intimates and lingerie brand, originally venture-backed (Cowboy Ventures, Uncork Capital) and now operating under PVH Corp. It sells bras, underwear, and loungewear online through a Shopify-hosted storefront at trueandco.com. The store exposes no traditional developer API, but it does expose a modern agent-commerce surface: a hosted Universal Commerce Protocol (UCP) MCP endpoint for catalog, cart, and checkout, Shopify Customer Account OAuth 2.0 / OIDC for buyer identity, a public read-only storefront JSON surface, and an agent-facing llms.txt / agents.md.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/true-and-co.png
layout: provider
modified: '2026-07-21'
name: True & Co
nav: Providers
network: true
overview: 'True & Co publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Retail, E-Commerce, and Apparel.


  True & Co''s developer surface includes authentication and 8 more developer resources.'
random_paper: 5
scopes:
- name: True And Co Scopes
  scope_count: 0
  slug: true-and-co-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 14.2
  coverage:
    artifact_dirs: 8
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 14.2
  provenance:
    mcp: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/true-and-co/refs/heads/main/screenshots/true-and-co-2026-09-02T164331.png
security:
- kind: authentication
  name: True And Co Authentication
  slug: true-and-co-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: True And Co Domain Security
  slug: true-and-co-domain-security
  summary_line: no transport/DNS hardening detected
slug: true-and-co
tags:
- Company
- Consumer
- Retail
- E-Commerce
- Apparel
- Intimates
- Agentic Commerce
- Shopify
- MCP
---
