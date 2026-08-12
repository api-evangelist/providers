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
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.0
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Zluri Agentic Access
  operation_count: 13
  slug: zluri-agentic-access
  summary_line: 13 operations · 8 acting
api_count: 4
apis:
- description: Upload snapshot and fact data within a sync session. Snapshot data represents current state, while fact data represents historical events. Data must be uploaded in paginated batches of up to 1000 reco
  name: Zluri Data Upload API
  slug: zluri-data-upload-api
- description: Manage integration instances for syncing data with Zluri.
  name: Zluri Instances API
  slug: zluri-instances-api
- description: Create and manage sync sessions for uploading data to Zluri. A sync must be created before uploading data, and finished after all data is uploaded.
  name: Zluri Syncs API
  slug: zluri-syncs-api
- description: Manage webhooks for receiving real-time notifications from Zluri.
  name: Zluri Webhooks API
  slug: zluri-webhooks-api
artifact_total: 64
collections:
- collection_type: postman
  name: Zluri Data Upload API
  slug: postman-zluri-data-upload-api
- collection_type: postman
  name: Zluri Data Upload Instances API
  slug: postman-zluri-instances-api
- collection_type: postman
  name: Zluri Data Upload Syncs API
  slug: postman-zluri-syncs-api
- collection_type: postman
  name: Zluri Data Upload Webhooks API
  slug: postman-zluri-webhooks-api
- collection_type: open
  name: Zluri API
  slug: open-zluri-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/zluri/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/zluri-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/zluri-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/zluri-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zluri-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/zluri-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ZluriHQ
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/zluri
- group: other
  title: ''
  type: Customers
  url: https://www.zluri.com/case-studies
- group: auth
  title: ''
  type: Security
  url: https://www.zluri.com/security
- group: other
  title: ''
  type: Events
  url: https://www.zluri.com/events
- group: operate
  title: ''
  type: Contact
  url: https://www.zluri.com/contact-us
- group: company
  title: ''
  type: Blog
  url: https://www.zluri.com/blog?all=All
- group: other
  title: ''
  type: WhitePapers
  url: https://www.zluri.com/whitepapers
- group: learn
  title: ''
  type: Webinars
  url: https://www.zluri.com/webinars
- group: start
  title: ''
  type: Login
  url: https://support.zluri.com/support/login
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.zluri.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.zluri.com/policy/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.zluri.com/policy/privacy-policy
- group: design
  title: ''
  type: JSONLD
  url: json-ld/zluri-context.jsonld
- group: design
  title: ''
  type: SpectralRules
  url: rules/zluri-spectral.yaml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/zluri-vocabulary.yaml
- group: agent
  title: ''
  type: LlmsText
  url: https://developers.zluri.com/llms.txt
created: '2025-07-15'
description: Zluri is a SaaS management and operations platform that helps organizations discover, govern, and optimize all their cloud applications. By connecting to SSO, finance, HR systems, and app APIs, it builds a unified system of record for SaaS usage, users, licenses, and spend. IT, finance, and procurement teams use Zluri to surface shadow IT, eliminate redundant or underused tools, rightsize licenses, and manage renewals and vendor relationships.
examples:
- key_count: 5
  name: Zluri Create Sync Example
  slug: zluri-create-sync-example
- key_count: 3
  name: Zluri Create Webhook Example
  slug: zluri-create-webhook-example
- key_count: 1
  name: Zluri List Instances Example
  slug: zluri-list-instances-example
- key_count: 3
  name: Zluri Upload Fact Data Example
  slug: zluri-upload-fact-data-example
- key_count: 3
  name: Zluri Upload Snapshot Data Example
  slug: zluri-upload-snapshot-data-example
features:
- name: SaaS Management
- name: Access Management
- name: Access Requests
- name: Access Reviews
- name: SOC 2
- name: ISO 27001
- name: HIPAA
- name: SOX ITGC
- name: PCI DSS
- name: User Activity Patterns
- name: Manage Renewals
- name: SaaS Discovery
- name: Security Policies
- name: Optimize Spends
- name: Smart Contracts
- name: Renewal Management
- name: Integrations
- name: Provisioning
- name: Deprovisioning
- name: Time Bound Access Controls
finops:
- name: Zluri Finops
  service_category: API
  slug: zluri-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zluri.png
json_schemas:
- name: Zluri API Error
  property_count: 2
  slug: error
- name: Zluri Fact Data Upload
  property_count: 3
  slug: fact-data-upload
- name: Zluri Integration Instance
  property_count: 6
  slug: instance
- name: Zluri Snapshot Data Upload
  property_count: 3
  slug: snapshot-data-upload
- name: Zluri Sync Session
  property_count: 5
  slug: sync
- name: Zluri Webhook
  property_count: 6
  slug: webhook
json_structures:
- name: Error Structure
  property_count: 2
  slug: error-structure
- name: Fact Data Upload Structure
  property_count: 3
  slug: fact-data-upload-structure
- name: Instance Structure
  property_count: 6
  slug: instance-structure
- name: Snapshot Data Upload Structure
  property_count: 3
  slug: snapshot-data-upload-structure
- name: Sync Structure
  property_count: 5
  slug: sync-structure
- name: Webhook Structure
  property_count: 6
  slug: webhook-structure
jsonld:
- class_count: 0
  name: Zluri Context
  property_count: 9
  slug: zluri-context
layout: provider
modified: '2026-05-19'
name: Zluri
nav: Providers
network: true
overview: 'Zluri publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Data Upload API, Instances API, Syncs API, and 1 more. Tagged areas include Access Management and SaaS Management.


  The Zluri catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Zluri''s developer surface includes authentication, engineering blog, and 21 more developer resources.'
plans:
- name: Zluri Plans Pricing
  plan_count: 3
  slug: zluri-plans-pricing
random_paper: 102
rate_limits:
- limit_count: 5
  name: Zluri Rate Limits
  slug: zluri-rate-limits
rules:
- name: Zluri API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: zluri-jsonschema-spectral-rules
- name: Zluri API Rules
  rule_count: 7
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 4
  slug: zluri-spectral
score:
  band: developing
  composite: 51.3
  delta: -7.9
  facets:
    commercial_clarity: 57.9
    contract_quality: 74.6
    developer_ergonomics: 17.4
    discoverability: 63.0
    governance: 68.8
    operational_transparency: 23.7
  previous_composite: 59.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
security:
- kind: authentication
  name: Zluri Authentication
  slug: zluri-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Zluri Domain Security
  slug: zluri-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Zluri Vulnerability Disclosure
  slug: zluri-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Zluri Trust Center
  slug: zluri-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, HIPAA, GDPR
slug: zluri
tags:
- Access Management
- SaaS Management
use_cases:
- name: Identity Visibility
- name: Application Visibility
- name: Uncover Shadow IT
- name: Monitor AI Apps
- name: Identity Lifecycle Management
- name: Access Requests
- name: Access Reviews
---
