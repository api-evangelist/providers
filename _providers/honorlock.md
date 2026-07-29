---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-07-28'
api_count: 6
apis:
- description: Generate the integration and user authentication tokens that authorize an assessment platform to provision and drive Honorlock proctoring on behalf of an institution. Endpoints are modeled from Honorl
  name: Honorlock Authentication API
  slug: honorlock-authentication-api
- description: 'Create and list the users (students, instructors, administrators) that participate in proctored exams. Part of the API-driven enablement flow that mirrors what LTI 1.3 provisions automatically inside '
  name: Honorlock Users API
  slug: honorlock-users-api
- description: 'Create and manage the courses that group exams and enrolled users when an assessment platform integrates directly rather than through an LMS. Endpoints are modeled from Honorlock''s public integration '
  name: Honorlock Courses API
  slug: honorlock-courses-api
- description: Create and configure proctored exams - the settings that determine which integrity controls (ID verification, browser guard, recording, room scan, live pop-in, Search and Destroy) apply to an assessme
  name: Honorlock Exams API
  slug: honorlock-exams-api
- description: Drive the exam-taker lifecycle - set up a session, verify that the test taker has completed the authentication steps (Verify Authentication), begin the proctored attempt, and close it out (End Exam Se
  name: Honorlock Exam Sessions API
  slug: honorlock-exam-sessions-api
- description: Browser-side Integration SDK and Elements UI components that embed the Honorlock exam-taker experience into a custom assessment platform - browser extension verification, pre-exam authentication and r
  name: Honorlock Elements & Integration SDK
  slug: honorlock-elements-sdk
artifact_total: 8
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/honorlock-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/honorlock-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/honorlock
- group: company
  title: ''
  type: Website
  url: https://honorlock.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.honorlock.com
- group: docs
  title: ''
  type: Documentation
  url: https://honorlock.com/custom-integrations/
- group: docs
  title: ''
  type: Documentation
  url: https://honorlock.com/integrations/
created: '2026-07-05'
description: Honorlock is an online exam proctoring and academic integrity platform for higher education and professional certification. Its primary integration path is LTI 1.3, installed natively into LMS platforms - Canvas, Blackboard, Moodle, D2L Brightspace, Open LMS, Docebo, and Intellum - plus publisher platforms such as Pearson, McGraw Hill, and ALEKS via LMS workflows. For assessment platforms that need to embed proctoring outside an LMS, Honorlock offers a partner developer toolkit ("APIs and Elements") documented at docs.honorlock.com - a REST API for provisioning users, courses, exams, authentication tokens, and exam sessions, plus a browser-based Elements/Integration SDK that drives the exam-taker experience (extension verification, session setup, begin/end session). The developer program is sales-gated (contact-sales onboarding); Honorlock does not publish a self-service API key flow, an OpenAPI description, or a public base URL.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/honorlock.png
layout: provider
modified: '2026-07-05'
name: Honorlock
nav: Providers
network: true
overview: 'Honorlock publishes 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Proctoring, Online Proctoring, Academic Integrity, Assessment, and EdTech.


  Honorlock''s developer surface includes documentation and 6 more developer resources.'
random_paper: 51
score:
  band: minimal
  composite: 9.8
  delta: -2.3
  facets:
    commercial_clarity: 7.9
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 12.1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/honorlock/refs/heads/main/screenshots/honorlock-2026-07-25T221411.png
security:
- kind: domain-security
  name: Honorlock Domain Security
  slug: honorlock-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Honorlock Trust Center
  slug: honorlock-trust-center
  summary_line: SOC 2
slug: honorlock
tags:
- Proctoring
- Online Proctoring
- Academic Integrity
- Assessment
- EdTech
- LTI
- Exams
- Education
website: https://honorlock.com
---
