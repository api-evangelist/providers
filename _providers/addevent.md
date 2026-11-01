---
agent_readiness:
  band: agent-aware
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 22.6
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Addevent Agentic Access
  operation_count: 22
  slug: addevent-agentic-access
  summary_line: 22 operations · 10 acting
api_count: 1
apis:
- baseURL: https://api.addevent.com/calevent/v2
  baseurl_source: declared
  description: The Calendar subscribers API from AddEvent — 2 operation(s) for calendar subscribers.
  name: AddEvent Calendar subscribers API
  slug: addevent-calendar-subscribers-api
- baseURL: https://api.addevent.com/calevent/v2
  baseurl_source: declared
  description: The Calendars API from AddEvent — 2 operation(s) for calendars.
  name: AddEvent Calendars API
  slug: addevent-calendars-api
- baseURL: https://api.addevent.com/calevent/v2
  baseurl_source: declared
  description: The Events API from AddEvent — 2 operation(s) for events.
  name: AddEvent Events API
  slug: addevent-events-api
- baseURL: https://api.addevent.com/calevent/v2
  baseurl_source: declared
  description: The RSVP attendees API from AddEvent — 3 operation(s) for rsvp attendees.
  name: AddEvent RSVP attendees API
  slug: addevent-rsvp-attendees-api
- baseURL: https://api.addevent.com/calevent/v2
  baseurl_source: declared
  description: The Templates API from AddEvent — 3 operation(s) for templates.
  name: AddEvent Templates API
  slug: addevent-templates-api
- baseURL: https://api.addevent.com/calevent/v2
  baseurl_source: declared
  description: The Timezones API from AddEvent — 1 operation(s) for timezones.
  name: AddEvent Timezones API
  slug: addevent-timezones-api
artifact_total: 17
common:
- group: auth
  href: https://artifacts.apis.io/addevent/well-known/addevent-addevent-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/addevent-addevent-security.txt
- group: agent
  href: https://artifacts.apis.io/addevent/agentic-access/addevent-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/addevent-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/addevent/plans/addevent-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/addevent-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/addevent/rules/addevent-rules.yml
  title: ''
  type: Spectral
  url: rules/addevent-rules.yml
- group: design
  href: https://artifacts.apis.io/addevent/json-ld/addevent-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/addevent-context.jsonld
- group: design
  href: https://artifacts.apis.io/addevent/vocabulary/addevent-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/addevent-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/addevent/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/addevent/data-model/addevent-data-model.yml
  title: ''
  type: DataModel
  url: data-model/addevent-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.addevent.com:443/c/legal/security
- group: auth
  href: https://artifacts.apis.io/addevent/authentication/addevent-authentication.yml
  title: ''
  type: Authentication
  url: authentication/addevent-authentication.yml
- group: design
  href: https://artifacts.apis.io/addevent/errors/addevent-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/addevent-problem-types.yml
- group: design
  href: https://artifacts.apis.io/addevent/conformance/addevent-conformance.yml
  title: ''
  type: Conformance
  url: conformance/addevent-conformance.yml
- group: agent
  href: https://artifacts.apis.io/addevent/llms/addevent-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/addevent-llms.txt
- group: auth
  href: https://artifacts.apis.io/addevent/well-known/addevent-jobs-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/addevent-jobs-security.txt
- group: agent
  href: https://artifacts.apis.io/addevent/well-known/addevent-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/addevent-well-known.yml
- group: other
  href: https://artifacts.apis.io/addevent/hosts/addevent-hosts.yml
  title: ''
  type: Hosts
  url: hosts/addevent-hosts.yml
- group: other
  href: https://artifacts.apis.io/addevent/vendors/addevent-vendors.yml
  title: ''
  type: Vendors
  url: vendors/addevent-vendors.yml
- group: build
  href: https://artifacts.apis.io/addevent/packages/addevent-packages.yml
  title: ''
  type: SDKs
  url: packages/addevent-packages.yml
- group: build
  href: https://artifacts.apis.io/addevent/packages/addevent-packages.yml
  title: ''
  type: Packages
  url: packages/addevent-packages.yml
- group: operate
  title: ''
  type: Support
  url: https://help.addevent.com
- group: operate
  title: ''
  type: StatusPage
  url: https://addevent.statuspage.io/
- group: auth
  title: ''
  type: Security
  url: https://www.addevent.com:443/c/legal/security
- group: operate
  title: ''
  type: Roadmap
  url: https://www.addevent.com/integrations/1684/roadmap/zapier
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AddEventinc
- group: operate
  title: ''
  type: ChangeLog
  url: https://help.addevent.com/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.addevent.com/reference/getting-started
- group: auth
  href: https://artifacts.apis.io/addevent/security/addevent-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/addevent-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/addevent/security/addevent-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/addevent-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/addevent/security/addevent-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/addevent-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.addevent.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.addevent.com/c/documentation
- group: docs
  title: ''
  type: APIReference
  url: https://www.addevent.com/c/documentation/calendar-events-api
- group: commercial
  title: ''
  type: Pricing
  url: https://www.addevent.com/c/plans-and-pricing
- group: company
  title: ''
  type: Blog
  url: https://www.addevent.com/blog
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.addevent.com/signup?source=homepage&position=navigation&btn=signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.addevent.com/c/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.addevent.com/c/legal/privacy
created: '2026-10-27'
description: AddEvent provides calendar integration tools that let websites and apps add events to users’ calendars via simple buttons, dynamic links, and subscription calendars. Their platform includes RSVP forms, analytics, and marketing features to reduce no‑shows and improve event attendance. Developers can access a RESTful Calendar Events API, documentation, and SDKs to embed scheduling functionality across multiple platforms.
image: https://cdn.addevent.com/web/images/opengraph-image.png
jsonld:
- class_count: 15
  name: Addevent Context
  property_count: 74
  slug: addevent-context
layout: provider
modified: '2026-10-27'
name: AddEvent
nav: Providers
network: true
overview: 'AddEvent publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Calendar subscribers API, Calendars API, Events API, and 3 more. Tagged areas include Calendar, Integration, Marketing, API, and SaaS.


  The AddEvent catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  AddEvent''s developer surface includes authentication, support, changelog, getting-started guide, documentation, API reference, pricing, and 30 more developer resources.'
plans:
- name: Addevent Plans Pricing
  plan_count: 7
  slug: addevent-plans-pricing
random_paper: 3
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: AddEvent API Rules
  rule_count: 14
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 1
  slug: addevent-rules
score:
  band: strong
  composite: 63.1
  coverage:
    artifact_dirs: 20
    catalog_earned: 65.8
    catalog_earned_first_party: 12.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 92.1
    contract_governance: 22.0
    contract_quality: 57.0
    developer_ergonomics: 56.5
    discoverability: 66.1
    operational_transparency: 52.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 6
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Addevent Authentication
  slug: addevent-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Addevent Domain Security
  slug: addevent-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Addevent Vulnerability Disclosure
  slug: addevent-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Addevent Trust Center
  slug: addevent-trust-center
  summary_line: SOC 2, HIPAA, GDPR
skill_count: 3
skills:
- name: addevent-create-and-retrieve-calendar
  slug: addevent-create-and-retrieve-calendar
- name: addevent-manage-event
  slug: addevent-manage-event
- name: addevent-rsvp-attendee-create-and-retrieve
  slug: addevent-rsvp-attendee-create-and-retrieve
slug: addevent
tags:
- Calendar
- Integration
- Marketing
- API
- SaaS
- Events
website: https://www.addevent.com/
---
