---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: unknown
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Patreon Agentic Access
  operation_count: 16
  slug: patreon-agentic-access
  summary_line: 16 operations · 6 acting
api_count: 1
apis:
- description: 'The Patreon REST API v2 follows the JSON:API specification. It exposes campaigns, members (patrons), posts, tiers, benefits, addresses, and webhooks. Authentication uses OAuth 2.0 with creator-issued '
  name: Patreon API v2
  slug: patreon-api-v2
- baseURL: https://www.patreon.com/api/oauth2/v2
  baseurl_source: declared
  description: The Oauth2 API from Patreon — 13 operation(s) for oauth2.
  name: Patreon Oauth2 API
  slug: patreon-oauth2-api
artifact_total: 12
collections:
- collection_type: open
  name: Patreon API v2 Oauth2 API
  slug: open-patreon-oauth2-api
- collection_type: open
  name: Patreon API v2
  slug: open-patreon
common:
- group: agent
  href: https://artifacts.apis.io/patreon/agentic-access/patreon-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/patreon-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/patreon/security/patreon-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/patreon-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/patreon/security/patreon-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/patreon-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/patreon/authentication/patreon-authentication.yml
  title: ''
  type: Authentication
  url: authentication/patreon-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Patreon
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/patreon
- group: company
  title: ''
  type: Website
  url: https://www.patreon.com/
- group: start
  title: ''
  type: Portal
  url: https://docs.patreon.com/
- group: start
  title: ''
  type: Signup
  url: https://www.patreon.com/portal/registration/register-clients
- group: operate
  title: ''
  type: Forums
  url: https://www.patreondevelopers.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.patreon.com/pricing
- group: commercial
  href: https://artifacts.apis.io/patreon/plans/patreon-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/patreon-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/patreon/rate-limits/patreon-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/patreon-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/patreon/finops/patreon-finops.yml
  title: ''
  type: FinOps
  url: finops/patreon-finops.yml
created: '2026-05-08'
description: Patreon is a membership platform for creators offering tiered subscriptions, content publishing, community, and payments. The Patreon API v2 follows the JSON:API specification and exposes campaigns, members, posts, tiers, benefits, and webhooks via OAuth 2.0.
finops:
- has_sources: true
  method: generated
  name: Patreon Finops
  primary_unit: ''
  service_category: Creator Economy
  slug: patreon-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/patreon.png
layout: provider
modified: '2026-05-08'
name: Patreon
nav: Providers
network: true
overview: 'Patreon publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including Oauth2 API, and 1 more. Tagged areas include Creator Economy, Membership, Subscription, Content, and Community.


  The Patreon catalog on APIs.io includes 1 Spectral governance ruleset.


  Patreon''s developer surface includes authentication, developer portal, signup flow, pricing, and 10 more developer resources.'
plans:
- name: Patreon Plans Pricing
  plan_count: 1
  slug: patreon-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 3
  name: Patreon Rate Limits
  slug: patreon-rate-limits
rules:
- authorship: generated
  effective_rule_count: 89
  extends:
  - spectral:oas
  name: Patreon API Rules
  rule_count: 48
  severity_counts:
    error: 46
    hint: 0
    info: 1
    warn: 1
  slug: patreon-rules
score:
  band: thin
  composite: 34.2
  coverage:
    artifact_dirs: 15
    catalog_earned: 46.5
    catalog_earned_first_party: 0.0
    catalog_gap: 68.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    contract_governance: 13.6
    contract_quality: 45.2
    developer_ergonomics: 29.8
    discoverability: 66.1
    operational_transparency: 25.0
  previous_composite: 34.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 17.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/patreon/patreon-2026-06-20T191442.png
security:
- kind: authentication
  name: Patreon Authentication
  slug: patreon-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Patreon Domain Security
  slug: patreon-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Patreon Vulnerability Disclosure
  slug: patreon-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: patreon
tags:
- Creator Economy
- Membership
- Subscription
- Content
- Community
website: https://www.patreon.com/
---
