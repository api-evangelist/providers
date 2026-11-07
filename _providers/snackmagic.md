---
access_model:
  confidence: high
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Snackmagic Agentic Access
  operation_count: 15
  slug: snackmagic-agentic-access
  summary_line: 15 operations · 8 acting
api_count: 1
apis:
- baseURL: https://api.bystadium.com/api/v2
  baseurl_source: declared
  description: 'Stadium uses JWT (as Bearer token) for authentication. API provides 4 different methods to generate the token: 1. Client Credentials 2. Authorization Code (OAuth2) 3. Authorization Code using PKCE 4. '
  name: SnackMagic Authentication API
  slug: snackmagic-authentication-api
- baseURL: https://api.bystadium.com/api/v2
  baseurl_source: declared
  description: Automation related API endpoints
  name: SnackMagic Automation management API
  slug: snackmagic-automation-management-api
- baseURL: https://api.bystadium.com/api/v2
  baseurl_source: declared
  description: Order related API endpoints
  name: SnackMagic Order management API
  slug: snackmagic-order-management-api
- baseURL: https://api.bystadium.com/api/v2
  baseurl_source: declared
  description: Store related API endpoints
  name: SnackMagic Store management API
  slug: snackmagic-store-management-api
- baseURL: https://api.bystadium.com/api/v2
  baseurl_source: declared
  description: User related API endpoints
  name: SnackMagic User management API
  slug: snackmagic-user-management-api
artifact_total: 20
collections:
- collection_type: open
  name: Stadium Authentication API
  slug: open-snackmagic-authentication-api
- collection_type: open
  name: Stadium Authentication Automation management API
  slug: open-snackmagic-automation-management-api
- collection_type: open
  name: Stadium Authentication Order management API
  slug: open-snackmagic-order-management-api
- collection_type: open
  name: Stadium Authentication Store management API
  slug: open-snackmagic-store-management-api
- collection_type: open
  name: Stadium Authentication User management API
  slug: open-snackmagic-user-management-api
common:
- group: commercial
  href: https://artifacts.apis.io/snackmagic/plans/snackmagic-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/snackmagic-plans-pricing.yml
- group: company
  title: ''
  type: Blog
  url: https://www.snackmagic.com:443/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.snackmagic.com/blog/feed/
- group: other
  href: https://artifacts.apis.io/snackmagic/capabilities/snackmagic-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/snackmagic-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/snackmagic/mcp/snackmagic-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/snackmagic-mcp.yml
- group: other
  href: https://artifacts.apis.io/snackmagic/overlays/snackmagic-stadium-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/snackmagic-stadium-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://snackmagic.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.bystadium.com/api-integrations
- group: docs
  title: ''
  type: Documentation
  url: https://api.bystadium.com/api/v2/docs
- group: docs
  title: ''
  type: APIReference
  url: https://api.bystadium.com/api/v2/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://www.bystadium.com/api-integrations
- group: auth
  href: https://artifacts.apis.io/snackmagic/authentication/snackmagic-authentication.yml
  title: ''
  type: Authentication
  url: authentication/snackmagic-authentication.yml
- group: agent
  href: https://artifacts.apis.io/snackmagic/agentic-access/snackmagic-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/snackmagic-agentic-access.yml
- group: agent
  href: https://artifacts.apis.io/snackmagic/llms/snackmagic-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/snackmagic-llms.txt
- group: auth
  href: https://artifacts.apis.io/snackmagic/security/snackmagic-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/snackmagic-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.bystadium.com
- group: operate
  title: ''
  type: StatusPage
  url: https://status.bystadium.com
- group: agent
  href: https://artifacts.apis.io/snackmagic/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://www.bystadium.com/go/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.bystadium.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bystadium.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bystadium.com/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://www.bystadium.com/blog
- group: operate
  title: ''
  type: Support
  url: https://help.bystadium.com/hc
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/snackmagic
- group: other
  title: ''
  type: Wallet
  url: https://www.bystadium.com/wallet
created: '2026-07-17'
description: SnackMagic is a 100% customizable snack-box gifting service, now part of Stadium, that lets recipients build their own box from 500+ snacks and beverages or receive curated gifts, delivered worldwide. Companies use it for employee, client, prospect, and event gifting. SnackMagic is exposed to developers through the Stadium API (api.bystadium.com), a JSON REST API for embedding a global gift, rewards, and branded-swag catalog, placing orders funded by a pre-purchased Wallet balance, sending Stadium Shop points via treat links, and triggering webhook-automation gift orders. This profile was enriched from the provider's public OpenAPI and developer surface.
finops:
- has_sources: true
  method: derived
  name: Snackmagic Finops
  primary_unit: ''
  service_category: ''
  slug: snackmagic-finops
  template: true
image: https://fecdn.snackmagic.com/static/media/snackmagic-logo.b9e03ebf.svg
layout: provider
modified: '2026-10-06'
name: SnackMagic
nav: Providers
network: true
overview: 'SnackMagic publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Authentication API, Automation management API, Order management API, and 2 more. Tagged areas include Company, Consumer, Gifting, Rewards, and Swag.


  The SnackMagic catalog on APIs.io includes 1 Spectral governance ruleset.


  SnackMagic''s developer surface includes engineering blog, documentation, API reference, getting-started guide, authentication, pricing, signup flow, and 19 more developer resources.'
plans:
- name: Snackmagic Plans Pricing
  plan_count: 5
  slug: snackmagic-plans-pricing
random_paper: 9
rules:
- authorship: generated
  effective_rule_count: 107
  extends:
  - spectral:oas
  name: SnackMagic API Rules
  rule_count: 66
  severity_counts:
    error: 64
    hint: 0
    info: 1
    warn: 1
  slug: snackmagic-rules
score:
  band: strong
  composite: 54.6
  coverage:
    artifact_dirs: 29
    catalog_earned: 53.5
    catalog_earned_first_party: 12.0
    catalog_gap: 61.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.4
  facets:
    access_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 58.3
    developer_ergonomics: 66.1
    discoverability: 73.2
    operational_transparency: 10.5
  previous_composite: 53.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 5
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/snackmagic/snackmagic-2026-08-17T081940.png
security:
- kind: authentication
  name: Snackmagic Authentication
  slug: snackmagic-authentication
  summary_line: http/apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Snackmagic Domain Security
  slug: snackmagic-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Snackmagic Trust Center
  slug: snackmagic-trust-center
  summary_line: trust center published
skill_count: 3
skills:
- name: Trigger a webhook-automation gift order
  slug: snackmagic-automation-gifting
- name: Browse a store catalog and place an order
  slug: snackmagic-place-order
- name: Send Stadium Shop points to a recipient
  slug: snackmagic-send-points
slug: snackmagic
tags:
- Company
- Consumer
- Gifting
- Rewards
- Swag
- Snacks
- E-Commerce
- Fulfillment
website: https://snackmagic.com
---
