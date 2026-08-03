---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 12.6
  scored_at: '2026-08-03'
api_count: 2
apis:
- description: d ACCOUNT Connect (dアカウント・コネクト) is DOCOMO's carrier identity service for businesses, offering OpenID Connect based social login backed by network line authentication and device biometrics against roug
  name: d ACCOUNT Connect
  slug: d-account-connect
- description: The docomo Mail IMAP interface is the one machine-interface specification NTT DOCOMO publishes openly, without registration, to third-party developers. It documents how a mail client connects to the d
  name: docomo Mail IMAP Interface
  slug: docomo-mail-imap-interface
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ntt-docomo-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ntt-docomo-authentication.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/ntt-docomo-well-known.yml
- group: other
  title: ''
  type: OpenIDConnectDiscovery
  url: well-known/ntt-docomo-openid-configuration.json
- group: design
  title: ''
  type: Conformance
  url: conformance/ntt-docomo-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ntt-docomo-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ntt-docomo-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://id.smt.docomo.ne.jp/src/dac/maintenance-g.html
- group: build
  title: ''
  type: Packages
  url: packages/ntt-docomo-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ntt-docomo-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.docomo.ne.jp/
- group: company
  title: ''
  type: Website
  url: https://www.docomo.ne.jp/english/
- group: docs
  title: ''
  type: Documentation
  url: https://www.docomo.ne.jp/service/developer/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.docomo.ne.jp/service/developer/policy/index.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.docomo.ne.jp/utility/privacy/
- group: operate
  title: ''
  type: Support
  url: https://www.nttdocomo.co.jp/support/inquiry/
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.docomo.ne.jp/support/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.docomo.ne.jp/charge/
- group: start
  title: ''
  type: SignUp
  url: https://id.smt.docomo.ne.jp/cgi8/id/register
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/docomo
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ntt-docomo
- group: company
  title: ''
  type: Blog
  url: https://www.docomo.ne.jp/english/info/media_center/pr/
- group: operate
  title: ''
  type: PressReleases
  url: https://www.docomo.ne.jp/info/news_release/
created: '2026-07-25'
description: 'NTT DOCOMO, Inc. is Japan''s largest mobile network operator and a wholly owned subsidiary of Nippon Telegraph and Telephone (NTT), serving roughly 90 million mobile subscriptions in its home market of Japan across the docomo, ahamo and irumo brands, alongside the d ACCOUNT identity, d POINT loyalty, d Payment wallet and Lemino media franchises. In the telecom value chain DOCOMO is a facilities-based incumbent carrier — it owns the 5G radio, core and subscriber identity — but it does not sell that capability to developers directly. Its API posture is partner-gated and sales-led: the first-party "docomo Developer support" programme launched in 2013 was shut down on 31 March 2021 and its host no longer resolves, no developer, developers, docs, api or opengateway subdomain exists on docomo.ne.jp, and the only surviving public developer page documents handset and content technical information rather than any HTTP API. DOCOMO''s network APIs reach developers only through aggregation:
  the company participates in the GSMA Open Gateway initiative and signed a distribution partnership with Aduna, the Ericsson-and-carrier joint venture, on 29 January 2026 to expose CAMARA Number Verification and SIM Swap for international markets — a commitment announced in press releases, with nothing callable published first-party as of this profile. Enterprise and wholesale API traffic is redirected to sibling company NTT DOCOMO BUSINESS on a separate domain.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-25'
name: NTT Docomo
nav: Providers
network: true
overview: 'NTT Docomo publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Telecommunications, Japan, Mobile Network Operator, Network APIs, and CAMARA.


  NTT Docomo''s developer surface includes authentication, documentation, support, pricing, signup flow, engineering blog, and 17 more developer resources.'
random_paper: 78
score:
  band: thin
  composite: 29.5
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 0.0
    developer_ergonomics: 26.1
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 21.1
  previous_composite: 29.5
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 43.1
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: authentication
  name: Ntt Docomo Authentication
  slug: ntt-docomo-authentication
  summary_line: openIdConnect · 1 scheme
- kind: domain-security
  name: Ntt Docomo Domain Security
  slug: ntt-docomo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ntt-docomo
tags:
- Telecommunications
- Japan
- Mobile Network Operator
- Network APIs
- CAMARA
- Open Gateway
- Aduna
- Carrier Identity
- SIM Swap
- Number Verification
- Carrier Billing
- 5G
- Partner Gated
website: https://www.docomo.ne.jp/
---
