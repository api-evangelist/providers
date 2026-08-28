---
agent_readiness:
  band: agent-ready
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
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.9
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Tvarka Atk Api Agentic Access
  operation_count: 22
  slug: tvarka-atk-api-agentic-access
  summary_line: 22 operations · 15 acting
api_count: 9
apis:
- description: The eID authentication ceremony (`/v1/auth/*`).
  name: Tvarka ATK API Auth API
  slug: tvarka-atk-api-auth-api
- description: The Erasure API from Tvarka ATK API — 3 operation(s) for erasure.
  name: Tvarka ATK API Erasure API
  slug: tvarka-atk-api-erasure-api
- description: Post-signature timestamp and long-term-validation upgrades.
  name: Tvarka ATK API LTV API
  slug: tvarka-atk-api-ltv-api
- description: NFC remote pairing - complete a request by tapping a card on a different device.
  name: Tvarka ATK API Pairing API
  slug: tvarka-atk-api-pairing-api
- description: The QES signing ceremony (`/v1/sign/*`).
  name: Tvarka ATK API Sign API
  slug: tvarka-atk-api-sign-api
- description: The Tvarka ATK API API from Tvarka ATK API — 0 operation(s) for tvarka atk api.
  name: Tvarka ATK API Tvarka ATK API API
  slug: tvarka-atk-api-tvarka-atk-api-api
- description: The Tvarka ATK QES Signing API (paid Tier Addendum) API from Tvarka ATK API — 0 operation(s) for tvarka atk qes signing api (paid tier addendum).
  name: Tvarka ATK API Tvarka ATK QES Signing API (paid Tier Addendum) API
  slug: tvarka-atk-api-tvarka-atk-qes-signing-api-paid-tier-addendum-api
- description: Standalone advisory validation of signed artifacts.
  name: Tvarka ATK API Validation API
  slug: tvarka-atk-api-validation-api
- description: Keys for verifying the optional `assertion` JWT.
  name: Tvarka ATK API Well Known API
  slug: tvarka-atk-api-well-known-api
arazzos:
- description: The full ATK authentication ceremony - create an audience-bound request on the backend, submit the card certificate, return the card signature, and read the verified identity.
  name: Authenticate a person with a Lithuanian eID card
  slug: tvarka-atk-api-authenticate-eid-card
- description: The ATK signing ceremony for a PAdES container - create the request, submit the card signing certificate, return the signature, check both result axes, then download the signed PDF.
  name: Sign a PDF with a qualified electronic signature
  slug: tvarka-atk-api-sign-pades-document
- description: The three stateless trust services in sequence - validate a container, add qualified timestamps to untimestamped XAdES, upgrade PAdES B-T to B-LT, then download the output.
  name: Validate, timestamp and archive an existing signed document
  slug: tvarka-atk-api-timestamp-and-archive
artifact_total: 30
asyncapis:
- description: ''
  name: Tvarka Atk Api Webhooks
  slug: tvarka-atk-api-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Tvarka Atk Auth API
  slug: open-tvarka-atk-api-auth-api
- collection_type: open
  name: Tvarka Atk Erasure API
  slug: open-tvarka-atk-api-erasure-api
- collection_type: open
  name: Tvarka Atk LTV API
  slug: open-tvarka-atk-api-ltv-api
- collection_type: open
  name: Tvarka Atk Pairing API
  slug: open-tvarka-atk-api-pairing-api
- collection_type: open
  name: Tvarka Atk Sign API
  slug: open-tvarka-atk-api-sign-api
- collection_type: open
  name: Tvarka ATK Tvarka ATK API API
  slug: open-tvarka-atk-api-tvarka-atk-api-api
- collection_type: open
  name: Tvarka ATK - QES Signing API (paid-tier addendum) Tvarka ATK QES Signing API (paid Tier Addendum) Tvarka ATK QES Signing API (paid Tier Addendum) API
  slug: open-tvarka-atk-api-tvarka-atk-qes-signing-api-paid-tier-addendum-api
- collection_type: open
  name: Tvarka Atk Validation API
  slug: open-tvarka-atk-api-validation-api
- collection_type: open
  name: Tvarka Atk Well Known API
  slug: open-tvarka-atk-api-well-known-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tvarka-atk-api-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tvarka-atk-api-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tvarka-atk-api-authentication.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://atk.tvarka.pro/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://atk.tvarka.pro/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://atk.tvarka.pro/docs/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://atk.tvarka.pro/docs/quickstart/
- group: operate
  title: ''
  type: Support
  url: https://tvarka.pro/kontaktai/
