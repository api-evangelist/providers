---
access_model:
  confidence: high
  label: Paid · Requires approval
  onboarding: approval
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
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
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 30.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Zendesk Sell Agentic Access
  operation_count: 18
  slug: zendesk-sell-agentic-access
  summary_line: 18 operations · 12 acting
api_count: 1
apis:
- baseURL: https://api.getbase.com
  baseurl_source: declared
  description: OAuth 2.0-authenticated REST API for managing leads, contacts, deals, accounts, notes, tasks, calls, sources, stages, pipelines, and custom fields in Zendesk Sell. Bearer access tokens are passed in t
  name: Zendesk Sell (Sales CRM) API
  slug: sales-crm-api
- baseURL: https://api.getbase.com
  baseurl_source: declared
  description: Individual people and organizations.
  name: Zendesk Sell Contacts API
  slug: zendesk-sell-contacts-api
- baseURL: https://api.getbase.com
  baseurl_source: declared
  description: Sales opportunities moving through pipeline stages.
  name: Zendesk Sell Deals API
  slug: zendesk-sell-deals-api
- baseURL: https://api.getbase.com
  baseurl_source: declared
  description: Pre-qualified sales prospects.
  name: Zendesk Sell Leads API
  slug: zendesk-sell-leads-api
artifact_total: 22
collections:
- collection_type: open
  name: Zendesk Sell (Sales CRM) Contacts API
  slug: open-zendesk-sell-contacts-api
- collection_type: open
  name: Zendesk Sell (Sales CRM) Contacts Deals API
  slug: open-zendesk-sell-deals-api
- collection_type: open
  name: Zendesk Sell (Sales CRM) Contacts Leads API
  slug: open-zendesk-sell-leads-api
- collection_type: open
  name: Zendesk Sell (Sales CRM) API
  slug: open-zendesk-sell
common:
- group: other
  href: https://artifacts.apis.io/zendesk-sell/capabilities/zendesk-sell-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/zendesk-sell-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/zendesk-sell/agentic-access/zendesk-sell-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/zendesk-sell-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/zendesk-sell/security/zendesk-sell-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/zendesk-sell-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/zendesk-sell/security/zendesk-sell-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/zendesk-sell-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/zendesk-sell/authentication/zendesk-sell-authentication.yml
  title: ''
  type: Authentication
  url: authentication/zendesk-sell-authentication.yml
- group: auth
  href: https://artifacts.apis.io/zendesk-sell/scopes/zendesk-sell-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/zendesk-sell-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.zendesk.com/sell/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.zendesk.com/api-reference/sales-crm/introduction/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.zendesk.com/api-reference/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.zendesk.com/pricing/
- group: start
  title: ''
  type: Signup
  url: https://www.zendesk.com/register/
- group: start
  title: ''
  type: Login
  url: https://www.zendesk.com/login/
- group: operate
  title: ''
  type: Support
  url: https://support.zendesk.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/zendesk
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.zendesk.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.zendesk.com/documentation/sales-crm/first-call/
- group: company
  title: ''
  type: Blog
  url: https://www.zendesk.com/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.zendesk.com/company/agreements-and-terms/zendesk-customer-agreement/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.zendesk.com/company/agreements-and-terms/privacy-notice/
- group: build
  href: https://artifacts.apis.io/zendesk-sell/packages/zendesk-sell-packages.yml
  title: ''
  type: Packages
  url: packages/zendesk-sell-packages.yml
- group: build
  href: https://artifacts.apis.io/zendesk-sell/packages/zendesk-sell-packages.yml
  title: ''
  type: SDKs
  url: packages/zendesk-sell-packages.yml
- group: agent
  href: https://artifacts.apis.io/zendesk-sell/well-known/zendesk-sell-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/zendesk-sell-well-known.yml
- group: auth
  href: https://artifacts.apis.io/zendesk-sell/well-known/zendesk-sell-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/zendesk-sell-security.txt
- group: agent
  href: https://artifacts.apis.io/zendesk-sell/mcp/zendesk-sell-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/zendesk-sell-mcp.yml
- group: agent
  href: https://artifacts.apis.io/zendesk-sell/llms/zendesk-sell-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/zendesk-sell-llms.txt
- group: design
  href: https://artifacts.apis.io/zendesk-sell/conformance/zendesk-sell-conformance.yml
  title: ''
  type: Conformance
  url: conformance/zendesk-sell-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.zendesk.com/trust-center/
- group: auth
  href: https://artifacts.apis.io/zendesk-sell/security/zendesk-sell-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/zendesk-sell-trust-center.yml
- group: auth
  title: ''
  type: Security
  url: https://www.zendesk.com/company/policies-and-guidelines/responsible-disclosure-policy/
- group: design
  href: https://artifacts.apis.io/zendesk-sell/errors/zendesk-sell-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/zendesk-sell-problem-types.yml
- group: design
  href: https://artifacts.apis.io/zendesk-sell/lifecycle/zendesk-sell-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/zendesk-sell-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.zendesk.com/
- group: operate
  title: ''
  type: Deprecation
  url: https://support.zendesk.com/hc/en-us/articles/9591462550042-Announcing-the-retiring-of-Zendesk-Sell
