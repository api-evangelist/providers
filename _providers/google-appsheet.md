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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Google Appsheet Agentic Access
  operation_count: 1
  slug: google-appsheet-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- description: The Apps API from Google AppSheet — 1 operation(s) for apps.
  name: Google AppSheet Apps API
  slug: google-appsheet-apps-api
artifact_total: 12
collections:
- collection_type: open
  name: Google AppSheet API
  slug: open-openapi
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-appsheet-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-appsheet-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-appsheet-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/google-appsheet-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/appsheet
- group: start
  title: ''
  type: GettingStarted
  url: https://support.google.com/appsheet/answer/10105398
- group: commercial
  title: ''
  type: Pricing
  url: https://workspace.google.com/products/appsheet/pricing/
- group: design
  title: ''
  type: JSONLD
  url: json-ld/context.jsonld
created: '2026-03-13'
description: The Google AppSheet API enables programmatic access to AppSheet applications, allowing developers to add, update, delete, and find records in AppSheet tables, as well as invoke predefined AppSheet actions via a REST interface.
finops:
- name: Google Appsheet Finops
  service_category: API
  slug: google-appsheet-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-appsheet.png
json_schemas:
- name: Google AppSheet Action Request
  property_count: 3
  slug: ActionRequest
jsonld:
- class_count: 11
  name: context Context
  property_count: 0
  slug: context
layout: provider
modified: '2026-05-19'
name: Google AppSheet
nav: Providers
network: true
overview: 'Google AppSheet publishes 1 API on the [APIs.io](https://apis.io/) network: Apps API. Tagged areas include Applications, Data, Google, Low-Code, and No-Code.


  The Google AppSheet catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Google AppSheet''s developer surface includes authentication, getting-started guide, pricing, and 5 more developer resources.'
plans:
- name: Google Appsheet Plans Pricing
  plan_count: 3
  slug: google-appsheet-plans-pricing
random_paper: 64
rate_limits:
- limit_count: 5
  name: Google Appsheet Rate Limits
  slug: google-appsheet-rate-limits
rules:
- name: Google AppSheet API Rules
  rule_count: 4
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 3
  slug: google-appsheet-jsonschema-spectral-rules
score:
  band: developing
  composite: 50.7
  delta: -4.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 73.7
    developer_ergonomics: 21.7
    discoverability: 68.5
    governance: 58.3
    operational_transparency: 31.6
  previous_composite: 54.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-appsheet/refs/heads/main/screenshots/google-appsheet-2026-06-20T182019.png
security:
- kind: authentication
  name: Google Appsheet Authentication
  slug: google-appsheet-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Google Appsheet Domain Security
  slug: google-appsheet-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Google Appsheet Vulnerability Disclosure
  slug: google-appsheet-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-appsheet
tags:
- Applications
- Data
- Google
- Low-Code
- No-Code
- Tables
---
