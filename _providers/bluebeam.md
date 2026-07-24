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
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Bluebeam Agentic Access
  operation_count: 10
  slug: bluebeam-agentic-access
  summary_line: 10 operations · 5 acting
api_count: 5
apis:
- description: 'The Bluebeam Studio Prime Integration API leverages the Bluebeam Public API to enable third-party application integrations with Studio Prime. APIs support programmatic access to project drawing sets, '
  name: Bluebeam Studio Prime Integration API
  slug: bluebeam-studio-prime-api
- description: Document management within sessions
  name: bluebeam Documents API
  slug: bluebeam-documents-api
- description: Markup and annotation access
  name: bluebeam Markups API
  slug: bluebeam-markups-api
- description: Studio Session management
  name: bluebeam Sessions API
  slug: bluebeam-sessions-api
- description: Session user management
  name: bluebeam Users API
  slug: bluebeam-users-api
artifact_total: 16
collections:
- collection_type: open
  name: Bluebeam Studio API
  slug: open-bluebeam-studio
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bluebeam-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bluebeam-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bluebeam-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/bluebeam-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Bluebeam
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bluebeam-software
- group: company
  title: ''
  type: Website
  url: https://www.bluebeam.com
- group: start
  title: ''
  type: Portal
  url: https://developers.bluebeam.com/
- group: docs
  title: ''
  type: Documentation
  url: https://support.bluebeam.com/integrations/develop-integrations.html
- group: start
  title: ''
  type: GettingStarted
  url: https://support.bluebeam.com/developer/getting-started-dev-portal.html
- group: auth
  title: ''
  type: Authentication
  url: https://support.bluebeam.com/developer/authentication-guide.html
- group: operate
  title: ''
  type: StatusPage
  url: https://status.bluebeam.com/
- group: company
  title: ''
  type: Blog
  url: https://blog.bluebeam.com/
- group: operate
  title: ''
  type: Support
  url: https://community.bluebeam.com/
- group: docs
  title: ''
  type: Documentation
  url: https://support.bluebeam.com/integrations/integrations-hub.html
- group: docs
  title: ''
  type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/bluebeam/refs/heads/main/openapi/bluebeam-studio-openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/bluebeam/refs/heads/main/json-schema/bluebeam-session-schema.json
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/bluebeam/refs/heads/main/json-ld/bluebeam-context.jsonld
description: Bluebeam develops smart, simple project efficiency and collaboration software for design and construction professionals worldwide, with its flagship Bluebeam Revu PDF markup and collaboration tool.
finops:
- name: Bluebeam Finops
  service_category: API
  slug: bluebeam-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bluebeam.png
json_schemas:
- name: Bluebeam Studio Session
  property_count: 13
  slug: bluebeam-session
jsonld:
- class_count: 0
  name: Bluebeam Context
  property_count: 4
  slug: bluebeam-context
layout: provider
modified: '2026-05-19'
name: bluebeam
nav: Providers
network: true
overview: 'bluebeam publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Documents API, Markups API, Sessions API, and 1 more.


  The bluebeam catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  bluebeam''s developer surface includes authentication, developer portal, documentation, getting-started guide, engineering blog, support, and 12 more developer resources.'
plans:
- name: Bluebeam Plans Pricing
  plan_count: 3
  slug: bluebeam-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 5
  name: Bluebeam Rate Limits
  slug: bluebeam-rate-limits
rules:
- name: bluebeam API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: bluebeam-jsonschema-spectral-rules
scopes:
- name: Bluebeam Scopes
  scope_count: 3
  slug: bluebeam-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: developing
  composite: 52.4
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 61.9
    developer_ergonomics: 45.7
    discoverability: 42.5
    governance: 73.7
    operational_transparency: 52.6
  previous_composite: 52.4
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bluebeam/refs/heads/main/screenshots/bluebeam-2026-06-20T173533.png
security:
- kind: authentication
  name: Bluebeam Authentication
  slug: bluebeam-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Bluebeam Domain Security
  slug: bluebeam-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bluebeam
website: https://www.bluebeam.com
---
