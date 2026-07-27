---
access_model:
  confidence: high
  label: Enterprise · Partner/approval onboarding · No public API
  onboarding: approval
  pricing: enterprise
  public: false
  source:
  - website
  - legal
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 0.0
  scored_at: '2026-07-27'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/commure-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/commure-llms.txt
- group: company
  title: ''
  type: Website
  url: https://commure.com/
- group: other
  title: ''
  type: Company
  url: https://commure.com/company
- group: company
  title: ''
  type: Blog
  url: https://commure.com/blog
- group: company
  title: ''
  type: News
  url: https://commure.com/news
- group: company
  title: ''
  type: Partners
  url: https://commure.com/partners
- group: operate
  title: ''
  type: Support
  url: https://commure.com/contact
- group: operate
  title: ''
  type: StatusPage
  url: https://status.commure.com
- group: auth
  title: ''
  type: TrustCenter
  url: https://commure.com/trust-center
- group: auth
  title: ''
  type: Compliance
  url: https://commure.com/trust-center
- group: commercial
  title: ''
  type: TermsOfService
  url: https://commure.com/legal/general-terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://commure.com/legal/privacy-policy
- group: commercial
  title: ''
  type: DeveloperUserAgreement
  url: https://commure.com/legal/developer-user-agreement
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/commure
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/commure
created: '2026-07-24'
description: Commure is a San Francisco-based AI-native healthcare technology company that operates an integrated clinical and operational platform for United States health systems following its 2023 combination with Athelas. Its products span Ambient AI clinical documentation (Scribe/Dictation), end-to-end Revenue Cycle Management (RCM), Call Center Agents, referral Orchestrator, patient Engage coordination, Commure Pro clinical intelligence, Strongline staff-safety alerting, and Athelas Home point-of-care diagnostics, integrating with 60+ EHRs across 130+ health systems processing over $25B in annual claims. Commure launched a FHIR-native open developer platform in 2020, but that public developer portal (developer.commure.com) is no longer live; today the API surface is a gated, partner-only offering governed by a Developer User Agreement (Sandbox Environment + Developer Services), with no self-serve public API documentation, FHIR CapabilityStatement, or downloadable OpenAPI currently
  published. Home market is the United States.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-24'
name: Commure
nav: Providers
network: true
overview: 'Commure is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare, United States, Clinical AI, Ambient AI, and Revenue Cycle Management.


  Commure''s developer surface includes engineering blog, product news, support, and 13 more developer resources.'
random_paper: 12
score:
  band: emerging
  composite: 21.6
  delta: 0.0
  facets:
    commercial_clarity: 36.8
    contract_quality: 0.0
    developer_ergonomics: 6.5
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 21.6
  regulatory:
    applies: true
    regime: Health
    regime_id: health
    score: 41.3
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/commure/refs/heads/main/screenshots/commure-2026-07-25T210143.png
security:
- kind: domain-security
  name: Commure Domain Security
  slug: commure-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Commure Trust Center
  slug: commure-trust-center
  summary_line: SOC 2 Type II, HIPAA, HITECH Act, CCPA
slug: commure
tags:
- Healthcare
- United States
- Clinical AI
- Ambient AI
- Revenue Cycle Management
- FHIR
- Interoperability
- EHR
- Remote Monitoring
- Health System
website: https://commure.com/
---
