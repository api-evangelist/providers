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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Amazon Opensearch Service Agentic Access
  operation_count: 5
  slug: amazon-opensearch-service-agentic-access
  summary_line: 5 operations · 3 acting
api_count: 1
apis:
- description: Operations for creating and managing OpenSearch domains
  name: Amazon OpenSearch Service Domains API
  slug: amazon-opensearch-service-domains-api
arazzos:
- description: Enumerate domains, bulk-describe them, and drill into a single target domain's status.
  name: Amazon OpenSearch Service Audit Domain Fleet Readiness
  slug: amazon-opensearch-service-audit-domain-readiness-workflow
- description: Read a source domain's engine version and create a new domain that matches it.
  name: Amazon OpenSearch Service Clone a Domain Engine Version
  slug: amazon-opensearch-service-clone-domain-engine-version-workflow
- description: Confirm a domain exists, delete it, and poll until the deletion completes.
  name: Amazon OpenSearch Service Decommission a Domain
  slug: amazon-opensearch-service-decommission-domain-workflow
- description: Create a domain only when it is not already present in the account.
  name: Amazon OpenSearch Service Ensure Domain Exists
  slug: amazon-opensearch-service-ensure-domain-exists-workflow
- description: List every domain name in the account and fetch full configuration details for all of them.
  name: Amazon OpenSearch Service Inventory All Domains
  slug: amazon-opensearch-service-inventory-domains-workflow
- description: Create an OpenSearch domain and poll its status until the search endpoint is live.
  name: Amazon OpenSearch Service Provision Domain and Confirm Endpoint
  slug: amazon-opensearch-service-provision-domain-workflow
artifact_total: 32
collections:
- collection_type: postman
  name: Amazon OpenSearch Service API
  slug: postman-amazon-opensearch-service
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Amazon OpenSearch Service Domains API
  slug: open-amazon-opensearch-service-domains-api
- collection_type: open
  name: Amazon OpenSearch Service API
  slug: open-amazon-opensearch-service
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-opensearch-service-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-opensearch-service-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-opensearch-service-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-opensearch-service-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-opensearch-service-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-opensearch-service/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-opensearch-service-audit-domain-readiness-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-opensearch-service-clone-domain-engine-version-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-opensearch-service-decommission-domain-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-opensearch-service-ensure-domain-exists-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-opensearch-service-inventory-domains-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-opensearch-service-provision-domain-workflow.yml
- group: company
  title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/big-data/category/analytics/amazon-opensearch-service/
- group: operate
  title: ''
  type: Support
  url: https://aws.amazon.com/premiumsupport/
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/aos/home
- group: docs
  title: ''
  type: CLI Reference
  url: https://docs.aws.amazon.com/cli/latest/reference/opensearch/
- group: build
  title: ''
  type: SDKs
  url: https://aws.amazon.com/tools/
- group: operate
  title: ''
  type: Service Status
  url: https://status.aws.amazon.com/
- group: auth
  title: ''
  type: Compliance
  url: https://aws.amazon.com/compliance/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- group: company
  title: ''
  type: Website
  url: https://aws.amazon.com/opensearch-service/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/opensearch-service/
- group: commercial
  title: ''
  type: Pricing
  url: https://aws.amazon.com/opensearch-service/pricing/
- group: start
  title: ''
  type: GettingStarted
  url: https://aws.amazon.com/opensearch-service/getting-started/
- group: operate
  title: ''
  type: FAQ
  url: https://aws.amazon.com/opensearch-service/faqs/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
- group: start
  title: ''
  type: Signup
  url: https://portal.aws.amazon.com/billing/signup
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/amazon-opensearch
- group: build
  title: ''
  type: Code Examples
  url: https://docs.aws.amazon.com/code-library/latest/ug/opensearch_code_examples.html
- group: design
  title: ''
  type: SpectralRules
  url: rules/amazon-opensearch-service-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-opensearch-service-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/amazon-opensearch-service-context.jsonld
- group: design
  title: ''
  type: JSONLD
  url: json-ld/amazon-opensearch-service-openapi-context.jsonld
