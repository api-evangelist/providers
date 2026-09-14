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
api_count: 2
apis:
- description: API Blueprint is a high-level API description language using Markdown-based syntax for designing, documenting, and prototyping APIs. Files use the .apib extension with media type text/vnd.apiblueprint
  name: API Blueprint
  slug: api-blueprint
- baseURL: https://api.apiblueprint.org
  baseurl_source: declared
  description: The API Blueprint API is the parsing service operated at api.apiblueprint.org by the API Blueprint project. It parses API Blueprint and Swagger 2.0 documents into the Refract Parse Result Namespace (A
  name: API Blueprint API
  slug: api-blueprint-api
artifact_total: 20
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/apiaryio/api-blueprint/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/apiaryio/api-blueprint/releases
- group: auth
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
  title: ''
  type: Packages
  url: packages/api-blueprint-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/api-blueprint-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/api-blueprint-cli.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/api-blueprint-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/api-blueprint-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/api-blueprint-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/api-blueprint-changelog.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/api-blueprint-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/api-blueprint-rate-limits.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/api-blueprint-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
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
overview: 'API Blueprint publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include API Design, Specification Language, Markdown, Documentation, and API Description Language.


  API Blueprint''s developer surface includes documentation, CLI, changelog, support, and 20 more developer resources.'
plans:
- name: Api Blueprint Plans Pricing
  plan_count: 0
  slug: api-blueprint-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Api Blueprint Rate Limits
  slug: api-blueprint-rate-limits
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
- Open Source
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
