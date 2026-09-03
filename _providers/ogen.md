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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.4
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: The ogen code generator. Invoked as a build-time CLI against a local OpenAPI v3 document — `ogen [options] <spec>` — it writes a Go package containing a typed client, server, router, validators and JS
  name: Ogen
  slug: ogen
artifact_total: 7
common:
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
  title: ''
  type: JSONSchema
  url: json-schema/ogen-config.jsonschema.json
- group: build
  title: ''
  type: Packages
  url: packages/ogen-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/ogen-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/ogen-cli.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/ogen-sandbox.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/ogen-extensions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ogen-conformance.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/ogen-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ogen-lifecycle.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ogen-llms.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ogen-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://github.com/ogen-go/ogen/blob/main/SECURITY.md
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ogen-domain-security.yml
created: '2026-03-25'
description: 'Ogen is an Apache-2.0 OpenAPI v3 code generator for Go, maintained by the ogen-go organization. It reads an OpenAPI v3 document at build time and emits a statically typed Go client and server: code-generated JSON encoding with no reflection or interface{}, code-generated validators, a static radix router, sum types for oneOf with name, type and value discrimination, Opt/Nil/OptNil wrappers instead of pointers, a typed SecuritySource interface, webhook client and server generation, Server-Sent Events client generation, and OpenTelemetry tracing and metrics. Behaviour is steered by a YAML config file with a published JSON Schema and by a twelve-term registry of x-ogen-* specification extensions. Ogen operates no hosted API of its own — it is distributed as a Go module, a pinned go.mod tool dependency, and a distroless container image.'
finops:
- name: Ogen Finops
  service_category: API
  slug: ogen-finops
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
overview: 'Ogen publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Code Generation, Go, OpenAPI, SDK, and Developer Tools.


  Ogen''s developer surface includes documentation, API reference, getting-started guide, support, CLI, sandbox, changelog, and 20 more developer resources.'
plans:
- name: Ogen Plans Pricing
  plan_count: 3
  slug: ogen-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 5
  name: Ogen Rate Limits
  slug: ogen-rate-limits
score:
  band: thin
  composite: 33.1
  coverage:
    artifact_dirs: 17
    catalog_gap: 63.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -5.2
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 33.3
    contract_quality: 8.0
    developer_ergonomics: 66.1
    discoverability: 59.3
    governance: 33.3
    operational_transparency: 36.8
  previous_composite: 38.3
  provenance:
    conformance: first-party
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/ogen/refs/heads/main/screenshots/ogen-2026-06-20T190640.png
security:
- kind: domain-security
  name: Ogen Domain Security
  slug: ogen-domain-security
  summary_line: TLSv1.3
- kind: vulnerability-disclosure
  name: Ogen Vulnerability Disclosure
  slug: ogen-vulnerability-disclosure
  summary_line: security.txt
slug: ogen
tags:
- Code Generation
- Go
- OpenAPI
- SDK
- Developer Tools
- Open-Source
- JSON-Schema
- Client Libraries
- API Design
- OpenTelemetry
website: https://ogen.dev
---
