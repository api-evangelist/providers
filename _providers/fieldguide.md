---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - authentication
  - scopes
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 19
  human_in_the_loop: 0
  name: Fieldguide Agentic Access
  operation_count: 56
  slug: fieldguide-agentic-access
  summary_line: 56 operations · 19 acting
api_count: 1
apis:
- baseURL: https://api.fieldguide.io
  baseurl_source: declared
  description: Endpoints used to interact with Fieldguide Comments
  name: Fieldguide Comments API
  slug: fieldguide-comments-api
- baseURL: https://api.fieldguide.io
  baseurl_source: declared
  description: Endpoints used to interact with Fieldguide Companies
  name: Fieldguide Companies API
  slug: fieldguide-companies-api
- baseURL: https://api.fieldguide.io
  baseurl_source: declared
  description: Endpoints used to interact with Fieldguide Controls
  name: Fieldguide Controls API
  slug: fieldguide-controls-api
- baseURL: https://api.fieldguide.io
  baseurl_source: declared
  description: Endpoints used to interact with Fieldguide Engagements
  name: Fieldguide Engagements API
  slug: fieldguide-engagements-api
- baseURL: https://api.fieldguide.io
  baseurl_source: declared
  description: Endpoints used to interact with Fieldguide Files
  name: Fieldguide Files API
  slug: fieldguide-files-api
- baseURL: https://api.fieldguide.io
  baseurl_source: declared
  description: Endpoints used to interact with Fieldguide Insights
  name: Fieldguide Insights API
  slug: fieldguide-insights-api
- baseURL: https://api.fieldguide.io
  baseurl_source: declared
  description: Endpoints used to interact with long-running processes (Jobs) in the Fieldguide API
  name: Fieldguide Jobs API
  slug: fieldguide-jobs-api
- baseURL: https://api.fieldguide.io
  baseurl_source: declared
  description: Endpoints used to interact with Fieldguide Milestones
  name: Fieldguide Milestones API
  slug: fieldguide-milestones-api
- baseURL: https://api.fieldguide.io
  baseurl_source: declared
  description: Endpoints used to interact with Fieldguide Requests
  name: Fieldguide Requests API
  slug: fieldguide-requests-api
- baseURL: https://api.fieldguide.io
  baseurl_source: declared
  description: Endpoints used to interact with Fieldguide Sheet Columns
  name: Fieldguide Sheet Columns API
  slug: fieldguide-sheet-columns-api
- baseURL: https://api.fieldguide.io
  baseurl_source: declared
  description: Endpoints used to interact with Fieldguide Sheet Rows
  name: Fieldguide Sheet Rows API
  slug: fieldguide-sheet-rows-api
- baseURL: https://api.fieldguide.io
  baseurl_source: declared
  description: Endpoints used to interact with Fieldguide Sheets
  name: Fieldguide Sheets API
  slug: fieldguide-sheets-api
- baseURL: https://api.fieldguide.io
  baseurl_source: declared
  description: Endpoints used to interact with Fieldguide Users
  name: Fieldguide Users API
  slug: fieldguide-users-api
- baseURL: https://api.fieldguide.io
  baseurl_source: declared
  description: Endpoints used to interact with Fieldguide Webhooks
  name: Fieldguide Webhooks API
  slug: fieldguide-webhooks-api
- baseURL: https://api.fieldguide.io
  baseurl_source: declared
  description: The Scopes API from Fieldguide — 1 operation(s) for scopes.
  name: Fieldguide Scopes API
  slug: fieldguide-scopes-api
- baseURL: https://api.fieldguide.io
  baseurl_source: declared
  description: The Token API from Fieldguide — 1 operation(s) for token.
  name: Fieldguide Token API
  slug: fieldguide-token-api
artifact_total: 43
asyncapis:
- description: ''
  name: Fieldguide Webhooks
  slug: fieldguide-webhooks
