---
aid: buildah
name: Buildah
description: Buildah is an open-source, Linux-based command-line tool for building OCI-compliant container images without requiring a full container runtime or daemon. It allows building images from scratch or using Dockerfiles, with fine-grained control over image layers. Buildah supports rootless builds in unprivileged environments and integrates seamlessly with Podman and Skopeo as part of the containers organization. It is commonly used in Kubernetes-based CI/CD pipelines to avoid Docker-in-Docker complexity.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/buildah/refs/heads/main/apis.yml
created: '2026-03-26'
modified: '2026-04-21'
specificationVersion: '0.19'
tags:
  - Build Tools
  - CI/CD
  - Container Images
  - Containers
  - Daemonless
  - OCI
  - Open Source
  - Rootless
apis: []
common:
  - type: Website
    url: https://buildah.io
  - type: Documentation
    url: https://github.com/containers/buildah/tree/main/docs
  - type: GettingStarted
    url: https://github.com/containers/buildah/blob/main/docs/tutorials/01-intro.md
  - type: GitHubRepository
    url: https://github.com/containers/buildah
  - type: GitHubOrganization
    url: https://github.com/containers
  - type: Blog
    url: https://buildah.io/blogs/
  - type: ReleaseNotes
    url: https://buildah.io/releases
  - type: MailingList
    url: https://buildah.io/mailinglist
  - type: Tutorials
    url: https://github.com/containers/buildah/tree/main/docs/tutorials
  - type: InstallGuide
    url: https://github.com/containers/buildah/blob/main/install.md
  - name: Use Cases
    type: UseCases
    data:
      - name: Daemonless Container Image Building
        url: https://github.com/containers/buildah/blob/main/docs/tutorials/01-intro.md
        features:
          - No Docker Daemon Required
          - No Root Privileges Required
          - OCI-Compliant Images
          - Dockerfile Support
          - Scratch-Based Builds
          - Layer-by-Layer Construction
      - name: Kubernetes CI/CD Integration
        url: https://github.com/containers/buildah/tree/main/docs/tutorials
        features:
          - Docker-in-Docker Alternative
          - Kubernetes Native Building
          - Unprivileged Container Builds
          - Pipeline Integration
          - Reproducible Builds
      - name: Container Image Analysis and Promotion
        url: https://github.com/containers/buildah/tree/main/docs
        features:
          - Image Layer Inspection
          - Image Mounting
          - Layer Manipulation
          - Multi-Stage Builds
          - Image Squashing
      - name: Package and Artifact Building
        url: https://buildah.io/blogs/
        features:
          - Debian Package Building
          - RPM Building
          - Ruby on Rails Container Images
          - Custom Base Images
          - Minimal Image Creation
  - name: Features
    type: Features
    data:
      - name: buildah build
        url: https://github.com/containers/buildah/tree/main/docs
        features:
          - Dockerfile Build
          - Containerfile Support
          - Multi-Stage Build Support
          - Build Arguments
          - Label and Annotation Support
          - Cache Layers
      - name: buildah from / buildah run
        url: https://github.com/containers/buildah/tree/main/docs
        features:
          - Start from Base Image
          - Run Commands in Container
          - Mount Volumes
          - Set Environment Variables
          - User and Working Directory Config
      - name: buildah commit
        url: https://github.com/containers/buildah/tree/main/docs
        features:
          - Commit Container to Image
          - OCI Format Output
          - Docker Format Output
          - Image Squashing
      - name: Rootless Builds
        url: https://github.com/containers/buildah/blob/main/docs/tutorials/01-intro.md
        features:
          - Unprivileged User Builds
          - User Namespace Support
          - Secure Build Environments
          - CI/CD Security Posture
      - name: Registry Integration
        url: https://github.com/containers/buildah/tree/main/docs
        features:
          - Push to Docker Hub
          - Push to Quay.io
          - Push to Private Registries
          - Pull from OCI Registries
          - Authentication Support
      - name: Podman and Skopeo Integration
        url: https://github.com/containers
        features:
          - Shared Image Storage with Podman
          - Compatible with Skopeo
          - containers/storage Backend
          - containers/image Library
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
