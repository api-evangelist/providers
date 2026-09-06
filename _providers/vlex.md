---
access_model:
  confidence: high
  label: Enterprise (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
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
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Vlex Agentic Access
  operation_count: 7
  slug: vlex-agentic-access
  summary_line: 7 operations · 6 acting
api_count: 2
apis:
- description: Single sign-on authentication API for corporate vLex accounts. Generates redirect URLs using HMAC authentication for seamless user access to vLex.com from institutional portals.
  name: vLex Remote Authentication API
  slug: remote-auth-api
- baseURL: https://api.vlex.com
  baseurl_source: spec
  description: Identify and anonymize personally identifiable information in text
  name: vLex Anonymization API
  slug: vlex-anonymization-api
- baseURL: https://api.vlex.com
  baseurl_source: spec
  description: Detect and resolve legal citations (vCite)
  name: vLex Citations API
  slug: vlex-citations-api
- baseURL: https://api.vlex.com
  baseurl_source: spec
  description: Classify legal documents and extract key phrases
  name: vLex Classification API
  slug: vlex-classification-api
- baseURL: https://api.vlex.com
  baseurl_source: spec
  description: Retrieve individual legal documents
  name: vLex Documents API
  slug: vlex-documents-api
- baseURL: https://api.vlex.com
  baseurl_source: spec
  description: Search the vLex legal document corpus
  name: vLex Search API
  slug: vlex-search-api
artifact_total: 27
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: vLex Iceberg Anonymization API
  slug: open-vlex-anonymization-api
- collection_type: open
  name: vLex Iceberg Anonymization Citations API
  slug: open-vlex-citations-api
- collection_type: open
  name: vLex Iceberg Anonymization Classification API
  slug: open-vlex-classification-api
- collection_type: open
  name: vLex Iceberg Anonymization Documents API
  slug: open-vlex-documents-api
- collection_type: open
  name: vLex Iceberg Anonymization API
  slug: open-vlex-iceberg-anonymization
- collection_type: open
  name: vLex Iceberg Legal Research API
  slug: open-vlex-iceberg-legal-research
- collection_type: open
  name: vLex Iceberg Anonymization Search API
  slug: open-vlex-search-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/vlex/remote_auth/issues
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/vlex-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/vlex-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vlex-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/vlex-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/vlex
- group: company
  title: ''
  type: Website
  url: https://vlex.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.vlex.com/
- group: docs
  title: ''
  type: Reference
  url: https://developer.vlex.com/apis
- group: docs
  title: ''
  type: Documentation
  url: https://vlex.com/iceberg-ai
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/vlex
- group: other
  title: ''
  type: Product
  url: https://vlex.com/products/fastcase
- group: operate
  title: ''
  type: Support
  url: https://support.vlex.com/
- group: company
  title: ''
  type: Blog
  url: https://vlex.com/news
created: '2025-03-01'
description: vLex (part of Clio) is a global legal intelligence platform that applies AI to ingest, enrich, classify, and deliver insights from over 100 million legal documents across 2,000+ multilingual sources. The vLex Iceberg platform provides REST APIs for legal document anonymization, classification, key phrase extraction, citation detection, and AI-powered legal research. vLex also offers the Fastcase Legal Data API for raw legal data feeds.
examples:
- key_count: 5
  name: Vlex Iceberg Anonymization Anonymize Text Example
  slug: vlex-iceberg-anonymization-anonymize-text-example
finops:
- name: Vlex Finops
  service_category: Legal Research / Legal AI
  slug: vlex-finops
image: https://vlex.com/hubfs/vlex-logo.svg
json_schemas:
- name: vLex Legal Document
  property_count: 10
  slug: vlex-legal-document
json_structures:
- name: Vlex Legal Document Structure
  property_count: 0
  slug: vlex-legal-document-structure
jsonld:
- class_count: 11
  name: Vlex Context
  property_count: 23
  slug: vlex-context
layout: provider
modified: '2026-05-19'
name: vLex
nav: Providers
network: true
overview: 'vLex publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Anonymization API, Citations API, Classification API, and 2 more. Tagged areas include Artificial Intelligence, Classification, Legal Research, Legal Tech, and Natural Language Processing.


  The vLex catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  vLex''s developer surface includes authentication, documentation, support, engineering blog, and 10 more developer resources.'
plans:
- name: Vlex Plans Pricing
  plan_count: 1
  slug: vlex-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 1
  name: Vlex Rate Limits
  slug: vlex-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: vLex API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: vlex-jsonschema-spectral-rules
- effective_rule_count: 49
  extends:
  - spectral:oas
  name: vLex API Rules
  rule_count: 8
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 5
  slug: vlex-rules
score:
  band: thin
  composite: 38.8
  coverage:
    artifact_dirs: 16
    catalog_earned: 54.5
    catalog_earned_first_party: 0.0
    catalog_gap: 60.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 13.6
    contract_quality: 66.3
    developer_ergonomics: 45.2
    discoverability: 59.3
    governance: 13.6
    operational_transparency: 10.5
  previous_composite: 38.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/vlex/refs/heads/main/screenshots/vlex-2026-06-20T201112.png
security:
- kind: authentication
  name: Vlex Authentication
  slug: vlex-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Vlex Domain Security
  slug: vlex-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Vlex Trust Center
  slug: vlex-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: vlex
tags:
- Artificial Intelligence
- Classification
- Legal Research
- Legal Tech
- Natural Language Processing
- Privacy
website: https://vlex.com/
---
