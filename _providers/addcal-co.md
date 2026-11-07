---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 24.7
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: Compliance
  url: https://addcal.co/security
- group: agent
  href: https://artifacts.apis.io/addcal-co/llms/addcal-co-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/addcal-co-llms.txt
- group: auth
  href: https://artifacts.apis.io/addcal-co/well-known/addcal-co-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/addcal-co-security.txt
- group: auth
  href: https://artifacts.apis.io/addcal-co/well-known/addcal-co-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/addcal-co-help-security.txt
- group: auth
  href: https://artifacts.apis.io/addcal-co/well-known/addcal-co-dev-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/addcal-co-dev-security.txt
- group: auth
  href: https://artifacts.apis.io/addcal-co/well-known/addcal-co-cdn-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/addcal-co-cdn-security.txt
- group: agent
  href: https://artifacts.apis.io/addcal-co/well-known/addcal-co-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/addcal-co-well-known.yml
- group: other
  href: https://artifacts.apis.io/addcal-co/hosts/addcal-co-hosts.yml
  title: ''
  type: Hosts
  url: hosts/addcal-co-hosts.yml
- group: other
  href: https://artifacts.apis.io/addcal-co/vendors/addcal-co-vendors.yml
  title: ''
  type: Vendors
  url: vendors/addcal-co-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://help.addcal.co/en/
- group: auth
  title: ''
  type: Security
  url: https://addcal.co/security
- group: start
  title: ''
  type: Login
  url: https://addcal.co/login
- group: operate
  title: ''
  type: ChangeLog
  url: https://addcal.co/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://help.addcal.co/en/articles/12087166-rsvp-quick-start-guide-addcal
- group: auth
  href: https://artifacts.apis.io/addcal-co/security/addcal-co-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/addcal-co-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/addcal-co/security/addcal-co-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/addcal-co-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/addcal-co/security/addcal-co-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/addcal-co-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://addcal.co/
- group: docs
  title: ''
  type: Documentation
  url: https://addcal.co/documentation
- group: docs
  title: ''
  type: APIReference
  url: https://addcal.co/documentation/api
- group: commercial
  title: ''
  type: Pricing
  url: https://addcal.co/pricing
- group: company
  title: ''
  type: Blog
  url: https://addcal.co/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://addcal.co/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://addcal.co/privacy-policy
coverage:
  checked: '2026-10-31'
  detail: Documentation page provides only HTML without a downloadable OpenAPI spec.
  evidence:
  - status: 200
    url: https://addcal.co/documentation/api
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: AddCal provides a suite of tools that let users create calendar event links, manage RSVPs, and embed calendars on websites. Their platform supports smart links, subscription calendars, and automated email invites, aiming to increase event attendance. The service offers a free tier with unlimited events and paid plans for advanced features, targeting event organizers, marketers, and developers needing seamless calendar integration.
image: https://cdn.addcal.co/static/og.webp
layout: provider
modified: '2026-10-31'
name: AddCal
nav: Providers
network: true
overview: 'AddCal is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Calendar, Event Management, Software-as-a-Service, Integration, and Productivity.


  AddCal''s developer surface includes support, changelog, getting-started guide, documentation, API reference, pricing, engineering blog, and 17 more developer resources.'
random_paper: 16
score:
  band: emerging
  composite: 18.3
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -11.5
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 17.9
    discoverability: 48.2
    operational_transparency: 13.2
  previous_composite: 29.8
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Addcal Co Domain Security
  slug: addcal-co-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Addcal Co Vulnerability Disclosure
  slug: addcal-co-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Addcal Co Trust Center
  slug: addcal-co-trust-center
  summary_line: SOC 2, PCI DSS, HIPAA, GDPR
slug: addcal-co
tags:
- Calendar
- Event Management
- Software-as-a-Service
- Integration
- Productivity
- Company
website: https://addcal.co/
---
