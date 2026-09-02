---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: 'Voiden is a desktop application (Electron/TypeScript) for API design, testing, and documentation using .void file format — plain Markdown with structured request blocks. Features reusable blocks with '
  name: Voiden Desktop Tool
  slug: voiden-tool
artifact_total: 10
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/VoidenHQ/voiden/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/VoidenHQ/voiden/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/VoidenHQ/voiden/blob/main/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/VoidenHQ/voiden/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/VoidenHQ/voiden/blob/main/CONTRIBUTING.md
- group: auth
  title: ''
  type: DomainSecurity
  url: security/voiden-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/voiden
- group: company
  title: ''
  type: Website
  url: https://voiden.md/
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/VoidenHQ/voiden
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/voiden-void-file-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/voiden-void-file-structure.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/voiden-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/voiden-vocabulary.yml
- group: company
  title: ''
  type: Blog
  url: https://voiden.md/blog/
- group: commercial
  title: ''
  type: License
  url: https://github.com/VoidenHQ/voiden/blob/main/LICENSE
created: '2026-01-02'
description: Voiden is an offline-first, Git-native API workspace that unifies API design, testing, and documentation in plain Markdown .void files stored alongside your codebase. It uses composable, reusable blocks (endpoints, auth, headers, params, bodies) that behave like code — inheritable, versionable, and composable — eliminating copy-paste drift across API definitions. Supports REST, GraphQL, WebSocket, and gRPC. Built on Electron (TypeScript), Apache 2.0 licensed.
finops:
- name: Voiden Finops
  service_category: API
  slug: voiden-finops
graphqls:
- description: ''
  name: Voiden GraphQL API
  slug: voiden-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/voiden.png
json_schemas:
- name: Voiden .void File
  property_count: 5
  slug: voiden-void-file
json_structures:
- name: Voiden Void File Structure
  property_count: 0
  slug: voiden-void-file-structure
jsonld:
- class_count: 14
  name: Voiden Context
  property_count: 0
  slug: voiden-context
layout: provider
modified: '2026-05-03'
name: Voiden
nav: Providers
network: true
overview: 'Voiden publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include API Design, API Testing, API Documentation, Developer Tools, and Git-Native.


  The Voiden catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Voiden''s developer surface includes engineering blog and 14 more developer resources.'
plans:
- name: Voiden Plans Pricing
  plan_count: 3
  slug: voiden-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 5
  name: Voiden Rate Limits
  slug: voiden-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Voiden API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: voiden-jsonschema-spectral-rules
score:
  band: thin
  composite: 32.5
  coverage:
    artifact_dirs: 12
    catalog_gap: 51.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 25.0
    contract_quality: 18.7
    developer_ergonomics: 11.9
    discoverability: 66.7
    governance: 25.0
    operational_transparency: 39.5
  open_source:
    applies: true
    score: 100.0
  previous_composite: 32.5
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/voiden/refs/heads/main/screenshots/voiden-2026-06-20T201127.png
security:
- kind: domain-security
  name: Voiden Domain Security
  slug: voiden-domain-security
  summary_line: TLSv1.3
slug: voiden
tags:
- API Design
- API Testing
- API Documentation
- Developer Tools
- Git-Native
- Markdown
website: https://voiden.md/
---
