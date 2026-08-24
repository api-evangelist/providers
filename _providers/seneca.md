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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-24'
api_count: 1
apis:
- description: Seneca is a microservices toolkit for Node.js that uses a pattern-matching approach to message handling. It provides transport independence, allowing services to communicate over HTTP, TCP, or message
  name: Seneca
  slug: seneca
artifact_total: 7
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/senecajs/seneca/blob/master/LICENSE
- group: auth
  title: ''
  type: DomainSecurity
  url: security/seneca-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://senecajs.org/
- group: start
  title: ''
  type: GettingStarted
  url: https://senecajs.org/getting-started/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/senecajs
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/senecajs/seneca
- group: build
  title: ''
  type: Plugins
  url: https://senecajs.org/plugins/
created: '2026-03-26'
description: Seneca is a microservices toolkit for Node.js that uses a pattern-matching approach to message handling. It provides transport independence, allowing services to communicate over HTTP, TCP, or message queues without changing business logic. Seneca emphasizes simplicity and composability through its plugin-based architecture.
finops:
- name: Seneca Finops
  service_category: API
  slug: seneca-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/seneca.png
json_schemas:
- name: Seneca Configuration
  property_count: 8
  slug: seneca-configuration
layout: provider
modified: '2026-03-26'
name: Seneca
nav: Providers
network: true
overview: 'Seneca publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Frameworks, JavaScript, Message Handling, Microservices, and Node.js.


  The Seneca catalog on APIs.io includes 1 Spectral governance ruleset.


  Seneca''s developer surface includes getting-started guide and 6 more developer resources.'
plans:
- name: Seneca Plans Pricing
  plan_count: 3
  slug: seneca-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 5
  name: Seneca Rate Limits
  slug: seneca-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Seneca API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: seneca-jsonschema-spectral-rules
score:
  band: emerging
  composite: 16.1
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 9.8
    contract_quality: 8.5
    developer_ergonomics: 11.9
    discoverability: 59.3
    governance: 9.8
    operational_transparency: 10.5
  previous_composite: 16.1
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/seneca/refs/heads/main/screenshots/seneca-2026-06-20T193656.png
security:
- kind: domain-security
  name: Seneca Domain Security
  slug: seneca-domain-security
  summary_line: TLSv1.3
slug: seneca
tags:
- Frameworks
- JavaScript
- Message Handling
- Microservices
- Node.js
- Pattern Matching
- Plugins
website: https://senecajs.org/
---
