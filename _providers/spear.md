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
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: Spear is a developer platform focused on API development workflows, providing tools for API design, collaboration, and delivery through a unified workspace experience.
  name: Spear
  slug: spear
artifact_total: 10
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/spear-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://spear.dev
- group: agent
  title: ''
  type: LlmsText
  url: https://spear.dev/llms.txt
created: '2024-01-01'
description: Spear is a developer platform focused on API development workflows, providing tools for API design, collaboration, and delivery. The platform enables teams to build, test, and ship APIs faster through a unified workspace experience.
examples:
- key_count: 3
  name: Spear Workspace Example
  slug: spear-workspace-example
finops:
- name: Spear Finops
  service_category: API
  slug: spear-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/spear.png
json_schemas:
- name: Spear Workspace
  property_count: 8
  slug: spear-workspace
json_structures:
- name: Spear Workspace Structure
  property_count: 0
  slug: spear-workspace-structure
jsonld:
- class_count: 3
  name: Spear Context
  property_count: 10
  slug: spear-context
layout: provider
modified: '2026-05-02'
name: Spear
nav: Providers
network: true
overview: 'Spear publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include API Development, Collaboration, Developer Tools, and Platform.


  The Spear catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
plans:
- name: Spear Plans Pricing
  plan_count: 3
  slug: spear-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 5
  name: Spear Rate Limits
  slug: spear-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Spear API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: spear-jsonschema-spectral-rules
score:
  band: emerging
  composite: 13.8
  coverage:
    artifact_dirs: 12
    catalog_gap: 67.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 9.8
    contract_quality: 10.7
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 9.8
    operational_transparency: 7.9
  previous_composite: 13.8
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/spear/refs/heads/main/screenshots/spear-2026-06-20T194252.png
security:
- kind: domain-security
  name: Spear Domain Security
  slug: spear-domain-security
  summary_line: TLSv1.3
slug: spear
tags:
- API Development
- Collaboration
- Developer Tools
- Platform
website: https://spear.dev
---
