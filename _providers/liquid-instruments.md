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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 14.9
  scored_at: '2026-08-26'
api_count: 2
apis:
- description: The Moku Scripting API is a RESTful HTTP interface served by the Moku device itself. A client first POSTs an empty JSON object to moku/claim_ownership to mint a Moku-Client-Key, then POSTs JSON parame
  name: Moku REST API
  slug: moku-rest-api
- description: The hosted identity service behind mokucli login, Moku Cloud Compile and licensed feature access. It publishes a full OpenID Connect discovery document at https://auth.liquidinstruments.com/.well-know
  name: Liquid Instruments Identity (OAuth 2.0 / OpenID Connect)
  slug: liquid-instruments-identity-oauth-20-openid-connect
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/liquid-instruments-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://liquidinstruments.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://apis.liquidinstruments.com/
- group: docs
  title: ''
  type: Documentation
  url: https://apis.liquidinstruments.com/
- group: docs
  title: ''
  type: APIReference
  url: https://apis.liquidinstruments.com/api/reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://apis.liquidinstruments.com/api/getting-started/
- group: operate
  title: ''
  type: Support
  url: https://liquidinstruments.com/support/contact/
- group: operate
  title: ''
  type: HelpCenter
  url: https://knowledge.liquidinstruments.com/
- group: operate
  title: ''
  type: Community
  url: https://forum.liquidinstruments.com/
- group: company
  title: ''
  type: Blog
  url: https://liquidinstruments.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://liquidinstruments.com/feed/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/liquidinstruments
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/liquidinstruments/moku-examples
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/liquidinstruments/moku-examples
- group: commercial
  title: ''
  type: Pricing
  url: https://store.liquidinstruments.com/
- group: start
  title: ''
  type: SignUp
  url: https://liquidinstruments.com/my-account/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://liquidinstruments.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://liquidinstruments.com/privacy
- group: other
  title: ''
  type: AcceptableUsePolicy
  url: https://liquidinstruments.com/terms/acceptable-use-policy
- group: operate
  title: ''
  type: ChangeLog
  url: https://apis.liquidinstruments.com/api/changelog/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/liquid-instruments-changelog.yml
- group: build
  title: ''
  type: Packages
  url: packages/liquid-instruments-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/liquid-instruments-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/liquid-instruments-cli.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/liquid-instruments-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/liquid-instruments-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/liquid-instruments-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/liquid-instruments-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/liquid-instruments-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/liquid-instruments-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/liquid-instruments-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/liquid-instruments-data-model.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/liquid-instruments-llms.txt
created: '2026-08-04'
description: Liquid Instruments builds Moku, a family of software-defined, FPGA-reconfigurable test-and-measurement hardware platforms (Moku:Go, Moku:Lab, Moku:Pro, Moku:Delta) that replace a bench of traditional instruments — oscilloscope, spectrum analyzer, waveform generator, lock-in amplifier, PID controller, phasemeter, laser lock box, logic analyzer, FIR/digital filter box, frequency response analyzer and more — with one reconfigurable device. Every Moku exposes a RESTful HTTP control API served by the device itself on the local network, wrapped by first-party Python, MATLAB and LabVIEW client libraries plus the MokuCLI command-line utility, and the company runs a hosted OpenID Connect identity service for Moku Cloud Compile and licensed feature access. The company was founded out of gravitational-wave detection research and is headquartered in San Diego, California with offices in Canberra and Melbourne, Australia.
image: https://liquidinstruments.com/wp-content/uploads/2022/01/liquid-instruments-logo.svg
layout: provider
modified: '2026-08-04'
name: Liquid Instruments
nav: Providers
network: true
overview: 'Liquid Instruments publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Test and Measurement, Instrumentation, Hardware, and Oscilloscope.


  Liquid Instruments'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, code examples, pricing, and 26 more developer resources.'
random_paper: 10
scopes:
- name: Liquid Instruments Scopes
  scope_count: 5
  slug: liquid-instruments-scopes
  summary_line: 5 scopes · authorizationCode/clientCredentials/deviceCode/implicit/password
score:
  band: thin
  composite: 35.8
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 4.5
    contract_quality: 6.7
    developer_ergonomics: 71.4
    discoverability: 79.6
    governance: 4.5
    operational_transparency: 18.4
  previous_composite: 35.8
  provenance:
    conformance: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/liquid-instruments/refs/heads/main/screenshots/liquid-instruments-2026-08-07T171731.png
security:
- kind: authentication
  name: Liquid Instruments Authentication
  slug: liquid-instruments-authentication
  summary_line: apiKey/oauth2/openIdConnect · 3 schemes
- kind: domain-security
  name: Liquid Instruments Domain Security
  slug: liquid-instruments-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: liquid-instruments
tags:
- Company
- Test and Measurement
- Instrumentation
- Hardware
- Oscilloscope
- Spectrum Analyzer
- Data Acquisition
- FPGA
- Photonics
- Scientific Instruments
- Electronics
- Laboratory
website: https://liquidinstruments.com/
---
