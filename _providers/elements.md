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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.0
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Elements Agentic Access
  operation_count: 6
  slug: elements-agentic-access
  summary_line: 6 operations
api_count: 1
apis:
- baseURL: https://stoplight.io
  baseurl_source: spec
  description: Configuration props and attributes for the Stoplight Elements API component controlling layout, visibility, Try It behavior, routing, and OpenAPI specification loading.
  name: Stoplight Elements Configuration API
  slug: elements-configuration-api
- baseURL: https://stoplight.io
  baseurl_source: spec
  description: Integration and embedding guides for using Elements in React, Angular, and plain HTML via Web Components or CDN.
  name: Stoplight Elements Integration API
  slug: elements-integration-api
artifact_total: 14
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Stoplight Elements Configuration API
  slug: open-elements-configuration-api
- collection_type: open
  name: Stoplight Elements API
  slug: open-elements-elements
- collection_type: open
  name: Stoplight Elements Configuration Integration API
  slug: open-elements-integration-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/elements-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/elements-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/stoplight
- group: docs
  title: ''
  type: Documentation
  url: https://docs.stoplight.io/docs/elements
- group: build
  title: ''
  type: GitHub
  url: https://github.com/stoplightio/elements
- group: build
  title: ''
  type: npm
  url: https://www.npmjs.com/package/@stoplight/elements
- group: other
  title: ''
  type: CDN
  url: https://unpkg.com/@stoplight/elements/web-components.min.js
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.stoplight.io/docs/elements/b074dc07b3bae-getting-started-with-elements-in-react
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.stoplight.io/docs/elements/19a7f9f0cbf23-getting-started-with-web-component
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.stoplight.io/docs/elements/507fb7fab9b7d-getting-started-with-elements-in-angular
- group: docs
  title: ''
  type: Reference
  url: https://docs.stoplight.io/docs/elements/ZG9jOjMyNjU5MTM-elements-configuration-options
- group: company
  title: ''
  type: Website
  url: https://stoplight.io/open-source/elements
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/stoplightio/elements/blob/main/CHANGELOG.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/stoplightio/elements/blob/main/LICENSE
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/elements-configuration-schema.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/elements-context.jsonld
created: '2026-03-18'
description: Stoplight Elements is an open-source API documentation component library for rendering OpenAPI specifications interactively. It provides embeddable React and Web Components that produce beautiful, interactive API reference documentation from any OpenAPI 2.0, 3.0, or 3.1 document, with support for a Try It console, code sample generation, sidebar and stacked layouts, and internal operation filtering.
finops:
- name: Elements Finops
  service_category: API
  slug: elements-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/elements.png
json_schemas:
- name: Stoplight Elements Configuration
  property_count: 20
  slug: elements-configuration
jsonld:
- class_count: 0
  name: Elements Context
  property_count: 7
  slug: elements-context
layout: provider
modified: '2026-05-19'
name: Stoplight Elements
nav: Providers
network: true
overview: 'Stoplight Elements publishes 2 APIs on the [APIs.io](https://apis.io/) network: Configuration API and Integration API. Tagged areas include API Documentation, Developer Tools, Documentation, Interactive Docs, and OpenAPI.


  The Stoplight Elements catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Stoplight Elements'' developer surface includes documentation, GitHub presence, getting-started guide, changelog, and 12 more developer resources.'
plans:
- name: Elements Plans Pricing
  plan_count: 3
  slug: elements-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 5
  name: Elements Rate Limits
  slug: elements-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Stoplight Elements API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: elements-jsonschema-spectral-rules
score:
  band: thin
  composite: 28.9
  coverage:
    artifact_dirs: 12
    catalog_gap: 50.8
    catalog_max: 100.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 9.8
    contract_quality: 57.1
    developer_ergonomics: 19.0
    discoverability: 59.3
    governance: 9.8
    operational_transparency: 28.9
  previous_composite: 28.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/elements/refs/heads/main/screenshots/elements-2026-06-20T180557.png
security:
- kind: domain-security
  name: Elements Domain Security
  slug: elements-domain-security
  summary_line: TLSv1.3 · DMARC
slug: elements
tags:
- API Documentation
- Developer Tools
- Documentation
- Interactive Docs
- OpenAPI
- React
- Web Components
website: https://stoplight.io/open-source/elements
---
