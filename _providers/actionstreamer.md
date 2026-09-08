---
agent_readiness:
  band: agent-aware
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.0
  scored_at: '2026-09-07'
api_count: 1
apis:
- baseURL: https://api.actionstreamer.com/v1
  baseurl_source: declared
  description: The ActionStreamer HTTP Web API — 186 paths and 247 operations across 43 resource areas — for managing devices, device health telemetry, device groups, Wi-Fi connections, events and event presets, liv
  name: ActionStreamer Web API
  slug: actionstreamer-web-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://actionstreamer.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.actionstreamer.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.actionstreamer.com/docs/intro
- group: docs
  title: ''
  type: APIReference
  url: https://developer.actionstreamer.com/docs/category/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.actionstreamer.com/docs/Guides/http-api-quickstart
- group: auth
  title: ''
  type: Authentication
  url: authentication/actionstreamer-authentication.yml
- group: start
  title: ''
  type: SignUp
  url: https://portal.actionstreamer.com/
- group: operate
  title: ''
  type: Support
  url: https://actionstreamer.com/contact
- group: company
  title: ''
  type: Blog
  url: https://actionstreamer.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ActionStreamer
- group: commercial
  title: ''
  type: TermsOfService
  url: https://actionstreamer.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://actionstreamer.com/privacy-policy
- group: build
  title: ''
  type: Packages
  url: packages/actionstreamer-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/actionstreamer-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/actionstreamer-llms.txt
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/actionstreamer-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/actionstreamer-vocabulary.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/actionstreamer-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/actionstreamer-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/actionstreamer-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/actionstreamer-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/actionstreamer-rate-limits.yml
created: '2026-09-06'
description: 'ActionStreamer is a Cincinnati, Ohio IoT video platform company, founded in 2016, that builds wearable and connected-device live streaming technology for industrial, public-safety, defense, aerospace/MRO and sports operations. Its ActionSync platform manages fleets of smart cameras and body-worn devices, moving live and store-and-forward video over Wi-Fi, private 5G, cellular and Starlink links, and its IRIS product layers AI object detection and alerting on top. ActionStreamer publishes a public developer platform at developer.actionstreamer.com: a 247-operation HTTP Web API at api.actionstreamer.com covering devices, device health, events, event presets, streams, video and audio clips, images, files, users and API keys, authenticated with HMAC-SHA256 request signing, plus a first-party Python library distributed on PyPI as "actionstreamer".'
image: https://framerusercontent.com/assets/nR8rjxhDfFwVzDiGHu10CgzYmZs.png
layout: provider
modified: '2026-09-06'
name: ActionStreamer
nav: Providers
network: true
overview: 'ActionStreamer publishes 1 API on the [APIs.io](https://apis.io/) network: Web API. Tagged areas include Company, Video, Live Streaming, Wearables, and Internet of Things.


  ActionStreamer''s developer surface includes documentation, API reference, getting-started guide, authentication, signup flow, support, engineering blog, and 16 more developer resources.'
plans:
- name: Actionstreamer Plans Pricing
  plan_count: 0
  slug: actionstreamer-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Actionstreamer Rate Limits
  slug: actionstreamer-rate-limits
score:
  band: thin
  composite: 33.4
  coverage:
    artifact_dirs: 18
    catalog_earned: 42.0
    catalog_earned_first_party: 5.0
    catalog_gap: 73.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.9
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 19.7
    contract_quality: 33.3
    developer_ergonomics: 56.5
    discoverability: 68.5
    governance: 19.7
    operational_transparency: 2.6
  previous_composite: 38.3
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  schema_version: 0.20.0
  scored_at: '2026-09-07'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Actionstreamer Authentication
  slug: actionstreamer-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Actionstreamer Domain Security
  slug: actionstreamer-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: actionstreamer
tags:
- Company
- Video
- Live Streaming
- Wearables
- Internet of Things
- Device Management
- Public Safety
- Industrial
- Computer Vision
- Media
website: https://actionstreamer.com/
---
