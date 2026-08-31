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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 17.3
  scored_at: '2026-08-30'
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
- description: The local REST API exposed by snapd over a Unix domain socket on every Ubuntu system running snaps. Enables local clients and tools to query snap state, install / refresh / remove snaps, manage interf
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
- description: The Assertions API from Canonical — 1 operation(s) for assertions.
  name: Canonical Assertions API
  slug: canonical-assertions-api
- description: The Search API from Canonical — 1 operation(s) for search.
  name: Canonical Search API
  slug: canonical-search-api
- description: The Snaps API from Canonical — 10 operation(s) for snaps.
  name: Canonical Snaps API
  slug: canonical-snaps-api
artifact_total: 21
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
created: '2026-03-16'
description: Canonical is the company behind Ubuntu, the world's most popular open source operating system for cloud, servers, desktops, IoT, and Kubernetes. Canonical publishes a broad set of developer APIs spanning the Ubuntu and Canonical ecosystem — the Snap Store and Snapcraft, the Charmhub charm marketplace, LXD system containers, MAAS bare-metal provisioning, Juju orchestration, Launchpad project hosting, Ubuntu Pro subscription services, and Landscape systems management — most of which are RESTful, open, and well documented.
finops:
- name: Canonical Finops
  service_category: API
  slug: canonical-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/canonical.png
layout: provider
modified: '2026-04-23'
name: Canonical
nav: Providers
network: true
overview: 'Canonical publishes 3 APIs on the [APIs.io](https://apis.io/) network: Assertions API, Search API, and Snaps API. Tagged areas include Cloud, Linux, Open-Source, Ubuntu, and Containers.


  Canonical''s developer surface includes documentation, engineering blog, and 12 more developer resources.'
plans:
- name: Canonical Plans Pricing
  plan_count: 3
  slug: canonical-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 5
  name: Canonical Rate Limits
  slug: canonical-rate-limits
score:
  band: thin
  composite: 31.3
  coverage:
    artifact_dirs: 9
    catalog_gap: 74.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.5
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 44.9
    developer_ergonomics: 35.7
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 31.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/canonical/refs/heads/main/screenshots/canonical-2026-06-20T173927.png
security:
- kind: domain-security
  name: Canonical Domain Security
  slug: canonical-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
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
