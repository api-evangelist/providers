---
aid: akita-software
name: Akita Software
description: Akita Software was an API observability and analysis platform that used passive traffic monitoring to automatically map APIs, detect changes, and identify issues without requiring code changes or proxies. Akita was acquired by Postman in November 2023 and its technology has been integrated into the Postman platform as Postman Live Insights. The Akita agent is now available as the open-source Postman Insights Agent.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Acquired
  - API Discovery
  - API Mapping
  - API Observability
  - Traffic Analysis
url: https://raw.githubusercontent.com/api-evangelist/akita-software/refs/heads/main/apis.yml
created: '2025-01-08'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: akita-software:akita-software
    name: Akita Software
    description: Akita Software provided an API observability platform that used passive traffic monitoring to automatically discover, map, and model APIs without requiring code changes or proxying. It could generate API specs from traffic, detect breaking changes, and monitor API performance. Akita was acquired by Postman in November 2023, and its capabilities are now available as Postman Live Insights with the open-source Postman Insights Agent.
    humanURL: https://www.akitasoftware.com
    tags:
      - API Discovery
      - API Mapping
      - API Observability
      - Traffic Analysis
    properties:
      - type: Documentation
        url: https://docs.akita.software
      - type: GitHubOrganization
        url: https://github.com/akitasoftware
      - type: GettingStarted
        url: https://docs.akita.software/docs/getting-started
  - aid: akita-software:postman-live-insights
    name: Postman Live Insights
    description: Postman Live Insights is the successor to Akita Software, now integrated into the Postman platform. The Postman Insights Agent (open source) makes it easy to see the behavior of production APIs, discover API endpoints, and find and fix issues through passive traffic monitoring.
    humanURL: https://www.postman.com/product/live-insights/
    tags:
      - API Discovery
      - API Monitoring
      - API Observability
      - Postman
    properties:
      - type: Documentation
        url: https://learning.postman.com/docs/insights/insights-overview/
      - type: GitHubRepository
        url: https://github.com/postmanlabs/postman-insights-agent
      - type: GettingStarted
        url: https://learning.postman.com/docs/insights/insights-gs/
common:
  - type: Website
    url: https://www.akitasoftware.com
  - type: Documentation
    url: https://docs.akita.software
  - type: GitHubOrganization
    url: https://github.com/akitasoftware
  - type: Blog
    url: https://blog.akita.software
  - type: X
    url: https://twitter.com/akaboraitasoftware
  - type: LinkedIn
    url: https://www.linkedin.com/company/akita-software/
  - type: Features
    data:
      - name: Passive Traffic Monitoring
        description: Monitors API traffic passively without code changes, SDK installation, or proxying, minimizing operational overhead and risk.
      - name: Automatic API Spec Generation
        description: Generates OpenAPI specifications automatically from observed traffic, keeping documentation always up to date.
      - name: Breaking Change Detection
        description: Detects breaking API changes by comparing observed traffic patterns across deployments and branches.
      - name: API Performance Monitoring
        description: Tracks API response times, error rates, and traffic patterns to help identify performance regressions.
      - name: Multi-Platform Integration
        description: Integrates with Docker, Kubernetes, NGINX, Rails, Django, Flask, FastAPI, and Heroku for broad platform coverage.
  - type: UseCases
    data:
      - name: API Documentation Generation
        description: Engineering teams automatically generate and maintain up-to-date API specs from production traffic without manual effort.
      - name: API Change Management
        description: Teams detect unintentional API breaking changes between branches or deployments before they reach production.
      - name: API Discovery
        description: Organizations discover undocumented and shadow APIs by monitoring actual network traffic across their services.
      - name: Production API Monitoring
        description: DevOps teams monitor API behavior and performance in production to quickly identify and diagnose issues.
  - type: Integrations
    data:
      - name: Docker
        description: Docker extension and container integration for traffic monitoring
      - name: Kubernetes
        description: Kubernetes deployment support for monitoring microservice APIs
      - name: NGINX
        description: NGINX module for mirroring API traffic to the Akita agent
      - name: Heroku
        description: Heroku buildpack for integrating Akita with Heroku applications
      - name: Postman
        description: Acquired by Postman in 2023; technology integrated as Postman Live Insights
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
