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
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    idempotency: documented
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
  score: 31.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://invoca.net
  baseurl_source: declared
  description: Messages
  name: Invoca Messages API
  slug: invoca-messages-api
- baseURL: https://invoca.net
  baseurl_source: declared
  description: Phone Numbers
  name: Invoca Phone Numbers API
  slug: invoca-phone-numbers-api
artifact_total: 12
common:
- group: other
  href: https://artifacts.apis.io/invoca/capabilities/invoca-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/invoca-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/invoca/overlays/invoca-sms-messaging-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/invoca-sms-messaging-overlay.yaml
- group: company
  title: ''
  type: Website
  url: http://www.invoca.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.invoca.net/en/latest/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.invoca.net/en/latest/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.invoca.net/en/latest/api_documentation/index.html
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.invoca.net/en/latest/basics/index.html
- group: operate
  title: ''
  type: Support
  url: https://community.invoca.com/
- group: company
  title: ''
  type: Blog
  url: https://www.invoca.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Invoca
- group: commercial
  title: ''
  type: Pricing
  url: https://www.invoca.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.invoca.com/trial
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.invoca.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.invoca.com/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.invoca.com
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.invoca.com
- group: auth
  title: ''
  type: Compliance
  url: https://www.invoca.com/product/security-compliance
- group: auth
  href: https://artifacts.apis.io/invoca/authentication/invoca-authentication.yml
  title: ''
  type: Authentication
  url: authentication/invoca-authentication.yml
- group: design
  href: https://artifacts.apis.io/invoca/conventions/invoca-conventions.yml
  title: ''
  type: Conventions
  url: conventions/invoca-conventions.yml
- group: design
  href: https://artifacts.apis.io/invoca/conventions/invoca-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/invoca-conventions.yml
- group: design
  href: https://artifacts.apis.io/invoca/lifecycle/invoca-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/invoca-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/invoca/lifecycle/invoca-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/invoca-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/invoca/conformance/invoca-conformance.yml
  title: ''
  type: Conformance
  url: conformance/invoca-conformance.yml
- group: design
  href: https://artifacts.apis.io/invoca/errors/invoca-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/invoca-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/invoca/mcp/invoca-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/invoca-mcp.yml
- group: auth
  href: https://artifacts.apis.io/invoca/security/invoca-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/invoca-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/invoca/llms/invoca-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/invoca-llms.txt
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.invoca.com/latest-releases
- group: operate
  href: https://artifacts.apis.io/invoca/changelog/invoca-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/invoca-changelog.yml
- group: build
  href: https://artifacts.apis.io/invoca/packages/invoca-packages.yml
  title: ''
  type: Packages
  url: packages/invoca-packages.yml
- group: commercial
  href: https://artifacts.apis.io/invoca/plans/invoca-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/invoca-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/invoca/rate-limits/invoca-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/invoca-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/invoca/components/invoca-components.yml
  title: ''
  type: Components
  url: components/invoca-components.yml
- group: start
  href: https://artifacts.apis.io/invoca/sandbox/invoca-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/invoca-sandbox.yml
- group: design
  href: https://artifacts.apis.io/invoca/data-model/invoca-data-model.yml
  title: ''
  type: DataModel
  url: data-model/invoca-data-model.yml
- group: agent
  href: https://artifacts.apis.io/invoca/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Invoca is an AI-powered revenue execution platform that connects marketing and sales teams by tracking and analyzing inbound phone calls across the buying journey. Its call tracking, conversation intelligence, and signal analytics attribute phone conversations back to the paid media, campaigns, and digital touchpoints that drove them, so revenue teams can optimize ad spend and improve buyer experiences. For developers, Invoca publishes a REST developer platform (developers.invoca.net) with date-versioned APIs covering call transactions, signals, call ingestion, RingPool number allocation, network integration, and pre-call insight, authenticated with self-serve Invoca API tokens or HTTP Basic.
finops:
- has_sources: true
  method: derived
  name: Invoca Finops
  primary_unit: ''
  service_category: ''
  slug: invoca-finops
  template: true
image: https://www.invoca.com/favicon.ico
layout: provider
modified: '2026-08-13'
name: Invoca
nav: Providers
network: true
overview: 'Invoca publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Messages API and Phone Numbers API. Tagged areas include Company, Artificial Intelligence, Call Tracking, Conversation Intelligence, and Marketing.


  The Invoca catalog on APIs.io includes 1 Spectral governance ruleset.


  Invoca''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 29 more developer resources.'
plans:
- name: Invoca Plans Pricing
  plan_count: 5
  slug: invoca-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Invoca Rate Limits
  slug: invoca-rate-limits
rules:
- authorship: generated
  effective_rule_count: 72
  extends:
  - spectral:oas
  name: Invoca API Rules
  rule_count: 31
  severity_counts:
    error: 29
    hint: 0
    info: 1
    warn: 1
  slug: invoca-rules
score:
  band: strong
  composite: 54.8
  coverage:
    artifact_dirs: 29
    catalog_earned: 53.5
    catalog_earned_first_party: 12.0
    catalog_gap: 61.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 78.9
    contract_governance: 18.2
    contract_quality: 38.6
    developer_ergonomics: 66.1
    discoverability: 73.2
    operational_transparency: 42.1
  previous_composite: 54.8
  provenance:
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
    - jurisdiction: US
      standard: ccpa
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 27.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/invoca/invoca-2026-07-25T222753.png
security:
- kind: authentication
  name: Invoca Authentication
  slug: invoca-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Invoca Domain Security
  slug: invoca-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Invoca Trust Center
  slug: invoca-trust-center
  summary_line: SOC 2 Type 2, ISO 27001, PCI DSS, HIPAA, GDPR, CCPA, FSQS, TRUSTe
skill_count: 3
skills:
- name: Ingest an externally originated call into Invoca
  slug: invoca-ingest-call
- name: Report a conversion Signal against an Invoca call
  slug: invoca-report-signal
- name: Send and track SMS through the Invoca SMS Messaging API
  slug: invoca-sms-messaging
slug: invoca
tags:
- Company
- Artificial Intelligence
- Call Tracking
- Conversation Intelligence
- Marketing
- Attribution
- Revenue
- Telephony
- Analytics
website: http://www.invoca.com
---
