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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Google Cloud Document Ai Agentic Access
  operation_count: 5
  slug: google-cloud-document-ai-agentic-access
  summary_line: 5 operations · 3 acting
api_count: 1
apis:
- description: The Projects API from Google Cloud Document AI — 4 operation(s) for projects.
  name: Google Cloud Document AI Projects API
  slug: google-cloud-document-ai-projects-api
artifact_total: 14
collections:
- collection_type: postman
  name: Google Cloud Document AI Projects API
  slug: postman-google-cloud-document-ai-projects-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Google Cloud Document AI Projects API
  slug: open-google-cloud-document-ai-projects-api
- collection_type: open
  name: Google Cloud Document AI API
  slug: open-openapi
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/google-cloud-document-ai/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-cloud-document-ai-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-cloud-document-ai-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-cloud-document-ai-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GoogleCloudPlatform
- group: start
  title: ''
  type: Portal
  url: https://cloud.google.com/document-ai
- group: start
  title: ''
  type: GettingStarted
  url: https://cloud.google.com/document-ai/docs/overview
- group: docs
  title: ''
  type: Documentation
  url: https://cloud.google.com/document-ai/docs
- group: auth
  title: ''
  type: Authentication
  url: https://cloud.google.com/document-ai/docs/authentication
- group: commercial
  title: ''
  type: Pricing
  url: https://cloud.google.com/document-ai/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cloud.google.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://policies.google.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cloud.google.com/
- group: operate
  title: ''
  type: Support
  url: https://cloud.google.com/document-ai/docs/support
- group: design
  title: ''
  type: JSONLD
  url: json-ld/context.jsonld
created: '2026-03-13'
description: Google Cloud Document AI uses machine learning to automatically classify, extract, and enrich data from documents. It processes scanned and digital documents including forms, invoices, receipts, and contracts, transforming unstructured content into structured, actionable data.
finops:
- name: Google Cloud Document Ai Finops
  service_category: API
  slug: google-cloud-document-ai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-cloud-document-ai.png
json_schemas:
- name: Document Processing Request
  property_count: 4
  slug: document-processing
jsonld:
- class_count: 13
  name: context Context
  property_count: 0
  slug: context
layout: provider
modified: '2026-05-19'
name: Google Cloud Document AI
nav: Providers
network: true
overview: 'Google Cloud Document AI publishes 1 API on the [APIs.io](https://apis.io/) network: Projects API. Tagged areas include Data Extraction, Document Processing, Forms, Google Cloud, and Machine Learning.


  The Google Cloud Document AI catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Google Cloud Document AI''s developer surface includes developer portal, getting-started guide, documentation, authentication, pricing, support, and 9 more developer resources.'
plans:
- name: Google Cloud Document Ai Plans Pricing
  plan_count: 3
  slug: google-cloud-document-ai-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 5
  name: Google Cloud Document Ai Rate Limits
  slug: google-cloud-document-ai-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Google Cloud Document AI API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: google-cloud-document-ai-jsonschema-spectral-rules
score:
  band: developing
  composite: 44.8
  delta: -8.1
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 9.8
    contract_quality: 62.9
    developer_ergonomics: 40.5
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 26.3
  previous_composite: 52.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/google-cloud-document-ai/refs/heads/main/screenshots/google-cloud-document-ai-2026-06-20T182108.png
security:
- kind: domain-security
  name: Google Cloud Document Ai Domain Security
  slug: google-cloud-document-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Cloud Document Ai Vulnerability Disclosure
  slug: google-cloud-document-ai-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-cloud-document-ai
tags:
- Data Extraction
- Document Processing
- Forms
- Google Cloud
- Machine Learning
- OCR
website: https://cloud.google.com/document-ai
---
