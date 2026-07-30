---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
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
- acting_count: 18
  human_in_the_loop: 0
  name: Cybereason Agentic Access
  operation_count: 26
  slug: cybereason-agentic-access
  summary_line: 26 operations · 18 acting
api_count: 10
apis:
- description: The Cybereason REST API is a gated, region-scoped API hosted at api.<region>.cybereason.net that allows customers and integration partners to query MalOps, retrieve sensor inventory and status, run th
  name: Cybereason REST API
  slug: cybereason-rest-api
- description: The Authentication API from Cybereason — 2 operation(s) for authentication.
  name: Cybereason Authentication API
  slug: cybereason-authentication-api
- description: The CustomDetectionRules API from Cybereason — 3 operation(s) for customdetectionrules.
  name: Cybereason CustomDetectionRules API
  slug: cybereason-customdetectionrules-api
- description: The IsolationRules API from Cybereason — 2 operation(s) for isolationrules.
  name: Cybereason IsolationRules API
  slug: cybereason-isolationrules-api
- description: The Malops API from Cybereason — 2 operation(s) for malops.
  name: Cybereason Malops API
  slug: cybereason-malops-api
- description: The Remediation API from Cybereason — 3 operation(s) for remediation.
  name: Cybereason Remediation API
  slug: cybereason-remediation-api
- description: The Reputation API from Cybereason — 1 operation(s) for reputation.
  name: Cybereason Reputation API
  slug: cybereason-reputation-api
- description: The Sensors API from Cybereason — 6 operation(s) for sensors.
  name: Cybereason Sensors API
  slug: cybereason-sensors-api
- description: The ThreatIntel API from Cybereason — 3 operation(s) for threatintel.
  name: Cybereason ThreatIntel API
  slug: cybereason-threatintel-api
- description: The VisualSearch API from Cybereason — 1 operation(s) for visualsearch.
  name: Cybereason VisualSearch API
  slug: cybereason-visualsearch-api
artifact_total: 38
collections:
- collection_type: open
  name: Cybereason API
  slug: open-cybereason
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cybereason-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/cybereason-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/cybereason-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cybereason-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cybereason-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cybereason
- group: company
  title: ''
  type: Website
  url: https://www.cybereason.com/
- group: start
  title: Cybereason Nest (Customer Portal)
  type: Portal
  url: https://nest.cybereason.com/
- group: docs
  title: ''
  type: Documentation
  url: https://nest.cybereason.com/documentation/api-documentation
- group: company
  title: ''
  type: Blog
  url: https://www.cybereason.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.cybereason.com/services/incident-response
- group: operate
  title: ''
  type: ContactSales
  url: https://www.cybereason.com/contact
- group: company
  title: ''
  type: Careers
  url: https://www.cybereason.com/company/careers
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cybereason.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cybereason.com/terms-of-use
created: '2026-05-23'
description: Cybereason is an enterprise cybersecurity company (now part of LevelBlue) that provides a defense platform spanning Extended Detection and Response (XDR), Endpoint Detection and Response (EDR), Next-Generation Antivirus (NGAV), Managed Detection and Response (MDR), mobile threat defense, and digital forensics and incident response. Its signature MalOp (Malicious Operation) engine correlates alerts across endpoints and identities into a single operation-centric attack story. Cybereason exposes a gated regional REST API (api.<region>.cybereason.net) for partner and customer integrations with SIEMs, SOARs, and security tooling.
features:
- description: Operation-centric detection that consolidates alerts and telemetry into a single contextualized attack story
  name: MalOp Engine
- description: Extended Detection and Response correlating endpoint, identity, network, and cloud signals
  name: XDR
- description: AI-powered Endpoint Detection and Response with deep behavioral analytics
  name: EDR
- description: Multi-layered Next-Generation Antivirus prevention including anti-ransomware
  name: NGAV
- description: 24x7 Managed Detection and Response across MDR Essentials, Essentials + XR, and MDR Complete tiers
  name: MDR
- description: Threat detection and response for iOS and Android endpoints
  name: Mobile Threat Defense
- description: Proactive risk reduction across the endpoint estate
  name: Vulnerability Management
- description: Proactive hunting across historical and live endpoint telemetry
  name: Threat Hunting
- description: DFIR services and 24x7 incident response on-call retainers
  name: Digital Forensics and Incident Response
- description: Threat intelligence and research from the Cybereason Nocturnus team
  name: Threat Intelligence
finops:
- name: Cybereason Finops
  service_category: API
  slug: cybereason-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cybereason.png
integrations:
- description: REST API and event forwarding integrations with Splunk, Microsoft Sentinel, Google Chronicle, and others
  name: SIEM
- description: Bidirectional integrations with SOAR platforms for automated containment and response actions
  name: SOAR
- description: Identity-based detections across major IdPs as part of the XDR coverage
  name: Identity Providers
- description: Mobile Threat Defense integrations with leading UEM/MDM platforms
  name: Mobile Device Management
layout: provider
modified: '2026-05-23'
name: Cybereason
nav: Providers
network: true
overview: 'Cybereason publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, CustomDetectionRules API, IsolationRules API, and 6 more. Tagged areas include Cybersecurity, XDR, EDR, NGAV, and MDR.


  Cybereason''s developer surface includes authentication, developer portal, documentation, engineering blog, support, and 10 more developer resources.'
plans:
- name: Cybereason Plans Pricing
  plan_count: 1
  slug: cybereason-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 2
  name: Cybereason Rate Limits
  slug: cybereason-rate-limits
score:
  band: thin
  composite: 41.3
  delta: -2.1
  facets:
    commercial_clarity: 57.9
    contract_quality: 50.4
    developer_ergonomics: 34.8
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 43.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cybereason/refs/heads/main/screenshots/cybereason-2026-06-20T175410.png
security:
- kind: authentication
  name: Cybereason Authentication
  slug: cybereason-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Cybereason Domain Security
  slug: cybereason-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Cybereason Vulnerability Disclosure
  slug: cybereason-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Cybereason Trust Center
  slug: cybereason-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, GDPR
slug: cybereason
tags:
- Cybersecurity
- XDR
- EDR
- NGAV
- MDR
- Endpoint Security
- Threat Detection
use_cases:
- description: Surface and triage MalOps directly inside the SOC with full attack-story context
  name: SOC Operations
- description: Stream detections and MalOps into Splunk, Sentinel, Chronicle, and other SIEMs via REST API
  name: SIEM Enrichment
- description: Outsource 24x7 detection and response to the Cybereason MDR team
  name: Managed Detection and Response
- description: Engage Cybereason DFIR services for breach investigation, containment, and recovery
  name: Incident Response
- description: Run targeted compromise assessments and cyber posture assessments across the environment
  name: Compromise Assessment
website: https://www.cybereason.com/
---
