---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 18
  human_in_the_loop: 0
  name: Checkpoint Agentic Access
  operation_count: 24
  slug: checkpoint-agentic-access
  summary_line: 24 operations · 18 acting
api_count: 21
apis:
- description: REST API for centrally managing Check Point Quantum Spark SMB appliances including configuration and policy.
  name: Check Point Spark Management API
  slug: spark-management-api
- description: REST API for the Zero Touch deployment service that streamlines bring-up of new Check Point appliances.
  name: Check Point Zero Touch API
  slug: zero-touch-api
- description: REST API for the Check Point Threat Hunting (TH) platform exposing threat intelligence, indicators, and hunting queries.
  name: Check Point Threat Hunting API
  slug: th-api
- description: Management API for the CloudGuard WAF cloud-native web application and API protection product.
  name: Check Point CloudGuard WAF API
  slug: cloudguard-waf-api
- description: The Access Rules API from Check Point — 2 operation(s) for access rules.
  name: Check Point Access Rules API
  slug: checkpoint-access-rules-api
- description: The Cloud Accounts API from Check Point — 1 operation(s) for cloud accounts.
  name: Check Point Cloud Accounts API
  slug: checkpoint-cloud-accounts-api
- description: The Compliance API from Check Point — 1 operation(s) for compliance.
  name: Check Point Compliance API
  slug: checkpoint-compliance-api
- description: The Events API from Check Point — 1 operation(s) for events.
  name: Check Point Events API
  slug: checkpoint-events-api
- description: The Findings API from Check Point — 1 operation(s) for findings.
  name: Check Point Findings API
  slug: checkpoint-findings-api
- description: The Hosts API from Check Point — 2 operation(s) for hosts.
  name: Check Point Hosts API
  slug: checkpoint-hosts-api
- description: The Identity API from Check Point — 2 operation(s) for identity.
  name: Check Point Identity API
  slug: checkpoint-identity-api
- description: The Interfaces API from Check Point — 1 operation(s) for interfaces.
  name: Check Point Interfaces API
  slug: checkpoint-interfaces-api
- description: The Login API from Check Point — 2 operation(s) for login.
  name: Check Point Login API
  slug: checkpoint-login-api
- description: The NAT Rules API from Check Point — 1 operation(s) for nat rules.
  name: Check Point NAT Rules API
  slug: checkpoint-nat-rules-api
- description: The Networks API from Check Point — 1 operation(s) for networks.
  name: Check Point Networks API
  slug: checkpoint-networks-api
- description: The Quarantine API from Check Point — 1 operation(s) for quarantine.
  name: Check Point Quarantine API
  slug: checkpoint-quarantine-api
- description: The Routes API from Check Point — 1 operation(s) for routes.
  name: Check Point Routes API
  slug: checkpoint-routes-api
- description: The Rulesets API from Check Point — 1 operation(s) for rulesets.
  name: Check Point Rulesets API
  slug: checkpoint-rulesets-api
- description: The Services API from Check Point — 1 operation(s) for services.
  name: Check Point Services API
  slug: checkpoint-services-api
- description: The Sessions API from Check Point — 2 operation(s) for sessions.
  name: Check Point Sessions API
  slug: checkpoint-sessions-api
- description: The System API from Check Point — 1 operation(s) for system.
  name: Check Point System API
  slug: checkpoint-system-api
artifact_total: 37
collections:
- collection_type: open
  name: Check Point CloudGuard API
  slug: open-checkpoint-cloudguard-api
- collection_type: open
  name: Check Point Gaia API
  slug: open-checkpoint-gaia-api
- collection_type: open
  name: Check Point Harmony Email API
  slug: open-checkpoint-harmony-email-api
- collection_type: open
  name: Check Point Identity Awareness API
  slug: open-checkpoint-identity-awareness-api
- collection_type: open
  name: Check Point Management API
  slug: open-checkpoint-management-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/checkpoint-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/checkpoint-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/checkpoint-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/check-point-software-technologies
- group: company
  title: ''
  type: Website
  url: https://www.checkpoint.com/
- group: docs
  title: ''
  type: Documentation
  url: https://sc1.checkpoint.com/documents/
- group: operate
  title: ''
  type: Support
  url: https://www.checkpoint.com/support-services/
- group: start
  title: ''
  type: Login
  url: https://portal.checkpoint.com/
- group: company
  title: ''
  type: Blog
  url: https://blog.checkpoint.com/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/CheckPointSW
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.checkpoint.com/about-us/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.checkpoint.com/about-us/privacy-statement/
- group: design
  title: ''
  type: JSONLD
  url: json-ld/checkpoint-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/checkpoint-host-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/checkpoint-access-rule-schema.json
- group: design
  title: ''
  type: Spectral
  url: spectral/checkpoint-spectral.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.cgn.portal.checkpoint.com/llms.txt
created: '2025-01-08'
description: Check Point Software Technologies is a global cybersecurity vendor providing network, cloud, endpoint, mobile, and email security through its Quantum, CloudGuard, and Harmony product families. Check Point exposes a wide range of REST APIs for security automation, including the Smart-1 Management API, Gaia OS API, CloudGuard cloud security posture API, Identity Awareness API, Spark and Zero Touch device management APIs, Harmony Email and Collaboration API, Threat Hunting (TH) API, and CloudGuard WAF API.
finops:
- name: Checkpoint Finops
  service_category: Security
  slug: checkpoint-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/checkpoint.png
json_schemas:
- name: Check Point Access Rule
  property_count: 9
  slug: checkpoint-access-rule
- name: Check Point Host Object
  property_count: 7
  slug: checkpoint-host
json_structures:
- name: Checkpoint Structure
  property_count: 0
  slug: checkpoint-structure
jsonld:
- class_count: 0
  name: Checkpoint Context
  property_count: 6
  slug: checkpoint-context
layout: provider
modified: '2026-05-19'
name: Check Point
nav: Providers
network: true
overview: 'Check Point publishes 17 APIs on the [APIs.io](https://apis.io/) network, including Access Rules API, Cloud Accounts API, Compliance API, and 14 more. Tagged areas include Cloud Security, Cybersecurity, Endpoint Security, Firewall, and Identity Awareness.


  The Check Point catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Check Point''s developer surface includes authentication, documentation, support, engineering blog, GitHub presence, and 12 more developer resources.'
plans:
- name: Checkpoint Plans Pricing
  plan_count: 1
  slug: checkpoint-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 2
  name: Checkpoint Rate Limits
  slug: checkpoint-rate-limits
rules:
- name: Check Point API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: checkpoint-jsonschema-spectral-rules
score:
  band: developing
  composite: 45.0
  delta: -5.1
  facets:
    commercial_clarity: 47.4
    contract_quality: 59.0
    developer_ergonomics: 26.1
    discoverability: 72.2
    governance: 58.3
    operational_transparency: 10.5
  previous_composite: 50.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 17
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/checkpoint/refs/heads/main/screenshots/checkpoint-2026-07-25T205134.png
security:
- kind: authentication
  name: Checkpoint Authentication
  slug: checkpoint-authentication
  summary_line: apiKey/http · 4 schemes
- kind: domain-security
  name: Checkpoint Domain Security
  slug: checkpoint-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: checkpoint
tags:
- Cloud Security
- Cybersecurity
- Endpoint Security
- Firewall
- Identity Awareness
- Mobile Security
- Network Security
- Security
- Threat Prevention
- WAF
website: https://www.checkpoint.com/
---
