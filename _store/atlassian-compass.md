---
aid: atlassian-compass
name: Atlassian Compass
description: |
  Atlassian Compass is a developer experience platform that helps engineering teams understand, manage, and improve the health of their software components and services. It provides a centralized catalog of software components with scorecards, metrics, dependency tracking, and event ingestion to improve developer productivity and software quality. Compass exposes a GraphQL API for querying and mutating component data and a REST Operations API for integrations.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Atlassian
  - Component Management
  - Developer Experience
  - Software Catalog
  - GraphQL
url: https://raw.githubusercontent.com/api-evangelist/atlassian-compass/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: atlassian-compass:atlassian-compass-graphql-api
    name: Atlassian Compass GraphQL API
    description: |
      The Compass GraphQL API enables programmatic management of software components, scorecards, metrics, relationships, custom fields, and event ingestion within the Compass developer experience platform using OAuth 2.0 authentication.
    humanURL: https://developer.atlassian.com/cloud/compass/graphql/
    baseURL: https://api.atlassian.com/graphql
    tags:
      - Components
      - Developer Experience
      - GraphQL
      - Software Catalog
    properties:
      - type: Documentation
        url: https://developer.atlassian.com/cloud/compass/graphql/
      - type: Authentication
        url: https://developer.atlassian.com/cloud/compass/getting-started/
      - type: GettingStarted
        url: https://developer.atlassian.com/cloud/compass/getting-started/
  - aid: atlassian-compass:atlassian-compass-rest-api
    name: Atlassian Compass REST API
    description: |
      The Compass REST API v1 provides operations for component management, scorecard configuration, and webhook registration via standard HTTP REST conventions with OAuth 2.0 authentication.
    humanURL: https://developer.atlassian.com/cloud/compass/rest/
    baseURL: https://api.atlassian.com/compass/v1
    tags:
      - Components
      - Developer Experience
      - REST
      - Software Catalog
    properties:
      - type: Documentation
        url: https://developer.atlassian.com/cloud/compass/rest/
      - type: Authentication
        url: https://developer.atlassian.com/cloud/compass/getting-started/
common:
  - type: Website
    url: https://www.atlassian.com/software/compass
  - type: Portal
    url: https://developer.atlassian.com/cloud/compass/
  - type: Documentation
    url: https://developer.atlassian.com/cloud/compass/
  - type: GettingStarted
    url: https://developer.atlassian.com/cloud/compass/getting-started/
  - type: Authentication
    url: https://developer.atlassian.com/cloud/compass/getting-started/
  - type: SignUp
    url: https://www.atlassian.com/software/compass
  - type: GitHubOrganization
    url: https://github.com/atlassian
  - type: StatusPage
    url: https://status.atlassian.com/
  - type: Support
    url: https://support.atlassian.com/
  - type: Community
    url: https://community.atlassian.com/
  - type: TermsOfService
    url: https://www.atlassian.com/legal/cloud-terms-of-service
  - type: PrivacyPolicy
    url: https://www.atlassian.com/legal/privacy-policy
  - type: Pricing
    url: https://www.atlassian.com/software/compass/pricing
  - type: Blog
    url: https://www.atlassian.com/blog/
  - type: ReleaseNotes
    url: https://developer.atlassian.com/cloud/compass/changelog/
  - type: Features
    data:
      - name: Component Catalog
        description: Central catalog of all software components with metadata, ownership, and lifecycle tracking across teams.
      - name: Scorecards
        description: Configurable scorecards that evaluate components against engineering standards and best practices to measure health.
      - name: Event Ingestion
        description: Ingest build, deployment, incident, and vulnerability events from CI/CD pipelines and monitoring tools via webhooks and REST.
      - name: Dependency Tracking
        description: Track relationships and dependencies between software components to understand blast radius and system topology.
      - name: Custom Fields
        description: Extend component metadata with custom text, number, boolean, and user fields to capture team-specific data.
      - name: Forge Integration
        description: Build custom Compass apps using the Atlassian Forge platform with the GraphQL toolkit for deep platform integration.
  - type: UseCases
    data:
      - name: Software Catalog Management
        description: Register and track all microservices, libraries, and software components with ownership and lifecycle metadata.
      - name: Engineering Health Monitoring
        description: Create scorecards to measure and improve engineering standards like on-call coverage, documentation, and security posture.
      - name: DORA Metrics Tracking
        description: Ingest deployment and incident events to track DORA metrics including deployment frequency and change failure rate.
      - name: Dependency Mapping
        description: Map dependencies between services to identify coupling, blast radius, and architectural debt.
      - name: Developer Portal Integration
        description: Integrate Compass with internal developer portals and CI/CD pipelines for automated component registration and event tracking.
  - type: Integrations
    data:
      - name: Jira
        description: Native integration with Jira for linking components to project tracking and incident management workflows.
      - name: Bitbucket
        description: Connect Bitbucket repositories to Compass components for automated code health and deployment event tracking.
      - name: GitHub
        description: Integrate GitHub repositories and GitHub Actions CI/CD pipelines with Compass component events.
      - name: PagerDuty
        description: Ingest PagerDuty incident events into Compass for on-call and incident tracking scorecard criteria.
      - name: Datadog
        description: Connect Datadog monitoring data and deployment events to Compass component metrics.
      - name: Terraform
        description: Manage Compass resources via the Atlassian Operations Terraform provider for infrastructure-as-code workflows.
  - type: Solutions
    data:
      - name: Developer Experience Platform
        description: Provide engineering teams with a centralized platform to understand, manage, and improve the health of their software systems.
      - name: Platform Engineering
        description: Enable platform engineering teams to enforce standards, track compliance, and improve developer productivity at scale.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
