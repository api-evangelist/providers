---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 15.5
  scored_at: '2026-08-30'
api_count: 5
apis:
- description: Query members and their profiles, emails, subscriptions, downloads, and custom JSON metadata (up to 50 keys), and create, update, or delete members through GraphQL mutations. Cursor-based pagination (
  name: Memberful Members API
  slug: memberful-members-api
- description: Read and manage member subscriptions - the link between a member and the pass/plan they pay for - including status, current period, trial state, activation and expiration, and the associated plan pric
  name: Memberful Subscriptions API
  slug: memberful-subscriptions-api
- description: Query the passes members subscribe to (called "Plans" in the dashboard) and the plans (pricing options such as monthly or annual) within each pass, including price, interval, and label. Coupons that d
  name: Memberful Plans and Passes API
  slug: memberful-plans-api
- description: Query orders (transaction records) for a member or account, including totals, status, coupons applied, and the member and plan involved. Orders back the order.purchased, order.completed, order.refunde
  name: Memberful Orders API
  slug: memberful-orders-api
- description: OAuth 2.0 Authorization Code flow (with PKCE) for signing members into external apps. Authorize at /oauth, exchange the code at /oauth/token, then query the signed-in member at /api/graphql/member. Ac
  name: Memberful OAuth SSO API
  slug: memberful-oauth-sso-api
artifact_total: 12
collections:
- collection_type: open
  name: Memberful GraphQL API
  slug: open-memberful
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/memberful-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/memberful-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/memberful
- group: company
  title: ''
  type: Website
  url: https://memberful.com
- group: docs
  title: ''
  type: Documentation
  url: https://memberful.com/help/custom-development-and-api/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/memberful
- group: commercial
  title: ''
  type: Plans
  url: plans/memberful-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/memberful-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/memberful-finops.yml
created: '2026-07-05'
description: Memberful is a membership and subscription platform (owned by Patreon) that lets independent publishers, educators, and creators sell memberships, subscriptions, digital downloads, podcasts, and courses on their own site while Memberful handles checkout, recurring billing (via Stripe), and member management. Its public developer surface is a GraphQL API served per account at https://ACCOUNT.memberful.com/api/graphql, authenticated with an API key (bearer token) or OAuth 2.0 access token, covering Members, Subscriptions, Plans/Passes, Coupons, and Orders through queries and mutations. Memberful also provides OAuth 2.0 single sign-on for apps and HMAC-signed webhooks for member, subscription, plan, order, and download events.
finops:
- name: Memberful Finops
  service_category: Membership and Subscription Commerce
  slug: memberful-finops
graphqls:
- description: Memberful (a Patreon-owned membership and subscription platform) exposes a **native GraphQL API** - this is a real, documented GraphQL surface, not a REST-to-GraphQL projection.
  name: Memberful GraphQL API
  slug: memberful-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/memberful.png
layout: provider
modified: '2026-07-05'
name: Memberful
nav: Providers
network: true
overview: 'Memberful publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Members API, Subscriptions API, Plans and Passes API, and 1 more. Tagged areas include Memberships, Subscription, Payments, Creators, and GraphQL.


  Memberful''s developer surface includes documentation and 8 more developer resources.'
plans:
- name: Memberful Plans Pricing
  plan_count: 3
  slug: memberful-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 4
  name: Memberful Rate Limits
  slug: memberful-rate-limits
score:
  band: thin
  composite: 29.4
  coverage:
    artifact_dirs: 7
    catalog_gap: 48.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 37.2
    developer_ergonomics: 11.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 29.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 18.8
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/memberful/refs/heads/main/screenshots/memberful-2026-08-07T172455.png
security:
- kind: domain-security
  name: Memberful Domain Security
  slug: memberful-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Memberful Vulnerability Disclosure
  slug: memberful-vulnerability-disclosure
  summary_line: disclosure policy published
slug: memberful
tags:
- Memberships
- Subscription
- Payments
- Creators
- GraphQL
- Patreon
website: https://memberful.com
---
