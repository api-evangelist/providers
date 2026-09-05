---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.4
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: America Movil Agentic Access
  operation_count: 4
  slug: america-movil-agentic-access
  summary_line: 4 operations · 3 acting
api_count: 3
apis:
- description: CAMARA-aligned Number Verification API from Claro Brasil — silent verification that a mobile number is the one actually attached to the device making the request, offered as an alternative to SMS one-
  name: Claro Number Verification API
  slug: claro-number-verification-api
- description: KYC Match-style API from Claro Brasil that validates user-supplied identity attributes — phone number, name, address, e-mail — against Claro's subscriber records for onboarding and fraud prevention. L
  name: Claro Know Your Customer API
  slug: claro-know-your-customer-api
- description: Returns verified customer registration data held by Claro Brasil so that onboarding forms can be pre-populated from carrier records rather than self-declared input. Listed in the Claro Insight catalog
  name: Claro KYC Fill In API
  slug: claro-kyc-fill-in-api
- description: Detects whether a Brazilian mobile number has changed owner — the recycling of a disconnected number to a new subscriber — so that accounts keyed to a phone number are not silently transferred. Listed
  name: Claro Number Recycling API
  slug: claro-number-recycling-api
- description: 'Reports how long a mobile number has been active on the Claro Brasil network and the plan associated with it, used as a stability and risk signal in identity and credit decisions. Listed in the Claro '
  name: Claro Tenure API
  slug: claro-tenure-api
- description: Monitors M2M/IoT devices on the Claro Brasil network against geographic fences and raises cellular-network notifications when a device enters or leaves an area. Listed in the Claro Insight catalog; do
  name: Claro Geofencing API
  slug: claro-geofencing-api
- description: Biometric face-match validation against Claro Brasil's own image records, sold as an identity-assurance step alongside the network APIs. Listed in the Claro Insight catalog; documentation requires por
  name: Claro Face Match API
  slug: claro-face-match-api
- description: Detects SIM-card or handset changes on a Claro Brasil mobile line and raises an alert, a Claro-branded companion to the CAMARA SIM Swap API. Listed in the Claro Insight catalog; documentation requires
  name: Claro Alerta API
  slug: claro-alerta-api
- description: Validates the relationship between a Brazilian CPF (taxpayer identifier) and a mobile number using Claro Brasil subscriber records. Listed in the Claro Insight catalog; documentation requires portal r
  name: Claro Valida Telefone API
  slug: claro-valida-telefone-api
- description: Scores a declared address against antenna-proximity analysis of the Claro Brasil network, used to corroborate residential address claims during onboarding. Listed in the Claro Insight catalog; documen
  name: Claro Valida Endereço 2.0 API
  slug: claro-valida-endereco-api
- description: Credit-risk scoring derived from Claro Brasil telecom behaviour, used to identify lower-risk consumers. Listed in the Claro Insight catalog; documentation requires portal registration.
  name: Claro Score API
  slug: claro-score-api
- description: América Móvil's GSMA Open Gateway surface in its home market of Mexico, marketed by Telcel to enterprises as "Autenticación Móvil" — Number Verification (silent authentication of the mobile number), S
  name: Telcel Mobile Authentication APIs
  slug: telcel-mobile-authentication-apis
- baseURL: https://api.claro.com.br/mobile/v1/gsma/gateway/simswap
  baseurl_source: declared
  description: The Check SIM swap API from América Móvil — 1 operation(s) for check sim swap.
  name: América Móvil Check SIM swap API
  slug: america-movil-check-sim-swap-api
- baseURL: https://api.claro.com.br/mobile/v1/gsma/gateway/simswap
  baseurl_source: declared
  description: The Device Locations API from América Móvil — 1 operation(s) for device locations.
  name: América Móvil Device Locations API
  slug: america-movil-device-locations-api
- baseURL: https://api.claro.com.br/mobile/v1/gsma/gateway/simswap
  baseurl_source: declared
  description: The Location verification API from América Móvil — 1 operation(s) for location verification.
  name: América Móvil Location verification API
  slug: america-movil-location-verification-api
- baseURL: https://api.claro.com.br/mobile/v1/gsma/gateway/simswap
  baseurl_source: declared
  description: The Retrieve SIM swap date API from América Móvil — 1 operation(s) for retrieve sim swap date.
  name: América Móvil Retrieve SIM swap date API
  slug: america-movil-retrieve-sim-swap-date-api
arazzos:
- description: 'Before trusting a phone number as an authentication factor, ask Claro Brasil two questions: has the SIM pairing changed recently, and where is the device on the network? Step one is the decision gate '
  name: Account-takeover check for a Brazilian mobile line
  slug: america-movil-account-takeover-check
artifact_total: 26
asyncapis:
- description: ''
  name: America Movil Webhooks
  slug: america-movil-webhooks
collections:
- collection_type: open
  name: "Mobile - LBS Devices Locations\n (Proxy Apigee: mobile-lbsdeviceslocations-v1)"
  slug: open-america-movil-claro-device-location
- collection_type: open
  name: SIM Swap
  slug: open-america-movil-claro-sim-swap
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/america-movil-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/america-movil-claro-sim-swap-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/america-movil-sim-swap-fraud-check.md
- group: other
  title: ''
  type: Overlay
  url: overlays/america-movil-claro-device-location-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/america-movil-device-location-lookup.md
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/america-movil-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/america-movil-domain-security.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/america-movil-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/america-movil-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.americamovil.com/
- group: company
  title: ''
  type: Website
  url: https://www.telcel.com/
- group: company
  title: ''
  type: Website
  url: https://www.claro.com.br/
