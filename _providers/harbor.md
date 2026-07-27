---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Harbor Agentic Access
  operation_count: 13
  slug: harbor-agentic-access
  summary_line: 13 operations · 6 acting
api_count: 6
apis:
- description: Operations for managing challenges that members complete to earn points and rewards.
  name: Harbor Challenges API
  slug: harbor-challenges-api
- description: Operations for managing community configuration and settings.
  name: Harbor Communities API
  slug: harbor-communities-api
- description: Operations for retrieving leaderboard rankings of community members by points or other engagement metrics.
  name: Harbor Leaderboards API
  slug: harbor-leaderboards-api
- description: Operations for managing community members, their profiles, point balances, and tier status.
  name: Harbor Members API
  slug: harbor-members-api
- description: Operations for managing reward redemption requests from members.
  name: Harbor Redemptions API
  slug: harbor-redemptions-api
- description: Operations for managing the rewards catalog that members can redeem with earned points.
  name: Harbor Rewards API
  slug: harbor-rewards-api
artifact_total: 17
collections:
- collection_type: open
  name: Harbor API
  slug: open-harbor
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/harbor-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/harbor-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/harbor-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/goharbor
- group: company
  title: ''
  type: Website
  url: https://www.harbor.gg/
- group: docs
  title: ''
  type: Documentation
  url: https://api.harbor.gg/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.harbor.gg/privacy-policy
- group: design
  title: ''
  type: JSONLD
  url: json-ld/harbor-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/harbor-member-schema.json
created: '2025-02-17'
description: Harbor is a no-code tool that lets brands build an owned community platform where superfans can engage with the brand and earn rewards. Harbor enables businesses to create superfan strategies through customizable community platforms with engagement and loyalty features.
finops:
- name: Harbor Finops
  service_category: API
  slug: harbor-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/harbor.png
json_schemas:
- name: Harbor Account
  property_count: 9
  slug: harbor-account
- name: Harbor Community Member
  property_count: 13
  slug: harbor-member
jsonld:
- class_count: 0
  name: Harbor Context
  property_count: 8
  slug: harbor-context
layout: provider
modified: '2026-05-19'
name: Harbor
nav: Providers
network: true
overview: 'Harbor publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Challenges API, Communities API, Leaderboards API, and 3 more. Tagged areas include Community, Engagement, Loyalty, and Superfans.


  The Harbor catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Harbor''s developer surface includes authentication, documentation, and 7 more developer resources.'
plans:
- name: Harbor Plans Pricing
  plan_count: 3
  slug: harbor-plans-pricing
random_paper: 26
rate_limits:
- limit_count: 5
  name: Harbor Rate Limits
  slug: harbor-rate-limits
rules:
- name: Harbor API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: harbor-jsonschema-spectral-rules
score:
  band: developing
  composite: 53.4
  delta: 4.2
  facets:
    commercial_clarity: 50.0
    contract_quality: 73.5
    developer_ergonomics: 19.6
    discoverability: 75.0
    governance: 73.7
    operational_transparency: 36.8
  previous_composite: 49.2
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/harbor/refs/heads/main/screenshots/harbor-2026-06-20T182512.png
security:
- kind: authentication
  name: Harbor Authentication
  slug: harbor-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Harbor Domain Security
  slug: harbor-domain-security
  summary_line: TLSv1.3
slug: harbor
tags:
- Community
- Engagement
- Loyalty
- Superfans
website: https://www.harbor.gg/
---
