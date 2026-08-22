---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-19'
api_count: 5
apis:
- description: Register and manage the exams (assessments) that will be proctored - exam name, proctoring type (automated, live, audit), duration, allowed resources, rules, and the launch URL handed back to the LMS.
  name: Examity Exams API
  slug: examity-exams-api
- description: Create, reschedule, and cancel proctoring appointments for a test-taker against a registered exam, and query available proctor slots for live proctoring. Modeled from Examity's partner integration and
  name: Examity Appointments (Scheduling) API
  slug: examity-appointments-api
- description: Launch and track a proctoring session - authenticate the test-taker, start the monitored exam session, and check live session status. Modeled from the LMS launch and monitoring flow; endpoints are not
  name: Examity Sessions API
  slug: examity-sessions-api
- description: Retrieve session outcomes after a proctored exam - completion status, integrity/violation flags, proctor notes, review verdicts, and links to recorded session evidence, so the calling platform can pos
  name: Examity Results & Flags API
  slug: examity-results-flags-api
- description: 'Provision and manage the people involved in proctoring - test-takers, instructors, and administrators - including profile details used for identity verification. In practice most user context arrives '
  name: Examity Users API
  slug: examity-users-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/examity-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.examity.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/examity
- group: commercial
  title: ''
  type: Plans
  url: plans/examity-plans-pricing.yml
- group: other
  title: ''
  type: Email
  url: mailto:developers@examity.com
created: '2026-07-05'
description: Examity is an online exam proctoring and test integrity platform used by universities, certification bodies, and enterprises to authenticate test-takers and monitor online assessments. It offers automated (AI/ML) proctoring, live proctoring, audit-based review, and ID verification, and integrates with learning management systems (Canvas, Blackboard, D2L Brightspace, Moodle, Sakai, Schoology, and others). Examity's programmatic surface is a partner/LMS integration - single sign-on via IMS LTI (consumer key plus shared secret) and a partner integration REST API that platform vendors use to register exams, schedule proctoring appointments, launch sessions, and retrieve completion status and integrity flags. Access is gated - there is no public self-service developer portal, and integration keys plus the integration manual are provided on request via developers@examity.com. Because no endpoints are publicly documented, the APIs below are modeled from the known integration model
  rather than a published reference.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/examity.png
layout: provider
modified: '2026-07-05'
name: Examity
nav: Providers
network: true
overview: Examity publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Proctoring, Exam Integrity, Online Assessment, EdTech, and LMS Integration.
plans:
- name: Examity Plans Pricing
  plan_count: 0
  slug: examity-plans-pricing
random_paper: 13
score:
  band: minimal
  composite: 4.0
  delta: -2.5
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 11.1
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: domain-security
  name: Examity Domain Security
  slug: examity-domain-security
  summary_line: TLSv1.3 · DMARC
slug: examity
tags:
- Proctoring
- Exam Integrity
- Online Assessment
- EdTech
- LMS Integration
- Identity Verification
- Test Security
website: https://www.examity.com
---
