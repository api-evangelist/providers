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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.5
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Zylo Agentic Access
  operation_count: 10
  slug: zylo-agentic-access
  summary_line: 10 operations · 3 acting
api_count: 1
apis:
- description: Applications represent SaaS software products tracked within the Zylo platform, including metadata such as owner, category, and custom fields.
  name: Zylo Applications API
  slug: zylo-applications-api
- description: Export Jobs allow you to export subscription data asynchronously. You first create an export job, then retrieve the results when the job is complete.
  name: Zylo Export Jobs API
  slug: zylo-export-jobs-api
- description: Import Jobs allow you to import user, license, and activity data from non-integrated applications via CSV upload to optimize license usage across SaaS applications.
  name: Zylo Import Jobs API
  slug: zylo-import-jobs-api
- description: Subscriptions are configured instances created in the Zylo user interface. They typically have a 1:1 relationship to a given application, though you may also have multiple subscriptions to the same ap
  name: Zylo Subscriptions API
  slug: zylo-subscriptions-api
artifact_total: 44
collections:
- collection_type: postman
  name: Zylo Enterprise Applications API
  slug: postman-zylo-applications-api
- collection_type: postman
  name: Zylo Enterprise Applications Export Jobs API
  slug: postman-zylo-export-jobs-api
- collection_type: postman
  name: Zylo Enterprise Applications Import Jobs API
  slug: postman-zylo-import-jobs-api
- collection_type: postman
  name: Zylo Enterprise Applications Subscriptions API
  slug: postman-zylo-subscriptions-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Zylo Enterprise Applications API
  slug: open-zylo-applications-api
- collection_type: open
  name: Zylo Enterprise API
  slug: open-zylo-enterprise
- collection_type: open
  name: Zylo Enterprise Applications Export Jobs API
  slug: open-zylo-export-jobs-api
- collection_type: open
  name: Zylo Enterprise Applications Import Jobs API
  slug: open-zylo-import-jobs-api
- collection_type: open
  name: Zylo Enterprise Applications Subscriptions API
  slug: open-zylo-subscriptions-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/zylo/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/zylo-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/zylo-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zylo-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/zylo-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://zylo.com/
- group: other
  title: ''
  type: Customers
  url: https://zylo.com/customers/
- group: company
  title: ''
  type: Partners
  url: https://zylo.com/partners/
- group: operate
  title: ''
  type: Contact
  url: https://zylo.com/contact/
- group: company
  title: ''
  type: Blog
  url: https://zylo.com/blog/
- group: other
  title: ''
  type: CaseStudies
  url: https://zylo.com/customers/
- group: other
  title: ''
  type: Events
  url: https://zylo.com/events/
- group: other
  title: ''
  type: Podcast
  url: https://podcast.zylo.com/public/112/SaaSMe-Unfiltered%3A-The-SaaS-Management-Podcast-c316deea
- group: learn
  title: ''
  type: Videos
  url: https://zylo.com/videos/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/zyloapp/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/zylo
- group: learn
  title: ''
  type: Webinars
  url: https://zylo.com/webinars/
- group: start
  title: ''
  type: Login
  url: https://app.zylo.com/login
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://zylo.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://zylo.com/msa/
- group: commercial
  title: ''
  type: Pricing
  url: https://zylo.com/pricing/
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.zylo.com/llms.txt
created: '2025-07-15'
description: Zylo is a SaaS management platform that helps organizations optimize their software usage and spending. By providing insights into software utilization, licensing agreements, and renewal dates, Zylo enables companies to make informed decisions about their software investments. With Zylo, businesses can track their software expenses, manage subscriptions, and ensure compliance with licensing agreements.
features:
- name: SaaS Management
- name: SaaS Spend
- name: Application Spend
- name: Application Utilization
- name: Renewal Data
- name: SaaS Inventory Management
- name: License Mangement
- name: Renewal Management
- name: Pricing Benchmarks
- name: Application Benchmarks
- name: Visiblity
- name: Cost Optimization
- name: SaaS Discovery
- name: SaaS Governance
- name: Software License Management
- name: SaaS Optimization
- name: Employee Productivity
finops:
- name: Zylo Finops
  service_category: API
  slug: zylo-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zylo.png
json_schemas:
- name: Zylo Application
  property_count: 11
  slug: application
- name: Zylo Export Job
  property_count: 6
  slug: export-job
- name: Zylo Import Job
  property_count: 9
  slug: import-job
- name: Zylo Subscription
  property_count: 13
  slug: subscription
jsonld:
- class_count: 2
  name: Zylo Context
  property_count: 4
  slug: zylo-context
layout: provider
modified: '2026-05-19'
name: Zylo
nav: Providers
network: true
overview: 'Zylo publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Applications API, Export Jobs API, Import Jobs API, and 1 more. Tagged areas include Budgets, SaaS Management, and Spend.


  The Zylo catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Zylo''s developer surface includes authentication, engineering blog, pricing, and 19 more developer resources.'
plans:
- name: Zylo Plans Pricing
  plan_count: 3
  slug: zylo-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 5
  name: Zylo Rate Limits
  slug: zylo-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Zylo API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: zylo-jsonschema-spectral-rules
score:
  band: developing
  composite: 44.8
  coverage:
    artifact_dirs: 15
    catalog_gap: 55.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 68.4
    commercial_clarity: 68.4
    contract_governance: 9.8
    contract_quality: 67.3
    developer_ergonomics: 23.8
    discoverability: 66.7
    governance: 9.8
    operational_transparency: 13.2
  previous_composite: 44.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/zylo/refs/heads/main/screenshots/zylo-2026-06-20T202009.png
security:
- kind: authentication
  name: Zylo Authentication
  slug: zylo-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Zylo Domain Security
  slug: zylo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Zylo Trust Center
  slug: zylo-trust-center
  summary_line: SOC 2, GDPR
slug: zylo
tags:
- Budgets
- SaaS Management
- Spend
website: https://zylo.com/
---
