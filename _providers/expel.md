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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-10'
api_count: 1
apis:
- description: The Expel Workbench API is a gated REST API used by customers and technology partners to integrate with the Expel MDR platform. The API powers ingest of signals from endpoint, cloud, SIEM, identity, a
  name: Expel Workbench API
  slug: expel-workbench-api
artifact_total: 27
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/expel-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/expel-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/expel-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/expel
- group: company
  title: ''
  type: Website
  url: https://expel.com/
- group: start
  title: Expel Workbench
  type: Portal
  url: https://workbench.expel.io
- group: company
  title: ''
  type: Blog
  url: https://expel.com/blog/
- group: other
  title: ''
  type: Resources
  url: https://expel.com/resources/
- group: operate
  title: ''
  type: ContactSales
  url: https://expel.com/contact/
- group: company
  title: ''
  type: Careers
  url: https://expel.com/careers/
- group: company
  title: ''
  type: Partners
  url: https://expel.com/partners/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://expel.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://expel.com/terms-of-use/
- group: agent
  title: ''
  type: LlmsText
  url: https://expel.com/llms.txt
created: '2026-05-23'
description: Expel is a managed detection and response (MDR) provider that delivers 24x7 security operations across endpoint, network, cloud, SaaS, identity, Kubernetes, and phishing surfaces. Customers and integration partners interact with Expel primarily through Workbench, Expel's investigation and case-management platform, which exposes a gated REST API for sending signals in from third-party tools and pulling alerts, investigations, and remediation actions back out into SIEMs, SOARs, and ticketing systems.
features:
- description: 24x7 managed detection and response across AWS, Azure, and Google Cloud
  name: MDR for Cloud
- description: Detection and response across Microsoft 365, Google Workspace, Okta, and other SaaS platforms
  name: MDR for SaaS
- description: Container and Kubernetes-aware detection and response
  name: MDR for Kubernetes
- description: Managed phishing triage, investigation, and remediation
  name: Phishing
- description: Proactive hunting across customer telemetry by Expel analysts
  name: Threat Hunting
- description: Risk-based vulnerability prioritization tied to threat context
  name: Vulnerability Prioritization
- description: Investigation, case-management, and analytics platform with REST API for customers and integration partners
  name: Workbench
finops:
- name: Expel Finops
  service_category: API
  slug: expel-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/expel.png
integrations:
- description: Native MDR integrations for AWS accounts, GuardDuty, and related cloud signals
  name: AWS
- description: MDR coverage and integrations for Azure, Entra ID, and Microsoft Defender
  name: Microsoft Azure
- description: MDR coverage for Google Cloud workloads and security signals
  name: Google Cloud
- description: SaaS detection and response coverage for Microsoft 365 tenants
  name: Microsoft 365
- description: SaaS detection and response coverage for Google Workspace tenants
  name: Google Workspace
- description: Bidirectional integrations with Splunk, Sentinel, Chronicle, and other SIEMs
  name: SIEM Platforms
- description: Workbench connectors for CrowdStrike, SentinelOne, Microsoft Defender, and other EDR tools
  name: EDR Platforms
- description: Integrations with Okta, Entra ID, and other identity providers for identity-centric detections
  name: Identity Providers
layout: provider
modified: '2026-05-23'
name: Expel
nav: Providers
network: true
overview: 'Expel publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Cybersecurity, MDR, Managed Detection and Response, SOC, and SIEM.


  Expel''s developer surface includes developer portal, engineering blog, and 12 more developer resources.'
plans:
- name: Expel Plans Pricing
  plan_count: 1
  slug: expel-plans-pricing
random_paper: 78
rate_limits:
- limit_count: 2
  name: Expel Rate Limits
  slug: expel-rate-limits
score:
  band: emerging
  composite: 23.4
  delta: 0.0
  facets:
    commercial_clarity: 57.9
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 23.4
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/expel/refs/heads/main/screenshots/expel-2026-06-20T180936.png
security:
- kind: domain-security
  name: Expel Domain Security
  slug: expel-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Expel Vulnerability Disclosure
  slug: expel-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Expel Trust Center
  slug: expel-trust-center
  summary_line: SOC 2, ISO 27001, GDPR, CSA STAR, FIPS 140
slug: expel
tags:
- Cybersecurity
- MDR
- Managed Detection and Response
- SOC
- SIEM
- Workbench
use_cases:
- description: Augment or replace an internal SOC with Expel's analysts and Workbench platform
  name: 24x7 SOC Outsourcing
- description: Continuous monitoring and incident response across multi-cloud environments
  name: Cloud Security Monitoring
- description: Automated and analyst-assisted phishing investigation and remediation
  name: Phishing Triage and Response
- description: Use Expel as the analyst layer on top of existing SIEM and SOAR investments
  name: SIEM and SOAR Augmentation
- description: Use Workbench data and reports to support SOC2, PCI, and other compliance regimes
  name: Compliance and Reporting
website: https://expel.com/
---
