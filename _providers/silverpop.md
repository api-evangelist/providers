---
access_model:
  confidence: high
  label: Public docs, sales-gated onboarding
  onboarding: unknown
  pricing: paid
  public: true
  source:
  - https://www.acoustic.com/pricing
  - https://developer.goacoustic.com/acoustic-campaign/reference/api-developers-guide-and-legal-information
  trial: false
  try_now: false
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 25.5
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Silverpop Agentic Access
  operation_count: 17
  slug: silverpop-agentic-access
  summary_line: 17 operations · 7 acting
api_count: 1
apis:
- description: OAuth 2.0 token management
  name: Silverpop Authentication API
  slug: silverpop-authentication-api
- description: Email campaign management
  name: Silverpop Campaigns API
  slug: silverpop-campaigns-api
- description: Contact (recipient) list management
  name: Silverpop Contacts API
  slug: silverpop-contacts-api
- description: Marketing automation program management
  name: Silverpop Programs API
  slug: silverpop-programs-api
- description: Campaign reporting and analytics
  name: Silverpop Reports API
  slug: silverpop-reports-api
- description: Transactional email and SMS messaging
  name: Silverpop Transactional API
  slug: silverpop-transactional-api
artifact_total: 27
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Silverpop Engage API (Acoustic Campaign) Authentication API
  slug: open-silverpop-authentication-api
- collection_type: open
  name: Silverpop Engage API (Acoustic Campaign) Authentication Campaigns API
  slug: open-silverpop-campaigns-api
- collection_type: open
  name: Silverpop Engage API (Acoustic Campaign) Authentication Contacts API
  slug: open-silverpop-contacts-api
- collection_type: open
  name: Silverpop Engage API (Acoustic Campaign) Authentication Programs API
  slug: open-silverpop-programs-api
- collection_type: open
  name: Silverpop Engage API (Acoustic Campaign) Authentication Reports API
  slug: open-silverpop-reports-api
- collection_type: open
  name: Silverpop Engage API (Acoustic Campaign) Authentication Transactional API
  slug: open-silverpop-transactional-api
- collection_type: open
  name: Silverpop Engage API (Acoustic Campaign)
  slug: open-silverpop
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/silverpop-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/silverpop-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/silverpop-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/silverpop-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/silverpop-systems-inc
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Silverpop
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.goacoustic.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.goacoustic.com/acoustic-campaign/reference/overview
- group: auth
  title: ''
  type: Authentication
  url: https://developer.goacoustic.com/acoustic-campaign/docs/authentication
- group: docs
  title: ''
  type: APIReference
  url: https://developer.goacoustic.com/acoustic-campaign/reference/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.goacoustic.com/acoustic-campaign/reference/getting-started-with-oauth
- group: build
  title: ''
  type: Postman
  url: https://documenter.getpostman.com/view/1643559/2sBXqQEHNz
- group: operate
  title: ''
  type: StatusPage
  url: https://status.goacoustic.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.acoustic.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.acoustic.com/resources/blog
- group: operate
  title: ''
  type: Support
  url: https://help.goacoustic.com
- group: start
  title: ''
  type: SignUp
  url: https://www.acoustic.com/demo
- group: start
  title: ''
  type: Login
  url: https://login.goacoustic.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.acoustic.com/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.acoustic.com/privacy-notice
- group: build
  title: ''
  type: Packages
  url: packages/silverpop-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/silverpop-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/silverpop-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: well-known/silverpop-api-catalog.json
- group: agent
  title: ''
  type: MCPServer
  url: mcp/silverpop-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/silverpop-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/silverpop-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/silverpop-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/silverpop-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/silverpop-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/silverpop-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/silverpop-conventions.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/silverpop-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/silverpop-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/silverpop-finops.yml
created: '2026-05-02'
description: 'Silverpop Engage is the email marketing, marketing automation and transactional messaging API now sold as Acoustic Campaign, and one of the longest-lived commercial marketing APIs still in production. The operation names an integrator calls today — AddRecipient, ScheduleMailing, RawRecipientDataExport — are the original Silverpop names, unchanged through acquisition by IBM in 2014 (as Watson Campaign Automation) and the carve-out to Acoustic in 2019; silverpop.com now 301s to acoustic.com and the developer portal lives at developer.goacoustic.com. Two surfaces sit behind one per-tenant host: a single-endpoint XML API at /XMLAPI carrying roughly sixty operations across contact databases, contact lists, relational tables, scoring models, templates and mailings, dynamic content and reporting, and a narrower JSON REST API at /rest with eleven resources including gdpr_jobs. Authentication is OAuth 2.0 with the refresh_token grant only and no scope model; the binding runtime limit
  is a cap of ten concurrent requests per organization rather than a request rate.'
examples:
- key_count: 4
  name: Silverpop Add Contact Example
  slug: silverpop-add-contact-example
finops:
- name: Silverpop Finops
  service_category: API
  slug: silverpop-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/silverpop.png
json_schemas:
- name: Silverpop Contact
  property_count: 8
  slug: silverpop-contact
json_structures:
- name: Silverpop Contact Structure
  property_count: 0
  slug: silverpop-contact-structure
jsonld:
- class_count: 25
  name: Silverpop Context
  property_count: 4
  slug: silverpop-context
layout: provider
mcp_servers:
- description: ''
  name: Silverpop MCP Server
  slug: silverpop-mcp-server
modified: '2026-08-13'
name: Silverpop
nav: Providers
network: true
overview: 'Silverpop publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Campaigns API, Contacts API, and 3 more. Tagged areas include Email Marketing, Marketing Automation, Campaign Management, Digital Marketing, and Transactional Email.


  The Silverpop catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Silverpop''s developer surface includes authentication, documentation, API reference, getting-started guide, pricing, engineering blog, support, and 28 more developer resources.'
plans:
- name: Silverpop Plans Pricing
  plan_count: 3
  slug: silverpop-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 2
  name: Silverpop Rate Limits
  slug: silverpop-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Silverpop API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: silverpop-jsonschema-spectral-rules
- effective_rule_count: 48
  extends:
  - spectral:oas
  name: Silverpop API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 6
  slug: silverpop-rules
score:
  band: strong
  composite: 64.0
  coverage:
    artifact_dirs: 25
    catalog_gap: 42.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 31.8
    contract_quality: 59.9
    developer_ergonomics: 48.8
    discoverability: 75.9
    governance: 31.8
    operational_transparency: 47.4
  previous_composite: 64.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 51.4
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/silverpop/refs/heads/main/screenshots/silverpop-2026-06-20T193920.png
security:
- kind: authentication
  name: Silverpop Authentication
  slug: silverpop-authentication
  summary_line: oauth2/http · 2 schemes
- kind: domain-security
  name: Silverpop Domain Security
  slug: silverpop-domain-security
  summary_line: TLSv1.3 · HSTS
slug: silverpop
tags:
- Email Marketing
- Marketing Automation
- Campaign Management
- Digital Marketing
- Transactional Email
- SMS
- Customer Data
- Contact Management
- Mobile Push
- Marketing Analytics
website: https://developer.goacoustic.com
---
