---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
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
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Symantec Agentic Access
  operation_count: 9
  slug: symantec-agentic-access
  summary_line: 9 operations · 5 acting
api_count: 8
apis:
- description: The Symantec Endpoint Security (SES) REST API provides access to cloud-based endpoint security management including device inventory, threat events, incident management, and behavioral analytics. Requ
  name: Symantec Endpoint Security API
  slug: ses-api
- description: 'The Symantec EDR REST API enables programmatic access to endpoint detection and response capabilities including incident management, threat hunting, forensics, and entity queries. Uses OAuth 2.0 with '
  name: Symantec Endpoint Detection and Response API
  slug: symantec-edr-api
- description: 'The Symantec DLP REST API enables integration with the DLP Enforce platform for incident management, policy management, and data discovery. Supports retrieving incidents, updating remediation status, '
  name: Symantec Data Loss Prevention API
  slug: symantec-dlp-api
- description: SEPM administrator account management
  name: Symantec Administrators API
  slug: symantec-administrators-api
- description: API version information
  name: Symantec API Version API
  slug: symantec-api-version-api
- description: OAuth 2.0 authentication endpoints
  name: Symantec Authentication API
  slug: symantec-authentication-api
- description: Endpoint computer management and querying
  name: Symantec Computers API
  slug: symantec-computers-api
- description: SEPM group management
  name: Symantec Groups API
  slug: symantec-groups-api
artifact_total: 22
collections:
- collection_type: open
  name: Symantec Endpoint Protection Manager API
  slug: open-symantec-sepm-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/symantec-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/symantec-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/symantec-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/symantec
- group: company
  title: ''
  type: Website
  url: https://www.broadcom.com/products/cybersecurity/endpoint
- group: docs
  title: ''
  type: APIDocumentation
  url: https://apidocs.securitycloud.symantec.com/
- group: docs
  title: ''
  type: APIDocumentation
  url: https://apidocs.symantec.com/
- group: docs
  title: ''
  type: Documentation
  url: https://techdocs.broadcom.com/us/en/symantec-security-software
- group: operate
  title: ''
  type: Support
  url: https://support.broadcom.com
- group: operate
  title: ''
  type: Community
  url: https://community.broadcom.com/symantecenterprise
- group: build
  title: ''
  type: GitHub
  url: https://github.com/Symantec
- group: start
  title: ''
  type: Login
  url: https://sep.securitycloud.symantec.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.broadcom.com/company/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.broadcom.com/company/legal/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.broadcom.com/services/symantec-endpoint-security-enterprise/
- group: company
  title: ''
  type: Blog
  url: https://www.broadcom.com/blog/category/cybersecurity
- group: docs
  title: ''
  type: TechDocs
  url: https://techdocs.broadcom.com
- group: agent
  title: ''
  type: LlmsText
  url: https://apidocs.securitycloud.symantec.com/llms.txt
created: '2026-05-03'
description: Symantec (now part of Broadcom) is a leading enterprise cybersecurity company providing endpoint security, threat detection, data loss prevention, identity security, and network protection products. Symantec offers REST APIs for Endpoint Protection Manager (SEPM), Endpoint Security Cloud (SES), Endpoint Detection and Response (EDR), Data Loss Prevention (DLP), and the Integrated Cyber Defense Manager (ICDm) platform.
examples:
- key_count: 4
  name: Symantec Authenticate Example
  slug: symantec-authenticate-example
- key_count: 4
  name: Symantec List Computers Example
  slug: symantec-list-computers-example
finops:
- name: Symantec Finops
  service_category: Cybersecurity / Endpoint Security
  slug: symantec-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/symantec.png
json_schemas:
- name: Symantec SEPM Computer
  property_count: 13
  slug: symantec-computer
json_structures:
- name: Symantec Computer Structure
  property_count: 0
  slug: symantec-computer-structure
jsonld:
- class_count: 15
  name: Symantec Context
  property_count: 1
  slug: symantec-context
layout: provider
modified: '2026-05-19'
name: Symantec
nav: Providers
network: true
overview: 'Symantec publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Administrators API, API Version API, Authentication API, and 2 more. Tagged areas include Broadcom, Cybersecurity, DLP, EDR, and Endpoint Protection.


  The Symantec catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Symantec''s developer surface includes authentication, documentation, support, GitHub presence, engineering blog, and 13 more developer resources.'
plans:
- name: Symantec Plans Pricing
  plan_count: 1
  slug: symantec-plans-pricing
press:
- date: '2026-05-25'
  title: Broadcom Completes Acquisition of Symantec Enterprise ...
  url: https://www.prnewswire.com/news-releases/broadcom-completes-acquisition-of-symantec-enterprise-security-business-300950721.html
- date: '2026-05-25'
  title: Press Releases | Gen Digital
  url: https://newsroom.gendigital.com/Symantec-Targeted-Attack-Analytics-Enables-Customers-to-Uncover-the-Most-Sophisticated-and-Dangerous-Cyber-Attacks
- date: '2026-05-25'
  title: Broadcom Introduces Industry's First Incident Prediction ...
  url: https://cybersecurityasia.net/broadcom-first-incident-predict-capability/
- date: '2026-05-25'
  title: Symantec Unveils AI-Powered ICS Cybersecurity Platform
  url: https://www.govconwire.com/articles/symantec-unveils-ai-powered-ics-cybersecurity-platform
- date: '2026-05-25'
  title: Cyber Security - Symantec Enterprise Cloud
  url: https://jp.broadcom.com/products/cybersecurity?ver=1.11.4
random_paper: 21
rate_limits:
- limit_count: 2
  name: Symantec Rate Limits
  slug: symantec-rate-limits
rules:
- name: Symantec API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: symantec-jsonschema-spectral-rules
- name: Symantec API Rules
  rule_count: 7
  severity_counts:
    error: 0
    hint: 1
    info: 0
    warn: 6
  slug: symantec-rules
score:
  band: developing
  composite: 54.3
  delta: -5.0
  facets:
    commercial_clarity: 63.2
    contract_quality: 64.8
    developer_ergonomics: 32.6
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 42.1
  previous_composite: 59.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/symantec/refs/heads/main/screenshots/symantec-2026-06-20T194819.png
security:
- kind: authentication
  name: Symantec Authentication
  slug: symantec-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Symantec Domain Security
  slug: symantec-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: symantec
tags:
- Broadcom
- Cybersecurity
- DLP
- EDR
- Endpoint Protection
- Endpoint Security
- Security
- Symantec
- Fortune 500
website: https://www.broadcom.com/products/cybersecurity/endpoint
---
