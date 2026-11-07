---
access_model:
  confidence: high
  label: Sales-gated onboarding, list pricing published
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://www.leadsquared.com/sales-crm-pricing/
  - https://www.leadsquared.com/marketing-automation-pricing/
  - https://www.leadsquared.com/free-trial/
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
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 35.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Leadsquared Agentic Access
  operation_count: 4
  slug: leadsquared-agentic-access
  summary_line: 4 operations · 2 acting
api_count: 1
apis:
- description: REST API for managing leads, opportunities, activities, tasks, users, campaigns, and other CRM resources in LeadSquared. Includes Sales CRM, Service CRM, Async, and Portal APIs along with Lapps, Batch
  name: LeadSquared REST API
  slug: rest-api
- description: Queued, retrying variants of the highest-volume LeadSquared write operations — Capture Leads, Update a Lead, Post an Activity on a Lead, Create a Lead and Activity, Capture Opportunities, Update an Op
  name: LeadSquared Async API
  slug: async-api
- baseURL: https://api.leadsquared.com
  baseurl_source: declared
  description: Activity events on leads
  name: LeadSquared Activities API
  slug: leadsquared-activities-api
- baseURL: https://api.leadsquared.com
  baseurl_source: declared
  description: Lead create, get, and search
  name: LeadSquared Leads API
  slug: leadsquared-leads-api
artifact_total: 19
asyncapis:
- description: ''
  name: Leadsquared Webhooks
  slug: leadsquared-webhooks
collections:
- collection_type: open
  name: LeadSquared REST Activities API
  slug: open-leadsquared-activities-api
- collection_type: open
  name: LeadSquared REST Activities Leads API
  slug: open-leadsquared-leads-api
- collection_type: open
  name: LeadSquared REST API
  slug: open-leadsquared
common:
- group: other
  href: https://artifacts.apis.io/leadsquared/capabilities/leadsquared-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/leadsquared-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/leadsquared/agentic-access/leadsquared-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/leadsquared-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/leadsquared/security/leadsquared-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/leadsquared-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/leadsquared/authentication/leadsquared-authentication.yml
  title: ''
  type: Authentication
  url: authentication/leadsquared-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/leadsquared
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/leadsquared
- group: company
  title: ''
  type: Website
  url: https://www.leadsquared.com
- group: docs
  title: ''
  type: Documentation
  url: https://apidocs.leadsquared.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.leadsquared.com/marketing-automation-pricing/
- group: start
  title: ''
  type: SignUp
  url: https://www.leadsquared.com/book-demo/
- group: start
  title: ''
  type: Login
  url: https://login.leadsquared.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://apidocs.leadsquared.com/
- group: docs
  title: ''
  type: APIReference
  url: https://apidocs.leadsquared.com/overview/
- group: start
  title: ''
  type: GettingStarted
  url: https://apidocs.leadsquared.com/getting-started/
- group: operate
  title: ''
  type: Support
  url: https://help.leadsquared.com/
- group: company
  title: ''
  type: Blog
  url: https://www.leadsquared.com/learn/
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/leadsquaredapi
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.leadsquared.com/leadsquared-terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.leadsquared.com/privacy-policy/
- group: build
  href: https://artifacts.apis.io/leadsquared/packages/leadsquared-packages.yml
  title: ''
  type: Packages
  url: packages/leadsquared-packages.yml
- group: build
  href: https://artifacts.apis.io/leadsquared/packages/leadsquared-packages.yml
  title: ''
  type: SDKs
  url: packages/leadsquared-packages.yml
- group: build
  href: https://artifacts.apis.io/leadsquared/cli/leadsquared-cli.yml
  title: ''
  type: CLI
  url: cli/leadsquared-cli.yml
- group: agent
  href: https://artifacts.apis.io/leadsquared/llms/leadsquared-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/leadsquared-llms.txt
- group: agent
  href: https://artifacts.apis.io/leadsquared/mcp/leadsquared-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/leadsquared-mcp.yml
- group: agent
  href: https://artifacts.apis.io/leadsquared/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/leadsquared/conventions/leadsquared-conventions.yml
  title: ''
  type: Conventions
  url: conventions/leadsquared-conventions.yml
