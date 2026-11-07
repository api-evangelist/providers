---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://backend.openenvoy.io/public/api/v1
  baseurl_source: declared
  description: Jobs in the system
  name: OpenEnvoy Job API
  slug: openenvoy-job-api
artifact_total: 10
common:
- group: operate
  href: https://artifacts.apis.io/openenvoy/rate-limits/openenvoy-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/openenvoy-rate-limits.yml
- group: other
  href: https://artifacts.apis.io/openenvoy/overlays/openenvoy-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/openenvoy-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/openenvoy/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/openenvoy/security/openenvoy-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/openenvoy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.openenvoy.com/
- group: docs
  title: ''
  type: Documentation
  url: https://apidocs.openenvoy.io/
- group: docs
  title: ''
  type: APIReference
  url: https://backend.openenvoy.io/api-docs
- group: operate
  title: ''
  type: Support
  url: https://support.openenvoy.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.openenvoy.com/
- group: company
  title: ''
  type: Blog
  url: https://www.openenvoy.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.openenvoy.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.openenvoy.com/services-agreement
- group: start
  title: ''
  type: GettingStarted
  url: https://support.openenvoy.com/collections/5817344542-getting_started
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.openenvoy.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/openenvoy
- group: operate
  title: ''
  type: ChangeLog
  url: https://changelog.openenvoy.io/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.openenvoy.com/
- group: design
  href: https://artifacts.apis.io/openenvoy/lifecycle/openenvoy-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/openenvoy-lifecycle.yml
- group: agent
  href: https://artifacts.apis.io/openenvoy/llms/openenvoy-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/openenvoy-llms.txt
- group: commercial
  href: https://artifacts.apis.io/openenvoy/plans/openenvoy-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/openenvoy-plans-pricing.yml
created: '2026-08-26'
description: OpenEnvoy is an AI-native financial operations platform for enterprise and mid-market finance teams, automating accounts payable, accounts receivable, invoice processing and cash application end to end. The platform ingests invoices from any format, extracts and GL-codes the data without OCR templates, and reconciles each invoice against purchase orders, contracts, rate sheets and receipts to catch duplicates, fraud and supplier overbilling before payment. OpenEnvoy publishes a public RESTful API covering job (invoice) creation, document upload, matching status and user/role administration, documented as a public Postman collection at apidocs.openenvoy.io with a Swagger 2.0 definition served from the API host itself. It integrates with SAP, Oracle, NetSuite, Microsoft Dynamics and QuickBooks Online.
finops:
- has_sources: true
  method: derived
  name: Openenvoy Finops
  primary_unit: ''
  service_category: ''
  slug: openenvoy-finops
  template: true
image: https://avatars.githubusercontent.com/u/65476969?v=4
layout: provider
modified: '2026-08-26'
name: OpenEnvoy
nav: Providers
network: true
overview: 'OpenEnvoy publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Job API. Tagged areas include Accounts Payable, Accounts Receivable, Invoice Processing, Finance Automation, and Accounting.


  The OpenEnvoy catalog on APIs.io includes 1 Spectral governance ruleset.


  OpenEnvoy''s developer surface includes documentation, API reference, support, engineering blog, pricing, getting-started guide, changelog, and 13 more developer resources.'
plans:
- name: Openenvoy Plans Pricing
  plan_count: 4
  slug: openenvoy-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Openenvoy Rate Limits
  slug: openenvoy-rate-limits
rules:
- authorship: generated
  effective_rule_count: 95
  extends:
  - spectral:oas
  name: OpenEnvoy API Rules
  rule_count: 54
  severity_counts:
    error: 52
    hint: 0
    info: 1
    warn: 1
  slug: openenvoy-rules
score:
  band: developing
  composite: 49.8
  coverage:
    artifact_dirs: 26
    catalog_earned: 53.5
    catalog_earned_first_party: 12.0
    catalog_gap: 61.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 63.2
    contract_governance: 13.6
    contract_quality: 50.2
    developer_ergonomics: 53.7
    discoverability: 73.2
    operational_transparency: 34.2
  previous_composite: 49.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/openenvoy/openenvoy-2026-09-02T150855.png
security:
- kind: authentication
  name: Openenvoy Authentication
  slug: openenvoy-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Openenvoy Domain Security
  slug: openenvoy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: openenvoy-manage-users-and-roles
  slug: openenvoy-manage-users-and-roles
- name: openenvoy-review-and-approve-job
  slug: openenvoy-review-and-approve-job
- name: openenvoy-submit-invoice-for-audit
  slug: openenvoy-submit-invoice-for-audit
slug: openenvoy
tags:
- Accounts Payable
- Accounts Receivable
- Invoice Processing
- Finance Automation
- Accounting
- Procure-to-Pay
- Document Processing
- Artificial Intelligence
- ERP Integration
- Spend Management
- Procurement
website: https://www.openenvoy.com/
---
