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
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Bluebeam Agentic Access
  operation_count: 10
  slug: bluebeam-agentic-access
  summary_line: 10 operations · 5 acting
api_count: 1
apis:
- description: 'The Bluebeam Studio Prime Integration API leverages the Bluebeam Public API to enable third-party application integrations with Studio Prime. APIs support programmatic access to project drawing sets, '
  name: Bluebeam Studio Prime Integration API
  slug: bluebeam-studio-prime-api
- baseURL: https://api.bluebeam.com
  baseurl_source: declared
  description: Document management within sessions
  name: bluebeam Documents API
  slug: bluebeam-documents-api
- baseURL: https://api.bluebeam.com
  baseurl_source: declared
  description: Markup and annotation access
  name: bluebeam Markups API
  slug: bluebeam-markups-api
- baseURL: https://api.bluebeam.com
  baseurl_source: declared
  description: Studio Session management
  name: bluebeam Sessions API
  slug: bluebeam-sessions-api
- baseURL: https://api.bluebeam.com
  baseurl_source: declared
  description: Session user management
  name: bluebeam Users API
  slug: bluebeam-users-api
artifact_total: 21
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Bluebeam Studio Documents API
  slug: open-bluebeam-documents-api
- collection_type: open
  name: Bluebeam Studio Documents Markups API
  slug: open-bluebeam-markups-api
- collection_type: open
  name: Bluebeam Studio Documents Sessions API
  slug: open-bluebeam-sessions-api
- collection_type: open
  name: Bluebeam Studio API
  slug: open-bluebeam-studio
- collection_type: open
  name: Bluebeam Studio Documents Users API
  slug: open-bluebeam-users-api
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
name: Bluebeam
nav: Providers
network: true
overview: 'Bluebeam publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Documents API, Markups API, Sessions API, and 1 more.


  The Bluebeam catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Bluebeam''s developer surface includes authentication, developer portal, documentation, getting-started guide, engineering blog, support, and 12 more developer resources.'
plans:
- name: Bluebeam Plans Pricing
  plan_count: 3
  slug: bluebeam-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 5
  name: Bluebeam Rate Limits
  slug: bluebeam-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Bluebeam API Rules
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
