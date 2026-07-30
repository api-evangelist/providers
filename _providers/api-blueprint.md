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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: API Blueprint is a high-level API description language using Markdown-based syntax for designing, documenting, and prototyping APIs. Files use the .apib extension with media type text/vnd.apiblueprint
  name: API Blueprint
  slug: api-blueprint
artifact_total: 17
common:
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
layout: provider
modified: '2026-04-19'
name: API Blueprint
nav: Providers
network: true
overview: 'API Blueprint publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include API Design, Specification Language, Markdown, and Documentation.


  API Blueprint''s developer surface includes documentation and 4 more developer resources.'
plans:
- name: Api Blueprint Plans Pricing
  plan_count: 3
  slug: api-blueprint-plans-pricing
random_paper: 28
rate_limits:
- limit_count: 5
  name: Api Blueprint Rate Limits
  slug: api-blueprint-rate-limits
score:
  band: emerging
  composite: 21.5
  delta: -1.8
  facets:
    commercial_clarity: 50.0
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 23.3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/api-blueprint/refs/heads/main/screenshots/api-blueprint-2026-06-20T172201.png
security:
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
use_cases:
- description: Write human-readable API documentation in Markdown that doubles as a machine-parseable specification for tooling.
  name: API Documentation
- description: Use API Blueprint specs with Dredd to verify that API implementations conform to their documented contracts in CI pipelines.
  name: Contract Testing
- description: Rapidly prototype APIs by writing Blueprint specs first, then generating mock servers from the specification.
  name: API Prototyping
website: https://apiblueprint.org
---
