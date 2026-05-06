---
aid: cloudbees
url: https://raw.githubusercontent.com/api-evangelist/cloudbees/refs/heads/main/apis.yml
name: CloudBees
created: '2025-01-08'
modified: '2026-04-23'
type: Index
access: 3rd-Party
position: Consumer
specificationVersion: '0.19'
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
x-type: company
tags:
  - CI/CD
  - Continuous Delivery
  - Continuous Integration
  - DevOps
  - Feature Flags
  - Feature Management
  - Jenkins
  - Release Orchestration
  - Software Delivery
description: CloudBees provides software delivery automation across continuous integration, continuous deployment, release orchestration, and feature management. Their developer surface includes the CloudBees CI REST API (an extension of the Jenkins REST API), the CloudBees CD/RO REST API for release orchestration, the CloudBees Feature Management REST API (formerly Rollout) for feature flags and environments, and the CloudBees Unify Platform API for the modern unified delivery platform. APIs are generally JSON, token-authenticated, and follow REST conventions.
apis:
  - aid: cloudbees:ci
    name: CloudBees CI REST API
    tags:
      - CI/CD
      - Continuous Integration
      - Jenkins
      - Pipelines
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.cloudbees.com
    humanURL: https://docs.cloudbees.com/docs/cloudbees-ci-kb/latest/best-practices/best-practice-for-using-jenkins-rest-api
    properties:
      - url: https://docs.cloudbees.com/docs/cloudbees-ci-kb/latest/best-practices/best-practice-for-using-jenkins-rest-api
        type: Documentation
      - url: https://docs.cloudbees.com/docs/release-notes/latest/cloudbees-ci/
        type: Release Notes
    description: CloudBees CI is a hardened, enterprise distribution of Jenkins. The REST API is the Jenkins remote access API exposed at /api on every controller and on individual jobs, runs, queues and nodes. Callers authenticate with a username and API token in HTTP basic auth and can list/create jobs, trigger builds, fetch build status and console logs, manage credentials, and inspect operations centers. Responses are available as JSON, XML, or Python.
  - aid: cloudbees:cd-ro
    name: CloudBees CD/RO REST API
    tags:
      - Continuous Delivery
      - DevOps
      - Pipelines
      - Release Orchestration
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example-cd.cloudbees.com/rest/v1.0
    humanURL: https://docs.cloudbees.com/docs/cloudbees-cd/latest/api/
    properties:
      - url: https://docs.cloudbees.com/docs/cloudbees-cd/latest/api/
        type: Documentation
      - url: https://docs.cloudbees.com/plugins/cd/ec-jenkins
        type: Jenkins Plugin
    description: The CloudBees CD/RO (Continuous Delivery / Release Orchestration) REST API exposes resources for pipelines, releases, environments, applications, deployments, projects and resources. Operations cover modelling deployment pipelines, launching releases, tracking stages, managing environments and inventories, and integrating with Jenkins and other CI tools.
  - aid: cloudbees:feature-management
    name: CloudBees Feature Management REST API
    tags:
      - Experimentation
      - Feature Flags
      - Feature Management
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://x-api.rollout.io/public-api
    humanURL: https://docs.cloudbees.com/docs/cloudbees-feature-management-rest-api/latest/introduction
    properties:
      - url: https://docs.cloudbees.com/docs/cloudbees-feature-management-rest-api/latest/introduction
        type: Documentation
      - url: https://docs.cloudbees.com/docs/cloudbees-feature-management-rest-api/latest/environments
        type: Environments
      - url: https://docs.cloudbees.com/docs/cloudbees-feature-management/latest/rest-api
        type: Reference
    description: The CloudBees Feature Management REST API (formerly Rollout) provides programmatic access to applications, environments, feature flags, experiments, target groups, audit logs, and users. Authentication uses a bearer token in the Authorization header. The API enforces a one request per second rate limit per IP, returning HTTP 555 when exceeded.
  - aid: cloudbees:unify
    name: CloudBees Unify Platform API
    tags:
      - DevOps
      - Platform
      - Software Delivery
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://docs.cloudbees.com/
    properties:
      - url: https://docs.cloudbees.com/
        type: Documentation
    description: CloudBees Unify is the modern, opinionated software delivery platform that unifies CI, CD, feature management, analytics, and security into a single workflow. The platform exposes APIs for managing organizations, components, workflows, environments, feature flags, and analytics; authentication is via personal access tokens and the surface is the recommended target for new integrations.
  - aid: cloudbees:jenkins-plugin
    name: CloudBees CD/RO Jenkins Plugin Steps
    tags:
      - Continuous Delivery
      - Jenkins
      - Plugin
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.jenkins.io/doc/pipeline/steps/electricflow/
    properties:
      - url: https://www.jenkins.io/doc/pipeline/steps/electricflow/
        type: Documentation
      - url: https://plugins.jenkins.io/electricflow
        type: Plugin
    description: The CloudBees CD plugin for Jenkins exposes Jenkins pipeline steps that call CloudBees CD/RO REST endpoints — triggering pipelines, running releases, deploying applications, and pulling artifacts from Jenkins build outputs into CD/RO release flows.
common:
  - type: Website
    url: https://www.cloudbees.com/
  - type: Documentation
    url: https://docs.cloudbees.com/
  - type: Support
    url: https://support.cloudbees.com/
  - type: Privacy Policy
    url: https://www.cloudbees.com/privacy
  - type: Plugins
    url: https://docs.cloudbees.com/plugins/ci
  - type: JSON-LD
    url: json-ld/cloudbees-context.jsonld
  - type: Spectral
    url: rules/cloudbees-rules.yml
  - type: Naftiko Capabilities
    url: capabilities/feature-management.yaml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
