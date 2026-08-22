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
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.9
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 60
  human_in_the_loop: 2
  name: Boldsign Agentic Access
  operation_count: 85
  slug: boldsign-agentic-access
  summary_line: 85 operations · 60 acting · 2 human-in-the-loop
api_count: 11
apis:
- description: The Branding API from BoldSign — 6 operation(s) for branding.
  name: BoldSign Branding API
  slug: boldsign-branding-api
- description: The Contacts API from BoldSign — 5 operation(s) for contacts.
  name: BoldSign Contacts API
  slug: boldsign-contacts-api
- description: The Custom Field API from BoldSign — 5 operation(s) for custom field.
  name: BoldSign Custom Field API
  slug: boldsign-custom-field-api
- description: The Document API from BoldSign — 25 operation(s) for document.
  name: BoldSign Document API
  slug: boldsign-document-api
- description: The GroupContacts API from BoldSign — 5 operation(s) for groupcontacts.
  name: BoldSign GroupContacts API
  slug: boldsign-groupcontacts-api
- description: The Identity Verification API from BoldSign — 3 operation(s) for identity verification.
  name: BoldSign Identity Verification API
  slug: boldsign-identity-verification-api
- description: The Plan API from BoldSign — 1 operation(s) for plan.
  name: BoldSign Plan API
  slug: boldsign-plan-api
- description: The Sender Identities API from BoldSign — 7 operation(s) for sender identities.
  name: BoldSign Sender Identities API
  slug: boldsign-sender-identities-api
- description: The Teams API from BoldSign — 4 operation(s) for teams.
  name: BoldSign Teams API
  slug: boldsign-teams-api
- description: The Template API from BoldSign — 16 operation(s) for template.
  name: BoldSign Template API
  slug: boldsign-template-api
- description: The User API from BoldSign — 8 operation(s) for user.
  name: BoldSign User API
  slug: boldsign-user-api
artifact_total: 36
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: BoldSign Branding API
  slug: open-boldsign-branding-api
- collection_type: open
  name: BoldSign Branding Contacts API
  slug: open-boldsign-contacts-api
- collection_type: open
  name: BoldSign Branding Custom Field API
  slug: open-boldsign-custom-field-api
- collection_type: open
  name: BoldSign Branding Document API
  slug: open-boldsign-document-api
- collection_type: open
  name: BoldSign Branding GroupContacts API
  slug: open-boldsign-groupcontacts-api
- collection_type: open
  name: BoldSign Branding Identity Verification API
  slug: open-boldsign-identity-verification-api
- collection_type: open
  name: BoldSign Branding Plan API
  slug: open-boldsign-plan-api
- collection_type: open
  name: BoldSign Branding Sender Identities API
  slug: open-boldsign-sender-identities-api
- collection_type: open
  name: BoldSign Branding Teams API
  slug: open-boldsign-teams-api
- collection_type: open
  name: BoldSign Branding Template API
  slug: open-boldsign-template-api
- collection_type: open
  name: BoldSign Branding User API
  slug: open-boldsign-user-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/boldsign-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/boldsign-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/boldsign-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://boldsign.com/esignature-api/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.boldsign.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/boldsign
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/bold-sign-app/
- group: other
  title: ''
  type: X
  url: https://twitter.com/boldsignapp
- group: company
  title: ''
  type: Blog
  url: https://boldsign.com/blogs/
- group: commercial
  title: ''
  type: Pricing
  url: https://boldsign.com/electronic-signature-pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.boldsign.com/
- group: start
  title: ''
  type: Sandbox
  url: https://developers.boldsign.com/api-overview/getting-started/
- group: commercial
  title: ''
  type: Plans
  url: plans/boldsign-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/boldsign-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/boldsign-finops.yml
created: 2026-06-12
description: BoldSign is an e-signature platform built by Syncfusion that provides a REST API for sending documents for electronic signature, managing reusable templates, tracking envelope status, and embedding signing and requesting workflows directly into third-party applications. The API supports both API key and OAuth 2.0 authentication and outputs JSON responses across US, EU, CA, and AU regional endpoints. BoldSign offers official SDKs for .NET, Python, Java, Node.js, and PHP, along with a free sandbox environment, a Postman collection, and an interactive API Explorer. The platform is SOC 2 Type II, HIPAA, GDPR, and eIDAS compliant, and supports webhooks for real-time event notifications.
examples:
- key_count: 4
  name: Boldsign Create Embedded Request Url Example
  slug: boldsign-create-embedded-request-url-example
- key_count: 4
  name: Boldsign Create Template Example
  slug: boldsign-create-template-example
- key_count: 4
  name: Boldsign Get Document Properties Example
  slug: boldsign-get-document-properties-example
- key_count: 4
  name: Boldsign Send Document Example
  slug: boldsign-send-document-example
finops:
- name: Boldsign Finops
  service_category: ''
  slug: boldsign-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/boldsign.png
json_schemas:
- name: BoldSign API Schemas
  property_count: 0
  slug: boldsign-schemas
jsonld:
- class_count: 22
  name: Boldsign Context
  property_count: 37
  slug: boldsign-context
layout: provider
modified: 2026-06-12
name: BoldSign
nav: Providers
network: true
overview: 'BoldSign publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Branding API, Contacts API, Custom Field API, and 8 more. Tagged areas include E-Signature, Electronic Signature, Document Management, Embedded Signing, and Webhooks.


  The BoldSign catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  BoldSign''s developer surface includes authentication, documentation, engineering blog, pricing, sandbox, and 10 more developer resources.'
plans:
- name: Boldsign Plans Pricing
  plan_count: 6
  slug: boldsign-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 2
  name: Boldsign Rate Limits
  slug: boldsign-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: BoldSign API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: boldsign-jsonschema-spectral-rules
score:
  band: developing
  composite: 45.4
  delta: -7.5
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 9.8
    contract_quality: 69.7
    developer_ergonomics: 21.4
    discoverability: 74.1
    governance: 9.8
    operational_transparency: 39.5
  previous_composite: 52.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/boldsign/refs/heads/main/screenshots/boldsign-2026-06-20T173555.png
security:
- kind: authentication
  name: Boldsign Authentication
  slug: boldsign-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Boldsign Domain Security
  slug: boldsign-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: boldsign
tags:
- E-Signature
- Electronic Signature
- Document Management
- Embedded Signing
- Webhooks
- Templates
- Identity Verification
- Compliance
website: https://boldsign.com/esignature-api/
---
