---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-native
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
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 48.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 31
  human_in_the_loop: 15
  name: Tvarka Agentic Access
  operation_count: 44
  slug: tvarka-agentic-access
  summary_line: 44 operations · 31 acting · 15 human-in-the-loop
api_count: 4
apis:
- description: The Tvarka ATK API API from Tvarka ATK API — 0 operation(s) for tvarka atk api.
  name: Tvarka ATK API Tvarka ATK API
  slug: tvarka-atk-api-tvarka-atk-api-api
- description: The Tvarka ATK QES Signing API (paid Tier Addendum) API from Tvarka ATK API — 0 operation(s) for tvarka atk qes signing api (paid tier addendum).
  name: Tvarka ATK API Tvarka ATK QES Signing API (paid Tier Addendum) API
  slug: tvarka-atk-api-tvarka-atk-qes-signing-api-paid-tier-addendum-api
- baseURL: https://sign-api.tvarka.pro
  baseurl_source: declared
  description: 'Machine channel for Tvarka Sign: post a document and a list of signers and Tvarka runs its ordinary qualified signing ceremony for each of them on the hosted page or in the Tvarka Sign mobile app (LT '
  name: Tvarka Sign API
  slug: tvarka-sign-api
- baseURL: https://atk.tvarka.pro/v1
  baseurl_source: declared
  description: The eID authentication ceremony (`/v1/auth/*`).
  name: Tvarka ATK API Auth API
  slug: tvarka-auth-api
- baseURL: https://atk.tvarka.pro/v1
  baseurl_source: declared
  description: The Batches API from Tvarka ATK API — 2 operation(s) for batches.
  name: Tvarka ATK API Batches API
  slug: tvarka-batches-api
- baseURL: https://atk.tvarka.pro/v1
  baseurl_source: declared
  description: The Erasure API from Tvarka ATK API — 3 operation(s) for erasure.
  name: Tvarka ATK API Erasure API
  slug: tvarka-erasure-api
- baseURL: https://atk.tvarka.pro/v1
  baseurl_source: declared
  description: The Files API from Tvarka ATK API — 2 operation(s) for files.
  name: Tvarka ATK API Files API
  slug: tvarka-files-api
- baseURL: https://atk.tvarka.pro/v1
  baseurl_source: declared
  description: Post-signature timestamp and long-term-validation upgrades.
  name: Tvarka ATK API LTV API
  slug: tvarka-ltv-api
- baseURL: https://atk.tvarka.pro/v1
  baseurl_source: declared
  description: NFC remote pairing - complete a request by tapping a card on a different device.
  name: Tvarka ATK API Pairing API
  slug: tvarka-pairing-api
- baseURL: https://atk.tvarka.pro/v1
  baseurl_source: declared
  description: Create and follow a signing.
  name: Tvarka ATK API Signings API
  slug: tvarka-signings-api
- baseURL: https://atk.tvarka.pro/v1
  baseurl_source: declared
  description: The Tvarka ATK API API from Tvarka ATK API — 0 operation(s) for tvarka atk api.
  name: Tvarka ATK API Tvarka ATK API
  slug: tvarka-tvarka-atk-api-api
- baseURL: https://atk.tvarka.pro/v1
  baseurl_source: declared
  description: The Tvarka Sign API API from Tvarka ATK API — 0 operation(s) for tvarka sign api.
  name: Tvarka ATK API Tvarka Sign API
  slug: tvarka-tvarka-sign-api-api
- baseURL: https://atk.tvarka.pro/v1
  baseurl_source: declared
  description: Standalone advisory validation of signed artifacts.
  name: Tvarka ATK API Validation API
  slug: tvarka-validation-api
- baseURL: https://atk.tvarka.pro/v1
  baseurl_source: declared
  description: Keys for verifying the optional `assertion` JWT.
  name: Tvarka ATK API Well Known API
  slug: tvarka-well-known-api
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
artifact_total: 45
asyncapis:
- description: ''
  name: Tvarka Atk Api Webhooks
  slug: tvarka-atk-api-webhooks
- description: ''
  name: Tvarka Sign Api Webhooks
  slug: tvarka-sign-api-webhooks
collections:
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
- group: other
  href: https://artifacts.apis.io/tvarka/capabilities/tvarka-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/tvarka-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://www.tvarka.pro/
- group: agent
  href: https://artifacts.apis.io/tvarka/agentic-access/tvarka-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/tvarka-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/tvarka/security/tvarka-atk-api-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tvarka-atk-api-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/tvarka/authentication/tvarka-atk-api-authentication.yml
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
  href: https://artifacts.apis.io/tvarka/packages/tvarka-atk-api-packages.yml
  title: ''
  type: Packages
  url: packages/tvarka-atk-api-packages.yml
- group: build
  href: https://artifacts.apis.io/tvarka/packages/tvarka-atk-api-packages.yml
  title: ''
  type: SDKs
  url: packages/tvarka-atk-api-packages.yml
