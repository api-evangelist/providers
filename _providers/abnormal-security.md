---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
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
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: The Abnormal Security Platform REST API at api.abnormalplatform.com gives customers and integration partners programmatic access to detected threats, attack cases, abuse mailbox submissions, account t
  name: Abnormal Security Platform API
  slug: abnormal-security-api
artifact_total: 30
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/abnormal-security-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/abnormal-security-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/abnormal-security
- group: company
  title: ''
  type: Website
  url: https://abnormal.ai/
- group: start
  title: Abnormal Security Customer Portal
  type: Portal
  url: https://portal.abnormalsecurity.com
- group: docs
  title: ''
  type: Documentation
  url: https://abnormal.ai/products
- group: company
  title: ''
  type: Blog
  url: https://abnormal.ai/blog
- group: other
  title: ''
  type: Resources
  url: https://abnormal.ai/resources
- group: operate
  title: ''
  type: ContactSales
  url: https://abnormal.ai/contact
- group: company
  title: ''
  type: Careers
  url: https://abnormal.ai/careers
- group: company
  title: ''
  type: Partners
  url: https://abnormal.ai/partners
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://abnormal.ai/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://abnormal.ai/terms
created: '2026-05-23'
description: Abnormal Security (operating under the abnormal.ai brand) is an AI-native email and SaaS security platform that uses behavioral AI to model normal communication and identity behavior, then detect socially engineered email attacks, business email compromise, vendor email compromise, and account takeovers across Microsoft 365, Google Workspace, Slack, Zoom, and Microsoft Teams. The Behavior Platform is paired with AI Security Agents (AI Security Mailbox, AI Phishing Coach, AI Data Analyst) and exposes a gated REST API at api.abnormalplatform.com for SOC, SIEM, SOAR, and ticketing integrations. 4,500+ customers including 25% of the Fortune 500; named a 2024 Gartner Magic Quadrant Leader for Email Security Platforms.
features:
- description: AI-native platform that models normal email and identity behavior to detect socially engineered attacks
  name: Behavior Platform
- description: Autonomous AI defense against phishing, BEC, vendor email compromise, and other inbound email attacks
  name: Inbound Email Security
- description: Detection and mitigation of account takeovers across email and identity platforms
  name: Account Takeover Protection
- description: Detection of Microsoft 365 misconfigurations before attackers can exploit them
  name: Security Posture Management
- description: Personalized graymail filtering to reduce inbox noise without compromising security
  name: Email Productivity
- description: Detect and prevent emails sent to the wrong recipient before data is exposed
  name: Misdirected Email Prevention
- description: AI agent that responds to user-reported emails and coaches users at superhuman speed
  name: AI Security Mailbox
- description: Hyper-personalized security training that reduces phishing susceptibility
  name: AI Phishing Coach
- description: Natural-language security reporting that produces board-ready insights
  name: AI Data Analyst
- description: Account takeover protection for SaaS applications such as Slack and Zoom
  name: SaaS Account Takeover Protection
- description: Detection of malicious content inside Microsoft Teams
  name: Messaging Security
finops:
- name: Abnormal Security Finops
  service_category: API
  slug: abnormal-security-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/abnormal-security.png
integrations:
- description: Native API-based integration with Microsoft 365 for email and identity protection
  name: Microsoft 365
- description: Native API-based integration with Google Workspace email and identity surfaces
  name: Google Workspace
- description: Messaging security integration with Microsoft Teams
  name: Microsoft Teams
- description: SaaS account takeover protection for Slack workspaces
  name: Slack
- description: SaaS account takeover protection for Zoom accounts
  name: Zoom
- description: REST API forwarding of detected threats and cases into Splunk, Sentinel, Chronicle, and similar SIEMs
  name: SIEM
- description: Bidirectional integrations with Cortex XSOAR, Splunk SOAR, Tines, and other SOAR platforms
  name: SOAR
- description: Ticketing integrations with ServiceNow, Jira, and other ITSM tools
  name: ITSM
layout: provider
modified: '2026-05-23'
name: Abnormal Security
nav: Providers
network: true
overview: 'Abnormal Security publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Cybersecurity, Email Security, Account Takeover, Behavioral AI, and SaaS Security.


  Abnormal Security''s developer surface includes developer portal, documentation, engineering blog, and 10 more developer resources.'
plans:
- name: Abnormal Security Plans Pricing
  plan_count: 1
  slug: abnormal-security-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 2
  name: Abnormal Security Rate Limits
  slug: abnormal-security-rate-limits
score:
  band: emerging
  composite: 23.4
  coverage:
    artifact_dirs: 6
    catalog_earned: 56.0
    catalog_earned_first_party: 0.0
    catalog_gap: 59.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 23.4
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/abnormal-security/refs/heads/main/screenshots/abnormal-security-2026-06-20T163301.png
security:
- kind: domain-security
  name: Abnormal Security Domain Security
  slug: abnormal-security-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Abnormal Security Trust Center
  slug: abnormal-security-trust-center
  summary_line: SOC 2, ISO 27001, FedRAMP, GDPR, CSA STAR
slug: abnormal-security
tags:
- Cybersecurity
- Email Security
- Account Takeover
- Behavioral AI
- SaaS Security
- Phishing
- BEC
use_cases:
- description: Stop business email compromise, phishing, and vendor email compromise on Microsoft 365 and Google Workspace
  name: BEC and Phishing Defense
- description: Detect and respond to compromised email and SaaS accounts in near-real time
  name: Account Takeover Response
- description: Use AI Security Agents to triage user-reported emails and automate SOC workflows
  name: SOC Automation
- description: Continuously identify and remediate Microsoft 365 misconfigurations
  name: Security Posture Hardening
- description: Use the AI Data Analyst to deliver board-ready security reporting through natural-language queries
  name: Executive Reporting
website: https://abnormal.ai/
---
