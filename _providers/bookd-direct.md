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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Bookd provides a platform for travelers to find and book independent accommodations directly with property owners.
  name: Bookd API
  slug: bookd-api
artifact_total: 3
common:
- group: auth
  href: https://artifacts.apis.io/bookd-direct/security/bookd-direct-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/bookd-direct-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/bookd-direct/conformance/bookd-direct-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bookd-direct-conformance.yml
- group: agent
  href: https://artifacts.apis.io/bookd-direct/llms/bookd-direct-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bookd-direct-llms.txt
- group: auth
  href: https://artifacts.apis.io/bookd-direct/well-known/bookd-direct-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bookd-direct-security.txt
- group: auth
  href: https://artifacts.apis.io/bookd-direct/well-known/bookd-direct-partners-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bookd-direct-partners-security.txt
- group: agent
  href: https://artifacts.apis.io/bookd-direct/well-known/bookd-direct-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bookd-direct-well-known.yml
- group: other
  href: https://artifacts.apis.io/bookd-direct/hosts/bookd-direct-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bookd-direct-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bookd.direct/terms
- group: operate
  title: ''
  type: Support
  url: https://bookd.direct/help
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bookd.direct/privacy
- group: docs
  title: ''
  type: Documentation
  url: https://bookd.direct/guides/florida-keys
- group: auth
  href: https://artifacts.apis.io/bookd-direct/security/bookd-direct-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/bookd-direct-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/bookd-direct/security/bookd-direct-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bookd-direct-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bookd.direct/
coverage:
  checked: '2026-11-02'
  detail: The provider's website offers HTML documentation but no publicly accessible OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL specifications were found.
  evidence:
  - status: 200
    url: https://bookd.direct/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: Bookd is a platform that helps travelers find and book independent hotels, B&Bs, guesthouses, and vacation rentals directly with the property. It connects guests with property owners through its website and AI assistants like ChatGPT and Claude, enabling direct bookings without holding guest money. Bookd is operated by Caius Data LLC in Wyoming, USA, with an EU representative in Ireland.
image: https://bookd.direct/brand/og-default.png
layout: provider
modified: '2026-11-02'
name: Bookd
nav: Providers
network: true
overview: 'Bookd is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Booking, Direct Booking, Independent Hotels, B&B, and Rentals.


  Bookd''s developer surface includes support, documentation, and 12 more developer resources.'
random_paper: 7
score:
  band: emerging
  composite: 13.6
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.1
    operational_transparency: 10.5
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bookd Direct Domain Security
  slug: bookd-direct-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Bookd Direct Vulnerability Disclosure
  slug: bookd-direct-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: bookd-direct
tags:
- Booking
- Direct Booking
- Independent Hotels
- B&B
- Rentals
- Property Owners
website: https://bookd.direct/
---
