---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-26'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/descartes-underwriting-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://descartesunderwriting.com/
- group: company
  title: ''
  type: Blog
  url: https://descartesunderwriting.com/insights
- group: operate
  title: ''
  type: Support
  url: https://descartesunderwriting.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://descartesunderwriting.com/legal-information
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://descartesunderwriting.com/legal-information
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/descartes-underwriting
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/descartes-underwriting-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/descartes-underwriting-plans-pricing.yml
coverage:
  checked: '2026-08-17'
  detail: Descartes Underwriting distributes bespoke parametric cover through corporate brokers and ships no public developer surface at all — /api, /docs, /developers, /openapi.json and every /.well-known/ path on descartesunderwriting.com return HTTP 404, no api./developer./docs./portal./ broker./app. subdomain resolves in DNS, and the company's seven public GitHub repositories are hiring technical tests and internal training rather than client SDKs.
  evidence:
  - status: 404
    url: https://descartesunderwriting.com/developers
  - status: 404
    url: https://descartesunderwriting.com/openapi.json
  - status: 404
    url: https://descartesunderwriting.com/.well-known/agent-card.json
  - status: 0
    url: https://api.descartesunderwriting.com/
  - status: 200
    url: https://api.github.com/orgs/descartes-underwriting/repos
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: Descartes Underwriting is a Paris-headquartered insurtech, founded in 2019, specializing in parametric insurance for climate, natural-catastrophe, cyber, and emerging corporate risks. It operates two complementary entities — Descartes Underwriting, a global parametric managing general agent (MGA), and Descartes Insurance, an ACPR-licensed European full-stack carrier — using AI, satellite imagery, IoT sensor data, and scientific risk models to structure index-based covers that pay out automatically within days when a predefined trigger is met, without a traditional claims-adjustment process. Backed by Battery Ventures and other investors, the company serves 600+ large corporations and public entities through corporate brokers across 20+ offices worldwide. No public developer API or documentation is published; the company distributes coverage through brokers rather than a self-serve API surface.
image: https://descartesunderwriting.com/themes/custom/webui/images/logo.svg
layout: provider
modified: '2026-08-17'
name: Descartes Underwriting
nav: Providers
network: true
overview: 'Descartes Underwriting is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Insurance, Parametric Insurance, Insurtech, and Climate Risk.


  Descartes Underwriting''s developer surface includes engineering blog, support, and 7 more developer resources.'
plans:
- name: Descartes Underwriting Plans Pricing
  plan_count: 0
  slug: descartes-underwriting-plans-pricing
random_paper: 7
score:
  band: minimal
  composite: 10.1
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 10.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 21.2
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/descartes-underwriting/refs/heads/main/screenshots/descartes-underwriting-2026-07-25T211753.png
security:
- kind: domain-security
  name: Descartes Underwriting Domain Security
  slug: descartes-underwriting-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: descartes-underwriting
tags:
- Company
- Insurance
- Parametric Insurance
- Insurtech
- Climate Risk
- Reinsurance
- Risk Management
- Cyber Insurance
website: https://descartesunderwriting.com/
---
