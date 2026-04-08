---
aid: bugsnag
url: https://raw.githubusercontent.com/api-evangelist/bugsnag/refs/heads/main/apis.yml
apis:
- aid: bugsnag:data-access-api
  name: Bugsnag Data Access API
  tags:
  - Analytics
  - Application Stability
  - Data Access
  - Error Monitoring
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.bugsnag.com
  humanURL: https://docs.bugsnag.com/api/data-access/
  properties:
  - url: https://docs.bugsnag.com/api/data-access/
    type: Documentation
  - url: openapi/bugsnag-data-access-openapi.yml
    type: OpenAPI
  description: The Bugsnag Data Access API provides programmatic access to information about your organization, projects, errors, events, and more. It allows developers to build custom integrations and dashboards using their Bugsnag data. The REST API uses JSON and requires authentication via an API token, which can be found in Bugsnag account settings. It supports querying error trends, project configurations, collaborators, and release information.
- aid: bugsnag:error-reporting-api
  name: Bugsnag Error Reporting API
  tags:
  - Error Monitoring
  - Error Reporting
  - Events
  - Notifications
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://notify.bugsnag.com
  humanURL: https://docs.bugsnag.com/api/error-reporting/
  properties:
  - url: https://docs.bugsnag.com/api/error-reporting/
    type: Documentation
  - url: openapi/bugsnag-error-reporting-openapi.yml
    type: OpenAPI
  description: The Bugsnag Error Reporting API allows applications to report error and exception details directly to the Bugsnag dashboard. If there is no official SDK available for your platform, you can use this API to send error payloads manually. The API accepts structured JSON payloads containing exception details, stack traces, device information, and application metadata. It is the underlying mechanism used by all official Bugsnag notifier SDKs to deliver error data.
- aid: bugsnag:session-tracking-api
  name: Bugsnag Session Tracking API
  tags:
  - Application Monitoring
  - Sessions
  - Stability
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://sessions.bugsnag.com
  humanURL: https://docs.bugsnag.com/api/sessions/
  properties:
  - url: https://docs.bugsnag.com/api/sessions/
    type: Documentation
  - url: openapi/bugsnag-session-tracking-openapi.yml
    type: OpenAPI
  description: The Bugsnag Session Tracking API enables applications to report session data, which is used to calculate release stability scores in the Bugsnag dashboard. By tracking when user sessions start and end, Bugsnag can determine crash rates and overall application stability. This API works in conjunction with the Error Reporting API to provide a complete picture of application health. Session data is required for accurate stability metrics and crash-free user percentages.
- aid: bugsnag:build-api
  name: Bugsnag Build API
  tags:
  - Builds
  - CI/CD
  - Deployments
  - Releases
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://build.bugsnag.com
  humanURL: https://docs.bugsnag.com/api/build/
  properties:
  - url: https://docs.bugsnag.com/api/build/
    type: Documentation
  - url: openapi/bugsnag-build-openapi.yml
    type: OpenAPI
  description: The Bugsnag Build API allows you to provide information about your application builds, releases, and deployments. By notifying Bugsnag when you deploy, you can track which releases introduced new errors, view error trends across releases, and identify regressions. The API accepts build metadata including version numbers, source control information, and release stages. It integrates with CI/CD pipelines to automate release tracking.
- aid: bugsnag:trace-api
  name: Bugsnag Trace API
  tags:
  - Observability
  - OpenTelemetry
  - Performance
  - Tracing
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://otlp.bugsnag.com
  humanURL: https://docs.bugsnag.com/api/
  properties:
  - url: https://docs.bugsnag.com/api/
    type: Documentation
  - url: openapi/bugsnag-trace-openapi.yml
    type: OpenAPI
  description: The Bugsnag Trace API allows applications to send OpenTelemetry span data to Bugsnag for performance monitoring and analysis. It enables developers to track request latency, identify slow operations, and monitor application performance alongside error data. The API accepts trace data in the OpenTelemetry format, making it compatible with existing instrumentation libraries and observability tooling. Performance data is displayed in the Bugsnag dashboard alongside error information.
name: Bugsnag
tags:
- API
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Bugsnag is an application stability monitoring platform that helps software teams detect, diagnose, and fix errors in web, mobile, and back-end applications.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

