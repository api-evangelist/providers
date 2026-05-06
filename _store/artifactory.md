---
aid: artifactory
name: JFrog Artifactory
description: JFrog Artifactory is a universal artifact repository manager supporting all major package formats and build tools including Maven, Gradle, npm, NuGet, PyPI, Docker, Helm, RubyGems, CocoaPods, and more. As the central hub of the JFrog Platform, Artifactory stores, manages, and distributes binary artifacts across the entire software development lifecycle. It integrates with CI/CD pipelines through native plugins for Jenkins, GitHub Actions, CircleCI, and other tools. Artifactory provides comprehensive REST APIs for managing repositories, artifacts, builds, security, and system configuration programmatically.
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/artifactory/refs/heads/main/apis.yml
created: '2024-01-15'
modified: '2026-04-19'
specificationVersion: '0.19'
type: Index
tags:
  - Artifacts
  - DevOps
  - CI/CD
  - Docker Registry
  - Maven
  - Package Management
  - Repository
apis:
  - aid: artifactory:rest-api
    name: Artifactory REST API
    description: Comprehensive REST API for managing artifacts, repositories, users, groups, permissions, replication, security, and system configuration in JFrog Artifactory.
    humanURL: https://jfrog.com/help/r/jfrog-rest-apis/artifactory-rest-apis
    baseURL: https://artifactory.example.com/artifactory/api
    tags:
      - Artifacts
      - Repositories
      - REST
    properties:
      - type: Documentation
        url: https://jfrog.com/help/r/jfrog-rest-apis/artifactory-rest-apis
      - type: OpenAPI
        url: openapi/artifactory-rest-api-openapi.yml
      - type: Authentication
        url: https://jfrog.com/help/r/jfrog-rest-apis/authentication
      - type: JSONSchema
        url: json-schema/artifactory-repository-configuration.json
      - type: JSONSchema
        url: json-schema/artifactory-file-info.json
      - type: JSONSchema
        url: json-schema/artifactory-permission-target.json
  - aid: artifactory:aql-api
    name: Artifactory Query Language (AQL) API
    description: Advanced search API using a SQL-like query language (AQL) for finding artifacts, builds, modules, and entries based on properties, statistics, and metadata.
    humanURL: https://jfrog.com/help/r/jfrog-artifactory-documentation/artifactory-query-language
    baseURL: https://artifactory.example.com/artifactory/api/search/aql
    tags:
      - AQL
      - Query
      - Search
    properties:
      - type: Documentation
        url: https://jfrog.com/help/r/jfrog-artifactory-documentation/artifactory-query-language
      - type: OpenAPI
        url: openapi/artifactory-aql-api-openapi.yml
      - type: CodeExamples
        url: https://jfrog.com/help/r/jfrog-artifactory-documentation/aql-examples
  - aid: artifactory:docker-registry-api
    name: Artifactory Docker Registry API
    description: Docker Registry v2 API for pushing, pulling, and managing Docker images stored in JFrog Artifactory acting as a Docker registry.
    humanURL: https://jfrog.com/help/r/jfrog-artifactory-documentation/docker-registry
    baseURL: https://artifactory.example.com/artifactory/api/docker
    tags:
      - Docker
      - Containers
      - Registry
    properties:
      - type: Documentation
        url: https://jfrog.com/help/r/jfrog-artifactory-documentation/docker-registry
      - type: OpenAPI
        url: openapi/artifactory-docker-registry-api-openapi.yml
  - aid: artifactory:build-integration-api
    name: Artifactory Build Integration API
    description: API for publishing and managing build information from CI/CD systems, enabling traceability between artifact versions and the builds that produced them.
    humanURL: https://jfrog.com/help/r/jfrog-rest-apis/builds
    baseURL: https://artifactory.example.com/artifactory/api/build
    tags:
      - Builds
      - CI/CD
      - Integration
    properties:
      - type: Documentation
        url: https://jfrog.com/help/r/jfrog-rest-apis/builds
      - type: OpenAPI
        url: openapi/artifactory-build-integration-api-openapi.yml
      - type: JSONSchema
        url: json-schema/artifactory-build-info.json
