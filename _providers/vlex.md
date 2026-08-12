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
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Vlex Agentic Access
  operation_count: 7
  slug: vlex-agentic-access
  summary_line: 7 operations · 6 acting
api_count: 6
apis:
- description: Single sign-on authentication API for corporate vLex accounts. Generates redirect URLs using HMAC authentication for seamless user access to vLex.com from institutional portals.
  name: vLex Remote Authentication API
  slug: remote-auth-api
- description: Identify and anonymize personally identifiable information in text
  name: vLex Anonymization API
  slug: vlex-anonymization-api
- description: Detect and resolve legal citations (vCite)
  name: vLex Citations API
  slug: vlex-citations-api
- description: Classify legal documents and extract key phrases
  name: vLex Classification API
  slug: vlex-classification-api
- description: Retrieve individual legal documents
  name: vLex Documents API
  slug: vlex-documents-api
- description: Search the vLex legal document corpus
  name: vLex Search API
  slug: vlex-search-api
artifact_total: 21
collections:
- collection_type: open
  name: vLex Iceberg Anonymization API
  slug: open-vlex-iceberg-anonymization
- collection_type: open
  name: vLex Iceberg Legal Research API
  slug: open-vlex-iceberg-legal-research
common:
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
overview: 'vLex publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Anonymization API, Citations API, Classification API, and 2 more. Tagged areas include AI, Classification, Legal Research, Legal Tech, and Natural Language Processing.


  The vLex catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  vLex''s developer surface includes authentication, documentation, support, engineering blog, and 9 more developer resources.'
plans:
- name: Vlex Plans Pricing
  plan_count: 1
  slug: vlex-plans-pricing
random_paper: 99
rate_limits:
- limit_count: 1
  name: Vlex Rate Limits
  slug: vlex-rate-limits
rules:
- name: vLex API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: vlex-jsonschema-spectral-rules
- name: vLex API Rules
  rule_count: 8
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 5
  slug: vlex-rules
score:
  band: developing
  composite: 45.3
  delta: -5.9
  facets:
    commercial_clarity: 21.1
    contract_quality: 71.8
    developer_ergonomics: 41.3
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 10.5
  previous_composite: 51.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
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
- AI
- Classification
- Legal Research
- Legal Tech
- Natural Language Processing
- Privacy
website: https://vlex.com/
---