- group: docs
  title: ''
  type: Documentation
  url: https://www.claroinsight.com.br/pt-br/catalogo-api
- group: start
  title: ''
  type: SignUp
  url: https://www.claroinsight.com.br/user/register
- group: start
  title: ''
  type: Login
  url: https://www.claroinsight.com.br/pt-br/user/login
- group: start
  title: ''
  type: Onboarding
  url: https://www.claroinsight.com.br/onboarding
- group: operate
  title: ''
  type: FAQ
  url: https://www.claroinsight.com.br/pt-br/perguntas-frequentes
- group: operate
  title: ''
  type: Contact
  url: https://www.claroinsight.com.br/pt-br/contato
- group: commercial
  title: ''
  type: Privacy
  url: https://www.claro.com.br/privacidade
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/america-movil
- group: other
  title: ''
  type: Standards
  url: https://camaraproject.org/
- group: other
  title: ''
  type: Standards
  url: https://www.gsma.com/solutions-and-impact/gsma-open-gateway/
- group: company
  title: ''
  type: Blog
  url: https://www.claro.com.br/blog
- group: build
  title: ''
  type: Packages
  url: packages/america-movil-packages.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/america-movil-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/america-movil-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/america-movil-claro-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/america-movil-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/america-movil-error-codes.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/america-movil-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/america-movil-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/america-movil-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/america-movil-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/america-movil-sandbox.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/america-movil-plans.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/america-movil-rate-limits.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/america-movil-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/america-movil-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/america-movil-account-takeover-check.yml
- group: build
  title: ''
  type: Examples
  url: examples/america-movil-examples.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.claroinsight.com.br/
- group: docs
  title: ''
  type: APIReference
  url: https://www.claroinsight.com.br/pt-br/catalogo-api
- group: operate
  title: ''
  type: Support
  url: https://www.claroinsight.com.br/pt-br/contato
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.claro.com.br/privacidade
created: '2026-07-25'
description: 'América Móvil, S.A.B. de C.V. is the largest telecommunications group in Latin America, headquartered in Mexico City and controlled by the Slim family. It serves roughly 331 million wireless subscribers and 79 million fixed revenue-generating units across 23 countries (2025 Form 20-F), operating as Telcel and Telmex in its home market of Mexico, as Claro across most of Latin America and the Caribbean, and as the majority owner of A1 Telekom Austria Group in Central and Eastern Europe. In the value chain it is a mobile network operator and fixed-line carrier — it owns the spectrum, the radio access network, the SIM estate and the subscriber identity records that network APIs monetize, and it does not resell anyone else''s connectivity. Its API posture is the classic carrier posture: there is no corporate developer portal at americamovil.com (the domain is an investor-relations site and returns 403 to non-browser clients; developer.*, developers.*, docs.*, api.* and opengateway.*
  subdomains do not resolve), and the only real API surface in the group sits inside one operating company — Claro Brasil''s "Claro Insight" marketplace at claroinsight.com.br, a registration-gated catalog of 14 network and identity APIs including CAMARA-aligned SIM Swap, Number Verification and Device Location. In Mexico, Telcel launched GSMA Open Gateway on 28 May 2025 alongside Altán Redes, AT&T Mexico and Telefónica Mexico with three APIs — SIM Swap, Number Verification and Device Location — but publishes no portal, no specification and no sandbox, only a business sales contact form. América Móvil is a GSMA Open Gateway participant and was named in Ericsson''s September 2024 launch of the Aduna network-API joint venture, but it is absent from the final twelve-CSP equity structure completed in July 2025; in Brazil its CAMARA APIs reach developers through the CPaaS aggregator Infobip. Outside the Brazilian marketplace, América Móvil is partner-gated and sales-led, and is reachable by most
  developers only through an aggregator rather than directly.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-25'
name: América Móvil
nav: Providers
network: true
overview: 'América Móvil publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Check SIM swap API, Device Locations API, Location verification API, and 1 more. Tagged areas include Telecommunications, Mexico, Latin America, Mobile Network Operator, and Network APIs.


  The América Móvil catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  América Móvil''s developer surface includes authentication, documentation, signup flow, FAQ, privacy policy, engineering blog, changelog, and 38 more developer resources.'
plans:
- name: America Movil Plans
  plan_count: 2
  slug: america-movil-plans
random_paper: 16
rate_limits:
- limit_count: 4
  name: America Movil Rate Limits
  slug: america-movil-rate-limits
scopes:
- name: America Movil Scopes
  scope_count: 2
  slug: america-movil-scopes
  summary_line: 2 scopes · clientCredentials
score:
  band: strong
  composite: 58.2
  coverage:
    artifact_dirs: 27
    catalog_earned: 55.0
    catalog_earned_first_party: 20.0
    catalog_gap: 60.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.2
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 18.2
    contract_quality: 61.6
    developer_ergonomics: 54.2
    discoverability: 72.2
    governance: 18.2
    operational_transparency: 55.3
  previous_composite: 58.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 72.2
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/america-movil/refs/heads/main/screenshots/america-movil-2026-08-07T161348.png
security:
- kind: authentication
  name: America Movil Authentication
  slug: america-movil-authentication
  summary_line: apiKey/http/oauth2 · 4 schemes
- kind: domain-security
  name: America Movil Domain Security
  slug: america-movil-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: america-movil
tags:
- Telecommunications
- Mexico
- Latin America
- Mobile Network Operator
- Network APIs
- CAMARA
- Open Gateway
- SIM Swap
- Identity Verification
- Device Location
- Broadband
- 5G
- Carrier
website: https://www.americamovil.com/
---