- group: agent
  href: https://artifacts.apis.io/tvarka/well-known/tvarka-atk-api-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/tvarka-atk-api-well-known.yml
- group: agent
  href: https://artifacts.apis.io/tvarka/llms/tvarka-atk-api-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/tvarka-atk-api-llms.txt
- group: agent
  href: https://artifacts.apis.io/tvarka/mcp/tvarka-sign-api-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/tvarka-sign-api-mcp.yml
- group: other
  href: https://artifacts.apis.io/tvarka/overlays/tvarka-atk-api-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/tvarka-atk-api-openapi-overlay.yaml
- group: design
  href: https://artifacts.apis.io/tvarka/conformance/tvarka-atk-api-conformance.yml
  title: ''
  type: Conformance
  url: conformance/tvarka-atk-api-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://tvarka.pro/saugumas/
- group: design
  href: https://artifacts.apis.io/tvarka/errors/tvarka-atk-api-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/tvarka-atk-api-problem-types.yml
- group: design
  href: https://artifacts.apis.io/tvarka/lifecycle/tvarka-atk-api-lifecycle.yml
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
  href: https://artifacts.apis.io/tvarka/changelog/tvarka-atk-api-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/tvarka-atk-api-changelog.yml
- group: auth
  title: ''
  type: Security
  url: https://tvarka.pro/saugumas/
- group: auth
  href: https://artifacts.apis.io/tvarka/security/tvarka-atk-api-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/tvarka-atk-api-vulnerability-disclosure.yml
- group: start
  href: https://artifacts.apis.io/tvarka/sandbox/tvarka-atk-api-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/tvarka-atk-api-sandbox.yml
- group: design
  href: https://artifacts.apis.io/tvarka/conventions/tvarka-atk-api-conventions.yml
  title: ''
  type: Conventions
  url: conventions/tvarka-atk-api-conventions.yml
- group: design
  href: https://artifacts.apis.io/tvarka/conventions/tvarka-atk-api-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/tvarka-atk-api-conventions.yml
- group: design
  href: https://artifacts.apis.io/tvarka/asyncapi/tvarka-atk-api-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/tvarka-atk-api-webhooks.yml
- group: design
  href: https://artifacts.apis.io/tvarka/data-model/tvarka-atk-api-data-model.yml
  title: ''
  type: DataModel
  url: data-model/tvarka-atk-api-data-model.yml
- group: build
  href: https://artifacts.apis.io/tvarka/examples/tvarka-atk-api-examples.yml
  title: ''
  type: Examples
  url: examples/tvarka-atk-api-examples.yml
- group: operate
  href: https://artifacts.apis.io/tvarka/rate-limits/tvarka-atk-api-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/tvarka-atk-api-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/tvarka/plans/tvarka-atk-api-plans.yml
  title: ''
  type: Plans
  url: plans/tvarka-atk-api-plans.yml
- group: agent
  href: https://artifacts.apis.io/tvarka/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/tvarka/arazzo/tvarka-atk-api-authenticate-eid-card.yml
  title: ''
  type: Arazzo
  url: arazzo/tvarka-atk-api-authenticate-eid-card.yml
- group: design
  href: https://artifacts.apis.io/tvarka/arazzo/tvarka-atk-api-sign-pades-document.yml
  title: ''
  type: Arazzo
  url: arazzo/tvarka-atk-api-sign-pades-document.yml
- group: design
  href: https://artifacts.apis.io/tvarka/arazzo/tvarka-atk-api-timestamp-and-archive.yml
  title: ''
  type: Arazzo
  url: arazzo/tvarka-atk-api-timestamp-and-archive.yml
- group: build
  href: https://artifacts.apis.io/tvarka/mcp/tvarka-sign-api-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/tvarka-sign-api-tool-crosswalk.yml
- group: auth
  href: https://artifacts.apis.io/tvarka/well-known/tvarka-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/tvarka-security.txt
- group: other
  title: ''
  type: APIsJSON
  url: https://atk.tvarka.pro/apis.json
- group: agent
  href: https://artifacts.apis.io/tvarka/llms/tvarka-sign-api-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/tvarka-sign-api-llms.txt
- group: design
  href: https://artifacts.apis.io/tvarka/asyncapi/tvarka-sign-api-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/tvarka-sign-api-webhooks.yml
- group: design
  href: https://artifacts.apis.io/tvarka/errors/tvarka-sign-api-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/tvarka-sign-api-problem-types.yml
- group: start
  href: https://artifacts.apis.io/tvarka/sandbox/tvarka-sign-api-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/tvarka-sign-api-sandbox.yml
- group: design
  href: https://artifacts.apis.io/tvarka/conventions/tvarka-sign-api-conventions.yml
  title: ''
  type: Conventions
  url: conventions/tvarka-sign-api-conventions.yml
- group: auth
  href: https://artifacts.apis.io/tvarka/authentication/tvarka-sign-api-authentication.yml
  title: ''
  type: Authentication
  url: authentication/tvarka-sign-api-authentication.yml
- group: operate
  title: ''
  type: HelpCenter
  url: https://tvarka.pro/pagalba/
