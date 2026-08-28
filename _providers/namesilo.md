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
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: 'The NameSilo Domain API allows developers to search, register, transfer, renew, and manage domains programmatically. All API calls use HTTPS GET requests and return XML or JSON. A sandbox environment '
  name: NameSilo Domain API
  slug: namesilo
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/namesilo-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/namesilo
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/namesilo
- group: company
  title: ''
  type: Website
  url: https://www.namesilo.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.namesilo.com/api-reference
- group: start
  title: ''
  type: Signup
  url: https://www.namesilo.com/account/api-manager
- group: commercial
  title: ''
  type: Pricing
  url: https://www.namesilo.com/pricing
- group: operate
  title: ''
  type: Support
  url: https://www.namesilo.com/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.namesilo.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.namesilo.com/privacy-policy
created: '2025-02-09'
description: NameSilo is a domain registrar and web services provider offering domain registration, hosting, email, and SSL solutions. NameSilo exposes a Domain API enabling programmatic domain search, registration, and management via HTTPS GET requests with XML or JSON responses, plus an MCP server for AI agents.
finops:
- name: Namesilo Finops
  service_category: API
  slug: namesilo-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/namesilo.png
layout: provider
modified: '2026-04-28'
name: NameSilo
nav: Providers
network: true
overview: 'NameSilo publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Domains, Domain Registrar, DNS, Hosting, and SSL.


  NameSilo''s developer surface includes documentation, signup flow, pricing, support, and 6 more developer resources.'
plans:
- name: Namesilo Plans Pricing
  plan_count: 3
  slug: namesilo-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 5
  name: Namesilo Rate Limits
  slug: namesilo-rate-limits
score:
  band: emerging
  composite: 17.0
  delta: 1.4
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 15.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 11.1
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/namesilo/refs/heads/main/screenshots/namesilo-2026-08-07T184613.png
security:
- kind: domain-security
  name: Namesilo Domain Security
  slug: namesilo-domain-security
  summary_line: TLSv1.3 · DMARC
slug: namesilo
tags:
- Domains
- Domain Registrar
- DNS
- Hosting
- SSL
- Email
website: https://www.namesilo.com/
---
