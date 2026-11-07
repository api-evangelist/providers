---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: unknown
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 34.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Splitforms Agentic Access
  operation_count: 1
  slug: splitforms-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- description: One HTTPS endpoint that receives HTML, fetch and server‑side form submissions. Provides /api/submit with access_key, rate limits, plans and webhook support.
  name: Form Submission API
  slug: form-submission-api
artifact_total: 10
common:
- group: agent
  href: https://artifacts.apis.io/splitforms/agentic-access/splitforms-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/splitforms-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/splitforms/plans/splitforms-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/splitforms-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/splitforms/rules/splitforms-rules.yml
  title: ''
  type: Spectral
  url: rules/splitforms-rules.yml
- group: design
  href: https://artifacts.apis.io/splitforms/vocabulary/splitforms-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/splitforms-vocabulary.yml
- group: operate
  href: https://artifacts.apis.io/splitforms/changelog/splitforms-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/splitforms-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://splitforms.com/security
- group: design
  href: https://artifacts.apis.io/splitforms/conformance/splitforms-conformance.yml
  title: ''
  type: Conformance
  url: conformance/splitforms-conformance.yml
- group: agent
  href: https://artifacts.apis.io/splitforms/llms/splitforms-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/splitforms-llms.txt
- group: build
  href: https://artifacts.apis.io/splitforms/mcp/splitforms-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/splitforms-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/splitforms/mcp/splitforms-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/splitforms-mcp.yml
- group: other
  href: https://artifacts.apis.io/splitforms/hosts/splitforms-hosts.yml
  title: ''
  type: Hosts
  url: hosts/splitforms-hosts.yml
- group: other
  href: https://artifacts.apis.io/splitforms/vendors/splitforms-vendors.yml
  title: ''
  type: Vendors
  url: vendors/splitforms-vendors.yml
- group: design
  title: ''
  type: Webhooks
  url: https://splitforms.com/features/webhooks
- group: operate
  title: ''
  type: StatusPage
  url: https://splitforms.com/status
- group: auth
  title: ''
  type: Security
  url: https://splitforms.com/security
- group: operate
  title: ''
  type: Roadmap
  url: https://splitforms.com/roadmap
- group: operate
  title: ''
  type: ChangeLog
  url: https://splitforms.com/changelog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/splitforms
- group: auth
  href: https://artifacts.apis.io/splitforms/security/splitforms-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/splitforms-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/splitforms/security/splitforms-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/splitforms-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/splitforms/security/splitforms-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/splitforms-domain-security.yml
- group: docs
  title: ''
  type: APIReference
  url: https://splitforms.com/api-reference
- group: docs
  title: ''
  type: Documentation
  url: https://splitforms.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://splitforms.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://splitforms.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://splitforms.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://splitforms.com/privacy
- group: start
  title: ''
  type: SignUp
  url: https://splitforms.com/signup
- group: company
  title: ''
  type: Website
  url: https://splitforms.com
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://splitforms.com/openapi.json
  - status: 401
    url: https://splitforms.com/api/mcp
  - status: 200
    url: https://splitforms.com
  reason: partner-login
  state: gated
created: '2026-10-12'
description: Split Forms provides a hosted form backend service that lets developers collect form submissions without building their own server. It supports HTML, React, Next.js, and AI‑generated sites, delivering submissions via email and a dashboard. The free tier offers 500 submissions with no credit‑card requirement, while paid plans add higher limits, webhooks, file uploads, and team seats.
finops:
- has_sources: true
  method: derived
  name: Splitforms Finops
  primary_unit: ''
  service_category: ''
  slug: splitforms-finops
  template: true
image: https://splitforms.com/og/hero-form-to-inbox.webp
layout: provider
mcp_servers:
- description: Remote MCP server at splitforms.com requiring an API key.
  name: Split Forms MCP Server
  slug: splitforms-mcp-yml
modified: '2026-10-12'
name: Split Forms
nav: Providers
network: true
overview: 'Split Forms publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Form Submission API. Tagged areas include Company, Form Backend, Developer Tools, Free Tier, and Webhook.


  The Split Forms catalog on APIs.io includes 1 Spectral governance ruleset.


  Split Forms'' developer surface includes changelog, API reference, documentation, pricing, engineering blog, signup flow, and 23 more developer resources.'
plans:
- name: Splitforms Plans Pricing
  plan_count: 3
  slug: splitforms-plans-pricing
- name: Splitforms Price Estimates
  plan_count: 0
  slug: splitforms-price-estimates
random_paper: 3
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Split Forms API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: splitforms-rules
score:
  band: developing
  composite: 42.4
  coverage:
    artifact_dirs: 19
    catalog_earned: 54.8
    catalog_earned_first_party: 12.0
    catalog_gap: 60.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.3
  facets:
    access_clarity: 65.8
    contract_governance: 35.6
    contract_quality: 44.7
    developer_ergonomics: 9.5
    discoverability: 75.0
    operational_transparency: 30.3
  previous_composite: 44.7
  provenance:
    agentic_access: derived
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 23.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/splitforms/splitforms-2026-11-03T143643.png
security:
- kind: domain-security
  name: Splitforms Domain Security
  slug: splitforms-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Splitforms Vulnerability Disclosure
  slug: splitforms-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Splitforms Trust Center
  slug: splitforms-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, HIPAA, GDPR
slug: splitforms
tags:
- Company
- Form Backend
- Developer Tools
- Free Tier
- Webhook
website: https://splitforms.com
---
