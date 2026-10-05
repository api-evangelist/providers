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
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.1
  scored_at: '2026-10-04'
api_count: 1
apis:
- description: Provides a unified entry point to Avid MediaCentral backend services via REST.
  name: MediaCentral Service Gateway
  slug: mediacentral-service-gateway
artifact_total: 3
common:
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/avid/refs/heads/main/changelog/avid-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/avid-changelog.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/avid/refs/heads/main/well-known/avid-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/avid-status-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/avid/refs/heads/main/well-known/avid-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/avid-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avid/refs/heads/main/hosts/avid-hosts.yml
  title: ''
  type: Hosts
  url: hosts/avid-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avid/refs/heads/main/vendors/avid-vendors.yml
  title: ''
  type: Vendors
  url: vendors/avid-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/avid/refs/heads/main/packages/avid-packages.yml
  title: ''
  type: Packages
  url: packages/avid-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.avid.com/terms.html
- group: operate
  title: ''
  type: Support
  url: https://www.avid.com/support
- group: operate
  title: ''
  type: StatusPage
  url: https://status.avid.com/
- group: auth
  title: ''
  type: Security
  url: https://www.avid.com/security/vulnerability-disclosure
- group: build
  title: ''
  type: SDKs
  url: https://my.avid.com/cpp/sdk/apc
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.avid.com/legal/privacy-policy-statement
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.avid.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.avid.com/learning/whats-new
- group: start
  title: ''
  type: GettingStarted
  url: https://www.avid.com/content-core/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://dev.avid.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/avid/refs/heads/main/security/avid-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/avid-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/avid/refs/heads/main/security/avid-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/avid-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.avid.com
coverage:
  checked: '2026-09-26'
  detail: Developer portal provides HTML documentation but no OpenAPI/AsyncAPI/GraphQL spec is publicly available.
  evidence:
  - status: 200
    url: https://developer.avid.com/connector_api/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-26'
description: Avid provides media creation and management solutions empowering audio, video, and broadcast professionals. Their platform includes MediaCentral, Content Core, and AI‑powered workflow tools used by millions of creators worldwide. Avid’s products support news, film, TV, music, and live events, earning multiple Emmy Awards and serving customers in over 60 countries.
image: https://edge.sitecorecloud.io/avidtech-d6a2e9a9/media/avidcom/home/home/og-avid-1200x630.jpg?h=630&iar=0&w=1200
layout: provider
modified: '2026-09-26'
name: Avid
nav: Providers
network: true
overview: 'Avid publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Media, Software, Audio, and Video.


  Avid''s developer surface includes changelog, support, getting-started guide, documentation, and 15 more developer resources.'
random_paper: 2
score:
  band: emerging
  composite: 25.5
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 42.9
    discoverability: 57.1
    operational_transparency: 42.1
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 25.5
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Avid Domain Security
  slug: avid-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Avid Vulnerability Disclosure
  slug: avid-vulnerability-disclosure
  summary_line: disclosure policy published
slug: avid
tags:
- Company
- Media
- Software
- Audio
- Video
website: https://www.avid.com
---
