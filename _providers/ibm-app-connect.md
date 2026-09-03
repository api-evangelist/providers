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
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: The IBM App Connect API provides programmatic access to manage integration flows, connectors, accounts, and other integration platform resources.
  name: IBM App Connect API
  slug: ibm-app-connect-api
artifact_total: 7
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/ibm/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ibm-app-connect-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ibm-app-connect-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/IBM
- group: company
  title: ''
  type: Website
  url: https://www.ibm.com/products/app-connect
- group: docs
  title: ''
  type: Documentation
  url: https://www.ibm.com/docs/en/app-connect/
- group: operate
  title: ''
  type: Support
  url: https://www.ibm.com/mysupport
- group: design
  title: ''
  type: Rules
  url: rules/ibm-app-connect-rules.yml
created: '2026-03-16'
description: IBM App Connect is an integration platform that enables organizations to connect applications, data, and services across cloud and on-premises environments. It provides low-code integration capabilities with pre-built connectors and a flow editor for building integration flows.
finops:
- name: Ibm App Connect Finops
  service_category: API
  slug: ibm-app-connect-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ibm-app-connect.png
layout: provider
modified: '2026-08-21'
name: IBM App Connect
nav: Providers
network: true
overview: 'IBM App Connect publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Connectors, IBM, Integration Platform, and iPaaS.


  The IBM App Connect catalog on APIs.io includes 1 Spectral governance ruleset.


  IBM App Connect''s developer surface includes documentation, support, and 6 more developer resources.'
plans:
- name: Ibm App Connect Plans Pricing
  plan_count: 3
  slug: ibm-app-connect-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 5
  name: Ibm App Connect Rate Limits
  slug: ibm-app-connect-rate-limits
rules:
- effective_rule_count: 0
  extends: []
  name: IBM App Connect API Rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: ibm-app-connect-rules
score:
  band: emerging
  composite: 14.8
  coverage:
    artifact_dirs: 6
    catalog_gap: 79.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 14.8
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ibm-app-connect/refs/heads/main/screenshots/ibm-app-connect-2026-06-20T183128.png
security:
- kind: domain-security
  name: Ibm App Connect Domain Security
  slug: ibm-app-connect-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Ibm App Connect Vulnerability Disclosure
  slug: ibm-app-connect-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: ibm-app-connect
tags:
- Connectors
- IBM
- Integration Platform
- iPaaS
website: https://www.ibm.com/products/app-connect
---
