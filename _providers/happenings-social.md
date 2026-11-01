---
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
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 16.9
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 6
common:
- group: commercial
  href: https://artifacts.apis.io/happenings-social/plans/happenings-social-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/happenings-social-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/happenings-social/security/happenings-social-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/happenings-social-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/happenings-social/llms/happenings-social-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/happenings-social-llms.txt
- group: auth
  href: https://artifacts.apis.io/happenings-social/well-known/happenings-social-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/happenings-social-security.txt
- group: agent
  href: https://artifacts.apis.io/happenings-social/well-known/happenings-social-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/happenings-social-well-known.yml
- group: other
  href: https://artifacts.apis.io/happenings-social/hosts/happenings-social-hosts.yml
  title: ''
  type: Hosts
  url: hosts/happenings-social-hosts.yml
- group: other
  href: https://artifacts.apis.io/happenings-social/vendors/happenings-social-vendors.yml
  title: ''
  type: Vendors
  url: vendors/happenings-social-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.happenings.social/
- group: auth
  href: https://artifacts.apis.io/happenings-social/security/happenings-social-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/happenings-social-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/happenings-social/security/happenings-social-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/happenings-social-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://happenings.social/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://happenings.social/developer
- group: docs
  title: ''
  type: Documentation
  url: https://happenings.social/docs
- group: docs
  title: ''
  type: APIReference
  url: https://happenings.social/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://happenings.social/getting-started
- group: operate
  title: ''
  type: Support
  url: https://happenings.social/support
- group: company
  title: ''
  type: Blog
  url: https://happenings.social/blog
- group: operate
  title: ''
  type: Roadmap
  url: https://happenings.social/roadmap
- group: commercial
  title: ''
  type: Pricing
  url: https://happenings.social/pricing
- group: start
  title: ''
  type: SignUp
  url: https://happenings.social/auth/register
- group: commercial
  title: ''
  type: TermsOfService
  url: https://happenings.social/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://happenings.social/legal/privacy
coverage:
  checked: '2026-10-30'
  detail: The provider's public help site contains human‑readable documentation but no published OpenAPI, AsyncAPI, GraphQL, or other machine‑readable spec.
  evidence:
  - status: 200
    url: https://help.happenings.social/help
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: Happenings Social is a modern platform that enables individuals and communities to create, share, and discover social events and gatherings. Users can browse events by location, category, or interest, RSVP, and interact with organizers. The service offers tools for event promotion, ticketing, and real‑time updates, fostering vibrant local experiences. Its API provides access to event listings, user profiles, and attendance data, allowing developers to integrate social event functionality into their applications.
image: https://media.happenings.social/image/v2/w128/organization/9c591a3f-4dc6-4a53-8a3d-f486713cafc0_original.jpg
layout: provider
modified: '2026-10-30'
name: happenings-social
nav: Providers
network: true
overview: 'happenings-social is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Social, Events, Platform, and Community.


  happenings-social''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 15 more developer resources.'
plans:
- name: Happenings Social Plans Pricing
  plan_count: 3
  slug: happenings-social-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 0
  name: Happenings Social Rate Limits
  slug: happenings-social-rate-limits
scopes:
- name: Happenings Social Scopes
  scope_count: 0
  slug: happenings-social-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 36.3
  coverage:
    artifact_dirs: 18
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 45.2
    discoverability: 48.2
    operational_transparency: 31.6
  provenance:
    conformance: unknown
    mcp: derived
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
  name: Happenings Social Authentication
  slug: happenings-social-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Happenings Social Domain Security
  slug: happenings-social-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Happenings Social Vulnerability Disclosure
  slug: happenings-social-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: happenings-social
tags:
- Company
- Social
- Events
- Platform
- Community
website: https://happenings.social/
---
