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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Silverpop Agentic Access
  operation_count: 17
  slug: silverpop-agentic-access
  summary_line: 17 operations · 7 acting
api_count: 6
apis:
- description: OAuth 2.0 token management
  name: Silverpop Authentication API
  slug: silverpop-authentication-api
- description: Email campaign management
  name: Silverpop Campaigns API
  slug: silverpop-campaigns-api
- description: Contact (recipient) list management
  name: Silverpop Contacts API
  slug: silverpop-contacts-api
- description: Marketing automation program management
  name: Silverpop Programs API
  slug: silverpop-programs-api
- description: Campaign reporting and analytics
  name: Silverpop Reports API
  slug: silverpop-reports-api
- description: Transactional email and SMS messaging
  name: Silverpop Transactional API
  slug: silverpop-transactional-api
artifact_total: 19
collections:
- collection_type: open
  name: Silverpop Engage API (Acoustic Campaign)
  slug: open-silverpop
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/silverpop-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/silverpop-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/silverpop-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/silverpop-systems-inc
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Silverpop
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.goacoustic.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.goacoustic.com/acoustic-campaign/reference/overview
- group: auth
  title: ''
  type: Authentication
  url: https://developer.goacoustic.com/acoustic-campaign/docs/authentication
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.goacoustic.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.goacoustic.com/privacy-notice
created: '2026-05-02'
description: Silverpop (now Acoustic, formerly IBM Watson Campaign Automation) is a digital marketing automation platform offering email marketing, marketing automation, mobile messaging, and campaign management. The platform provides XML and REST APIs for list management, contact data, campaign execution, transactional messaging, and reporting.
examples:
- key_count: 4
  name: Silverpop Add Contact Example
  slug: silverpop-add-contact-example
finops:
- name: Silverpop Finops
  service_category: API
  slug: silverpop-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/silverpop.png
json_schemas:
- name: Silverpop Contact
  property_count: 8
  slug: silverpop-contact
json_structures:
- name: Silverpop Contact Structure
  property_count: 0
  slug: silverpop-contact-structure
jsonld:
- class_count: 25
  name: Silverpop Context
  property_count: 4
  slug: silverpop-context
layout: provider
modified: '2026-05-02'
name: Silverpop
nav: Providers
network: true
overview: 'Silverpop publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Campaigns API, Contacts API, and 3 more. Tagged areas include Email Marketing, Marketing Automation, Campaign Management, and Digital Marketing.


  The Silverpop catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Silverpop''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Silverpop Plans Pricing
  plan_count: 3
  slug: silverpop-plans-pricing
random_paper: 72
rate_limits:
- limit_count: 5
  name: Silverpop Rate Limits
  slug: silverpop-rate-limits
rules:
- name: Silverpop API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: silverpop-jsonschema-spectral-rules
- name: Silverpop API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 6
  slug: silverpop-rules
score:
  band: developing
  composite: 52.3
  delta: -3.9
  facets:
    commercial_clarity: 60.5
    contract_quality: 65.3
    developer_ergonomics: 28.3
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 36.8
  previous_composite: 56.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/silverpop/refs/heads/main/screenshots/silverpop-2026-06-20T193920.png
security:
- kind: authentication
  name: Silverpop Authentication
  slug: silverpop-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Silverpop Domain Security
  slug: silverpop-domain-security
  summary_line: TLSv1.3 · HSTS
slug: silverpop
tags:
- Email Marketing
- Marketing Automation
- Campaign Management
- Digital Marketing
website: https://developer.goacoustic.com
---
