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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Onetrust Agentic Access
  operation_count: 24
  slug: onetrust-agentic-access
  summary_line: 24 operations · 13 acting
api_count: 12
apis:
- description: Cross-product REST API reference for the OneTrust platform covering privacy, GRC, ethics, third-party risk, and consent.
  name: OneTrust Platform API
  slug: platform-api
- description: Server-Side Consent Management Platform API for persisting consent, retrieving banner/preference center UI, and logging consent. Supports IAB TCF 2.3 and GPP.
  name: Server-Side CMP API
  slug: server-side-cmp
- description: REST API for AI risk classifications and metrics. Includes POST /classifications/v1, POST /metric, and GET /health.
  name: OneTrust AI Guard API
  slug: ai-guard
- description: Vendor risk and assessment APIs for the OneTrust Third-Party Risk Management module (formerly Vendorpedia).
  name: OneTrust Third-Party Risk (Vendorpedia) API
  slug: vendorpedia
- description: Mobile (iOS, Android), OTT/CTV (Roku, Fire TV, Apple TV, Android TV, Web OS, Tizen), and Website CMP SDKs.
  name: OneTrust SDK Suite
  slug: sdks
- description: The AI Governance API from OneTrust — 1 operation(s) for ai governance.
  name: OneTrust AI Governance API
  slug: onetrust-ai-governance-api
- description: The Applications API from OneTrust — 1 operation(s) for applications.
  name: OneTrust Applications API
  slug: onetrust-applications-api
- description: The Consent API from OneTrust — 4 operation(s) for consent.
  name: OneTrust Consent API
  slug: onetrust-consent-api
- description: The Cookies API from OneTrust — 3 operation(s) for cookies.
  name: OneTrust Cookies API
  slug: onetrust-cookies-api
- description: The Data Subjects API from OneTrust — 2 operation(s) for data subjects.
  name: OneTrust Data Subjects API
  slug: onetrust-data-subjects-api
- description: The Domains API from OneTrust — 2 operation(s) for domains.
  name: OneTrust Domains API
  slug: onetrust-domains-api
- description: The Privacy Notices API from OneTrust — 2 operation(s) for privacy notices.
  name: OneTrust Privacy Notices API
  slug: onetrust-privacy-notices-api
artifact_total: 28
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: OneTrust Platform AI Governance API
  slug: open-onetrust-ai-governance-api
- collection_type: open
  name: OneTrust Platform AI Governance Applications API
  slug: open-onetrust-applications-api
- collection_type: open
  name: OneTrust Platform AI Governance Consent API
  slug: open-onetrust-consent-api
- collection_type: open
  name: OneTrust Platform AI Governance Cookies API
  slug: open-onetrust-cookies-api
- collection_type: open
  name: OneTrust Platform AI Governance Data Subjects API
  slug: open-onetrust-data-subjects-api
- collection_type: open
  name: OneTrust Platform AI Governance Domains API
  slug: open-onetrust-domains-api
- collection_type: open
  name: OneTrust Platform AI Governance Privacy Notices API
  slug: open-onetrust-privacy-notices-api
- collection_type: open
  name: OneTrust Platform API
  slug: open-onetrust
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/onetrust-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/onetrust-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/onetrust-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/onetrust-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/onetrust
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/onetrust
- group: company
  title: ''
  type: Website
  url: https://www.onetrust.com/
- group: other
  title: ''
  type: Developer
  url: https://developer.onetrust.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/onetrust-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/onetrust-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/onetrust-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.onetrust.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.onetrust.com/blog/
created: '2026-05-08'
description: OneTrust is an enterprise privacy, security, ethics, and ESG platform. Its developer portal exposes APIs across Privacy Management, Third-Party Risk (Vendorpedia), Cookie Consent (Server-Side CMP), Certification Automation, GRC, AI Guard, and a broad SDK suite for mobile, OTT/CTV, and web.
finops:
- name: Onetrust Finops
  service_category: Compliance & Governance
  slug: onetrust-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/onetrust.png
layout: provider
modified: '2026-05-08'
name: OneTrust
nav: Providers
network: true
overview: 'OneTrust publishes 7 APIs on the [APIs.io](https://apis.io/) network, including AI Governance API, Applications API, Consent API, and 4 more. Tagged areas include Privacy, GRC, Compliance, Consent, and TPRM.


  OneTrust''s developer surface includes authentication, engineering blog, and 11 more developer resources.'
plans:
- name: Onetrust Plans Pricing
  plan_count: 1
  slug: onetrust-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 1
  name: Onetrust Rate Limits
  slug: onetrust-rate-limits
score:
  band: thin
  composite: 26.8
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 49.0
    developer_ergonomics: 14.3
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 26.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/onetrust/refs/heads/main/screenshots/onetrust-2026-06-20T190718.png
security:
- kind: authentication
  name: Onetrust Authentication
  slug: onetrust-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Onetrust Domain Security
  slug: onetrust-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Onetrust Trust Center
  slug: onetrust-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: onetrust
tags:
- Privacy
- GRC
- Compliance
- Consent
- TPRM
website: https://www.onetrust.com/
---
