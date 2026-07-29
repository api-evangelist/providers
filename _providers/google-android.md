---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 46.4
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Google Android Agentic Access
  operation_count: 15
  slug: google-android-agentic-access
  summary_line: 15 operations · 7 acting
api_count: 12
apis:
- description: The Android Device Provisioning Partner API allows device resellers and enterprise mobility management providers to programmatically manage zero-touch enrollment for enterprise Android devices, includ
  name: Android Device Provisioning Partner API
  slug: android-device-provisioning-partner-api
- description: 'The Google Play EMM API enables enterprise mobility management providers to manage the distribution of Android apps and configurations to enterprise users and devices. This API is no longer accepting '
  name: Google Play EMM API
  slug: google-play-emm-api
- description: The Play Integrity API helps protect your apps and games from potentially risky and fraudulent interactions by checking that interactions and server requests are coming from your genuine app binary ru
  name: Play Integrity API
  slug: play-integrity-api
- description: The Cloud Testing API powers Firebase Test Lab, enabling developers to test Android and iOS apps on real and virtual devices hosted in Google data centers, including instrumentation tests and robo tes
  name: Cloud Testing API
  slug: cloud-testing-api
- description: The Android Management API API from Google Android — 2 operation(s) for android management api.
  name: Google Android Android Management API API
  slug: google-android-android-management-api-api
- description: The Device API from Google Android — 1 operation(s) for device.
  name: Google Android Device API
  slug: google-android-device-api
- description: The Devices API from Google Android — 1 operation(s) for devices.
  name: Google Android Devices API
  slug: google-android-devices-api
- description: The EnrollmentTokens API from Google Android — 1 operation(s) for enrollmenttokens.
  name: Google Android EnrollmentTokens API
  slug: google-android-enrollmenttokens-api
- description: The Enterprises API from Google Android — 1 operation(s) for enterprises.
  name: Google Android Enterprises API
  slug: google-android-enterprises-api
- description: The Policies API from Google Android — 1 operation(s) for policies.
  name: Google Android Policies API
  slug: google-android-policies-api
- description: The Policy API from Google Android — 1 operation(s) for policy.
  name: Google Android Policy API
  slug: google-android-policy-api
- description: The WebApps API from Google Android — 1 operation(s) for webapps.
  name: Google Android WebApps API
  slug: google-android-webapps-api
arazzos:
- description: Confirm the target policy exists, mint an enrollment token, then poll the fleet until the new device appears.
  name: Google Android Enroll a Device and Confirm It Checked In
  slug: google-android-device-enrollment-workflow
- description: Inventory the fleet, relinquish ownership of each managed device, then delete the enterprise.
  name: Google Android Offboard an Enterprise
  slug: google-android-enterprise-offboarding-workflow
- description: Bind a signup token to a new enterprise, attach a baseline policy, and mint a first enrollment token.
  name: Google Android Onboard an Enterprise
  slug: google-android-enterprise-onboarding-workflow
- description: Walk enterprises, devices, and policies read-only to produce a fleet inventory an auditor can sign off on.
  name: Google Android Audit an Enterprise Fleet
  slug: google-android-fleet-inventory-audit-workflow
- description: Read the enterprise, patch its Pub/Sub topic and notification types with an updateMask, then read back to confirm.
  name: Google Android Configure Enterprise Pub/Sub Notifications
  slug: google-android-notification-configuration-workflow
- description: Read the current policy, patch a targeted field with an updateMask, then confirm a device actually applied the new version.
  name: Google Android Roll Out a Policy Change and Verify It Applied
  slug: google-android-policy-rollout-workflow
- description: Confirm a device is reachable, issue a LOCK/REBOOT/RESET_PASSWORD command, then poll the device until it reports back.
  name: Google Android Issue a Remote Command and Poll the Device
  slug: google-android-remote-device-command-workflow
- description: Create a hosted web app, confirm it registered, then add it to a policy so it installs on the fleet.
  name: Google Android Publish a Web App and Push It to a Policy
  slug: google-android-web-app-publishing-workflow
artifact_total: 49
collections:
- collection_type: open
  name: Android Management API
  slug: open-google-android
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-android-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-android-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/google-android-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/google-android-scopes.yml
- group: build
  title: ''
  type: Packages
  url: packages/google-android-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/google-android-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/google-android-security.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/google-android-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/google-android-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/google-android-android-management-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/google-android-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/google-android-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/google-android-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/google-android-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/google-android-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/google-android-data-model.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-android-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/google-android-trust-center.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/google-android-enterprise-onboarding-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/google-android-device-enrollment-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/google-android-policy-rollout-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/google-android-remote-device-command-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/google-android-fleet-inventory-audit-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/google-android-web-app-publishing-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/google-android-notification-configuration-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/google-android-enterprise-offboarding-workflow.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/android_by_google
