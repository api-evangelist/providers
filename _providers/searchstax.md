---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
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
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.0
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 8
  human_in_the_loop: 1
  name: Searchstax Agentic Access
  operation_count: 17
  slug: searchstax-agentic-access
  summary_line: 17 operations · 8 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: The SearchStax Site Search API returns JSON search results from a SearchStax Studio Site Search application. It provides real-time search via the /emselect endpoint, supporting faceted search, auto-su
  name: SearchStax Site Search API
  slug: searchstax-site-search-api
- baseURL: https://app.searchstax.com/api/rest/v2
  baseurl_source: declared
  description: The Authentication API from SearchStax — 2 operation(s) for authentication.
  name: SearchStax Authentication API
  slug: searchstax-authentication-api
- baseURL: https://app.searchstax.com/api/rest/v2
  baseurl_source: declared
  description: The Backup API from SearchStax — 1 operation(s) for backup.
  name: SearchStax Backup API
  slug: searchstax-backup-api
- baseURL: https://app.searchstax.com/api/rest/v2
  baseurl_source: declared
  description: The Deployments API from SearchStax — 5 operation(s) for deployments.
  name: SearchStax Deployments API
  slug: searchstax-deployments-api
- baseURL: https://app.searchstax.com/api/rest/v2
  baseurl_source: declared
  description: The Nodes API from SearchStax — 4 operation(s) for nodes.
  name: SearchStax Nodes API
  slug: searchstax-nodes-api
- baseURL: https://app.searchstax.com/api/rest/v2
  baseurl_source: declared
  description: The Plans API from SearchStax — 1 operation(s) for plans.
  name: SearchStax Plans API
  slug: searchstax-plans-api
- baseURL: https://app.searchstax.com/api/rest/v2
  baseurl_source: declared
  description: The Usage API from SearchStax — 1 operation(s) for usage.
  name: SearchStax Usage API
  slug: searchstax-usage-api
artifact_total: 28
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: SearchStax Provisioning Authentication API
  slug: open-searchstax-authentication-api
- collection_type: open
  name: SearchStax Provisioning Authentication Backup API
  slug: open-searchstax-backup-api
- collection_type: open
  name: SearchStax Provisioning Authentication Deployments API
  slug: open-searchstax-deployments-api
- collection_type: open
  name: SearchStax Provisioning Authentication Nodes API
  slug: open-searchstax-nodes-api
- collection_type: open
  name: SearchStax Provisioning Authentication Plans API
  slug: open-searchstax-plans-api
- collection_type: open
  name: SearchStax Provisioning API
  slug: open-searchstax-provisioning
- collection_type: open
  name: SearchStax Provisioning Authentication Usage API
  slug: open-searchstax-usage-api
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
random_paper: 7
rate_limits:
- limit_count: 5
  name: Searchstax Rate Limits
  slug: searchstax-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: SearchStax API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: searchstax-jsonschema-spectral-rules
- effective_rule_count: 49
  extends:
  - spectral:oas
  name: SearchStax API Rules
  rule_count: 8
  severity_counts:
    error: 2
    hint: 0
    info: 2
    warn: 4
  slug: searchstax-rules
score:
  band: thin
  composite: 37.2
  coverage:
    artifact_dirs: 16
    catalog_earned: 63.5
    catalog_earned_first_party: 0.0
    catalog_gap: 51.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 28.8
    contract_quality: 62.8
    developer_ergonomics: 23.8
    discoverability: 68.5
    governance: 28.8
    operational_transparency: 13.2
  previous_composite: 37.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.18.3
  scored_at: '2026-09-05'
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