collections:
- collection_type: open
  name: Fieldguide api API
  slug: open-fieldguide-api-api
- collection_type: open
  name: Fieldguide api comments API
  slug: open-fieldguide-comments-api
- collection_type: open
  name: Fieldguide api companies API
  slug: open-fieldguide-companies-api
- collection_type: open
  name: Fieldguide api controls API
  slug: open-fieldguide-controls-api
- collection_type: open
  name: Fieldguide api engagements API
  slug: open-fieldguide-engagements-api
- collection_type: open
  name: Fieldguide api files API
  slug: open-fieldguide-files-api
- collection_type: open
  name: Fieldguide api insights API
  slug: open-fieldguide-insights-api
- collection_type: open
  name: Fieldguide api jobs API
  slug: open-fieldguide-jobs-api
- collection_type: open
  name: Fieldguide api milestones API
  slug: open-fieldguide-milestones-api
- collection_type: open
  name: Fieldguide api requests API
  slug: open-fieldguide-requests-api
- collection_type: open
  name: Fieldguide api sheet-columns API
  slug: open-fieldguide-sheet-columns-api
- collection_type: open
  name: Fieldguide api sheet-rows API
  slug: open-fieldguide-sheet-rows-api
- collection_type: open
  name: Fieldguide api sheets API
  slug: open-fieldguide-sheets-api
- collection_type: open
  name: Fieldguide api users API
  slug: open-fieldguide-users-api
- collection_type: open
  name: Fieldguide api webhooks API
  slug: open-fieldguide-webhooks-api
common:
- group: commercial
  href: https://artifacts.apis.io/fieldguide/plans/fieldguide-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/fieldguide-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/fieldguide/capabilities/fieldguide-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/fieldguide-capability-edges.yml
- group: auth
  href: https://artifacts.apis.io/fieldguide/security/fieldguide-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/fieldguide-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/fieldguide/security/fieldguide-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fieldguide-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/fieldguide/agentic-access/fieldguide-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/fieldguide-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/fieldguide/authentication/fieldguide-authentication.yml
  title: ''
  type: Authentication
  url: authentication/fieldguide-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.fieldguide.io
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.fieldguide.io/developers
- group: docs
  title: ''
  type: Documentation
  url: https://fieldguide.notion.site/Fieldguide-API-Documentation-650f03765dc0402c96ccb750ecd70eda
- group: docs
  title: ''
  type: APIReference
  url: https://api.fieldguide.io/api
- group: company
  title: ''
  type: Blog
  url: https://www.fieldguide.io/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://changelog.fieldguide.io
- group: operate
  title: ''
  type: StatusPage
  url: https://status.fieldguide.io
- group: commercial
  title: ''
  type: Pricing
  url: https://www.fieldguide.io/demo
- group: start
  title: ''
  type: SignUp
  url: https://app.fieldguide.io
- group: start
  title: ''
  type: Login
  url: https://app.fieldguide.io
- group: operate
  title: ''
  type: Support
  url: mailto:support@fieldguide.io
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.fieldguide.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.fieldguide.io/privacy-policy
- group: auth
  title: ''
  type: Compliance
  url: https://www.fieldguide.io/trust
- group: auth
  href: https://artifacts.apis.io/fieldguide/scopes/fieldguide-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/fieldguide-scopes.yml
- group: design
  href: https://artifacts.apis.io/fieldguide/conventions/fieldguide-conventions.yml
  title: ''
  type: Conventions
  url: conventions/fieldguide-conventions.yml
- group: design
  href: https://artifacts.apis.io/fieldguide/errors/fieldguide-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/fieldguide-problem-types.yml
- group: design
  href: https://artifacts.apis.io/fieldguide/lifecycle/fieldguide-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/fieldguide-lifecycle.yml
- group: agent
  href: https://artifacts.apis.io/fieldguide/mcp/fieldguide-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/fieldguide-mcp.yml
