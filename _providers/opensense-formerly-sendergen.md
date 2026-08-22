---
access_model:
  confidence: high
  label: Requires approval
  onboarding: approval
  pricing: paid
  public: false
  source:
  - https://www.opensense.com/pricing
  - https://www.opensense.com/demo
  trial: true
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 15.0
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://www.opensense.com/
- group: operate
  title: ''
  type: Support
  url: https://help.opensense.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.opensense.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.opensense.com/blog
- group: start
  title: ''
  type: Login
  url: https://app.opensense.com
- group: start
  title: ''
  type: SignUp
  url: https://www.opensense.com/demo
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.opensense.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.opensense.com/terms-and-conditions
- group: operate
  title: ''
  type: StatusPage
  url: https://status.opensense.com
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/opensense-formerly-sendergen-lifecycle.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/opensense-formerly-sendergen-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.opensense.com/security
- group: auth
  title: ''
  type: DomainSecurity
  url: security/opensense-formerly-sendergen-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/opensense-formerly-sendergen-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.opensense.com/security
- group: docs
  title: ''
  type: Documentation
  url: https://help.opensense.com/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/opensense-formerly-sendergen-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/opensense-formerly-sendergen-plans-pricing.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/opensense-formerly-sendergen-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/opensense-formerly-sendergen-conformance.yml
coverage:
  checked: '2026-08-13'
  detail: Opensense advertises a "robust API" on opensense.com/integrations and in its own llms.txt, but the only documented way to get a credential is the Zapier setup page, which says an Opensense integration specialist will provide an API key — there is no developer portal, no API reference among the 190 pages indexed in help.opensense.com/llms.txt, and api.opensense.com 302s to the marketing site with every spec path returning text/plain "Not Found".
  evidence:
  - status: 404
    url: https://api.opensense.com/openapi.json
  - status: 302
    url: https://api.opensense.com/
  - status: 200
    url: https://help.opensense.com/docs/zapier-integration.md
  - status: 200
    url: https://www.opensense.com/llms.txt
  reason: sales-gate
  state: gated
created: '2026-07-17'
description: Opensense (formerly SenderGen) is an email signature management platform that centrally governs email signatures, banners, and digital business cards across Microsoft 365 and Google Workspace. It lets IT enforce on-brand, compliant signatures while marketing and sales teams run targeted campaigns, track engagement, and connect to CRM and marketing platforms such as Salesforce, HubSpot, Marketo, and Outreach. Opensense is SOC 2 Type II attested, operates under GDPR and CCPA, and is the only email signature platform running inside Microsoft 365 GCC High for ITAR, DFARS, CMMC and FedRAMP-driven tenants. It advertises a REST API for custom integrations and serves an llms.txt on both its marketing and documentation hosts, but publishes no developer portal, no API reference and no machine-readable specification; API keys are issued manually by an Opensense integration specialist.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/opensense-formerly-sendergen.png
layout: provider
modified: '2026-08-13'
name: Opensense (formerly SenderGen)
nav: Providers
network: true
overview: 'Opensense (formerly SenderGen) is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Email Signature Management, Email Marketing, Brand Management, and Sales Enablement.


  Opensense (formerly SenderGen)''s developer surface includes support, pricing, engineering blog, signup flow, documentation, authentication, and 14 more developer resources.'
plans:
- name: Opensense Formerly Sendergen Plans Pricing
  plan_count: 0
  slug: opensense-formerly-sendergen-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Opensense Formerly Sendergen Rate Limits
  slug: opensense-formerly-sendergen-rate-limits
score:
  band: emerging
  composite: 26.1
  delta: -3.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 10.5
  previous_composite: 29.1
  provenance:
    conformance: first-party
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/opensense-formerly-sendergen/refs/heads/main/screenshots/opensense-formerly-sendergen-2026-08-07T190637.png
security:
- kind: authentication
  name: Opensense Formerly Sendergen Authentication
  slug: opensense-formerly-sendergen-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Opensense Formerly Sendergen Domain Security
  slug: opensense-formerly-sendergen-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Opensense Formerly Sendergen Vulnerability Disclosure
  slug: opensense-formerly-sendergen-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Opensense Formerly Sendergen Trust Center
  slug: opensense-formerly-sendergen-trust-center
  summary_line: SOC 2, HIPAA, FedRAMP, GDPR
slug: opensense-formerly-sendergen
tags:
- Company
- Email Signature Management
- Email Marketing
- Brand Management
- Sales Enablement
- Marketing
- Email
website: https://www.opensense.com/
---
