---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: The Spendflo API provides programmatic access to SaaS spend management, procurement workflows, vendor management, usage analytics, and contract management data. It enables enterprise-grade integration
  name: Spendflo API
  slug: spendflo-api
artifact_total: 13
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/spendflo-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/spendflo-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/spendflo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.spendflo.com/
- group: company
  title: ''
  type: Blog
  url: https://www.spendflo.com/blog
- group: company
  title: ''
  type: About
  url: https://www.spendflo.com/what-is-spendflo
- group: commercial
  title: ''
  type: Pricing
  url: https://www.spendflo.com/pricing
- group: other
  title: ''
  type: Vendors
  url: https://www.spendflo.com/vendors
- group: other
  title: ''
  type: UsageAnalytics
  url: https://www.spendflo.com/usage-analytics
- group: other
  title: ''
  type: VendorManagement
  url: https://www.spendflo.com/vendor-management
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.spendflo.com/support/home
- group: start
  title: ''
  type: Login
  url: https://app.spendflo.com/
- group: start
  title: ''
  type: Signup
  url: https://www.spendflo.com/book-a-demo
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/spendflo
created: '2026-03-16'
description: Spendflo is an AI-native procurement platform that centralizes intake-to-pay, enforces procurement policy, and reduces SaaS and vendor spend by combining AI-powered automation with expert-led negotiation. The Flash AI suite includes a Contract Analyst, Payables Agent, Procurement Analyst, and AI Workflow Builder. The platform provides intake management, supplier management, PO management, contract management, usage analytics, conversational reporting, and pricing benchmarks, with native integrations to finance (NetSuite, QuickBooks, Coupa, Xero), SSO (Okta, Azure AD), HRMS (BambooHR, HiBob), procurement (Jira, Ironclad, DocuSign, Slack), and spend tools.
examples:
- key_count: 17
  name: Spendflo Vendor Example
  slug: spendflo-vendor-example
finops:
- name: Spendflo Finops
  service_category: API
  slug: spendflo-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/spendflo.png
json_schemas:
- name: Spendflo Vendor
  property_count: 17
  slug: spendflo-vendor
json_structures:
- name: Spendflo Vendor Structure
  property_count: 0
  slug: spendflo-vendor-structure
jsonld:
- class_count: 10
  name: Spendflo Context
  property_count: 13
  slug: spendflo-context
layout: provider
modified: '2026-05-02'
name: Spendflo
nav: Providers
network: true
overview: 'Spendflo publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include License Management, Procurement, SaaS Management, Spend Management, and Usage Analytics.


  The Spendflo catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Spendflo''s developer surface includes engineering blog, pricing, signup flow, and 11 more developer resources.'
plans:
- name: Spendflo Plans Pricing
  plan_count: 3
  slug: spendflo-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 5
  name: Spendflo Rate Limits
  slug: spendflo-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Spendflo API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: spendflo-jsonschema-spectral-rules
- effective_rule_count: 45
  extends:
  - spectral:oas
  name: Spendflo API Rules
  rule_count: 4
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 2
  slug: spendflo-rules
score:
  band: thin
  composite: 28.5
  coverage:
    artifact_dirs: 12
    catalog_gap: 42.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 40.8
    commercial_clarity: 40.8
    contract_governance: 28.8
    contract_quality: 22.7
    developer_ergonomics: 16.7
    discoverability: 68.5
    governance: 28.8
    operational_transparency: 7.9
  previous_composite: 28.5
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/spendflo/refs/heads/main/screenshots/spendflo-2026-06-20T194314.png
security:
- kind: domain-security
  name: Spendflo Domain Security
  slug: spendflo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Spendflo Vulnerability Disclosure
  slug: spendflo-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Spendflo Trust Center
  slug: spendflo-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: spendflo
tags:
- License Management
- Procurement
- SaaS Management
- Spend Management
- Usage Analytics
- Vendor Management
website: https://www.spendflo.com/
---
