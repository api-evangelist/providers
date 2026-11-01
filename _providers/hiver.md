---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 46.0
  scored_at: '2026-10-31'
api_count: 1
apis:
- baseURL: https://api2.hiverhq.com/v1
  baseurl_source: declared
  description: The Conversations API from Hiver — 4 operation(s) for conversations.
  name: Hiver Conversations API
  slug: hiver-conversations-api
- baseURL: https://api2.hiverhq.com/v1
  baseurl_source: declared
  description: The Inbox API from Hiver — 6 operation(s) for inbox.
  name: Hiver Inbox API
  slug: hiver-inbox-api
artifact_total: 14
asyncapis:
- description: ''
  name: Hiver Webhooks
  slug: hiver-webhooks
common:
- group: company
  title: ''
  type: BlogRSS
  url: https://hiverhq.com/feed
- group: other
  href: https://artifacts.apis.io/hiver/capabilities/hiver-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/hiver-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/hiver/overlays/hiver-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/hiver-api-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://hiverhq.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.hiverhq.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.hiverhq.com/hiver-api
- group: docs
  title: ''
  type: APIReference
  url: https://developer.hiverhq.com/api-runner/hiverhq/hiver-api
- group: start
  title: ''
  type: GettingStarted
  url: https://help.hiverhq.com/hiver-api/hiver-api
- group: operate
  title: ''
  type: Support
  url: https://help.hiverhq.com/
- group: company
  title: ''
  type: Blog
  url: https://hiverhq.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GrexIt
- group: operate
  title: ''
  type: Roadmap
  url: https://updates.hiverhq.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://updates.hiverhq.com/changelog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.hiverhq.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://hiverhq.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://hiverhq.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://hiverhq.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://hiverhq.com/privacy
- group: auth
  title: ''
  type: Security
  url: https://hiverhq.com/disclosure
- group: auth
  title: ''
  type: TrustCenter
  url: https://trustcenter.hiverhq.com/
- group: auth
  title: ''
  type: Compliance
  url: https://hiverhq.com/security-center
- group: design
  href: https://artifacts.apis.io/hiver/lifecycle/hiver-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/hiver-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/hiver/changelog/hiver-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/hiver-changelog.yml
- group: commercial
  href: https://artifacts.apis.io/hiver/plans/hiver-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/hiver-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/hiver/rate-limits/hiver-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/hiver-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/hiver/conformance/hiver-conformance.yml
  title: ''
  type: Conformance
  url: conformance/hiver-conformance.yml
- group: auth
  href: https://artifacts.apis.io/hiver/security/hiver-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/hiver-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/hiver/security/hiver-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/hiver-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/hiver/security/hiver-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hiver-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/hiver/well-known/hiver-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/hiver-well-known.yml
- group: agent
  href: https://artifacts.apis.io/hiver/llms/hiver-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/hiver-llms.txt
- group: build
  href: https://artifacts.apis.io/hiver/packages/hiver-packages.yml
  title: ''
  type: Packages
  url: packages/hiver-packages.yml
- group: agent
  href: https://artifacts.apis.io/hiver/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-22'
description: 'Hiver (Hiver Inc., originally GrexIt) builds an AI-powered customer service platform for teams that run support out of shared email addresses. It ships in two forms: Hiver in Gmail, a Chrome-extension helpdesk that turns shared inboxes like support@ and billing@ into assignable, SLA-tracked queues without leaving Gmail; and Hiver Omni, a standalone omnichannel platform covering email, live chat, Slack, voice, WhatsApp, a help center and a customer portal. Hiver publishes a public REST API for Shared Inboxes, conversations, users, tags and internal notes, documented on a Theneo developer portal with a downloadable OpenAPI 3.0.2 contract, and gates API access to its Pro plan and above.'
finops:
- has_sources: true
  method: derived
  name: Hiver Finops
  primary_unit: user/month
  service_category: ''
  slug: hiver-finops
  template: false
image: https://hiverhq.com/wp-content/uploads/2025/05/hiver-dark-logo@2x.png
layout: provider
modified: '2026-10-06'
name: Hiver
nav: Providers
network: true
overview: 'Hiver publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Conversations API and Inbox API. Tagged areas include Company, Customer Service, Help Desk, Shared Inbox, and Email.


  The Hiver catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Hiver''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, changelog, pricing, and 26 more developer resources.'
plans:
- name: Hiver Plans Pricing
  plan_count: 4
  slug: hiver-plans-pricing
- name: Hiver Price Estimates
  plan_count: 0
  slug: hiver-price-estimates
random_paper: 14
rate_limits:
- limit_count: 2
  name: Hiver Rate Limits
  slug: hiver-rate-limits
score:
  band: strong
  composite: 65.1
  coverage:
    artifact_dirs: 24
    catalog_earned: 60.0
    catalog_earned_first_party: 20.0
    catalog_gap: 55.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 7.9
  facets:
    access_clarity: 100.0
    contract_governance: 18.2
    contract_quality: 49.1
    developer_ergonomics: 58.9
    discoverability: 66.1
    operational_transparency: 73.7
  previous_composite: 57.2
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 32.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/hiver/hiver-2026-09-02T145747.png
security:
- kind: authentication
  name: Hiver Authentication
  slug: hiver-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Hiver Domain Security
  slug: hiver-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Hiver Vulnerability Disclosure
  slug: hiver-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Hiver Trust Center
  slug: hiver-trust-center
  summary_line: ISO/IEC 27001, SOC 2 Type II, HIPAA
skill_count: 3
skills:
- name: hiver-manage-inbox-tags
  slug: hiver-manage-inbox-tags
- name: hiver-post-internal-note
  slug: hiver-post-internal-note
- name: hiver-triage-shared-inbox
  slug: hiver-triage-shared-inbox
slug: hiver
tags:
- Company
- Customer Service
- Help Desk
- Shared Inbox
- Email
- Ticketing
- Collaboration
- Gmail
- Google Workspace
- Omnichannel
- Live Chat
- Software-as-a-Service
- Artificial Intelligence
website: https://hiverhq.com/
---
