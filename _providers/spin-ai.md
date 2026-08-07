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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.8
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Spin Ai Agentic Access
  operation_count: 3
  slug: spin-ai-agentic-access
  summary_line: 3 operations · 2 acting
api_count: 1
apis:
- description: Entity management operations for reading, filtering, and updating the backup status of Google Workspace, Microsoft 365, and Salesforce entities such as users, groups, and shared drives
  name: Spin.AI Entities API
  slug: spin-ai-entities-api
artifact_total: 18
collections:
- collection_type: postman
  name: Spin.AI SpinOne Entities API
  slug: postman-spin-ai-entities-api
- collection_type: open
  name: Spin.AI SpinOne API
  slug: open-spin-ai
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/spinai/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/spin-ai-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/spin-ai-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/spin-ai-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/spin-ai-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/spin-ai-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.spin.ai
- group: docs
  title: ''
  type: Documentation
  url: https://spin.ai/help/
- group: start
  title: ''
  type: Portal
  url: https://spin.ai/help/gworkspace-administration/setting-up-public-api
- group: operate
  title: ''
  type: Support
  url: https://spin.ai/support/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://spin.ai/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://spin.ai/privacy-policy/
- group: company
  title: ''
  type: Blog
  url: https://spin.ai/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://spin.ai/blog/feed/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/spin-ai/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/spin-ai-openapi.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/spin-ai-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/spin-ai-vocabulary.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://spin.ai/llms.txt
created: '2026-03-27'
description: Spin.AI is a SaaS security platform providing data protection, ransomware detection, and compliance management for cloud applications including Google Workspace, Microsoft 365, Salesforce, and Slack. The SpinOne Public API enables programmatic integration for managing backup entity lifecycle across enterprise SaaS environments.
examples:
- key_count: 2
  name: Spin Ai Get All Entities Example
  slug: spin-ai-get-all-entities-example
- key_count: 2
  name: Spin Ai Update Entity Status Example
  slug: spin-ai-update-entity-status-example
finops:
- name: Spin Ai Finops
  service_category: API
  slug: spin-ai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/spin-ai.png
json_schemas:
- name: Spin.AI Backup Entity
  property_count: 11
  slug: spin-ai-entity
json_structures:
- name: Spin Ai Entity Structure
  property_count: 0
  slug: spin-ai-entity-structure
jsonld:
- class_count: 3
  name: Spin Ai Context
  property_count: 10
  slug: spin-ai-context
layout: provider
modified: '2026-05-19'
name: Spin.AI
nav: Providers
network: true
overview: 'Spin.AI publishes 1 API on the [APIs.io](https://apis.io/) network: Entities API. Tagged areas include Backup, Compliance, Data Protection, Ransomware, and SaaS Security.


  The Spin.AI catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Spin.AI''s developer surface includes authentication, documentation, developer portal, support, engineering blog, and 14 more developer resources.'
plans:
- name: Spin Ai Plans Pricing
  plan_count: 3
  slug: spin-ai-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 5
  name: Spin Ai Rate Limits
  slug: spin-ai-rate-limits
rules:
- name: Spin.AI API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: spin-ai-jsonschema-spectral-rules
- name: Spin.AI API Rules
  rule_count: 8
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 5
  slug: spin-ai-rules
score:
  band: strong
  composite: 57.6
  delta: 0.0
  facets:
    commercial_clarity: 68.4
    contract_quality: 71.3
    developer_ergonomics: 39.1
    discoverability: 59.3
    governance: 68.8
    operational_transparency: 31.6
  previous_composite: 57.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/spin-ai/refs/heads/main/screenshots/spin-ai-2026-06-20T194315.png
security:
- kind: authentication
  name: Spin Ai Authentication
  slug: spin-ai-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Spin Ai Domain Security
  slug: spin-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Spin Ai Vulnerability Disclosure
  slug: spin-ai-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Spin Ai Trust Center
  slug: spin-ai-trust-center
  summary_line: SOC 2, PCI DSS, HIPAA, GDPR
slug: spin-ai
tags:
- Backup
- Compliance
- Data Protection
- Ransomware
- SaaS Security
website: https://www.spin.ai
---
