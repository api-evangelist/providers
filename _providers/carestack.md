---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 17.3
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: RESTful API surface for CareStack dental practice management, covering patient resources (patient information, health conditions, payment summaries, communications, treatment codes, documents) and pra
  name: CareStack API
  slug: carestack-api
artifact_total: 4
asyncapis:
- description: ''
  name: Carestack Webhooks
  slug: carestack-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.carestack.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.carestack.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://carestack.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://carestack.com/demo
- group: operate
  title: ''
  type: Support
  url: https://carestack.com/support
- group: company
  title: ''
  type: Blog
  url: https://resources.carestack.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://carestack.com/legal/2020-1/termsofuse
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://carestack.com/legal/2020-1/privacypolicy
- group: auth
  title: ''
  type: TrustCenter
  url: security/carestack-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.carestack.com/
- group: design
  title: ''
  type: Conformance
  url: conformance/carestack-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/carestack-domain-security.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/carestack-webhooks.yml
created: '2026-07-17'
description: CareStack is an all-in-one, cloud-based dental practice management platform used by dental practices and DSOs (dental service organizations) for scheduling, patient management, clinical charting, billing, payments, revenue cycle management, and analytics. For developers, CareStack exposes a RESTful API surface covering patient resources (patient information, health conditions, payment summaries, communications, treatment/procedure codes, and documents) and practice resources, complemented by webhooks for real-time data propagation and scheduled data extracts. The platform is HIPAA compliant and carries SOC 2 Type 2, ISO 27001:2022, and GDPR attestations, published via its trust center. This profile was surfaced as an Accel portfolio company and enriched by the API Evangelist pipeline.
image: https://a.storyblok.com/f/144863/1200x630/db57474aa8/carestack-og.png
layout: provider
modified: '2026-07-18'
name: CareStack
nav: Providers
network: true
overview: 'CareStack publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Dental, Practice Management, and Electronic Health Records.


  The CareStack catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  CareStack''s developer surface includes pricing, signup flow, support, engineering blog, and 9 more developer resources.'
random_paper: 0
score:
  band: thin
  composite: 36.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 16.7
    discoverability: 59.3
    governance: 18.2
    operational_transparency: 7.9
  previous_composite: 36.7
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 2
    matched_via: tags
    regime: Health
    regime_id: health
    score: 30.0
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/carestack/refs/heads/main/screenshots/carestack-2026-07-25T204559.png
security:
- kind: domain-security
  name: Carestack Domain Security
  slug: carestack-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Carestack Trust Center
  slug: carestack-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: carestack
tags:
- Company
- Healthcare
- Dental
- Practice Management
- Electronic Health Records
- Revenue Cycle Management
- Patient Engagement
- Payments
- Software-as-a-Service
website: https://www.carestack.com
---
