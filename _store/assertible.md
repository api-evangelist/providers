---
aid: assertible
name: Assertible
description: Assertible provides a reliable first line of defense against web service failures by providing simple and powerful assertions to test and monitor APIs. It enables automated API testing with assertions on response status, headers, body content, and performance, with integrations for CI/CD pipelines and notifications. Assertible supports scheduled API monitoring, deployment testing triggered via webhooks, and team collaboration for API quality assurance workflows. The platform integrates with GitHub, Slack, PagerDuty, and other tools for seamless notification and incident management.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - API Testing
  - Monitoring
  - Quality Assurance
  - Testing
  - CI/CD
created: '2025-01-08'
modified: '2026-04-19'
specificationVersion: '0.19'
url: https://raw.githubusercontent.com/api-evangelist/assertible/refs/heads/main/apis.yml
apis:
  - aid: assertible:assertible-api
    name: Assertible API
    description: The Assertible API enables programmatic management of API tests, test suites, and monitoring configurations for automated quality assurance. It allows triggering test runs, managing webhooks, and accessing test results programmatically for CI/CD integration.
    humanURL: https://assertible.com/
    baseURL: https://api.assertible.com
    tags:
      - API Testing
      - Monitoring
      - Quality Assurance
    properties:
      - type: Documentation
        url: https://assertible.com/docs
      - type: GettingStarted
        url: https://assertible.com/docs/guide/getting-started
      - type: Authentication
        url: https://assertible.com/docs/guide/authentication
common:
  - type: Portal
    url: https://assertible.com/
    title: Assertible Website
  - type: Documentation
    url: https://assertible.com/docs
    title: Documentation
  - type: Blog
    url: https://assertible.com/blog
    title: Blog
  - type: SignUp
    url: https://assertible.com/signup
    title: Sign Up
  - type: Login
    url: https://assertible.com/login
    title: Login
  - type: GitHubOrganization
    url: https://github.com/assertible
    title: Assertible GitHub Organization
  - type: Features
    data:
      - name: API Test Assertions
        description: Define assertions on API response status codes, headers, response body content, JSON Schema compliance, and response time to validate API behavior.
      - name: Scheduled Monitoring
        description: Run API tests on a scheduled basis (hourly, daily, etc.) to continuously monitor production APIs for availability and correctness.
      - name: Deployment Testing
        description: Trigger Assertible test suites automatically after deployments via webhooks, ensuring API quality gates are enforced in CI/CD pipelines.
      - name: JSON Schema Validation
        description: Validate API responses against JSON Schema definitions to ensure response payloads match expected data structures.
      - name: Team Collaboration
        description: Share test suites and API monitoring configurations across teams with role-based access and shared notification channels.
  - type: UseCases
    data:
      - name: Post-Deployment Validation
        description: Development teams trigger Assertible test suites after each deployment to verify APIs are functioning correctly before traffic shifts.
      - name: API Uptime Monitoring
        description: Operations teams use scheduled Assertible tests to monitor API availability and receive alerts when endpoints fail.
      - name: API Contract Testing
        description: QA teams use JSON Schema assertions to validate that API responses match documented contracts and catch breaking changes.
  - type: Integrations
    data:
      - name: GitHub
        description: Integration with GitHub for triggering tests on pull requests and deployment events through GitHub Actions and webhooks.
      - name: Slack
        description: Slack notifications for test failures, alerts, and monitoring events from Assertible test runs.
      - name: PagerDuty
        description: PagerDuty integration for escalating API monitoring failures to on-call teams for incident response.
      - name: CircleCI
        description: Integration with CircleCI pipelines for running Assertible test suites as part of continuous integration workflows.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