- group: docs
  title: Amazon Opensearch Service
  type: JSONSchema
  url: json-schema/amazon-opensearch-service-schema.json
- group: docs
  title: Openapi Create Domain Request
  type: JSONSchema
  url: json-schema/openapi-create-domain-request-schema.json
- group: docs
  title: Openapi Domain Status
  type: JSONSchema
  url: json-schema/openapi-domain-status-schema.json
created: '2024-01-15'
description: Amazon OpenSearch Service is a managed service that makes it easy to deploy, operate, and scale OpenSearch clusters for log analytics, full-text search, application monitoring, and more.
examples:
- key_count: 15
  name: Amazon Opensearch Service Example
  slug: amazon-opensearch-service-example
- key_count: 5
  name: Openapi Create Domain Request Example
  slug: openapi-create-domain-request-example
- key_count: 7
  name: Openapi Domain Status Example
  slug: openapi-domain-status-example
finops:
- name: Amazon Opensearch Service Finops
  service_category: API
  slug: amazon-opensearch-service-finops
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
json_schemas:
- name: Amazon OpenSearch Service Domain Definition
  property_count: 20
  slug: amazon-opensearch-service
- name: CreateDomainRequest
  property_count: 5
  slug: openapi-create-domain-request
- name: DomainStatus
  property_count: 7
  slug: openapi-domain-status
json_structures:
- name: Amazon Opensearch Service Structure
  property_count: 20
  slug: amazon-opensearch-service-structure
- name: Openapi Create Domain Request Structure
  property_count: 5
  slug: openapi-create-domain-request-structure
- name: Openapi Domain Status Structure
  property_count: 7
  slug: openapi-domain-status-structure
jsonld:
- class_count: 0
  name: Amazon Opensearch Service Context
  property_count: 3
  slug: amazon-opensearch-service-context
- class_count: 2
  name: Amazon Opensearch Service Openapi Context
  property_count: 10
  slug: amazon-opensearch-service-openapi-context
layout: provider
modified: '2026-05-19'
name: Amazon OpenSearch Service
nav: Providers
network: true
overview: 'Amazon OpenSearch Service publishes 1 API on the [APIs.io](https://apis.io/) network: Domains API. Tagged areas include Analytics, Elasticsearch, Full-Text Search, Log Analytics, and OpenSearch.


  The Amazon OpenSearch Service catalog on APIs.io includes 2 JSON-LD contexts and 2 Spectral governance rulesets.


  Amazon OpenSearch Service''s developer surface includes authentication, engineering blog, support, developer console, documentation, pricing, getting-started guide, and 30 more developer resources.'
plans:
- name: Amazon Opensearch Service Plans Pricing
  plan_count: 3
  slug: amazon-opensearch-service-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 5
  name: Amazon Opensearch Service Rate Limits
  slug: amazon-opensearch-service-rate-limits
rules:
- name: Amazon OpenSearch Service API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: amazon-opensearch-service-jsonschema-spectral-rules
- name: Amazon OpenSearch Service API Rules
  rule_count: 24
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 13
  slug: amazon-opensearch-service-spectral-rules
score:
  band: strong
  composite: 60.6
  delta: 0.0
  facets:
    commercial_clarity: 76.3
    contract_quality: 71.3
    developer_ergonomics: 54.3
    discoverability: 66.7
    governance: 68.8
    operational_transparency: 13.2
  previous_composite: 60.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-opensearch-service/refs/heads/main/screenshots/amazon-opensearch-service-2026-06-20T171751.png
security:
- kind: authentication
  name: Amazon Opensearch Service Authentication
  slug: amazon-opensearch-service-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Opensearch Service Domain Security
  slug: amazon-opensearch-service-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Opensearch Service Vulnerability Disclosure
  slug: amazon-opensearch-service-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Opensearch Service Trust Center
  slug: amazon-opensearch-service-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-opensearch-service
tags:
- Analytics
- Elasticsearch
- Full-Text Search
- Log Analytics
- OpenSearch
- Search
website: https://aws.amazon.com/opensearch-service/
---
