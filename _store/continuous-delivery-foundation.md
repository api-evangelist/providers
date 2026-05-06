---
aid: continuous-delivery-foundation
name: Continuous Delivery Foundation
description: The Continuous Delivery Foundation (CDF) is a Linux Foundation project that hosts vendor-neutral open source projects for continuous integration, continuous delivery, and DevOps. It is the home of CDEvents, Jenkins, Spinnaker, Screwdriver, Ortelius, JayeX, and was previously the home of Tekton (now a CNCF graduated project) and other CD-focused tooling.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Automation
  - CI/CD
  - DevOps
  - Linux Foundation
  - Open Source
created: '2026-03-16'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/continuous-delivery-foundation/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: continuous-delivery-foundation:cdevents
    name: CDEvents Specification
    description: CDEvents is a common specification for Continuous Delivery events that enables interoperability across CI/CD systems. It extends the CloudEvents specification and defines event vocabularies for source code control, continuous integration, testing, continuous deployment, continuous operations, and core lifecycle events. The specification is maintained at github.com/cdevents/spec.
    humanURL: https://cdevents.dev/
    tags:
      - CDEvents
      - CI/CD
      - CloudEvents
      - Events
      - Specification
    properties:
      - type: Documentation
        url: https://cdevents.dev/docs/
      - type: Specification
        url: https://github.com/cdevents/spec
      - type: GitHubOrg
        url: https://github.com/cdevents
      - type: Community
        url: https://cdevents.dev/community/
  - aid: continuous-delivery-foundation:jenkins
    name: Jenkins
    description: Jenkins is the leading open source automation server, providing hundreds of plugins for building, deploying, and automating software projects. Jenkins exposes a remote access REST API that supports XML, JSON, and Python representations and is the de facto standard automation engine for many organizations.
    humanURL: https://www.jenkins.io/
    tags:
      - Automation
      - CI/CD
      - Jenkins
      - Pipelines
      - REST
    properties:
      - type: Documentation
        url: https://www.jenkins.io/doc/
      - type: APIDocumentation
        url: https://www.jenkins.io/doc/book/using/remote-access-api/
      - type: GettingStarted
        url: https://www.jenkins.io/doc/pipeline/tour/getting-started/
      - type: GitHubOrg
        url: https://github.com/jenkinsci
  - aid: continuous-delivery-foundation:spinnaker
    name: Spinnaker
    description: Spinnaker is an open-source, multi-cloud continuous delivery platform originally built at Netflix and Google for releasing software changes with high velocity and confidence. Spinnaker exposes a Gate REST API that drives pipelines, applications, and deployment workflows across AWS, GCP, Azure, Kubernetes, and other cloud targets.
    humanURL: https://spinnaker.io/
    tags:
      - CD
      - Cloud
      - Deployment
      - Multi-cloud
      - Spinnaker
    properties:
      - type: Documentation
        url: https://spinnaker.io/docs/
      - type: APIDocumentation
        url: https://spinnaker.io/docs/reference/api/
      - type: Community
        url: https://spinnaker.io/docs/community/
      - type: GitHubOrg
        url: https://github.com/spinnaker
  - aid: continuous-delivery-foundation:screwdriver
    name: Screwdriver
    description: Screwdriver is an open-source build platform designed for Continuous Delivery, originally built at Yahoo. It provides a REST API for managing pipelines, builds, jobs, and webhooks and is designed to coordinate complex CD workflows across multiple repositories.
    humanURL: https://screwdriver.cd/
    tags:
      - Build
      - CD
      - CI/CD
      - Pipelines
      - Screwdriver
    properties:
      - type: Documentation
        url: https://docs.screwdriver.cd/
      - type: APIDocumentation
        url: https://docs.screwdriver.cd/api/
      - type: GettingStarted
        url: https://docs.screwdriver.cd/user-guide/quickstart
      - type: GitHubOrg
        url: https://github.com/screwdriver-cd
  - aid: continuous-delivery-foundation:ortelius
    name: Ortelius
    description: Ortelius is an open source supply chain evidence store that aggregates continuous security intelligence across the software delivery lifecycle. It exposes APIs for tracking microservice components, SBOMs, vulnerabilities, and deployment evidence so platform teams can answer where any component is running and what is in it.
    humanURL: https://ortelius.io/
    tags:
      - Evidence Store
      - SBOM
      - Supply Chain
      - Security
    properties:
      - type: Documentation
        url: https://docs.ortelius.io/
      - type: GettingStarted
        url: https://docs.ortelius.io/guides/
      - type: GitHubOrg
        url: https://github.com/ortelius
  - aid: continuous-delivery-foundation:jayex
    name: JayeX
    description: JayeX is a customizable cloud developer tool suite hosted by the Continuous Delivery Foundation that provides built-in CI/CD capabilities and developer self-service tooling for cloud-native teams.
    humanURL: https://jayex.io/
    tags:
      - CI/CD
      - Cloud Native
      - Developer Tools
      - Platform
    properties:
      - type: Documentation
        url: https://jayex.io/v3/
      - type: Community
        url: https://jayex.io/community/
  - aid: continuous-delivery-foundation:tekton
    name: Tekton
    description: Tekton is a Kubernetes-native open source framework for creating CI/CD systems. It defines Custom Resource Definitions for Pipelines, Tasks, PipelineRuns, and TaskRuns and was originally hosted at the CDF before moving to the Cloud Native Computing Foundation (CNCF). It is included here for historical context with the CDF ecosystem.
    humanURL: https://tekton.dev/
    tags:
      - CI/CD
      - Kubernetes
      - Pipelines
      - Tekton
    properties:
      - type: Documentation
        url: https://tekton.dev/docs/
      - type: APIDocumentation
        url: https://tekton.dev/docs/pipelines/api/
      - type: GitHubOrg
        url: https://github.com/tektoncd
common:
  - type: Website
    url: https://cd.foundation/
  - type: Projects
    url: https://cd.foundation/projects/
  - type: Documentation
    url: https://cd.foundation/projects/
  - type: Blog
    url: https://cd.foundation/blog/
  - type: Newsroom
    url: https://cd.foundation/news/
  - type: GitHubOrg
    url: https://github.com/cdfoundation
  - type: Community
    url: https://cd.foundation/community/
  - type: Events
    url: https://cd.foundation/events/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
