---
access_model:
  confidence: high
  label: Open Source (Apache-2.0)
  onboarding: unknown
  pricing: unknown
  public: true
  source:
  - https://github.com/ogen-go/ogen/blob/main/LICENSE
  - https://ogen.dev/docs/intro
  trial: false
  try_now: true
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: derived
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 1.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: The ogen code generator. Invoked as a build-time CLI against a local OpenAPI v3 document — `ogen [options] <spec>` — it writes a Go package containing a typed client, server, router, validators and JS
  name: Ogen
  slug: ogen
artifact_total: 9
common:
- group: commercial
  href: https://artifacts.apis.io/ogen/plans/ogen-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ogen-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/ogen/rate-limits/ogen-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/ogen-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/ogen/finops/ogen-finops.yml
  title: ''
  type: FinOps
  url: finops/ogen-finops.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/ogen-go/ogen/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/ogen-go/ogen/releases
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/ogen-go/ogen/blob/main/CONTRIBUTING.md
- group: company
  title: ''
  type: Website
  url: https://ogen.dev
- group: start
  title: ''
  type: DeveloperPortal
  url: https://ogen.dev
- group: docs
  title: ''
  type: Documentation
  url: https://ogen.dev/docs/intro
- group: docs
  title: ''
  type: APIReference
  url: https://pkg.go.dev/github.com/ogen-go/ogen
- group: start
  title: ''
  type: GettingStarted
  url: https://ogen.dev/docs/intro
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ogen-go
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/ogen-go/ogen
- group: commercial
  title: ''
  type: License
  url: https://github.com/ogen-go/ogen/blob/main/LICENSE
- group: operate
  title: ''
  type: Support
  url: https://github.com/ogen-go/ogen/discussions
- group: operate
  title: ''
  type: Community
  url: https://t.me/ogen_dev
- group: docs
  href: https://artifacts.apis.io/ogen/json-schema/ogen-config.jsonschema.json
  title: ''
  type: JSONSchema
  url: json-schema/ogen-config.jsonschema.json
- group: build
  href: https://artifacts.apis.io/ogen/packages/ogen-packages.yml
  title: ''
  type: Packages
  url: packages/ogen-packages.yml
- group: build
  href: https://artifacts.apis.io/ogen/packages/ogen-packages.yml
  title: ''
  type: SDKs
  url: packages/ogen-packages.yml
- group: build
  href: https://artifacts.apis.io/ogen/cli/ogen-cli.yml
  title: ''
  type: CLI
  url: cli/ogen-cli.yml
- group: start
  href: https://artifacts.apis.io/ogen/sandbox/ogen-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/ogen-sandbox.yml
- group: design
  href: https://artifacts.apis.io/ogen/vocabulary/ogen-extensions.yml
  title: ''
  type: Vocabulary
  url: vocabulary/ogen-extensions.yml
- group: design
  href: https://artifacts.apis.io/ogen/conformance/ogen-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ogen-conformance.yml
- group: operate
  href: https://artifacts.apis.io/ogen/changelog/ogen-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/ogen-changelog.yml
- group: design
  href: https://artifacts.apis.io/ogen/lifecycle/ogen-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/ogen-lifecycle.yml
- group: agent
  href: https://artifacts.apis.io/ogen/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/ogen/llms/ogen-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ogen-llms.txt
- group: auth
  href: https://artifacts.apis.io/ogen/security/ogen-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/ogen-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://github.com/ogen-go/ogen/blob/main/SECURITY.md
- group: auth
  href: https://artifacts.apis.io/ogen/security/ogen-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ogen-domain-security.yml
created: '2026-03-25'
description: 'Ogen is an Apache-2.0 OpenAPI v3 code generator for Go, maintained by the ogen-go organization. It reads an OpenAPI v3 document at build time and emits a statically typed Go client and server: code-generated JSON encoding with no reflection or interface{}, code-generated validators, a static radix router, sum types for oneOf with name, type and value discrimination, Opt/Nil/OptNil wrappers instead of pointers, a typed SecuritySource interface, webhook client and server generation, Server-Sent Events client generation, and OpenTelemetry tracing and metrics. Behaviour is steered by a YAML config file with a published JSON Schema and by a twelve-term registry of x-ogen-* specification extensions. Ogen operates no hosted API of its own — it is distributed as a Go module, a pinned go.mod tool dependency, and a distroless container image.'
finops:
- has_sources: false
  method: generated
  name: Ogen Finops
  primary_unit: request
  service_category: API
  slug: ogen-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ogen.png
json_schemas:
- name: Ogen Configuration Schema
  property_count: 3
  slug: ogen-config.jsonschema
layout: provider
modified: '2026-08-06'
name: Ogen
nav: Providers
network: true
overview: 'Ogen is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Code Generation, Go, OpenAPI, SDK, and Developer Tools.


  Ogen''s developer surface includes documentation, API reference, getting-started guide, support, CLI, sandbox, changelog, and 23 more developer resources.'
plans:
- name: Ogen Plans Pricing
  plan_count: 3
  slug: ogen-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 5
  name: Ogen Rate Limits
  slug: ogen-rate-limits
score:
  band: thin
  composite: 36.2
  coverage:
    artifact_dirs: 20
    catalog_earned: 48.4
    catalog_earned_first_party: 5.0
    catalog_gap: 66.6
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 7.9
    contract_governance: 33.3
    contract_quality: 7.2
    developer_ergonomics: 66.1
    discoverability: 57.1
    operational_transparency: 36.8
  open_source:
    applies: true
    score: 85.0
  previous_composite: 36.2
  provenance:
    conformance: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/ogen/ogen-2026-06-20T190640.png
security:
- kind: domain-security
  name: Ogen Domain Security
  slug: ogen-domain-security
  summary_line: TLSv1.3
- kind: vulnerability-disclosure
  name: Ogen Vulnerability Disclosure
  slug: ogen-vulnerability-disclosure
  summary_line: security.txt
skill_count: 2
skills:
- name: Generate a Go client and server from an OpenAPI v3 spec with ogen
  slug: ogen-generate-go-client-server
- name: Validate an OpenAPI v3 document against the ogen parser
  slug: ogen-validate-openapi
slug: ogen
tags:
- Code Generation
- Go
- OpenAPI
- SDK
- Developer Tools
- Open Source
- JSON Schema
- Client Library
- API Design
- OpenTelemetry
- SDK Generation
website: https://ogen.dev
---
