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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: FOCUS defines a common normalized data schema for cloud and technology billing data. The specification is delivered as a set of normative documents and supporting artifacts (column library, requiremen
  name: FOCUS (FinOps Open Cost and Usage Specification)
  slug: focus-spec
artifact_total: 7
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/releases
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/blob/working_draft/CONTRIBUTING.md
- group: auth
  title: ''
  type: DomainSecurity
  url: security/focus-spec-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://focus.finops.org/
- group: docs
  title: ''
  type: Documentation
  url: https://focus.finops.org/
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/FinOps-Open-Cost-and-Usage-Spec
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/focus-billing-record-schema.json
created: '2026-03-27'
description: FOCUS, the FinOps Open Cost and Usage Specification, is an open standard maintained under the FinOps Foundation that normalizes cost and usage data across cloud, SaaS, data center, and other technology vendors. FOCUS defines a common data schema, a controlled vocabulary of column names, allowed values, and pricing attributes so that practitioners can apply a consistent set of FinOps practices regardless of which provider generated the underlying billing dataset. FOCUS is purely a data specification rather than a REST API; conforming providers expose exports of their billing data in the FOCUS format, and tooling consumes those exports against the published column library, data model, and validator.
finops:
- name: Focus Spec Finops
  service_category: API
  slug: focus-spec-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/focus-spec.png
json_schemas:
- name: FOCUS Billing Record
  property_count: 47
  slug: focus-billing-record
layout: provider
modified: '2026-04-28'
name: FOCUS (FinOps Open Cost and Usage Specification)
nav: Providers
network: true
overview: 'FOCUS (FinOps Open Cost and Usage Specification) publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Billing, Cost and Usage, FinOps, Open Standard, and Specification.


  The FOCUS (FinOps Open Cost and Usage Specification) catalog on APIs.io includes 1 Spectral governance ruleset.


  FOCUS (FinOps Open Cost and Usage Specification)''s developer surface includes documentation and 8 more developer resources.'
plans:
- name: Focus Spec Plans Pricing
  plan_count: 3
  slug: focus-spec-plans-pricing
random_paper: 122
rate_limits:
- limit_count: 5
  name: Focus Spec Rate Limits
  slug: focus-spec-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: FOCUS (FinOps Open Cost and Usage Specification) API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: focus-spec-jsonschema-spectral-rules
score:
  band: emerging
  composite: 17.7
  delta: -6.3
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 9.8
    contract_quality: 8.5
    developer_ergonomics: 9.5
    discoverability: 59.3
    governance: 9.8
    operational_transparency: 26.3
  previous_composite: 24.0
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/focus-spec/refs/heads/main/screenshots/focus-spec-2026-06-20T181352.png
security:
- kind: domain-security
  name: Focus Spec Domain Security
  slug: focus-spec-domain-security
  summary_line: TLSv1.3 · DMARC
slug: focus-spec
tags:
- Billing
- Cost and Usage
- FinOps
- Open Standard
- Specification
website: https://focus.finops.org/
---
