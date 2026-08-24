---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: na
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.7
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Google Voice Agentic Access
  operation_count: 3
  slug: google-voice-agentic-access
  summary_line: 3 operations
api_count: 2
apis:
- description: Manage Google Voice locations
  name: Google Voice Locations API
  slug: google-voice-locations-api
- description: Manage Google Voice user assignments
  name: Google Voice Users API
  slug: google-voice-users-api
artifact_total: 17
collections:
- collection_type: postman
  name: Google Voice Locations API
  slug: postman-google-voice-locations-api
- collection_type: postman
  name: Google Voice Locations Users API
  slug: postman-google-voice-users-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Google Voice Locations API
  slug: open-google-voice-locations-api
- collection_type: open
  name: Google Voice Locations Users API
  slug: open-google-voice-users-api
- collection_type: open
  name: Google Voice API
  slug: open-openapi
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/google-voice/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-voice-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-voice-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-voice-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://workspace.google.com/products/voice/
- group: start
  title: ''
  type: GettingStarted
  url: https://support.google.com/voice/answer/115061
- group: docs
  title: ''
  type: Documentation
  url: https://developers.google.com/workspace/products/voice
- group: auth
  title: ''
  type: Authentication
  url: https://developers.google.com/workspace/guides/auth-overview
- group: commercial
  title: ''
  type: Pricing
  url: https://workspace.google.com/products/voice/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://policies.google.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://policies.google.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cloud.google.com/
- group: operate
  title: ''
  type: Support
  url: https://support.google.com/voice
- group: design
  title: ''
  type: JSONLD
  url: https://raw.githubusercontent.com/api-evangelist/google-voice/refs/heads/main/json-ld/google-voice.jsonld
- group: company
  title: ''
  type: Blog
  url: https://workspaceupdates.googleblog.com/feeds/posts/default?alt=rss
created: '2026-03-13'
description: Google Voice is a telecommunications service by Google that provides call forwarding, voicemail, text messaging, and voice calling for personal and Google Workspace business accounts. While Google Voice does not offer an official standalone REST API, voice services can be managed programmatically through the Google Workspace Admin SDK for provisioning users, assigning numbers, and managing locations. Google Voice integrates with Google Workspace for enterprise telephony management.
finops:
- name: Google Voice Finops
  service_category: API
  slug: google-voice-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-voice.png
json_schemas:
- name: Google Voice API Schema
  property_count: 0
  slug: google-voice
jsonld:
- class_count: 0
  name: Google Voice Context
  property_count: 9
  slug: google-voice
layout: provider
modified: '2026-05-19'
name: Google Voice
nav: Providers
network: true
overview: 'Google Voice publishes 2 APIs on the [APIs.io](https://apis.io/) network: Locations API and Users API. Tagged areas include Google Voice, Messaging, Phone, Telecommunications, and Voice.


  The Google Voice catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Google Voice''s developer surface includes developer portal, getting-started guide, documentation, authentication, pricing, support, engineering blog, and 8 more developer resources.'
plans:
- name: Google Voice Plans Pricing
  plan_count: 3
  slug: google-voice-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 5
  name: Google Voice Rate Limits
  slug: google-voice-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Google Voice API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: google-voice-jsonschema-spectral-rules
score:
  band: developing
  composite: 43.0
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 9.8
    contract_quality: 58.7
    developer_ergonomics: 28.6
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 23.7
  previous_composite: 43.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 43.1
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-voice/refs/heads/main/screenshots/google-voice-2026-06-20T182246.png
security:
- kind: domain-security
  name: Google Voice Domain Security
  slug: google-voice-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Voice Vulnerability Disclosure
  slug: google-voice-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-voice
tags:
- Google Voice
- Messaging
- Phone
- Telecommunications
- Voice
- Voicemail
- VoIP
website: https://workspace.google.com/products/voice/
---
