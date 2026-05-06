---
aid: openstack
name: OpenStack
description: Open source cloud computing platform for building and managing public and private clouds, providing infrastructure as a service (IaaS) through a set of interrelated services including Compute (Nova), Object Storage (Swift), Block Storage (Cinder), Networking (Neutron), Identity (Keystone), Image (Glance), Orchestration (Heat), Database (Trove), DNS (Designate), and Load Balancer (Octavia). Each service exposes its own REST API; clients authenticate against Keystone and use the returned service catalog to discover per-region endpoints for the remaining services.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Cloud Platform
  - Infrastructure as a Service
  - Open Source
  - Virtualization
  - Linux Foundation
created: '2025-01-01'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/openstack/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: openstack:keystone
    name: OpenStack Identity (Keystone) API
    description: Keystone is the OpenStack Identity service that provides authentication, authorization, and a service catalog for an OpenStack cloud. Tokens issued by Keystone are required to call any other OpenStack service API. The v3 API exposes endpoints for tokens, users, groups, projects, domains, roles, role assignments, services, endpoints, and the service catalog.
    humanURL: https://docs.openstack.org/api-ref/identity/v3/
    baseURL: https://{keystone-host}:5000/v3
    tags:
      - Identity
      - Authentication
      - Authorization
      - Service Catalog
    properties:
      - type: Documentation
        url: https://docs.openstack.org/api-ref/identity/v3/
      - type: Documentation
        url: https://docs.openstack.org/keystone/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/openstack/refs/heads/main/openapi/openstack-keystone-openapi.yml
      - type: JSONLDContext
        url: https://raw.githubusercontent.com/api-evangelist/openstack/refs/heads/main/json-ld/openstack-context.jsonld
  - aid: openstack:nova
    name: OpenStack Compute (Nova) API
    description: Nova is the OpenStack Compute service that manages the lifecycle of compute instances (virtual machines, bare-metal, containers). The API exposes endpoints for servers, flavors, images, key pairs, security groups, attached volumes, and lifecycle actions such as start, stop, reboot, resize, rebuild, and snapshot.
    humanURL: https://docs.openstack.org/api-ref/compute/
    baseURL: https://{nova-host}/compute/v2.1
    tags:
      - Compute
      - Virtual Machines
      - Bare Metal
    properties:
      - type: Documentation
        url: https://docs.openstack.org/api-ref/compute/
      - type: Documentation
        url: https://docs.openstack.org/nova/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/openstack/refs/heads/main/openapi/openstack-nova-openapi.yml
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/openstack/refs/heads/main/json-schema/openstack-server-schema.json
      - type: JSONLDContext
        url: https://raw.githubusercontent.com/api-evangelist/openstack/refs/heads/main/json-ld/openstack-context.jsonld
  - aid: openstack:neutron
    name: OpenStack Networking (Neutron) API
    description: Neutron provides networking as a service, exposing endpoints for networks, subnets, ports, routers, floating IPs, security groups, load balancers, firewalls, and VPN-as-a-Service.
    humanURL: https://docs.openstack.org/api-ref/network/
    baseURL: https://{neutron-host}/networking/v2.0
    tags:
      - Networking
      - SDN
      - Security Groups
    properties:
      - type: Documentation
        url: https://docs.openstack.org/api-ref/network/
      - type: Documentation
        url: https://docs.openstack.org/neutron/
  - aid: openstack:cinder
    name: OpenStack Block Storage (Cinder) API
    description: Cinder provides persistent block-level storage volumes that can be attached to Nova instances. The v3 API exposes endpoints for volumes, snapshots, backups, volume types, attachments, transfers, and quotas.
    humanURL: https://docs.openstack.org/api-ref/block-storage/
    baseURL: https://{cinder-host}/volume/v3
    tags:
      - Block Storage
      - Volumes
      - Snapshots
    properties:
      - type: Documentation
        url: https://docs.openstack.org/api-ref/block-storage/
      - type: Documentation
        url: https://docs.openstack.org/cinder/
  - aid: openstack:swift
    name: OpenStack Object Storage (Swift) API
    description: Swift is the OpenStack object storage service. The API exposes endpoints for accounts, containers, and objects with eventual- consistency replication, large-object support, and configurable access controls.
    humanURL: https://docs.openstack.org/api-ref/object-store/
    baseURL: https://{swift-host}/v1/AUTH_{tenant_id}
    tags:
      - Object Storage
      - Containers
      - Replication
    properties:
      - type: Documentation
        url: https://docs.openstack.org/api-ref/object-store/
      - type: Documentation
        url: https://docs.openstack.org/swift/
  - aid: openstack:glance
    name: OpenStack Image (Glance) API
    description: Glance manages disk and server images. The v2 API exposes endpoints for images, image members, image tags, image data upload/download, tasks, schemas, and metadata definitions.
    humanURL: https://docs.openstack.org/api-ref/image/
    baseURL: https://{glance-host}/image/v2
    tags:
      - Images
      - Disk Images
    properties:
      - type: Documentation
        url: https://docs.openstack.org/api-ref/image/
      - type: Documentation
        url: https://docs.openstack.org/glance/
  - aid: openstack:heat
    name: OpenStack Orchestration (Heat) API
    description: Heat is the OpenStack orchestration service that manages infrastructure-as-code deployments via HOT (Heat Orchestration Template) and AWS CloudFormation-compatible templates. The API exposes endpoints for stacks, resources, events, software configs, and template validation.
    humanURL: https://docs.openstack.org/api-ref/orchestration/
    baseURL: https://{heat-host}/heat-api/v1
    tags:
      - Orchestration
      - Infrastructure as Code
    properties:
      - type: Documentation
        url: https://docs.openstack.org/api-ref/orchestration/
      - type: Documentation
        url: https://docs.openstack.org/heat/
  - aid: openstack:octavia
    name: OpenStack Load Balancer (Octavia) API
    description: Octavia provides Load Balancing as a Service. The v2 API exposes endpoints for load balancers, listeners, pools, members, health monitors, L7 policies and rules, and TLS containers.
    humanURL: https://docs.openstack.org/api-ref/load-balancer/
    baseURL: https://{octavia-host}/load-balancer/v2
    tags:
      - Load Balancer
      - LBaaS
    properties:
      - type: Documentation
        url: https://docs.openstack.org/api-ref/load-balancer/
      - type: Documentation
        url: https://docs.openstack.org/octavia/
  - aid: openstack:designate
    name: OpenStack DNS (Designate) API
    description: Designate is the OpenStack DNS-as-a-Service. The v2 API exposes endpoints for zones, recordsets, pools, transfers, and TSIG keys.
    humanURL: https://docs.openstack.org/api-ref/dns/
    baseURL: https://{designate-host}/dns/v2
    tags:
      - DNS
      - DNSaaS
    properties:
      - type: Documentation
        url: https://docs.openstack.org/api-ref/dns/
      - type: Documentation
        url: https://docs.openstack.org/designate/
  - aid: openstack:trove
    name: OpenStack Database (Trove) API
    description: Trove is the OpenStack Database-as-a-Service that provisions and manages database instances (MySQL, PostgreSQL, MongoDB, Redis, MariaDB, Cassandra, etc.) on top of OpenStack.
    humanURL: https://docs.openstack.org/api-ref/database/
    baseURL: https://{trove-host}/database/v1.0
    tags:
      - Database
      - DBaaS
    properties:
      - type: Documentation
        url: https://docs.openstack.org/api-ref/database/
      - type: Documentation
        url: https://docs.openstack.org/trove/
common:
  - url: https://www.openstack.org/
    name: OpenStack
    type: Website
  - url: https://docs.openstack.org/
    name: Documentation Portal
    type: Portal
  - url: https://docs.openstack.org/api-ref/
    name: API Reference
    type: Documentation
  - url: https://docs.openstack.org/api-quick-start/
    name: API Quick Start
    type: GettingStarted
  - url: https://www.openstack.org/community/
    name: Community
    type: Community
  - url: https://www.openstack.org/blog/
    name: Blog
    type: Blog
  - url: https://github.com/openstack
    name: GitHub Organization
    type: GitHubOrganization
  - url: https://opendev.org/openstack
    name: OpenDev Source
    type: SourceCode
  - url: https://www.openstack.org/legal/
    name: Legal
    type: TermsOfService
  - url: https://www.apache.org/licenses/LICENSE-2.0
    name: Apache 2.0 License
    type: License
  - url: https://www.openstack.org/foundation/
    name: Open Infrastructure Foundation
    type: Organization
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
