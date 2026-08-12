---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 45.9
  scored_at: '2026-08-11'
api_count: 2
apis:
- description: Attestation/proof-of-existence REST API. Client-side SHA-256 hashing, signed PDF certificates, RFC 3161 timestamps, OpenTimestamps/Bitcoin anchoring, verifiable certificate pages, and status telemetry
  name: imgauth REST API
  slug: imgauth-rest-api
- description: 'Hosted, zero-install MCP server (Streamable HTTP, protocol 2025-06-18) exposing the attestation service to MCP-capable agents. The eight tools were read live from tools/list on 2026-08-11: service_sta'
  name: imgauth Remote MCP Server
  slug: imgauth-remote-mcp-server
artifact_total: 10
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/imgauth-api-di-attestazione-opere-digitali-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/imgauth-api-di-attestazione-opere-digitali-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/imgauth-api-di-attestazione-opere-digitali-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/imgauth-api-di-attestazione-opere-digitali-authentication.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://attestazione.spaziogenesi.org/en/developer/
- group: docs
  title: ''
  type: Documentation
  url: https://attestazione.spaziogenesi.org/en/developer/
- group: docs
  title: ''
  type: APIReference
  url: https://attestazione.spaziogenesi.org/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://attestazione.spaziogenesi.org/en/developer/keys/
- group: start
  title: ''
  type: SignUp
  url: https://attestazione.spaziogenesi.org/en/developer/keys/
- group: commercial
  title: ''
  type: Pricing
  url: https://attestazione.spaziogenesi.org/professionale/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://attestazione.spaziogenesi.org/en/condizioni/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://attestazione.spaziogenesi.org/en/privacy.html
- group: operate
  title: ''
  type: Support
  url: mailto:it@spaziogenesi.org
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SPAZIO-GENESI
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/SPAZIO-GENESI/imgauth
- group: agent
  title: ''
  type: WellKnown
  url: well-known/imgauth-api-di-attestazione-opere-digitali-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/imgauth-api-di-attestazione-opere-digitali-security.txt
- group: auth
  title: ''
  type: Security
  url: https://attestazione.spaziogenesi.org/sicurezza/
- group: auth
  title: ''
  type: Compliance
  url: https://trust.spaziogenesi.org/
- group: build
  title: ''
  type: Packages
  url: packages/imgauth-api-di-attestazione-opere-digitali-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/imgauth-api-di-attestazione-opere-digitali-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/imgauth-api-di-attestazione-opere-digitali-cli.yml
- group: design
  title: ''
  type: Components
  url: components/imgauth-api-di-attestazione-opere-digitali-components.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/imgauth-api-di-attestazione-opere-digitali-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/imgauth-api-di-attestazione-opere-digitali-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/imgauth-api-di-attestazione-opere-digitali-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/imgauth-api-di-attestazione-opere-digitali-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://attestazione.spaziogenesi.org/status/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/imgauth-api-di-attestazione-opere-digitali-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://attestazione.spaziogenesi.org/changelog/
- group: design
  title: ''
  type: Conventions
  url: conventions/imgauth-api-di-attestazione-opere-digitali-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/imgauth-api-di-attestazione-opere-digitali-data-model.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/imgauth-api-di-attestazione-opere-digitali-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/imgauth-api-di-attestazione-opere-digitali-rate-limits.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-19'
description: Digital-work attestation and proof-of-existence service operated by Spazio Genesi ETS, an Italian non-profit (third-sector entity). The client computes a SHA-256 fingerprint locally and sends only the 64-hex hash — file bytes never leave the device. The service binds that fingerprint to a signed server-side timestamp (HMAC), issues a PAdES B-LT signed PDF certificate carrying an RFC 3161 timestamp from an Adobe AATL-recognised TSA, and anchors the fingerprint in Bitcoin through OpenTimestamps across four independent calendars. Verification is free and unlimited for anyone, and the proof of existence never expires. Exposes an 18-operation public REST API (OpenAPI 3.0.3, served at the API host root), a hosted zero-install remote MCP server whose eight tools answer tools/list anonymously, an sg-attest CLI, a GitHub Action, embeddable SVG badges and three CORS-open public status endpoints. The API contract is in Italian by design. Positioned explicitly as a NON-QUALIFIED attestation
  under eIDAS 2.0.
image: https://attestazione.spaziogenesi.org/og.png
layout: provider
mcp_servers:
- description: ''
  name: mcp
  slug: mcp
- description: ''
  name: imgauth-api-di-attestazione-opere-digitali-mcp.yml
  slug: imgauth-api-di-attestazione-opere-digitali-mcpyml
modified: '2026-08-11'
name: imgauth — API di attestazione opere digitali
nav: Providers
network: true
overview: 'imgauth — API di attestazione opere digitali publishes 1 API on the [APIs.io](https://apis.io/) network: imgauth REST API. Tagged areas include digital notarization, timestamping, proof-of-existence, content authenticity, and provenance.


  imgauth — API di attestazione opere digitali''s developer surface includes authentication, documentation, API reference, getting-started guide, signup flow, pricing, support, and 28 more developer resources.'
plans:
- name: Imgauth Api Di Attestazione Opere Digitali Plans Pricing
  plan_count: 4
  slug: imgauth-api-di-attestazione-opere-digitali-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 3
  name: Imgauth Api Di Attestazione Opere Digitali Rate Limits
  slug: imgauth-api-di-attestazione-opere-digitali-rate-limits
score:
  band: strong
  composite: 65.7
  delta: 51.7
  facets:
    commercial_clarity: 92.1
    contract_quality: 52.0
    developer_ergonomics: 69.6
    discoverability: 75.9
    governance: 20.8
    operational_transparency: 78.9
  previous_composite: 14.0
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: rising
security:
- kind: authentication
  name: Imgauth Api Di Attestazione Opere Digitali Authentication
  slug: imgauth-api-di-attestazione-opere-digitali-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Imgauth Api Di Attestazione Opere Digitali Domain Security
  slug: imgauth-api-di-attestazione-opere-digitali-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Imgauth Api Di Attestazione Opere Digitali Vulnerability Disclosure
  slug: imgauth-api-di-attestazione-opere-digitali-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Imgauth Api Di Attestazione Opere Digitali Trust Center
  slug: imgauth-api-di-attestazione-opere-digitali-trust-center
  summary_line: trust center published
slug: imgauth-api-di-attestazione-opere-digitali
tags:
- digital notarization
- timestamping
- proof-of-existence
- content authenticity
- provenance
- copyright
- IP protection
- blockchain
- Bitcoin
- OpenTimestamps
- security
- document
- e-signature
- MCP
website: https://attestazione.spaziogenesi.org/en/developer/
---
