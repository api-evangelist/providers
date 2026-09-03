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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.8
  scored_at: '2026-09-03'
api_count: 1
apis:
- baseURL: https://backend.openenvoy.io/public/api/v1
  baseurl_source: declared
  description: Jobs in the system
  name: OpenEnvoy Job API
  slug: openenvoy-job-api
artifact_total: 5
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/openenvoy-openapi-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
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
  title: ''
  type: Lifecycle
  url: lifecycle/openenvoy-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/openenvoy-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/openenvoy-plans-pricing.yml
created: '2026-08-26'
description: OpenEnvoy is an AI-native financial operations platform for enterprise and mid-market finance teams, automating accounts payable, accounts receivable, invoice processing and cash application end to end. The platform ingests invoices from any format, extracts and GL-codes the data without OCR templates, and reconciles each invoice against purchase orders, contracts, rate sheets and receipts to catch duplicates, fraud and supplier overbilling before payment. OpenEnvoy publishes a public RESTful API covering job (invoice) creation, document upload, matching status and user/role administration, documented as a public Postman collection at apidocs.openenvoy.io with a Swagger 2.0 definition served from the API host itself. It integrates with SAP, Oracle, NetSuite, Microsoft Dynamics and QuickBooks Online.
image: https://avatars.githubusercontent.com/u/65476969?v=4
layout: provider
modified: '2026-08-26'
name: OpenEnvoy
nav: Providers
network: true
overview: 'OpenEnvoy publishes 1 API on the [APIs.io](https://apis.io/) network: Job API. Tagged areas include Accounts Payable, Accounts Receivable, Invoice Processing, Finance Automation, and Accounting.


  OpenEnvoy''s developer surface includes documentation, API reference, support, engineering blog, pricing, getting-started guide, changelog, and 12 more developer resources.'
plans:
- name: Openenvoy Plans Pricing
  plan_count: 3
  slug: openenvoy-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Openenvoy Rate Limits
  slug: openenvoy-rate-limits
score:
  band: developing
  composite: 47.8
  coverage:
    artifact_dirs: 20
    catalog_gap: 66.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 63.2
    commercial_clarity: 63.2
    contract_governance: 0.0
    contract_quality: 49.0
    developer_ergonomics: 54.2
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 47.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/openenvoy/refs/heads/main/screenshots/openenvoy-2026-09-02T150855.png
security:
- kind: authentication
  name: Openenvoy Authentication
  slug: openenvoy-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Openenvoy Domain Security
  slug: openenvoy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
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
website: https://www.openenvoy.com/
---
