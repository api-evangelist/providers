---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-09-20'
api_count: 0
artifact_total: 3
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/affinity3/refs/heads/main/security/affinity3-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/affinity3-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.fromthelobby.com/
- group: operate
  title: ''
  type: Support
  url: https://www.fromthelobby.com/support
- group: start
  title: ''
  type: SignUp
  url: https://www.fromthelobby.com/creator-application/new
- group: start
  title: ''
  type: Login
  url: https://www.fromthelobby.com/users/sign_in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.fromthelobby.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.fromthelobby.com/privacy
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/affinity3/refs/heads/main/plans/affinity3-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/affinity3-plans-pricing.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/affinity3/refs/heads/main/llms/affinity3-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/affinity3-llms.txt
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/affinity3/refs/heads/main/rate-limits/affinity3-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/affinity3-rate-limits.yml
coverage:
  checked: '2026-09-12'
  detail: Affinity Technology, Inc. ships The Lobby only as an end-user SaaS for brands and creators — there is no developer portal, API reference or api.* host on either fromthelobby.com or tryaffinity.com, and its one advertised integration is a Shopify connection configured inside the authenticated brand dashboard rather than a documented API a third party can call.
  evidence:
  - status: 404
    url: https://www.fromthelobby.com/developers
  - status: 404
    url: https://www.fromthelobby.com/api
  - status: 404
    url: https://tryaffinity.com/openapi.json
  - status: 404
    url: https://www.fromthelobby.com/.well-known/api-catalog
  - status: 200
    url: https://www.fromthelobby.com/
  reason: no-developer-program
  state: none
created: '2026-09-12'
description: 'Affinity Technology, Inc. operates The Lobby (fromthelobby.com; app at tryaffinity.com), an invite-only creator-marketing marketplace connecting direct-to-consumer brands with content creators for product seeding, paid partnerships and user-generated content. Brands stock a Creator Closet that vetted creators request from, and the platform handles standardized one-click partnership offers, contracts, Shopify-driven fulfilment and shipment tracking, deliverable reminders, a content library and social-listening reporting. The company began as Affinity, an AI personalized-fashion recommendation service for brands and retailers (San Francisco, backed by 8VC, EquityZen ticker AFFI) and pivoted the same entity and domain to the creator-marketing product. It publishes NO developer program: no portal, no API reference, no OpenAPI/GraphQL/MCP surface, no api.* host, no public code org. Its only advertised integration is a Shopify connection configured inside the authenticated brand
  dashboard.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/affinity3.png
layout: provider
modified: '2026-09-12'
name: Affinity Technology (The Lobby)
nav: Providers
network: true
overview: 'Affinity Technology (The Lobby) is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Influencer Marketing, Creator Economy, User Generated Content, and Marketing.


  Affinity Technology (The Lobby)''s developer surface includes support, signup flow, and 8 more developer resources.'
plans:
- name: Affinity3 Plans Pricing
  plan_count: 0
  slug: affinity3-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Affinity3 Rate Limits
  slug: affinity3-rate-limits
score:
  band: emerging
  composite: 12.8
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
    operational_transparency: 0.0
  previous_composite: 12.8
  schema_version: 0.22.0
  scored_at: '2026-09-20'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Affinity3 Domain Security
  slug: affinity3-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: affinity3
tags:
- Company
- Influencer Marketing
- Creator Economy
- User Generated Content
- Marketing
- E-Commerce
- Social-Media
- Shopify
- Direct to Consumer
website: https://www.fromthelobby.com/
---
