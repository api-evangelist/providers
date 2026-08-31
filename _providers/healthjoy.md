---
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/healthjoy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.healthjoy.com/
- group: company
  title: ''
  type: Blog
  url: https://www.healthjoy.com/resources
- group: operate
  title: ''
  type: Support
  url: https://healthjoymemberservices.zendesk.com/hc/en-us
- group: start
  title: ''
  type: Login
  url: https://www.healthjoy.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.healthjoy.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.healthjoy.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/healthjoy
- group: auth
  title: ''
  type: Compliance
  url: https://www.healthjoy.com/privacy-security
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/healthjoy-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/healthjoy-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/healthjoy-conformance.yml
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/healthjoy_stock/
created: '2026-08-04'
description: HealthJoy is a Chicago-based employee-benefits engagement, healthcare navigation, and cost-containment platform founded in 2014, which markets itself as a "Benefits Operating System" (BOS) for employers and benefit consultants. It unifies fragmented health benefits into a single member-facing app combining Joy AI — a 24/7 AI assistant trained on each client's benefits plan — with a licensed human healthcare concierge team, provider search with cost scores and quality ratings, prescription savings, medical bill review, and an intelligent steerage engine that routes members to high-value, fair-priced care. Employers and consultants get a client dashboard reporting engagement, utilization, savings, and ROI. HealthJoy reports 1,800+ client companies and 1.25M+ members. It publishes no public developer API, developer portal, or machine-readable API contract; integrations with benefits-administration and TPA vendors (e.g. Employee Navigator) are delivered as managed eligibility/census
  data feeds set up by its implementation team rather than as a self-serve API.
image: https://framerusercontent.com/images/V67oySpbzNWmW6h5NeKzMj7v8.png
layout: provider
modified: '2026-08-04'
name: HealthJoy
nav: Providers
network: true
overview: 'HealthJoy is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Healthcare, Employee Benefits, and Benefits Administration.


  HealthJoy''s developer surface includes engineering blog, support, and 11 more developer resources.'
random_paper: 2
score:
  band: emerging
  composite: 18.2
  coverage:
    artifact_dirs: 7
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 18.2
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 36.4
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/healthjoy/refs/heads/main/screenshots/healthjoy-2026-08-07T170219.png
security:
- kind: domain-security
  name: Healthjoy Domain Security
  slug: healthjoy-domain-security
  summary_line: TLSv1.3 · DMARC
slug: healthjoy
tags:
- Company
- Health
- Healthcare
- Employee Benefits
- Benefits Administration
- Health Insurance
- Healthcare Navigation
- Human Resources
- Insurance
- Artificial Intelligence
- HIPAA
- Cost Containment
website: https://www.healthjoy.com/
---
