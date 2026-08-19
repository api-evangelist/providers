---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
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
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: na
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.5
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Lobsters Agentic Access
  operation_count: 8
  slug: lobsters-agentic-access
  summary_line: 8 operations
api_count: 4
apis:
- description: Community discussion comments on stories
  name: Lobsters Comments API
  slug: lobsters-comments-api
- description: Technology link aggregation stories submitted by the community
  name: Lobsters Stories API
  slug: lobsters-stories-api
- description: Community-maintained taxonomy tags for categorizing stories
  name: Lobsters Tags API
  slug: lobsters-tags-api
- description: Lobsters user profiles
  name: Lobsters Users API
  slug: lobsters-users-api
artifact_total: 25
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Lobsters Comments API
  slug: open-lobsters-comments-api
- collection_type: open
  name: Lobsters Comments Stories API
  slug: open-lobsters-stories-api
- collection_type: open
  name: Lobsters Comments Tags API
  slug: open-lobsters-tags-api
- collection_type: open
  name: Lobsters Comments Users API
  slug: open-lobsters-users-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/lobsters/lobsters/issues
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/lobsters/lobsters/blob/main/SECURITY.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/lobsters/lobsters/blob/main/CONTRIBUTING.md
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/lobsters-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/lobsters-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lobsters-domain-security.yml
- group: build
  title: ''
  type: GitHub
  url: https://github.com/lobsters/lobsters
- group: company
  title: ''
  type: About
  url: https://lobste.rs/about
- group: other
  title: ''
  type: Tags
  url: https://lobste.rs/tags
- group: other
  title: ''
  type: RSS
  url: https://lobste.rs/rss
created: '2026-06-13'
description: Lobsters is a technology-focused link aggregation and community discussion platform. Its public REST API provides access to stories, comments, tags, and user profiles, returning JSON representations of community-submitted technology links, ranked and filtered by the community.
examples:
- key_count: 14
  name: Comment
  slug: comment
- key_count: 12
  name: Story
  slug: story
- key_count: 8
  name: Tag
  slug: tag
- key_count: 10
  name: User
  slug: user
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lobsters.png
json_schemas:
- name: Comment
  property_count: 14
  slug: comment
- name: Story
  property_count: 12
  slug: story
- name: Tag
  property_count: 8
  slug: tag
- name: User
  property_count: 11
  slug: user
jsonld:
- class_count: 23
  name: Lobsters Context
  property_count: 0
  slug: lobsters
layout: provider
modified: '2026-06-13'
name: Lobsters
nav: Providers
network: true
overview: 'Lobsters publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Comments API, Stories API, Tags API, and 1 more. Tagged areas include Link Aggregation, Community, Technology, News, and Stories.


  The Lobsters catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Lobsters'' developer surface includes GitHub presence and 9 more developer resources.'
plans:
- name: Plans
  plan_count: 1
  slug: plans
random_paper: 133
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Lobsters API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: lobsters-jsonschema-spectral-rules
score:
  band: thin
  composite: 30.9
  delta: -6.8
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 9.8
    contract_quality: 58.0
    developer_ergonomics: 0.0
    discoverability: 74.1
    governance: 9.8
    operational_transparency: 15.8
  previous_composite: 37.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/lobsters/refs/heads/main/screenshots/lobsters-2026-06-20T184628.png
security:
- kind: domain-security
  name: Lobsters Domain Security
  slug: lobsters-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Lobsters Vulnerability Disclosure
  slug: lobsters-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: lobsters
tags:
- Link Aggregation
- Community
- Technology
- News
- Stories
- Comments
- Tags
---
