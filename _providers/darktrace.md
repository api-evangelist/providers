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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: The Darktrace OmniAPI is a gated REST API hosted on each customer's Darktrace cloud instance at <instance>.cloud.darktrace.com/omniapi. It provides programmatic access to Darktrace's ActiveAI platform
  name: Darktrace OmniAPI
  slug: darktrace-omniapi
artifact_total: 33
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/darktrace-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/darktrace-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/darktrace-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/darktrace
- group: company
  title: ''
  type: Website
  url: https://www.darktrace.com/
- group: start
  title: Darktrace Customer Portal
  type: Portal
  url: https://customerportal.darktrace.com
- group: company
  title: ''
  type: Blog
  url: https://www.darktrace.com/blog
- group: other
  title: ''
  type: Resources
  url: https://www.darktrace.com/resources
- group: operate
  title: ''
  type: ContactSales
  url: https://www.darktrace.com/contact
- group: company
  title: ''
  type: Careers
  url: https://www.darktrace.com/careers
- group: company
  title: ''
  type: Partners
  url: https://www.darktrace.com/partners
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.darktrace.com/legal/privacy-statement
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.darktrace.com/legal/terms-and-conditions
created: '2026-05-23'
description: Darktrace builds the ActiveAI Security Platform, an AI-native cybersecurity platform powered by Self-Learning AI that models normal behavior across network, email, cloud, identity, OT, and endpoint environments to detect novel threats without relying on predefined signatures. The platform spans Network, Email, Cloud, Identity, OT, Endpoint, and Secure AI products plus cross-platform capabilities including Cyber AI Analyst, Proactive Exposure Management, Attack Surface Management, Adaptive Human Defense, and Forensic Acquisition & Investigation. Darktrace exposes a gated REST API at <instance>.cloud.darktrace.com/omniapi for partner and customer integrations. Named a Leader in the 2025 Gartner Magic Quadrant for NDR; serves 10,000+ customers globally.
features:
- description: Unsupervised AI that learns each organization's normal behavior to detect novel and unknown threats
  name: Self-Learning AI
- description: Unified AI cybersecurity platform spanning network, email, cloud, identity, OT, and endpoint
  name: ActiveAI Security Platform
- description: AI-driven NDR with proactive protection beyond traditional signature-based tools
  name: Network
- description: Cloud-native AI email security for phishing, BEC, and account takeover
  name: Email
- description: AI security across AWS, Azure, and Google Cloud workloads and control planes
  name: Cloud
- description: 360-degree user protection against identity-based threats
  name: Identity
- description: AI security for operational technology and converged IT/OT environments
  name: OT
- description: AI-driven endpoint coverage across managed and unmanaged devices
  name: Endpoint
- description: Security controls for safely deploying internal and third-party AI agents
  name: Secure AI
- description: Autonomous investigation that accelerates triage by up to 10x
  name: Cyber AI Analyst
- description: Risk reduction across internal and external attack surfaces
  name: Proactive Exposure Management
- description: Continuous discovery surfacing 30-50% more external assets than traditional tools
  name: Attack Surface Management
- description: Human-focused security awareness and behavior change
  name: Adaptive Human Defense
- description: Evidence collection and forensic investigation capabilities
  name: Forensic Acquisition and Investigation
- description: Preparation, response, and recovery services for security incidents
  name: Incident Readiness and Recovery
finops:
- name: Darktrace Finops
  service_category: API
  slug: darktrace-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/darktrace.png
integrations:
- description: OmniAPI-driven integrations with Splunk, Microsoft Sentinel, Chronicle, QRadar, and others
  name: SIEM
- description: Bidirectional integrations with Cortex XSOAR, Splunk SOAR, Tines, and similar platforms
  name: SOAR
- description: Native integrations with AWS, Azure, and Google Cloud for cloud telemetry and response
  name: Cloud Providers
- description: Integrations with Microsoft Entra ID, Okta, and other IdPs for identity-centric detection
  name: Identity Providers
- description: Ticketing integrations with ServiceNow, Jira, and other ITSM platforms
  name: ITSM
layout: provider
modified: '2026-05-23'
name: Darktrace
nav: Providers
network: true
overview: 'Darktrace publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Cybersecurity, Self-Learning AI, ActiveAI, NDR, and Email Security.


  Darktrace''s developer surface includes developer portal, engineering blog, and 11 more developer resources.'
plans:
- name: Darktrace Plans Pricing
  plan_count: 1
  slug: darktrace-plans-pricing
random_paper: 54
rate_limits:
- limit_count: 2
  name: Darktrace Rate Limits
  slug: darktrace-rate-limits
score:
  band: emerging
  composite: 23.4
  delta: -2.4
  facets:
    commercial_clarity: 57.9
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 25.8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/darktrace/refs/heads/main/screenshots/darktrace-2026-06-20T175459.png
security:
- kind: domain-security
  name: Darktrace Domain Security
  slug: darktrace-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Darktrace Vulnerability Disclosure
  slug: darktrace-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Darktrace Trust Center
  slug: darktrace-trust-center
  summary_line: trust center published
slug: darktrace
tags:
- Cybersecurity
- Self-Learning AI
- ActiveAI
- NDR
- Email Security
- Cloud Security
- OT Security
- Endpoint Security
use_cases:
- description: Use Self-Learning AI to detect zero-day, insider, and AI-driven attacks without signatures
  name: Novel Threat Detection
- description: Use Antigena to take targeted, surgical autonomous response actions on detected threats
  name: Autonomous Response
- description: Deploy AI email security against phishing, BEC, supply-chain compromise, and account takeover
  name: Email and Phishing Defense
- description: Protect industrial control systems and converged IT/OT environments
  name: OT and Critical Infrastructure
- description: Detect threats across multi-cloud workloads and cloud control planes
  name: Cloud Workload Protection
- description: Use Cyber AI Analyst to automate investigation and surface narrative incidents
  name: SOC Triage Acceleration
website: https://www.darktrace.com/
---
