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
  band: human-only
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/anybotics-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: security/anybotics-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/anybotics-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/anybotics-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/anybotics-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/anybotics-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/anybotics-security.txt
- group: company
  title: ''
  type: Website
  url: https://www.anybotics.com/anymal-autonomous-legged-robot/
- group: operate
  title: ''
  type: Support
  url: https://support.anybotics.com/
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://anybotics.com/responsible-disclosure
created: '2026-07-17'
description: ANYbotics is a Swiss deep-tech robotics company that builds ANYmal, an autonomous four-legged inspection robot used to automate routine and hazardous industrial inspections across power and utilities, oil and gas, mining, chemicals, and metals. Its platform pairs the legged robot with inspection-management software and analytics to increase plant uptime, cut costs, and remove workers from dangerous areas. ANYbotics is backed by Bessemer Venture Partners. No public developer API, SDK, or OpenAPI surface is exposed; this API Evangelist profile currently captures the company's published security and trust posture.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/anybotics.png
layout: provider
modified: '2026-07-18'
name: ANYbotics
nav: Providers
network: true
overview: 'ANYbotics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Deep Tech, Robotics, Industrial Automation, and Autonomous Inspection.


  ANYbotics'' developer surface includes support and 9 more developer resources.'
random_paper: 6
score:
  band: minimal
  composite: 10.5
  coverage:
    artifact_dirs: 3
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 10.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/anybotics/refs/heads/main/screenshots/anybotics-2026-07-25T200459.png
security:
- kind: domain-security
  name: Anybotics Domain Security
  slug: anybotics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Anybotics Vulnerability Disclosure
  slug: anybotics-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Anybotics Trust Center
  slug: anybotics-trust-center
  summary_line: SOC 2, ISO 27001
slug: anybotics
tags:
- Company
- Deep Tech
- Robotics
- Industrial Automation
- Autonomous Inspection
- Legged Robots
website: https://www.anybotics.com/anymal-autonomous-legged-robot/
---
