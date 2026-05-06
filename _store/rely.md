---
aid: rely
name: Rely.io
description: Rely.io is an internal developer portal that aggregates engineering data, provides software catalogs with blueprints and entities, engineering scorecards, self-service developer actions, and workflow automation for platform engineering teams. The platform integrates with CI/CD pipelines, incident management, observability, and cloud providers to create a centralized service catalog with real-time data. Rely.io's Public REST API provides full CRUD access to blueprints, entities, scorecards, self-service actions, and automations using Bearer token authentication.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Developer Experience
  - Internal Developer Portal
  - Platform Engineering
  - Software Catalog
  - Service Catalog
  - Engineering Scorecards
url: https://raw.githubusercontent.com/api-evangelist/rely/refs/heads/main/apis.yml
created: '2026-03-27'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: rely:public-api
    name: Rely.io Public API
    description: Full CRUD REST API for managing blueprints, entities, scorecards, self-service actions, and automations in the Rely.io internal developer portal. Authentication uses a long-lived Bearer API key.
    humanURL: https://docs.rely.io/public-api
    baseURL: https://api.rely.io
    tags:
      - Developer Experience
      - Internal Developer Portal
      - Platform Engineering
      - Software Catalog
      - Scorecards
      - Self-Service Actions
    properties:
      - type: Documentation
        url: https://docs.rely.io/public-api
      - type: OpenAPI
        url: openapi/rely-openapi.yml
      - type: Getting Started
        url: https://docs.rely.io/getting-started
common:
  - type: Website
    url: https://www.rely.io
  - type: Documentation
    url: https://docs.rely.io
  - type: GitHub Organization
    url: https://github.com/Rely-io
  - type: GitHub SDK
    url: https://github.com/Rely-io/galaxy-oss
  - type: Sign Up
    url: https://app.rely.io/register
  - type: Demo
    url: https://demo.rely.io
  - type: Support
    url: mailto:support@rely.io
  - type: LinkedIn
    url: https://www.linkedin.com/company/rely-io
features:
  - name: Software Catalog
    description: Centralized service catalog powered by blueprints and entities tracking ownership, dependencies, documentation, and deployments.
  - name: Engineering Scorecards
    description: Define and track production readiness, DORA metrics, and observability standards across all services with automated scoring.
  - name: Self-Service Actions
    description: Enable developers to scaffold services, provision cloud resources, and trigger deployments via UI or API without platform team involvement.
  - name: Automation Workflows
    description: Create automation rules that respond to catalog changes and trigger actions in integrated tools automatically.
  - name: Plugin Integrations
    description: Galaxy-based plugin framework for connecting to GitHub, GitLab, PagerDuty, Datadog, AWS, and other tools via self-hosted or managed agents.
  - name: GitOps Support
    description: Manage blueprints, entities, scorecards, and actions as code in Git repositories for version-controlled portal configuration.
solutions:
  - name: Platform Engineering Portal
    description: Build an internal developer portal that gives developers self-service access to infrastructure and eliminates toil from platform engineering teams.
  - name: Service Ownership Tracking
    description: Track service ownership, runbooks, SLOs, and dependencies in a centralized catalog updated automatically via CI/CD integrations.
  - name: Engineering Standards Enforcement
    description: Define and enforce engineering standards via scorecards with leaderboards that drive adoption across engineering teams.
  - name: Developer Onboarding Automation
    description: Automate new service scaffolding, repository creation, and tool provisioning via self-service actions tied to golden path templates.
useCases:
  - name: Service Catalog Management
    description: Aggregate services, libraries, infrastructure resources, and teams into a searchable catalog with real-time data from CI/CD and observability tools.
  - name: Production Readiness Scoring
    description: Score services on production readiness criteria (on-call coverage, SLO definitions, runbooks, deployment frequency) and track improvement.
  - name: Self-Service Provisioning
    description: Allow developers to provision cloud infrastructure, create repositories, and onboard new services without opening platform team tickets.
integrations:
  - name: GitHub Integration
    description: Sync repositories, workflows, and deployment data to the catalog
  - name: GitLab Integration
    description: Sync GitLab projects, pipelines, and deployment visibility
  - name: PagerDuty Integration
    description: Surface on-call rotations and incident data in service catalog
  - name: Datadog Integration
    description: Pull monitoring metrics and SLO data into service scorecards
  - name: AWS Integration
    description: Track cloud resources and infrastructure entities in the catalog
  - name: Kubernetes Integration
    description: Discover and catalog Kubernetes workloads and deployments
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