- group: other
  href: https://artifacts.apis.io/tvarka/overlays/tvarka-sign-api-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/tvarka-sign-api-openapi-overlay.yaml
- group: design
  href: https://artifacts.apis.io/tvarka/data-model/tvarka-sign-api-data-model.yml
  title: ''
  type: DataModel
  url: data-model/tvarka-sign-api-data-model.yml
- group: operate
  href: https://artifacts.apis.io/tvarka/rate-limits/tvarka-sign-api-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/tvarka-sign-api-rate-limits.yml
created: '2026-08-02'
description: A single REST API estate for Lithuanian eID authentication and qualified electronic signing (QES). The ATK API reads the Lithuanian identity card itself - physical smart-card reader or NFC phone tap - through one request, polling, webhook and metering model, and adds standalone validation, timestamping and long-term-validation (LTV)/archive trust services; contract 1.4.0 withdrew the short-lived Smart-ID and Mobile-ID passthrough, so the ATK surface is deliberately card-only. Hosted remote-method ceremonies moved to the separate Tvarka Sign API (sign-api.tvarka.pro), an orchestration contract with RFC 9457 problem details and a live, anonymously introspectable MCP server at /mcp. eIDAS-aligned and EU-resident, operated from Lithuania by Advokato M. Kiskio kontora INVENT and Socialiniai algoritmai, UAB, and priced per successful operation with no subscription or minimum.
finops:
- has_sources: true
  method: derived
  name: Tvarka Finops
  primary_unit: successful operation, excluding vat
  service_category: ''
  slug: tvarka-finops
  template: false
image: https://tvarka.pro/static/img/tvarka-logo-closer.53b2d1b2a9b0.svg
layout: provider
mcp_servers:
- description: Remote MCP server at sign-api.tvarka.pro over HTTP requiring an API key; 6 tools listed.
  name: Tvarka Sign
  slug: tvarka-sign
modified: '2026-09-16'
name: Tvarka ATK API
nav: Providers
network: true
overview: 'Tvarka ATK API publishes 14 API contracts indexed on the [APIs.io](https://apis.io/) network, including Tvarka ATK API, Tvarka ATK QES Signing API (paid Tier Addendum) API, Tvarka Sign API, and 11 more. Tagged areas include Authentication, Digital Signature, eIDAS, QES, and Lithuania.


  The Tvarka ATK API catalog on APIs.io includes 2 event-driven AsyncAPI specifications and 1 Spectral governance ruleset.


  Tvarka ATK API''s developer surface includes authentication, documentation, API reference, getting-started guide, support, signup flow, pricing, and 49 more developer resources.'
plans:
- name: Tvarka Atk Api Plans
  plan_count: 3
  slug: tvarka-atk-api-plans
random_paper: 1
rate_limits:
- limit_count: 0
  name: Tvarka Atk Api Rate Limits
  slug: tvarka-atk-api-rate-limits
- limit_count: 1
  name: Tvarka Sign Api Rate Limits
  slug: tvarka-sign-api-rate-limits
rules:
- authorship: generated
  effective_rule_count: 103
  extends:
  - spectral:oas
  name: Tvarka ATK API API Rules
  rule_count: 62
  severity_counts:
    error: 56
    hint: 0
    info: 1
    warn: 5
  slug: tvarka-rules
score:
  band: exemplar
  composite: 74.1
  coverage:
    artifact_dirs: 30
    catalog_earned: 59.5
    catalog_earned_first_party: 12.0
    catalog_gap: 55.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 92.1
    contract_governance: 31.8
    contract_quality: 61.7
    developer_ergonomics: 75.6
    discoverability: 86.7
    operational_transparency: 57.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - lithuania
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 74.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 27.8
screenshot: https://apis.io/screenshots/tvarka/tvarka-atk-api-2026-08-17T082503.png
security:
- kind: authentication
  name: Tvarka Atk Api Authentication
  slug: tvarka-atk-api-authentication
  summary_line: http/apiKey · 3 schemes
- kind: authentication
  name: Tvarka Sign Api Authentication
  slug: tvarka-sign-api-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Tvarka Atk Api Domain Security
  slug: tvarka-atk-api-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Tvarka Atk Api Vulnerability Disclosure
  slug: tvarka-atk-api-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
skill_count: 6
skills:
- name: Authenticate a person with a Lithuanian eID card
  slug: tvarka-atk-api-authenticate-with-eid
- name: Erase request data on demand (GDPR)
  slug: tvarka-atk-api-erase-request-data
- name: Hand a card ceremony off to a phone over NFC
  slug: tvarka-atk-api-nfc-pairing-handoff
- name: Sign a document with a qualified electronic signature
  slug: tvarka-atk-api-sign-document-qes
- name: Validate, timestamp and archive a signed document
  slug: tvarka-atk-api-validate-timestamp-archive
- name: Collect qualified signatures from several people on one document
  slug: tvarka-sign-api-request-signatures
slug: tvarka
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
website: https://www.tvarka.pro/
---
