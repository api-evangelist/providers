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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.7
  scored_at: '2026-09-16'
api_count: 1
apis:
- description: API Blueprint is a high-level API description language using Markdown-based syntax for designing, documenting, and prototyping APIs. Files use the .apib extension with media type text/vnd.apiblueprint
  name: API Blueprint
  slug: api-blueprint
- baseURL: https://api.apiblueprint.org
  baseurl_source: declared
  description: Compose an API description format from API Elements.
  name: API Blueprint Composer API
  slug: api-blueprint-composer-api
- baseURL: https://api.apiblueprint.org
  baseurl_source: declared
  description: Parse an API description format into API Elements.
  name: API Blueprint Parser API
  slug: api-blueprint-parser-api
- baseURL: https://api.apiblueprint.org
  baseurl_source: declared
  description: Entry point listing the available affordances.
  name: API Blueprint Service Root API
  slug: api-blueprint-service-root-api
- baseURL: https://api.apiblueprint.org
  baseurl_source: declared
  description: Convert an API description between formats through a JSON envelope. Advertised by the live service root; absent from the provider's published contract.
  name: API Blueprint Transform API
  slug: api-blueprint-transform-api
- baseURL: https://api.apiblueprint.org
  baseurl_source: declared
  description: Validate an API description and return its annotations. Advertised by the live service root; absent from the provider's published contract.
  name: API Blueprint Validate API
  slug: api-blueprint-validate-api
artifact_total: 24
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/api-blueprint/refs/heads/main/overlays/api-blueprint-parsing-service-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/api-blueprint-parsing-service-overlay.yaml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/apiaryio/api-blueprint/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/apiaryio/api-blueprint/releases
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/api-blueprint/refs/heads/main/security/api-blueprint-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/api-blueprint-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://apiblueprint.org
- group: docs
  title: ''
  type: Documentation
  url: https://apiblueprint.org/documentation/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apiaryio
- group: commercial
  title: ''
  type: TermsOfService
  url: https://github.com/apiaryio/api-blueprint/blob/master/LICENSE
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/api-blueprint/refs/heads/main/packages/api-blueprint-packages.yml
  title: ''
  type: Packages
  url: packages/api-blueprint-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/api-blueprint/refs/heads/main/packages/api-blueprint-packages.yml
  title: ''
  type: SDKs
  url: packages/api-blueprint-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/api-blueprint/refs/heads/main/cli/api-blueprint-cli.yml
  title: ''
  type: CLI
  url: cli/api-blueprint-cli.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/api-blueprint/refs/heads/main/llms/api-blueprint-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/api-blueprint-llms.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/api-blueprint/refs/heads/main/conformance/api-blueprint-conformance.yml
  title: ''
  type: Conformance
  url: conformance/api-blueprint-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/api-blueprint/refs/heads/main/lifecycle/api-blueprint-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/api-blueprint-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/api-blueprint/refs/heads/main/changelog/api-blueprint-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/api-blueprint-changelog.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/api-blueprint/refs/heads/main/plans/api-blueprint-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/api-blueprint-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/api-blueprint/refs/heads/main/rate-limits/api-blueprint-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/api-blueprint-rate-limits.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/api-blueprint/refs/heads/main/mcp/api-blueprint-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/api-blueprint-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/api-blueprint/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/api-blueprint/refs/heads/main/finops/api-blueprint-finops.yml
  title: ''
  type: FinOps
  url: finops/api-blueprint-finops.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://apiblueprint.org/developers.html
- group: operate
  title: ''
  type: Support
  url: https://apiblueprint.org/support.html
- group: learn
  title: ''
  type: Tutorials
  url: https://apiblueprint.org/documentation/tutorial.html
