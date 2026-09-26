---
access_model:
  confidence: medium
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
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.4
  scored_at: '2026-09-25'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Medium Agentic Access
  operation_count: 9
  slug: medium-agentic-access
  summary_line: 9 operations · 5 acting
api_count: 2
apis:
- baseURL: https://api.medium.com/v1
  baseurl_source: declared
  description: Endpoints for initiating the OAuth2 authorization flow by redirecting users to Medium's authorization page.
  name: medium Authorization API
  slug: medium-authorization-api
- baseURL: https://api.medium.com/v1
  baseurl_source: declared
  description: Operations for uploading images to Medium for use in posts. Supports JPEG, PNG, GIF, and TIFF formats.
  name: medium Images API
  slug: medium-images-api
- baseURL: https://api.medium.com/v1
  baseurl_source: declared
  description: Operations for creating new posts on a user's profile or within a publication, supporting HTML and Markdown content formats.
  name: medium Posts API
  slug: medium-posts-api
- baseURL: https://api.medium.com/v1
  baseurl_source: declared
  description: Operations for listing publications a user is associated with and retrieving contributors for a given publication.
  name: medium Publications API
  slug: medium-publications-api
- baseURL: https://api.medium.com/v1
  baseurl_source: declared
  description: Endpoints for exchanging authorization codes for access tokens and refreshing expired access tokens.
  name: medium Tokens API
  slug: medium-tokens-api
- baseURL: https://api.medium.com/v1
  baseurl_source: declared
  description: Operations for retrieving authenticated user profile information including username, name, URL, and avatar image.
  name: medium Users API
  slug: medium-users-api
artifact_total: 27
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Medium OAuth2 Authorization API
  slug: open-medium-authorization-api
- collection_type: open
  name: Medium OAuth2 Authorization Images API
  slug: open-medium-images-api
- collection_type: open
  name: Medium OAuth2 API
  slug: open-medium-oauth2
- collection_type: open
  name: Medium OAuth2 Authorization Posts API
  slug: open-medium-posts-api
- collection_type: open
  name: Medium OAuth2 Authorization Publications API
  slug: open-medium-publications-api
- collection_type: open
  name: Medium REST API
  slug: open-medium-rest-api
- collection_type: open
  name: Medium OAuth2 Authorization Tokens API
  slug: open-medium-tokens-api
- collection_type: open
  name: Medium OAuth2 Authorization Users API
  slug: open-medium-users-api
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/medium/refs/heads/main/agentic-access/medium-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/medium-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/medium/refs/heads/main/security/medium-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/medium-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/medium/refs/heads/main/authentication/medium-authentication.yml
  title: ''
  type: Authentication
  url: authentication/medium-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/medium-com
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/medium/refs/heads/main/json-ld/medium-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/medium-context.jsonld
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/medium/refs/heads/main/json-schema/medium-post-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/medium-post-schema.json
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/medium/refs/heads/main/json-schema/medium-user-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/medium-user-schema.json
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/medium/refs/heads/main/json-schema/medium-publication-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/medium-publication-schema.json
- group: company
  title: ''
  type: Blog
  url: https://medium.com/feed/blog
- group: company
  title: ''
  type: Website
  url: https://medium.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Medium
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/Medium/medium-api-docs
- group: docs
  title: ''
  type: APIReference
  url: https://github.com/Medium/medium-api-docs#3-resources
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/Medium/medium-api-docs#2-authentication
- group: operate
  title: ''
  type: Support
  url: https://help.medium.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.medium.com/
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/medium/refs/heads/main/lifecycle/medium-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/medium-lifecycle.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/medium/refs/heads/main/packages/medium-packages.yml
  title: ''
  type: Packages
  url: packages/medium-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/medium/refs/heads/main/packages/medium-packages.yml
  title: ''
  type: SDKs
  url: packages/medium-packages.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/medium/refs/heads/main/scopes/medium-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/medium-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/medium/refs/heads/main/conventions/medium-conventions.yml
  title: ''
  type: Conventions
  url: conventions/medium-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/medium/refs/heads/main/errors/medium-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/medium-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/medium/refs/heads/main/conformance/medium-conformance.yml
  title: ''
  type: Conformance
  url: conformance/medium-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/medium/refs/heads/main/data-model/medium-data-model.yml
  title: ''
  type: DataModel
  url: data-model/medium-data-model.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/medium/refs/heads/main/llms/medium-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/medium-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/medium/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-05-04'
description: 'Medium is an online publishing platform where writers publish stories and readers follow topics, publications and authors. Its developer surface is a small OAuth2 REST API at api.medium.com/v1 that lets an integration read the authenticated user''s profile, list the publications they write to or edit, upload images, and publish posts to a profile or into a publication. Medium states the API is no longer supported and does not accept new integrations: existing tokens continue to work, but new integration tokens have not been issued since 2023 and the documentation repository was archived in 2023.'
finops:
- name: Medium Finops
  service_category: API
  slug: medium-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/medium.png
json_schemas:
- name: Medium Post
  property_count: 14
  slug: medium-post
- name: Medium Publication
  property_count: 6
  slug: medium-publication
- name: Medium User
  property_count: 5
  slug: medium-user
jsonld:
- class_count: 0
  name: Medium Context
  property_count: 5
  slug: medium-context
layout: provider
modified: '2026-09-17'
name: Medium
nav: Providers
network: true
overview: 'Medium publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Authorization API, Images API, Posts API, and 3 more. Tagged areas include Publishing, Content, Blogging, Media, and Social.


  The Medium catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Medium''s developer surface includes authentication, engineering blog, documentation, API reference, getting-started guide, support, and 20 more developer resources.'
plans:
- name: Medium Plans Pricing
  plan_count: 0
  slug: medium-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Medium Rate Limits
  slug: medium-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Medium API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: medium-jsonschema-spectral-rules
scopes:
- name: Medium Scopes
  scope_count: 0
  slug: medium-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 37.7
  coverage:
    artifact_dirs: 26
    catalog_earned: 48.3
    catalog_earned_first_party: 0.0
    catalog_gap: 66.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.1
  facets:
    access_clarity: 7.9
    contract_governance: 14.4
    contract_quality: 52.5
    developer_ergonomics: 56.5
    discoverability: 66.1
    operational_transparency: 18.4
  previous_composite: 37.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.5
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/medium/refs/heads/main/screenshots/medium-2026-06-20T185123.png
security:
- kind: authentication
  name: Medium Authentication
  slug: medium-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Medium Domain Security
  slug: medium-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: medium
tags:
- Publishing
- Content
- Blogging
- Media
- Social
- Writing
- Authentication
- Deprecated API
website: https://medium.com
---
