---
aid: canonical
name: Canonical
url: https://raw.githubusercontent.com/api-evangelist/canonical/refs/heads/main/apis.yml
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
type: Index
tags:
  - Cloud
  - Linux
  - Open Source
  - Ubuntu
  - Containers
  - Bare Metal
  - Charms
  - Identity
access: Open
created: '2026-03-16'
modified: '2026-04-23'
position: Provider
specificationVersion: '0.19'
description: Canonical is the company behind Ubuntu, the world's most popular open source operating system for cloud, servers, desktops, IoT, and Kubernetes. Canonical publishes a broad set of developer APIs spanning the Ubuntu and Canonical ecosystem — the Snap Store and Snapcraft, the Charmhub charm marketplace, LXD system containers, MAAS bare-metal provisioning, Juju orchestration, Launchpad project hosting, Ubuntu Pro subscription services, and Landscape systems management — most of which are RESTful, open, and well documented.
apis:
  - aid: canonical:snap-store-api
    name: Snap Store API
    description: The public Snap Store Device API (api.snapcraft.io) serves information about snaps, revisions, channels, tracks, assertions, and refresh state to snap clients. The Snapcraft Dashboard API (dashboard.snapcraft.io) lets snap publishers manage releases, brand stores, and snap metadata programmatically.
    humanURL: https://api.snapcraft.io/docs/
    baseURL: https://api.snapcraft.io
    tags:
      - Snaps
      - Store
      - Packaging
    properties:
      - type: Documentation
        url: https://api.snapcraft.io/docs/
      - type: DashboardAPI
        url: https://dashboard.snapcraft.io/docs/reference/v2/en/index.html
      - type: HowTo
        url: https://snapcraft.io/docs/using-the-api
  - aid: canonical:charmhub-api
    name: Charmhub API
    description: Developer-facing REST API for Charmhub, Canonical's marketplace for charms (Kubernetes and machine operators). Supports charm discovery, publishing, release channels, and token exchange — macaroons issued by dashboard.snapcraft.io SSO are exchanged for Charmhub developer tokens used in the Authorization header.
    humanURL: https://api.charmhub.io/docs/default.html
    baseURL: https://api.charmhub.io
    tags:
      - Charms
      - Operators
      - Kubernetes
    properties:
      - type: Documentation
        url: https://api.charmhub.io/docs/default.html
      - type: Portal
        url: https://charmhub.io/
  - aid: canonical:snapd-rest-api
    name: snapd REST API
    description: The local REST API exposed by snapd over a Unix domain socket on every Ubuntu system running snaps. Enables local clients and tools to query snap state, install / refresh / remove snaps, manage interfaces and connections, and read system information.
    humanURL: https://snapcraft.io/docs/reference/development/snapd-rest-api/
    tags:
      - Local
      - System
      - Snaps
    properties:
      - type: Documentation
        url: https://snapcraft.io/docs/reference/development/snapd-rest-api/
      - type: HowTo
        url: https://snapcraft.io/docs/how-to-guides/snap-development/use-the-rest-api/
  - aid: canonical:lxd-api
    name: LXD REST API
    description: The REST API exposed by LXD, Canonical's system-container and VM manager. All client–daemon communication happens over HTTPS (remote) or a Unix socket (local). Provides endpoints for instances, images, networks, storage pools, profiles, projects, cluster members, and events. Fully documented in an auto-generated OpenAPI (Swagger) spec.
    humanURL: https://documentation.ubuntu.com/lxd/latest/rest-api/
    baseURL: https://<host>:8443/1.0
    tags:
      - Containers
      - Virtualisation
      - OpenAPI
    properties:
      - type: Documentation
        url: https://documentation.ubuntu.com/lxd/latest/rest-api/
      - type: OpenAPI
        url: https://github.com/canonical/lxd/blob/main/doc/rest-api.yaml
      - type: Reference
        url: https://linuxcontainers.org/lxd/rest-api/
  - aid: canonical:maas-api
    name: MAAS API
    description: The RESTful API for MAAS (Metal as a Service). Everything the MAAS UI can do — commissioning, allocation, deployment, DHCP/DNS, tags, zones, pools, users, machines — is available through the API, making bare- metal infrastructure programmable and suitable for Infrastructure as Code workflows. Python and CLI bindings are provided.
    humanURL: https://canonical.com/maas/docs/api
    baseURL: https://<maas-host>/MAAS/api/2.0
    tags:
      - Bare Metal
      - Provisioning
      - Infrastructure
    properties:
      - type: Documentation
        url: https://canonical.com/maas/docs/api
      - type: Overview
        url: https://canonical.com/maas
      - type: Portal
        url: https://maas.io/docs
  - aid: canonical:juju-api
    name: Juju Client / Controller API
    description: Juju is Canonical's open-source orchestration engine for deploying, integrating, scaling, and managing applications on clouds, MAAS, LXD, and Kubernetes via charms. Juju clients communicate with a controller over a websocket-based API; Python and Go libraries plus the juju CLI consume this API.
    humanURL: https://documentation.ubuntu.com/juju/
    tags:
      - Orchestration
      - DevOps
      - Charms
    properties:
      - type: Documentation
        url: https://documentation.ubuntu.com/juju/
      - type: Overview
        url: https://canonical.com/juju
      - type: Architecture
        url: https://canonical.com/juju/juju-architecture
  - aid: canonical:launchpad-api
    name: Launchpad Web Services API
    description: Launchpad exposes a RESTful Web Services API over its project hosting, bug tracking, code, builds, translations, and distribution data. The API is authenticated with OAuth; anonymous access gives read-only access to public data. The launchpadlib Python library is the officially supported client.
    humanURL: https://documentation.ubuntu.com/launchpad/user/how-to/launchpad-api/
    baseURL: https://api.launchpad.net/
    tags:
      - OAuth
      - Open Source
      - Project Hosting
    properties:
      - type: Documentation
        url: https://documentation.ubuntu.com/launchpad/user/how-to/launchpad-api/
      - type: Reference
        url: https://help.launchpad.net/API
      - type: ClientLibrary
        url: https://launchpadlib.readthedocs.io/en/latest/introduction.html
      - type: Portal
        url: https://api.launchpad.net/
  - aid: canonical:ubuntu-pro-api
    name: Ubuntu Pro Client API
    description: The Ubuntu Pro client exposes a local API/CLI for managing Ubuntu Pro subscription services on a host — enabling, disabling, and inspecting Extended Security Maintenance (ESM), Livepatch, FIPS, compliance tooling (CIS, DISA-STIG), USG, and Landscape integration.
    humanURL: https://documentation.ubuntu.com/pro/
    tags:
      - ESM
      - Livepatch
      - FIPS
      - Compliance
      - Subscription
    properties:
      - type: Documentation
        url: https://documentation.ubuntu.com/pro/
      - type: ClientDocs
        url: https://documentation.ubuntu.com/pro-client/en/latest/
      - type: Portal
        url: https://ubuntu.com/pro
  - aid: canonical:landscape-api
    name: Landscape API
    description: Canonical Landscape is the systems-management platform for Ubuntu at scale. Its API lets operators manage and automate inventories, upgrades, patch compliance, reboots, scripts, monitoring, and alerts across fleets of Ubuntu machines (on-prem, hybrid, or hosted Landscape SaaS).
    humanURL: https://ubuntu.com/landscape/docs
    tags:
      - Systems Management
      - Patch Management
      - Fleet
    properties:
      - type: Documentation
        url: https://ubuntu.com/landscape/docs
      - type: Portal
        url: https://ubuntu.com/landscape
common:
  - type: Website
    url: https://canonical.com/
  - type: UbuntuWebsite
    url: https://ubuntu.com/
  - type: Documentation
    url: https://documentation.ubuntu.com/
  - type: GitHubOrg
    url: https://github.com/canonical
  - type: SnapStore
    url: https://snapcraft.io/
  - type: Charmhub
    url: https://charmhub.io/
  - type: Launchpad
    url: https://launchpad.net/
  - type: DiscourseForum
    url: https://discourse.ubuntu.com/
  - type: DataPrivacy
    url: https://ubuntu.com/legal/data-privacy
  - type: TermsOfService
    url: https://ubuntu.com/legal/terms
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