- group: agent
  href: https://artifacts.apis.io/fieldguide/llms/fieldguide-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/fieldguide-llms.txt
- group: other
  href: https://artifacts.apis.io/fieldguide/overlays/fieldguide-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/fieldguide-openapi-overlay.yaml
- group: design
  href: https://artifacts.apis.io/fieldguide/conformance/fieldguide-conformance.yml
  title: ''
  type: Conformance
  url: conformance/fieldguide-conformance.yml
- group: design
  href: https://artifacts.apis.io/fieldguide/asyncapi/fieldguide-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/fieldguide-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/fieldguide/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/fieldguide/data-model/fieldguide-data-model.yml
  title: ''
  type: DataModel
  url: data-model/fieldguide-data-model.yml
created: '2026-07-17'
description: Fieldguide is an AI-native platform for audit and advisory firms, providing professional-grade "Field Agents" that plan, execute, and document engagement work end-to-end across financial audit, SOC audits, IT audit, risk advisory, tax, cybersecurity, and regulatory compliance engagements. The platform pairs engagement management, document management, insights and analytics, and a client hub with an open REST API (api.fieldguide.io) that exposes companies, engagements, requests, sheets, files, comments, milestones, users, insights, and webhook subscriptions. Fieldguide is used by half of the top 100 firms, is SOC 2 Type 2 and ISO/IEC 42001 certified, and is backed by 8VC and Bessemer Venture Partners.
finops:
- has_sources: true
  method: derived
  name: Fieldguide Finops
  primary_unit: ''
  service_category: ''
  slug: fieldguide-finops
  template: true
image: https://app.fieldguide.io/img/logo192.png
layout: provider
modified: '2026-09-16'
name: Fieldguide
nav: Providers
network: true
overview: 'Fieldguide publishes 16 API contracts indexed on the [APIs.io](https://apis.io/) network, including Comments API, Companies API, Controls API, and 13 more. Tagged areas include Company, Audit, Advisory, Accounting, and Compliance.


  The Fieldguide catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Fieldguide''s developer surface includes authentication, documentation, API reference, engineering blog, changelog, pricing, signup flow, and 24 more developer resources.'
plans:
- name: Fieldguide Plans Pricing
  plan_count: 0
  slug: fieldguide-plans-pricing
random_paper: 10
rules:
- authorship: generated
  effective_rule_count: 107
  extends:
  - spectral:oas
  name: Fieldguide API Rules
  rule_count: 66
  severity_counts:
    error: 54
    hint: 0
    info: 6
    warn: 6
  slug: fieldguide-rules
scopes:
- name: Fieldguide Scopes
  scope_count: 21
  slug: fieldguide-scopes
  summary_line: 21 scopes
score:
  band: developing
  composite: 47.1
  coverage:
    artifact_dirs: 27
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 47.4
    contract_governance: 18.2
    contract_quality: 56.0
    developer_ergonomics: 37.5
    discoverability: 73.2
    operational_transparency: 31.6
  previous_composite: 47.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 16
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 36.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/fieldguide/fieldguide-2026-07-25T214434.png
security:
- kind: authentication
  name: Fieldguide Authentication
  slug: fieldguide-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Fieldguide Domain Security
  slug: fieldguide-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Fieldguide Trust Center
  slug: fieldguide-trust-center
  summary_line: SOC 2, PCI DSS, HIPAA
skill_count: 3
skills:
- name: Manage Fieldguide engagements
  slug: fieldguide-manage-engagements
- name: Work Fieldguide requests and comments
  slug: fieldguide-requests-and-comments
- name: Subscribe to Fieldguide webhooks
  slug: fieldguide-webhooks
slug: fieldguide
tags:
- Company
- Audit
- Advisory
- Accounting
- Compliance
- Risk Management
- Engagement Management
- Artificial Intelligence
- Agents
- Webhook
website: https://www.fieldguide.io
---
