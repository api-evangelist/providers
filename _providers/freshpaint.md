---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 40.0
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Freshpaint Agentic Access
  operation_count: 1
  slug: freshpaint-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 2
apis:
- description: Destinations are the marketing, analytics, advertising, and data-warehouse tools Freshpaint forwards collected events to. Destinations are configured in the Freshpaint app; per-event routing is contro
  name: Freshpaint Destinations
  slug: freshpaint-destinations
- description: The Events API from Freshpaint — 1 operation(s) for events.
  name: Freshpaint Events API
  slug: freshpaint-events-api
artifact_total: 12
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Freshpaint HTTP Events API
  slug: open-freshpaint-events-api
- collection_type: open
  name: Freshpaint HTTP API
  slug: open-freshpaint
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/freshpaint-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/freshpaint-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/freshpaint-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/freshpaint-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/freshpaint-io
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/freshpaint
- group: company
  title: ''
  type: Website
  url: https://www.freshpaint.io
- group: docs
  title: ''
  type: Documentation
  url: https://documentation.freshpaint.io
- group: commercial
  title: ''
  type: Plans
  url: plans/freshpaint-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/freshpaint-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/freshpaint-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.freshpaint.io/blog
- group: build
  title: ''
  type: Packages
  url: packages/freshpaint-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/freshpaint-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/freshpaint-llms.txt
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/freshpaint-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.freshpaint.io
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/freshpaint-changelog.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/freshpaint-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/freshpaint-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/freshpaint-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.freshpaint.io/
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://www.freshpaint.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.freshpaint.io/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.freshpaint.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.freshpaint.io/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://www.freshpaint.io/contact-us
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.freshpaint.io/faq
created: '2026-06-25'
description: Freshpaint is a healthcare privacy platform and customer-data platform that collects first-party event data and governs it for HIPAA compliance before fanning it out to 100+ marketing, analytics, and data destinations. Its server-side HTTP API ingests track, identify, page, and screen events at https://api.perfalytics.com/track authenticated with an environment token.
finops:
- name: Freshpaint Finops
  service_category: Analytics
  slug: freshpaint-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/freshpaint.png
layout: provider
modified: '2026-08-13'
name: Freshpaint
nav: Providers
network: true
overview: 'Freshpaint publishes 1 API on the [APIs.io](https://apis.io/) network: Events API. Tagged areas include Customer Data Platform, Event Tracking, Healthcare, HIPAA, and Privacy.


  Freshpaint''s developer surface includes authentication, documentation, engineering blog, changelog, pricing, signup flow, support, and 22 more developer resources.'
plans:
- name: Freshpaint Plans Pricing
  plan_count: 3
  slug: freshpaint-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 2
  name: Freshpaint Rate Limits
  slug: freshpaint-rate-limits
score:
  band: strong
  composite: 56.6
  delta: 0.0
  facets:
    access_clarity: 86.8
    commercial_clarity: 86.8
    contract_governance: 30.3
    contract_quality: 58.0
    developer_ergonomics: 28.0
    discoverability: 75.9
    governance: 30.3
    operational_transparency: 39.5
  previous_composite: 56.6
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
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 37.5
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/freshpaint/refs/heads/main/screenshots/freshpaint-2026-07-25T215208.png
security:
- kind: authentication
  name: Freshpaint Authentication
  slug: freshpaint-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Freshpaint Domain Security
  slug: freshpaint-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Freshpaint Trust Center
  slug: freshpaint-trust-center
  summary_line: SOC 2 Type 2, HIPAA
slug: freshpaint
tags:
- Customer Data Platform
- Event Tracking
- Healthcare
- HIPAA
- Privacy
- Analytics
website: https://www.freshpaint.io
---
