---
aid: bootc
name: Bootc
description: Bootc is an open source tool that enables transactional, in-place operating system updates using OCI/Docker container images as the source for OS updates. It applies the container layering model to bootable host systems, using standard OCI containers as a transport and delivery format for base operating system updates. The container image includes a Linux kernel, and when deployed the base userspace runs normally with systemd as PID 1. Bootc is a CNCF Sandbox project with a stable CLI and API.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/bootc/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-19'
specificationVersion: '0.19'
tags:
  - CNCF
  - Container Images
  - Infrastructure
  - OCI
  - Open Source
  - Operating Systems
  - System Updates
apis: []
common:
  - type: Website
    url: https://bootc.dev
  - type: Documentation
    url: https://bootc.dev/bootc/
  - type: GitHubRepository
    url: https://github.com/bootc-dev/bootc
  - type: GitHubOrganization
    url: https://github.com/containers/bootc
  - type: Community
    url: https://github.com/bootc-dev/bootc/discussions
  - type: ReleaseNotes
    url: https://github.com/bootc-dev/bootc/releases
  - name: Use Cases
    type: UseCases
    data:
      - name: OS Image Updates
        url: https://bootc.dev/bootc/upgrades.html
        features:
          - Transactional Updates
          - In-Place OS Updates
          - Atomic Upgrades
          - Rollback Support
          - Container-Based Updates
          - OCI Image Updates
      - name: OS Image Installation
        url: https://bootc.dev/bootc/bootc-install.html
        features:
          - Disk Installation
          - Filesystem Installation
          - Container to Disk
          - Day 2 OS Setup
      - name: Container Image Switching
        url: https://bootc.dev/bootc/
        features:
          - Image Reference Switching
          - Distribution Switching
          - Container Registry Tracking
      - name: Immutable Infrastructure
        url: https://bootc.dev/bootc/
        features:
          - Immutable OS
          - Reproducible Systems
          - GitOps for OS
          - Infrastructure as Code
          - Container Native OS
  - name: Features
    type: Features
    data:
      - name: bootc upgrade
        url: https://bootc.dev/bootc/
        features:
          - Pull Latest OCI Image
          - Stage New Deployment
          - Auto-Apply on Reboot
          - Download-Only Mode
          - Update Checking
      - name: bootc switch
        url: https://bootc.dev/bootc/
        features:
          - Change Container Image Reference
          - Switch OS Distribution
          - Change Registry Source
          - Seamless Image Tracking
      - name: bootc status
        url: https://bootc.dev/bootc/
        features:
          - Current Booted Image Display
          - Staged Changes Status
          - JSON Output
          - YAML Output
      - name: bootc rollback
        url: https://bootc.dev/bootc/
        features:
          - Revert to Previous Boot
          - Boot Loader Entry Reordering
          - Safe Rollback
      - name: bootc install
        url: https://bootc.dev/bootc/bootc-install.html
        features:
          - Install to Disk
          - Install to Filesystem
          - Offline Installation
          - Air-Gapped Deployment
      - name: OCI/Docker Compatibility
        url: https://bootc.dev/bootc/
        features:
          - OCI Image Format
          - Docker Image Compatibility
          - Container Registry Support
          - Layered Image Model
          - Linux Kernel in Image
      - name: ostree Integration
        url: https://bootc.dev/bootc/
        features:
          - ostree Backend
          - Atomic Updates
          - Content-Addressed Storage
          - Deployment Management
maintainers:
  - FN: Kin Lane
    email: kinlane@gmail.com
---