- group: design
  href: https://artifacts.apis.io/zendesk-sell/conventions/zendesk-sell-conventions.yml
  title: ''
  type: Conventions
  url: conventions/zendesk-sell-conventions.yml
- group: operate
  href: https://artifacts.apis.io/zendesk-sell/changelog/zendesk-sell-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/zendesk-sell-changelog.yml
- group: build
  href: https://artifacts.apis.io/zendesk-sell/cli/zendesk-sell-cli.yml
  title: ''
  type: CLI
  url: cli/zendesk-sell-cli.yml
- group: design
  href: https://artifacts.apis.io/zendesk-sell/data-model/zendesk-sell-data-model.yml
  title: ''
  type: DataModel
  url: data-model/zendesk-sell-data-model.yml
- group: operate
  href: https://artifacts.apis.io/zendesk-sell/rate-limits/zendesk-sell-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/zendesk-sell-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/zendesk-sell/plans/zendesk-sell-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/zendesk-sell-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/zendesk-sell/events/zendesk-sell-events.yml
  title: ''
  type: EventTypes
  url: events/zendesk-sell-events.yml
- group: agent
  href: https://artifacts.apis.io/zendesk-sell/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-05-11'
description: Zendesk Sell (formerly Base CRM) is a sales CRM platform that helps sales teams manage leads, contacts, deals, and pipelines while integrating with the broader Zendesk customer experience suite. The platform offers pipeline analytics, email and call tracking, mobile apps, and territory management for high-velocity sales organizations. The Sell API is a RESTful API authenticated via OAuth 2.0 (authorization code, implicit, password, and refresh token grants) at the api.getbase.com host that provides full CRUD access to leads, contacts, deals, accounts, notes, tasks, calls, and custom fields, alongside a premium Sync API, a client-pulled Firehose change stream and a Search API. Zendesk announced on 2025-09-09 that Sell is being retired on 2027-08-31 and is no longer sold as a standalone plan, so the API carries a hard end date.
finops:
- has_sources: true
  method: derived
  name: Zendesk Sell Finops
  primary_unit: agent/month paid yearly
  service_category: ''
  slug: zendesk-sell-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zendesk-sell.png
layout: provider
modified: '2026-08-13'
name: Zendesk Sell
nav: Providers
network: true
overview: 'Zendesk Sell publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including (Sales CRM) API, Contacts API, Deals API, and 1 more. Tagged areas include CRM, Sales, Sales Automation, Leads, and Deals.


  The Zendesk Sell catalog on APIs.io includes 1 Spectral governance ruleset.


  Zendesk Sell''s developer surface includes authentication, documentation, API reference, pricing, signup flow, support, getting-started guide, and 34 more developer resources.'
plans:
- name: Zendesk Sell Plans Pricing
  plan_count: 11
  slug: zendesk-sell-plans-pricing
- name: Zendesk Sell Price Estimates
  plan_count: 0
  slug: zendesk-sell-price-estimates
random_paper: 9
rate_limits:
- limit_count: 1
  name: Zendesk Sell Rate Limits
  slug: zendesk-sell-rate-limits
rules:
- authorship: generated
  effective_rule_count: 95
  extends:
  - spectral:oas
  name: Zendesk Sell API Rules
  rule_count: 54
  severity_counts:
    error: 52
    hint: 0
    info: 1
    warn: 1
  slug: zendesk-sell-rules
scopes:
- name: Zendesk Sell Scopes
  scope_count: 3
  slug: zendesk-sell-scopes
  summary_line: 3 scopes · authorizationCode/implicit/password
score:
  band: exemplar
  composite: 70.1
  coverage:
    artifact_dirs: 31
    catalog_earned: 64.5
    catalog_earned_first_party: 20.0
    catalog_gap: 50.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 93.4
    contract_governance: 18.2
    contract_quality: 48.7
    developer_ergonomics: 74.4
    discoverability: 66.1
    operational_transparency: 73.7
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 70.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 45.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 22.2
screenshot: https://apis.io/screenshots/zendesk-sell/zendesk-sell-2026-06-20T201812.png
security:
- kind: authentication
  name: Zendesk Sell Authentication
  slug: zendesk-sell-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Zendesk Sell Domain Security
  slug: zendesk-sell-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Zendesk Sell Vulnerability Disclosure
  slug: zendesk-sell-vulnerability-disclosure
  summary_line: Bugcrowd · security.txt · contact published
- kind: trust-center
  name: Zendesk Sell Trust Center
  slug: zendesk-sell-trust-center
  summary_line: SOC 2 Type II, ISO 27001, ISO 27018, ISO 27701, CSA STAR, FedRAMP, HIPAA, GDPR, C5
skill_count: 3
skills:
- name: Capture and qualify a Zendesk Sell lead
  slug: zendesk-sell-capture-and-qualify-lead
- name: Move a Zendesk Sell deal through the pipeline
  slug: zendesk-sell-manage-deal-pipeline
- name: Mirror Zendesk Sell records into a local store
  slug: zendesk-sell-mirror-crm-changes
slug: zendesk-sell
tags:
- CRM
- Sales
- Sales Automation
- Leads
- Deals
- Pipelines
- Customer Experience
website: https://www.zendesk.com/sell/
---
