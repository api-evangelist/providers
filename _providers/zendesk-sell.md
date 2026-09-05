---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - authentication
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.6
  scored_at: '2026-09-04'
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
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
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
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/zendesk-sell-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/zendesk-sell-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zendesk-sell-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/zendesk-sell-authentication.yml
- group: auth
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
  title: ''
  type: Packages
  url: packages/zendesk-sell-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/zendesk-sell-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/zendesk-sell-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/zendesk-sell-security.txt
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/zendesk-sell-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/zendesk-sell-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/zendesk-sell-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.zendesk.com/trust-center/
- group: auth
  title: ''
  type: TrustCenter
  url: security/zendesk-sell-trust-center.yml
- group: auth
  title: ''
  type: Security
  url: https://www.zendesk.com/company/policies-and-guidelines/responsible-disclosure-policy/
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/zendesk-sell-problem-types.yml
- group: design
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
  title: ''
  type: Conventions
  url: conventions/zendesk-sell-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/zendesk-sell-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/zendesk-sell-cli.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/zendesk-sell-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/zendesk-sell-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/zendesk-sell-plans-pricing.yml
- group: other
  title: ''
  type: EventTypes
  url: events/zendesk-sell-events.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-05-11'
description: Zendesk Sell (formerly Base CRM) is a sales CRM platform that helps sales teams manage leads, contacts, deals, and pipelines while integrating with the broader Zendesk customer experience suite. The platform offers pipeline analytics, email and call tracking, mobile apps, and territory management for high-velocity sales organizations. The Sell API is a RESTful API authenticated via OAuth 2.0 (authorization code, implicit, password, and refresh token grants) at the api.getbase.com host that provides full CRUD access to leads, contacts, deals, accounts, notes, tasks, calls, and custom fields, alongside a premium Sync API, a client-pulled Firehose change stream and a Search API. Zendesk announced on 2025-09-09 that Sell is being retired on 2027-08-31 and is no longer sold as a standalone plan, so the API carries a hard end date.
graphqls:
- description: This directory contains a conceptual GraphQL schema for the Zendesk Sell (formerly Base CRM) Sales CRM API. The schema is derived from the [Zendesk Sell REST API reference](https://developer.zendesk.c
  name: Zendesk Sell GraphQL Schema
  slug: zendesk-sell-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zendesk-sell.png
layout: provider
modified: '2026-08-13'
name: Zendesk Sell
nav: Providers
network: true
overview: 'Zendesk Sell publishes 4 APIs on the [APIs.io](https://apis.io/) network, including (Sales CRM) API, Contacts API, Deals API, and 1 more. Tagged areas include CRM, Sales, Sales Automation, Leads, and Deals.


  Zendesk Sell''s developer surface includes authentication, documentation, API reference, pricing, signup flow, support, getting-started guide, and 33 more developer resources.'
plans:
- name: Zendesk Sell Plans Pricing
  plan_count: 0
  slug: zendesk-sell-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 1
  name: Zendesk Sell Rate Limits
  slug: zendesk-sell-rate-limits
scopes:
- name: Zendesk Sell Scopes
  scope_count: 3
  slug: zendesk-sell-scopes
  summary_line: 3 scopes · authorizationCode/implicit/password
score:
  band: strong
  composite: 57.4
  coverage:
    artifact_dirs: 25
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.7
  facets:
    access_clarity: 53.9
    commercial_clarity: 53.9
    contract_governance: 4.5
    contract_quality: 59.0
    developer_ergonomics: 74.4
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 73.7
  previous_composite: 58.1
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
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/zendesk-sell/refs/heads/main/screenshots/zendesk-sell-2026-06-20T201812.png
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
slug: zendesk-sell
tags:
- CRM
- Sales
- Sales Automation
- Leads
- Deals
- Pipeline
- Customer Experience
website: https://www.zendesk.com/sell/
---
