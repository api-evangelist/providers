---
aid: beeceptor
name: Beeceptor
url: https://raw.githubusercontent.com/api-evangelist/beeceptor/refs/heads/main/apis.yml
created: '2025-01-08'
modified: '2026-05-04'
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
position: Consumer
specificationVersion: '0.19'
description: Beeceptor is an API mocking, HTTP debugging, and proxy platform that lets developers create mock servers instantly without any coding. It supports REST, SOAP, GraphQL, and gRPC mocking, provides real-time HTTP traffic inspection, webhook testing, local tunneling, and AI-powered spec generation. Teams use Beeceptor to unblock frontend, backend, and QA workflows by simulating APIs before they are built or while avoiding dependencies on live services.
tags:
  - API Mocking
  - Automation
  - Debugging
  - HTTP Proxy
  - Integrations
  - Mock Servers
  - Platform
  - Testing
  - Webhooks
apis:
  - aid: beeceptor:beeceptor
    name: Beeceptor API
    tags:
      - API Mocking
      - HTTP Proxy
      - Mock Servers
      - Testing
    humanURL: https://beeceptor.com/
    description: Beeceptor's management API provides programmatic access to create and manage mock endpoints, rules, and traffic inspection on Scale and Enterprise plans. It enables teams to automate mock server provisioning, configure request matching rules, and integrate Beeceptor into CI/CD pipelines.
    properties:
      - type: Documentation
        url: https://beeceptor.com/docs/
      - type: APIReference
        url: https://beeceptor.com/docs/
      - type: GettingStarted
        url: https://beeceptor.com/docs/
common:
  - type: Website
    url: https://beeceptor.com
  - type: Portal
    url: https://app.beeceptor.com
  - type: Pricing
    url: https://beeceptor.com/pricing/
  - type: FAQ
    url: https://beeceptor.com/faq/
  - type: Blog
    url: https://beeceptor.com/blog/
  - type: StatusPage
    url: https://beeceptorstatus.statuspage.io
  - type: PrivacyPolicy
    url: https://beeceptor.com/privacy-policy/
  - type: TermsOfService
    url: https://beeceptor.com/terms-of-service/
  - type: GitHubOrganization
    url: https://github.com/beeceptor
  - type: Features
    data:
      - 'Beeceptor: free public API'
      - Free for personal mock APIs (1 endpoint, 50 requests/day). Paid plans from $10/mo.
      - 'Public URL: https://beeceptor.com/'
    sources:
      - https://beeceptor.com/pricing/
    updated: '2026-05-04'
  - type: Plans
    data:
      - name: Free Plan
        description: Forever-free plan with 50 requests per day per endpoint, 3 mock rules, public endpoints, flexible request matching, fault injection, live inspection, traffic recording, and CORS support. No signup or credit card required.
      - name: Individual Plan
        description: $10 per month. 15,000 requests per month per endpoint, up to 50 mock rules, private endpoints, AI-powered spec generation, and persistent local tunneling.
      - name: Team Plan
        description: $25 per month. 100,000 requests per month per endpoint, up to 250 mock rules, private endpoints, mTLS, custom domains, and forward proxy support.
      - name: Scale Plan
        description: $99 per month with metered overage at $40 per additional 1M requests. 1M+ requests per month per endpoint, up to 500 mock rules, API control for programmatic management, audit logs, and API contract drift detection.
      - name: Enterprise Plan
        description: Custom pricing. Unlimited usage, SSO integration, observability integrations, on-premises deployment, dedicated support, IP whitelisting, and SOC 2 Type II compliance.
  - type: UseCases
    data:
      - name: Frontend Development
        description: Build and test frontend applications against mock APIs without waiting for backend APIs to be ready, removing cross-team blocking dependencies.
      - name: Backend Development
        description: Mock downstream microservices and third-party APIs to test API behavior under various conditions including timeouts and error states.
      - name: Mobile Development
        description: Access mock servers to enable parallel mobile development without backend dependencies, accelerating the mobile app development cycle.
      - name: QA Engineering
        description: Simulate edge cases, rate limits, latencies, and rarely reachable code paths to achieve comprehensive test coverage without live API dependencies.
      - name: Webhook Testing
        description: Inspect and debug HTTP payloads for webhook consumers and producers from platforms like Shopify, Stripe, and Sendgrid using local tunneling.
      - name: Load Testing
        description: Mimic external service behavior for predictable load test outcomes and reduce costs associated with third-party API usage during performance testing.
      - name: API Contract Sharing
        description: Collaborate with teammates by sharing intercepted requests and mock servers via permanent links for distributed team workflows.
  - type: Integrations
    data:
      - name: Shopify
        description: Inspect and debug Shopify webhook payloads by tunneling webhook deliveries through Beeceptor for local development and testing.
      - name: Stripe
        description: Test Stripe webhook events and payment API callbacks using Beeceptor local tunneling and traffic inspection.
      - name: Sendgrid
        description: Debug email delivery webhook callbacks and event notifications from Sendgrid using Beeceptor HTTP inspection and mock responses.
      - name: CI/CD Pipelines
        description: Integrate Beeceptor programmatic API (Scale plan and above) into CI/CD pipelines to automate mock provisioning and teardown during testing.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
