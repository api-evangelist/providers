---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 38.4
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: Public API for the Weflow platform, documented at the Swagger UI.
  name: Weflow Public API
  slug: weflow-public-api
- description: 'Weflow API as documented publicly: 12 operations. Contract generated from the documentation by API Evangelist (2026-10-29); not the provider''s own document.'
  name: Weflow API
  slug: weflow-api
artifact_total: 9
common:
- group: operate
  href: https://artifacts.apis.io/weflow/rate-limits/weflow-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/weflow-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/weflow/plans/weflow-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/weflow-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/weflow/rules/weflow-rules.yml
  title: ''
  type: Spectral
  url: rules/weflow-rules.yml
- group: design
  href: https://artifacts.apis.io/weflow/vocabulary/weflow-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/weflow-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/weflow/components/weflow-components.yml
  title: ''
  type: Components
  url: components/weflow-components.yml
- group: design
  href: https://artifacts.apis.io/weflow/conventions/weflow-conventions.yml
  title: ''
  type: Conventions
  url: conventions/weflow-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.weflow.ai/security
- group: auth
  href: https://artifacts.apis.io/weflow/authentication/weflow-authentication.yml
  title: ''
  type: Authentication
  url: authentication/weflow-authentication.yml
- group: design
  href: https://artifacts.apis.io/weflow/conformance/weflow-conformance.yml
  title: ''
  type: Conformance
  url: conformance/weflow-conformance.yml
- group: agent
  href: https://artifacts.apis.io/weflow/llms/weflow-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/weflow-llms.txt
- group: auth
  href: https://artifacts.apis.io/weflow/well-known/weflow-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/weflow-help-security.txt
- group: agent
  href: https://artifacts.apis.io/weflow/well-known/weflow-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/weflow-well-known.yml
- group: other
  href: https://artifacts.apis.io/weflow/hosts/weflow-hosts.yml
  title: ''
  type: Hosts
  url: hosts/weflow-hosts.yml
- group: other
  href: https://artifacts.apis.io/weflow/vendors/weflow-vendors.yml
  title: ''
  type: Vendors
  url: vendors/weflow-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.weflow.ai/legal-notice
- group: auth
  title: ''
  type: Security
  url: https://www.weflow.ai/security
- group: start
  title: ''
  type: GettingStarted
  url: https://help.weflow.ai/en/articles/12067354-weflow-setup-salesforce-package-integration-user-and-mail-app
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.getweflow.app/api/v1/docs
- group: auth
  href: https://artifacts.apis.io/weflow/security/weflow-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/weflow-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/weflow/security/weflow-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/weflow-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.getweflow.com
- group: docs
  title: ''
  type: Documentation
  url: https://help.weflow.ai/en/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.weflow.ai/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.weflow.ai/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.weflow.ai/privacy
- group: operate
  title: ''
  type: Support
  url: https://help.weflow.ai/en/
- group: start
  title: ''
  type: SignUp
  url: https://www.weflow.ai/free-trial
coverage:
  checked: '2026-10-29'
  detail: API spec requires an authentication token, returning INVALID_TOKEN on unauthenticated requests.
  evidence:
  - status: 200
    url: https://api.getweflow.app/api/v1/docs/
  reason: partner-login
  state: gated
created: '2026-10-29'
description: Weflow provides a Revenue AI Orchestration Platform for RevOps teams, automating Salesforce data capture, delivering real-time deal intelligence, forecasting, and AI-driven insights. The platform syncs emails, meetings and contacts from Outlook and Google into Salesforce, offers conversation intelligence, AI agents to orchestrate actions, and a suite of tools that improve pipeline visibility, forecast accuracy and sales performance for fast-growing companies.
image: https://cdn.prod.website-files.com/647e329e7adac8431aa23816/66ba481b5c5d4dc17fce6a97_weflow-logo.svg
layout: provider
modified: '2026-10-29'
name: Weflow
nav: Providers
network: true
overview: 'Weflow is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include RevenueAI, RevOps, Salesforce, Automation, and AI.


  The Weflow catalog on APIs.io includes 1 Spectral governance ruleset.


  Weflow''s developer surface includes authentication, getting-started guide, documentation, pricing, engineering blog, support, signup flow, and 20 more developer resources.'
plans:
- name: Weflow Plans Pricing
  plan_count: 10
  slug: weflow-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 1
  name: Weflow Rate Limits
  slug: weflow-rate-limits
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Weflow API Rules
  rule_count: 10
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 0
  slug: weflow-rules
scopes:
- name: Weflow Scopes
  scope_count: 0
  slug: weflow-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 46.4
  coverage:
    artifact_dirs: 23
    catalog_earned: 57.0
    catalog_earned_first_party: 20.0
    catalog_gap: 58.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 92.1
    contract_governance: 19.7
    contract_quality: 10.5
    developer_ergonomics: 50.0
    discoverability: 57.1
    operational_transparency: 31.6
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 3
      marker_coverage: 100.0
      total: 3
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 36.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Weflow Authentication
  slug: weflow-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Weflow Domain Security
  slug: weflow-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Weflow Trust Center
  slug: weflow-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: weflow
tags:
- RevenueAI
- RevOps
- Salesforce
- Automation
- AI
- Analytics
website: https://www.getweflow.com
---
