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
  score: 13.9
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: Compliance
  url: https://aws.amazon.com/compliance/
- group: agent
  href: https://artifacts.apis.io/amazon-chime/llms/amazon-chime-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/amazon-chime-llms.txt
- group: auth
  href: https://artifacts.apis.io/amazon-chime/well-known/amazon-chime-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/amazon-chime-security.txt
- group: agent
  href: https://artifacts.apis.io/amazon-chime/well-known/amazon-chime-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/amazon-chime-well-known.yml
- group: other
  href: https://artifacts.apis.io/amazon-chime/hosts/amazon-chime-hosts.yml
  title: ''
  type: Hosts
  url: hosts/amazon-chime-hosts.yml
- group: other
  href: https://artifacts.apis.io/amazon-chime/vendors/amazon-chime-vendors.yml
  title: ''
  type: Vendors
  url: vendors/amazon-chime-vendors.yml
- group: build
  href: https://artifacts.apis.io/amazon-chime/packages/amazon-chime-packages.yml
  title: ''
  type: SDKs
  url: packages/amazon-chime-packages.yml
- group: build
  href: https://artifacts.apis.io/amazon-chime/packages/amazon-chime-packages.yml
  title: ''
  type: Packages
  url: packages/amazon-chime-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.amazon.com/terms-and-agreements
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
- group: docs
  title: ''
  type: APIReference
  url: https://docs.aws.amazon.com/cli/latest/reference/chime/index.html
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.aws.amazon.com/AmazonRDS/latest/gettingstartedguide/what-is-rds
- group: docs
  title: ''
  type: Documentation
  url: https://developer.amazon.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: auth
  href: https://artifacts.apis.io/amazon-chime/security/amazon-chime-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/amazon-chime-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/amazon-chime/security/amazon-chime-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-chime-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/amazon-chime/security/amazon-chime-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/amazon-chime-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aws.amazon.com/chime/
created: '2026-10-26'
description: Amazon Chime SDK enables developers to add real-time audio, video, and screen sharing capabilities to their web and mobile applications. It provides a set of flexible APIs and client SDKs that let you build custom communication experiences, such as meetings, webinars, and collaborative workspaces, without managing the underlying infrastructure. The service integrates with AWS security, monitoring, and scaling features, allowing seamless integration into existing cloud architectures.
layout: provider
modified: '2026-10-26'
name: Amazon Chime SDK
nav: Providers
network: true
overview: 'Amazon Chime SDK is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Communications, Video, Messaging, SDK, and RealTime.


  Amazon Chime SDK''s developer surface includes support, signup flow, sandbox, API reference, getting-started guide, documentation, and 17 more developer resources.'
random_paper: 9
score:
  band: thin
  composite: 28.5
  coverage:
    artifact_dirs: 8
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 47.6
    discoverability: 46.4
    operational_transparency: 15.8
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Amazon Chime Domain Security
  slug: amazon-chime-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Chime Vulnerability Disclosure
  slug: amazon-chime-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Chime Trust Center
  slug: amazon-chime-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-chime
tags:
- Communications
- Video
- Messaging
- SDK
- RealTime
website: https://aws.amazon.com/chime/
---
