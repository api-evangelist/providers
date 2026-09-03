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
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: Command-line tool and Go library that converts OpenAPI 3.0 and 3.1 specifications into Go server-side, client-side, and HTTP model code with support for multiple Go web frameworks.
  name: Oapi-Codegen
  slug: oapi-codegen
artifact_total: 6
common:
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/oapi-codegen/oapi-codegen/blob/main/CONTRIBUTING.md
- group: company
  title: ''
  type: Website
  url: https://github.com/oapi-codegen/oapi-codegen
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/oapi-codegen/oapi-codegen#readme
- group: docs
  title: ''
  type: APIReference
  url: https://pkg.go.dev/github.com/oapi-codegen/oapi-codegen/v2/pkg/codegen
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/oapi-codegen/oapi-codegen#install
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/oapi-codegen
- group: other
  title: ''
  type: GoDoc
  url: https://pkg.go.dev/github.com/oapi-codegen/oapi-codegen/v2
- group: operate
  title: ''
  type: Support
  url: https://github.com/oapi-codegen/oapi-codegen/discussions
- group: other
  title: ''
  type: Governance
  url: https://github.com/oapi-codegen/governance
- group: commercial
  title: ''
  type: License
  url: https://github.com/oapi-codegen/oapi-codegen/blob/main/LICENSE
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/oapi-codegen-changelog.yml
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://github.com/oapi-codegen/oapi-codegen/releases
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/oapi-codegen-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://github.com/oapi-codegen/oapi-codegen#backwards-compatibility
- group: build
  title: ''
  type: Packages
  url: packages/oapi-codegen-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/oapi-codegen-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/oapi-codegen-cli.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/oapi-codegen-configuration-schema.json
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/oapi-codegen-openapi-extensions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/oapi-codegen-conformance.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/oapi-codegen-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://github.com/oapi-codegen/.github/blob/main/SECURITY.md
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/oapi-codegen-llms.txt
created: '2026-03-25'
description: oapi-codegen is an open source Go code generator that produces client and server boilerplate from OpenAPI 3.0 and 3.1 specifications with support for Echo, Chi, Gin, Gorilla/Mux, Iris, Fiber, and the standard library net/http router.
finops:
- name: Oapi Codegen Finops
  service_category: API
  slug: oapi-codegen-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/oapi-codegen.png
json_schemas:
- name: Oapi Codegen Configuration
  property_count: 7
  slug: oapi-codegen-configuration
layout: provider
modified: '2026-08-06'
name: Oapi-Codegen
nav: Providers
network: true
overview: 'Oapi-Codegen publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Code Generation, Developer Tools, Go, OpenAPI, and SDK.


  Oapi-Codegen''s developer surface includes documentation, API reference, getting-started guide, support, changelog, release notes, CLI, and 16 more developer resources.'
plans:
- name: Oapi Codegen Plans Pricing
  plan_count: 3
  slug: oapi-codegen-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 5
  name: Oapi Codegen Rate Limits
  slug: oapi-codegen-rate-limits
score:
  band: thin
  composite: 33.0
  coverage:
    artifact_dirs: 13
    catalog_gap: 63.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 33.3
    contract_quality: 8.0
    developer_ergonomics: 47.6
    discoverability: 66.7
    governance: 33.3
    operational_transparency: 44.7
  open_source:
    applies: true
    score: 50.0
  previous_composite: 33.0
  provenance:
    conformance: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/oapi-codegen/refs/heads/main/screenshots/oapi-codegen-2026-06-20T190551.png
security:
- kind: vulnerability-disclosure
  name: Oapi Codegen Vulnerability Disclosure
  slug: oapi-codegen-vulnerability-disclosure
  summary_line: contact published
slug: oapi-codegen
tags:
- Code Generation
- Developer Tools
- Go
- OpenAPI
- SDK
- Tooling
---
