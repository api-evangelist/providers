---
aid: kubevirt
name: KubeVirt
description: KubeVirt is a CNCF incubating project that extends Kubernetes to run traditional virtual machines alongside containers. It allows users to create, manage, and run VMs using the same Kubernetes APIs and tools used for containers. KubeVirt is ideal for migrating legacy workloads to Kubernetes without requiring application rewriting.
url: https://kubevirt.io
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Cloud Native
  - Incubating
  - Kubernetes
  - Migration
  - Virtual Machines
  - Virtualization
created: '2026-03-16'
modified: '2026-04-28'
specificationVersion: '0.19'
type: Index
apis:
  - aid: kubevirt:kubevirt-api
    name: KubeVirt VM Management API
    description: KubeVirt extends the Kubernetes API with custom resources for virtual machine management. VirtualMachine resources define VM specifications including CPU, memory, disks, and network interfaces. VirtualMachineInstance tracks running VMs, and VirtualMachineInstanceMigration handles live migrations. The API supports start, stop, pause, migrate, and snapshot operations through standard kubectl commands.
    humanURL: https://kubevirt.io/user-guide/
    properties:
      - type: Documentation
        url: https://kubevirt.io/user-guide/
      - type: Reference
        url: https://kubevirt.io/api-reference/
      - type: OpenAPI
        url: openapi/kubevirt-vm-openapi.yml
      - type: JSONSchema
        url: json-schema/kubevirt-vm-schema.json
    tags:
      - Kubernetes API
      - Live Migration
      - Virtual Machines
  - aid: kubevirt:kubevirt-cdi-api
    name: KubeVirt Containerized Data Importer API
    description: REST API for the Containerized Data Importer (CDI), which provides facilities for importing and cloning virtual machine disk images into PersistentVolumeClaims for use as KubeVirt VM disks. The CDI API includes DataVolume, DataSource, and StorageProfile resources for managing data import pipelines.
    humanURL: https://kubevirt.io/user-guide/storage/containerized_data_importer/
    properties:
      - type: Documentation
        url: https://kubevirt.io/user-guide/storage/containerized_data_importer/
      - type: Reference
        url: https://kubevirt.io/cdi-api-reference/
      - type: GitHubRepository
        url: https://github.com/kubevirt/containerized-data-importer
      - type: OpenAPI
        url: openapi/kubevirt-cdi-openapi.yml
    tags:
      - Data Import
      - Kubernetes
      - PersistentVolumeClaims
      - Storage
      - Virtual Machines
common:
  - type: Website
    url: https://kubevirt.io/
  - type: JSON-LD
    url: json-ld/kubevirt-context.jsonld
  - type: JSONSchema
    url: json-schema/kubevirt-vm-schema.json
  - type: Documentation
    url: https://kubevirt.io/user-guide/
  - type: GitHub Organization
    url: https://github.com/kubevirt
  - type: GitHubRepository
    url: https://github.com/kubevirt/kubevirt
  - type: Blog
    url: https://kubevirt.io/blogs/
  - type: Community
    url: https://github.com/kubevirt/community
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
