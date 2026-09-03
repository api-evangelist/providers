---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.8
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: 'Hosted, zero-install MCP server (Streamable HTTP, protocol 2025-06-18) exposing the attestation service to MCP-capable agents. The eight tools were read live from tools/list on 2026-08-11: service_sta'
  name: imgauth Remote MCP Server
  slug: imgauth-remote-mcp-server
- baseURL: https://imgauth.spaziogenesi.org
  baseurl_source: declared
  description: The Agent API from imgauth — API di attestazione opere digitali — 4 operation(s) for agent.
  name: imgauth — API di attestazione opere digitali Agent API
  slug: imgauth-api-di-attestazione-opere-digitali-agent-api
- baseURL: https://imgauth.spaziogenesi.org
  baseurl_source: declared
  description: The Badge API from imgauth — API di attestazione opere digitali — 2 operation(s) for badge.
  name: imgauth — API di attestazione opere digitali Badge API
  slug: imgauth-api-di-attestazione-opere-digitali-badge-api
- baseURL: https://imgauth.spaziogenesi.org
  baseurl_source: declared
  description: The C API from imgauth — API di attestazione opere digitali — 1 operation(s) for c.
  name: imgauth — API di attestazione opere digitali C API
  slug: imgauth-api-di-attestazione-opere-digitali-c-api
- baseURL: https://imgauth.spaziogenesi.org
  baseurl_source: declared
  description: The Cert API from imgauth — API di attestazione opere digitali — 1 operation(s) for cert.
  name: imgauth — API di attestazione opere digitali Cert API
  slug: imgauth-api-di-attestazione-opere-digitali-cert-api
- baseURL: https://imgauth.spaziogenesi.org
  baseurl_source: declared
  description: The Cert Pdf API from imgauth — API di attestazione opere digitali — 1 operation(s) for cert pdf.
  name: imgauth — API di attestazione opere digitali Cert Pdf API
  slug: imgauth-api-di-attestazione-opere-digitali-cert-pdf-api
- baseURL: https://imgauth.spaziogenesi.org
  baseurl_source: declared
  description: The Hash API from imgauth — API di attestazione opere digitali — 1 operation(s) for hash.
  name: imgauth — API di attestazione opere digitali Hash API
  slug: imgauth-api-di-attestazione-opere-digitali-hash-api
- baseURL: https://imgauth.spaziogenesi.org
  baseurl_source: declared
  description: The Health Log API from imgauth — API di attestazione opere digitali — 1 operation(s) for health log.
  name: imgauth — API di attestazione opere digitali Health Log API
  slug: imgauth-api-di-attestazione-opere-digitali-health-log-api
- baseURL: https://imgauth.spaziogenesi.org
  baseurl_source: declared
  description: The Integrations API from imgauth — API di attestazione opere digitali — 1 operation(s) for integrations.
  name: imgauth — API di attestazione opere digitali Integrations API
  slug: imgauth-api-di-attestazione-opere-digitali-integrations-api
- baseURL: https://imgauth.spaziogenesi.org
  baseurl_source: declared
  description: The Integrazioni API from imgauth — API di attestazione opere digitali — 1 operation(s) for integrazioni.
  name: imgauth — API di attestazione opere digitali Integrazioni API
  slug: imgauth-api-di-attestazione-opere-digitali-integrazioni-api
- baseURL: https://imgauth.spaziogenesi.org
  baseurl_source: declared
  description: The Ots API from imgauth — API di attestazione opere digitali — 1 operation(s) for ots.
  name: imgauth — API di attestazione opere digitali Ots API
  slug: imgauth-api-di-attestazione-opere-digitali-ots-api
- baseURL: https://imgauth.spaziogenesi.org
  baseurl_source: declared
  description: The Ping API from imgauth — API di attestazione opere digitali — 1 operation(s) for ping.
  name: imgauth — API di attestazione opere digitali Ping API
  slug: imgauth-api-di-attestazione-opere-digitali-ping-api
- baseURL: https://imgauth.spaziogenesi.org
  baseurl_source: declared
  description: The Status API from imgauth — API di attestazione opere digitali — 1 operation(s) for status.
  name: imgauth — API di attestazione opere digitali Status API
  slug: imgauth-api-di-attestazione-opere-digitali-status-api
- baseURL: https://imgauth.spaziogenesi.org
  baseurl_source: declared
  description: The Status History API from imgauth — API di attestazione opere digitali — 1 operation(s) for status history.
  name: imgauth — API di attestazione opere digitali Status History API
  slug: imgauth-api-di-attestazione-opere-digitali-status-history-api
- baseURL: https://imgauth.spaziogenesi.org
  baseurl_source: declared
  description: The Verify API from imgauth — API di attestazione opere digitali — 1 operation(s) for verify.
  name: imgauth — API di attestazione opere digitali Verify API
  slug: imgauth-api-di-attestazione-opere-digitali-verify-api
artifact_total: 24
collections:
- collection_type: open
  name: imgauth — API di attestazione opere digitali
  slug: open-imgauth-api-di-attestazione-opere-digitali-openapi-original
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/SPAZIO-GENESI/imgauth/blob/main/LICENSE
- group: other
  title: ''
  type: Overlay
  url: overlays/imgauth-api-di-attestazione-opere-digitali-openapi-overlay.yaml
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
  name: imgauth — API di attestazione opere digitali MCP Server
  slug: imgauth-api-di-attestazione-opere-digitali-mcp-server
- description: ''
  name: imgauth — API di attestazione opere digitali MCP Server
  slug: imgauth-api-di-attestazione-opere-digitali-mcp-server-2
modified: '2026-08-11'
name: imgauth — API di attestazione opere digitali
nav: Providers
network: true
overview: 'imgauth — API di attestazione opere digitali publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Agent API, Badge API, C API, and 11 more. Tagged areas include digital notarization, Timestamping, proof-of-existence, content authenticity, and Provenance.


  imgauth — API di attestazione opere digitali''s developer surface includes authentication, documentation, API reference, getting-started guide, signup flow, pricing, support, and 30 more developer resources.'
plans:
- name: Imgauth Api Di Attestazione Opere Digitali Plans Pricing
  plan_count: 4
  slug: imgauth-api-di-attestazione-opere-digitali-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 3
  name: Imgauth Api Di Attestazione Opere Digitali Rate Limits
  slug: imgauth-api-di-attestazione-opere-digitali-rate-limits
score:
  band: strong
  composite: 64.2
  coverage:
    artifact_dirs: 21
    catalog_gap: 54.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 18.2
    contract_quality: 50.5
    developer_ergonomics: 70.8
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 76.3
  previous_composite: 64.2
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
    mcp: first-party
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/imgauth-api-di-attestazione-opere-digitali/refs/heads/main/screenshots/imgauth-api-di-attestazione-opere-digitali-2026-08-17T080953.png
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
- Timestamping
- proof-of-existence
- content authenticity
- Provenance
- Copyright
- IP protection
- Blockchain
- Bitcoin
- OpenTimestamps
- Security
- Document
- E-Signature
- MCP
website: https://attestazione.spaziogenesi.org/en/developer/
---