- group: start
  title: ''
  type: Portal
  url: https://developers.android.com/
- group: company
  title: ''
  type: Blog
  url: https://android-developers.googleblog.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/android
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developers.google.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://policies.google.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://developer.android.com/support
- group: company
  title: ''
  type: Newsletter
  url: https://developer.android.com/newsletter
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/android
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/androiddevelopers
- group: operate
  title: ''
  type: Support
  url: https://issuetracker.google.com/issues?q=componentid:192735
- group: learn
  title: ''
  type: Training
  url: https://developer.android.com/courses
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cloud.google.com/
created: '2024-01-01'
description: Android is a mobile operating system developed by Google, based on a modified version of the Linux kernel and other open-source software. It powers billions of devices worldwide including smartphones, tablets, TVs, and wearables.
features:
- description: Remotely manage and configure Android devices with policies for enterprise mobility.
  name: Enterprise Device Management
- description: Publish and manage Android apps on Google Play including in-app purchases and subscriptions.
  name: App Publishing and Distribution
- description: Send cross-platform push notifications to Android devices via Firebase Cloud Messaging.
  name: Push Notifications
- description: Verify that interactions come from genuine app binaries running on genuine Android devices.
  name: Play Integrity
- description: Automate enterprise device provisioning and enrollment at scale.
  name: Zero-Touch Enrollment
- description: Test Android apps on real and virtual devices in Google data centers via Firebase Test Lab.
  name: Cloud Testing
- description: Integrate achievements, leaderboards, and multiplayer features into Android games.
  name: Game Services
- description: Manage system updates and firmware deployments for Android device fleets.
  name: Over-the-Air Updates
finops:
- name: Google Android Finops
  service_category: API
  slug: google-android-finops
image: https://www.android.com/static/images/logos/android-logo.png
integrations:
- description: Integrate with Firebase for analytics, crashlytics, authentication, and cloud messaging.
  name: Firebase
- description: Connect Android apps to Google Cloud services for storage, ML, and compute.
  name: Google Cloud
- description: Manage app releases, testing tracks, and performance metrics through the Play Console.
  name: Google Play Console
- description: Develop and debug Android apps with the official IDE and its integrated tools.
  name: Android Studio
- description: Use Android Jetpack libraries for architecture, UI, and behavior best practices.
  name: Jetpack Libraries
layout: provider
mcp_servers:
- description: ''
  name: google-android-mcp.yml
  slug: google-android-mcpyml
modified: '2026-06-20'
name: Google Android
nav: Providers
network: true
overview: 'Google Android publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Android Management API API, Device API, Devices API, and 5 more. Tagged areas include Android, Google, Mobile Development, Mobile Operating System, and Open Source.


  Google Android''s developer surface includes authentication, changelog, developer portal, engineering blog, support, Stack Overflow tag, YouTube channel, and 32 more developer resources.'
plans:
- name: Google Android Plans Pricing
  plan_count: 3
  slug: google-android-plans-pricing
random_paper: 76
rate_limits:
- limit_count: 5
  name: Google Android Rate Limits
  slug: google-android-rate-limits
scopes:
- name: Google Android Scopes
  scope_count: 9
  slug: google-android-scopes
  summary_line: 9 scopes
score:
  band: developing
  composite: 51.6
  delta: -0.2
  facets:
    commercial_clarity: 68.4
    contract_quality: 51.0
    developer_ergonomics: 28.3
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 68.4
  previous_composite: 51.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-android/refs/heads/main/screenshots/google-android-2026-06-20T182012.png
security:
- kind: authentication
  name: Google Android Authentication
  slug: google-android-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Google Android Domain Security
  slug: google-android-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Android Vulnerability Disclosure
  slug: google-android-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Google Android Trust Center
  slug: google-android-trust-center
  summary_line: SOC 2, SOC 3, ISO 27001, ISO 27017, ISO 27018, ISO 27701, PCI DSS, HIPAA, FedRAMP, CSA STAR, GDPR
slug: google-android
tags:
- Android
- Google
- Mobile Development
- Mobile Operating System
- Open Source
use_cases:
- description: Deploy and manage corporate Android devices with security policies and app distribution.
  name: Enterprise Mobility Management
- description: Automate app publishing, pricing, and subscription management on Google Play.
  name: App Store Management
- description: Drive user engagement with push notifications, in-app messages, and game achievements.
  name: User Engagement
- description: Manage large fleets of Android devices for retail, logistics, or field operations.
  name: Device Fleet Management
- description: Automate testing of Android apps across device configurations using Cloud Testing.
  name: App Quality Assurance
website: https://developers.android.com/
---
