---
access_model:
  confidence: high
  label: Freemium (free trial) · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.3
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 25
  human_in_the_loop: 0
  name: Twenty Agentic Access
  operation_count: 42
  slug: twenty-agentic-access
  summary_line: 42 operations · 25 acting
api_count: 2
apis:
- baseURL: https://api.twenty.com/rest/core
  baseurl_source: spec
  description: Company CRM records
  name: Twenty companies API
  slug: twenty-companies-api
- baseURL: https://api.twenty.com/rest/core
  baseurl_source: spec
  description: Custom field metadata management
  name: Twenty fields API
  slug: twenty-fields-api
- baseURL: https://api.twenty.com/rest/core
  baseurl_source: spec
  description: Note records associated with CRM objects
  name: Twenty notes API
  slug: twenty-notes-api
- baseURL: https://api.twenty.com/rest/core
  baseurl_source: spec
  description: Custom object metadata management
  name: Twenty objects API
  slug: twenty-objects-api
- baseURL: https://api.twenty.com/rest/core
  baseurl_source: spec
  description: OpenAPI schema discovery
  name: Twenty openapi API
  slug: twenty-openapi-api
- baseURL: https://api.twenty.com/rest/core
  baseurl_source: spec
  description: Opportunity/deal CRM records
  name: Twenty opportunities API
  slug: twenty-opportunities-api
- baseURL: https://api.twenty.com/rest/core
  baseurl_source: spec
  description: Person/contact CRM records
  name: Twenty people API
  slug: twenty-people-api
- baseURL: https://api.twenty.com/rest/core
  baseurl_source: spec
  description: Custom relation metadata management
  name: Twenty relations API
  slug: twenty-relations-api
- baseURL: https://api.twenty.com/rest/core
  baseurl_source: spec
  description: Task records associated with CRM objects
  name: Twenty tasks API
  slug: twenty-tasks-api
artifact_total: 35
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Twenty Core companies API
  slug: open-twenty-companies-api
- collection_type: open
  name: Twenty Core companies fields API
  slug: open-twenty-fields-api
- collection_type: open
  name: Twenty Core companies notes API
  slug: open-twenty-notes-api
- collection_type: open
  name: Twenty Core companies objects API
  slug: open-twenty-objects-api
- collection_type: open
  name: Twenty Core companies openapi API
  slug: open-twenty-openapi-api
- collection_type: open
  name: Twenty Core companies opportunities API
  slug: open-twenty-opportunities-api
- collection_type: open
  name: Twenty Core companies people API
  slug: open-twenty-people-api
- collection_type: open
  name: Twenty Core companies relations API
  slug: open-twenty-relations-api
- collection_type: open
  name: Twenty Core companies tasks API
  slug: open-twenty-tasks-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/twenty-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/twenty-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/twenty-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/twenty-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://twenty.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.twenty.com/developers/introduction
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/twentyhq
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/twenty
- group: company
  title: ''
  type: Blog
  url: https://twenty.com/releases
- group: company
  title: ''
  type: BlogRSS
  url: https://github.com/twentyhq/twenty/releases.atom
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/twenty-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/twenty-context.jsonld
- group: commercial
  title: ''
  type: Pricing
  url: https://twenty.com/pricing
- group: other
  title: ''
  type: X
  url: https://x.com/twentycrm
- group: commercial
  title: ''
  type: Plans
  url: plans/twenty-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/twenty-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/twenty-finops.yml
created: 2026-06-12
description: Twenty is an open-source CRM platform built as a modern alternative to Salesforce, designed for teams that need flexibility, data ownership, and a contemporary developer experience. It provides REST and GraphQL APIs covering core CRM operations such as managing companies, people, opportunities, notes, tasks, and fully customizable objects. Developers can extend Twenty with custom objects, server-side logic, UI components, and AI agents as TypeScript packages, all surfaced through the same API surface. The platform is available as a cloud service or as a self-hosted deployment via Docker Compose, giving teams full control over their data residency and infrastructure.
examples:
- key_count: 4
  name: Twenty Create Company
  slug: twenty-create-company
- key_count: 3
  name: Twenty Create Custom Object
  slug: twenty-create-custom-object
- key_count: 4
  name: Twenty List Companies
  slug: twenty-list-companies
finops:
- name: Twenty Finops
  service_category: ''
  slug: twenty-finops
graphqls:
- description: 'Twenty exposes two GraphQL endpoints for every workspace: the Core API at `/graphql` and the Metadata API at `/metadata`. The Core API is schema-per-tenant — the types and fields available at query ti'
  name: Twenty CRM GraphQL API
  slug: twenty-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/twenty.png
json_schemas:
- name: Company
  property_count: 13
  slug: twenty-company
- name: Opportunity
  property_count: 14
  slug: twenty-opportunity
- name: Person
  property_count: 13
  slug: twenty-person
jsonld:
- class_count: 2
  name: Twenty Context
  property_count: 19
  slug: twenty-context
layout: provider
modified: 2026-06-12
name: Twenty
nav: Providers
network: true
overview: 'Twenty publishes 9 APIs on the [APIs.io](https://apis.io/) network, including companies API, fields API, notes API, and 6 more. Tagged areas include CRM, Open-Source, REST, GraphQL, and Webhook.


  The Twenty catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Twenty''s developer surface includes authentication, documentation, engineering blog, pricing, and 13 more developer resources.'
plans:
- name: Twenty Plans Pricing
  plan_count: 3
  slug: twenty-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 5
  name: Twenty Rate Limits
  slug: twenty-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Twenty API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: twenty-jsonschema-spectral-rules
score:
  band: developing
  composite: 46.0
  coverage:
    artifact_dirs: 16
    catalog_gap: 34.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 25.0
    contract_quality: 73.7
    developer_ergonomics: 23.8
    discoverability: 50.0
    governance: 25.0
    operational_transparency: 36.8
  previous_composite: 46.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/twenty/refs/heads/main/screenshots/twenty-2026-06-20T195948.png
security:
- kind: authentication
  name: Twenty Authentication
  slug: twenty-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Twenty Domain Security
  slug: twenty-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Twenty Vulnerability Disclosure
  slug: twenty-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: twenty
tags:
- CRM
- Open-Source
- REST
- GraphQL
- Webhook
- Self-Hosted
- Companies
- People
- Opportunities
- Workflows
- AI Agents
- Custom Objects
website: https://twenty.com
---
