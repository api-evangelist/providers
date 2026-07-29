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
- description: REST Client is a Visual Studio Code extension for sending HTTP requests and viewing responses directly within the editor. It supports .http and .rest file formats, GraphQL, cURL, multiple auth schemes
  name: REST Client
  slug: rest-client
artifact_total: 12
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rest-client-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://marketplace.visualstudio.com/items?itemName=humao.rest-client
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/Huachao/vscode-restclient#readme
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Huachao/vscode-restclient
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/rest-client/refs/heads/main/vocabulary/rest-client-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/rest-client/refs/heads/main/json-ld/rest-client-context.jsonld
created: '2026-03-27'
description: REST Client is a Visual Studio Code extension developed by Huachao Mao that enables developers to send HTTP requests and view responses directly within the VS Code editor. It supports RFC 2616 HTTP request format using .http and .rest files, GraphQL queries, cURL commands, multiple authentication schemes (Basic, Digest, SSL Client Certificates, Azure AD, AWS Signature v4, AWS Cognito), environment and file variables, request chaining, cookie management, code generation to multiple languages, and response saving. The extension is installed via the VS Code Marketplace under the identifier humao.rest-client and is widely used as a lightweight alternative to dedicated API clients like Postman and Insomnia.
examples:
- key_count: 5
  name: Rest Client Get Request Example
  slug: rest-client-get-request-example
- key_count: 4
  name: Rest Client Request Chaining Example
  slug: rest-client-request-chaining-example
finops:
- name: Rest Client Finops
  service_category: API
  slug: rest-client-finops
graphqls:
- description: REST Client is a Visual Studio Code extension for sending HTTP requests and viewing responses directly within the editor. It supports .http and .rest file formats, GraphQL, cURL, multiple auth schemes
  name: REST Client GraphQL API
  slug: rest-client-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rest-client.png
json_schemas:
- name: REST Client HTTP Request
  property_count: 9
  slug: rest-client-request
json_structures:
- name: Rest Client Request Structure
  property_count: 0
  slug: rest-client-request-structure
jsonld:
- class_count: 8
  name: Rest Client Context
  property_count: 13
  slug: rest-client-context
layout: provider
modified: '2026-05-02'
name: REST Client
nav: Providers
network: true
overview: 'REST Client publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Clients, HTTP Client, IDE Extension, VS Code, and API Testing.


  The REST Client catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  REST Client''s developer surface includes documentation and 5 more developer resources.'
plans:
- name: Rest Client Plans Pricing
  plan_count: 3
  slug: rest-client-plans-pricing
random_paper: 77
rate_limits:
- limit_count: 5
  name: Rest Client Rate Limits
  slug: rest-client-rate-limits
rules:
- name: REST Client API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: rest-client-jsonschema-spectral-rules
score:
  band: thin
  composite: 35.5
  delta: -5.4
  facets:
    commercial_clarity: 39.5
    contract_quality: 27.4
    developer_ergonomics: 8.7
    discoverability: 59.3
    governance: 68.8
    operational_transparency: 36.8
  previous_composite: 40.9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/rest-client/refs/heads/main/screenshots/rest-client-2026-06-20T193111.png
security:
- kind: domain-security
  name: Rest Client Domain Security
  slug: rest-client-domain-security
  summary_line: TLSv1.3
slug: rest-client
tags:
- Clients
- HTTP Client
- IDE Extension
- VS Code
- API Testing
website: https://marketplace.visualstudio.com/items?itemName=humao.rest-client
---
