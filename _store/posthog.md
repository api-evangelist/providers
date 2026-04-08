---
aid: posthog
url: https://raw.githubusercontent.com/api-evangelist/posthog/refs/heads/main/apis.yml
apis:
- aid: posthog:capture-api
  name: PostHog Capture API
  description: The PostHog Capture API allows developers to send events, identify users, and set user or group properties from any server or client. It is the primary ingestion endpoint for sending analytics data to PostHog and supports batch event submission, feature flag evaluation, and alias operations for identity resolution.
  humanURL: https://posthog.com/docs/api/capture
  tags:
  - Analytics
  - Events
  - Ingestion
  - Tracking
  properties:
  - type: Documentation
    url: https://posthog.com/docs/api/capture
- aid: posthog:query-api
  name: PostHog Query API
  description: The PostHog Query API provides programmatic access to run HogQL queries against your PostHog data. HogQL is PostHog's SQL-like query language that enables custom analytics queries, funnel analysis, retention analysis, and trend calculations. This API allows developers to build custom dashboards and reporting tools powered by PostHog data.
  humanURL: https://posthog.com/docs/api/query
  tags:
  - Analytics
  - HogQL
  - Queries
  - Reporting
  properties:
  - type: Documentation
    url: https://posthog.com/docs/api/query
- aid: posthog:persons-api
  name: PostHog Persons API
  description: The PostHog Persons API allows developers to retrieve, search, and manage person profiles in PostHog. It supports listing persons with filters, retrieving individual person details, viewing associated events and properties, and managing person data including deletions for privacy compliance.
  humanURL: https://posthog.com/docs/api/persons
  tags:
  - Analytics
  - Identity
  - Profiles
  - Users
  properties:
  - type: Documentation
    url: https://posthog.com/docs/api/persons
- aid: posthog:feature-flags-api
  name: PostHog Feature Flags API
  description: The PostHog Feature Flags API enables developers to create, manage, and evaluate feature flags programmatically. It supports boolean and multivariate flags, percentage-based rollouts, user targeting with property filters, and integration with PostHog's experimentation framework for A/B testing.
  humanURL: https://posthog.com/docs/api/feature-flags
  tags:
  - A/B Testing
  - Experimentation
  - Feature Flags
  - Rollouts
  properties:
  - type: Documentation
    url: https://posthog.com/docs/api/feature-flags
- aid: posthog:experiments-api
  name: PostHog Experiments API
  description: The PostHog Experiments API provides programmatic management of A/B tests and experiments. It supports creating experiments with control and test variants, defining goal metrics, launching and stopping experiments, and retrieving experiment results with statistical significance calculations.
  humanURL: https://posthog.com/docs/api/experiments
  tags:
  - A/B Testing
  - Experimentation
  - Metrics
  - Variants
  properties:
  - type: Documentation
    url: https://posthog.com/docs/api/experiments
- aid: posthog:insights-api
  name: PostHog Insights API
  description: The PostHog Insights API allows developers to create, retrieve, and manage saved insights such as trends, funnels, retention charts, paths, and lifecycle analyses. It provides programmatic access to the same analytics visualizations available in the PostHog UI, enabling integration with external dashboards and automated reporting workflows.
  humanURL: https://posthog.com/docs/api/insights
  tags:
  - Analytics
  - Dashboards
  - Insights
  - Reporting
  properties:
  - type: Documentation
    url: https://posthog.com/docs/api/insights
- aid: posthog:cohorts-api
  name: PostHog Cohorts API
  description: The PostHog Cohorts API enables developers to create and manage cohorts, which are groups of users defined by shared properties or behavioral patterns. Cohorts can be used for targeting feature flags, filtering analytics queries, and segmenting experiment populations.
  humanURL: https://posthog.com/docs/api/cohorts
  tags:
  - Analytics
  - Cohorts
  - Segmentation
  - Users
  properties:
  - type: Documentation
    url: https://posthog.com/docs/api/cohorts
- aid: posthog:annotations-api
  name: PostHog Annotations API
  description: The PostHog Annotations API allows developers to create and manage annotations that mark significant events on PostHog charts and dashboards. Annotations provide context for data changes by recording deployments, marketing campaigns, incidents, and other events that may affect metrics.
  humanURL: https://posthog.com/docs/api/annotations
  tags:
  - Analytics
  - Annotations
  - Charts
  properties:
  - type: Documentation
    url: https://posthog.com/docs/api/annotations
name: PostHog
tags:
- A/B Testing
- Analytics
- Feature Flags
- Open Source
- Product Analytics
- Session Recording
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: PostHog is an open source product analytics platform that provides event tracking, session recording, feature flags, A/B testing, and user surveys in a single platform. It can be self-hosted or used as a cloud service, giving teams full control over their product data while providing comprehensive tools for understanding and improving user experiences.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

