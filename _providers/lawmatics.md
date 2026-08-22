---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - docs
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 47.6
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 87
  human_in_the_loop: 0
  name: Lawmatics Agentic Access
  operation_count: 177
  slug: lawmatics-agentic-access
  summary_line: 177 operations · 87 acting
api_count: 1
apis:
- description: 'RESTful OAuth API for managing leads, matters, contacts, intake forms, pipelines, and automated client follow-ups within the Lawmatics legal CRM platform. 177 operations over 95 paths, all under /v1, '
  name: Lawmatics OAuth API
  slug: lawmatics-oauth-api
artifact_total: 11
asyncapis:
- description: ''
  name: Lawmatics Webhooks
  slug: lawmatics-webhooks
collections:
- collection_type: postman
  name: Lawmatics OAuth API v1.22.0
  slug: postman-lawmatics-oauth-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/lawmatics-agentic-access.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/lawmatics-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/lawmatics-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lawmatics-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/lawmatics-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/lawmatics-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/lawmatics-openapi-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/lawmatics-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.lawmatics.com/security
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/lawmatics-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/lawmatics-changelog.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/lawmatics-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/lawmatics-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/lawmatics-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/lawmatics-webhooks.yml
- group: design
  title: ''
  type: Components
  url: components/lawmatics-components.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Postman
  url: postman/lawmatics-oauth-api.postman_collection.json
- group: company
  title: ''
  type: Website
  url: https://www.lawmatics.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.lawmatics.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.lawmatics.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://help.lawmatics.com/en/articles/10699983-lawmatics-open-api
- group: operate
  title: ''
  type: Support
  url: https://help.lawmatics.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/boost-legal
- group: start
  title: ''
  type: Login
  url: https://app.lawmatics.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.lawmatics.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.lawmatics.com/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://www.lawmatics.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.lawmatics.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.lawmatics.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lawmatics
- group: other
  title: ''
  type: X
  url: https://x.com/lawmatics
- group: commercial
  title: ''
  type: Plans
  url: plans/lawmatics-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/lawmatics-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/lawmatics-finops.yml
created: '2026-06-13'
description: Lawmatics is a legal CRM, client-intake and marketing-automation platform for law firms, from solo practices to multi-office firms. Its public developer surface is the Lawmatics OAuth API — a REST API of 177 operations across matters (called prospects in the API), contacts, companies, custom intake forms and form entries, custom fields, collections, pipelines, stages, practice areas, marketing sources and campaigns, events, tasks, notes, files, tags, users, time entries, expenses, invoices and transactions — plus a set of signed outbound webhooks. Access is OAuth 2.0 authorization code, gated on a Lawmatics support representative enabling developer settings on the account, and the resulting access token is non-expiring, unscoped and grants full CRUD over the firm.
finops:
- name: Lawmatics Finops
  service_category: ''
  slug: lawmatics-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lawmatics.png
jsonld:
- class_count: 5
  name: Lawmatics Context
  property_count: 26
  slug: lawmatics-context
layout: provider
modified: '2026-08-13'
name: Lawmatics
nav: Providers
network: true
overview: 'Lawmatics publishes 1 API on the [APIs.io](https://apis.io/) network: OAuth API. Tagged areas include Legal, CRM, Law Firms, Client Intake, and Marketing Automation.


  The Lawmatics catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 JSON-LD context.


  Lawmatics'' developer surface includes authentication, changelog, documentation, API reference, getting-started guide, support, engineering blog, and 28 more developer resources.'
plans:
- name: Lawmatics Plans Pricing
  plan_count: 3
  slug: lawmatics-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 2
  name: Lawmatics Rate Limits
  slug: lawmatics-rate-limits
scopes:
- name: Lawmatics Scopes
  scope_count: 0
  slug: lawmatics-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 64.0
  delta: -2.0
  facets:
    access_clarity: 85.5
    commercial_clarity: 85.5
    contract_governance: 30.3
    contract_quality: 74.8
    developer_ergonomics: 54.2
    discoverability: 75.9
    governance: 30.3
    operational_transparency: 47.4
  previous_composite: 66.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lawmatics/refs/heads/main/screenshots/lawmatics-2026-06-20T184337.png
security:
- kind: authentication
  name: Lawmatics Authentication
  slug: lawmatics-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Lawmatics Domain Security
  slug: lawmatics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: lawmatics
tags:
- Legal
- CRM
- Law Firms
- Client Intake
- Marketing Automation
- Matter Management
- E-Signature
- Workflow Automation
- Legal Tech
- Time and Billing
- Webhooks
- OAuth
website: https://www.lawmatics.com/
---
