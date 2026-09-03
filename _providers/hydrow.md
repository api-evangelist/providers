---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - rate-limits
  - security
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.4
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://hydrow.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.hydrow.com/
- group: operate
  title: ''
  type: Support
  url: https://support.hydrow.com/s/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/TrueRowing
- group: commercial
  title: ''
  type: Pricing
  url: https://support.hydrow.com/s/article/Hydrow-membership-pricing-1651497389211
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/hydrow-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/hydrow-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hydrow-llms.txt
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/hydrow-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/hydrow-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/hydrow-plans-pricing.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hydrow-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/hydrow-conformance.yml
coverage:
  checked: '2026-08-22'
  detail: 'Hydrow ships software only as an end-user product: contract discovery reached its two real production backends and found nothing published on either — every OpenAPI, Swagger, GraphQL, /.well-known/ and agent-card path on v2.api.prod.hydrow-external.net returns a genuine JSON 404 matching the control path, while v1.api.prod.hydrow-external.net answers a blanket 401 — and its developer-shaped hostnames (api./developer./docs.hydrow.com) exist only as a Vercel wildcard DNS record that never completes a TLS handshake.'
  evidence:
  - status: 404
    url: https://v2.api.prod.hydrow-external.net/openapi.json
  - status: 404
    url: https://v2.api.prod.hydrow-external.net/.well-known/agent-card.json
  - status: 401
    url: https://v1.api.prod.hydrow-external.net/api-docs
  - status: 429
    url: https://hydrow.com/llms.txt
  - status: 404
    url: https://registry.npmjs.org/hydrow
  - status: 200
    url: https://github.com/TrueRowing
  - status: 200
    url: https://status.hydrow.com/api/v2/summary.json
  reason: no-developer-program
  state: none
created: '2026-08-22'
description: Hydrow (legally True Rowing, Inc., Boston, Massachusetts) is a connected-fitness hardware company that makes the Hydrow indoor rowing machine and the LYQUID strength-training platform, sold with a subscription to a library of live and on-demand athlete-led workouts filmed on real water. Members interact with Hydrow through its rower touchscreens and the Hydrow iOS/Android companion apps, which sync workout summaries outward to Strava and Apple Health. Hydrow operates a real production backend for those apps, but publishes no public developer program, no API reference, no OpenAPI or other machine-readable contract, and no first-party SDK in any package registry; its developer-facing subdomains do not resolve to a service. Its public machine-readable surface is limited to an Atlassian Statuspage.
image: https://avatars.githubusercontent.com/u/34552552?v=4
layout: provider
modified: '2026-08-22'
name: Hydrow
nav: Providers
network: true
overview: 'Hydrow is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Connected Fitness, Consumer Hardware, Rowing, and Fitness.


  Hydrow''s developer surface includes support, pricing, and 11 more developer resources.'
plans:
- name: Hydrow Plans Pricing
  plan_count: 0
  slug: hydrow-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Hydrow Rate Limits
  slug: hydrow-rate-limits
score:
  band: minimal
  composite: 8.2
  coverage:
    artifact_dirs: 11
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 5.3
    commercial_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 18.4
  previous_composite: 8.2
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 13.8
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hydrow/refs/heads/main/screenshots/hydrow-2026-09-02T145814.png
security:
- kind: domain-security
  name: Hydrow Domain Security
  slug: hydrow-domain-security
  summary_line: TLSv1.3 · DMARC
slug: hydrow
tags:
- Company
- Connected Fitness
- Consumer Hardware
- Rowing
- Fitness
- Wellness
- Health
- Streaming Media
- Subscription
- Internet of Things
website: https://hydrow.com/
---
