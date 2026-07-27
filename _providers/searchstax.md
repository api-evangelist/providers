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
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: true
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 54.8
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 8
  human_in_the_loop: 1
  name: Searchstax Agentic Access
  operation_count: 17
  slug: searchstax-agentic-access
  summary_line: 17 operations · 8 acting · 1 human-in-the-loop
api_count: 7
apis:
- description: The SearchStax Site Search API returns JSON search results from a SearchStax Studio Site Search application. It provides real-time search via the /emselect endpoint, supporting faceted search, auto-su
  name: SearchStax Site Search API
  slug: searchstax-site-search-api
- description: The Authentication API from SearchStax — 2 operation(s) for authentication.
  name: SearchStax Authentication API
  slug: searchstax-authentication-api
- description: The Backup API from SearchStax — 1 operation(s) for backup.
  name: SearchStax Backup API
  slug: searchstax-backup-api
- description: The Deployments API from SearchStax — 5 operation(s) for deployments.
  name: SearchStax Deployments API
  slug: searchstax-deployments-api
- description: The Nodes API from SearchStax — 4 operation(s) for nodes.
  name: SearchStax Nodes API
  slug: searchstax-nodes-api
- description: The Plans API from SearchStax — 1 operation(s) for plans.
  name: SearchStax Plans API
  slug: searchstax-plans-api
- description: The Usage API from SearchStax — 1 operation(s) for usage.
  name: SearchStax Usage API
  slug: searchstax-usage-api
artifact_total: 21
collections:
- collection_type: open
  name: SearchStax Provisioning API
  slug: open-searchstax-provisioning
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/searchstax-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/searchstax-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/searchstax-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/searchstax-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/searchstax
- group: company
  title: ''
  type: Website
  url: https://www.searchstax.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.searchstax.com/docs/hc/searchstax-api-library/
- group: docs
  title: ''
  type: Documentation
  url: https://www.searchstax.com/docs/searchstax-cloud-apis-overview/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/searchstax
- group: docs
  title: ''
  type: Documentation
  url: https://www.searchstax.com/docs/searchstax-cloud-deployment-api/
- group: docs
  title: ''
  type: Documentation
  url: https://www.searchstax.com/docs/searchstax-cloud-backup-restore-api/
- group: docs
  title: ''
  type: Documentation
  url: https://www.searchstax.com/docs/searchstax-cloud-authentication-api/
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/searchstax-deployment-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/searchstax-deployment-structure.json
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/searchstax-context.jsonld
- group: build
  title: ''
  type: Examples
  url: examples/searchstax-list-deployments-example.json
- group: design
  title: ''
  type: SpectralRuleset
  url: rules/searchstax-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/searchstax-vocabulary.yml
- group: company
  title: ''
  type: Blog
  url: https://www.searchstax.com/blog/
created: '2026-05-02'
description: SearchStax is a managed Solr search infrastructure company that provides cloud-hosted Apache Solr deployments and a Site Search platform. SearchStax eliminates the complexity of running and scaling Solr by offering fully managed dedicated and serverless deployments on AWS, Azure, and Google Cloud. The platform exposes a comprehensive REST Provisioning API for managing deployments, backup and restore, authentication, webhooks, and infrastructure configuration, along with a Site Search API for delivering search results from SearchStax Studio applications.
examples:
- key_count: 2
  name: Searchstax List Deployments Example
  slug: searchstax-list-deployments-example
finops:
- name: Searchstax Finops
  service_category: API
  slug: searchstax-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/searchstax.png
json_schemas:
- name: SearchStax Deployment
  property_count: 13
  slug: searchstax-deployment
json_structures:
- name: Searchstax Deployment Structure
  property_count: 12
  slug: searchstax-deployment-structure
jsonld:
- class_count: 22
  name: Searchstax Context
  property_count: 1
  slug: searchstax-context
layout: provider
modified: '2026-05-19'
name: SearchStax
nav: Providers
network: true
overview: 'SearchStax publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Backup API, Deployments API, and 3 more. Tagged areas include Search, Solr, Managed Search, Search Infrastructure, and Full-Text Search.


  The SearchStax catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  SearchStax''s developer surface includes authentication, documentation, code examples, engineering blog, and 15 more developer resources.'
plans:
- name: Searchstax Plans Pricing
  plan_count: 3
  slug: searchstax-plans-pricing
random_paper: 58
rate_limits:
- limit_count: 5
  name: Searchstax Rate Limits
  slug: searchstax-rate-limits
rules:
- name: SearchStax API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: searchstax-jsonschema-spectral-rules
- name: SearchStax API Rules
  rule_count: 8
  severity_counts:
    error: 2
    hint: 0
    info: 2
    warn: 4
  slug: searchstax-rules
score:
  band: developing
  composite: 54.8
  delta: 3.3
  facets:
    commercial_clarity: 47.4
    contract_quality: 63.1
    developer_ergonomics: 21.7
    discoverability: 100.0
    governance: 86.8
    operational_transparency: 36.8
  previous_composite: 51.5
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/searchstax/refs/heads/main/screenshots/searchstax-2026-06-20T193615.png
security:
- kind: authentication
  name: Searchstax Authentication
  slug: searchstax-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Searchstax Domain Security
  slug: searchstax-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: trust-center
  name: Searchstax Trust Center
  slug: searchstax-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, HIPAA, GDPR, CSA STAR
slug: searchstax
tags:
- Search
- Solr
- Managed Search
- Search Infrastructure
- Full-Text Search
- Site Search
website: https://www.searchstax.com
---
