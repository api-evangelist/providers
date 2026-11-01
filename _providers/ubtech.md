---
access_model:
  confidence: medium
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  trial: false
  try_now: false
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
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.2
  scored_at: '2026-10-31'
api_count: 1
apis:
- baseURL: http://<robot-ip>:9090/v1
  baseurl_source: declared
  description: Receive data from remote device.
  name: UBTech Subscriptions API
  slug: ubtech-subscriptions-api
artifact_total: 7
asyncapis:
- description: ''
  name: Ubtech Yanshee Subscriptions Webhooks
  slug: ubtech-yanshee-subscriptions-webhooks
collections:
- collection_type: open
  name: Yanshee Open ADK subscriptions API
  slug: open-ubtech-subscriptions-api
common:
- group: company
  title: ''
  type: Website
  url: https://ubtrobot.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://yandev.ubtrobot.com/
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/UBTEDU/Yan_ADK/tree/master/docs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/UBTEDU
- group: company
  title: ''
  type: Blog
  url: https://www.ubtrobot.com/en/about/news
- group: operate
  title: ''
  type: Support
  url: https://www.ubtrobot.com/en/support/downloads
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ubtrobot.com/en/privacy/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ubtrobot.com/en/privacy/term-of-use
- group: auth
  title: ''
  type: Security
  url: https://www.ubtrobot.com/en/privacy/loophole/
- group: auth
  href: https://artifacts.apis.io/ubtech/security/ubtech-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/ubtech-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/ubtech/security/ubtech-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ubtech-domain-security.yml
- group: build
  href: https://artifacts.apis.io/ubtech/packages/ubtech-packages.yml
  title: ''
  type: Packages
  url: packages/ubtech-packages.yml
- group: build
  href: https://artifacts.apis.io/ubtech/packages/ubtech-packages.yml
  title: ''
  type: SDKs
  url: packages/ubtech-packages.yml
- group: agent
  href: https://artifacts.apis.io/ubtech/mcp/ubtech-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/ubtech-mcp.yml
- group: agent
  href: https://artifacts.apis.io/ubtech/llms/ubtech-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ubtech-llms.txt
- group: other
  href: https://artifacts.apis.io/ubtech/overlays/ubtech-yanshee-openadk-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/ubtech-yanshee-openadk-overlay.yaml
- group: design
  href: https://artifacts.apis.io/ubtech/conformance/ubtech-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ubtech-conformance.yml
- group: design
  href: https://artifacts.apis.io/ubtech/lifecycle/ubtech-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/ubtech-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/ubtech/changelog/ubtech-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/ubtech-changelog.yml
- group: design
  href: https://artifacts.apis.io/ubtech/conventions/ubtech-conventions.yml
  title: ''
  type: Conventions
  url: conventions/ubtech-conventions.yml
- group: auth
  href: https://artifacts.apis.io/ubtech/authentication/ubtech-authentication.yml
  title: ''
  type: Authentication
  url: authentication/ubtech-authentication.yml
- group: design
  href: https://artifacts.apis.io/ubtech/asyncapi/ubtech-yanshee-subscriptions-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/ubtech-yanshee-subscriptions-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/ubtech/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: UBTech Robotics is a Shenzhen-based robotics company building humanoid robots (the Walker series), commercial service robots (Cruzr, CADEBOT), AI education robots and kits (Yanshee, uKit, UGOT, Jimu), and consumer smart hardware (Alpha robots, AIRROBO). Its developer surface centers on the Yanshee educational humanoid, an open Raspberry Pi-based robot that exposes a device-local REST API (Yanshee Open ADK, Swagger 2.0) with an on-robot Swagger UI, a push-based subscription event surface, and Python, C, and Arduino SDKs published through the UBTEDU GitHub organization.
image: https://avatars.githubusercontent.com/u/32864785?v=4
layout: provider
modified: '2026-07-21'
name: UBTech
nav: Providers
network: true
overview: 'UBTech publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Subscriptions API. Tagged areas include Company, Robotics, Humanoid Robots, Education Technology, and Artificial Intelligence.


  The UBTech catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  UBTech''s developer surface includes documentation, engineering blog, support, changelog, authentication, and 18 more developer resources.'
random_paper: 11
score:
  band: developing
  composite: 42.3
  coverage:
    artifact_dirs: 18
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 44.3
    developer_ergonomics: 66.1
    discoverability: 66.1
    operational_transparency: 39.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - china
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - greater-china
  previous_composite: 42.3
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 28.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/ubtech/ubtech-2026-09-02T164832.png
security:
- kind: authentication
  name: Ubtech Authentication
  slug: ubtech-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Ubtech Domain Security
  slug: ubtech-domain-security
  summary_line: TLSv1.2 · DMARC
- kind: vulnerability-disclosure
  name: Ubtech Vulnerability Disclosure
  slug: ubtech-vulnerability-disclosure
  summary_line: Hackerone
skill_count: 1
skills:
- name: Receive Yanshee robot events
  slug: ubtech-receive-yanshee-events
slug: ubtech
tags:
- Company
- Robotics
- Humanoid Robots
- Education Technology
- Artificial Intelligence
- Consumer Electronics
- Service Robots
website: https://ubtrobot.com
---
