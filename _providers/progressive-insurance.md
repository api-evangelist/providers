---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-11'
api_count: 3
apis:
- description: Returns an estimated auto insurance rate from consumer-supplied vehicle and driver data; partners embed the quote flow directly inside their own product surfaces and complete the policy purchase end-t
  name: Embedded Direct Quoting API
  slug: embedded-direct-quoting
- description: Quoting product for commercial auto policies; enables partners to surface Progressive commercial-lines coverage and rate options within their onboarding or fleet-management flows.
  name: Commercial Auto Quoting API
  slug: commercial-auto-quoting
- description: Generates or retrieves a certificate of insurance (COI) for a Progressive commercial policy; used by lenders, brokers, and operations platforms that need real-time proof-of-coverage documents.
  name: Certificate of Insurance API
  slug: certificate-of-insurance
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/progressive-insurance-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Progressive-Insurance
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/progressive-insurance
- group: company
  title: ''
  type: Website
  url: https://www.progressive.com/
- group: start
  title: ''
  type: AgentPortal
  url: https://www.foragentsonly.com/
- group: company
  title: ''
  type: Partners
  url: https://www.progressive.com/partners/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.progressive.com/
created: '2026-05-05'
description: One of the largest auto insurance providers in the United States offering personal auto, motorcycle, boat, RV, home, renters, and commercial insurance. Progressive is known for its direct-to-consumer model (1-800-PROGRESSIVE and progressive.com), its independent-agent channel, the comparative rate quoting experience, and the Snapshot usage-based insurance program that prices premiums against telematics-captured driving behaviour from a plug-in OBD-II dongle or the Snapshot mobile app. Progressive also runs the ForAgents agent portal and a public Developer Portal at developer.progressive.com that hosts embedded-quoting APIs for partners — including the Embedded Direct auto quoting API, the Commercial Auto Quoting product, and the Certificate of Insurance API — alongside private B2B integrations with comparative-rater carriers, agency-management systems, and telematics providers.
finops:
- name: Progressive Insurance Finops
  service_category: API
  slug: progressive-insurance-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/progressive-insurance.png
layout: provider
modified: '2026-05-23'
name: Progressive Insurance
nav: Providers
network: true
overview: Progressive Insurance publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, Auto Insurance, Property & Casualty, Telematics, and Fortune 500.
plans:
- name: Progressive Insurance Plans Pricing
  plan_count: 1
  slug: progressive-insurance-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 2
  name: Progressive Insurance Rate Limits
  slug: progressive-insurance-rate-limits
score:
  band: emerging
  composite: 16.2
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 16.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 9.1
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/progressive-insurance/refs/heads/main/screenshots/progressive-insurance-2026-06-20T192148.png
security:
- kind: domain-security
  name: Progressive Insurance Domain Security
  slug: progressive-insurance-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: progressive-insurance
tags:
- Insurance
- Auto Insurance
- Property & Casualty
- Telematics
- Fortune 500
- Personal Lines
- Commercial Insurance
website: https://www.progressive.com/
---
