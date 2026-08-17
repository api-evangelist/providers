---
access_model:
  confidence: high
  label: Open Source (MIT)
  onboarding: unknown
  pricing: unknown
  public: true
  source:
  - https://github.com/microsoft/kiota/blob/main/LICENSE
  - https://learn.microsoft.com/en-us/openapi/kiota/install
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 14.9
  scored_at: '2026-08-17'
api_count: 1
apis:
- description: Kiota generates strongly-typed, lightweight API clients from OpenAPI descriptions in C#, Dart, Go, Java, PHP, Python, Ruby and TypeScript, with minimal dependencies and idiomatic code patterns, plus a
  name: Kiota
  slug: kiota
artifact_total: 9
common:
- group: operate
  title: ''
  type: Releases
  url: https://github.com/microsoft/kiota/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/microsoft/kiota/blob/main/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/microsoft/kiota/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/microsoft/kiota/blob/main/CONTRIBUTING.md
- group: company
  title: ''
  type: Website
  url: https://learn.microsoft.com/en-us/openapi/kiota/
- group: start
  title: ''
  type: Portal
  url: https://learn.microsoft.com/en-us/openapi/kiota/
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/openapi/kiota/overview
- group: docs
  title: ''
  type: APIReference
  url: https://learn.microsoft.com/en-us/openapi/kiota/using
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/openapi/kiota/quickstarts/
- group: operate
  title: ''
  type: Support
  url: https://github.com/microsoft/kiota/issues
- group: operate
  title: ''
  type: Community
  url: https://github.com/microsoft/kiota/discussions
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/microsoft/kiota
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/microsoft/kiota
- group: company
  title: ''
  type: Blog
  url: https://devblogs.microsoft.com/microsoft365dev/
- group: commercial
  title: ''
  type: License
  url: https://github.com/microsoft/kiota/blob/main/LICENSE
- group: commercial
  title: ''
  type: TermsOfService
  url: https://learn.microsoft.com/en-us/legal/termsofuse
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: build
  title: ''
  type: CLI
  url: cli/kiota-cli.yml
- group: build
  title: ''
  type: Packages
  url: packages/kiota-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/kiota-packages.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/kiota-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/kiota-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://learn.microsoft.com/en-us/openapi/kiota/support
- group: auth
  title: ''
  type: Authentication
  url: authentication/kiota-authentication.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/kiota-vocabulary.yml
- group: design
  title: ''
  type: Rules
  url: rules/kiota-validation-rules.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/kiota-conformance.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/kiota-workspace-schema.json
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kiota-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/kiota-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/kiota-security.txt
- group: auth
  title: ''
  type: Security
  url: security/kiota-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/kiota-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kiota-domain-security.yml
created: '2026-03-25'
description: 'Kiota is Microsoft''s open source (MIT) API client generator: a command line tool that turns any OpenAPI-described API into a strongly-typed, lightweight client in C#, Dart, Go, Java, PHP, Python, Ruby or TypeScript. It exists to remove the need to take a dependency on a different hand-written SDK for every API you call. Kiota generates only the source it needs on top of a small per-language core library, keeps external dependencies minimal, and can target a filtered subset of a large description. Beyond code SDKs it also emits agent-facing plugin packages — apiplugin for Microsoft 365 Copilot declarative agents, openai manifests, and API Manifest permission snapshots. Kiota is a consumer of API descriptions rather than a publisher of an API: there is no Kiota endpoint, base URL, API key or status page. Its surface is a CLI, runtime libraries in eight package registries, a published OpenAPI extension vocabulary, and a nine-rule description validation ruleset it runs before
  every generation.'
finops:
- name: Kiota Finops
  service_category: API
  slug: kiota-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kiota.png
json_schemas:
- name: Kiota Workspace
  property_count: 3
  slug: kiota-workspace
layout: provider
modified: '2026-08-06'
name: Kiota
nav: Providers
network: true
overview: 'Kiota publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Code Generation, Microsoft, OpenAPI, SDKs, and Developer Tools.


  The Kiota catalog on APIs.io includes 1 Spectral governance ruleset.


  Kiota''s developer surface includes developer portal, documentation, API reference, getting-started guide, support, engineering blog, CLI, and 27 more developer resources.'
plans:
- name: Kiota Plans Pricing
  plan_count: 3
  slug: kiota-plans-pricing
random_paper: 89
rate_limits:
- limit_count: 5
  name: Kiota Rate Limits
  slug: kiota-rate-limits
rules:
- name: Kiota API Rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: kiota-validation-rules
score:
  band: thin
  composite: 38.3
  delta: 0.0
  facets:
    commercial_clarity: 36.8
    contract_quality: 0.0
    developer_ergonomics: 65.2
    discoverability: 77.8
    governance: 33.3
    operational_transparency: 47.4
  previous_composite: 38.3
  provenance:
    conformance: first-party
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kiota/refs/heads/main/screenshots/kiota-2026-06-20T184046.png
security:
- kind: authentication
  name: Kiota Authentication
  slug: kiota-authentication
  summary_line: oauth2-device-code/apiKey/http-bearer/anonymous · 0 schemes
- kind: domain-security
  name: Kiota Domain Security
  slug: kiota-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Kiota Vulnerability Disclosure
  slug: kiota-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: kiota
tags:
- Code Generation
- Microsoft
- OpenAPI
- SDKs
- Developer Tools
- API Clients
- Open Source
- CLI
- JSON Schema
website: https://learn.microsoft.com/en-us/openapi/kiota/
---
