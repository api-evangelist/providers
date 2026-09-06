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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 43.3
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Canonical Agentic Access
  operation_count: 12
  slug: canonical-agentic-access
  summary_line: 12 operations · 5 acting
api_count: 1
apis:
- description: The public Snap Store Device API (api.snapcraft.io) serves information about snaps, revisions, channels, tracks, assertions, and refresh state to snap clients. The Snapcraft Dashboard API (dashboard.s
  name: Snap Store API
  slug: snap-store-api
- description: Developer-facing REST API for Charmhub, Canonical's marketplace for charms (Kubernetes and machine operators). Supports charm discovery, publishing, release channels, and token exchange — macaroons is
  name: Charmhub API
  slug: charmhub-api
- baseURL: unix:///run/snapd.socket
  baseurl_source: spec
  description: The local REST API exposed by snapd over a Unix domain socket on every Ubuntu system running snaps. Enables local clients and tools to query snap state, install / refresh / remove snaps, manage interf
  name: snapd REST API
  slug: snapd-rest-api
- description: The RESTful API for MAAS (Metal as a Service). Everything the MAAS UI can do — commissioning, allocation, deployment, DHCP/DNS, tags, zones, pools, users, machines — is available through the API, maki
  name: MAAS API
  slug: maas-api
- description: Juju is Canonical's open-source orchestration engine for deploying, integrating, scaling, and managing applications on clouds, MAAS, LXD, and Kubernetes via charms. Juju clients communicate with a con
  name: Juju Client / Controller API
  slug: juju-api
- description: Launchpad exposes a RESTful Web Services API over its project hosting, bug tracking, code, builds, translations, and distribution data. The API is authenticated with OAuth; anonymous access gives read
  name: Launchpad Web Services API
  slug: launchpad-api
- description: The Ubuntu Pro client exposes a local API/CLI for managing Ubuntu Pro subscription services on a host — enabling, disabling, and inspecting Extended Security Maintenance (ESM), Livepatch, FIPS, compli
  name: Ubuntu Pro Client API
  slug: ubuntu-pro-api
- description: Canonical Landscape is the systems-management platform for Ubuntu at scale. Its API lets operators manage and automate inventories, upgrades, patch compliance, reboots, scripts, monitoring, and alerts
  name: Landscape API
  slug: landscape-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: The Assertions API from Canonical — 1 operation(s) for assertions.
  name: Canonical Assertions API
  slug: canonical-assertions-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: The Search API from Canonical — 1 operation(s) for search.
  name: Canonical Search API
  slug: canonical-search-api
- baseURL: https://api.snapcraft.io
  baseurl_source: declared
  description: The Snaps API from Canonical — 10 operation(s) for snaps.
  name: Canonical Snaps API
  slug: canonical-snaps-api
- baseURL: https://<lxd-host>:8443
  baseurl_source: declared
  description: The REST API used by every LXD client. LXD is Canonical's system container and virtual machine manager; the API is available over a local unix+http socket and over remote https, authenticated by TLS c
  name: LXD REST API
  slug: lxd-rest-api
- baseURL: https://ubuntu.com
  baseurl_source: declared
  description: An open, unauthenticated API over Canonical's vulnerability data — Ubuntu Security Notices (USNs), CVE records with CVSS3 scoring, and per-release support status. Canonical publishes a Swagger 2.0 con
  name: Ubuntu Security API
  slug: ubuntu-security-api
- description: Pebble is Canonical's lightweight service manager, used inside snaps, ROCKs and Kubernetes charm workloads. It exposes a local REST API over a unix socket for managing services, layers, checks, files,
  name: Pebble API
  slug: pebble-api
- baseURL: https://testflinger.canonical.com
  baseurl_source: declared
  description: Testflinger is Canonical's hardware test-orchestration service. Its REST API accepts test jobs against named device queues, reports job status and results, serves build artifacts, and exposes agent an
  name: Testflinger API
  slug: testflinger-api
- baseURL: https://hw.ubuntu.com
  baseurl_source: declared
  description: The Ubuntu hardware certification API. Given a machine's hardware identifiers it reports whether that configuration is certified for Ubuntu and on which releases. Serves its own OpenAPI 3.1.0 contract
  name: Ubuntu Hardware API (hwapi)
  slug: hardware-api
- description: The API of Canonical's Identity Platform — an OIDC/OAuth 2.0 identity provider built on Ory and delivered as a Juju charm bundle. Covers identities, clients, schemas, providers, roles, groups, rules a
  name: Canonical Identity Platform API
  slug: identity-platform-api
- baseURL: https://test-observer-api.canonical.com
  baseurl_source: declared
  description: Test Observer is Canonical's dashboard for tracking test execution across Ubuntu artefacts — snaps, debs, charms and images — through their release stages. The backend publishes an OpenAPI 3.1.0 contr
  name: Test Observer API
  slug: test-observer-api
- description: The external REST API of the Anbox Management Service (AMS), the control plane of Canonical's Anbox Cloud product for running Android at scale. Covers applications, images, instances, nodes, addons, c
  name: Anbox Cloud AMS API
  slug: anbox-cloud-ams-api
- description: The Anbox Cloud streaming control API — creates and manages streaming sessions between clients and Android instances, plus the accounts, applications and configuration behind them. Canonical publishes
  name: Anbox Stream Gateway API
  slug: anbox-stream-gateway-api
- description: Part of the Canonical Observability Stack for robotics and edge fleets. The registration server API registers devices and manages their per-application configuration — Grafana dashboards, Foxglove lay
  name: COS Registration Server API
  slug: cos-registration-server-api
- description: MicroCeph is Canonical's opinionated, snap-delivered Ceph distribution. It publishes a small OpenAPI 3.1.0 contract for its cluster REST surface. Recorded here because it is a real published first-par
  name: MicroCeph REST API
  slug: microceph-api
artifact_total: 37
asyncapis:
- description: ''
  name: Canonical Launchpad Webhooks
  slug: canonical-launchpad-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Canonical Snap Store Device Assertions API
  slug: open-canonical-assertions-api
- collection_type: open
  name: Canonical Snap Store Device Assertions Search API
  slug: open-canonical-search-api
- collection_type: open
  name: Canonical Snap Store Device Assertions Snaps API
  slug: open-canonical-snaps-api
- collection_type: open
  name: Canonical Snap Store Device API
  slug: open-canonical
common:
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/canonical-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/canonical-authentication.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/canonical-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/canonical-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/canonical
- group: company
  title: ''
  type: Website
  url: https://canonical.com/
- group: company
  title: ''
  type: UbuntuWebsite
  url: https://ubuntu.com/
- group: docs
  title: ''
  type: Documentation
  url: https://documentation.ubuntu.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/canonical
- group: other
  title: ''
  type: SnapStore
  url: https://snapcraft.io/
- group: other
  title: ''
  type: Charmhub
  url: https://charmhub.io/
- group: other
  title: ''
  type: Launchpad
  url: https://launchpad.net/
- group: learn
  title: ''
  type: DiscourseForum
  url: https://discourse.ubuntu.com/
- group: commercial
  title: ''
  type: DataPrivacy
  url: https://ubuntu.com/legal/data-privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ubuntu.com/legal/terms
- group: company
  title: ''
  type: Blog
  url: https://canonical.com/blog/feed/
- group: build
  title: ''
  type: Packages
  url: packages/canonical-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/canonical-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/canonical-cli.yml
- group: design
  title: ''
  type: Components
  url: components/canonical-components.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/canonical-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/canonical-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/canonical-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/canonical-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/canonical-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/canonical-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.canonical.com/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/canonical-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/canonical-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/canonical-trust-center.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/canonical-trust-center.yml
- group: auth
  title: ''
  type: Security
  url: security/canonical-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/canonical-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/canonical-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/canonical-security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/canonical-llms.txt
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/canonical-launchpad-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/canonical-landscape-debarchive-provider-overlay.yaml
- group: commercial
  title: ''
  type: Plans
  url: plans/canonical-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/canonical-rate-limits.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://ubuntu.com/pricing/pro
- group: start
  title: ''
  type: SignUp
  url: https://ubuntu.com/pro/subscribe
- group: start
  title: ''
  type: Login
  url: https://login.ubuntu.com/
- group: operate
  title: ''
  type: Support
  url: https://ubuntu.com/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ubuntu.com/legal/data-privacy
- group: docs
  title: ''
  type: APIReference
  url: https://documentation.ubuntu.com/lxd/latest/rest-api/
- group: start
  title: ''
  type: GettingStarted
  url: https://ubuntu.com/tutorials
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/canonical
created: '2026-03-16'
description: Canonical is the company behind Ubuntu, the world's most popular open source operating system for cloud, servers, desktops, IoT, and Kubernetes. Canonical publishes a broad set of developer APIs spanning the Ubuntu and Canonical ecosystem — the Snap Store and Snapcraft, the Charmhub charm marketplace, LXD system containers, MAAS bare-metal provisioning, Juju orchestration, Launchpad project hosting, Ubuntu Pro subscription services, and Landscape systems management — most of which are RESTful, open, and well documented.
finops:
- name: Canonical Finops
  service_category: API
  slug: canonical-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/canonical.png
layout: provider
modified: '2026-09-05'
name: Canonical
nav: Providers
network: true
overview: 'Canonical publishes 16 APIs on the [APIs.io](https://apis.io/) network, including snapd REST API, Landscape API, Assertions API, and 13 more. Tagged areas include Cloud, Linux, Open-Source, Ubuntu, and Containers.


  The Canonical catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Canonical''s developer surface includes authentication, documentation, engineering blog, CLI, changelog, pricing, signup flow, and 42 more developer resources.'
plans:
- name: Canonical Plans Pricing
  plan_count: 4
  slug: canonical-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Canonical Rate Limits
  slug: canonical-rate-limits
scopes:
- name: Canonical Scopes
  scope_count: 3
  slug: canonical-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: strong
  composite: 62.9
  coverage:
    artifact_dirs: 26
    catalog_earned: 47.0
    catalog_earned_first_party: 12.0
    catalog_gap: 68.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 31.6
  facets:
    access_clarity: 100.0
    commercial_clarity: 100.0
    contract_governance: 18.2
    contract_quality: 46.2
    developer_ergonomics: 73.2
    discoverability: 66.7
    governance: 18.2
    operational_transparency: 60.5
  previous_composite: 31.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 23.1
      derived: 3
      marker_coverage: 23.1
      total: 13
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/canonical/refs/heads/main/screenshots/canonical-2026-06-20T173927.png
security:
- kind: authentication
  name: Canonical Authentication
  slug: canonical-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Canonical Domain Security
  slug: canonical-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Canonical Vulnerability Disclosure
  slug: canonical-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Canonical Trust Center
  slug: canonical-trust-center
  summary_line: trust center published
slug: canonical
tags:
- Cloud
- Linux
- Open-Source
- Ubuntu
- Containers
- Bare Metal
- Charms
- Identity
website: https://canonical.com/
---