- group: start
  title: ''
  type: SignUp
  url: https://atk.tvarka.pro/docs/access/
- group: commercial
  title: ''
  type: Pricing
  url: https://atk.tvarka.pro/docs/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tvarka.pro/salygos/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tvarka.pro/privatumas/
- group: build
  title: ''
  type: Postman
  url: https://atk.tvarka.pro/postman/auth.json
- group: build
  title: ''
  type: Postman
  url: https://atk.tvarka.pro/postman/sign.json
- group: build
  title: ''
  type: Packages
  url: packages/tvarka-atk-api-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/tvarka-atk-api-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/tvarka-atk-api-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tvarka-atk-api-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/tvarka-atk-api-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/tvarka-atk-api-openapi-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/tvarka-atk-api-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://tvarka.pro/saugumas/
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/tvarka-atk-api-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tvarka-atk-api-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://atk.tvarka.pro/status/
- group: operate
  title: ''
  type: Deprecation
  url: https://atk.tvarka.pro/docs/lifecycle/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/tvarka-atk-api-changelog.yml
- group: auth
  title: ''
  type: Security
  url: https://tvarka.pro/saugumas/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/tvarka-atk-api-vulnerability-disclosure.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/tvarka-atk-api-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/tvarka-atk-api-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/tvarka-atk-api-conventions.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/tvarka-atk-api-webhooks.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/tvarka-atk-api-data-model.yml
- group: build
  title: ''
  type: Examples
  url: examples/tvarka-atk-api-examples.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tvarka-atk-api-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/tvarka-atk-api-plans.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/tvarka-atk-api-authenticate-eid-card.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/tvarka-atk-api-sign-pades-document.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/tvarka-atk-api-timestamp-and-archive.yml
created: '2026-08-02'
description: A single REST API for Lithuanian eID authentication and qualified electronic signing (QES), plus validation, timestamping and long-term-validation (LTV)/archive trust services. The primary ceremonies read the Lithuanian identity card (ATK) through a physical smart-card reader or an NFC phone tap, with Smart-ID and Mobile-ID as optional server-side methods under the same request, polling, webhook and metering model. Signing produces PAdES, ASiC-E, ADOC or detached CAdES artifacts with a qualified timestamp and an advisory validation axis. eIDAS-aligned and EU-resident, operated from Lithuania by Advokato M. Kiskio kontora INVENT and Socialiniai algoritmai, UAB, and priced per successful operation with no subscription or minimum.
image: https://tvarka.pro/static/img/tvarka-logo-closer.53b2d1b2a9b0.svg
layout: provider
mcp_servers:
- description: ''
  name: Tvarka ATK API MCP Server
  slug: tvarka-atk-api-mcp-server
modified: '2026-08-09'
name: Tvarka ATK API
nav: Providers
network: true
overview: 'Tvarka ATK API publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Auth API, Erasure API, LTV API, and 6 more. Tagged areas include Authentication, Digital Signature, eIDAS, QES, and Lithuania.


  The Tvarka ATK API catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Tvarka ATK API''s developer surface includes authentication, documentation, API reference, getting-started guide, support, signup flow, pricing, and 34 more developer resources.'
plans:
- name: Tvarka Atk Api Plans
  plan_count: 5
  slug: tvarka-atk-api-plans
random_paper: 8
rate_limits:
- limit_count: 0
  name: Tvarka Atk Api Rate Limits
  slug: tvarka-atk-api-rate-limits
score:
  band: exemplar
  composite: 66.6
  delta: 0.0
  facets:
    access_clarity: 84.2
    commercial_clarity: 84.2
    contract_governance: 30.3
    contract_quality: 61.4
    developer_ergonomics: 75.6
    discoverability: 81.5
    governance: 30.3
    operational_transparency: 57.9
  previous_composite: 66.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
    skills: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tvarka-atk-api/refs/heads/main/screenshots/tvarka-atk-api-2026-08-17T082503.png
security:
- kind: authentication
  name: Tvarka Atk Api Authentication
  slug: tvarka-atk-api-authentication
  summary_line: http/apiKey · 3 schemes
- kind: domain-security
  name: Tvarka Atk Api Domain Security
  slug: tvarka-atk-api-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Tvarka Atk Api Vulnerability Disclosure
  slug: tvarka-atk-api-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: tvarka-atk-api
tags:
- Authentication
- Digital Signature
- eIDAS
- QES
- Lithuania
- OpenAPI
- eID
- Smart-ID
- Mobile-ID
- NFC
- Timestamping
- LTV
- Webhook
- Identity
- Trust Services
- GDPR
website: https://atk.tvarka.pro/docs/
---