- group: design
  href: https://artifacts.apis.io/leadsquared/errors/leadsquared-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/leadsquared-problem-types.yml
- group: operate
  href: https://artifacts.apis.io/leadsquared/rate-limits/leadsquared-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/leadsquared-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/leadsquared/plans/leadsquared-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/leadsquared-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/leadsquared/data-model/leadsquared-data-model.yml
  title: ''
  type: DataModel
  url: data-model/leadsquared-data-model.yml
- group: design
  href: https://artifacts.apis.io/leadsquared/asyncapi/leadsquared-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/leadsquared-webhooks.yml
- group: design
  href: https://artifacts.apis.io/leadsquared/lifecycle/leadsquared-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/leadsquared-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.leadsquared.com/
- group: operate
  href: https://artifacts.apis.io/leadsquared/changelog/leadsquared-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/leadsquared-changelog.yml
- group: design
  href: https://artifacts.apis.io/leadsquared/conformance/leadsquared-conformance.yml
  title: ''
  type: Conformance
  url: conformance/leadsquared-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.leadsquared.com/security/
- group: auth
  href: https://artifacts.apis.io/leadsquared/security/leadsquared-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/leadsquared-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/leadsquared/security/leadsquared-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/leadsquared-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.leadsquared.com/security/
created: '2026-05-11'
description: LeadSquared is a marketing automation and CRM platform that helps businesses capture, manage, nurture, and convert leads across sales, marketing, and service workflows. It offers Sales CRM, Service CRM, marketing automation, field force automation, and a no-code/low-code platform for building industry-specific customer experiences. The LeadSquared REST API provides access to core platform resources like leads, opportunities, activities, tasks, and users using API key authentication.
finops:
- has_sources: true
  method: derived
  name: Leadsquared Finops
  primary_unit: account
  service_category: ''
  slug: leadsquared-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/leadsquared.png
layout: provider
modified: '2026-08-13'
name: LeadSquared
nav: Providers
network: true
overview: 'LeadSquared publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including REST API, Activities API, Leads API, and 1 more. Tagged areas include Marketing Automation, CRM, Sales Automation, Lead Management, and Customer Engagement.


  The LeadSquared catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  LeadSquared''s developer surface includes authentication, documentation, pricing, signup flow, API reference, getting-started guide, support, and 32 more developer resources.'
plans:
- name: Leadsquared Plans Pricing
  plan_count: 2
  slug: leadsquared-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 10
  name: Leadsquared Rate Limits
  slug: leadsquared-rate-limits
rules:
- authorship: generated
  effective_rule_count: 91
  extends:
  - spectral:oas
  name: LeadSquared API Rules
  rule_count: 50
  severity_counts:
    error: 48
    hint: 0
    info: 1
    warn: 1
  slug: leadsquared-rules
score:
  band: strong
  composite: 55.5
  coverage:
    artifact_dirs: 32
    catalog_earned: 64.5
    catalog_earned_first_party: 20.0
    catalog_gap: 50.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 43.4
    contract_governance: 18.2
    contract_quality: 50.7
    developer_ergonomics: 73.2
    discoverability: 73.2
    operational_transparency: 73.7
  previous_composite: 55.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/leadsquared/leadsquared-2026-06-20T184350.png
security:
- kind: authentication
  name: Leadsquared Authentication
  slug: leadsquared-authentication
  summary_line: apiKey · 5 schemes
- kind: domain-security
  name: Leadsquared Domain Security
  slug: leadsquared-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Leadsquared Vulnerability Disclosure
  slug: leadsquared-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Leadsquared Trust Center
  slug: leadsquared-trust-center
  summary_line: ISO 27001:2022, GDPR
skill_count: 2
skills:
- name: Capture a lead and log its first activity in LeadSquared
  slug: leadsquared-capture-and-log-lead
- name: Look up a LeadSquared lead by identifier or search term
  slug: leadsquared-lookup-lead
slug: leadsquared
tags:
- Marketing Automation
- CRM
- Sales Automation
- Lead Management
- Customer Engagement
- Field Force Automation
website: https://www.leadsquared.com
---
