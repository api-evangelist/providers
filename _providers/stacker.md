---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.1
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Stacker Agentic Access
  operation_count: 10
  slug: stacker-agentic-access
  summary_line: 10 operations · 5 acting
api_count: 4
apis:
- description: Manage Stacker accounts
  name: Stacker Accounts API
  slug: stacker-accounts-api
- description: Health check and connectivity test
  name: Stacker Hello API
  slug: stacker-hello-api
- description: Manage objects (tables) within a stack
  name: Stacker Objects API
  slug: stacker-objects-api
- description: CRUD operations on records within an object
  name: Stacker Records API
  slug: stacker-records-api
artifact_total: 24
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Stacker Accounts API
  slug: open-stacker-accounts-api
- collection_type: open
  name: Stacker Accounts Hello API
  slug: open-stacker-hello-api
- collection_type: open
  name: Stacker Accounts Objects API
  slug: open-stacker-objects-api
- collection_type: open
  name: Stacker Accounts Records API
  slug: open-stacker-records-api
- collection_type: open
  name: Stacker API
  slug: open-stacker
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/stacker-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/stacker-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/stacker-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/stackermedia
- group: company
  title: ''
  type: Website
  url: https://stacker.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.stackerhq.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.stackerhq.com/stacker/ai-and-automations/open-api-overview
- group: auth
  title: ''
  type: Authentication
  url: https://docs.stackerhq.com/stacker/ai-and-automations/open-api-overview/authentication
- group: commercial
  title: ''
  type: Pricing
  url: https://stacker.ai/pricing
- group: company
  title: ''
  type: Blog
  url: https://stacker.ai/blog
- group: start
  title: ''
  type: Login
  url: https://app.stackerhq.com/
- group: agent
  title: ''
  type: LlmsText
  url: https://api.go.stackerhq.com/llms.txt
created: '2025-01-01'
description: Stacker is a no-code platform that enables organizations to build custom business applications, internal tools, and customer portals on top of their existing data sources — including Airtable, Google Sheets, SQL databases, and Salesforce — without writing code. Its drag-and-drop interface, role-based access controls, and Open API enable teams to create data-driven portals, automate workflows, and integrate with third-party services.
examples:
- key_count: 4
  name: Stacker Create Record Example
  slug: stacker-create-record-example
- key_count: 4
  name: Stacker Search Records Example
  slug: stacker-search-records-example
finops:
- name: Stacker Finops
  service_category: API
  slug: stacker-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/stacker.png
json_schemas:
- name: Stacker Record
  property_count: 1
  slug: stacker-record
- name: Stacker Search Request
  property_count: 7
  slug: stacker-search-request
json_structures:
- name: Stacker Record Structure
  property_count: 0
  slug: stacker-record-structure
jsonld:
- class_count: 10
  name: Stacker Context
  property_count: 3
  slug: stacker-context
layout: provider
modified: '2026-05-19'
name: Stacker
nav: Providers
network: true
overview: 'Stacker publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Hello API, Objects API, and 1 more. Tagged areas include Application Development, Low-Code, No-Code, Portal, and Workflow-Automation.


  The Stacker catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Stacker''s developer surface includes authentication, documentation, getting-started guide, pricing, engineering blog, and 7 more developer resources.'
plans:
- name: Stacker Plans Pricing
  plan_count: 3
  slug: stacker-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 5
  name: Stacker Rate Limits
  slug: stacker-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Stacker API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: stacker-jsonschema-spectral-rules
- effective_rule_count: 7
  extends: []
  name: Stacker API Rules
  rule_count: 7
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 4
  slug: stacker-rules
score:
  band: thin
  composite: 38.7
  delta: 0.0
  facets:
    access_clarity: 32.9
    commercial_clarity: 32.9
    contract_governance: 9.8
    contract_quality: 61.4
    developer_ergonomics: 35.7
    discoverability: 74.1
    governance: 9.8
    operational_transparency: 7.9
  previous_composite: 38.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/stacker/refs/heads/main/screenshots/stacker-2026-06-20T194549.png
security:
- kind: authentication
  name: Stacker Authentication
  slug: stacker-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Stacker Domain Security
  slug: stacker-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: stacker
tags:
- Application Development
- Low-Code
- No-Code
- Portal
- Workflow-Automation
website: https://stacker.ai/
---
