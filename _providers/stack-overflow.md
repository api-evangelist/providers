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
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Stack Overflow Agentic Access
  operation_count: 37
  slug: stack-overflow-agentic-access
  summary_line: 37 operations · 8 acting
api_count: 10
apis:
- description: Operations for managing answers to questions in a Teams workspace.
  name: Stack Overflow Answers API
  slug: stack-overflow-answers-api
- description: Operations for managing knowledge articles in a Teams workspace.
  name: Stack Overflow Articles API
  slug: stack-overflow-articles-api
- description: Operations for retrieving badge information on Stack Overflow.
  name: Stack Overflow Badges API
  slug: stack-overflow-badges-api
- description: Operations for retrieving and writing comments on Stack Overflow posts.
  name: Stack Overflow Comments API
  slug: stack-overflow-comments-api
- description: Operations for managing questions in a Stack Overflow for Teams workspace.
  name: Stack Overflow Questions API
  slug: stack-overflow-questions-api
- description: Operations for searching Stack Overflow questions and content.
  name: Stack Overflow Search API
  slug: stack-overflow-search-api
- description: Operations for managing Subject Matter Experts (SMEs) for tags in a Teams workspace.
  name: Stack Overflow SMEs API
  slug: stack-overflow-smes-api
- description: Operations for managing tags in a Teams workspace.
  name: Stack Overflow Tags API
  slug: stack-overflow-tags-api
- description: Operations for managing user groups in a Teams workspace.
  name: Stack Overflow User Groups API
  slug: stack-overflow-user-groups-api
- description: Operations for managing users in a Teams workspace.
  name: Stack Overflow Users API
  slug: stack-overflow-users-api
artifact_total: 36
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Stack Overflow for Teams Answers API
  slug: open-stack-overflow-answers-api
- collection_type: open
  name: Stack Overflow for Teams Answers Articles API
  slug: open-stack-overflow-articles-api
- collection_type: open
  name: Stack Overflow for Teams Answers Badges API
  slug: open-stack-overflow-badges-api
- collection_type: open
  name: Stack Overflow for Teams Answers Comments API
  slug: open-stack-overflow-comments-api
- collection_type: open
  name: Stack Overflow for Teams API
  slug: open-stack-overflow-for-teams
- collection_type: open
  name: Stack Overflow for Teams Answers Questions API
  slug: open-stack-overflow-questions-api
- collection_type: open
  name: Stack Overflow for Teams Answers Search API
  slug: open-stack-overflow-search-api
- collection_type: open
  name: Stack Overflow for Teams Answers SMEs API
  slug: open-stack-overflow-smes-api
- collection_type: open
  name: Stack Overflow for Teams Answers Tags API
  slug: open-stack-overflow-tags-api
- collection_type: open
  name: Stack Overflow for Teams Answers User Groups API
  slug: open-stack-overflow-user-groups-api
- collection_type: open
  name: Stack Overflow for Teams Answers Users API
  slug: open-stack-overflow-users-api
- collection_type: open
  name: Stack Overflow API
  slug: open-stack-overflow
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/stack-overflow-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/stack-overflow-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/stack-overflow-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/stack-overflow-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/stackexchange
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/stack-overflow
- group: company
  title: ''
  type: Website
  url: https://stackoverflow.com
- group: company
  title: ''
  type: Blog
  url: https://stackoverflow.blog/
- group: auth
  title: ''
  type: Authentication
  url: https://api.stackexchange.com/docs/authentication
- group: start
  title: ''
  type: Signup
  url: http://stackapps.com/apps/oauth/register
- group: commercial
  title: ''
  type: TermsOfService
  url: https://stackexchange.com/legal/api-terms-of-use
- group: design
  title: ''
  type: JSONLD
  url: json-ld/stack-overflow-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/stack-overflow-question-schema.json
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/stack-overflow-vocabulary.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/stack-overflow-rules.yml
created: '2026-05-02'
description: 'Stack Overflow is the world''s largest question-and-answer community for developers, with over 23 million questions on programming, software development, and technology topics. Stack Overflow offers two API products: the public Stack Exchange API v2.3 for read/write access to Stack Overflow questions, answers, comments, users, tags, and badges; and the Stack Overflow for Teams API v3, a private team knowledge-base API with endpoints for questions, answers, articles, user groups, and SME management.'
examples:
- key_count: 4
  name: Stack Overflow Get Questions Example
  slug: stack-overflow-get-questions-example
finops:
- name: Stack Overflow Finops
  service_category: API
  slug: stack-overflow-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/stack-overflow.png
json_schemas:
- name: Stack Overflow Question
  property_count: 14
  slug: stack-overflow-question
json_structures:
- name: Stack Overflow Question Structure
  property_count: 14
  slug: stack-overflow-question-structure
jsonld:
- class_count: 27
  name: Stack Overflow Context
  property_count: 4
  slug: stack-overflow-context
layout: provider
modified: '2026-05-19'
name: Stack Overflow
nav: Providers
network: true
overview: 'Stack Overflow publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Answers API, Articles API, Badges API, and 7 more. Tagged areas include Answers, Code, Developer Community, Developer Tools, and Knowledge Base.


  The Stack Overflow catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Stack Overflow''s developer surface includes authentication, engineering blog, signup flow, and 12 more developer resources.'
plans:
- name: Stack Overflow Plans Pricing
  plan_count: 3
  slug: stack-overflow-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 5
  name: Stack Overflow Rate Limits
  slug: stack-overflow-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Stack Overflow API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: stack-overflow-jsonschema-spectral-rules
- effective_rule_count: 50
  extends:
  - spectral:oas
  name: Stack Overflow API Rules
  rule_count: 9
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 6
  slug: stack-overflow-rules
scopes:
- name: Stack Overflow Scopes
  scope_count: 3
  slug: stack-overflow-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: thin
  composite: 37.9
  delta: -6.1
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 25.0
    contract_quality: 63.7
    developer_ergonomics: 14.3
    discoverability: 68.5
    governance: 25.0
    operational_transparency: 10.5
  previous_composite: 44.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/stack-overflow/refs/heads/main/screenshots/stack-overflow-2026-06-20T194441.png
security:
- kind: authentication
  name: Stack Overflow Authentication
  slug: stack-overflow-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Stack Overflow Domain Security
  slug: stack-overflow-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: stack-overflow
tags:
- Answers
- Code
- Developer Community
- Developer Tools
- Knowledge Base
- Programming
- Q&A
- Questions
- Stack Overflow
website: https://stackoverflow.com
---
