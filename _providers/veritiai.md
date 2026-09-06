---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://veriti.ai/'', ''status'': 301, ''note'': ''declared website redirects to https://www.checkpoint.com/exposure-management/ — a different registrable domain (veriti.ai -> checkpoint.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://veriti.ai/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/veritiai-domain-security.yml
created: '2026-07-17'
description: Veriti Cybersecurity is a Preemptive Exposure Management (PEM) platform founded in 2021 that continuously discovers, prioritizes, and remediates vulnerabilities, misconfigurations, and exploitability risk across an organization's multi-vendor security stack, on-premises and in the cloud. Its AI-driven engine analyzes each environment's exposures, configurations, and existing protections to apply safe controls and automated (including virtual) patching without disrupting business, with integrations spanning 70+ security vendors. Originally an Insight Partners portfolio company, Veriti was acquired by Check Point (agreement announced May 2025); its capabilities are being folded into the Check Point Infinity Platform's Threat Exposure and Risk Management offering, and veriti.ai now redirects to checkpoint.com/exposure-management. Veriti is delivered as an enterprise security platform and does not publish a public self-serve developer API, OpenAPI, or developer portal; this profile
  therefore carries identity and domain-security signals only.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/veritiai.png
layout: provider
modified: '2026-07-21'
name: Veriti.ai
nav: Providers
network: true
overview: Veriti.ai is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cybersecurity, Exposure Management, Vulnerability Management, and Threat Intelligence.
random_paper: 0
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 2
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/veritiai/refs/heads/main/screenshots/veritiai-2026-09-02T165727.png
security:
- kind: domain-security
  name: Veritiai Domain Security
  slug: veritiai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: veritiai
tags:
- Company
- Cybersecurity
- Exposure Management
- Vulnerability Management
- Threat Intelligence
- Remediation
- Security Automation
website: https://veriti.ai/
---
