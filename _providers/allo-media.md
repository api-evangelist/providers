---
agent_readiness:
  band: agent-ready
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
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.8
  scored_at: '2026-09-01'
api_count: 4
apis:
- description: 'Read-only REST API over calls that have finished processing on the Allo-Media platform — transcription, redaction, analysis and tagging complete. Three operations: list calls with date/status filters '
  name: Allo-Media Activate API
  slug: allo-media-activate-api
- description: Real-time transcription of live human-to-human conversations over a WebSocket (Phoenix Channels). A client joins a conversation, streams binary audio chunks, and receives interim and final decoded seg
  name: Allo-Media Stream API for Humans
  slug: allo-media-stream-api-humans
- description: Real-time speech recognition for voicebots and IVR (human-to-bot), offered over either MRCP or WebSocket, with regex-based grammars constraining expected input. Documents its own input/output model, g
  name: Allo-Media Stream API for Voicebots
  slug: allo-media-stream-api-voicebots
- description: First-party browser JavaScript that performs dynamic number insertion so an inbound phone call can be attributed back to a web session — the mechanism behind the Vocal Cookie lead-attribution product.
  name: Allo-Media Hermes Call Tracking
  slug: allo-media-hermes
artifact_total: 11
asyncapis:
- description: ''
  name: Allo Media Events
  slug: allo-media-events
common:
- group: company
  title: ''
  type: Website
  url: https://uh.live/en/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.allo-media.net/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.allo-media.net/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.allo-media.net/activate-api/rest/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.allo-media.net/activate-api/rest/getting-started/
- group: operate
  title: ''
  type: Support
  url: https://uh.live/en/contact/
- group: company
  title: ''
  type: Blog
  url: https://uh.live/en/articles/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/allo-media
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/uhlive
- group: operate
  title: ''
  type: Roadmap
  url: https://docs.allo-media.net/products-description/roadmap/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.uh.live/
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.allo-media.net/activate-api/rest/older-version/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://uh.live/en/legal-notices/
- group: auth
  title: ''
  type: Authentication
  url: authentication/allo-media-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/allo-media-scopes.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/allo-media-openid-configuration.json
- group: design
  title: ''
  type: Conventions
  url: conventions/allo-media-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/allo-media-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/allo-media-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/allo-media-changelog.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/allo-media-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/allo-media-plans-pricing.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/allo-media-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/allo-media-components.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/allo-media-conformance.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/allo-media-events.yml
- group: build
  title: ''
  type: Packages
  url: packages/allo-media-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/allo-media-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/allo-media-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/allo-media-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: https://uh.live/.well-known/security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/allo-media-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://uh.live/.well-known/security.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/allo-media-domain-security.yml
created: '2026-08-17'
description: 'Allo-Media, which now trades as uh!ive, is a French conversational-voice-AI company that transcribes and analyses telephone conversations in real time and in batch. Its platform pairs speech-to-text tuned for 8kHz telephony with named entity recognition and redaction, speech analytics (intent, emotion and compliance tagging) and call tracking, hosted in France. Developers integrate through four surfaces: a read-only Activate REST API over processed calls and their transcripts, a WebSocket Stream API for live human-to-human conversations, an MRCP/WebSocket Stream API for voicebots, and a browser call-tracking script (Hermes), plus SFTP batch ingestion (JUpload) and an HMAC-signed webhook. Authentication is OAuth 2.0 client_credentials against a Keycloak realm; credentials are issued by an account manager rather than self-service.'
image: https://avatars.githubusercontent.com/u/30897478?v=4
layout: provider
modified: '2026-08-17'
name: Allo-Media
nav: Providers
network: true
overview: 'Allo-Media publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Ai Data, Speech Recognition, Speech-to-Text, and Conversation Intelligence.


  The Allo-Media catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Allo-Media''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, changelog, and 27 more developer resources.'
plans:
- name: Allo Media Plans Pricing
  plan_count: 0
  slug: allo-media-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 4
  name: Allo Media Rate Limits
  slug: allo-media-rate-limits
scopes:
- name: Allo Media Scopes
  scope_count: 19
  slug: allo-media-scopes
  summary_line: 19 scopes · clientCredentials/authorizationCode/deviceCode/password/refreshToken/tokenExchange/jwtBearer/uma/ciba
score:
  band: developing
  composite: 48.8
  coverage:
    artifact_dirs: 18
    catalog_gap: 63.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.3
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 64.3
    discoverability: 92.6
    governance: 18.2
    operational_transparency: 92.1
  previous_composite: 49.1
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Allo Media Authentication
  slug: allo-media-authentication
  summary_line: oauth2/openIdConnect/http · 5 schemes
- kind: domain-security
  name: Allo Media Domain Security
  slug: allo-media-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Allo Media Vulnerability Disclosure
  slug: allo-media-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: allo-media
tags:
- Company
- Ai Data
- Speech Recognition
- Speech-to-Text
- Conversation Intelligence
- Call Tracking
- Voice AI
- Natural Language Processing
- Call Analytics
- Contact Center
- Speech Analytics
- Transcription
- France
website: https://uh.live/en/
---
