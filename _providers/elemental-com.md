---
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
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: operate
  href: https://artifacts.apis.io/elemental-com/changelog/elemental-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/elemental-com-changelog.yml
- group: agent
  href: https://artifacts.apis.io/elemental-com/llms/elemental-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/elemental-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/elemental-com/well-known/elemental-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/elemental-com-security.txt
- group: agent
  href: https://artifacts.apis.io/elemental-com/well-known/elemental-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/elemental-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/elemental-com/hosts/elemental-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/elemental-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/elemental-com/vendors/elemental-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/elemental-com-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://aws.amazon.com/trust-center/?nc2=h_dsc_aa_trc
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aws.amazon.com/terms/
- group: operate
  title: ''
  type: Support
  url: https://console.aws.amazon.com/support/home/?nc1=f_dr
- group: start
  title: ''
  type: SignUp
  url: https://signin.aws.amazon.com/signup?request_type=builderId
- group: auth
  title: ''
  type: Security
  url: https://aws.amazon.com/security/?nc2=h_dsc_aa_sec
- group: start
  title: ''
  type: Sandbox
  url: https://console.aws.amazon.com/console/home/?nc2=h_si&src=header-signin
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
- group: company
  title: ''
  type: Newsroom
  url: https://aws.amazon.com/media/?nc2=h_sol_ind_med
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.aws.amazon.com/AmazonRDS/latest/gettingstartedguide/what-is-rds
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/
- group: auth
  href: https://artifacts.apis.io/elemental-com/security/elemental-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/elemental-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aws.amazon.com/media-services/elemental/
coverage:
  checked: '2026-10-29'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contract found on discovered hosts.
  evidence:
  - status: 0
    url: https://api.elemental.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Elemental provides cloud-based media processing and video workflow solutions, enabling developers and enterprises to encode, package, and stream video at scale. The company offers APIs for transcoding, packaging, DRM, and live streaming, integrating with AWS services and supporting a range of formats and delivery methods. Their platform is designed for flexibility, automation, and high-performance media pipelines, catering to broadcasters, OTT services, and content creators.
layout: provider
modified: '2026-10-29'
name: Elemental
nav: Providers
network: true
overview: 'Elemental is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Media, Video, Cloud, Streaming, and API.


  Elemental''s developer surface includes changelog, support, signup flow, sandbox, getting-started guide, documentation, and 12 more developer resources.'
random_paper: 19
score:
  band: emerging
  composite: 23.7
  coverage:
    artifact_dirs: 8
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 42.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 33.3
    discoverability: 46.4
    operational_transparency: 26.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Elemental Com Domain Security
  slug: elemental-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: elemental-com
tags:
- Media
- Video
- Cloud
- Streaming
- API
website: https://aws.amazon.com/media-services/elemental/
---
