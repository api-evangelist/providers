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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-07-28'
api_count: 7
apis:
- description: The Buildpack API is the contract between a buildpack and the lifecycle. It defines the detect and build executables, layers, build-plan provisions and requirements, and image extension lifecycle that
  name: Buildpack API
  slug: buildpack-api
- description: The Platform API is the contract between the CNB lifecycle and a platform such as pack, kpack, or a CI runner. It defines how builders, stacks, run images, and inputs are passed to the lifecycle phase
  name: Platform API
  slug: platform-api
- description: The Distribution API specifies how buildpacks and builders are packaged as OCI artifacts, signed, and distributed through OCI registries. It also covers how meta-buildpacks compose other buildpacks an
  name: Distribution API
  slug: distribution-api
- description: pack is the reference command-line interface for Cloud Native Buildpacks. It implements the Platform API to build OCI images from source on a developer's workstation, manages builders and buildpack pa
  name: pack CLI
  slug: pack-cli
- description: The CNB Lifecycle is the reference implementation of the Buildpack and Platform APIs. It runs the detect, analyze, restore, build, export, and rebase phases used by all CNB platforms to produce reprod
  name: CNB Lifecycle
  slug: lifecycle
- description: kpack is a community Kubernetes-native implementation of Cloud Native Buildpacks. It exposes Image, Builder, ClusterBuilder, and ClusterStack custom resources for declaring continuously rebuilt OCI im
  name: kpack
  slug: kpack
- description: The Cloud Native Buildpacks registry indexes published buildpacks for discovery and reuse. It mirrors metadata for buildpack packages stored in OCI registries and exposes a browseable catalog at regis
  name: Buildpack Registry
  slug: registry
artifact_total: 10
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cloud-native-buildpacks-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://buildpacks.io/
- group: docs
  title: ''
  type: Documentation
  url: https://buildpacks.io/docs/
- group: docs
  title: ''
  type: Specification
  url: https://github.com/buildpacks/spec
- group: build
  title: ''
  type: GitHub
  url: https://github.com/buildpacks
- group: operate
  title: ''
  type: Community
  url: https://buildpacks.io/community/
- group: operate
  title: ''
  type: Slack
  url: https://slack.cncf.io/
- group: company
  title: ''
  type: Blog
  url: https://medium.com/buildpacks
- group: operate
  title: ''
  type: RoadMap
  url: https://github.com/buildpacks/roadmap
- group: other
  title: ''
  type: CNCF
  url: https://www.cncf.io/projects/buildpacks/
- group: design
  title: ''
  type: JSONLD
  url: json-ld/cloud-native-buildpacks-context.jsonld
- group: design
  title: ''
  type: Spectral
  url: rules/cloud-native-buildpacks-rules.yml
created: '2024-01-01'
description: Cloud Native Buildpacks (CNB) is a CNCF-graduated specification and set of tooling for transforming application source code into OCI images that can run on any cloud. The project unifies the Heroku and Cloud Foundry buildpack ecosystems around an open standard for detection, build, and image export. The reference implementation lifecycle, the pack CLI for local builds, the kpack server-side builder, and a registry of distribution buildpacks together form the CNB ecosystem. CNB is built around a documented Buildpack API, Platform API, and Distribution API, all versioned and published in the github.com/buildpacks specifications.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cloud-native-buildpacks.png
jsonld:
- class_count: 0
  name: Cloud Native Buildpacks Context
  property_count: 7
  slug: cloud-native-buildpacks-context
layout: provider
modified: '2026-04-23'
name: Cloud Native Buildpacks
nav: Providers
network: true
overview: 'Cloud Native Buildpacks publishes 7 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Buildpacks, CNCF, Containers, Images, and OCI.


  The Cloud Native Buildpacks catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Cloud Native Buildpacks'' developer surface includes documentation, GitHub presence, engineering blog, and 9 more developer resources.'
random_paper: 34
rules:
- name: Cloud Native Buildpacks API Rules
  rule_count: 8
  severity_counts:
    error: 3
    hint: 0
    info: 1
    warn: 4
  slug: cloud-native-buildpacks-rules
score:
  band: emerging
  composite: 16.2
  delta: -3.4
  facets:
    commercial_clarity: 0.0
    contract_quality: 8.1
    developer_ergonomics: 15.2
    discoverability: 64.8
    governance: 27.1
    operational_transparency: 10.5
  previous_composite: 19.6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cloud-native-buildpacks/refs/heads/main/screenshots/cloud-native-buildpacks-2026-06-20T174537.png
security:
- kind: domain-security
  name: Cloud Native Buildpacks Domain Security
  slug: cloud-native-buildpacks-domain-security
  summary_line: TLSv1.3 · HSTS
slug: cloud-native-buildpacks
tags:
- Buildpacks
- CNCF
- Containers
- Images
- OCI
- Open Source
- Platform
- Reproducible Builds
website: https://buildpacks.io/
---
