---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.3
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Kit Agentic Access
  operation_count: 9
  slug: kit-agentic-access
  summary_line: 9 operations · 3 acting
api_count: 4
apis:
- description: The legacy ConvertKit V3 API is deprecated and slated for discontinuation; new integrations should target V4.
  name: Kit API V3 (Deprecated)
  slug: kit-api-v3
- description: Account, creator profile, and account-level statistics
  name: Kit Account API
  slug: kit-account-api
- description: One-off email broadcasts
  name: Kit Broadcasts API
  slug: kit-broadcasts-api
- description: Subscriber records and lifecycle
  name: Kit Subscribers API
  slug: kit-subscribers-api
artifact_total: 20
asyncapis:
- description: AsyncAPI 2.6 description of the Kit (formerly ConvertKit) webhook surface. Kit delivers webhook notifications via HTTP `POST` requests with a JSON body to a `target_url` registered through the Kit API
  name: Kit Webhooks
  slug: kit-webhooks-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Kit API V4 Account API
  slug: open-kit-account-api
- collection_type: open
  name: Kit API V4 Account Broadcasts API
  slug: open-kit-broadcasts-api
- collection_type: open
  name: Kit API V4 Account Subscribers API
  slug: open-kit-subscribers-api
- collection_type: open
  name: Kit API V4
  slug: open-kit
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/kit-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/kit-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/kit-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kit-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/kit-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/kit-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kit
- group: company
  title: ''
  type: Website
  url: https://kit.com/
- group: start
  title: ''
  type: Portal
  url: https://developers.kit.com/
- group: start
  title: ''
  type: Signup
  url: https://app.kit.com/users/signup
- group: commercial
  title: ''
  type: Pricing
  url: https://kit.com/pricing
- group: commercial
  title: ''
  type: Plans
  url: plans/kit-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/kit-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/kit-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://kit.com/resources/blog
created: '2026-05-08'
description: Kit (formerly ConvertKit) is an email marketing and creator platform. The Kit API V4 exposes subscribers, broadcasts, sequences, tags, custom fields, forms, purchases, and webhooks. V3 is deprecated.
finops:
- name: Kit Finops
  service_category: Email Marketing
  slug: kit-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kit.png
layout: provider
modified: '2026-05-30'
name: Kit
nav: Providers
network: true
overview: 'Kit publishes 3 APIs on the [APIs.io](https://apis.io/) network: Account API, Broadcasts API, and Subscribers API. Tagged areas include Email Marketing, Creator Economy, Newsletters, Automation, and Subscribers.


  The Kit catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Kit''s developer surface includes authentication, developer portal, signup flow, pricing, engineering blog, and 10 more developer resources.'
plans:
- name: Kit Plans Pricing
  plan_count: 3
  slug: kit-plans-pricing
random_paper: 30
rate_limits:
- limit_count: 1
  name: Kit Rate Limits
  slug: kit-rate-limits
rules:
- effective_rule_count: 34
  extends:
  - spectral:asyncapi
  name: Kit API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 6
  slug: kit-asyncapi-spectral-rules
scopes:
- name: Kit Scopes
  scope_count: 1
  slug: kit-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: developing
  composite: 43.6
  delta: -2.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 11.4
    contract_quality: 66.4
    developer_ergonomics: 23.8
    discoverability: 64.8
    governance: 11.4
    operational_transparency: 7.9
  previous_composite: 45.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 55.6
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kit/refs/heads/main/screenshots/kit-2026-06-20T184050.png
security:
- kind: authentication
  name: Kit Authentication
  slug: kit-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Kit Domain Security
  slug: kit-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Kit Vulnerability Disclosure
  slug: kit-vulnerability-disclosure
  summary_line: Bugcrowd
- kind: trust-center
  name: Kit Trust Center
  slug: kit-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27018, GDPR
slug: kit
tags:
- Email Marketing
- Creator Economy
- Newsletters
- Automation
- Subscribers
website: https://kit.com/
---
