---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.9
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Comeet Agentic Access
  operation_count: 2
  slug: comeet-agentic-access
  summary_line: 2 operations
api_count: 3
apis:
- description: The Recruiting API is a partner-scoped REST API for building on top of Spark Hire Recruit (Comeet). It supports listing companies, positions, candidates, and pipeline events, and is the underlying int
  name: Comeet Recruiting API
  slug: comeet-recruiting-api
- description: The Hires API captures new-hire data from Comeet and pushes employee profile information into downstream HRIS, onboarding, and provisioning systems. It is typically used to trigger an onboarding workf
  name: Comeet Hires API
  slug: comeet-hires-api
- description: Published positions for a company.
  name: Comeet Positions API
  slug: comeet-positions-api
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Comeet Careers API
  slug: open-comeet-careers-api
- collection_type: open
  name: Comeet Careers Positions API
  slug: open-comeet-positions-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/comeet-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/comeet-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/comeet-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ComeetCo
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/comeet-hire-better-together
- group: company
  title: ''
  type: Website
  url: https://www.comeet.com/
- group: start
  title: ''
  type: Portal
  url: https://developers.comeet.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://recruit-support.sparkhire.com/hc/en-us
- group: other
  title: ''
  type: ParentCompany
  url: https://www.sparkhire.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.comeet.com/privacy-policy/
- group: design
  title: ''
  type: JSONLD
  url: json-ld/comeet-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/comeet-position-schema.json
- group: design
  title: ''
  type: Spectral
  url: rules/comeet-rules.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://developers.comeet.com/llms.txt
created: '2025-01-07'
description: Comeet (now Spark Hire Recruit, after Spark Hire's acquisition of Comeet) is a collaborative talent acquisition platform that helps companies post jobs, source and screen candidates, schedule interviews, and coordinate hiring teams. Comeet exposes a public Careers API (used to embed published positions on a custom careers website), a Recruiting API (used by integration partners to manage candidates and pipeline events), and a Hires API (used to push new-hire data into HRIS/onboarding systems).
finops:
- name: Comeet Finops
  service_category: HR Software
  slug: comeet-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/comeet.png
json_schemas:
- name: Comeet Position
  property_count: 9
  slug: comeet-position
jsonld:
- class_count: 0
  name: Comeet Context
  property_count: 3
  slug: comeet-context
layout: provider
modified: '2026-05-19'
name: Comeet
nav: Providers
network: true
overview: 'Comeet publishes 1 API on the [APIs.io](https://apis.io/) network: Positions API. Tagged areas include ATS, Candidates, Careers, Interviews, and Job.


  The Comeet catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Comeet''s developer surface includes authentication, developer portal, and 12 more developer resources.'
plans:
- name: Comeet Plans Pricing
  plan_count: 3
  slug: comeet-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 1
  name: Comeet Rate Limits
  slug: comeet-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Comeet API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: comeet-jsonschema-spectral-rules
- effective_rule_count: 49
  extends:
  - spectral:oas
  name: Comeet API Rules
  rule_count: 8
  severity_counts:
    error: 3
    hint: 0
    info: 1
    warn: 4
  slug: comeet-rules
score:
  band: thin
  composite: 34.8
  delta: 1.9
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 13.6
    contract_quality: 58.5
    developer_ergonomics: 35.7
    discoverability: 72.2
    governance: 13.6
    operational_transparency: 7.9
  previous_composite: 32.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/comeet/refs/heads/main/screenshots/comeet-2026-06-20T174801.png
security:
- kind: authentication
  name: Comeet Authentication
  slug: comeet-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Comeet Domain Security
  slug: comeet-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: comeet
tags:
- ATS
- Candidates
- Careers
- Interviews
- Job
- Recruiting
- Talent Acquisition
website: https://www.comeet.com/
---
