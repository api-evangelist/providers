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
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-08-30'
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
random_paper: 10
rate_limits:
- limit_count: 5
  name: Bluebeam Rate Limits
  slug: bluebeam-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: bluebeam API Rules
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
  band: thin
  composite: 37.0
  coverage:
    artifact_dirs: 14
    catalog_gap: 70.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 9.8
    contract_quality: 59.0
    developer_ergonomics: 47.6
    discoverability: 50.0
    governance: 9.8
    operational_transparency: 26.3
  previous_composite: 37.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: false
    note: provider carries no tags; regime could not be determined
    undetermined: true
  schema_version: 0.17.2
  scored_at: '2026-08-30'
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
