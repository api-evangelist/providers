---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.1
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: The gRPC surface a HARIX skill application uses to drive a CloudMinds cloud robot and to consume HARIX cloud AI. Five robotSkillApi services cover control (move/rotate/stop/emergency-stop, RCU reboot/
  name: HARIX Robot Skill API (gRPC)
  slug: harix-robot-skill-api
artifact_total: 6
asyncapis:
- description: ''
  name: Cloudminds Harix Events
  slug: cloudminds-harix-events
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cloudminds-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.dataarobotics.com/en
- group: start
  title: ''
  type: DeveloperPortal
  url: https://harix.dataarobotics.com/#/index/community/home
- group: company
  title: ''
  type: Blog
  url: https://www.dataarobotics.com/en/blog/index
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/HarixRDK
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CloudmindsRobot
- group: operate
  title: ''
  type: Support
  url: mailto:robotsupport@dataarobotics.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dataarobotics.com/zh/Uploads/contact/%E8%BE%BE%E9%97%BC%E5%AE%98%E7%BD%91%E9%9A%90%E7%A7%81%E6%94%BF%E7%AD%96.pdf
- group: build
  title: ''
  type: Packages
  url: packages/cloudminds-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/cloudminds-packages.yml
- group: other
  title: ''
  type: Protobuf
  url: grpc/cloudminds-grpc-index.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cloudminds-conventions.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cloudminds-authentication.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/cloudminds-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cloudminds-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cloudminds-lifecycle.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/cloudminds-harix-events.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/cloudminds-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cloudminds-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cloudminds-llms.txt
created: '2026-07-17'
description: CloudMinds — now operating as Dataa Robotics (达闼机器人股份有限公司) — is a cloud-robotics company founded in 2015, originally with dual headquarters in Beijing, China and Santa Clara/Irvine, California, and backed by SoftBank and Foxconn. It builds cloud-connected smart machines and the HARIX ("Human Augmented Robot Intelligence with eXtreme reality") cloud AI robot brain, operating cloud robots over its robot secure private network and a digital-twin simulation layer. Its developer offering is the HARIX Robot Development Kit (RDK) — an app behavior blueprint editor, motion/dance editor, scene-map tools, and a robot simulation/training platform — distributed through the HARIX RDK portal, the HarixRDK GitHub organization, and the official "harix" Python SDK on PyPI. CloudMinds publishes no OpenAPI and no public REST API; its machine-readable contract is gRPC/protobuf3 — 14 services and 88 RPCs across robot control, navigation, configuration, TTS, skill dispatch, speech recognition, vision
  recognition and NLU — shipped as compiled descriptors inside the first-party Python SDK. The US-facing cloudminds.com domain no longer answers; the live corporate surface is dataarobotics.com. Added to the U.S. BIS Entity List in May 2020.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cloudminds.png
layout: provider
modified: '2026-08-10'
name: CloudMinds
nav: Providers
network: true
overview: 'CloudMinds publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Frontier Tech, Robotics, Cloud Robotics, and Artificial Intelligence.


  The CloudMinds catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  CloudMinds'' developer surface includes engineering blog, support, authentication, and 17 more developer resources.'
plans:
- name: Cloudminds Plans Pricing
  plan_count: 0
  slug: cloudminds-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Cloudminds Rate Limits
  slug: cloudminds-rate-limits
score:
  band: thin
  composite: 27.3
  coverage:
    artifact_dirs: 14
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 4.5
    contract_quality: 41.6
    developer_ergonomics: 31.0
    discoverability: 66.7
    governance: 4.5
    operational_transparency: 10.5
  previous_composite: 27.3
  provenance:
    conformance: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
security:
- kind: authentication
  name: Cloudminds Authentication
  slug: cloudminds-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Cloudminds Domain Security
  slug: cloudminds-domain-security
  summary_line: TLSv1.3 · HSTS
slug: cloudminds
tags:
- Company
- Frontier Tech
- Robotics
- Cloud Robotics
- Artificial Intelligence
- Robot Development Kit
- HARIX
- gRPC
- Protobuf
- Robot Operating System
- Computer-Vision
- Speech Recognition
website: https://www.dataarobotics.com/en
---
