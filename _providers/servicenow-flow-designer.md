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
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: ServiceNow Flow Designer is an enterprise workflow automation tool for building automated processes within the ServiceNow platform.
  name: ServiceNow Flow Designer
  slug: servicenow-flow-designer
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/servicenow-flow-designer-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ServiceNow
- group: company
  title: ''
  type: Website
  url: https://www.servicenow.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.servicenow.com/bundle/flow-designer
created: 2026-03-27
description: ServiceNow Flow Designer is an enterprise workflow automation tool for building automated processes within the ServiceNow platform.
finops:
- name: Servicenow Flow Designer Finops
  service_category: API
  slug: servicenow-flow-designer-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/servicenow-flow-designer.png
layout: provider
modified: 2026-03-27
name: ServiceNow Flow Designer
nav: Providers
network: true
overview: 'ServiceNow Flow Designer publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Enterprise and Workflow-Automation.


  ServiceNow Flow Designer''s developer surface includes documentation and 3 more developer resources.'
plans:
- name: Servicenow Flow Designer Plans Pricing
  plan_count: 3
  slug: servicenow-flow-designer-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 5
  name: Servicenow Flow Designer Rate Limits
  slug: servicenow-flow-designer-rate-limits
score:
  band: minimal
  composite: 8.6
  coverage:
    artifact_dirs: 5
    catalog_earned: 31.0
    catalog_earned_first_party: 0.0
    catalog_gap: 84.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 40.7
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 8.6
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/servicenow-flow-designer/refs/heads/main/screenshots/servicenow-flow-designer-2026-06-20T193733.png
security:
- kind: domain-security
  name: Servicenow Flow Designer Domain Security
  slug: servicenow-flow-designer-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: servicenow-flow-designer
tags:
- Enterprise
- Workflow-Automation
website: https://www.servicenow.com
---
