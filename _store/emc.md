---
aid: emc
name: EMC
description: EMC Corporation (now Dell EMC, a division of Dell Technologies) provides enterprise storage, data management, and cloud infrastructure solutions. EMC products include VMAX, VNX, Isilon, and ECS storage platforms, as well as data protection and information management solutions. EMC was acquired by Dell Technologies in 2016.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/emc/refs/heads/main/apis.yml
created: '2026-03-24'
modified: '2026-04-18'
specificationVersion: '0.19'
tags:
  - Cloud Infrastructure
  - Data Management
  - Data Protection
  - Enterprise Storage
  - Storage
apis:
  - aid: emc:ecs-management-api
    name: EMC ECS Management REST API
    description: The ECS Management REST API provides programmatic access to manage Dell EMC Elastic Cloud Storage (ECS) object storage platform. It supports namespace management, user management, storage pool configuration, replication groups, bucket management, and monitoring operations.
    humanURL: https://www.dell.com/support/kbdoc/en-us/000020064/ecs-api-documentation
    baseURL: https://ecs.example.com:4443
    tags:
      - Buckets
      - Cloud Storage
      - Namespaces
      - Object Storage
    properties:
      - type: Documentation
        url: https://www.dell.com/support/kbdoc/en-us/000020064/ecs-api-documentation
    contact:
      - type: Support
        url: https://www.dell.com/support/home/en-us
  - aid: emc:unisphere-api
    name: EMC Unisphere REST API
    description: The Unisphere Management REST API provides programmatic access to manage Dell EMC Unity and PowerStore storage arrays. It supports storage resource provisioning, performance monitoring, alert management, and system configuration operations.
    humanURL: https://www.dell.com/support/kbdoc/en-us/000020064/ecs-api-documentation
    baseURL: https://unity.example.com/api
    tags:
      - Enterprise Storage
      - Management
      - Monitoring
      - Storage Arrays
    properties:
      - type: Documentation
        url: https://www.dell.com/support/kbdoc/en-us/000020064/ecs-api-documentation
    contact:
      - type: Support
        url: https://www.dell.com/support/home/en-us
common:
  - type: Documentation
    url: https://www.dell.com/support/kbdoc/en-us/000020064/ecs-api-documentation
  - type: Support
    url: https://www.dell.com/support/home/en-us
  - type: DeveloperPortal
    url: https://developer.dell.com/
  - type: Features
    data:
      - Enterprise-grade object and block storage
      - Multi-protocol support (S3, Swift, Atmos, HDFS)
      - Geo-distributed replication
      - Namespace and tenant management
      - Role-based access control
      - Performance monitoring and alerting
      - Storage pool and provisioning management
  - type: UseCases
    data:
      - Managing enterprise storage infrastructure programmatically
      - Automating storage provisioning for cloud workloads
      - Monitoring storage array health and performance
      - Configuring data protection and replication policies
      - Managing multi-tenant storage environments
  - type: Integrations
    data:
      - VMware vSphere
      - Microsoft Hyper-V
      - Amazon S3
      - OpenStack Swift
      - Hadoop HDFS
      - Kubernetes CSI
      - Ansible
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