common:
  - type: TermsOfService
    url: https://jfrog.com/terms-of-service/
    title: Terms of Service
  - type: PrivacyPolicy
    url: https://jfrog.com/privacy-policy/
    title: Privacy Policy
  - type: StatusPage
    url: https://status.jfrog.com/
    title: Status Page
  - type: Pricing
    url: https://jfrog.com/pricing/
    title: Pricing
  - type: Blog
    url: https://jfrog.com/blog/
    title: Blog
  - type: GitHubOrganization
    url: https://github.com/jfrog
    title: JFrog GitHub
  - type: X
    url: https://twitter.com/jfrog
    title: JFrog on X
  - type: Support
    url: https://jfrog.com/support/
    title: Support
  - type: Portal
    url: https://jfrog.com/developers/
    title: Developer Portal
  - type: Documentation
    url: https://jfrog.com/help/
    title: Documentation
  - type: GettingStarted
    url: https://jfrog.com/help/r/jfrog-artifactory-documentation/getting-started-with-artifactory
    title: Getting Started
  - type: SignUp
    url: https://jfrog.com/start-free/
    title: Sign Up Free
  - type: Login
    url: https://my.jfrog.com/login/
    title: Login
  - type: Resources
    url: https://community.jfrog.com/
    title: JFrog Community
  - type: YouTube
    url: https://www.youtube.com/@jfrog
    title: YouTube
  - type: CLI
    url: https://jfrog.com/help/r/jfrog-cli/jfrog-cli
    title: JFrog CLI
  - type: ChangeLog
    url: https://jfrog.com/help/r/jfrog-release-information/jfrog-release-notes
    title: Release Notes
  - type: Features
    data:
      - name: Universal Package Management
        description: Single repository manager supporting 30+ package formats including Maven, npm, NuGet, PyPI, Docker, Helm, Conda, Conan, and more.
      - name: Artifact Metadata and Search
        description: Rich metadata tagging and AQL query language for finding artifacts based on properties, statistics, dates, and custom attributes.
      - name: Build Integration
        description: Native CI/CD integration publishing build information to track which artifacts were produced by which build, enabling full artifact traceability.
      - name: Security and Permissions
        description: Fine-grained permission targets, LDAP/SAML/SSO integration, API key management, and access tokens for secure artifact access control.
      - name: Replication
        description: Push and pull replication across multiple Artifactory instances for geo-distributed teams and disaster recovery.
      - name: Docker Registry
        description: Full Docker Registry v2 API compliance for pushing, pulling, and managing Docker images with automated vulnerability scanning.
  - type: UseCases
    data:
      - name: CI/CD Pipeline Integration
        description: Development teams integrate Artifactory with Jenkins, GitHub Actions, and other CI/CD tools to store, version, and distribute build artifacts.
      - name: Container Registry
        description: Platform engineering teams use Artifactory as an enterprise Docker registry with security scanning, access controls, and promotion workflows.
      - name: Dependency Proxy
        description: Organizations proxy public package registries (npm, PyPI, Maven Central) through Artifactory to cache dependencies, apply security policies, and ensure build reproducibility.
      - name: Release Management
        description: Release engineers promote artifacts through staging environments using build promotion, managing the lifecycle from snapshot to release.
  - type: Integrations
    data:
      - name: Jenkins
        description: Official Jenkins Artifactory Plugin for publishing artifacts and build information from Jenkins pipelines.
      - name: GitHub Actions
        description: JFrog GitHub Actions for integrating Artifactory into GitHub CI/CD workflows.
      - name: JFrog Xray
        description: Deep integration with JFrog Xray for continuous security and compliance scanning of artifacts and dependencies.
      - name: JFrog Pipelines
        description: Native integration with JFrog Pipelines for end-to-end CI/CD orchestration using Artifactory as the artifact store.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
