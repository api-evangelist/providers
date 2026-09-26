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
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-09-25'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://kinvey.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Kinvey
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/kinvey/refs/heads/main/packages/kinvey-packages.yml
  title: ''
  type: Packages
  url: packages/kinvey-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/kinvey/refs/heads/main/packages/kinvey-packages.yml
  title: ''
  type: SDKs
  url: packages/kinvey-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/kinvey/refs/heads/main/cli/kinvey-cli.yml
  title: ''
  type: CLI
  url: cli/kinvey-cli.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kinvey/refs/heads/main/lifecycle/kinvey-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/kinvey-lifecycle.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/kinvey/refs/heads/main/llms/kinvey-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/kinvey-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/kinvey/refs/heads/main/security/kinvey-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/kinvey-domain-security.yml
created: '2026-07-17'
description: Kinvey was a mobile Backend-as-a-Service (BaaS / mBaaS) platform providing app developers with hosted data storage, user management and authentication, file storage, push notifications, caching/offline sync, and serverless business logic through its Flex (FlexData / FlexFunctions) services. It shipped first-party client SDKs for web, Node.js, iOS/macOS (Swift), Android/Java, Xamarin/.NET, NativeScript, Angular/Ionic, and Cordova/PhoneGap, plus a command-line utility for managing apps, environments, and Flex microservices. Kinvey was acquired by Progress Software; the standalone developer surface has since been retired (kinvey.com redirects into Progress and the GitHub organization was archived in February 2025), though the published SDKs and CLI remain available on their package registries.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kinvey.png
layout: provider
modified: '2026-07-19'
name: Kinvey
nav: Providers
network: true
overview: 'Kinvey is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Backend-as-a-Service, Mobile, SDK, and Serverless.


  Kinvey''s developer surface includes CLI and 7 more developer resources.'
random_paper: 2
score:
  band: minimal
  composite: 7.3
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.6
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 55.4
    operational_transparency: 2.6
  previous_composite: 8.9
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Kinvey Domain Security
  slug: kinvey-domain-security
  summary_line: DMARC
slug: kinvey
tags:
- Company
- Backend-as-a-Service
- Mobile
- SDK
- Serverless
- Data Storage
- Authentication
- Push Notifications
website: https://kinvey.com/
---
