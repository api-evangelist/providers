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
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.7
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Stack Exchange Agentic Access
  operation_count: 24
  slug: stack-exchange-agentic-access
  summary_line: 24 operations
api_count: 1
apis:
- baseURL: https://api.stackexchange.com/2.3
  baseurl_source: declared
  description: Operations for retrieving and managing answers to questions on Stack Exchange sites.
  name: Stack Exchange Answers API
  slug: stack-exchange-answers-api
- baseURL: https://api.stackexchange.com/2.3
  baseurl_source: declared
  description: Operations for retrieving badge definitions and badge awards on Stack Exchange sites.
  name: Stack Exchange Badges API
  slug: stack-exchange-badges-api
- baseURL: https://api.stackexchange.com/2.3
  baseurl_source: declared
  description: Operations for retrieving and managing comments on questions and answers.
  name: Stack Exchange Comments API
  slug: stack-exchange-comments-api
- baseURL: https://api.stackexchange.com/2.3
  baseurl_source: declared
  description: Operations for retrieving, searching, and managing questions across the Stack Exchange network.
  name: Stack Exchange Questions API
  slug: stack-exchange-questions-api
- baseURL: https://api.stackexchange.com/2.3
  baseurl_source: declared
  description: Operations for searching questions and content across the Stack Exchange network.
  name: Stack Exchange Search API
  slug: stack-exchange-search-api
- baseURL: https://api.stackexchange.com/2.3
  baseurl_source: declared
  description: Operations for retrieving information about Stack Exchange network sites.
  name: Stack Exchange Sites API
  slug: stack-exchange-sites-api
- baseURL: https://api.stackexchange.com/2.3
  baseurl_source: declared
  description: Operations for retrieving and managing tags used to categorize questions.
  name: Stack Exchange Tags API
  slug: stack-exchange-tags-api
- baseURL: https://api.stackexchange.com/2.3
  baseurl_source: declared
  description: Operations for retrieving user profiles, activity, and reputation on Stack Exchange sites.
  name: Stack Exchange Users API
  slug: stack-exchange-users-api
artifact_total: 31
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Stack Exchange Answers API
  slug: open-stack-exchange-answers-api
- collection_type: open
  name: Stack Exchange Answers Badges API
  slug: open-stack-exchange-badges-api
- collection_type: open
  name: Stack Exchange Answers Comments API
  slug: open-stack-exchange-comments-api
- collection_type: open
  name: Stack Exchange Answers Questions API
  slug: open-stack-exchange-questions-api
- collection_type: open
  name: Stack Exchange Answers Search API
  slug: open-stack-exchange-search-api
- collection_type: open
  name: Stack Exchange Answers Sites API
  slug: open-stack-exchange-sites-api
- collection_type: open
  name: Stack Exchange Answers Tags API
  slug: open-stack-exchange-tags-api
- collection_type: open
  name: Stack Exchange Answers Users API
  slug: open-stack-exchange-users-api
- collection_type: open
  name: Stack Exchange API
  slug: open-stack-exchange
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/stack-exchange-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/stack-exchange-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/stack-exchange-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/stack-exchange-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/stack-exchange
- group: auth
  title: ''
  type: Authentication
  url: https://api.stackexchange.com/docs/authentication
- group: company
  title: ''
  type: Blog
  url: https://stackoverflow.blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://stackexchange.com/legal/api-terms-of-use
- group: operate
  title: ''
  type: RateLimits
  url: https://api.stackexchange.com/docs/throttle
- group: start
  title: ''
  type: Signup
  url: http://stackapps.com/apps/oauth/register
- group: other
  title: ''
  type: Applications
  url: http://stackapps.com/apps/oauth
- group: build
  title: ''
  type: GitHub Topics
  url: https://github.com/topics/stackexchange-api
- group: design
  title: ''
  type: JSONLD
  url: json-ld/stack-exchange-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/stack-exchange-question-schema.json
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/stack-exchange-vocabulary.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/stack-exchange-rules.yml
created: '2023-11-15'
description: Stack Exchange is a network of question-and-answer websites on topics in diverse fields, each site covering a specific topic, where questions, answers, and users are subject to a reputation award process. The network includes over 170 communities including Stack Overflow (programming), Server Fault (system administration), Super User (computing), and many others. The Stack Exchange API v2.3 provides programmatic access to questions, answers, comments, users, tags, badges, and search across all sites in the network.
examples:
- key_count: 7
  name: Stack Exchange Get Questions Example
  slug: stack-exchange-get-questions-example
finops:
- name: Stack Exchange Finops
  service_category: API
  slug: stack-exchange-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/stack-exchange.png
json_schemas:
- name: Stack Exchange Question
  property_count: 20
  slug: stack-exchange-question
json_structures:
- name: Stack Exchange Question Structure
  property_count: 14
  slug: stack-exchange-question-structure
jsonld:
- class_count: 32
  name: Stack Exchange Context
  property_count: 4
  slug: stack-exchange-context
layout: provider
modified: '2026-05-19'
name: Stack Exchange
nav: Providers
network: true
overview: 'Stack Exchange publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Answers API, Badges API, Comments API, and 5 more. Tagged areas include Answers, Code, Community, Developer Tools, and Knowledge Base.


  The Stack Exchange catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Stack Exchange''s developer surface includes authentication, engineering blog, signup flow, and 13 more developer resources.'
plans:
- name: Stack Exchange Plans Pricing
  plan_count: 3
  slug: stack-exchange-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 5
  name: Stack Exchange Rate Limits
  slug: stack-exchange-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Stack Exchange API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: stack-exchange-jsonschema-spectral-rules
- effective_rule_count: 50
  extends:
  - spectral:oas
  name: Stack Exchange API Rules
  rule_count: 9
  severity_counts:
    error: 2
    hint: 0
    info: 2
    warn: 5
  slug: stack-exchange-rules
scopes:
- name: Stack Exchange Scopes
  scope_count: 3
  slug: stack-exchange-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: thin
  composite: 38.8
  coverage:
    artifact_dirs: 17
    catalog_gap: 54.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 28.8
    contract_quality: 61.5
    developer_ergonomics: 23.8
    discoverability: 63.0
    governance: 28.8
    operational_transparency: 7.9
  previous_composite: 38.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/stack-exchange/refs/heads/main/screenshots/stack-exchange-2026-06-20T194440.png
security:
- kind: authentication
  name: Stack Exchange Authentication
  slug: stack-exchange-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Stack Exchange Domain Security
  slug: stack-exchange-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: stack-exchange
tags:
- Answers
- Code
- Community
- Developer Tools
- Knowledge Base
- Q&A
- Questions
- Stack Exchange
---