- group: docs
  title: ''
  type: Reference
  url: https://apiblueprint.org/documentation/specification.html
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/apiaryio/api-blueprint
created: '2026-03-25'
description: API Blueprint is a high-level API description language using Markdown-based syntax for designing, documenting, and prototyping web APIs. Created by Apiary and released under the MIT License, API Blueprint uses .apib files with a concise Markdown format that makes APIs accessible to both technical and non-technical stakeholders. The project is no longer actively maintained (all apiaryio GitHub repos are archived as of 2024) but remains a notable specification in API design history, influencing later formats like OpenAPI.
features:
- description: API Blueprint uses concise Markdown syntax making API descriptions readable by both developers and non-technical stakeholders. Files use the .apib extension with media type text/vnd.apiblueprint.
  name: Markdown-Based Syntax
- description: Supports reusable data structure definitions using MSON (Markdown Syntax for Object Notation) for describing complex request and response schemas.
  name: Data Structure Modeling
- description: API Blueprint documents can drive mock server generation for rapid prototyping and front-end development before backend implementation.
  name: Mock Server Generation
- description: The Dredd HTTP testing tool uses API Blueprint specs to run contract tests validating that API implementations match their documented contracts.
  name: Testing with Dredd
- description: API Blueprint evolution was governed through an RFC process similar to Rust and Django, with proposals submitted to the api-blueprint-rfcs repository.
  name: RFC-Driven Governance
finops:
- name: Api Blueprint Finops
  service_category: API
  slug: api-blueprint-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/api-blueprint.png
integrations:
- description: API Blueprint was the native specification format of the Apiary platform (acquired by Oracle), which provided hosted documentation, mock servers, and testing.
  name: Apiary
- description: The canonical API Blueprint parser written in C++ with bindings for Node.js (drafter.js, drafter-npm) and other languages.
  name: Drafter Parser
- description: Language-agnostic HTTP API testing tool that validates live API implementations against API Blueprint or Swagger/OpenAPI specs.
  name: Dredd Testing Framework
- description: The swagger2blueprint tool converted Swagger API descriptions into API Blueprint format for migration workflows.
  name: Swagger Conversion
json_schemas:
- name: Api Blueprint Api Elements Element
  property_count: 0
  slug: api-blueprint-api-elements-element
layout: provider
modified: '2026-09-02'
name: API Blueprint
nav: Providers
network: true
overview: 'API Blueprint publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Composer API, Parser API, Service Root API, and 2 more. Tagged areas include API Design, Specification Language, Markdown, Documentation, and API Description Language.


  API Blueprint''s developer surface includes documentation, CLI, changelog, support, and 21 more developer resources.'
plans:
- name: Api Blueprint Plans Pricing
  plan_count: 0
  slug: api-blueprint-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Api Blueprint Rate Limits
  slug: api-blueprint-rate-limits
score:
  band: developing
  composite: 40.5
  coverage:
    artifact_dirs: 22
    catalog_earned: 41.0
    catalog_earned_first_party: 0.0
    catalog_gap: 74.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.7
  facets:
    access_clarity: 18.4
    contract_governance: 4.5
    contract_quality: 58.1
    developer_ergonomics: 70.8
    discoverability: 59.3
    operational_transparency: 18.4
  previous_composite: 41.2
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/api-blueprint/refs/heads/main/screenshots/api-blueprint-2026-06-20T172201.png
security:
- kind: authentication
  name: Api Blueprint Authentication
  slug: api-blueprint-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Api Blueprint Domain Security
  slug: api-blueprint-domain-security
  summary_line: TLSv1.3 · DMARC
slug: api-blueprint
tags:
- API Design
- Specification Language
- Markdown
- Documentation
- API Description Language
- Parsing
- Open-Source
- Developer Tools
use_cases:
- description: Write human-readable API documentation in Markdown that doubles as a machine-parseable specification for tooling.
  name: API Documentation
- description: Use API Blueprint specs with Dredd to verify that API implementations conform to their documented contracts in CI pipelines.
  name: Contract Testing
- description: Rapidly prototype APIs by writing Blueprint specs first, then generating mock servers from the specification.
  name: API Prototyping
website: https://apiblueprint.org
---
