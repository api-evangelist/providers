---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Veriff Agentic Access
  operation_count: 13
  slug: veriff-agentic-access
  summary_line: 13 operations · 6 acting
api_count: 15
apis:
- description: Uploads document images, selfies, and supporting media to a session and lists the media already attached. Used by custom flows that do not embed the Veriff SDK and capture media themselves.
  name: Veriff Media API
  slug: media
- description: Retrieves the final verification decision for a submitted session - status (approved, declined, resubmission, expired), reason, code, person data extracted from the document, and risk metadata. Availa
  name: Veriff Decisions API
  slug: decisions
- description: Lists individual attempts within a session - useful when a session results in resubmission. Each attempt carries its own captured media and reason metadata.
  name: Veriff Attempts API
  slug: attempts
- description: Retrieves the person record extracted from a session decision - structured fields (first name, last name, date of birth, document number, nationality) and document metadata used for downstream KYC and
  name: Veriff Persons API
  slug: persons
- description: Runs and retrieves PEP, sanctions, adverse-media, and ongoing-monitoring screening tied to a verification session or to a stand-alone identity payload.
  name: Veriff Watchlist Screening API
  slug: watchlist-screening
- description: Server-to-server delivery of decision and event notifications. Veriff signs each payload via the customer's shared secret using the X-HMAC-SIGNATURE header so receivers can verify authenticity. Custom
  name: Veriff Webhook Delivery
  slug: webhooks
- description: Browser-based capture experience that embeds verification inside the customer's site (InContext) or runs as a Veriff-hosted page. Requires a session token issued by the Sessions API.
  name: Veriff Web (InContext / Hosted) SDK
  slug: web-sdk
- description: Native iOS SDK that drives capture and streams media to Veriff. Initialised with a session URL.
  name: Veriff iOS SDK
  slug: ios-sdk
- description: Native Android SDK for capture and media upload. Initialised with a session URL from the Sessions API.
  name: Veriff Android SDK
  slug: android-sdk
- baseURL: https://stationapi.veriff.com/v1
  baseurl_source: declared
  description: The Attempts API from Veriff — 2 operation(s) for attempts.
  name: Veriff Attempts API
  slug: veriff-attempts-api
- baseURL: https://stationapi.veriff.com/v1
  baseurl_source: declared
  description: The Decisions API from Veriff — 1 operation(s) for decisions.
  name: Veriff Decisions API
  slug: veriff-decisions-api
- baseURL: https://stationapi.veriff.com/v1
  baseurl_source: declared
  description: The Media API from Veriff — 2 operation(s) for media.
  name: Veriff Media API
  slug: veriff-media-api
- baseURL: https://stationapi.veriff.com/v1
  baseurl_source: declared
  description: The Persons API from Veriff — 1 operation(s) for persons.
  name: Veriff Persons API
  slug: veriff-persons-api
- baseURL: https://stationapi.veriff.com/v1
  baseurl_source: declared
  description: The Sessions API from Veriff — 4 operation(s) for sessions.
  name: Veriff Sessions API
  slug: veriff-sessions-api
- baseURL: https://stationapi.veriff.com/v1
  baseurl_source: declared
  description: The Watchlist API from Veriff — 1 operation(s) for watchlist.
  name: Veriff Watchlist API
  slug: veriff-watchlist-api
artifact_total: 30
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Veriff Public Attempts API
  slug: open-veriff-attempts-api
- collection_type: open
  name: Veriff Public Attempts Decisions API
  slug: open-veriff-decisions-api
- collection_type: open
  name: Veriff Public Attempts Media API
  slug: open-veriff-media-api
- collection_type: open
  name: Veriff Public Attempts Persons API
  slug: open-veriff-persons-api
- collection_type: open
  name: Veriff Public Attempts Sessions API
  slug: open-veriff-sessions-api
- collection_type: open
  name: Veriff Public Attempts Watchlist API
  slug: open-veriff-watchlist-api
- collection_type: open
  name: Veriff Public API
  slug: open-veriff
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/veriff-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/veriff-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/veriff-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/veriff-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/veriff
- group: company
  title: ''
  type: Website
  url: https://www.veriff.com/
- group: docs
  title: ''
  type: Documentation
  url: https://devdocs.veriff.com/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/Veriff
- group: commercial
  title: ''
  type: Plans
  url: plans/veriff-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/veriff-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/veriff-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.veriff.com/feed
created: '2026-05-08'
description: Veriff is an AI-driven identity verification platform offering document, biometric, age, and proof-of-address verification, plus PEP/sanctions screening, ongoing monitoring, and Identity Fraud Protection. The Veriff Public API exposes session creation, media upload, decisions, attempts, watchlist screening, persons, and webhook delivery, with web and mobile SDKs hosting the capture experience.
finops:
- name: Veriff Finops
  service_category: Identity Verification
  slug: veriff-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/veriff.png
layout: provider
modified: '2026-05-19'
name: Veriff
nav: Providers
network: true
overview: 'Veriff publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Attempts API, Decisions API, Media API, and 3 more. Tagged areas include KYC, Identity Verification, Biometrics, Fraud Prevention, and AML.


  Veriff''s developer surface includes authentication, documentation, GitHub presence, engineering blog, and 8 more developer resources.'
plans:
- name: Veriff Plans Pricing
  plan_count: 6
  slug: veriff-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 3
  name: Veriff Rate Limits
  slug: veriff-rate-limits
score:
  band: thin
  composite: 28.3
  coverage:
    artifact_dirs: 10
    catalog_earned: 49.0
    catalog_earned_first_party: 0.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 44.9
    developer_ergonomics: 23.8
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 28.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/veriff/refs/heads/main/screenshots/veriff-2026-06-20T200925.png
security:
- kind: authentication
  name: Veriff Authentication
  slug: veriff-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Veriff Domain Security
  slug: veriff-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Veriff Vulnerability Disclosure
  slug: veriff-vulnerability-disclosure
  summary_line: disclosure policy published
slug: veriff
tags:
- KYC
- Identity Verification
- Biometrics
- Fraud Prevention
- AML
- Software-as-a-Service
website: https://www.veriff.com/
---
