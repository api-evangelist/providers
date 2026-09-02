---
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-01'
api_count: 2
apis:
- description: The HTTP API at api.vrchat.cloud/api/1 that backs the VRChat client and the vrchat.com website — authentication, users, friends, worlds, avatars, instances, groups, files and notifications. VRChat ope
  name: VRChat Web API
  slug: vrchat-web-api
- description: The VRChat Package Manager repository API — machine-readable VPM listing documents served over HTTP that enumerate every first-party VRChat SDK package (Base, Worlds, Avatars, Package Resolver) and th
  name: VRChat Package Manager (VPM) Listing API
  slug: vrchat-vpm
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vrchat-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://hello.vrchat.com/
- group: other
  title: ''
  type: Application
  url: https://vrchat.com/home
- group: start
  title: ''
  type: DeveloperPortal
  url: https://creators.vrchat.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.vrchat.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://creators.vrchat.com/sdk/
- group: company
  title: ''
  type: Blog
  url: https://hello.vrchat.com/blog
- group: operate
  title: ''
  type: Support
  url: https://ask.vrchat.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/vrchat-community
- group: start
  title: ''
  type: SignUp
  url: https://vrchat.com/home/register
- group: start
  title: ''
  type: Login
  url: https://vrchat.com/home/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://hello.vrchat.com/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://hello.vrchat.com/privacy
- group: docs
  title: ''
  type: CreatorGuidelines
  url: https://hello.vrchat.com/creator-guidelines
- group: docs
  title: ''
  type: CommunityGuidelines
  url: https://hello.vrchat.com/community-guidelines
- group: other
  title: ''
  type: FeatureRequests
  url: https://feedback.vrchat.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.vrchat.com
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.vrchat.com/docs/recent-releases
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/vrchat-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/vrchat-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/vrchat-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/vrchat-cli.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/vrchat-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/vrchat-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/vrchat-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/vrchat-conformance.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/vrchat-changelog.yml
created: '2026-08-05'
description: 'VRChat is a social virtual-reality platform where users create avatars and worlds in Unity with the first-party VRChat SDK (Worlds, Avatars, Udon and UdonSharp), publish them through the VRChat Package Manager, and meet inside a persistent multi-user universe playable on PC VR, standalone headsets and desktop. VRChat operates a live web API at api.vrchat.cloud that powers its own client and website, but it explicitly does not document, version, or support that API for public use: its Creator Guidelines state endpoints may be added, removed, or changed with no warning. The machine-readable surface VRChat does publish is the creator toolchain — the VPM package listings at packages.vrchat.com, the vpm CLI on NuGet, the OSC and OSCQuery interfaces for external avatar and input control, an llms.txt documentation index, and a public Statuspage.'
image: https://static1.squarespace.com/static/5f0770791aaf57311515b23d/t/6508c787b8ced41ca3404f36/1718212268632/VRC_Logo.png?format=1500w
layout: provider
modified: '2026-08-05'
name: VRChat
nav: Providers
network: true
overview: 'VRChat publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Virtual Reality, Social Networks, Gaming, and Metaverse.


  VRChat''s developer surface includes documentation, getting-started guide, engineering blog, support, signup flow, changelog, CLI, and 20 more developer resources.'
random_paper: 18
score:
  band: thin
  composite: 33.0
  coverage:
    artifact_dirs: 11
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 59.5
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 34.2
  previous_composite: 33.0
  provenance:
    conformance: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Vrchat Domain Security
  slug: vrchat-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: vrchat
tags:
- Company
- Virtual Reality
- Social Networks
- Gaming
- Metaverse
- Avatars
- Unity
- Creator Economy
- User Generated Content
- OSC
website: https://hello.vrchat.com/
---
