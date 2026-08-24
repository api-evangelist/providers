---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-24'
api_count: 7
apis:
- description: Cloud compilation and code-signing service for Android and iOS React Native apps. Submits build jobs via eas-cli or programmatic token access, returns build artifacts, and fires BUILD webhooks on comp
  name: EAS Build API
  slug: eas-build-api
- description: Automated upload service that publishes compiled app binaries to the Apple App Store and Google Play Store directly from the cloud. Fires SUBMIT webhooks on completion. Removes manual upload steps and
  name: EAS Submit API
  slug: eas-submit-api
- description: Over-the-air update delivery service that pushes JavaScript bundle fixes directly to end users without requiring a full app store submission. Tracks Monthly Active Users (MAU) and delivers updates via
  name: EAS Update API
  slug: eas-update-api
- description: CI/CD automation service for React Native apps supporting scheduled cron jobs, Slack integration, and automated build and release pipelines. Extends EAS Build and Submit with workflow orchestration. I
  name: EAS Workflows API
  slug: eas-workflows-api
- description: Edge deployment service for Expo Router and React Native web applications, including API routes. Provides 100,000 monthly requests, 1 million CPU-ms, and 1 GB storage on all plans, with global CDN del
  name: EAS Hosting API
  slug: eas-hosting-api
- description: Expo's hosted push notification broker that abstracts Apple APNs and Google FCM into a single REST endpoint. Delivers push messages to iOS and Android devices registered with the Expo Push Token syste
  name: Push Notifications API
  slug: push-notifications-api
- description: Event notification system that delivers HTTP POST payloads to configured endpoints when EAS Build or EAS Submit jobs complete. Payloads are signed with HMAC-SHA1 using a shared secret. Supports expone
  name: EAS Webhooks API
  slug: eas-webhooks-api
artifact_total: 14
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/expo-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/expo-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/expo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://expo.dev
- group: docs
  title: ''
  type: Documentation
  url: https://docs.expo.dev
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/expo
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/expo-dev
- group: company
  title: ''
  type: Blog
  url: https://expo.dev/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://expo.dev/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.expo.dev
- group: other
  title: ''
  type: X
  url: https://x.com/expo
- group: operate
  title: ''
  type: ChangeLog
  url: https://expo.dev/changelog
- group: build
  title: ''
  type: CLI
  url: https://github.com/expo/eas-cli
- group: commercial
  title: ''
  type: Plans
  url: plans/expo-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/expo-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/expo-finops.yml
created: 2026-06-13
description: Expo is a React Native development platform providing cloud infrastructure for building, submitting, updating, and managing mobile apps. Expo Application Services (EAS) delivers REST and CLI-driven APIs for EAS Build (cloud compilation and code signing for Android and iOS), EAS Submit (automated App Store and Google Play submissions), EAS Update (over-the-air JavaScript bundle delivery), EAS Workflows (CI/CD pipelines with cron and Slack integration), EAS Hosting (edge deployment of Expo Router and React Native web apps), EAS Insights (analytics), EAS Observe (performance monitoring), and a Push Notifications broker. All services are accessible programmatically via the eas-cli, Personal Access Tokens, or Robot User tokens, and support webhooks for build and submission events.
finops:
- name: Expo Finops
  service_category: ''
  slug: expo-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/expo.png
jsonld:
- class_count: 11
  name: Expo Context
  property_count: 33
  slug: expo-context
layout: provider
modified: 2026-06-13
name: Expo
nav: Providers
network: true
overview: 'Expo publishes 7 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include React Native, Mobile Development, Build Automation, Over-the-Air Updates, and CI/CD.


  The Expo catalog on APIs.io includes 1 JSON-LD context.


  Expo''s developer surface includes documentation, engineering blog, pricing, changelog, CLI, and 11 more developer resources.'
plans:
- name: Expo Plans Pricing
  plan_count: 4
  slug: expo-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Expo Rate Limits
  slug: expo-rate-limits
score:
  band: thin
  composite: 31.4
  delta: 0.0
  facets:
    access_clarity: 57.9
    commercial_clarity: 57.9
    contract_governance: 0.0
    contract_quality: 15.5
    developer_ergonomics: 19.0
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 31.4
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/expo/refs/heads/main/screenshots/expo-2026-06-20T180939.png
security:
- kind: domain-security
  name: Expo Domain Security
  slug: expo-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Expo Vulnerability Disclosure
  slug: expo-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Expo Trust Center
  slug: expo-trust-center
  summary_line: SOC 2, GDPR
slug: expo
tags:
- React Native
- Mobile Development
- Build Automation
- Over-the-Air Updates
- CI/CD
- App Store Submission
- Push Notifications
- Cloud Build
- Developer Tools
website: https://expo.dev
---
