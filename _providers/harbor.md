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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-19'
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
artifact_total: 24
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Harbor Challenges API
  slug: open-harbor-challenges-api
- collection_type: open
  name: Harbor Challenges Communities API
  slug: open-harbor-communities-api
- collection_type: open
  name: Harbor Challenges Leaderboards API
  slug: open-harbor-leaderboards-api
- collection_type: open
  name: Harbor Challenges Members API
  slug: open-harbor-members-api
- collection_type: open
  name: Harbor Challenges Redemptions API
  slug: open-harbor-redemptions-api
- collection_type: open
  name: Harbor Challenges Rewards API
  slug: open-harbor-rewards-api
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
random_paper: 8
rate_limits:
- limit_count: 5
  name: Harbor Rate Limits
  slug: harbor-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Harbor API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: harbor-jsonschema-spectral-rules
score:
  band: thin
  composite: 35.1
  delta: -6.8
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 9.8
    contract_quality: 69.9
    developer_ergonomics: 21.4
    discoverability: 55.6
    governance: 9.8
    operational_transparency: 10.5
  previous_composite: 41.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
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
